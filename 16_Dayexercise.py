#Exercise level 1
#1
import datetime
now = datetime.datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
current_timestamp = now.timestamp()

print(f"Día: {current_day}, Mes: {current_month}, Año: {current_year}, Hora: {current_hour}, Minuto: {current_minute}, Timestamp: {current_timestamp}")

#2
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Fecha formateada: {formatted_date}")

#3
time_string = "12/05/2019, 14:30:00"
date_object = datetime.datetime.strptime(time_string, "%m/%d/%Y, %H:%M:%S")
print(f"Objeto datetime: {date_object}")

#4
now = datetime.datetime.now()
new_year = datetime.datetime(now.year + 1, 1, 1)
time_difference = new_year - now
print(f"Diferencia de tiempo entre ahora y el Año Nuevo: {time_difference}")

#5
epoch = datetime.datetime(1970, 1, 1)
time_difference_epoch = now - epoch
print(f"Diferencia de tiempo desde el 1 de enero de 1970: {time_difference_epoch}")

#6
import pandas as pd
import datetime
fechas = pd.date_range(start="2020-01-01", periods=10, freq="D")
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

df = pd.DataFrame({"Fecha": fechas, "Valor": datos})
print(df)


import datetime
actividad = "Usuario inició sesión"
timestamp = datetime.datetime.now()

print(f"{actividad} a las {timestamp}")


import datetime
fecha_publicacion = datetime.datetime.now()

print(f"Post publicado el: {fecha_publicacion.strftime('%d/%m/%Y, %H:%M:%S')}")
