secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 'a', 'l', 's']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for l in secretWord:
        if l not in lettersGuessed:
            return False
        else:
            return True

print isWordGuessed('zzz',['z'])