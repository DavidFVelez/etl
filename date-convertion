import pandas as pd

dic_profesionales = { 
    'name': ['David', 'Andrea', 'Valeria'], 
    'Profesion':['Ingeniero Electrónico','Comunicadora social', 'Ingeniera de Alimentos'], 
    'Fecha': ["2022/11/06", "2022/12/06", "2023/01/06"]}

df_profesionales = pd.DataFrame(dic_profesionales)
df_prof_datetime = df_profesionales.copy()

print(df_profesionales)

serie_date = pd.to_datetime(df_profesionales['Fecha'])

months_dict = {
        '01': 'Enero', '02': 'Febrero', '03': 'Marzo', '04':'Abril', '05':'Mayo', '06':'Junio', '07':'Julio', '08':'Agosto', '09':'Septiembre', '10':'Octubre', '11':'Noviembre', '12':'Diciembre'
    }

def date_convertion(date):
    año, mes, dia = date.split('/')
    month_name = months_dict[mes]

    return month_name

def date_convertion_1(date):
    dia = str(date.day)
    mes = str(date.month)
    ann = str(date.year)
    
    if len(mes) == 1:
        mes = f'{str(0)}{mes}'
    month_name = months_dict[mes]
    return f'{dia}/{month_name}/{ann}'

df_profesionales['Fecha'] = df_profesionales['Fecha'].apply(date_convertion)
print(df_profesionales)
print('\n')
print(serie_date)

df_prof_datetime['Fecha'] = pd.to_datetime(df_prof_datetime['Fecha'])
df_prof_datetime['Fecha'] = df_prof_datetime['Fecha'].apply(date_convertion_1)
print(df_prof_datetime['Fecha'])




