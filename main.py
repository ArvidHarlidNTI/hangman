import json
import re
from pathlib import Path

script_dir = Path(__file__).parent
hang_path = script_dir / 'hangman.json'

with open(hang_path, 'r', encoding='utf-8') as file:
    hangman = json.load(file)

def main():
    tword = input("P1, Please pick a word: ").strip().casefold()
    if tword.find("_") != -1:
     print("Error: Word may not contain underscores.")
     return
    hword = re.sub(r'[^ ]', '_', tword)
    tlist = list(tword)
    hlist = list(hword)
    win = 0
    print(hangman[win])
    print(hword)
    if win != 7:
        while win < 7:
          guess = input("P2, Please pick a character: ")
          if len(guess) > 1: 
            print("Error: Guess is more than one character!")
          elif len(guess) == 0:
             print("Error: Guess is empty!")
          elif tword.find(guess) == -1:
            win = win + 1
            if win == 6:
              print(hangman[win])
              print("You Lose!")
              break
            print(hangman[win])
            print("".join(hlist))
          elif len(guess) == 1:
            gindex = [i for i, char in enumerate(tword) if char == guess] 
            for i in gindex:
               hlist[i] = tlist[i]
            print(hangman[win])
            print("".join(hlist))
            if "".join(hlist).find("_") == -1:
             print("You Win!")
             break
while True:
   main()