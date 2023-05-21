from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1><marquee>This is the first SFB</h1></marquee>')
def second(request):
    return HttpResponse('<h1><b><marquee>This is the second SVB</marquee></b></h1>')
def sai(request):
    return HttpResponse('<h1><center>sai is innocent boy</center></h1>')
def shankar(request):
    return HttpResponse('<h1><p style="text-align:right;">shankar is a beer drinking boy </p></h1>')