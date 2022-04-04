from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def addProduct(request):
    return HttpResponse('add product called...')

def viewProduct(request):
    return HttpResponse('view product called...')


