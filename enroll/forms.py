from django import forms
from .models import Student


class modelform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fname','lname','email','city']
        widgets={'fname':forms.TextInput(attrs={'class':'form-control','pattern':'[A-Za-z]+'}),
                 'lname':forms.TextInput(attrs={'class':'form-control','pattern':'[A-Za-z]+'}),
                 'city':forms.TextInput(attrs={'class':'form-control','pattern':'[A-Za-z]+'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),}
        labels={'fname':'First Name :','lname':'Last Name','city':'City',
                'email':'Email Address :'}