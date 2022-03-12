# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


## lab 1
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
