from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .validators import validate_phone
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
class UserForm(UserCreationForm):
    # 추가할 필드 속성
    first_name = forms.CharField(max_length=150, label='이름')
    email = forms.EmailField(label='이메일')
    phone = forms.CharField(max_length=11, validators=[validate_phone], label='휴대전화')
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'email',  'phone')
        labels = {
            'username': '아이디',
            'password1': '비밀번호',
            'password2': '비밀번호 재확인',
            'first_name': '이름',
            'email': '이메일',
            'phone': '휴대전화',
        }


class CustomUserChangeForm(UserChangeForm):
    phone = forms.CharField(max_length=11, validators=[validate_phone], label='휴대전화')
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email', 'phone']
        labels = {
            'username': '아이디',
            'first_name': '이름',
            'email': '이메일',
            'phone': '휴대전화',
        }

class Get_UserIDForm(forms.ModelForm):
    pass


class CustomUserChangeForm2(UserChangeForm):
    phone = forms.CharField(max_length=11, validators=[validate_phone], label='휴대전화')
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email', 'phone']
        labels = {
            'username': '아이디',
            'first_name': '이름',
            'email': '이메일',
            'phone': '휴대전화',
        }

