from django import forms
from .models import ContactInfo

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['name', 'email', 'phone', 'message']
        widgets = {'name': forms.TextInput(attrs={'class':'form-control'}),
                   'email': forms.EmailInput(attrs={'class':'form-control'}),
                   'phone': forms.NumberInput(attrs={'class':'form-control'}),
                   'message': forms.Textarea(attrs={'class':'form-control'}),
                   }
        error_messages = {'name':{'required':'Name is Required'}, 
                          'email':{'required':'Email is Required'}, 
                          'phone':{'required':'Phone is Required'}, 
                          'message':{'required':'Message is Required'}, 
                          
                          }
        