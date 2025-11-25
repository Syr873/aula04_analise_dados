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

pontos = int(input('Informe sua quantidade de pontos: '))
if pontos >= 100:
    print('Parabéns!! Você atingiu o nível máximo!!')
elif pontos >= 50:
    print('Boa pontuação! Nível médio')
elif pontos >= 25:
    print('Pontuação baixa! Nível baixo')
else:
    print('Infelizmente a pontuação não é suficiente... Nível muito baixo')
