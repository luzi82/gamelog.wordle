import futsu.fs
import futsu.json
import os.path
import string

def is_all_letter(txt):
  return all(map(lambda i:i in string.ascii_letters, txt))

def process_wordlist(in_fn,out_fn):
  txt_list = futsu.fs.file_to_string_list(in_fn)
  txt_list = filter(lambda i:len(i)==5,txt_list)
  txt_list = filter(is_all_letter,txt_list)
  txt_list = map(lambda i:i.lower(),txt_list)
  txt_list = set(txt_list)
  txt_list = sorted(txt_list)
  futsu.fs.string_list_to_file(out_fn, txt_list)

futsu.fs.reset_dir('wordlist')

process_wordlist(os.path.join('wordlist.src','american-english'),os.path.join('wordlist','american-english'))
process_wordlist(os.path.join('wordlist.src','british-english'),os.path.join('wordlist','british-english'))

wordlela_txt_list = futsu.json.path_to_data(os.path.join('wordlist.src','wordle.La'))
wordleta_txt_list = futsu.json.path_to_data(os.path.join('wordlist.src','wordle.Ta'))

wordle_ans_txt_list = sorted(set(wordlela_txt_list))
wordle_all_txt_list = sorted(set(wordlela_txt_list+wordleta_txt_list))

futsu.fs.string_list_to_file(os.path.join('wordlist','wordle_ans_list'), wordle_ans_txt_list)
futsu.fs.string_list_to_file(os.path.join('wordlist','wordle_all_list'), wordle_all_txt_list)
