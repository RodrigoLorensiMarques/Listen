
from django.db import connection

def Read_TotalTime():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM english") 
        TotalTime = cursor.fetchall()
        print(TotalTime)
    return TotalTime







#Criar função que recebe o iput_time e da update no banco de dados
#Essa fução deve ser criada aqui e executada na views onde vai receber o seu valor parâmetro.

