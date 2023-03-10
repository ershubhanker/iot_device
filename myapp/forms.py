from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from beagledata import settings

class wifiForm(forms.ModelForm):
    ssid = forms.CharField(required=False)
    password = forms.CharField(required=False)    
    # confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = WifiDetails
        fields = "__all__"
        # fields = ('ssid','password','confirm_password')

    # def clean(self):
    #     cleaned_data = super(wifiForm, self).clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")

    #     if password != confirm_password:
    #         msg = "Password Mismatch Error"
    #         self.add_error('password', msg)
    #         # raise forms.ValidationError(
    #         #     "password and confirm_password does not match"
    #         # )
        
    #     min_length = 8
    #     if len(password) < min_length:
    #         msg = 'Password must be at least %s characters long.' % (str(min_length))
    #         self.add_error('password', msg)
            # raise forms.ValidationError(
            #     "Password must be at least 8 character"
            # )


class DateTimeForm(ModelForm):
    
    class Meta:
        
        model = DateTimeDetails
        fields = "__all__"
        

class LockoutForm(forms.ModelForm):
    weekday_from_1 = forms.IntegerField(required=False,initial=0)
    weekday_to_1 = forms.IntegerField(required=False,initial=0)
    weekday_from_2 = forms.IntegerField(required=False,initial=0)
    weekday_to_2 = forms.IntegerField(required=False,initial=0)

    weekend_from_1 = forms.IntegerField(required=False,initial=0)
    weekend_to_1 = forms.IntegerField(required=False,initial=0)
    weekend_from_2 = forms.IntegerField(required=False,initial=0)
    weekend_to_2 = forms.IntegerField(required=False,initial=0)


    class Meta:
        model = tou_details
        fields = "__all__"


class EcForm(forms.ModelForm):
    sensed_panel_rating = forms.IntegerField(required=False, initial=100)
    c1 = forms.CharField(required=False)
    max_amp1 = forms.IntegerField(required=False,initial=0)
    # c1ab = forms.IntegerField(required=False,initial='A')
    c2 = forms.CharField(required=False)
    max_amp2 = forms.IntegerField(required=False,initial=0)
    # c2ab = forms.IntegerField(required=False,initial='A')
    c3 = forms.CharField(required=False)
    max_amp3 = forms.IntegerField(required=False,initial=0)
    # c3ab = forms.IntegerField(required=False,initial='A')
    c4 = forms.CharField(required=False)
    max_amp4 = forms.IntegerField(required=False,initial=0)
    # c4ab = forms.IntegerField(required=False,initial='A')
    
    class Meta:
        model = ECDetails
        fields = "__all__"

# class CcAssignmentForm(forms.ModelForm):
#     class Meta:
#         model = CcAssignmentDetails
#         fields = "__all__"