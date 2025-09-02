from django.shortcuts import render, redirect
from .forms import BaraaForm, Baraa


def baraa_burtgel(request):

    if request.method == 'GET':
        baraaModels = Baraa.objects.all()
        baraaForm = BaraaForm()
        return render(request, 'baraa/index.html', {'nForm': baraaForm, 'baraa': baraaModels})
    elif request.method == 'POST':
        subbaraa = BaraaForm(request.POST)
        if subbaraa.is_valid():
            subbaraa.save()
        return redirect('/')
