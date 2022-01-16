# gamelog.wordle

A code act as player of Wordle.
Wordle pick a word everyday.
The code give word suggestion according to Wordle output.
Hard mode NOT included.

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
  ROATE - 3.2125269978401727
  SOARE - 3.2315334773218143
  TEALS - 3.2336933045356373
  TASER - 3.2354211663066956
  TAELS - 3.23585313174946
# ( Put ROATE to wordle, reply XX--X )
2315 > guess roate xx--x
50 > suggest
Calculating...
Suggestion:
  TACIT - 2.66
  TAINT - 2.66
  CUNIT - 2.68
  BAVIN - 2.7
  BUIST - 2.7
# ( Put TACIT to wordle, reply OOXXX )
50 > guess tacit ooxxx
5 > suggest
Calculating...
Suggestion:
  BANAL - 2.0
  BINAL - 2.0
  BLAND - 2.0
  BLANK - 2.0
  BLAWN - 2.0
# ( Put BANAL to wordle, reply XOOXX )
5 > guess banal xooxx
1 > suggest
Calculating...
Suggestion:
  TANGY - 1.0
  AAHED - 2.0
  AALII - 2.0
  AARGH - 2.0
  AARTI - 2.0
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
