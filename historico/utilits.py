from django.db import connection

def Read_Historico():
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT *FROM historico
            """)
        
        result= cursor.fetchall()

        Historico = []
        for time, date in result:
            Date_Str = str(date).replace('-', '/')
            Date_Hist = "/".join(Date_Str.split("/")[::-1])
            Time_Hist = str(time)
            Historico.append((Date_Hist, Time_Hist))

        print (Historico)
        return Historico