import random

high = 10
ans = random.randrange(high)
guess = raw_input('Guess %d: ' %high)
while(int(guess) != ans):
    if(int(guess) < ans):
        print "Answer Higher"
    else:
        print 'Answer is lower'
    guess = raw_input('Guess %d: ' %high)
raw_input('You win')
