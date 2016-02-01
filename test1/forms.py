from django.contrib.auth.hashers import make_password

__author__ = 'miner'
from django import forms
from .models import MyUser


class UserCreationForm(forms.ModelForm):
    field1 = forms.CharField(label="char1")
    field2 = forms.CharField(label="char2")
    field3 = forms.CharField(label="char3")
    class Meta:
        model = MyUser
        fields = ("username","password","field1","field2","field3",)
        widgets = {
        'password': forms.PasswordInput(),
    }



    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data["password"])
        user.field1= self.cleaned_data["field1"]
        user.field2= self.cleaned_data["field2"]
        user.field3= self.cleaned_data["field3"]
        if commit:
            user.save()
            return user
class InputForm(forms.Form):
    input_user = forms.CharField(label='Search for data .. ', max_length=100)
