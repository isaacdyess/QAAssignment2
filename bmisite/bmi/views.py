from django.shortcuts import render
from django.http import HttpResponse
from .bmicalculations import *


def index(request):
    if request.method == "POST":
        pounds = float(request.POST["pounds"])
        feet = float(request.POST["feet"])
        inches = float(request.POST["inches"])

        user_bmi = calculate_bmi(feet, inches, pounds)
        res = {'output': output(user_bmi)}

        return render(request, 'bmi/index.html', res)
    else:
        return render(request, 'bmi/index.html')
