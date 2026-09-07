alunos = []
medias = []

print('===== SISTEMA DE NOTAS =====')

while True:
    aluno = input('Digite o nome do aluno(a): ')
    alunos.append(aluno)

    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))


    media = (nota1 + nota2) / 2
    medias.append(media)

    if media >= 6.0:
            print(f'Aluno(a): {aluno}\nSituação: APROVADO')
    elif media >= 3:
            print(f'Aluno(a): {aluno}\nSituação: RECUPERAÇÃO')
    else:
        print(f'Aluno(a): {aluno}\nSituação: REPROVADO')

    continuar = input('Deseja continuar com o programa? s/n: ').lower()

    if continuar == 'n' or continuar =='nao':
        print('Você optou por não continuar.')
        resultados = input('Deseja visualizar todos os resultados? s/n: ').lower()
        if resultados == 's' or resultados == 'sim':
                for aluno, media in zip(alunos, medias):
                 print(f'Aluno(a): {aluno} | Média: {media}')


              



