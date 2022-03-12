from django.contrib.auth.models import User
from .models import Profile
from django import forms

class update_user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    


class update_profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','image_attribution','image_attribution_name','age','occupation','about','city','degree']