# faça uma programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É um número com letra', a.isalnum())
print('Está é maiusculo?', a.isupper())
print('Está em minusculo?', a.islower())
print('É caractere?', a.isascii())
print('Está capitalizada?', a.istitle())
print('É decimal?', a.isdecimal())
print('É imprimivel?', a.isprintable())
print('Tem espaço?', a.isspace())
print('É indentificado?', a.isidentifier())
print('É um digito?', a.isdigit())
