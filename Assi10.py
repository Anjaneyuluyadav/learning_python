#Ass8
#Ass8

# 1) what is dictionary and write all dictionary functions with example

#dict is collection of key and value pear
# dict is douplicte are not allowed but values are allowd
# none tyoe values are allows
# dict is represends are {}
# dict[name ]={key,value}
x={"a":10,"b":20}
print(type(x))


# 2) x={'A':1,'B':'5'} o/p :{1:'A','5':'B'} interchnage the keys and values
x={'A':1,'B':'5'}
d=x.keys(sorted())
print(d)
#
# 3) x= {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ['ac','ad','bc','bd']
#
#
# 4)x='EMBEDDED' o/p : {'E':'3','M':1,'B':1,'D':3}
#
# 5) x={'A':3,'B':5,'C':4,'D':2,'E':1} Arrnage keys and vaules as per assending order of vaues
# o/p : {'E':1,'D':2,'A':3,'C':4,'B':5}
#
# 6){'A': 'Red','D':None 'B': 'Green', 'C': None} New Dictionary after dropping empty items
#
#   o/p :{'A': 'Red', 'B': 'Green'}
#
# 7) x={'A':123,'B':100} check key is exits or not in dic
# key= take key from input use eval fun
#
# 8) x='Hello PYTHON who ARE YOU'
# o/p : {'H':'HELLO','P':'PYTHON','W':'WHO','A':'ARE','Y':'YOU'}
#
# 9){'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# reverse the list values in the dictionary:
# {'C1': [30,20,10], 'C2': [40,30,20], 'C3': [34,12]}
#
# 10){1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values:
# o/p : {'red': 3, 'green': 5, 'black': 5, 'white': 5}