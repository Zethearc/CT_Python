# Python Intermedio

'''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

# PEP 8

'https://peps.python.org/pep-0008/'

# Listas y diccionarios anidados

def run():
    my_list = [1, 'Hello', 4.5]
    my_dict = {'firstname': "Facundo", 'lastname': "Garcia"}

    super_list = [{'firstname': "Facundo", 'lastname': "Garcia"},
                  {'firstname': "Miguel", 'lastname': "Torres"},
                  {'firstname': "Pepe", 'lastname': "Rodelo"},
                  {'firstname': "Susana", 'lastname': "Martinez"},
                  {'firstname': "Jose", 'lastname': "Garcia"}
    ]
    
    super_dict = {"natural_nums": [1,2,3,4,5],
                  "integer_nums": [-1,-2,0,1,2],
                  "floating_nums": [1.1,4.5, 6.43]
    }
    
    for key,value in super_dict.items():
        print(key, '->', value)
if __name__=='__main__':
    run()
    
# List comprehensions

def run():
    squares = []
    for i in range(1, 101):
        squares.append(i**2)
    print(squares)
    
    #Ahora si no es divisible para 3 guardamos los cuadrados
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    # print(squares)
    
    #Este concepto se puede resumir en una linea de codigo
    # squares = [i**2 for i in range (1, 101) if i % 3 != 0]
    # print(squares)
    
    '[element for element in iterable if condition]'

if __name__=='__main__':
    run()
    
# Diictionary comprenhensions

def run():
    my_dict = {}
    
    for i in range (1, 101):
        my_dict[i] = i**3
    print(my_dict)
    
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3
    # print(my_dict)

    # my_dict = {i: i**3 for i in range(i,101) if i % 3 != 0}    
    # print(my_dict)
    
    '{key:value for value in iterable if condition}'

if __name__=='__main__':
    run()
    