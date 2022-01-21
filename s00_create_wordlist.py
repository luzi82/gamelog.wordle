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
  txt_list = map(lambda i:i.upper(),txt_list)
  txt_list = set(txt_list)
  txt_list = sorted(txt_list)
  futsu.fs.string_list_to_file(out_fn, txt_list)

futsu.fs.reset_dir('wordlist')

process_wordlist(os.path.join('wordlist.src','american-english'),os.path.join('wordlist','american-english'))
process_wordlist(os.path.join('wordlist.src','british-english'),os.path.join('wordlist','british-english'))

wordlela_txt_list = futsu.json.path_to_data(os.path.join('wordlist.src','wordle.La'))
wordleta_txt_list = futsu.json.path_to_data(os.path.join('wordlist.src','wordle.Ta'))

wordlela_txt_list = list(map(lambda i:i.upper(), wordlela_txt_list))
wordleta_txt_list = list(map(lambda i:i.upper(), wordleta_txt_list))

wordle_ans_txt_list = sorted(set(wordlela_txt_list))
wordle_all_txt_list = sorted(set(wordlela_txt_list+wordleta_txt_list))

futsu.fs.string_list_to_file(os.path.join('wordlist','wordle_ans_txt_list'), wordle_ans_txt_list)
futsu.fs.string_list_to_file(os.path.join('wordlist','wordle_all_txt_list'), wordle_all_txt_list)

jndlela_txt_list = futsu.json.path_to_data(os.path.join('wordlist.src','jndle.La'))
jndleta_txt_list = futsu.json.path_to_data(os.path.join('wordlist.src','jndle.Ta'))

JNDLE_CHAR_DICT = {
  '日':'A',
  '月':'B',
  '金':'C',
  '木':'D',
  '水':'E',
  '火':'F',
  '土':'G',
  '竹':'H',
  '戈':'I',
  '十':'J',
  '大':'K',
  '中':'L',
  '一':'M',
  '弓':'N',
  '人':'O',
  '心':'P',
  '手':'Q',
  '口':'R',
  '尸':'S',
  '廿':'T',
  '山':'U',
  '女':'V',
  '田':'W',
  '卜':'Y',
  '難':'Z',
}

def jndle_word_conv(txt):
  return ''.join(map(lambda i:JNDLE_CHAR_DICT[i],txt))


jndlela_txt_list = map(jndle_word_conv,jndlela_txt_list)
jndleta_txt_list = map(jndle_word_conv,jndleta_txt_list)
jndlela_txt_list = map(lambda i:i.upper(), jndlela_txt_list)
jndleta_txt_list = map(lambda i:i.upper(), jndleta_txt_list)

jndlela_txt_list = list(jndlela_txt_list)
jndleta_txt_list = list(jndleta_txt_list)

jndlela_txt_list = sorted(set(jndlela_txt_list))
jndleta_txt_list = sorted(set(jndleta_txt_list))

futsu.fs.string_list_to_file(os.path.join('wordlist','jndle_ans_txt_list'), jndlela_txt_list)
futsu.fs.string_list_to_file(os.path.join('wordlist','jndle_all_txt_list'), jndleta_txt_list)
