print('\033[4;30;44m Olá, Mundo!\033[m')

#########################################################################

a = 1
b = 2
print(f'Os valores são:\033[31m {a}\033[m e\033[33m {b}\033[m')

#########################################################################

nome = 'amogusඞ'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7m'}

print('Olá! Prazer em te conhecer, {}{}{}!!!' .format(cores['pretoebranco'], nome, cores['limpa']))
