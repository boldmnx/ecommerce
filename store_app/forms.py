from django import forms
from .models import *


class BaraaForm(forms.ModelForm):
    class Meta:
        model = Baraa
        fields = '__all__'
        labels = {
            'ner': 'Нэр',
            'une': 'Үнэ',
            'too': 'Тоо ширхэг',
        }
        # widgets = {
        #     'npara': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        #     # 'nognoo':  forms.DateInput(attrs={'type': 'date'}),
        #     'nognoo':  forms.HiddenInput(),
        # }