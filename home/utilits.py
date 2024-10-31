
from django.db import connection

def Read_TotalTime():
    with connection.cursor() as cursor:
        cursor.execute("SELECT SUM(TIME_TO_SEC(total_time)) FROM english")
        result = cursor.fetchone() 

        if result and result[0] is not None:
            total_seconds = result[0]
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60) 

            total_time = f"{hours}:{minutes:02}"
            print(total_time)
            return total_time 
        else:
            return "00:00:00"


def Update_TotalTime(input_time):
    with connection.cursor() as cursor:
        cursor.execute(f"""
        UPDATE english
        SET total_time = ADDTIME(total_time, '{input_time}:00')
        limit 1;
                       """)
