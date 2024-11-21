nome = str(input('Digite o seu nome: ')).strip()
print('Seu nome em letras maiúsculas é {}' .format(nome.upper()))
print('Seu nome em letras minúsculas é {}' .format(nome.lower()))
print('Seu nome tem {} letras' .format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0])))
#################################################################################################

nome = str(input('Digite o seu nome: ')).strip()
print(f"Seu nome em letras maiúsculas é {nome.upper()}")
print(f"Seu nome em letras minúsculas é {nome.lower()}")
print(f"Seu nome tem {len(nome)-nome.count(' ')} letras")
print(f"Seu primeiro nome tem {nome.find(' ')} letras")

separa = nome.split()
print(f"Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras")