from django.shortcuts import render, HttpResponse, redirect

def newUser(request):
    response = 'placeholder to create new user'
    return HttpResponse(response)

def login(request):
    response = 'placeholder for login form'
    return HttpResponse(response)

def users(request):
    response = 'placeholder for a list of all users'
    return HttpResponse(response)
