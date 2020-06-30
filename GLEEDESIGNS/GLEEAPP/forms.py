from django import forms

from .models import IMAGES


class IMAGESForm(forms.ModelForm):
    class Meta:
        model = IMAGES
        fields = ['title', 'category', 'feature_image', 'attachment']
