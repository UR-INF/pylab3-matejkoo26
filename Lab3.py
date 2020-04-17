# fragmenty dotyczące rozwiązania poszczególnych zadań proszę oddzielić odpowiednimi komentarzami

## zadanie 2 ##
from array import *

print('Podaj ile chcesz dodać znaków do tablicy: ')
num = input()

my_array = array('u', [])

for i in range(0,int(num)):
    my_array.append(input('Podaj znak: '))

my_array.reverse()
for i in my_array:
    print(i)
    
    
## zadanie 3 ## 

from array import * 
import random

print('Podaj ile znaków wylosować do tablicy: ')
number = input()

tab = array('f',[5])
for i in range(0,int(number)):
    tab.append(random.uniform(-5,5))


plik = open("result.txt","w")
for i in tab:
    plik.write(str(i)+", ")
    
## zadanie 4 ##
