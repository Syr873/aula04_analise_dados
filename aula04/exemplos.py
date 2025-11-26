#Verifica maior idade
# idade = int(input('Digite sua idade:'))
# if idade < 18:
#     print('Você é menor de idade!')
#     print('Acesso negado!')
# else:
#     print('Você é maior de idade!')
#     print('Bem-vindo!')

#Teste mais condiçoes
#Teste de pontos

# pontos = int(input('Informe sua quantidade de pontos: '))
# if pontos >= 100:
#     print('Parabéns!! Você atingiu o nível máximo!!')
# elif pontos >= 50:
#     print('Boa pontuação! Nível médio')
# elif pontos >= 25:
#     print('Pontuação baixa! Nível baixo')
# else:
#     print('Infelizmente a pontuação não é suficiente... Nível muito baixo')

#Verificação de login
# usuario = input('Informe o usuario: ').lower()
# senha = input('Digite a senha: ')
# print(usuario)
# if usuario == 'admin' and senha == '1234':
#     print('Bem-vindo!')
# else:
#     print('Ops! Usuario ou senha incorretos!')

#Condição para brinde
# compra = float(input('Valor da compra: '))
# cliente_frequente = input('Cliente frequente? [S/N]: ').lower()
# if compra >= 1000 or cliente_frequente == 's':
#     print('Tem direito ao brinde!')
# else:
#     print('Não tem direito ao brinde!')

#Aprovação nota e frequência
nota = float(input('Informe a nota: '))
frequencia = float(input('Informe a frequencia: '))
if nota >= 7:
    if frequencia >= 75:
        print('Aprovado!')
    else:
        print('Reprovado!Boa nota porém baixa frequência...')
else:
    print('Reprovado! Nota baixa...')