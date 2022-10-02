from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import COVID_REGION, COVID_DOMESTIC
import time

def region(request):
    filename = time.strftime('%y%m%d')
    context = {'filename' : filename}
    return render(request, 'covid/regcovid.html', context)

def domestic(request):
    filename = time.strftime('%y%m%d')
    context = {'filename' : filename}
    return render(request, 'covid/domcovid.html', context)

def regional_table(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        regions = COVID_REGION.objects.filter(REGION__contains=searched) \
                  |COVID_REGION.objects.filter(REGDATE__contains=searched)
        context = {'searched' : searched, 'regions': regions}
        return render(request, 'covid/regiontable.html', context)
    else:
        return render(request, 'covid/regiontable.html', {})

def domestic_table(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        domestic = COVID_DOMESTIC.objects.filter(COVDATE__contains=searched)
        context = {'searched' : searched, 'domestic': domestic}
        return render(request, 'covid/domestictable.html', context)
    else:
        return render(request, 'covid/domestictable.html', {})
