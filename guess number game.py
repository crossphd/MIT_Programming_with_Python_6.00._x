high = 100
low = 0
guess = 50
i = ''

print "Please think of a number between 0 and 100!"
print "Is your secret number 50?"

while i != "c":
    i = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if i == "c":
        break
    elif i == "l":
        low = guess
        guess = high - (round((high - low) /2))
        print "Is your secret number", str(guess)+"?"
    elif i == "h":
        high = guess
        guess = high - (round((high - low) /2))
        print "Is your secret number", str(guess)+"?"
    else:
        print "Sorry, I did not understand your input."
        print "Is your secret number", str(guess)+"?"
        
if i == "c":
    print "Game over. Your secret number was:",str(guess)
