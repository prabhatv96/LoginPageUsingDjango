from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
def test(request):
    # return HttpResponse("<h1>This is my HomePage</h1>")
    return render(request,'DemoApp/test.html', { 'name' : 'USER'})