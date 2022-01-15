import argparse
import copy
import futsu.fs
import math
import multiprocessing
import os.path
import re

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('ans_txt_list_path')
  parser.add_argument('all_txt_list_path')
  args = parser.parse_args()
  
  ans_txt_list = futsu.fs.file_to_string_list(args.ans_txt_list_path)
  all_txt_list = futsu.fs.file_to_string_list(args.all_txt_list_path)
  
  ans_txt_list = list(map(lambda i:i.upper(),ans_txt_list))
  all_txt_list = list(map(lambda i:i.upper(),all_txt_list))

  while True:
    tmp = guess_game(ans_txt_list,all_txt_list)
    if tmp == 'EXIT': return

def guess_game(ans_txt_list,all_txt_list): # return: 'RESET', 'EXIT'
  game_ans_txt_list = copy.copy(ans_txt_list)
  while True:
    game_ans_txt_list_len = len(game_ans_txt_list)
    input_txt = input(f'{game_ans_txt_list_len} > ')

    if input_txt == '': continue

    if input_txt == 'help':
      print('O=green -=yellow X=gray')
      print('exit')
      print('reset')
      print('suggest')
      print('list')
      print('check GUESS')
      print('guess GUESS OX-XO')
      print('compare ANSWR GUESS')
      continue

    if input_txt == 'reset': return 'RESET'

    if input_txt == 'exit': return 'EXIT'

    if input_txt == 'suggest':
      print('Calculating...')
      score_txt_list = get_score_txt_list(game_ans_txt_list, all_txt_list)
      print('Suggestion:')
      for score_txt in score_txt_list[:5]:
        score,txt = score_txt
        print(f'  {txt} - {score}')
      continue

    if input_txt == 'list':
      for game_ans_txt in game_ans_txt_list:
        print(f'? {game_ans_txt}')
      continue

    m = re.fullmatch('check ([a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z])', input_txt)
    if m is not None:
      key = m.group(1).upper()
      gresult_to_cnt_dict = get_gresult_to_cnt_dict(key, game_ans_txt_list)
      for gresult in sorted(gresult_to_cnt_dict.keys()):
        cnt = gresult_to_cnt_dict[gresult]
        print(f'    {gresult} = {cnt}')
      score = gresult_to_cnt_dict__to__score(gresult_to_cnt_dict)
      print(f'  score = {score}')
      continue

    m = re.fullmatch('guess ([a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]) ([oxOX\\-][oxOX\\-][oxOX\\-][oxOX\\-][oxOX\\-])', input_txt)
    if m is not None:
      guess_txt = m.group(1).upper()
      gresult_txt = m.group(2).upper()
      game_ans_txt_list = filter_game_ans_txt_list(game_ans_txt_list, guess_txt, gresult_txt)
      continue

    m = re.fullmatch('compare ([a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]) ([a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z])', input_txt)
    if m is not None:
      ans_txt = m.group(1).upper()
      guess_txt = m.group(2).upper()
      gresult = get_guess_result(ans_txt, guess_txt)
      print(f'  {gresult}')
      continue

    print('Input ERROR')

def get_score_txt_list(game_ans_txt_list, all_txt_list):
  score_txt_list = None
  with multiprocessing.Pool(processes=multiprocessing.cpu_count()*3//2) as pool:
    score_txt_list = pool.map(get_score_txt, map(lambda i:(i,game_ans_txt_list),all_txt_list))
  score_txt_list = sorted(score_txt_list)
  return score_txt_list

def get_score_txt(txt__game_ans_txt_list):
  txt,game_ans_txt_list=txt__game_ans_txt_list
  return (get_score(txt, game_ans_txt_list),txt)

def get_score(txt, game_ans_txt_list):
  ret = _get_score(txt, game_ans_txt_list)
  # print(f'get_score({txt}, {len(game_ans_txt_list)}) > {ret}')
  return ret

def _get_score(txt, game_ans_txt_list):
  gresult_to_cnt_dict = get_gresult_to_cnt_dict(txt, game_ans_txt_list)

  return gresult_to_cnt_dict__to__score(gresult_to_cnt_dict)

def gresult_to_cnt_dict__to__score(gresult_to_cnt_dict):
  score_sum = 0
  cnt_sum = 0
  for gresult,cnt in gresult_to_cnt_dict.items():
    cnt_sum += cnt
    if gresult=='OOOOO': continue
    score_sum += cnt_to_score(cnt)

  return score_sum / cnt_sum

LOG_BASE = (3**5)/math.e
def cnt_to_score(cnt):
  return cnt * math.ceil(1+math.log(cnt,LOG_BASE))

def get_gresult_to_cnt_dict(txt, game_ans_txt_list):
  gresult_to_cnt_dict = {}
  for game_ans_txt in game_ans_txt_list:
    gresult = get_guess_result(game_ans_txt, txt)
    gresult_to_cnt_dict[gresult] = gresult_to_cnt_dict.get(gresult,0)+1
  return gresult_to_cnt_dict

def get_guess_result(ans_txt, guess_txt): # 'X-O'
  assert(len(ans_txt)==len(guess_txt))

  ret_list = ['X'] * len(ans_txt)
  
  unused_ans_char_list = []
  for i in range(len(ret_list)):
    if ans_txt[i] == guess_txt[i]:
      ret_list[i] = 'O'
    else:
      unused_ans_char_list.append(ans_txt[i])
  
  for i in range(len(ret_list)):
    if ret_list[i] != 'X': continue
    if guess_txt[i] in unused_ans_char_list:
      ret_list[i] = '-'
      unused_ans_char_list.remove(guess_txt[i])
  
  return ''.join(ret_list)

def filter_game_ans_txt_list(game_ans_txt_list, guess_txt, guess_result_txt):
  game_ans_txt_list = filter(lambda i:get_guess_result(i, guess_txt)==guess_result_txt, game_ans_txt_list)
  game_ans_txt_list = list(game_ans_txt_list)
  return game_ans_txt_list

if __name__=='__main__':
  main()
