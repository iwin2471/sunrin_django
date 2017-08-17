# sunrin_django
2017 sunrin django 

# 초기설정

* 중간 문제
![프로젝트풀더](https://github.com/iwin2471/sunrin_django/blob/master/dir.PNG)

test 가상환경 기능집합

firstapp 어드민관련

first 서버설정

* 1. path 설정

* 2. 가상환경구동

foo_bar\Scripts\activate

* 3. django 설치

pip install django

* 4. 프로젝트 생성

django-admin startproject foo_bar .

* 5. 앱생성

manage.py startapp firstapp

* 6. DB update

manage.py migrate  

* 7. 관리자계정생성

manage.py createsuperuser

* 8. 서버구동 

manage.py runserver

localhost:8000/admin

* 9. 셋팅(first/setting.py)

INSTALLED_APPS의 마지막줄에 프로젝트이름 추가

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

9월셋째주 수행
