import random
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
print("Welcome to Hangman! ")
word = random.choice(words)
word = list(word)
n = len(word)
blanks = []
i = 0
while i < n:
    blanks.append("_")
    i += 1
print(hangman[0] + "         " + " ".join(blanks))
guesses_left = 6
guess_count = 0
user_guess = []
while guess_count < guesses_left:
    guess = input("Guess a letter: \n")
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                blanks[i] = guess
        print(hangman[guess_count] + "       " + " ".join(blanks))
        if "_" not in blanks:
            print("You win!")
            guess_count = guesses_left
    else:
        guess_count += 1
        print(hangman[guess_count] + "       " + " ".join(blanks))
    if guess_count == guesses_left and "_" in blanks:
        print("You lose!")
