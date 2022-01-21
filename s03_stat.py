import argparse
import futsu.fs
import s01_guess


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('ans_txt_list_path')
  args = parser.parse_args()
  
  ans_txt_list = futsu.fs.file_to_string_list(args.ans_txt_list_path)
  
  ans_txt_list = list(map(lambda i:i.upper(),ans_txt_list))

  char_to_cnt_dict = {}

  for ans_txt in ans_txt_list:
    for ans_char in ans_txt:
      char_to_cnt_dict[ans_char] = char_to_cnt_dict.get(ans_char,0)+1

  cnt_char_tuple_list = []
  for c, cnt in char_to_cnt_dict.items():
    cnt_char_tuple_list.append((cnt,c))

  cnt_char_tuple_list = sorted(cnt_char_tuple_list)
  for cnt_char in reversed(cnt_char_tuple_list):
    cnt, c = cnt_char
    print(f'{cnt:5} {c}')

if __name__=='__main__':
  main()
