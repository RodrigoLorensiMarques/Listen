from django.shortcuts import render,redirect
from .utilits import Read_TotalTime, Update_TotalTime, Verify_Date_Today, Insert_Date, Count_Date, Verify_TimeMeta,Very_MetaDays,Insert_historico, Verify_Time_Now

def home(request):
    context={}
    Total_Time=Read_TotalTime()
    Total_Days = Count_Date()
    Meta_Time = Verify_TimeMeta(Total_Time)
    Meta_Days = Very_MetaDays(Total_Days)

    if Meta_Time:
        context['Meta_Time'] = ' '

    if Meta_Days:
        context['Meta_Days'] = ' '
    

    if request.method == 'POST':
        Input_Time = request.POST.get('input_time')
        print(f"Tempo inputado: {Input_Time}")

        Update_TotalTime(Input_Time)
        Time_Now = Verify_Time_Now()
        Date_Today = Verify_Date_Today()
        Insert_Date(Date_Today)

        Insert_historico(Input_Time,Date_Today,Time_Now)

        Total_Time=Read_TotalTime()
        return redirect('home')

    context['Total_Time'] = Total_Time
    context['Total_Days'] = Total_Days
    

    return render(request, 'home.html', context)


