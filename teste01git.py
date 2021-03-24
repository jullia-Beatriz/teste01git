#arquivo python teste github

animais = []
print('=-' * 20)
print("         Cadastro de animais")

while True:
    animais.append(input('Nome: '))
    animais.append(input('Especie: '))
    animais.append(input('Idade: '))
    stop = input('Deseja cadastrar mais? [s/n]')
    if stop in 'Ss':
        continue
    else:
        break

print(animais)

