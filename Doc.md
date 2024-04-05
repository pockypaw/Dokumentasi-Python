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
