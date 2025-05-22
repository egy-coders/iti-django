from django import forms
from .models import Product

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Name'})
    )
    phone = forms.CharField(
        max_length=11,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Phone'})
        )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email'})
        )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Your Message', 'rows':2})
    )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'category': forms.Select(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'rows':3}),
            'pub_date' : forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'price' : forms.TextInput(attrs={'class':'form-control'}),
            'discount' : forms.TextInput(attrs={'class':'form-control'}),
            'featured' : forms.CheckboxInput(attrs={'class':'form-check-control'}),
            'image' : forms.FileInput(attrs={'class':'form-control'}),
            'branch' : forms.SelectMultiple(attrs={'class':'form-control'}),
        }