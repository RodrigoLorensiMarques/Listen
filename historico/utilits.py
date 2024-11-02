import locale
from django.db import connection

import locale

def Read_Historico():
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM historico
            """
        )
        
        result = cursor.fetchall()

        Historico = []
        for time_hist, date_rec, time_rec in result:
            Time_Record = f"{time_rec.hour:02}:{time_rec.minute:02}"
            Time_Hist = f"{time_hist.hour:02}:{time_hist.minute:02}"

            locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
            Extensive_Date = date_rec.strftime("%d de %B de %Y")

            Historico.append((Extensive_Date, Time_Hist, Time_Record))

        print(Historico)
        return Historico[::-1]
