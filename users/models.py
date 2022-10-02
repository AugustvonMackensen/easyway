from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_phone
# Create your models here.

# class User(models.Model):
#     id = models.CharField(max_length=32, primary_key=True, verbose_name='사용자 아이디')
#     pwd = models.CharField(max_length=64, verbose_name='사용자 비밀번호')
#     salt = models.CharField(max_length=32, verbose_name='암호화용 salt')
#     name = models.CharField(max_length=16, verbose_name='사용자 이름')
#     phone = models.CharField(max_length=13, unique=True, verbose_name='휴대폰 번호')
#     ssn = models.CharField(max_length=14, unique=True, verbose_name='주민번호')
#     email = models.EmailField(max_length=64, unique=True, verbose_name='이메일')
#     gender = models.CharField(max_length=1,default='M', verbose_name='성별')
#     admin = models.CharField(max_length=1, default='N', blank=True, verbose_name='관리자유무')
#     reg_date = models.DateTimeField(auto_now_add=True, verbose_name='계정 생성시간')
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         constraints = [
#             models.CheckConstraint(check=(models.Q(admin='Y')   # admin 에 대한 check 제약조건
#                                        | models.Q(admin='N')),name='admin check constraint'),
#             models.CheckConstraint(check=(models.Q(gender='F')  # gender 에 대한 check 제약조건
#                                           | models.Q(gender='M')), name='gender check constraint'),
#         ]

#https://velog.io/@nathan29849/Django-User-%EB%AA%A8%EB%8D%B8%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-Signup-User-%ED%99%95%EC%9E%A5
#상속하여 User생성
class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True, verbose_name='휴대폰 번호',validators=[validate_phone]) # 11로 바꾸기

    def __str__(self):
        return self.username