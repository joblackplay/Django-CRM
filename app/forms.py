from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Adress'}))
    first_name = forms.CharField(label="",max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label="",max_length=60,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text ='<span class="form-text text-muted"><small>Required. 150 character or fewer, digits and @/./ +/-/_only</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text ='<ul class="form-text text-muted small"><li>Your password can\'t be too similar your infamation personal</li><li>Your password must contain at least 8 caracter.</li><li>Your password can\'t be a commoly used password</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text ='<span class="form-text text-muted"><small>Enter the same as before, for verification</small></span>'




#Create Add Record Form

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label="",max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Last Name"}),max_length=50)
    email = forms.EmailField(required=True,label="",widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}),max_length=100)
    phone = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Phone"}),max_length=20)
    address = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Address"}),max_length=100)
    city = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"City"}),max_length=50)
    state = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"State"}),max_length=50)
    zipcode = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Zipcode"}),max_length=20)


    class Meta:
        model =Record
        exclude = ("user",)

