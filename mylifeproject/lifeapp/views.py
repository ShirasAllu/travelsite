from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from  . models import person
# Create your views here.
#def homepage(request):
    #return render(request,"homepage.html")
def about(request):
    obj=place.objects.all()
    ob=person.objects.all()
    return render(request,"index.html",{'result':obj,'results':ob})
#def contact(request):
    #return HttpResponse('welcome contact page')
#def detail(request):
    #return render(request,"detail.html")
#def thankspage(request):
   # return HttpResponse('WELCOME TO THANKS PAGE')