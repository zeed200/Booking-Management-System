from django import forms
from .models import *

class chbook(forms.ModelForm):
    class Meta:
        model = Reservecha 
        fields = [
            'chalits',
            'customers',
            'bunch',
            'res_cha_date',
            'login_time',
            'exit_time',
            'res_cha_price',
            'user',
        ]
        widgets = {
            'customers': forms.Select(attrs={'class':'fullname'}),
            'bunch': forms.Select(attrs={'class':'from-control'}),
            'res_cha_date': forms.DateInput(),
            'login_time': forms.TimeInput(attrs={'class':'rescha'}),
            'exit_time': forms.TimeInput(attrs={'class':'rescha'}),
            'res_cha_price': forms.TextInput(attrs={'class':'rescha'}),
           
        }

class apbook(forms.ModelForm):
    class Meta:
        model = Reserveape
        fields = [
            'apartments',
            'customers',
            'login_date',
            'exit_date',
            'res_price',
            'res_notice',
            'user',
        ]
        widgets = {
            'customers': forms.Select(attrs={'class':'fullname'}),
            'bunch': forms.Select(attrs={'class':'from-control'}),
            'login_date': forms.DateInput(),
            'exit_date': forms.DateInput(),
            'res_notice': forms.TextInput(),
            'res_price': forms.NumberInput(attrs={'class':'res_priesinp'}),
           
        }  

class Peoplech(forms.ModelForm):
    class Meta:
        model = People
        fields = [
            'reservecha',
            'peo_name',
            'peo_age',
            'peo_card_number',
            'user',
        ]
        widgets = {
            'reservecha': forms.Select(attrs={'class':'rescha'}),
            'peo_name': forms.TextInput(attrs={'class':'from-control'}),
            'peo_age': forms.NumberInput(attrs={'class':'peoage'}),
            'peo_card_number': forms.NumberInput(attrs={'class':'peocard'}),   
        }                     

class ac(forms.ModelForm):
    class Meta:
        model = Operation
        fields = [
            'fund',
            'reservecha',
            'reserveape',
            'pay_notice',
            'pay_amountoutside',
            'pay_amountinside',
            'pay_date',
            'user',
            'customers',
            'f_or',
            'recipient_name'
        ]   
        widgets = {
            'pay_notice': forms.TextInput(),
            'user': forms.TextInput(),
            'reservecha': forms.NumberInput(attrs={'class':'hide'}),
            'reserveape': forms.NumberInput(),
            'customers': forms.Select(attrs={'class':'rescha'}),
            'user': forms.Select(attrs={'class':'rescha'}),
        }   

class mo(forms.ModelForm):
    class Meta:
        model = Mortgage
        fields = [
            'fund',
            'reservecha',
            'mor_date',
            'mor_type',
            'mor_notice',
            'mor_amaunt',
            'user',
            
        ]      

class cus(forms.ModelForm):
    class Meta:
        model = Customers
        fields = [
            'cus_name',
            'cus_card_id',
            'cus_phone_number',
            'cus_address',
            'cus_age',
            'cus_gender',
            'user',
            
        ] 
          