from django import forms
from Home.models import Employes


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Employes
        fields = ('E_id', 'F_name','L_name','Email','profile_pic')