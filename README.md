# SLA_HORAS_UTEIS
DESCRIÇÃO: Essa é a melhor função que conheço que leva em consideração o horario comercial dentro do calculo

Essa função tem o objetivo de calcular apenas as horas uteis importante levar em consideração que uma data incial = 09/03/2023 15:00 e uma data final 10/03/2023 9:00 o resultado será(com horario comercial das 8:30 as 17:30) igual a 2.5 + 1.5 = 4
A função trata a data para que caso a data inicial seja fora do horario comercial pule para o horario e dia mais ideal para o calculo final.


para usar a função com um DataFrame faça isso:

df.apply(lambda row: sla(row['data1'], row['data2']) if not pd.isna(row['data2']) else None, axis=1)# isso passará por todas as linhas caso a data2 seja vaziou estou retornando null com o objetivo de caso voce esteja tentando ver um dataFrame com a data2 vazia pode acontecer caso ainda essa data não foi adicioanda por algum motivo

