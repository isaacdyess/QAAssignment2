from django.shortcuts import render
from django.http import HttpResponse
from .bmicalculations import *
from .forms import *


def index(request):
    form = BMIForm()
    if request.method == "POST":
        form = BMIForm(request.POST)
        pounds = float(form.data["pounds"])
        feet = float(form.data["feet"])
        inches = float(form.data["inches"])

        user_bmi = calculate_bmi(feet, inches, pounds)
        res = output(user_bmi)

        
        return render(request, 'bmi/index.html', {"form": form, "output": res})

    else:
        return render(request, 'bmi/index.html', {"form": form})