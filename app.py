import sys
print('Hello World')
print(sys.version)

# Python Indentasi : lingkup mulai baris kode 
if 5 > 2 :
    print('true')

integer = 5 # tipe data bilangan bulat
floatNum = 5.3 # tipe data bilangan desimal
string = "hello, i'm string"
print(integer)
print(floatNum)
print(string)

# Casting : tipe data spesifik
int(integer)
float(floatNum)
str(string)

# Cek tipe data 
print(type(string))

# String dapat digunakan dengan single quotes atau double quotes

# Variabel tipikal case-sensitive yang 
string = 'ardian'
String = 'hello'

# contoh diatas merupakan variabel yang berbeda, jadi tidak ada perubahan pada variabel sebelumnya

"""
 Variable Names
    A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
    A variable name cannot be any of the Python keywords.
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVARs = "John"
myvar2 = "John"

# Nama variabel bentuk Camel Case
myVariableName = 'Ardian'

# bentuk Pascal Case
MyVariableName = 'Ridho'

# bentuk Snake Case
my_variable_name = MyVariableName + ' ' + myVariableName

print(my_variable_name)

# Many values to multiple variables
orange, banana, cherry = "Orange", "Banana", "Cherry"

buah_1 = buah_2 = buah_3 = "Manis"

print(orange,buah_1, banana,buah_2, cherry,buah_3)

# Destructuring assignment : unpack collection value from list, tuple // extract values pada variabel
# biasa disebut unpacking  

buah = ['Durian', 'Mangga', 'Rambutan']
durian,mangga,rambutan = buah

# Output Variable
print(durian,mangga,rambutan)
print(durian + mangga, rambutan)

# Note : Output variabel tidak bisa berbeda tipe data misalkan integer dengan string, 
#        maka harus diubah dulu salah satunya

# Global Variable

GlobalVariable = "Aku di luar fungsi"

def cetakOutput():
    GlobalVariable = "Aku di dalam fungsi"
    return GlobalVariable


print(GlobalVariable)

GlobalVariable = "Aku di luar dan setelah fungsi"

print(cetakOutput())
print(GlobalVariable)

"""
Data types in programming dictate how data is stored and manipulated. Python has several built-in data types:

    Text Type (str): Stores text characters.
    Numeric Types:
        Integer (int): Stores whole numbers.
        Float (float): Stores decimal numbers.
        Complex: Stores complex numbers.
    Sequence Types:
        List: Stores ordered collections of items.
        Tuple: Stores ordered collections of items (immutable).
        Range: Generates a sequence of numbers.
    Mapping Type:
        Dictionary (dict): Stores key-value pairs.
    Set Types:
        Set: Stores unique items without any order.
        Frozenset: Immutable set.
    Boolean Type (bool): Stores true or false values.
    Binary Types:
        Bytes: Stores sequences of bytes.
        Bytearray: Mutable sequence of bytes.
        Memoryview: Exposes an array's interface.
    None Type (NoneType): Represents the absence of a value.

"""

text = str('Hello i"text') # you can type just 'hello i"text' it's ok too and whole under type similiar can this
integer = int(40)
floatNum = float(35.3)
complex = 3j
lists = [True, 'String', 34, 4.2, 2j]
tuples = (3,5,2, lists)
range = range(5)
maps = {'name' : 'Ardian', 
        'kelas': 'PJJ Informatika'}
frozensets = frozenset({5,3,2,1,1})
boolean = True or False
# bytes = b'Hello'
ByteArray = bytearray(3)
MemoryView = bytes((5))
none = None

print(frozensets)
print(integer)
print(floatNum)
print(complex)
print(lists)
print(tuples)
print(range)
print(maps)
print(boolean)

# Python Numbers
x = 5
y = 213432434535
z = -2134354321

print(x,y,z)

# Float
x = 1.2
y = 4.2
z = 2.3

print(x,y,z)

# Complex
x = 35e2
y = 12E4
z = -4324.123e3

import random
print(random.randrange(1,5))

# Python Casting
x = int(2.4)
x = float(x)
z = int(5)
z = str(z)

print(x)
print(z)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)

# Note: in the result, the line breaks are inserted at the same position as in the code.

# Strings are Arrays

string = "Hello World"
print(string[0])

for i in string:
    print(i)

print(len(string))

# Check String

txt = 'The best things in life are free!'
print('best' in txt)

if "things" in txt :
    print("Iya, ada 'things' di dalam variable txt")

print('best' not in txt)


# Python Lists

"""
List item are ordered, changeable, allow duplicate value
index start with as first item [0]
"""
myFruits = ['Banana', 'Apple', 'Mango']

print('Apple' in myFruits)

# inputFruit = input('Check Buah ')
# inputFruit = inputFruit.capitalize()

# if inputFruit in myFruits :
#     print('Iya ada buah', inputFruit, 'di dalam lists')
# else:
#     print('Tidak ada', inputFruit, 'di dalam list fruits')

# Access list item by index
print(myFruits[0])

# Negative index
print(myFruits[-1])

# Range of indexes
print(myFruits[1:])
print(myFruits[:1])

# List length
print(len(myFruits))

# the list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Change a Range of Item Values

myFruits[3:5] = ['Rambutan', 'Semangka']
print(myFruits)

myFruits[1:2] = ['Durian','Jeruk']
print(myFruits)

# Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

# Insert Items
myFruits.insert(3,'Kelengkeng')
print(myFruits)
