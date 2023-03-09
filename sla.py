from datetime import datetime, timedelta
import pandas as pd

def tratar_data(data1,data2):
    #tratar as data inicial 
    if data1<data1.replace(hour=8, minute=30):#caso a data seja antes das 8:30 vamos colocar esse horario
        data1=data1.replace(hour=8, minute=30)
    if data1>data1.replace(hour=17, minute=30):#caso a data seja depois do horario comercial 17:30 vamos acrecentar um dia e colocar o horario 8:30 ja que seria o real inicio do "atenddimetno"
        data1=data1 + timedelta(days=1)
        data1=data1.replace(hour=8, minute=30)

    #tratar as data final
    if data2<data2.replace(hour=8, minute=30):#caso a data de encerramento seja menor que 8:30 vou colocar esse horario(obs: o resultado do horas_final será 0)
        data2=data2.replace(hour=8, minute=30)
    if data2>data2.replace(hour=17, minute=30):#observe que isso não é necessario, mas ainda sim eu sou quero considerar a data_final não pode passar do horario comercial(isso seria hora extra, sabe)
        data2=data2.replace(hour=17, minute=30)#obs: caso voce queira calcular a hora extra deverá implenmentar isso não é dificil faça isso dentro desse if antes de fazer o replace voce tera que criar uma nova variavel ok? não esqueça de deixar essa variavel = 0 antes do if e colocar no return
    return(data1,data2)

def sla(data1,data2):#função do SLA
    data1,data2=tratar_data(data1,data2)#tratar a data com a função: objetivo dela é colocar a data dentro do horario comercial
    datas = pd.date_range(start=data1, end=data2, freq='d').to_series()#estou pegando todas as data que tem em diferença entre a data1 e data2(isso é um range)
    horas=0
    if data1.date() == data2.date():#caso a data seja igual fazer a subtração
        horas=(data2 - data1).total_seconds() / 3600
    else:
        # Selecionar apenas as datas de segunda a sexta-feira
        data_uteis=datas[datas.dt.weekday < 5]#dentro do range que criei quero tirar todas as datas sabado e domingo usando o weekday
        if len(data_uteis)>=3:# se a quantidade de dias for maior que 2, ou seja, mais que dois dias de diferença mutiplica vezes 8 esses dias
            horas=(len(data_uteis)-2)*8
        #importante divisão precisamos calcular quantas horas gastamos no primeiro dia
        nova_data1 = data1.replace(hour=17, minute=30#fantoche para saber ate a ultima hora

        horas_inicial=( nova_data1-data1).total_seconds() / 3600
        if horas_inicial >=5:
            horas_inicial-=1#caso a hora for maior ou igual a 5 fazer - 1 pois tenho que calcular o horario do almoço, isso é relativo dependendo do seu horario comercial
        #importante divisão precisamos calcular quantas horas gastamos no ultimo dia
        nova_data2 = data2.replace(hour=8, minute=30)

        horas_final=(data2- nova_data2).total_seconds() / 3600
        if horas_final >=5:
            horas_final-=1
        horas += horas_final + horas_inicial#somamos tudo que fizemos (calcular quantas horas gastamos no ultimo dia+calcular quantas horas gastamos no primeiro dia+(quantidade de dias for maior que 2*8))
        return(horas)
