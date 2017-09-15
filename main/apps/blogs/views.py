from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = 'placeholder to later display a list of all the blogs'
    return HttpResponse(response)

def new(request):
    response = 'placeholder to later display a new form to create a new blog'
    return HttpResponse(response)

def create(request):
    return redirect(index)

def show(request,num):
    response = 'placeholder to display blog '+num
    return HttpResponse(response)

def edit(requst,num):
    response = 'placeholder to edit blog '+num
    return HttpResponse(response)

def destroy(request,num):
    return redirect(index)
