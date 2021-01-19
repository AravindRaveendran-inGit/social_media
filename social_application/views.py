from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




def home(request):
    hello = 'working'
    return render(request,'main/home.html',{'hello': hello })