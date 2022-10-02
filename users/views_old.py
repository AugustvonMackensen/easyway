from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


from .forms import UserForm
from django.core.validators import validate_email
# Create your views here.
from .validators import validate_name

# 페이징 처리를 위한 클래스 임포트함


# HttpRequest : 서버로 오는 클라이언트 요청 객체
#HttpResponse : 서버에서 요청한 클라이언트로 답을 보내는 객체

# Create your views here.
# 브라우저 url 에서 ..../pyboard/ 서비스 요청시
# 등록된 url 매핑에 의해서 views.index 함수가 응답처리됨

def index(request):
    return render(request, 'index.html')
def index_login(request):
    return render(request, 'users/login.html')
# from .forms import BoardForm, UserCreateForm # UserCreateForm를 import한다.
# from django.contrib.auth.models import User # User 모델을 import한다.
from .models import User

def signup(request):
    if request.method == "POST": # 회원가입 폼의 값이 전송오면
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'users/signup.html', {'form': form})


from django.core.mail.message import EmailMessage

def send_email(request):
    subject = "message"
    to = ["tjgyqo2@gmail.com"]
    from_email = "tjgyqo2@gmail.com"
    message = "메지시 테스트"
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()


from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.urls import reverse_lazy

class UserPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'  # 템플릿을 변경하려면 이와같은 형식으로 입력
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm

    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            return render(self.request, 'users/password_reset_done_fail.html')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'  # 템플릿을 변경하려면 이와같은 형식으로 입력

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')
    form_class = SetPasswordForm
    def form_valid(self, form):
        return super().form_valid(form)

def view_complete(request):
    return render(request, 'users/password_reset_complete.html')

# 정보변경
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserChangeForm2
from .validators import validate_phone

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm2(request.POST, instance=request.user)
        if form.is_valid() and validate_phone(form.cleaned_data.get('phone')):
            print('valid')
            form.save()
            return redirect('users:index')
    else:
        form = CustomUserChangeForm2(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'users/update.html', context)

@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('users:login')
    return render(request, 'users/delete.html')

from django.contrib.auth import update_session_auth_hash
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            # 로그아웃 되지 않도록 새로운 password hash로 session을 업데이트함
            return redirect('users:index')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,
    }

    return render(request, 'users/change_password.html', context)
    # 위와 같은 상황에서 비밀번호를 바꾸면 로그아웃이 되어버림. 사용자 정보가 바뀌었기 때문에

from .utils import send_sms
from django.contrib import messages
def forgot_id(request):
    context = {}
    if request.method == 'POST':
        phone = request.POST.get('phone').replace('-','')
        try:
            user = User.objects.get(phone=phone)
            if user is not None:
                send_sms(user)
                return render(request, 'users/forgot_id_complete.html', context)
        except:
            messages.info(request, "해당하는 번호가 존재하지 않습니다.")

    return render(request, 'users/forgot_id.html', context)

#문자보내기

