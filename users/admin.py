from django.contrib import admin
from .models import User
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['id'] # 검색항목 지정

# 모델과 모델관리자 연결 처리
admin.site.register(User, QuestionAdmin)
#admin.register(Question, QuestionAdmin)