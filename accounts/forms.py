from django import forms
#from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from .models import stu


class s1(UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        
        for fieldname in ['username','password1','password2']:
            self.fields[fieldname].help_text = None
            
    print(UserCreationForm)     
    
    class Meta(UserCreationForm.Meta):
        model = stu
        fields = ('student','username')
        



class s2(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = stu
        fields = ('student','username')


# class UserCreateForm(UserCreationForm):
# 	fields = ("username", "student ID","password1", "password2")
# 	model = get_user_model()

# 	def __init__(self, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
# 		self.fields['username'].help_text = None		
# 		self.fields['password1'].help_text = None
# 		self.fields['password2'].help_text = None
