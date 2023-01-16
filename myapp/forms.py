from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from beagledata import settings

class wifiForm(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = WifiDetails
        fields = ('ssid','password','confirm_password')

    def clean(self):
        cleaned_data = super(wifiForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            msg = "Password Mismatch Error"
            self.add_error('password', msg)
            # raise forms.ValidationError(
            #     "password and confirm_password does not match"
            # )
        
        min_length = 8
        if len(password) < min_length:
            msg = 'Password must be at least %s characters long.' % (str(min_length))
            self.add_error('password', msg)
            # raise forms.ValidationError(
            #     "Password must be at least 8 character"
            # )


class DateTimeForm(ModelForm):
    
    class Meta:
        
        model = DateTimeDetails
        fields = "__all__"
        

class LockoutForm(forms.ModelForm):
    class Meta:
        model = lockoutDetails
        fields = "__all__"

class EcForm(forms.ModelForm):
    class Meta:
        model = ECDetails
        fields = "__all__"

# class CcAssignmentForm(forms.ModelForm):
#     class Meta:
#         model = CcAssignmentDetails
#         fields = "__all__"