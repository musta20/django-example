from django import forms
from fristpy_app.models import testUser,UserProfileInfo
from django.core import validators
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_site','profile_pic')




class newUser(forms.ModelForm):
    class Meta():
            model = testUser
            fields = '__all__'



class formname(forms.Form):
    name = forms.CharField(max_length=264)
    email = forms.EmailField()
    veremail = forms.EmailField(label = 'ENTER YOUR EMAIL AGAIN')
    botcat = forms.CharField(required = False,
                            widget =  forms.HiddenInput ,
                            validators = [validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        veremail = all_clean_data['veremail']

        if email != veremail :
            raise forms.ValidationError("MATCH THE EMAIL MUTHER FUCLER")