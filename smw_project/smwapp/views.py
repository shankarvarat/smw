from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html = "<html><body>Welcome !!</body></html>" 
    return HttpResponse(html)