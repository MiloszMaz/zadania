# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

## lab 1
def lab1():
    # Zadanie 1
    varInt = 3
    varFloat = 3.5
    varString = 'cos tam'
    varZespolone = 5+3j
    varBool = True

    print(varInt)
    print(varFloat)
    print(varString)
    print(varZespolone)
    print(varBool)

    # Zadanie 2
    # a = int( input("Podaj pierwszą liczbę") )
    # b = int( input("Podaj drugą liczbę") )
    # c = input("Podaj rodzaj działania")
    #
    # if c == '*':
    #     result = a * b
    # elif c == '-':
    #     result = a - b
    # elif c == '+':
    #     result = a + b
    # elif c == '/':
    #     result = a / b

    # print('Wynik to ' + str( result ))
    # Zadanie 5
    name = 'MIŁOSZ'
    lastname = 'MAZUREWICZ'

    result = name.capitalize() + ' ' + lastname.capitalize()

    print(result)

    # Zadanie 6
    sing = 'la la la la la'
    result = sing.count('la')
    print(result)

    # Zadanie 7
    text = 'Dowolny tekst'
    print('Druga: ' + text[1])
    print('Ostatnia: ' + text[len(text) - 1])

    # Zadanie 8
    listForSing = sing.split()

    print(listForSing)

    # Zadanie 9
    myString = 'cos tam'
    myFloat = 3.42
    myHex = 0xffff

    print(type(myString))
    print(type(myFloat))
    print(type(myHex))

def lab2():
    ## lab 2
    # Zadanie 1
    myList = ['Piłka nożna', 'Koszykówka']

    myList.reverse()

    myList.append('Siatkówka')

    print(myList)

    # Zadanie 2
    myShorts = {
        'n': 'next',
        'p': 'previous'
    }

    print(myShorts)

    # Zadanie 3
    myGames = {
        'cs': 'Counter Strike',
        'mc': 'Minecraft',
        'cod': 'Call of Duty'
    }

    print(len(myGames))

    # Zadanie 4
    # myText = input('Podaj tekst ')
    #
    # print(myText.count('a'))


    # Zadanie 6
    a = int( input('Podaj a ') )
    b = int( input('Podaj b ') )
    c = int( input('Podaj c ') )

    if a > b:
        if a > c:
            print('a ' + a)
        else:
            print('c ' + c)
    elif b > a:
        if b > c:
            print('a ' + a)
        else:
            print('c ' + c)

    # Zadanie 7
    myListForX = [
        2,
        3.3,
        4,
        6.5
    ]

    for x in myListForX:
        print('x*x ' + x*x)

    # Zadanie 8
    i = 0
    myWhileList = []
    while i < 10:
        a = input('Podaj liczbę')
        myWhileList.append(int(a))
        i += 1

    myEndWhileList = []

    for x in myWhileList:
        if x % 2 == 0:
            myEndWhileList.append(x)

    print(myEndWhileList)

    # Zadanie 9
    x = int( input('Podaj liczbę') )
    if(x < 0):
        print('Błąd')
    else:
        print( sqrt( x ) )

## lab 3
def lab3():
    # Zadanie 1
    print("Zadanie 1")

    lista = [a-1 for a in range(1, 11)]
    print(lista)

    listaB = [pow(4, a) for a in range(0, 8)]
    print(listaB)

    listaC = [a for a in listaB if(a%2 == 0)]
    print(listaC)

    # Zadanie 2
    print("Zadanie 2")
    lista1 = [random.randrange(10) for a in range(10)]
    lista2 = [a for a in lista1 if a%2 == 0]
    print(lista2)

    # Zadanie 3
    print("Zadanie 3")
    products = {
        'Chipsy': 'kg',
        'Chleb': 'sztuki',
        'Cola': 'sztuki',
        'Jogurt': 'sztuki'
    }
    new_products = {k: v for k,v in products.items() if v == 'sztuki'}
    print(new_products)

    # Zadanie 4
    print("Zadanie 4")
    def rectangular(a, b, c):
        isRec = False
        if(a > b and a > c):
            if(pow(b, 2) + pow(c, 2) == pow(a, 2)):
                isRec = True
        elif((a > b & a < c) or (a < b & b < c) ):
            if(pow(b, 2) + pow(a, 2) == pow(c, 2)):
                isRec = True
        elif(a < b &  b > c):
            if(pow(c, 2) + pow(a, 2) == pow(b, 2)):
                isRec = True

        print("Trójkąt " + str(a) + " " + str(b) + " " + str(c) + " czy jest prostokątny? " + str(isRec))

    rectangular(random.randrange(10), random.randrange(10), random.randrange(10))

    # Zadanie 5
    print("Zadanie 5")

    def trapeze(a, b, h):
        area = (a+b)*h/2
        print(area)

    trapeze(random.randrange(10), random.randrange(10), random.randrange(10))

    # Zadanie 6
    print("Zadanie 6")

    def ratio(a, b, ile):
        out = a
        i = 1
        while i < ile:
            out = out * b
            i = i+1

        print(out)

    ratio(1, 4, 10)

    # Zadanie 8
    print("Zadanie 8")

    ship = {
        'Sok': 32,
        'Chleb': 3,
        'Ser': 4,
        'Piwo': 2,
        'Baton': 4
    }

    totalShip = 0
    def shipping(key, value, totalShip):
        totalShip = totalShip + value

        return totalShip

    for key, value in ship.items():
        totalShip = shipping(key,value, totalShip)

    print(totalShip)

    # Zadanie 10
    print("Zadanie 10")

    file = open('plik', 'w+')

    for x in range(0, 100):
        num = x//4
        print(num)
        if(type(x//4) == 'int'):
            print(x)
        #file.write()

    file.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lab3()