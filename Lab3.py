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
import numpy as numpy

def funkcja():
    tablica = numpy.array([[2,3,4,5,6],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    i = 1

    while i<5:
        for j in range (5):
            tablica[i][j] = pow(tablica[i-1][j],2)
        i += 1
    return tablica

print(funkcja())    

## zadanie 6 ##
import random


def deck():
    talia = []
    rangi = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    kolory = ['c', 'd', 'h', 's']
    for i in rangi:
        for l in kolory:
            talia.append((i, l))
    return talia


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def deal(deck, n):
    stolik = []
    for i in range(0, n):
        stolik.append(random.sample(deck, 5))
    return stolik


talia = deck()
potasowanaTalia = shuffle_deck(talia)
print('Podaj ilość graczy przy stole: ')
l_graczy = int(input())
rozdanie_dla_graczy = deal(potasowanaTalia,l_graczy )
print(rozdanie_dla_graczy)
