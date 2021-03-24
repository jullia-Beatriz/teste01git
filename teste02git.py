convidados = list()
tot = 0

for pessoas in range(0,5):
    convidados.append(input('Digite nome e Sobrenome: '))
    tot += 1


print(f'Seja bem vindo(a)! {convidados}'.title())
print(f'No total foram cadastrados {tot} convidados!')
