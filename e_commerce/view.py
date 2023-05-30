from django.http import HttpResponse
from django.shortcuts import render

def hoje_page(request):
    return render(request, 'home_page.html', {})