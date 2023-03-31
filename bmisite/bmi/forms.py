from django import forms

class BMIForm(forms.Form):
    pounds = forms.FloatField(label="Enter your weight in pounds")
    feet = forms.FloatField(label="Enter your height in feet")
    inches = forms.FloatField(label="Enter your remaining height in inches")