# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


Ramka:
for i=0 to 1
    for j=0 to 1
    tab[i,j]=0
for i=2 to 197
    for j=2 to 197
    tab[i,j]=1

2c

for i=piksele/2      - i indexu od środka
for j=0              - j indexu 0
    i,j++            - i oraz j ++
    tab[i,j]=1       - wszystkie iteracje malowane na czarno

import numpy as np
array = zeros([10,10], dtype=bool)
for y in range(10):
    for x in range(5):
    array[x,y]=1
    print(array.astype(int))



50x50 siatka, zaprojektować własne inicjały, zmalaować inicjały, zapisać jako png i wstawić jako zad.dom.
2. c i d piksele powyzej przekatnej (...)


array=zeros([200,200], dtype=bool) - stworzenie macierzy 200-200
for y in range(0,200)              - kolumny od 0 do 200 to zera
    if array[x=y]=1                - jeżeli index x oraz y jest takie samo - daję czarny <przekątna>
    if array[x,y>x]=1               - jeżeli index y jest większy od index x, daję czarny
