from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def meghana(request):
    return HttpResponse('MY Name Is Meghanaaaaaaaaaa Sir')

def mahesh(request):
    return HttpResponse('<h1>Mahesh Manchi AaataaGadu</h1>')

def seenu(request):
    return HttpResponse('<h1><marquee>Adhuuuu Seeenu</marquee></h1>')

def bioData(request):
    return HttpResponse('''
    <h1> Name is Kasai</h1>
    <i>age is 22</i>
    <b>Gender is Male(Not Defined)</b>
    <img src='https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTVHGeZCTsTPvuOgAkELpiPJLbt92DtizNPe7YNg6pQumJCr6Kd'>''')




