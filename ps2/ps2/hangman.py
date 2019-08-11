# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import operator

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    assert secret_word.islower(),"secret_word has uppercase, please input lowercase again!"
    try:
        for list_element in letters_guessed:
            if list_element not in string.ascii_lowercase:
                raise Exception('letters_guessed has uppercase!')
            else:
                pass
    except:
        print("Please assure all letters are lowercase!")
    for letter in secret_word:
        if letter in letters_guessed:
            continue
        else:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    alist_secret_word=list(secret_word)
    flag_list=[False]*len(secret_word)
    for index,letter in enumerate(secret_word):
        if letter in letters_guessed:
            flag_list[index]=True
        else:
            pass
    for index,flag in enumerate(flag_list):
        if not flag:
            alist_secret_word[index]='_ '
        else:
            pass
    return "".join(alist_secret_word)
    
    

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    if letters_guessed!=[]:
        assert "".join(letters_guessed).islower(),"letters_guessed has uppercase"
    lowercase_set=set(string.ascii_lowercase)
    letters_guessed_set=set(letters_guessed)
    result_set=lowercase_set.difference(letters_guessed_set)
    result_list=list(result_set) #set is unorderd aset={'1','2','3','4','5'} "".join(aset)
    result_list.sort()
    return "".join(result_list)
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %d letters long."%len(secret_word))
    print("-------------")
    guesses=6
    warnings=3
    letters_guessed_string=''
    letters_guessed=[]
    guessed_word='_ '*len(secret_word)
    vowel_set={'a','e','i','o','u'}
    consonant_set=set(string.ascii_lowercase).difference(vowel_set)
    while guesses>0 and not is_word_guessed(secret_word,letters_guessed):
        print("You have %d guesses left."%guesses)
        print("Available letters:%s"%get_available_letters(letters_guessed))
        
        while True:
            try:
                letters_guessed_string=input("Please guess a letter:")
                letters_guessed_string=letters_guessed_string.lower() #NOT sensentive to uppercase or lowercase: just transform to lowercase uniformlly
                if letters_guessed_string in letters_guessed:
                    warnings-=1
                    raise Exception("You have already guessed this letter. You have %d warnings left."%warnings)
                if letters_guessed_string not in string.ascii_letters or len(letters_guessed_string)>1:
                    warnings-=1
                    raise Exception("Oops! That is not a valid letter. You have %d warnings left."%warnings)#只要是字符串输出，就可以用格式化的字符串输出
            except Exception as e:
                print(e) #very elegant!
                #print("Invail input, please try to input a letter again")
                if warnings==0:
                    guesses-=1
                    warnings=3 #reset warnings
            else:
                break
            
        if letters_guessed_string in secret_word:
            letters_guessed.append(letters_guessed_string)
            guessed_word=get_guessed_word(secret_word,letters_guessed)
            print("Good guess:%s"%guessed_word)
            #guesses-=1  #猜对不扣剩余次数
            if is_word_guessed(secret_word,letters_guessed):
                score=guesses*len(set(secret_word))
                print('''------------
Congratulations, you won!
Your total score for this game is: %d'''%score)
                break
            else:
                continue
        elif letters_guessed_string not in secret_word and letters_guessed_string in consonant_set:
            letters_guessed.append(letters_guessed_string)
            print("Oops! That letter is not in my word:%s"%guessed_word)
            guesses-=1
        elif letters_guessed_string not in secret_word and letters_guessed_string in vowel_set:
            letters_guessed.append(letters_guessed_string)
            print("Oops! That letter is not in my word:%s"%guessed_word)
            guesses-=2
        else:
            pass
    #print(guesses)
    if guesses<=0: #--1 or --2, so '==0' is wrong and '<=0' is right
        print('''-----------
Sorry, you ran out of guesses. The word was %s.'''%secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    assert isinstance(my_word,str),"the first function parameter 'my_word' is not a string"
    try:
        if not isinstance(other_word,str):
            raise Exception("other_word is not a string")
    except:
        print("the second function parameter 'other_word' is not a string")
    
    my_word_new=my_word.replace("_ ","*")      
    if len(my_word_new)!=len(other_word):
        return False
    else:
        match_flag_one=True
        match_flag_two=True
        for my_word_char,other_word_char in zip(my_word_new,other_word):
            if my_word_char!="*":
                match_flag_one=match_flag_one and operator.eq(my_word_char,other_word_char)
                continue
            else:
                if other_word_char not in my_word_new:
                    match_flag_two=True
                else:
                    match_flag_two=False
        match=match_flag_one and match_flag_two
        if match:
            return True
        else:
            return False
#my_word = input("my word:")
#other_word = input("other_word:")        
#print(match_with_gaps(my_word,other_word))
  

          
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result_list=[]
    for word in wordlist:
        if match_with_gaps(my_word, word):
            result_list.append(word)
        else:
            pass
    #print(result_list)
    return result_list

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %d letters long."%len(secret_word))
    print("-------------")
    guesses=6
    warnings=3
    letters_guessed_string=''
    letters_guessed=[]
    guessed_word='_ '*len(secret_word)
    vowel_set={'a','e','i','o','u'}
    consonant_set=set(string.ascii_lowercase).difference(vowel_set)
    new_ascii_letters=string.ascii_letters+"*"
    while guesses>0 and not is_word_guessed(secret_word,letters_guessed):
        print("You have %d guesses left."%guesses)
        print("Available letters:%s"%get_available_letters(letters_guessed))
        
        while True:
            try:
                letters_guessed_string=input("Please guess a letter:")
                letters_guessed_string=letters_guessed_string.lower() #NOT sensentive to uppercase or lowercase: just transform to lowercase uniformlly
                if letters_guessed_string in letters_guessed:
                    warnings-=1
                    raise Exception("You have already guessed this letter. You have %d warnings left."%warnings)
                if letters_guessed_string not in new_ascii_letters or len(letters_guessed_string)>1:
                    warnings-=1
                    raise Exception("Oops! That is not a valid letter. You have %d warnings left."%warnings)#只要是字符串输出，就可以用格式化的字符串输出
            except Exception as e:
                print(e) #very elegant!
                #print("Invail input, please try to input a letter again")
                if warnings==0:
                    guesses-=1
                    warnings=3 #reset warnings
            else:
                break
            
        if letters_guessed_string in secret_word:
            letters_guessed.append(letters_guessed_string)
            guessed_word=get_guessed_word(secret_word,letters_guessed)
            print("Good guess:%s"%guessed_word)
            #guesses-=1  #猜对不扣剩余次数
            if is_word_guessed(secret_word,letters_guessed):
                score=guesses*len(set(secret_word))
                print('''------------
Congratulations, you won!
Your total score for this game is: %d'''%score)
                break
            else:
                continue
        elif letters_guessed_string == "*":
            print(show_possible_matches(guessed_word))
            continue
        elif letters_guessed_string not in secret_word and letters_guessed_string in consonant_set:
            letters_guessed.append(letters_guessed_string)
            print("Oops! That letter is not in my word:%s"%guessed_word)
            guesses-=1
            print(show_possible_matches(guessed_word))
        elif letters_guessed_string not in secret_word and letters_guessed_string in vowel_set:
            letters_guessed.append(letters_guessed_string)
            print("Oops! That letter is not in my word:%s"%guessed_word)
            guesses-=2
            print(show_possible_matches(guessed_word))
        else:
            pass
    #print(guesses)
    if guesses<=0: #--1 or --2, so '==0' is wrong and '<=0' is right
        print('''-----------
Sorry, you ran out of guesses. The word was %s.'''%secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #print(secret_word)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    #print(secret_word)
    hangman_with_hints(secret_word)
