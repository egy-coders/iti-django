from django import forms
from .models import Product
from django.core.exceptions import ValidationError
from django.utils import timezone

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

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not (3 <= len(name) <100):
            raise ValidationError("Name Must Be between 3 and 100 Characters")
        return name    
    
    def clean_pub_date(self):
        pub_date = self.cleaned_data.get('pub_date')
        if pub_date and pub_date > timezone.localdate():
            raise ValidationError("Date must be before today")
        return pub_date
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None or price <=0:
            raise ValidationError("Price must be greater than 0")
        return price

    def clean_discount(self):
        discount = self.cleaned_data.get('discount')
        if not (0 <= discount <=100):
            raise ValidationError("Discount between 0 and 100")
        return discount

    def clean(self):
        cleaned_data = super().clean()

        discount = cleaned_data.get('discount')
        featured = cleaned_data.get('featured')

        if discount > 50 and not featured:
            raise ValidationError("If disocunt > 50\%\ item must be featured!")

        return cleaned_data