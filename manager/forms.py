from django import forms
from manager.models import Purchase
from  manager.models import Purchase,Inventory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['medicine_id','quantity','medicine_name','purchase_amount']

