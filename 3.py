import json

with open('dados.json', 'r') as file:
    data = json.loads(file.read())


# Retorna menor valor de faturamento (desprezando os dias em que o mesmo foi 0)
min_faturamento = data[1]['valor']
min_dia = 0

for i in data:
    if i['valor'] == 0:
        pass
    else:
        if i['valor'] < min_faturamento:
            min_faturamento = i['valor']
            min_dia = i['dia']

# Retorna mairo valor de faturamento
max_faturamento = data[1]['valor']
max_dia = 0

for i in data:
    if i['valor'] > max_faturamento:
        max_faturamento = i['valor']
        max_dia = i['dia']

# Retorna a média de faturamento (desprezando os dias em que o mesmo foi 0)
soma_faturamentos = 0
numero_dias = 0

for i in data:
    if i['valor'] == 0:
        pass
    else:
        soma_faturamentos += i['valor']
        numero_dias += 1

media_faturamento = soma_faturamentos / numero_dias

# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_maiores_media = 0
for i in data:
    if i['valor'] > media_faturamento:
        dias_maiores_media += 1


print(f'''O menor faturamento foi no dia {min_dia} com o faturamento de R${min_faturamento}
O menor faturamento foi no dia {max_dia} com o faturamento de R${max_faturamento}
O Número de dias no mês em que o valor de faturamento diário foi superior à média mensal é igual a {dias_maiores_media}''')

