import pandas as pd 
import numpy as np




list_elf = list(open("day_1_1.txt", "r"))
elf_dict = {}
num_elf = 0
a=0
for i in list_elf:
    if i == "\n":
        num_elf += 1
        a=0
    else:
        a += int(i)
        elf_dict[num_elf] = a
         



print(max(elf_dict.values()))

#print(pd.DataFrame(elf_dict))
