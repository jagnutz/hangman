import random
import re

print('H A N G M A N')


def hangman():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    right_word = random.choice(word_list)
    hint = list('-' * len(right_word))
    s = set()
    life = 8
    while life > 0:

        hint_update = ''.join(hint)
        print(f'\n{hint_update}')

        if '-' not in hint:
            print(f'You guessed the word {right_word}!')
            print('You survived!')
            break

        else:

            while True:
                guess = input('Input a letter: ')
                if len(guess) == 1:
                    pattern = '[a-z]'
                    charMatch = re.match(pattern, guess)
                    if charMatch:
                        break
                    else:
                        print('It is not an ASCII lowercase letter\n')
                        print(f'\n{hint_update}')
                else:
                    print('You should print a single letter\n')
                    print(f'\n{hint_update}')

            if guess in right_word:
                if guess in hint:
                    print('You already typed this letter')
                else:
                    for letter in range(len(right_word)):
                        if right_word[letter] == guess:
                            hint[letter] = guess
            else:
                if guess not in s:
                    print('No such letter in the word')
                    life -= 1
                    s.add(guess)
                else:
                    print('You already typed this letter')
    else:
        print('You are hanged!')


while True:
    option = input('Type "play" to play the game, "exit" to quit: ')
    if option == 'play':
        hangman()
    if option == 'exit':
        break
