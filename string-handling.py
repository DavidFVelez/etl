import pandas as pd

text_licenses="""Ju*anPér*ez;juan.pere*z@gm*ail.com;+346001*23456;CalleF*alsa123,Madrid,Es*paña*;29\nMaría*Lopez;mar*ia.lopez@ho*tmail.com;+346779*87654;Av*enidaSiempreViva742,B*arcelona,España;34;\nCar*los-Sánche*z;carlos.san*chez**@yahoo.com;+3464532198*7;PlazaM*ayor1,Sev*illa,Es*paña;41;
Ana.M*artínez;a*na.martine*z@outlo*ok.com;600-1*23-456;GranVía23,Madrid,España;27;
"""
text_licenses= text_licenses.replace('*','')
list_datos = text_licenses.split('\n')

data = []
list_var = ['name', 'email', 'phone', 'address', 'years']

# Way 1
for row in list_datos:
    sep_data = row.split(';')
    zip_data = dict(zip(list_var,sep_data))
    data.append(zip_data)

df_data = pd.DataFrame(data)
print(df_data)

# Way 2
list_datos = map(lambda item: item.split(';'), list_datos)
list_zip = map(lambda row: dict(zip(list_var, row)), list_datos)
zip_df = pd.DataFrame(list_zip)
print(zip_df)
