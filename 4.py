faturamentos = [
    {
        'estado': 'SP',
        'faturamento': 67836.43
    },
    {
        'estado': 'RJ',
        'faturamento': 36678.66
    },
    {
        'estado': 'MG',
        'faturamento': 29229.88
    },
    {
        'estado': 'ES',
        'faturamento': 27165.48
    },
    {
        'estado': 'outros',
        'faturamento': 19849.53
    }
]

total_faturamento = 0
for i in faturamentos:
    total_faturamento += i['faturamento']

for i in faturamentos:
    i['percentual'] = i['faturamento'] / total_faturamento * 100
    if i['estado'] != 'outros':
        print(f'O percentual de faturamento do estado {i["estado"]} é igual a: {"{:.2f}".format(i["percentual"])}%')
    else:
        print(f'O percentual de faturamento dos outros estados é igual a: {"{:.2f}".format(i["percentual"])}%')

