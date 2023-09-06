from django.shortcuts import render, redirect

def handler404(request, excpetion):
    return render(request, '404.html')