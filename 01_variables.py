#Variables

my_variable= "My String Variable"
print(my_variable)

numero=5
print(numero)

my_int_to_str=str(numero)
print(my_int_to_str)
print(type(my_int_to_str))

my_bool =True
print(my_bool)

#concatenacion de variables en un print 
print(my_variable,my_int_to_str,my_bool)
print('este es el valor de :', my_bool)

#Algunas funcion del sistema
print(len(my_int_to_str))

#variables en una sola linea
name,surname,alias,age="brais","moure","mouredev",35
print("Me llamo: ",name,surname,". Mi edad es: ",age,". Y mi alias es:",alias)

"""
name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
"""

#cambiamos su tipo
name=35
age="brias"
print(name)
print(age)


#forzamos el tipo
address :str="Mi direccion"
address =32
print(type(address))