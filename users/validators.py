import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
# 이메일 validate
def validate_email(email):
	# 이메일의 정규식
    email_regex = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    # 주어진 email을 email_regex에 match한다.
    return re.match(email_regex, email)

# 비밀번호 validate
def validate_password(password):
	# 패스워드의 정규식
    password_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
    # 주어진 password를 password_regex에 match한다.
    return re.match(password_regex, password)

def validate_name(name):
    # 이름 정규식
    hangul_regex = r'[^ ㄱ-ㅣ가-힣]+'
    #b = re.match(hangul_regex, name)
    if ~re.match(hangul_regex, name):
        raise ValidationError("띄어쓰기를 제외한 한글만 입력하세요.")
def continuousPwd(pwd):
    pwdlist = []
    for i in range(len(pwd)):
        pwdlist.append(ord(pwd[i]))
    print(pwdlist)

    for i in range(len(pwd)-2):
        # if ((pwdlist[i] > 47 and pwdlist[i + 2]) <58 or (pwdlist[i] > 64 and pwdlist[i + 2] < 91)):
            #배열의 연속된 수 검사
            # 3번째 글자 - 2번쨰 글자 = 1, 3번쨰 글자 - 1번째 글자 = 2
        if (abs(pwdlist[i+2] - pwdlist[i+1]) == 1 and abs(pwdlist[i+2] - pwdlist[i]) == 2):
            c1 = chr(pwdlist[i])
            c2 = chr(pwdlist[i+1])
            c3 = chr(pwdlist[i+2])
            return print(c1, c2, c3)


class ContinuousPwd3:
    def validate(self, password, user=None):
        pwdlist = []
        for i in range(len(password)):
            pwdlist.append(ord(password[i]))
        print(pwdlist)
        for i in range(len(password) - 2):
            # if ((pwdlist[i] > 47 and pwdlist[i + 2]) <58 or (pwdlist[i] > 64 and pwdlist[i + 2] < 91)):
            # 배열의 연속된 수 검사
            # 3번째 글자 - 2번쨰 글자 = 1, 3번쨰 글자 - 1번째 글자 = 2
            if (abs(pwdlist[i + 2] - pwdlist[i + 1]) == 1 and abs(pwdlist[i + 2] - pwdlist[i]) == 2):
                c1 = chr(pwdlist[i])
                c2 = chr(pwdlist[i + 1])
                c3 = chr(pwdlist[i + 2])
                if abs(pwdlist[i]-pwdlist[i + 1]) != 1:
                    continue
                else:
                    raise ValidationError(_(f"연속 문자 3자리{c1}{c2}{c3}은(는) 비밀번호로 사용할 수 없습니다."), code='continuous3')
                    return print(c1, c2, c3)
    def get_help_text(self):
        return _("비밀번호는 연속된 3자리의 문자 또는 숫자가 포함될 수 없습니다.")

def validate_phone(phone):
    a = 'asdf'
    phone = phone.replace('-', '')
    if phone.isdigit():
        if (len(phone) == 10) or (len(phone) == 11):
            return True #raise ValidationError('숫자만 입력하세요.', code='isdigit')
        else:
            raise ValidationError('번호가 너무 짧습니다.', code='isdigit2')
    else:
        raise ValidationError('숫자만 입력하세요.', code='isdigit')
