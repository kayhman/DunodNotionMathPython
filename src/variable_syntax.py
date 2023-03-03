# Le nom de cette variable n'est pas valide
3_not_possible = 6
#> SyntaxError: invalid decimal literal

# Ces deux variables sont bien distinctes,
# en raison de la casse (majuscule/minuscule) qui n'est pas la même
variable_1 = 1
vAriable_1 = 2

print(variable_1)
# > 1
print(vAriable_1)
# > 2

# Le nom de cette fonction n'est pas valide non plus
def 3_not_possible_function():
    return 3
