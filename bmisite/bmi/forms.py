from django import forms

class BMIForm(forms.Form):
    feet = forms.FloatField(label="Enter your height in feet")
    inches = forms.FloatField(label="Enter your remaining height in inches")
    pounds = forms.FloatField(label="Enter your weight in pounds")