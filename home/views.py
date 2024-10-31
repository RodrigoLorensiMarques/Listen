from django.shortcuts import render
from .utilits import Read_TotalTime

def home(request):
    Total_Time=Read_TotalTime()

    if request.method == 'POST':
        tempo = request.POST.get('input_time')
        print(tempo)

    return render(request, 'home.html', {'Total_Time': Total_Time}) #Precisa formatar