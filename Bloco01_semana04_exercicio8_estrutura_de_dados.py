'''
Crie uma tupla com alguns elementos e remova um elemento específico.
'''

t = (1, 2, 3)

remove = 3

t_modif = tuple(x for x in t if x != remove)

print("tupla incial:", t)
print("tupla modificada", t_modif)