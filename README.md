# SLA_HORAS_UTEIS
DESCRIÇÃO: Esta é uma função útil que leva em consideração o horário comercial ao calcular apenas as horas úteis entre duas datas.

A função é projetada para calcular apenas as horas úteis, considerando o horário comercial das 8h30 às 17h30. Por exemplo, se a data inicial for 09/03/2023 às 15h00 e a data final for 10/03/2023 às 9h00, o resultado será 4 horas (2,5 horas no primeiro dia e 1,5 horas no segundo dia). A função também trata datas que não estejam dentro do horário comercial, pulando para o dia e horário mais adequados para o cálculo final.

Para usar a função com um DataFrame, você pode usar o seguinte código:

df.apply(lambda row: sla(row['data1'], row['data2']) if not pd.isna(row['data2']) else None, axis=1)

Observe que este código passará por todas as linhas do DataFrame. Se a data2 estiver vazia, o valor retornado será nulo. Isso pode acontecer se essa data ainda não foi adicionada por algum motivo.

Para testar a função, você pode usar o seguinte código:

sla(datetime(2020, 6, 15, 10, 8),datetime(2020, 6, 23, 12, 4))

Espero que isso ajude a esclarecer a ideia por trás da função e como ela pode ser usada.
