# Cette fonction exécute une opération
# impossible entre un entier
# et une chaîne de caractères
def this_codes_fails():
    a = 12
    b = 'rabbit'
    return a + b

# le type d'une variable peut changer dynamiquement au cours du programme
var1 = 12
print(type(var1))
#> <class 'int'>
var1 = 'rabbit'
print(type(var1))
#> <class 'str'>

print('jusque la tout va bien')
#> jusque la tout va bien
# L'interpréteur va échouer ici en levant une exception
print(this_codes_fails())
#> TypeError: unsupported operand type(s) for +: 'int' and 'str'
