from django.shortcuts import render
from django.http import HttpResponse
from .utilits import Read_Historico


def historico (request):
    context={}
    Historico_Now = Read_Historico()
    print (Historico_Now)
    context['Historico_Now'] = Historico_Now
    return render(request,'historico.html',context)
