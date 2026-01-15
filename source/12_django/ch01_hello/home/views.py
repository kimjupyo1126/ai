from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
   # return HttpResponse("Hello World")
    return render(request, template_name:"home.html", context:{"msg":"Django(장고)"})