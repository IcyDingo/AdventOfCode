import pandas as pd
import numpy as np
from striprtf.striprtf import rtf_to_text




list_stra = list(open("day_2.txt").read().splitlines())


elf_di = {"A": "Rock", "B":"Paper", "C":"Scissor"}
me_di = {"X": "Rock", "Y":"Paper", "Z":"Scissor"}

##### Part 1 
score = 0
for i in list_stra:
    elf,me = i.split()

 
    
    if me_di[me] == "Rock":
        score += 1
    if me_di[me] =="Paper":
        score += 2
    if me_di[me] == "Scissor":
        score += 3

    if me_di[me] == elf_di[elf]:
        print("Draw", i)
        score+=3
    elif (elf_di[elf], me_di[me]) in [("Rock", "Scissor"),("Paper","Rock"), ("Scissor", "Paper")]:
        print("Lost", i)
        score += 0
    else:
        print("Won", i)
        score += 6

print("Final Score Round 1", score)

##### Part 2 

elf_di = {"A": "Rock", "B":"Paper", "C":"Scissor"}

win_di = {"Rock":2, "Paper":3, "Scissor":1}
lose_di = {"Rock":3, "Paper":1, "Scissor":2}
draw_di = {"Rock":1, "Paper":2, "Scissor":3}

res_di = {"X": "Lose", "Y":"Draw", "Z":"Win"}

score_2 = 0
for i in list_stra:
    elf,me = i.split()

    if res_di[me] == "Lose":
        print("Lose")
        score_2 += lose_di[elf_di[elf]]


    elif res_di[me] == "Win":
        print("Win")
        score_2 += 6
        score_2 += win_di[elf_di[elf]]

    else:
        print("Draw")
        score_2 += 3
        score_2 += draw_di[elf_di[elf]]

print("Final Score Round 2:",score_2)

