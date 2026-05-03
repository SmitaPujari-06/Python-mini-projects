import random
word_bank = [
    "apple", "brave", "crane", "doubt", "eagle", "flame", "grape", "house", "input", "joker",
    "knife", "lemon", "mango", "noble", "ocean", "piano", "queen", "river", "stone", "table",
    "unity", "vivid", "whale", "xenon", "youth", "zebra", "angel", "baker", "cable", "dance",
    "earth", "faith", "giant", "happy", "ideal", "jolly", "karma", "laser", "magic", "night",
    "opera", "peace", "quick", "round", "smile", "tiger", "urban", "value", "world", "yummy",
    "zesty", "adore", "blaze", "charm", "dream", "elite", "frost", "glory", "honor", "irony",
    "jaunt", "kneel", "lucky", "mirth", "novel", "olive", "pride", "quest", "risky", "shiny",
    "trend", "usage", "vapor", "witty", "yield", "zonal", "amber", "beach", "coral", "daisy",
    "ember", "flora", "gloom", "haste", "inbox", "jewel", "koala", "lunar", "medal", "nerve",
    "orbit", "polar", "quilt", "raven", "solar", "tease", "ultra", "vital", "woven", "yearn"
]
word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 10
while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessedWord))

  guess = input('Guess a letter: ').lower()

  if guess in word:
    for i in range(len(word)):
        if word[i] == guess:
            guessedWord[i] = guess
    print('Great guess!')
  else:
    attempts -= 1
    print('Wrong guess! Attempts left: ' + str(attempts))
  if '_' not in guessedWord:
    print('\nCongratulations!! You guessed the word: ' + word)
    break

if attempts == 0 and '_' in guessedWord:
  print('\nYou\'ve run out of attempts! The word was: ' + word)