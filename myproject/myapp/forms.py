from django import forms
from .models import Header_top, Header_middle, Footer

class Header_topForm(forms.ModelForm):
    class Meta:
        model = Header_top
        fields = ['number', 'text', 'joined_on']
        widgets = {
            'joined_on': forms.DateInput(attrs={
                'placeholder': 'DD.MM.YYYY or YYYY-MM-DD',
                'type': 'date'  # Optional, depending on how you want the input to appear
            }),
        }

class Header_middleForm(forms.ModelForm):
    class Meta:
        model = Header_middle
        fields = ['title']

class FooterForm(forms.ModelForm):
    class Meta:
        model = Footer
        fields = ['text2', 'description']
