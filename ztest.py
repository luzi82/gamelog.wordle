import s01_guess

assert(s01_guess.get_guess_result('ABCDE','XBYEZ')=='XOX-X')
assert(s01_guess.get_guess_result('AABBB','ABABC')=='O--OX')
assert(s01_guess.get_guess_result('XXXAA','AAAAA')=='XXXOO')
assert(s01_guess.get_guess_result('XXXAA','YAAAY')=='X-XOX')
