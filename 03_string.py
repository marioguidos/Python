my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string+" "+ my_other_string)

my_new_string= "estes es un string \ncon salto de linea"
print(my_new_string)

my_tab_string= "\testes es un string con salto de linea"
print(my_tab_string)

my_scape_string= "\t estes es un string con salto de linea \n escapado"
print(my_scape_string)

#formateo

name, apellido,edad="marioo","guidos",23

print("mi nombre es {} {}  y mi edad es {}".format(name,apellido,edad) )
print("mi nombre es %s %s  y mi edad es %d" %(name,apellido,edad))
print(f"mi nombre es {name} {apellido} y mi edad es {edad}")

#Desempaquetado de caracteres
language= "python"
a,b,c,d,e,f  = language
print(a)
print(b)

#División

language_slice= language[1:3]
print(language_slice)


language_slice= language[1:]
print(language_slice)


language_slice= language[-2]
print(language_slice)

language_slice= language[0:6:2]
print(language_slice)
#reverse

reversed_language=language[::-1]
print(reversed_language)

#Funciones 

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))