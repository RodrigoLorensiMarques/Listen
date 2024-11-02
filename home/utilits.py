
from datetime import datetime, timedelta
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
        
def Verify_Date_Today():
    Time_Now = datetime.now()
    Date = Time_Now.date()
    Date_Now = str(Date)
    print(f"Data de hoje: {Date_Now}")
    return Date_Now



def Insert_Date(Date_Input):
        with connection.cursor() as cursor:
            cursor.execute(f"""
            SELECT DATE_TIME FROM ENGLISH
            WHERE DATE_TIME='{Date_Input}';
                                    """) 
            Valor= cursor.fetchall()

        if not Valor:
            with connection.cursor() as cursor:   
                cursor.execute(f"""
                INSERT INTO english (date_time)
                VALUES ('{Date_Input}');                
                                                """)
                print("Data inserida na datebase.")
            
        else:
            print("Data já exite na datebase.")                


def Count_Date():
    with connection.cursor() as cursor:
        cursor.execute(
        """
        Select count(date_time)from english; 

        """)
        Valor = cursor.fetchone()
        return Valor[0]


def Verify_TimeMeta(Total_Time):
    if isinstance(Total_Time, str):
        h, m= map(int, Total_Time.split(':'))
        Total_Time = timedelta(hours=h, minutes=m,)

    Meta = timedelta(hours=100) 

    TimeMeta = Total_Time >= Meta

    print(f"Meta de 100 horas atingida? {TimeMeta}")
    return TimeMeta


def Very_MetaDays(TotalDays):
    DaysMeta = TotalDays>=100
    print(f"Meta de 100 dias atingida? {DaysMeta}")
    return DaysMeta


def Insert_historico(Input_Time,Date_Today):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""
        INSERT INTO historico (Input_Time,date_input)
        VALUES ('{Input_Time}','{Date_Today}')

            """)