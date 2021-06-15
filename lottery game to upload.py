# generate a three-digit lottery number and have the user guess, then compare the guess to the lottery number
# alerts user of prizes based on if the digits match or not

import random

# generate a lottery number
lottery = random.randint(0, 999)

# ask the user for a guess
guess = eval(input('Enter your lottery pick (THREE digits - integers only): ')) 

# get digits from lottery
lotteryDigit1 = lottery // 100
lotteryDigit2 = (lottery % 100) // 10
lotteryDigit3 = lottery % 10

# get digits from the guess
guessDigit1 = guess // 100
guessDigit2 = (guess % 100) // 10
guessDigit3 = guess % 10

# if statement
if lottery == guess:
    print('Holy whoa! This is an exact match; you win $10,000!')
elif (lotteryDigit1 == guessDigit1 or lotteryDigit1 == guessDigit2 or lotteryDigit1 == guessDigit3) \
    and (lotteryDigit2 == guessDigit1 or lotteryDigit2 == guessDigit2 or lotteryDigit2 == guessDigit3) \
    and (lotteryDigit3 == guessDigit1 or lotteryDigit3 == guessDigit2 or lotteryDigit3 == guessDigit3):
    print('All the numbers in your guess matches, just not in the correct order. Your award is $3,000!')
elif lotteryDigit1 == guessDigit1 or lotteryDigit1 == guessDigit2 or lotteryDigit1 == guessDigit3 or \
    lotteryDigit2 == guessDigit1 or lotteryDigit2 == guessDigit2 or lotteryDigit2 == guessDigit3 or \
    lotteryDigit3 == guessDigit1 or lotteryDigit3 == guessDigit2 or lotteryDigit3 == guessDigit3:
    print('You got something! Since one of the digits matches, you win $1,000!')
else:
    print('Sorry, no match. You do not win anything.')
