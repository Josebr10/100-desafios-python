nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print('O alundo esta1\033[1:32m PROVADO\033[m')
elif media < 5:
    print('O aluno esta\033[1:31m REPROVADO\033[m')
else:
    print('O aluno esta de\033[1:33m RECUPERACAO\033[m')

nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
media2= (nota3 + nota4 ) / 2 

if media2 >= 7:
    print(' Você está APROVADOO!')
elif media2 >=4 :
    print(' Você está de RECUPERAÇÃO')
else:
    print(' Você está REPROVADO')
