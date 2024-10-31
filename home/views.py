from django.shortcuts import render,redirect
from .utilits import Read_TotalTime, Update_TotalTime, Verify_Date, Insert_Date

def home(request):
    Total_Time=Read_TotalTime()

    if request.method == 'POST':
        tempo = request.POST.get('input_time')
        print(tempo)

        Update_TotalTime(tempo)

        Date_Today = Verify_Date()
        Insert_Date(Date_Today)

        Total_Time=Read_TotalTime()
        return redirect('home')

    return render(request, 'home.html', {'Total_Time': Total_Time})


