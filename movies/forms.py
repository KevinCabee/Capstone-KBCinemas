from django import forms

class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255)
    email = forms.EmailField()
    card_number = forms.CharField(max_length=16)
    cvv = forms.CharField(max_length=3)
    expiration_date = forms.DateField()
