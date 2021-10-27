from django.db.models import fields
from django.forms import widgets
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields ={'title','description'}

class DateInput(forms.DateInput):
    input_type ='date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets ={'due':DateInput()}
        fields = ['subject','title','description','due','is_finished']

class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100,label="Enter Your Search : ")

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields =['title','is_finished']

class UserRegistrationform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']