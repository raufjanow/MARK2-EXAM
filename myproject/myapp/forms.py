from django import forms
from .models import header_top, header_middle, header_bot

class Header_topForm(forms.ModelForm):
    class Meta:
        model = header_top
        fields = ['number', 'text', 'joined_on']
        widgets = {
            'joined_on': forms.DateInput(attrs={
                'placeholder': 'DD.MM.YYYY or YYYY-MM-DD',
                'type': 'date'  # Optional, depending on how you want the input to appear
            }),
        }

class Header_middleForm(forms.ModelForm):
    class Meta:
        model = header_middle
        fields = ['title']

class header_botForm(forms.ModelForm):
    class Meta:
        model = header_bot
        fields = ['text2', 'description']

