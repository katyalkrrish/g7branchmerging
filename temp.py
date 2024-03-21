import random

HANGMAN_PICS = [
    '''
       +---+
           |
           |
           |
          ===''',
    '''
       +---+
       O   |
           |
           |
          ===''',
    '''
       +---+
       O   |
       |   |
           |
          ===''',
    '''
       +---+
       O   |
      /|   |
           |
          ===''',
    '''
       +---+
       O   |
      /|\\  |
           |
          ===''',
    '''
       +---+
       O   |
      /|\\  |
      /    |
          ===''',
    '''
       +---+
       O   |
      /|\\  |
      / \\  |
          ==='''
]

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def get_random_word(word_list):
    """Returns a random word from the word list."""
    return random.choice(word_list)

def display_board(missed_letters, correct_letters, secret_word):
    """Displays the hangman ASCII art, missed letters, and secret word."""
    print(HANGMAN_PICS[len(missed_letters)])
    print('Missed letters:', ' '.join(missed_letters))
    
    # Display the secret word with underscores for unrevealed letters
    display_word = ''.join([letter if letter in correct_letters else '_' for letter in secret_word])
    print('Secret Word:', ' '.join(display_word))

def get_guess(already_guessed):
    """Gets a valid letter guess from the player."""
    while True:
        guess = input('Please guess a letter: ').lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter from the alphabet.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Try again.')
        else:
            return guess

def play_again():
    """Asks the player if they want to play again."""
    return input('Would you like to play again? (y)es or (n)o: ').lower().startswith('y')

def hangman():
    print('|_H_A_N_G_M_A_N_|')
    missed_letters = ''
    correct_letters = ''
    secret_word = get_random_word(words)
    game_is_done = False

    while True:
        display_board(missed_letters, correct_letters, secret_word)

        # Get a guess from the player
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters += guess
            # Check if the player has won
            if all(letter in correct_letters for letter in secret_word):
                print('You guessed it!')
                print('The secret word is:', secret_word)
                game_is_done = True
        else:
            missed_letters += guess

            # Check if the player has lost
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_board(missed_letters, correct_letters, secret_word)
                print('You have run out of guesses!')
                print('The secret word was:', secret_word)
                game_is_done = True

        if game_is_done:
            if play_again():
                missed_letters = ''
                correct_letters = ''
                secret_word = get_random_word(words)
                game_is_done = False
            else:
                break

hangman()
