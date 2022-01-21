from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



#calling the inbuilt in functions from django
#this calss creates a user form
class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','password']
        exclude =['user']

#this class creates member form
class NewMemberForm(ModelForm):
    
    class Meta:
        model = Member
        fields ='__all__'
        exclude =['user']

#this class creates a book form
class NewBookForm(ModelForm):

    class Meta:
        model = Book
        fields ='__all__'
        

