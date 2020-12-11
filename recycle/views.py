from django.shortcuts import render


def index(request):
    return render(request, 'recycle/index.html')

def chart(request):
    return render(request, 'recycle/chart.html')

def table(request):
    return render(request, 'recycle/table.html')

