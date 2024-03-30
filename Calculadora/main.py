nome = input('Qual o seu nome?')

print(f'Ola Sr(a) {nome}, seja bem vindo(a) a calculadora de juros compostos!')

montante_inicial = int(input('Qual o valor que você tem para iniciar o investimento? '))
tempo_desejado = int(input('Quantos meses você deixará o dinheiro investindo ? '))
taxa = float(input('Informe em numeros decimais, o valor da taxa mensalmente para o retorno do seu investimento? ').replace(',', '.'))
aporte = int(input('Quanto tempo você consegue aportar por mês: '))
salario_desejado = int(input('Digte o salário que voce quer receber quando se aposentar: '))

tempo_decorrido = 0
while tempo_decorrido < tempo_desejado:
  if tempo_decorrido == 0:
    montante_final = round(montante_inicial * (1 + taxa) ** 1, 2)
    tempo_decorrido = tempo_decorrido + 1
    
  else:
    montante_final = round((montante_final + aporte) * (1 + taxa) ** 1, 2)
    tempo_decorrido = tempo_decorrido + 1

print(f'Aguarde ... ')
print(f'Parabens, Sr(a) {nome}! Ao final do período, o Sr(a) tera o retorno de {montante_final}') 

salario_mensal = (montante_final * taxa)
salario_mensal = round(salario_mensal, 2)

if salario_mensal >= salario_desejado:
  print(f'Parabéns, voce pode se aposentar! Seu salário mensal com esse montate sera de R$ {salario_mensal}')
elif salario_mensal < salario_desejado:
  print(f'Infelizmente se aponsentar não será possivel. Com esse montate mensal é de R$ {salario_mensal}')