# gamelog.wordle

A code act as player of Wordle.
Wordle pick a word everyday.
The code give word suggestion according to Wordle output.

# init
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

# generate wordlist folder
python3 s00_create_wordlist.py

# Wordle 209 TANGY
./wordle.sh

2315 > suggest
Calculating...
Suggestion:
  ROATE - 2.2125269978401727
  SOARE - 2.2315334773218143
  TEALS - 2.2336933045356373
  TASER - 2.2354211663066956
  TAELS - 2.23585313174946
# ( Put ROATE to wordle, reply XX--X )
2315 > guess roate xx--x
50 > suggest
Calculating...
Suggestion:
  TACIT - 1.66
  TAINT - 1.66
  CUNIT - 1.68
  BAVIN - 1.7
  BUIST - 1.7
# ( Put TACIT to wordle, reply OOXXX )
50 > guess tacit ooxxx
5 > suggest
Calculating...
Suggestion:
  BANAL - 1.0
  BINAL - 1.0
  BLAND - 1.0
  BLANK - 1.0
  BLAWN - 1.0
# ( Put BANAL to wordle, reply XOOXX )
5 > guess banal xooxx
1 > suggest
Calculating...
Suggestion:
  TANGY - 0.0
  AAHED - 1.0
  AALII - 1.0
  AARGH - 1.0
  AARTI - 1.0
# ( TANGY is the answer )

# interface commands
help
  Show help

exit
  Exit

reset 
  Forget current status, start new game

suggest
  Suggest guess word

list
  List possible word

check GUESS
  Check the possible output of input the GUESS word, and the size of word list afterward.

guess GUESS OX-XO
  You put GUESS to Wordle, and Wordle reply OX-XO.
  O=green -=yellow X=gray
  Ths software update the status

compare ANSWR GUESS
  Calculate the output if answer is ANSWR, and guess is GUESS.
  compare ABCDE AXXEX give OXX-X

# Extra
./wordle_stat.sh
  Calculate how good is wordle.sh
  Trying all possible answer in Wordle, and calculate number of step need to solve the puzzle.
  Output as wordle_stat.log

wordlist.src/american-english
  From http://wordlist.sourceforge.net/
  Debian package "wamerican"
  Just for reference

wordlist.src/british-english
  From http://wordlist.sourceforge.net/
  Debian package "wbritish"
  Just for reference

wordlist.src/wordle.La
  From Wordle source
  List of answer, sorted by date
  DONT READ THIS, your fun will be ruined

wordlist.src/wordle.Ta
  From Wordle source
  List of word which can be input to Wordle, but will not be answer.
  Includes TREES, PENIS.

Hard mode is NOT included in this code.
