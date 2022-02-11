from django import forms

class ObjectForm(forms.Form):
    object_name = forms.CharField(label='Объект', max_length=100)
    object_place = forms.CharField(label='Место объекта', max_length=100)