import datetime

fecha_de_hoy=datetime.datetime.now()
print("la fecha de hoy es ",fecha_de_hoy)

fecha_personalizada=datetime.datetime(2025,11,13,8,30)
print("fecha personalizada es : ",fecha_personalizada.strftime("%d/%m/%y %H:%M"))