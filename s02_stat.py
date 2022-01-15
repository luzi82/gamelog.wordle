import argparse
import futsu.fs
import s01_guess


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('ans_txt_list_path')
  parser.add_argument('all_txt_list_path')
  args = parser.parse_args()
  
  ans_txt_list = futsu.fs.file_to_string_list(args.ans_txt_list_path)
  all_txt_list = futsu.fs.file_to_string_list(args.all_txt_list_path)
  
  ans_txt_list = list(map(lambda i:i.upper(),ans_txt_list))
  all_txt_list = list(map(lambda i:i.upper(),all_txt_list))

  ans_txt_to_step_dict = {}
  
  dfs(ans_txt_to_step_dict, ans_txt_list, all_txt_list, 0)

  total_step = sum(ans_txt_to_step_dict.values())
  avg_step = total_step / len(ans_txt_to_step_dict)
  max_step = max(ans_txt_to_step_dict.values())
  
  print(f'AVG STEP: {avg_step}')
  print(f'MAX STEP: {max_step}')

def dfs(ans_txt_to_step_dict, ans_txt_list, all_txt_list, step):
  if len(ans_txt_list) == 1:
    print(f'{ans_txt_list[0]} = {step+1}')
    ans_txt_to_step_dict[ans_txt_list[0]] = step+1
    return
  
  score_txt_list = s01_guess.get_score_txt_list(ans_txt_list, all_txt_list)
  guess_txt = score_txt_list[0][1]
  
  gresult_to_ans_txt_list_dict = {}
  for ans_txt in ans_txt_list:
    gresult = s01_guess.get_guess_result(ans_txt, guess_txt)
    if gresult == 'OOOOO':
      print(f'{guess_txt} = {step+1}')
      ans_txt_to_step_dict[guess_txt] = step+1
      continue
    if gresult not in gresult_to_ans_txt_list_dict:
      gresult_to_ans_txt_list_dict[gresult] = []
    gresult_to_ans_txt_list_dict[gresult].append(ans_txt)

  for ans_txt_listt in gresult_to_ans_txt_list_dict.values():
    dfs(ans_txt_to_step_dict, ans_txt_listt, all_txt_list, step+1)

if __name__=='__main__':
  main()
