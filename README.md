# Facebook
👋 Hello! 🗣️ Design presentation about online Social project named “Facebook”.

🎨 Design motivation for an online Facebook project.

💖 Please click like and appreciate.

🙏 Thank you for supporting and appreciating my efforts

## Website Build


# Preview Login
![This is an image](https://raw.githubusercontent.com/learncodingeasy/Facebook/main/facebook_vue/src/assets/image/Login.png)

# Preview Signup
![This is an image](https://raw.githubusercontent.com/learncodingeasy/Facebook/main/facebook_vue/src/assets/image/Signup.png)

# Facebook
👋 Hello! 🗣️ Design presentation about online Social project named “Faceb ook”.

🎨 Design motivation for an online Facebook project.

💖 Please click like and appreciate.

🙏 Thank you for supporting and appreciating my efforts

## Website Build


### 1 Git Clone Project
```
git clone https://github.com/LearnCodingEasy/Facebook.git
``` 
__________________________________________________
### 2 Create File [ LICENSE ]
```
LICENSE
``` 
#### In Side File [ LICENSE ]
```
MIT License
Copyright (c) 2024 Hossam Rashad
```
__________________________________________________
### 3 Create Virtual Environment
```cmd
python -m venv facebook_virtual_environment
```
#### Activate Virtual Environment
```cmd
facebook_virtual_environment\Scripts\activate
```
__________________________________________________
### 4 Install Django
```cmd
pip install django
```
__________________________________________________
### 5 Install Django Libraries [ 1 - djangorestframework | 2 - djangorestframework-simplejwt | 3 - django-cors-headers | 4 - pillow ]
```cmd
pip install djangorestframework djangorestframework-simplejwt django-cors-headers pillow
```
__________________________________________________
### 6 Create Django Project
```cmd
django-admin startproject facebook_django
```
__________________________________________________
### 7 Create Django App
```cmd
cd facebook_django
```
```python
python manage.py startapp account
```
__________________________________________________
### 8 Setup Djang Libraries
```python
# Page [facebook/facebook_django/facebook_django/settings.py]

# استيراد مكتبة timedelta عشان نحدد مدة صلاحية التوكين
from datetime import timedelta

# ALLOWED_HOSTS ده المتغير اللي بنحدد فيه الدومينات أو الآيبيهات اللي مسموح لها تشغل المشروع
ALLOWED_HOSTS = []

# URL أو على سيرفر حقيقي (localhost) الموقع اللي بنشتغل عليه سواء كان محلي
WEBSITE_URL = "http://127.0.0.1:8000"

# EMAIL_BACKEND ده اللي بيحدد طريقة إرسال الإيميلات من خلال 
# Django، هنا مختار انه يطبع الإيميلات في الكونسل
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# Django، هنا سيتم إرسال الرسائل الإيميلات الى الإيميلات
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# مزود SMTP الخاص بك (في هذه الحالة Gmail)
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# البريد الإلكتروني الذي سيتم إرسال الرسائل منه
EMAIL_HOST_USER = "learncodingeasy0100@gmail.com"
# كلمة مرور البريد الإلكتروني
EMAIL_HOST_PASSWORD = "uxcg nuae kfjq txre"
DEFAULT_FROM_EMAIL = "learncodingeasy0100@gmail.com"


# AUTH_USER_MODEL ده اللي بنحدد فيه موديل المستخدمين اللي شغالين عليه
AUTH_USER_MODEL = "account.User"

# SIMPLE_JWT دي إعدادات مكتبة JWT اللي بنستخدمها لإدارة التوكينات
SIMPLE_JWT = {
    # ACCESS_TOKEN_LIFETIME ده اللي بيحدد مدة صلاحية توكين الدخول
    # (Access Token)، هنا مدته 30 يوم
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    # REFRESH_TOKEN_LIFETIME ده اللي بيحدد مدة صلاحية توكين التحديث
    # (Refresh Token)، هنا مدته 180 يوم
    "REFRESH_TOKEN_LIFETIME": timedelta(days=180),
    # ROTATE_REFRESH_TOKENS ده اللي بيحدد لو التوكين بيتجدد مع كل تحديث للتوكين ولا لأ، هنا مش بيتجدد
    "ROTATE_REFRESH_TOKENS": False,
}

# REST_FRAMEWORK دي إعدادات مكتبة Django Rest Framework
REST_FRAMEWORK = {
    # DEFAULT_AUTHENTICATION_CLASSES دي اللي بتحدد نوع المصادقة الافتراضية اللي هتكون JWT
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # DEFAULT_PERMISSION_CLASSES دي بتحدد الإذن الافتراضي اللي هو أن المستخدم لازم يكون مصدق عليه (Authenticated)
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

# CORS_ALLOWED_ORIGINS دي بنحدد فيها الأصول المسموح لها تتواصل مع السيرفر بتاعنا
CORS_ALLOWED_ORIGINS = [
    # أصل خاص بـ Vue.js على بورت 5173
    "http://localhost:5173",
    # أصل خاص بـ Vue.js على بورت 5174
    "http://localhost:5174",
]

# CSRF_TRUSTED_ORIGINS دي بنحدد فيها الأصول الموثوقة اللي بنسمح لها تستخدم
# CSRF مع السيرفر
CSRF_TRUSTED_ORIGINS = [
    # أصل خاص بـ Vue.js على بورت 5173
    "http://localhost:5173",
    # أصل خاص بـ Vue.js على بورت 5174
    "http://localhost:5174",
]

# Django اللي متضافه لمشروع (Libraries) والمكتبات (Apps) دي قائمة بالتطبيقات 
INSTALLED_APPS = [
    # ...
    # Apps
    "account",
    # Libraries
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
]

# 🛡️ (requests) هي عبارة عن مكونات أو طبقات بتتعامل مع الطلبات Middleware الـ
# اللي بتجيلك من المستخدمين قبل ما توصل لوجهتها النهائية في السرفر
MIDDLEWARE = [
    # ...
    "corsheaders.middleware.CorsMiddleware",
    # ...
]

# - 🌐 `STATIC_URL` بيحدد الرابط اللي هتعرض عليه الملفات الثابتة.
STATIC_URL = "static/"
# - 📷 `MEDIA_URL` بيحدد الرابط اللي هتعرض عليه ملفات الميديا اللي بيرفعها المستخدمين.
MEDIA_URL = "media/"
# - 💾 `MEDIA_ROOT` بيحدد مكان تخزين ملفات الميديا الفعلي على جهاز السيرفر
MEDIA_ROOT = BASE_DIR / "media"
```
__________________________________________________
### 9 Setup App [ Account ]
```python
# Page [ facebook/facebook_django/account/models.py ]
# uuid: يُستخدم لإنشاء معرّفات فريدة عالمياً
# (UUID) التي يمكن استخدامها لتعريف المستخدمين
import uuid

# settings: لاستيراد إعدادات
# Django الخاصة بالمشروع
from django.conf import settings

# AbstractBaseUser, PermissionsMixin: لإنشاء نموذج مستخدم مخصص
# UserManager: لإدارة إنشاء المستخدمين
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

# models: Django لإنشاء نماذج
from django.db import models

# timezone: للتعامل مع التوقيتات
from django.utils import timezone

# 🔧 لإدارة المستخدمين المخصص CustomUserManager تم إنشاء كلاس باسم
# Django المتوفر افتراضيًا في UserManager وهو يرث من كلاس
class CustomUserManager(UserManager):
    """
    _create_user دالة داخلية لإنشاء مستخدم جديد
    name: اسم المستخدم
    email: البريد الإلكتروني للمستخدم
    password: كلمة المرور
    **extra_fields: أي حقول إضافية
    """

    def _create_user(self, name, email, password, **extra_fields):
        # الجزء ده بيتأكد إن الإيميل مش فاضي، ولو كان فاضي سيتم رفع خطأ
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        # ومظبوط small letters هنا بنعمل عملية تنسيق للإيميل بحيث يبقى كله
        # normalize_email باستخدام
        email = self.normalize_email(email)
        # هنا بنعمل إنشاء للمستخدم نفسه وبنمرر الاسم والإيميل وبقية الحقول الإضافية
        user = self.model(email=email, name=name, **extra_fields)
        # هنا بنعمل إعداد كلمة السر للمستخدم
        user.set_password(password)
        # database وأخيرًا هنا بنحفظ المستخدم في قاعدة البيانات باستخدام الـ
        # اللي إحنا شغالين عليها
        user.save(using=self._db)
        # وبعدين بنرجع المستخدم اللي اتعمله إنشاء
        return user

    # عشان تعمل إنشاء مستخدم عادي create_user هنا بنعرف ميثود جديدة اللي هي
    def create_user(self, name=None, email=None, password=None, **extra_fields):
        # هنا بنحدد أن المستخدم العادي مش هيبقى
        # staff ومش هيبقى superuser
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        # _create_user وبعدين بننادي على الميثود اللي عملناها فوق
        # عشان تكمل عملية الإنشاء
        return self._create_user(name, email, password, **extra_fields)

    # create_superuser هنا بنعرف ميثود جديدة اللي هي
    # superuser عشان تعمل إنشاء للمستخدم اللي هو
    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        # هنا بنحدد أن المستخدم ده هيبقى
        # staff وكمان هيبقى superuser
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        # _create_user وبعدين برضه بننادي على الميثود
        # superuse عشان تكمل عملية الإنشاء بس للمستخدم اللي هو
        return self._create_user(name, email, password, **extra_fields)


        # اللي هو المستخدم User بنعمل كلاس اسمه
        # AbstractBaseUser و PermissionsMixin وده بيورث من
        # Djangoاللي فيهم أساسيات المستخدم في
        class User(AbstractBaseUser, PermissionsMixin):
            # id: اللي بيكون مفتاح أساسي للمستخدم، عشان يكون فريد لكل مستخدم UUID ده الـ
            id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
            # ___________________
            # حقل يتم تعبئة من المستخدام
            # ___________________
            # تسجيل الدخول
            # name: الاسم الخاص بالمستخدم
            name = models.CharField(max_length=255, blank=True, default="")
            # surname: الاسم العائلةالخاص بالمستخدم
            surname = models.CharField(max_length=255, blank=True, default="")
            # email: البريد الإلكتروني الخاص بالمستخدم
            email = models.EmailField(unique=True)
            # Date of birth تاريخ الميلاد
            date_of_birth = models.DateField(default=timezone.now)
            # Gender الجنس المستخدم
            gender = models.CharField(max_length=15, blank=True, null=True)
            # avatar: الصورة الشخصية للمستخدم
            avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
            # cover: الصورة الغلاف للمستخدم
            cover = models.ImageField(upload_to="covers", blank=True, null=True)
        
            # is_active: حالة تفعيل المستخدم
            is_active = models.BooleanField(default=True)
            # is_superuser: حالة المستخدم كمشرف
            is_superuser = models.BooleanField(default=False)
            # is_staff: حالة المستخدم كموظف
            is_staff = models.BooleanField(default=False)
        
            # ___________________
            # حقل يتم تعبئة تلقائي
            # ___________________
            # date_joined: تاريخ انضمام المستخدم
            date_joined = models.DateTimeField(default=timezone.now)
            # last_login: تاريخ آخر تسجيل دخول للمستخدم
            last_login = models.DateTimeField(blank=True, null=True)
        
            # تخصيص السلوك في إدارة المستخدمين بشكل مرن ومنظم
            objects = CustomUserManager()
        
            # email يحدد الحقل الذي سيتم استخدامه لتسجيل الدخول. في هذه الحالة، هو
            USERNAME_FIELD = "email"
            # يحدد الحقل الذي يتم استخدامه كالبريد الإلكتروني الرئيسي للمستخدم. في هذه الحالة، هو email.
            EMAIL_FIELD = "email"
            # 📝 لا توجد حقول إضافية مطلوبة بجانب البريد الإلكتروني وكلمة المرور عند إنشاء مستخدم جديد عبر الأوامر الإدارية.
            REQUIRED_FIELDS = []

# اللي هو المستخدم User بنعمل كلاس اسمه
# AbstractBaseUser و PermissionsMixin وده بيورث من
# Djangoاللي فيهم أساسيات المستخدم في
class User(AbstractBaseUser, PermissionsMixin):
    # id: اللي بيكون مفتاح أساسي للمستخدم، عشان يكون فريد لكل مستخدم UUID ده الـ
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # ___________________
    # حقل يتم تعبئة من المستخدام
    # ___________________
    # تسجيل الدخول
    # name: الاسم الخاص بالمستخدم
    name = models.CharField(max_length=255, blank=True, default="")
    # surname: الاسم العائلةالخاص بالمستخدم
    surname = models.CharField(max_length=255, blank=True, default="")
    # email: البريد الإلكتروني الخاص بالمستخدم
    email = models.EmailField(unique=True)
    # Date of birth تاريخ الميلاد
    date_of_birth = models.DateField(default=timezone.now)
    # Gender الجنس المستخدم
    gender = models.CharField(max_length=15, blank=True, null=True)
    # avatar: الصورة الشخصية للمستخدم
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    # cover: الصورة الغلاف للمستخدم
    cover = models.ImageField(upload_to="covers", blank=True, null=True)

    # is_active: حالة تفعيل المستخدم
    is_active = models.BooleanField(default=True)
    # is_superuser: حالة المستخدم كمشرف
    is_superuser = models.BooleanField(default=False)
    # is_staff: حالة المستخدم كموظف
    is_staff = models.BooleanField(default=False)

    # ___________________
    # حقل يتم تعبئة تلقائي
    # ___________________
    # date_joined: تاريخ انضمام المستخدم
    date_joined = models.DateTimeField(default=timezone.now)
    # last_login: تاريخ آخر تسجيل دخول للمستخدم
    last_login = models.DateTimeField(blank=True, null=True)

    # تخصيص السلوك في إدارة المستخدمين بشكل مرن ومنظم
    objects = CustomUserManager()

    # email يحدد الحقل الذي سيتم استخدامه لتسجيل الدخول. في هذه الحالة، هو
    USERNAME_FIELD = "email"
    # يحدد الحقل الذي يتم استخدامه كالبريد الإلكتروني الرئيسي للمستخدم. في هذه الحالة، هو email.
    EMAIL_FIELD = "email"
    # 📝 لا توجد حقول إضافية مطلوبة بجانب البريد الإلكتروني وكلمة المرور عند إنشاء مستخدم جديد عبر الأوامر الإدارية.
    REQUIRED_FIELDS = []
    
    
```
* Create Page [ serializers.py ] Inside App Account 
```cmd
serializers.py
```
```python
# Page [ facebook/facebook_django/account/serializers.py ]
# Django Rest Framework من serializers هنا بنستورد مكتبة
# JSON اللي بتساعدنا في تحويل البيانات لأنواع مختلفة زي
from rest_framework import serializers

# اللي بنستخدمه في تكوين البيانات User هنا بنستورد الموديل الخاص بـ
from .models import User

# UserSerializer بنعمل كلاس اسمه
# اللي هو هيكون مسؤول عن تحويل البيانات من وإلى شكل مناسب للاستخدام
class UserSerializer(serializers.ModelSerializer):
    # Serializer هنا بنحدد الميتا كلاس اللي بيحتوي على إعدادات الـ
    class Meta:
        # User هو موديل الـ Serializer بنحدد ان الموديل اللي هنستخدمه في الـ
        model = User
        # API بنحدد الحقول اللي عايزين نحولها أو نرجعها عند التعامل مع الـ
        fields = (
            # الخاص بالمستخدم ID الحقل ده بيخزن الـ
            "id",
            # الحقل ده بيخزن الاسم الأول للمستخدم
            "name",
            # الحقل ده بيخزن اسم العائلة للمستخدم
            "surname",
            # الحقل ده بيخزن البريد الإلكتروني للمستخدم
            "email",
            # الحقل ده بيخزن تاريخ الميلاد للمستخدم
            "date_of_birth",
            # الحقل ده بيخزن الجنس الخاص بالمستخدم
            "gender",
        )

```
* Create Page [ forms.py ] Inside App Account 
```cmd
forms.py
```
```python
# Page [ facebook/facebook_django/account/forms.py ]

# UserCreationForm خاص بإنشاء المستخدمين اللي هو Django هنا بنستورد فورم جاهز من
from django.contrib.auth.forms import UserCreationForm

# اللي بتساعدنا في إنشاء الفورمات Django من forms هنا بنستورد مكتبة
from django import forms

# app من الموديلز الخاصة بالـ User هنا بنستورد الموديل الخاص بالمستخدم اللي هو
from .models import User

# UserCreationForm اللي بيرث من SignupForm بنعمل كلاس اسمه
# الكلاس ده هيستخدم لإنشاء فورم لتسجيل المستخدمين الجدد
class SignupForm(UserCreationForm):
    # بنحدد الميتا كلاس اللي بيحتوي على إعدادات الفورم
    class Meta:
        # User بنحدد ان الموديل اللي الفورم ده هيشتغل عليه هو موديل الـ
        model = User
        fields = (
            # الاسم الأول للمستخدم
            "name",
            # اسم العائلة للمستخدم
            "surname",
            # البريد الإلكتروني للمستخدم
            "email",
            # تاريخ ميلاد المستخدم
            "date_of_birth",
            # الجنس الخاص بالمستخدم
            "gender",
            # كلمة المرور الأولى اللي المستخدم هيكتبها
            "password1",
            # تأكيد كلمة المرور اللي المستخدم هيكتبها للمطابقة
            "password2",
        )

```
```python
# Page [ facebook/facebook_django/account/views.py ]

# بسيطة HTTP عشان نستخدمها في إرجاع استجابات Django من HttpResponse إستيراد دالة
from django.http import HttpResponse

# (لو احتجناها) HTML عشان نستخدمها في عرض الصفحات Django من render إستيراد دالة
from django.shortcuts import render

# إستيراد نموذج المستخدم من الموديلات
from .models import User

def activateemail(request):
    # (اللي جايين في الرابط) request من الـ ID الحصول على البريد الإلكتروني و
    email = request.GET.get("email", "")
    id = request.GET.get("id", "")
    # ( ID الإيميل و ) هنا بنتأكد إن البيانات المطلوبة موجودة
    if email and id:

        # بنجيب المستخدم من قاعدة البيانات اللي ليه الـ ID والإيميل دول
        user = User.objects.get(id=id, email=email)
        # بنفعّل حساب المستخدم
        user.is_active = True
        # بنحفظ التغييرات في قاعدة البيانات
        user.save()

        # بنرجع رد نصي بيقول إن المستخدم تم تفعيله ويقدر يسجل دخول
        return HttpResponse("The user is now activated. You can go ahead and log in!")
    else:
        # لو البيانات مش كاملة أو مش صحيحة، بنرجع رد نصي بيقول إن البارامترات غير صحيحة
        return HttpResponse("The parameters is not valid!")

```
* Create Page [ api.py ] Inside App Account 
```cmd
api.py
```
```python
# Page [ facebook/facebook_django/account/api.py ]
# Django إستيراد إعدادات المشروع عشان نستخدمها في الكود
from django.conf import settings

# إستيراد نموذج تغيير كلمة المرور
# هنا بنستورد نموذج تغيير كلمة المرور الجاهز من Django

from django.contrib.auth.forms import PasswordChangeForm

# إستيراد دالة إرسال البريد الإلكتروني
# هنا بنستورد دالة إرسال البريد الإلكتروني عشان نستخدمها في إرسال إيميل التفعيل
from django.core.mail import send_mail

# JSON لإرجاع استجابات JsonResponse إستيراد
from django.http import JsonResponse

# إستيراد الديكورات لتعريف وحدات الواجهة البرمجية
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

# إستيراد دالة إنشاء الإشعارات
# from notification.utils import create_notification

# إستيراد النماذج المخصصة لتسجيل المستخدم وتعديل الملف الشخصي
from .forms import SignupForm

# إستيراد النماذج المخصصة للمستخدم وطلبات الصداقة
from .models import User

# FriendshipRequest

# إستيراد المسلسلات للمستخدم وطلبات الصداقة
from .serializers import UserSerializer

# FriendshipRequestSerializer


@api_view(["POST"])
# لا توجد فئات مصادقة مطلوبة لهذه العملية
@authentication_classes([])
# لا توجد أذونات مطلوبة لهذه العملية
@permission_classes([])
def signup(request):

    data = request.data
    # القيمة الافتراضية للرسالة هي نجاح
    message = "success"

    form = SignupForm(
        {
            "name": data.get("name"),
            "surname": data.get("surname"),
            "email": data.get("email"),
            "date_of_birth": data.get("date_of_birth"),
            "gender": data.get("gender"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
        }
    )

    if form.is_valid():
        # حفظ النموذج إذا كان صالحًا واسترجاع كائن المستخدم
        user = form.save()
        # تعيين حالة المستخدم على غير نشط
        user.is_active = False
        user.save()

        url = f"{settings.WEBSITE_URL}/activateemail/?email={user.email}&id={user.id}"

        send_mail(
            "Please verify your email",
            f"The url for activating your account is: {url}",
            "learncodingeasy@yahoo.com",
            [user.email],
            fail_silently=False,
        )
        # إضافة رسالة تأكيد إرسال البريد الإلكتروني
        return JsonResponse({"message": message, "email_sent": True}, safe=False)
    else:
        # JSON إذا كان النموذج غير صالح، استرجاع الأخطاء كرسالة
        message = form.errors.as_json()

    # طباعة حالة العملية (نجاح أو الأخطاء) إلى وحدة التحكم
    print(message)

    # تحتوي على حالة العملية JSON إرجاع رسالة
    return JsonResponse({"message": message}, safe=False)


# JSON إرجاع بيانات المستخدم الحالي كاستجابة
@api_view(["GET"])
def me(request):
    return JsonResponse(
        {
            "id": request.user.id,
            "name": request.user.name,
            "surname": request.user.surname,
            "email": request.user.email,
            "date_of_birth": request.user.date_of_birth,
            "gender": request.user.gender,
        }
    )

```
* Create Page [ urls.py ] Inside App Account 
```cmd
urls.py
```
```python
# Page [ facebook/facebook_django/account/urls.py ]
# URLs عشان أستخدمهم في تعريف مسارات الـ path بستورد
from django.urls import path

# Simple JWT من مكتبة TokenObtainPairView و TokenRefreshView بستورد
# login والـ token refresh عشان أستخدمهم في الـ  DRF الخاصة بالـ
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# اللى في نفس المجلد عشان أستخدم الفيوهات اللى فيه api بستورد كل حاجة من ملف
from . import api

# هنا بقوم بتعريف كل المسارات الـ
# URLs الخاصة بالـ app دي
urlpatterns = [
    # لما يتطلب loginالمسار ده بيعرض معلومات المستخدم اللى عامل
    path("me/", api.me, name="me"),
    # المسار ده مسئول عن عملية تسجيل حساب جديد
    path("signup/", api.signup, name="signup"),
    # tokens (access و refresh) وإصدار الـ login المسار ده مسئول عن عملية الـ
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    # refresh token باستخدام الـ access token المسار ده مسئول عن تجديد الـ
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
```
```python
# Page [ facebook/facebook_django/facebook_django/urls.py ]
# djangoمن admin بعمل استيراد لـ
# Django عشان اقدر أستخدم لوحة التحكم الخاصة بـ
from django.contrib import admin

# URLs عشان أستخدمهم في تعريف مسارات الـ path و include بستورد
from django.urls import path, include

# بستورد الإعدادات
# `settings` و`static`
# عشان أستخدمهم في إضافة مسارات الملفات الثابتة زي الصور
from django.conf import settings
from django.conf.urls.static import static

# بستورد الفيو اللى هستخدمه لتفعيل الإيميل
from account.views import activateemail

# هنا بقوم بتعريف كل المسارات الـ
# URLs اللي الموقع هيستخدمها
urlpatterns = [
    # include وبستخدم /api/،و اللى كل حاجة فيه هتبقى تحت API مسار الـ
    # account اللى اسمها app عشان أضيف كل المسارات الخاصة بالـ
    path("api/", include("account.urls")),
    # اللي هيكون شغال لما حد يضغط على لينك التفعيل في الإيميل activateemail مسار الـ
    path("activateemail/", activateemail, name="activateemail"),
    # Django اللى بيدخلني على لوحة التحكم بتاعة admin المسار الخاص بالـ
    path("admin/", admin.site.urls),
    # ده لإضافة مسارات الملفات الثابتة زي الصور،
    #  وبيبقى شغال بس لما الموقع بيكون في وضع التطوير (development)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

-  🛠️ جاهز migration عشان يبقى في ملف models أمر ده بيعمل تحضير للتعديلات اللى حصلت في الـ 
```cmd
python manage.py makemigrations
```
- 💾 على الداتابيس migrations أمر ده بيطبق التعديلات اللي اتحضرت في ملفات الـ 
```cmd
python manage.py migrate
```
- عشان تقدر تجرب المشروع على جهازك local server وصف: 🚀 أمر ده بيشغل الـ 
```cmd
python manage.py runserver
```
__________________________________________________
__________________________________________________
__________________________________________________
__________________________________________________
__________________________________________________
__________________________________________________
__________________________________________________
__________________________________________________
__________________________________________________

### 10 Create Vue Project
```
npm create vue@latest
```
__________________________________________________

### 11 Choose Vite [ Project name & Select a framework ]
```
√ Project name: ... facebook_vue
√ Add TypeScript? ... No / Yes
√ Add JSX Support? ... No / Yes
√ Add Vue Router for Single Page Application development? ... No / Yes
√ Add Pinia for state management? ... No / Yes
√ Add Vitest for Unit Testing? ... No / Yes
√ Add an End-to-End Testing Solution? » No
√ Add ESLint for code quality? ... No / Yes
√ Add Prettier for code formatting? ... No / Yes
√ Add Vue DevTools 7 extension for debugging? (experimental) ... No / Yes

Scaffolding project in E:\Projects\Facebook\facebook_vue...

Done. Now run:
  cd facebook_vue
  npm install
  npm run format
  npm run dev
```
__________________________________________________

### 12 Go To Project [ Install & Run Dev ]
```
cd facebook_vue
npm install
npm run format
npm run build
npm run dev
```

__________________________________________________
### 13  Install Vue Libraries [ 1 - Tailwind | 2 - PrimeVue | 3 - scss | 4 - Axios | 5 - Font Awesome | 6 - Pwa | 7 -  | 8 - | 9 - |  ]
```
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

npm install primevue primeicons
npm install @primevue/themes

npm install -D sass

npm install axios

npm i --save @fortawesome/fontawesome-svg-core @fortawesome/vue-fontawesome@latest @fortawesome/vue-fontawesome@prerelease @fortawesome/free-solid-svg-icons @fortawesome/free-brands-svg-icons @fortawesome/free-regular-svg-icons

npm install -D vite-plugin-pwa

npm i swiper
```
__________________________________________________

### 14 Configure Tailwind
* tailwind.config.js
```js
// Page [ facebook/facebook_vue/tailwind.config.js ]
content: [
"./index.html",
"./src/**/*.{vue,js,ts,jsx,tsx}",
],
```
* style.css
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

__________________________________________________

### 15 Import Font Awesome
```js
// Page [ facebook/facebook_vue/src/main.js ]
// Font Awesome
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
// Add Free Icons Styles To SVG Core
library.add(fas, far, fab);

// eslint-disable-next-line vue/multi-word-component-names
app.component("fa", FontAwesomeIcon)
```


__________________________________________________
### 16 Add Pwa To Vue 
```js
// Page [ facebook/facebook_vue/vite.config.js ]

import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// For Pwa
// https://vite-pwa-org.netlify.app/guide/
import { VitePWA } from 'vite-plugin-pwa'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    // For Pwa
    VitePWA({ 
      // ليكون "تحديث تلقائي" Service Worker إعداد نوع التسجيل لـ 
      registerType: 'autoUpdate',
      workbox: {
        // Service Worker أنماط الملفات التي سيتم تخزينها مسبقًا في الـ 
        globPatterns: ['**/*.{js,css,html,ico,png,svg}'],
        // يتحكم في كل العملاء الحاليين دون الحاجة لإعادة التحميل Service Worker يجعل الـ 
        clientsClaim: true,
         //  Service Worker يتجاوز فترة الانتظار وينشط الـ 
        skipWaiting: true,
        // ولا يُنظفها Cache يُبقي على النسخ القديمة من الـ 
        cleanupOutdatedCaches: false,
        // للعمل أثناء عدم الاتصال بالإنترنت Google يتيح تحليلات 
        offlineGoogleAnalytics: true,
        // (الخرائط المصدرية) لتسهيل تتبع الأخطاء sourcemaps تفعيل 
        sourcemap: true,
        runtimeCaching: [
          {
            // أو نوع الطلبات التي سيتم تخزينها أثناء التشغيل URL تحديد نمط 
            urlPattern: ({ request }) => 
              request.destination === 'document' || 
              request.destination === 'script' || 
              request.destination === 'style' || 
              request.destination === 'image' || 
              request.destination === 'font',
            // استراتيجية التخزين المؤقت التي تعرض النسخة المخزنة مؤقتًا أثناء الحصول على نسخة جديدة من الشبكة
            handler: 'StaleWhileRevalidate',
            options: {
              // المستخدم لتخزين هذه الملفات (cache) اسم الكاش 
              cacheName: 'assets-cache',
              expiration: {
                // عدد الملفات التي يمكن تخزينها في الكاش كحد أقصى
                maxEntries: 100,
                // مدة التخزين المؤقت لهذه الملفات (30 يومًا)
                maxAgeSeconds: 60 * 60 * 24 * 30 
              }
            }
          }
        ],
      },
      devOptions: {
         // PWA تمكين خيارات التطوير أثناء تطوير 
        enabled: true
      },
      injectRegister: 'auto',
      includeAssets: ["**/*"],
      manifest: {
        name: 'Facebook',
        short_name: 'Facebook',
        description: 'My Awesome App Facebook',
        theme_color: '#ffffff',
        icons: [
                {
                  "src": "./images/icons/facebook_icon_72x72.png",
                  "type": "image/png",
                  "sizes": "72x72",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_96x96.png",
                  "type": "image/png",
                  "sizes": "96x96",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_128x128.png",
                  "type": "image/png",
                  "sizes": "128x128",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_144x144.png",
                  "type": "image/png",
                  "sizes": "144x144",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_152x152.png",
                  "type": "image/png",
                  "sizes": "152x152",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_192x192.png",
                  "type": "image/png",
                  "sizes": "192x192",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_384x384.png",
                  "type": "image/png",
                  "sizes": "384x384",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_512x512.png",
                  "type": "image/png",
                  "sizes": "512x512",
                  "purpose": "any maskable"
                }
              ],
              screenshots: [
                {
                  "src": "./images/screenshots/screenshots.png",
                  "sizes": "640x480",
                  "type": "image/png",
                  "form_factor": "wide"
                  // "form_factor": "narrow"
                }
              ]
      },
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
```
* Add Image Inside Public
```
├── public/
│   ├── images/
│   |   ├── icons/
│   │   |   ├── 🖼️ facebook_icon_72x72.png
│   │   |   ├── 🖼️ facebook_icon_96x96.png
│   │   |   ├── 🖼️ facebook_icon_128x128.png
│   │   |   ├── 🖼️ facebook_icon_144x144.png
│   │   |   ├── 🖼️ facebook_icon_152x152.png
│   │   |   ├── 🖼️ facebook_icon_192x192.png
│   │   |   ├── 🖼️ facebook_icon_384x384.png
│   │   |   ├── 🖼️ facebook_icon_512x512.png
│   |   ├── screenshots/
│   │   |   ├── 🖼️ screenshots.png
```
__________________________________________________

### 17 Setup Axios
```js
// Axios
// axios استيراد
import axios from "axios"
axios.defaults.baseURL = "http://127.0.0.1:8000"

app.use(router, axios)
```

__________________________________________________
### 18 Setup PrimeVue
```js
// Page [ facebook/facebook_vue/src/main.js ]
// Prime Vue 
import PrimeVue from "primevue/config";
// Popup
import ConfirmationService from 'primevue/confirmationservice'
import DialogService from 'primevue/dialogservice'
// Button
import Button from 'primevue/button';
// Form
import Fluid from 'primevue/fluid';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import FloatLabel from 'primevue/floatlabel';
import Checkbox from 'primevue/checkbox';
import DatePicker from 'primevue/datepicker';
import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';
// Menu
import Menubar from 'primevue/menubar';
import TieredMenu from 'primevue/tieredmenu';
// Image
import Avatar from 'primevue/avatar';
import AvatarGroup from 'primevue/avatargroup';
// Popup
import Popover from 'primevue/popover';
import Dialog from 'primevue/dialog';
// Card
import Card from 'primevue/card';
// Theme
import Noir from './presets/Noir.js';
import ThemeSwitcher from './components/Theme/ThemeSwitcher.vue';
// Toast
import Toast from 'primevue/toast';
import ToastService from 'primevue/toastservice';
// Message
import Message from 'primevue/message';
// PrimeIcons أيقونات 
import 'primeicons/primeicons.css'
import 'tailwindcss/tailwind.css'

// Prime Vue 
app.use(PrimeVue, {
  theme: {
      preset: Noir,
      options: {
          prefix: 'p',
          darkModeSelector: '.p-dark',
          cssLayer: false,
      }
  }
});
app.use(ConfirmationService);
app.use(DialogService);
// Prime Theme Switcher
app.component('ThemeSwitcher', ThemeSwitcher);
// Prime Button
app.component('prime_button', Button);
// Prime Form
app.component('prime_fluid', Fluid);
app.component('prime_input_text', InputText);
app.component('prime_input_password', Password);
app.component('prime_float_label', FloatLabel);
app.component('prime_check_box', Checkbox);
app.component('prime_date_picker', DatePicker);
app.component('prime_input_group', InputGroup);
app.component('prime_input_group_addon', InputGroupAddon);
// Prime Menu
app.component('prime_menubar', Menubar);
app.component('prime_tiered_menu', TieredMenu);
app.component('prime_avatar', Avatar);
app.component('prime_avatar_group', AvatarGroup);
app.component('prime_popover', Popover);
app.component('prime_card', Card);
app.component('prime_dialog', Dialog);
// Toast
// app.use(Toast);
app.component('prime_toast', Toast);
app.use(ToastService);
// Message
// app.use(Message);
app.component('prime_message', Message);
```
* Setup Prime Theme
- Create Page [ primeTheme.js ] Inside stores
```js
// Page [ facebook/facebook_vue/src/stores/primeTheme.js ]

import { reactive } from 'vue';
export default {
    install: (app) => {
        const _appState = reactive({ theme: 'Aura', darkTheme: false });
        app.config.globalProperties.$appState = _appState;
    }
};
```
- Create Page [ ThemeSwitcher.vue ] components/Theme/
```html
<template>
  <span class="">
    <ul class="flex list-none m-0 p-0 gap-2 items-center">
      <li>
        <button
          type="button"
          class="inline-flex w-8 h-8 p-0 items-center justify-center surface-0 dark:surface-800 border border-surface-200 dark:border-surface-600 rounded-full"
          @click="onThemeToggler"
        >
          <i :class="`dark:text-white pi ${iconClass}`" />
        </button>
      </li>
    </ul>
  </span>
</template>
```
```js
<script>
  import { updatePreset, updateSurfacePalette } from '@primevue/themes'
  
  export default {
    data() {
      return {
        iconClass: 'pi-moon',
        selectedPrimaryColor: 'noir',
        selectedSurfaceColor: null
      }
    },
    methods: {
      onThemeToggler() {
        const root = document.getElementsByTagName('html')[0]
        root.classList.toggle('p-dark')
        this.iconClass = this.iconClass === 'pi-moon' ? 'pi-sun' : 'pi-moon'
      },
  
      updateColors(type, color) {
        if (type === 'primary') this.selectedPrimaryColor = color.name
        else if (type === 'surface') this.selectedSurfaceColor = color.name
  
        this.applyTheme(type, color)
      },
      applyTheme(type, color) {
        if (type === 'primary') {
          updatePreset(this.getPresetExt())
        } else if (type === 'surface') {
          updateSurfacePalette(color.palette)
        }
      },
      onRippleChange(value) {
        this.$primevue.config.ripple = value
      }
    },
    computed: {
      rippleActive() {
        return this.$primevue.config.ripple
      }
    }
  }
</script>
```
* Setup Prime Theme
- Create Page [ Noir.js ] Inside src/presets 
```js
import { definePreset } from '@primevue/themes';
import Aura from '@primevue/themes/aura';

const Noir = definePreset(Aura, {
    semantic: {
        primary: {
        50: '{surface.50}',
        100: '{surface.100}',
        200: '{surface.200}',
        300: '{surface.300}',
        400: '{surface.400}',
        500: '{surface.500}',
        600: '{surface.600}',
        700: '{surface.700}',
        800: '{surface.800}',
        900: '{surface.900}',
        950: '{surface.950}'
        },
        colorScheme: {
            light: {
                primary: {
                color: '{primary.950}',
                contrastColor: '#ffffff',
                hoverColor: '{primary.900}',
                activeColor: '{primary.800}'
                },
                highlight: {
                background: '{primary.950}',
                focusBackground: '{primary.700}',
                color: '#ffffff',
                focusColor: '#ffffff'
                },
            },
            dark: {
                primary: {
                color: '{primary.50}',
                contrastColor: '{primary.950}',
                hoverColor: '{primary.100}',
                activeColor: '{primary.200}'
                },
                highlight: {
                background: '{primary.50}',
                focusBackground: '{primary.300}',
                color: '{primary.950}',
                focusColor: '{primary.950}'
                }
            }
        }
    }
});

export default Noir;

```
__________________________________________________
### 19 Setup Vuex
* Creat Page [ user.js ] Inside Store
```js
// Page [ facebook/facebook_vue/src/stores/user.js ]
// `pinia`من مكتبة `defineStore` استيراد 
import { defineStore } from 'pinia'
// HTTP للتعامل مع طلبات `axios` استيراد 
import axios from 'axios'
// `defineStore` باستخدام `useUserStore` تعريف وتصدير
export const useUserStore = defineStore({
    // (store) تعيين معرّف فريد للمخزن 
    id: 'user',
    // (store) تعيين معرّف فريد للمخزن 
    state: () => ({
        // تحديد الخصائص الافتراضية للمستخدم
        user: {
            // هل المستخدم مسجل دخول أم لا
            isAuthenticated: false, 
            // معرّف المستخدم
            id: null,
            // اسم المستخدم
            name: null,
            // لقب المستخدم
            surname: null,
            // بريد المستخدم الإلكتروني
            email: null,
            // تاريخ ميلاد المستخدم
            date_of_birth: null,
            // رمز الوصول (Access Token)
            access: null,
            // رمز التجديد (Refresh Token)
            refresh: null,
            // personal_phone: null, // هاتف المستخدم الشخصي (غير مستخدم حالياً)
            // public_phone: null,   // هاتف المستخدم العام (غير مستخدم حالياً)
            // address: null,        // عنوان المستخدم (غير مستخدم حالياً)
            // workplace_company: null, // شركة العمل (غير مستخدم حالياً)
            // workplace_position: null, // منصب العمل (غير مستخدم حالياً)
            // workplace_city_town: null, // مدينة أو بلدة العمل (غير مستخدم حالياً)
            // workplace_description: null, // وصف العمل (غير مستخدم حالياً)
            // workplace_time_period: null, // فترة العمل (غير مستخدم حالياً)
            // avatar: null,         // صورة المستخدم الرمزية (غير مستخدم حالياً)
            // cover: null           // صورة غلاف المستخدم (غير مستخدم حالياً)
        }
    }),
    // (store) في المخزن (actions) تعريف الإجراءات 
    actions: {
        // إجراء لتهيئة المخزن واستعادة بيانات المستخدم من التخزين المحلي
        initStore() {
            // console.log('initStore', localStorage.getItem('user.access'))
            // إذا كان هناك رمز وصول محفوظ في التخزين المحلي
            if (localStorage.getItem('user.access')) {
                console.log('User has access!')
                // تعيين خصائص المستخدم باستخدام البيانات المخزنة محلياً
                this.user.isAuthenticated = true
                this.user.id = localStorage.getItem('user.id')
                this.user.name = localStorage.getItem('user.name')
                this.user.surname = localStorage.getItem('user.surname')
                this.user.email = localStorage.getItem('user.email')
                this.user.date_of_birth = localStorage.getItem('user.date_of_birth')
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                // this.user.personal_phone = localStorage.getItem('user.personal_phone')
                // this.user.public_phone = localStorage.getItem('user.public_phone')
                // this.user.address = localStorage.getItem('user.address')
                // this.user.workplace_company = localStorage.getItem('user.workplace_company')
                // this.user.workplace_position = localStorage.getItem('user.workplace_position')
                // this.user.workplace_city_town = localStorage.getItem('user.workplace_city_town')
                // this.user.workplace_description = localStorage.getItem('user.workplace_description')
                // this.user.workplace_time_period = localStorage.getItem('user.workplace_time_period')
                // this.user.avatar = localStorage.getItem('user.avatar')
                // this.user.cover = localStorage.getItem('user.cover')
                // تحديث رمز الوصول
                this.refreshToken()
                // console.log('Initialized user:', this.user)
            }
        },
        // إجراء لتعيين رموز الوصول والتجديد في المخزن وفي التخزين المحلي
        setToken(data) {
            console.log('setToken', data)
            // تعيين الرموز في المخزن
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true
            // تخزين الرموز في التخزين المحلي
            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)

            console.log('user.access: ', localStorage.getItem('user.access'))
        },
        // إجراء لإزالة الرموز وتفريغ بيانات المستخدم
        removeToken() {
            console.log('removeToken')
            // إعادة تعيين بيانات المستخدم إلى قيمها الافتراضية
            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = false
            this.user.id = null
            this.user.name = null
            this.user.surname = null
            this.user.email = null
            this.user.date_of_birth = null
            // this.user.personal_phone = null
            // this.user.public_phone = null
            // this.user.address = null
            // this.user.workplace_company = null
            // this.user.workplace_position = null
            // this.user.workplace_city_town = null
            // this.user.workplace_description = null
            // this.user.workplace_time_period = null
            // this.user.avatar = null
            // this.user.cover = null
            // إزالة البيانات المخزنة في التخزين المحلي
            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.surname', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.date_of_birth', '')
            // localStorage.setItem('user.personal_phone', '')
            // localStorage.setItem('user.public_phone', '')
            // localStorage.setItem('user.address', '')
            // localStorage.setItem('user.workplace_company', '')
            // localStorage.setItem('user.workplace_position', '')
            // localStorage.setItem('user.workplace_city_town', '')
            // localStorage.setItem('user.workplace_description', '')
            // localStorage.setItem('user.workplace_time_period', '')
            // localStorage.setItem('user.avatar', '')
            // localStorage.setItem('user.cover', '')
        },
        // إجراء لتحديث بيانات المستخدم وتخزينها في التخزين المحلي
        setUserInfo(user) {
            console.log('setUserInfo', user)
            // تعيين بيانات المستخدم في المخزن
            this.user.id = user.id
            this.user.name = user.name
            this.user.surname = user.surname
            this.user.email = user.email
            this.user.date_of_birth = user.date_of_birth
            // this.user.personal_phone = user.personal_phone
            // this.user.public_phone = user.public_phone
            // this.user.address = user.address
            // this.user.workplace_company = user.workplace_company
            // this.user.workplace_position = user.workplace_position
            // this.user.workplace_city_town = user.workplace_city_town
            // this.user.workplace_description = user.workplace_description
            // this.user.workplace_time_period = user.workplace_time_period
            // this.user.avatar = user.avatar
            // this.user.cover = user.cover

            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.name', this.user.name)
            localStorage.setItem('user.surname', this.user.surname)
            localStorage.setItem('user.email', this.user.email)
            localStorage.setItem('user.date_of_birth', this.user.date_of_birth)
            // localStorage.setItem('user.personal_phone', this.user.personal_phone)
            // localStorage.setItem('user.public_phone', this.user.public_phone)
            // localStorage.setItem('user.address', this.user.address)
            // localStorage.setItem('user.workplace_company', this.user.workplace_company)
            // localStorage.setItem('user.workplace_position', this.user.workplace_position)
            // localStorage.setItem('user.workplace_city_town', this.user.workplace_city_town)
            // localStorage.setItem('user.workplace_description', this.user.workplace_description)
            // localStorage.setItem('user.workplace_time_period', this.user.workplace_time_period)
            // localStorage.setItem('user.avatar', this.user.avatar)
            // localStorage.setItem('user.cover', this.user.cover)
            // console.log('User', this.user)
        },
        // إجراء لتحديث رمز الوصول باستخدام رمز التجديد
        refreshToken() {
            // لتحديث رمز الوصول HTTP إرسال طلب 
            axios.post('/api/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    // تحديث رمز الوصول في المخزن والتخزين المحلي
                    this.user.access = response.data.access
                    localStorage.setItem('user.access', response.data.access)
                    // للطلبات المستقبلية Authorization تعيين رأس 
                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error)=>{
                    // في حالة وجود خطأ، إزالة الرموز
                    console.log(error)
                    this.removeToken()
                })
        },
    }
})
```

__________________________________________________
### 20 Edite Page [ App ]
```js
<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  
  import { ref } from 'vue'
  //
  import { onMounted } from 'vue'
  import { useUserStore } from '@/stores/user'
  import { useRouter } from 'vue-router'
  
  const userStore = useUserStore()
  userStore.initStore()
  const router = useRouter()
  
  onMounted(() => {
    // Perform any necessary operations on component mount
    if (!userStore.user.access) {
      console.log('User Data: ', userStore.user.access)
      // Replace '/login' with your actual login route
      router.push('/login')
    } else {
      // Set default Authorization header for axios
      axios.defaults.headers.common['Authorization'] = `Bearer ${userStore.user.access}`
      // console.log('User Data: ', userStore.user)
    }
  })
  
  // For Toggle Theme
  const op = ref(null)
  const toggle = (event) => {
    op.value.toggle(event)
  }
  // Log Out
  let logout = () => {
    console.log('User Log out')
    userStore.removeToken()
    // توجيه المستخدم إلى صفحة تسجيل الدخول
    setTimeout(() => {
      router.push('/login').then(() => {})
    }, 10)
  }
  </script>
```
```html
<template>
  <!-- Header -->
  <prime_card class="header_wrapper" v-if="userStore.user.isAuthenticated">
    <template #content>
      <header class="card shadow-md fixed top-0 left-0 right-0">
        <div class="container mx-auto flex justify-between items-center">
          <!-- Left Section (Logo and Search Bar) -->
          <div class="header_left_section flex items-center space-x-1 basis-1/4">
            <!-- Logo -->
            <RouterLink to="/" class="logo">
              <!-- <i class="fab fa-facebook fa-fw"></i> -->
              <fa :icon="['fab', 'facebook']" />
            </RouterLink>
            <!-- Search Bar -->
            <div class="search_bar w-full">
              <span class="icon">
                <!-- <i class="fas fa-search fa-fw"></i> -->
                <fa :icon="['fas', 'search']" />
              </span>
              <input
                type="text"
                class="w-full p-2 rounded-full focus:outline-none"
                placeholder="Search Facebook"
              />
            </div>
          </div>

          <!-- Center Section (Navigation Icons) -->
          <div class="header_center_section flex items-center justify-center space-x-1 basis-1/2">
            <RouterLink to="/" class="header_center_section_link_home grow">
              <span class="header_center_section_link_home_span">
                <svg
                  viewBox="0 0 24 24"
                  width="24"
                  height="24"
                  fill="currentColor"
                  class="header_center_section_link_home_svg"
                >
                  <path
                    d="M9.464 1.286C10.294.803 11.092.5 12 .5c.908 0 1.707.303 2.537.786.795.462 1.7 1.142 2.815 1.977l2.232 1.675c1.391 1.042 2.359 1.766 2.888 2.826.53 1.059.53 2.268.528 4.006v4.3c0 1.355 0 2.471-.119 3.355-.124.928-.396 1.747-1.052 2.403-.657.657-1.476.928-2.404 1.053-.884.119-2 .119-3.354.119H7.93c-1.354 0-2.471 0-3.355-.119-.928-.125-1.747-.396-2.403-1.053-.656-.656-.928-1.475-1.053-2.403C1 18.541 1 17.425 1 16.07v-4.3c0-1.738-.002-2.947.528-4.006.53-1.06 1.497-1.784 2.888-2.826L6.65 3.263c1.114-.835 2.02-1.515 2.815-1.977zM10.5 13A1.5 1.5 0 0 0 9 14.5V21h6v-6.5a1.5 1.5 0 0 0-1.5-1.5h-3z"
                  ></path>
                </svg>
              </span>
            </RouterLink>
            <RouterLinka to="/" class="text-white text-xl grow header_center_section_link_friends">
              <span class="header_center_section_link_friends_span">
                <svg
                  viewBox="0 0 24 24"
                  width="24"
                  height="24"
                  fill="currentColor"
                  class="header_center_section_link_friends_svg"
                >
                  <path
                    d="M12.496 5a4 4 0 1 1 8 0 4 4 0 0 1-8 0zm4-2a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm-9 2.5a4 4 0 1 0 0 8 4 4 0 0 0 0-8zm-2 4a2 2 0 1 1 4 0 2 2 0 0 1-4 0zM5.5 15a5 5 0 0 0-5 5 3 3 0 0 0 3 3h8.006a3 3 0 0 0 3-3 5 5 0 0 0-5-5H5.5zm-3 5a3 3 0 0 1 3-3h4.006a3 3 0 0 1 3 3 1 1 0 0 1-1 1H3.5a1 1 0 0 1-1-1zm12-9.5a5.04 5.04 0 0 0-.37.014 1 1 0 0 0 .146 1.994c.074-.005.149-.008.224-.008h4.006a3 3 0 0 1 3 3 1 1 0 0 1-1 1h-3.398a1 1 0 1 0 0 2h3.398a3 3 0 0 0 3-3 5 5 0 0 0-5-5H14.5z"
                  ></path>
                </svg>
              </span>
            </RouterLinka>
            <RouterLink to="/" class="text-white text-xl grow header_center_section_link_videos">
              <span class="header_center_section_link_videos_span">
                <svg
                  viewBox="0 0 24 24"
                  width="24"
                  height="24"
                  fill="currentColor"
                  class="header_center_section_link_videos_svg"
                >
                  <path
                    d="M10.996 8.132A1 1 0 0 0 9.5 9v4a1 1 0 0 0 1.496.868l3.5-2a1 1 0 0 0 0-1.736l-3.5-2z"
                  ></path>
                  <path
                    d="M14.573 2H9.427c-1.824 0-3.293 0-4.45.155-1.2.162-2.21.507-3.013 1.31C1.162 4.266.817 5.277.655 6.477.5 7.634.5 9.103.5 10.927v.146c0 1.824 0 3.293.155 4.45.162 1.2.507 2.21 1.31 3.012.802.803 1.813 1.148 3.013 1.31C6.134 20 7.603 20 9.427 20h5.146c1.824 0 3.293 0 4.45-.155 1.2-.162 2.21-.507 3.012-1.31.803-.802 1.148-1.813 1.31-3.013.155-1.156.155-2.625.155-4.449v-.146c0-1.824 0-3.293-.155-4.45-.162-1.2-.507-2.21-1.31-3.013-.802-.802-1.813-1.147-3.013-1.309C17.866 2 16.397 2 14.573 2zM3.38 4.879c.369-.37.887-.61 1.865-.741C6.251 4.002 7.586 4 9.5 4h5c1.914 0 3.249.002 4.256.138.978.131 1.496.372 1.865.74.37.37.61.888.742 1.866.135 1.007.137 2.342.137 4.256 0 1.914-.002 3.249-.137 4.256-.132.978-.373 1.496-.742 1.865-.369.37-.887.61-1.865.742-1.007.135-2.342.137-4.256.137h-5c-1.914 0-3.249-.002-4.256-.137-.978-.132-1.496-.373-1.865-.742-.37-.369-.61-.887-.741-1.865C2.502 14.249 2.5 12.914 2.5 11c0-1.914.002-3.249.138-4.256.131-.978.372-1.496.74-1.865zM8 21.5a1 1 0 1 0 0 2h8a1 1 0 1 0 0-2H8z"
                  ></path>
                </svg>
              </span>
            </RouterLink>
            <RouterLink
              to="/"
              class="text-white text-xl grow header_center_section_link_marketplace"
            >
              <span class="header_center_section_link_marketplace_span">
                <svg
                  viewBox="0 0 24 24"
                  width="24"
                  height="24"
                  fill="currentColor"
                  class="header_center_section_link_marketplace_svg"
                >
                  <path
                    d="M1.588 3.227A3.125 3.125 0 0 1 4.58 1h14.84c1.38 0 2.597.905 2.993 2.227l.816 2.719a6.47 6.47 0 0 1 .272 1.854A5.183 5.183 0 0 1 22 11.455v4.615c0 1.355 0 2.471-.119 3.355-.125.928-.396 1.747-1.053 2.403-.656.657-1.475.928-2.403 1.053-.884.12-2 .119-3.354.119H8.929c-1.354 0-2.47 0-3.354-.119-.928-.125-1.747-.396-2.403-1.053-.657-.656-.929-1.475-1.053-2.403-.12-.884-.119-2-.119-3.354V11.5l.001-.045A5.184 5.184 0 0 1 .5 7.8c0-.628.092-1.252.272-1.854l.816-2.719zM10 21h4v-3.5a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5V21zm6-.002c.918-.005 1.608-.025 2.159-.099.706-.095 1.033-.262 1.255-.485.223-.222.39-.55.485-1.255.099-.735.101-1.716.101-3.159v-3.284a5.195 5.195 0 0 1-1.7.284 5.18 5.18 0 0 1-3.15-1.062A5.18 5.18 0 0 1 12 13a5.18 5.18 0 0 1-3.15-1.062A5.18 5.18 0 0 1 5.7 13a5.2 5.2 0 0 1-1.7-.284V16c0 1.442.002 2.424.1 3.159.096.706.263 1.033.486 1.255.222.223.55.39 1.255.485.551.074 1.24.094 2.159.1V17.5a2.5 2.5 0 0 1 2.5-2.5h3a2.5 2.5 0 0 1 2.5 2.5v3.498zM4.581 3c-.497 0-.935.326-1.078.802l-.815 2.72A4.45 4.45 0 0 0 2.5 7.8a3.2 3.2 0 0 0 5.6 2.117 1 1 0 0 1 1.5 0A3.19 3.19 0 0 0 12 11a3.19 3.19 0 0 0 2.4-1.083 1 1 0 0 1 1.5 0A3.2 3.2 0 0 0 21.5 7.8c0-.434-.063-.865-.188-1.28l-.816-2.72A1.125 1.125 0 0 0 19.42 3H4.58z"
                  ></path>
                </svg>
              </span>
            </RouterLink>
            <RouterLink to="/" class="text-white text-xl grow header_center_section_link_groups">
              <span class="header_center_section_link_groups_span">
                <svg
                  viewBox="0 0 24 24"
                  width="24"
                  height="24"
                  fill="currentColor"
                  class="header_center_section_link_groups_svg"
                >
                  <path
                    d="M12 5a4 4 0 1 0 0 8 4 4 0 0 0 0-8zm-2 4a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"
                  ></path>
                  <path
                    d="M12 .5C5.649.5.5 5.649.5 12S5.649 23.5 12 23.5 23.5 18.351 23.5 12 18.351.5 12 .5zM2.5 12c0-.682.072-1.348.209-1.99a2 2 0 0 1 0 3.98A9.539 9.539 0 0 1 2.5 12zm4 0a4.001 4.001 0 0 0-3.16-3.912A9.502 9.502 0 0 1 12 2.5a9.502 9.502 0 0 1 8.66 5.588 4.001 4.001 0 0 0 0 7.824 9.514 9.514 0 0 1-1.755 2.613A5.002 5.002 0 0 0 14 14.5h-4a5.002 5.002 0 0 0-4.905 4.025 9.515 9.515 0 0 1-1.755-2.613A4.001 4.001 0 0 0 6.5 12zm13 0a2 2 0 0 1 1.791-1.99 9.538 9.538 0 0 1 0 3.98A2 2 0 0 1 19.5 12zm-2.51 8.086A9.455 9.455 0 0 1 12 21.5c-1.83 0-3.54-.517-4.99-1.414a1.004 1.004 0 0 1-.01-.148V19.5a3 3 0 0 1 3-3h4a3 3 0 0 1 3 3v.438a1 1 0 0 1-.01.148z"
                  ></path>
                </svg>
              </span>
            </RouterLink>
          </div>
          <!--  -->
          <div class="toggle_header_left_section">
            <span class="icon"> <i class="fas fa-bars"></i> </span>
          </div>
          <!-- Right Section (Profile and Notifications) -->
          <div class="header_right_section flex items-center justify-end space-x-1 basis-1/4">
            <RouterLinka to="/" class="header_right_section_link">
              <span class="header_right_section_link_span">
                <svg
                  viewBox="0 0 24 24"
                  width="20"
                  height="20"
                  fill="currentColor"
                  class="header_right_section_link_svg"
                >
                  <path
                    d="M18.5 1A1.5 1.5 0 0 0 17 2.5v3A1.5 1.5 0 0 0 18.5 7h3A1.5 1.5 0 0 0 23 5.5v-3A1.5 1.5 0 0 0 21.5 1h-3zm0 8a1.5 1.5 0 0 0-1.5 1.5v3a1.5 1.5 0 0 0 1.5 1.5h3a1.5 1.5 0 0 0 1.5-1.5v-3A1.5 1.5 0 0 0 21.5 9h-3zm-16 8A1.5 1.5 0 0 0 1 18.5v3A1.5 1.5 0 0 0 2.5 23h3A1.5 1.5 0 0 0 7 21.5v-3A1.5 1.5 0 0 0 5.5 17h-3zm8 0A1.5 1.5 0 0 0 9 18.5v3a1.5 1.5 0 0 0 1.5 1.5h3a1.5 1.5 0 0 0 1.5-1.5v-3a1.5 1.5 0 0 0-1.5-1.5h-3zm8 0a1.5 1.5 0 0 0-1.5 1.5v3a1.5 1.5 0 0 0 1.5 1.5h3a1.5 1.5 0 0 0 1.5-1.5v-3a1.5 1.5 0 0 0-1.5-1.5h-3zm-16-8A1.5 1.5 0 0 0 1 10.5v3A1.5 1.5 0 0 0 2.5 15h3A1.5 1.5 0 0 0 7 13.5v-3A1.5 1.5 0 0 0 5.5 9h-3zm0-8A1.5 1.5 0 0 0 1 2.5v3A1.5 1.5 0 0 0 2.5 7h3A1.5 1.5 0 0 0 7 5.5v-3A1.5 1.5 0 0 0 5.5 1h-3zm8 0A1.5 1.5 0 0 0 9 2.5v3A1.5 1.5 0 0 0 10.5 7h3A1.5 1.5 0 0 0 15 5.5v-3A1.5 1.5 0 0 0 13.5 1h-3zm0 8A1.5 1.5 0 0 0 9 10.5v3a1.5 1.5 0 0 0 1.5 1.5h3a1.5 1.5 0 0 0 1.5-1.5v-3A1.5 1.5 0 0 0 13.5 9h-3z"
                  ></path>
                </svg>
              </span>
            </RouterLinka>
            <RouterLinka to="/" class="header_right_section_link">
              <span class="header_right_section_link_span">
                <svg
                  viewBox="0 0 12 13"
                  width="20"
                  height="20"
                  fill="currentColor"
                  class="header_right_section_link_svg"
                >
                  <g fill-rule="evenodd" transform="translate(-450 -1073)">
                    <path
                      d="m459.603 1077.948-1.762 2.851a.89.89 0 0 1-1.302.245l-1.402-1.072a.354.354 0 0 0-.433.001l-1.893 1.465c-.253.196-.583-.112-.414-.386l1.763-2.851a.89.89 0 0 1 1.301-.245l1.402 1.072a.354.354 0 0 0 .434-.001l1.893-1.465c.253-.196.582.112.413.386M456 1073.5c-3.38 0-6 2.476-6 5.82 0 1.75.717 3.26 1.884 4.305.099.087.158.21.162.342l.032 1.067a.48.48 0 0 0 .674.425l1.191-.526a.473.473 0 0 1 .32-.024c.548.151 1.13.231 1.737.231 3.38 0 6-2.476 6-5.82 0-3.344-2.62-5.82-6-5.82"
                    ></path>
                  </g>
                </svg>
              </span>
            </RouterLinka>
            <RouterLink to="/" class="header_right_section_link">
              <span class="header_right_section_link_span">
                <svg
                  viewBox="0 0 24 24"
                  width="20"
                  height="20"
                  fill="currentColor"
                  class="header_right_section_link_svg"
                >
                  <path
                    d="M3 9.5a9 9 0 1 1 18 0v2.927c0 1.69.475 3.345 1.37 4.778a1.5 1.5 0 0 1-1.272 2.295h-4.625a4.5 4.5 0 0 1-8.946 0H2.902a1.5 1.5 0 0 1-1.272-2.295A9.01 9.01 0 0 0 3 12.43V9.5zm6.55 10a2.5 2.5 0 0 0 4.9 0h-4.9z"
                  ></path>
                </svg>
              </span>
            </RouterLink>
            <!-- Avatar -->
            <prime_avatar
              image="./src/assets/image/user.png"
              size="large"
              shape="circle"
              alt="Profile Picture"
              class="w-10 h-10 rounded-full"
              @click="toggle"
              type="button"
              aria-haspopup="true"
              aria-controls="overlay_tmenu"
            />
            <!-- Popup User Option -->
            <prime_popover ref="op">
              <div class="w-[25rem]">
                <!-- User Profile -->
                <div class="div_wrapper_profile">
                  <RouterLink
                    class="flex align-middle"
                    v-if="userStore.user.id"
                    :to="{ name: 'profile', params: { id: userStore.user.id } }"
                  >
                    <span class="user_img">
                      <!-- v-if="userStore.user.avatar" -->
                      <img
                        v-if="userStore.user.avatar"
                        :src="userStore.user.avatar"
                        class="rounded-full"
                        alt=""
                      />
                      <!-- v-else  -->
                      <img v-else src="./assets/image/user.png" class="rounded-full" alt="" />
                    </span>
                    <span class="user_name">{{ userStore.user.name }}</span>
                  </RouterLink>
                </div>
                <!-- Log Out -->
                <div class="div_wrapper_logout flex align-middle cursor-pointer" @click="logout">
                  <div class="icon_logout flex justify-center align-middle">
                    <i class="pi pi-sign-out" style="font-size: 1rem" shape="circle"></i>
                  </div>
                  <button class="font-bold">Log out</button>
                </div>
                <!-- Toggle Theme -->
                <div class="flex div_wrapper_toggle_theme cursor-pointer">
                  <ThemeSwitcher />
                  <span class="font-medium mb-2">Toggle theme</span>
                </div>
              </div>
            </prime_popover>
          </div>
        </div>
      </header>
    </template>
  </prime_card>

  <prime_toast />

  <RouterView />
</template>
```
```js
<script>
  import axios from 'axios'
  
  export default {
    setup() {
      return {}
    },
    methods: {}
  }
</script>
```
__________________________________________________
### 21 Create Page [ Signup & Login ]
* Create Page [ Authentication/LoginView.vue ] Inside views/Authentication
```html
<template>
  <div class="wrapper_login_page">
    <div class="inner_login_page">
      <div class="container">
        <div class="flex justify-center align-middle w_80 m-auto">
          <div class="grid grid-cols-3 gap-4 w_95">
            <div class="wrapper_text_login col-span-2">
              <div class="inner">
                <div class="title">facebook</div>
                <div class="subtitle">
                  Facebook helps you connect and share <br />
                  with the people in your life.
                </div>
              </div>
            </div>
            <div class="wrapper_form_login shadow-2xl rounded-lg">
              <!-- Log in -->
              <form class="form_login" v-on:submit.prevent="submitFormLogin">
                <prime_card class="p-3">
                  <template #header>
                    <div class="my-5 font-bold text-3xl">Log in</div>
                  </template>
                  <template #title>
                    <prime_float_label class="mt-5">
                      <prime_input_text
                        id="emailAddress"
                        v-model="formLogin.email"
                        class="block w_100"
                      />
                      <label for="emailAddress" class="text-base">Your E-mail Address</label>
                    </prime_float_label>
                  </template>
                  <template #content>
                    <prime_float_label class="mt-5">
                      <prime_input_password
                        id="password"
                        v-model="formLogin.password"
                        :feedback="false"
                      />
                      <label for="password">password</label>
                    </prime_float_label>
                  </template>
                  <template #footer>
                    <div class="row">
                      <!-- Errors -->
                      <template v-if="errorsLogin.length > 0">
                        <prime_toast></prime_toast>
                      </template>
                      <!-- Login -->
                      <div class="mt-3">
                        <button
                          type="submit"
                          class="d_block_important mt-5 mb-3 mx-auto w_100 bg-blue-500 py-3 px-5 rounded text-white"
                          @click.prevent="submitFormLogin"
                        >
                          Log In
                        </button>
                        <a href="#" class="text-blue-600 mx-auto my-4 block text-center"
                          >Forgotten password?</a
                        >
                        <hr />
                        <!-- Button Signup -->
                        <prime_button
                          label="Create new account"
                          severity="success"
                          @click="visible = true"
                          class="d_block_important my-5 mx-auto"
                        />
                      </div>
                    </div>
                  </template>
                </prime_card>
              </form>
              <!-- Signup -->
              <div class="card flex justify-center">
                <!-- @submit.prevent="submitFormSignup" -->
                <form class="space-y-6">
                  <!-- <form class="space-y-6" @submit.prevent="submitFormSignup"> -->
                  <prime_dialog
                    v-model:visible="visible"
                    modal
                    header="Sign Up"
                    :style="{ width: '25rem' }"
                  >
                    <span class="text-surface-500 dark:text-surface-400 block mb-8"
                      >It's quick and easy.</span
                    >
                    <prime_fluid>
                      <div class="grid grid-cols-2 gap-4">
                        <!-- First name -->
                        <div>
                          <prime_input_text placeholder="First name" v-model="formSignup.name" />
                        </div>
                        <!-- Surname -->
                        <div>
                          <prime_input_text placeholder="Surname" v-model="formSignup.surname" />
                        </div>
                        <!-- Mobile number or email address -->
                        <div class="col-span-full">
                          <prime_input_text
                            placeholder="Mobile number or email address"
                            v-model="formSignup.email"
                          />
                        </div>
                        <!-- password1 -->
                        <div class="col-span-full">
                          <prime_input_password
                            placeholder="New Password"
                            v-model="formSignup.password1"
                          />
                        </div>
                        <!-- password2 -->
                        <div class="col-span-full">
                          <prime_input_password
                            placeholder="Repeat password"
                            v-model="formSignup.password2"
                          />
                        </div>
                        <!-- Date of birth -->
                        <div class="col-span-full">Date of birth</div>
                        <div class="col-span-full">
                          <div class="flex flex-col md:flex-row gap-2">
                            <!-- Day -->
                            <prime_input_group>
                              <prime_date_picker v-model="day" view="day" dateFormat="dd" />
                            </prime_input_group>
                            <!-- Month -->
                            <prime_input_group>
                              <prime_date_picker v-model="month" view="month" dateFormat="mm" />
                            </prime_input_group>
                            <!-- Year -->
                            <prime_input_group>
                              <prime_date_picker v-model="year" view="year" dateFormat="yy" />
                            </prime_input_group>
                          </div>
                        </div>
                        <!-- Gender -->
                        <div class="col-span-full">Gender</div>
                        <div class="flex flex-col md:flex-row gap-2">
                          <prime_input_group>
                            <prime_check_box
                              v-model="formSignup.gender"
                              inputId="ingredient1"
                              name="gender"
                              value="Female"
                            />
                            <label for="ingredient1" class="ml-2"> Female </label>
                          </prime_input_group>
                          <prime_input_group>
                            <prime_check_box
                              v-model="formSignup.gender"
                              inputId="ingredient2"
                              name="gender"
                              value="Male"
                            />
                            <label for="ingredient2" class="ml-2"> Male </label>
                          </prime_input_group>

                          <prime_input_group>
                            <prime_check_box
                              v-model="formSignup.gender"
                              inputId="ingredient3"
                              name="gender"
                              value="Custom"
                            />
                            <label for="ingredient3" class="ml-2"> Custom </label>
                          </prime_input_group>
                        </div>
                      </div>
                    </prime_fluid>
                    <div class="flex justify-center gap-2">
                      <button
                        type="submit"
                        class="d_block_important mt-5 mb-3 mx-auto w_50 bg-green-500 py-3 px-5 rounded text-white"
                        @click.prevent="submitFormSignup"
                      >
                        Submit
                      </button>
                    </div>
                  </prime_dialog>
                  <!-- Errors -->
                  <template v-if="errorsSignup.length > 0">
                    <prime_toast />
                  </template>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <prime_toast />
  </div>
</template>
```
```js
<script>
  import axios from 'axios'
  // eslint-disable-next-line no-unused-vars
  import { RouterLink } from 'vue-router'
  import { useUserStore } from '@/stores/user'
  export default {
    name: 'loginView',
    setup() {
      const userStore = useUserStore()
      return {
        userStore
      }
    },
    data() {
      return {
        formLogin: {
          email: '',
          password: ''
        },
        errorsLogin: [],
        // visible Signup
        visible: false,
        // Signup
        formSignup: {
          name: '',
          surname: '',
          email: '',
          date_of_birth: null,
          gender: '',
          password1: '',
          password2: ''
        },
        day: '',
        month: '',
        year: '',
        errorsSignup: []
      }
    },
    methods: {
      async submitFormLogin() {
        this.errorsLogin = []
        if (this.formLogin.email === '') {
          this.$toast.add({
            severity: 'error',
            summary: 'User Name missing',
            detail: 'Your name is missing',
            life: 3000
          })
          this.errorsLogin.push('Your e-mail is missing')
        }
        if (this.formLogin.password === '') {
          this.$toast.add({
            severity: 'error',
            summary: 'User password is missing',
            detail: 'Your password is missing',
            life: 3000
          })
          this.errorsLogin.push('Your password is missing')
        }
        if (this.errorsLogin.length === 0) {
          await axios
            .post('/api/login/', this.formLogin)
            .then((response) => {
              this.userStore.setToken(response.data)
              console.log('response.data: ', response.data)
              axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
            })
            .catch((error) => {
              console.log('error', error)
              if (error.response.data.detail) {
                // Code If True
                this.$toast.add({
                  severity: 'error',
                  summary: 'Error Message',
                  detail: `${error.response.data.detail}`,
                  life: 6000
                })
              }
  
              this.errorsLogin.push(
                'The email or password is incorrect! Or the user is not activated!'
              )
            })
        }
        if (this.errorsLogin.length === 0) {
          await axios
            .get('/api/me/')
            .then((response) => {
              this.userStore.setUserInfo(response.data)
              this.$router.push('/')
            })
            .catch((error) => {
              console.log('error', error)
            })
        }
      },
      submitFormSignup() {
        this.errorsSignup = []
  
        // استخراج اليوم، الشهر، والسنة من كائنات Date وتنسيقها
        const day = this.day.getDate().toString().padStart(2, '0')
        const month = (this.month.getMonth() + 1).toString().padStart(2, '0')
        const year = this.year.getFullYear()
  
        const formattedDate = `${year}-${month}-${day}`
        this.formSignup.date_of_birth = formattedDate
  
        if (this.formSignup.name === '') {
          this.$toast.add({
            severity: 'error',
            summary: 'User Name missing',
            detail: 'Your name is missing',
            life: 3000
          })
          this.errorsSignup.push('Your name is missing')
        }
        if (this.formSignup.surname === '') {
          this.$toast.add({
            severity: 'error',
            summary: 'User Surname missing',
            detail: 'Your Surname is missing',
            life: 3000
          })
          this.errorsSignup.push('Your surname is missing')
        }
        if (this.formSignup.email === '') {
          this.$toast.add({
            severity: 'error',
            summary: 'User Is missing',
            detail: 'Your e-mail is missing',
            life: 3000
          })
          this.errorsSignup.push('Your e-mail is missing')
        }
        if (this.formSignup.password1 === '') {
          this.$toast.add({
            severity: 'error',
            summary: 'User passwordIs missing',
            detail: 'Your password is missing',
            life: 3000
          })
          this.errorsSignup.push('Your password is missing')
        }
        if (this.formSignup.password1 !== this.formSignup.password2) {
          this.$toast.add({
            severity: 'error',
            summary: 'User  password does not match',
            detail: 'Your password  does not match',
            life: 3000
          })
          this.errorsSignup.push('The password does not match')
        }
        if (this.errorsSignup.length === 0) {
          axios
            .post('/api/signup/', this.formSignup)
            .then((response) => {
              if (response.data.message === 'success') {
                if (response.data.email_sent) {
                  this.$toast.add({
                    severity: 'success',
                    summary: 'User Registered',
                    detail: 'Please activate your account by clicking the link sent to your email.',
                    life: 3000
                  })
                }
                this.$toast.add({
                  severity: 'success',
                  summary: 'User Is Registered',
                  detail: 'Please activate your account by clicking your email link',
                  life: 3000
                })
                this.formSignup.name = ''
                this.formSignup.surname = ''
                this.formSignup.email = ''
                this.formSignup.date_of_birth = ''
                this.formSignup.gender = ''
                this.formSignup.password1 = ''
                this.formSignup.password2 = ''
                // this.$router.push('/loginView')
                window.location.reload()
              } else {
                const data = JSON.parse(response.data.message)
                this.$toast.add({
                  severity: 'error',
                  summary: 'Error Message',
                  detail: 'Message Content Something went wrong. Please try again',
                  life: 6000
                })
                for (const key in data) {
                  this.errors.push(data[key][0].message)
                }
                console.log(`Bad`, this.formSignup.date_of_birth)
                console.log(`Day`, this.day)
                console.log(`month`, this.month)
                console.log(`year`, this.year)
              }
            })
            .catch((error) => {
              console.log('error', error)
            })
        }
      }
    }
  }
</script>
```

__________________________________________________
### 22 Create Page [ Account/LoginView.vue ] Inside views/Account
```html
<template>
  <div class="Component-Name">Page Profile View</div>
</template>
```
```js
<script>
export default { name: 'ProfileView' }
</script>
```
__________________________________________________
### 23 Edite Page [ index.js ] Inside router
```js
// index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

// Authentication
import LoginView from '../views/Authentication/LoginView.vue'

// Account
import ProfileView from '../views/Account/ProfileView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    // Authentication 
    // Login
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    // Account
    {
      path: '/profile/:id',
      name: 'profile',
      component: ProfileView,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router

```

__________________________________________________
### 23 Edite Page [ style.scss ] Inside src/assets/Scss
* Import Css Style To Use It Inside Glopal [ index.js ]
```js
// Page [ facebook/facebook_vue/src/main.js ]
import './assets/main.css'
import './assets/Scss/Style.scss'
```
* Project Structure
```
├── src/
│   ├── assets/
│   |   ├── Scss/
│   |   |   ├── Authentication/
│   │   |   |   ├── 📝 _login.scss
│   |   |   ├── Header/
│   │   |   |   ├── 📝 _header.scss
│   |   |   ├── Style.scss
```
* Creat This Pages
```cmd
Scss/Authentication/_login.scss
Header/_header.scss
Style.scss
```
* style
```css
// Global Color Light Theme
:root {
  /* Body */
  --body-bg-hr: #f0f2f5;
  --body-bg: #f8fafc;
  // Header Style
  --header-height: 4rem;
  --header-bg: #fff;
  // Logo
  --header-facebook-icon-color: #0866ff;
  --header-facebook-icon-font-size: 2.5rem;
  // search
  --header-search-icon-color: #65676b;
  --header-search-input-text-color: #050505;
  --header-search-input-placeholder-color: #0505059e;
  // placeholder
  --header-search-input-color: #f0f2f5;
  // Linke Center
  --header_center_section_link_home_border: #0866ff;
  --header_center_section_link_home_active_color: #0866ff;
  --header_center_section_link_home_color: #65676b;
  --header_center_section_link_home_hover_bg: #f2f2f2;
  //
  --header-center-section-icon-size: 1.5rem;
  --header-link-border-color: #0866ff;
  --header-link-background-color: #d8dadf;
  --header-user-option-btn-bg-light: #e4e6eb;
  //
  // Index Style
  //

  /* Fore Content Page Index Center Content */
  --page-index-content-center: #fff;
  --page-index-post-bg: #fff;
  --page-index-post-button-hover: #f0f2f5;
  --page-index-post-icon-trand: #65676b;
  /* For Scrollbar Page Index Lift Sidebar */
  --page-index-sidebar-lift-scrollbar: #e6e8eb;
  --page-index-sidebar-lift-scrollbar-thumb: #bcc0c4;

  /* For Scrollbar Page Index right Sidebar */
  --page-index-sidebar-right-scrollbar: #e6e8eb;
  --page-index-sidebar-right-scrollbar-thumb: #bcc0c4;
  --page-index-sidebar-right-border-user-control: #bcc0c4;
  --page-index-sidebar-right-text-color: #65676b;
  --page-index-sidebar-right-icon-bg: #65676b;
  //
}

// Header
@import 'Header/header';
// Authentication
@import 'Authentication/login';
// Style For Dark Mode
html.dark,
html.p-dark {
  /* Body */
  // --body-bg: #0d121b;
  --body-bg: #09090b;
  --header-user-option-btn-bg-light: #09090b;
  --header-bg: #18181b;
}
body {
  // background-color: var(--body-bg-hr);
  background-color: var(--body-bg);
  transition:
    background-color 0.95s linear,
    color 0.95s linear;
}

```
* login
```css
.wrapper_login_page {
  padding-top: 60px;
  .inner_login_page {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 94vh;
    .container,
    .container {
      .flex {
        .wrapper_text_login {
          .inner {
            .title {
              color: #0866ff;
              font-size: 8vh;
              font-weight: bold;
            }
            .subtitle {
              font-family: SFProDisplay-Regular, Helvetica, Arial, sans-serif;
              font-size: 28px;
              font-weight: normal;
              line-height: 32px;
              width: 500px;
            }
          }
        }
        .wrapper_form_login {
          // background-color: #fff;
          // padding: 1rem;
          // border-radius: 1rem;
          .form_login {
            .p-card-body {
              padding: 0 !important;
              .p-password {
                display: block !important;
                input[type='password'] {
                  width: 100% !important;
                }
              }
            }
          }
          .button_signup {
            // background-color: #42b72a;
            // color: #fff;
            // width: 50%;
            display: block;
            margin: 2rem auto;
          }
        }
      }
    }
  }
}
```
* header
```css
.header_wrapper {
  > div {
    padding: 0;
    header {
      height: var(--header-height);
      background-color: var(--header-bg);
      width: 100%;
      z-index: 1000;
      padding: 0 0.5rem;
      .container {
        height: var(--header-height);
        // Left Section (Logo and Search Bar)
        .header_left_section {
          .logo {
            color: var(--header-facebook-icon-color);
            font-size: var(--header-facebook-icon-font-size);
          }
          .search_bar {
            position: relative;
            span.icon {
              position: absolute;
              left: 7px;
              top: 7px;
              i,
              svg {
                font-size: 16px;
                color: var(--header-search-icon-color);
                font-weight: 700;
              }
              /* Console Devices */
              /* Mobil S, Less Than 320px */
              @media screen and (max-width: 320px) {
                left: 10px;
              }
              /* Mobil M, Less Than 375px */
              @media screen and (min-width: 321px) and (max-width: 375px) {
                left: 10px;
              }
              /* Mobil L, Less Than 425px */
              @media screen and (min-width: 376px) and (max-width: 425px) {
                left: 10px;
              }
            }
            input {
              background-color: var(--header-search-input-color);
              padding-left: 2rem;
              color: var(--header-search-input-text-color);
              &::placeholder {
                color: var(--header-search-input-placeholder-color);
                // font-weight: 500;
                font-size: 15px;
              }
              /* Console Devices */
              /* Mobil S, Less Than 320px */
              @media screen and (max-width: 320px) {
                width: 35px;
              }
              /* Mobil M, Less Than 375px */
              @media screen and (min-width: 321px) and (max-width: 375px) {
                width: 35px;
              }
              /* Mobil L, Less Than 425px */
              @media screen and (min-width: 376px) and (max-width: 425px) {
                width: 35px;
              }
              /* Tablet , Less Than 768px */
              @media screen and (min-width: 426px) and (max-width: 768px) {
                width: 35px;
              }
              /* Laptop , Less Than 1024px */
              @media screen and (min-width: 769px) and (max-width: 1024px) {
              }
              /* Laptop L, Less Than 1440px */
              @media screen and (min-width: 1025px) and (max-width: 1440px) {
              }
              /* 4K , Less Than 2560px */
              @media screen and (min-width: 1441px) and (max-width: 2560px) {
              }
            }
          }
        }
        .toggle_header_left_section {
          // border: 0.5rem solid #f00;
          font-size: 1.5rem;
          padding: 0.5rem 1rem;
          margin: 5px 0;
          display: flex;
          justify-content: center;
          align-items: center;
          border-radius: 5px;
          &:hover {
            background-color: var(--header_center_section_link_home_hover_bg);
          }
          /* Console Devices */
          /* Mobil S, Less Than 320px */
          @media screen and (max-width: 320px) {
            display: flex;
            align-items: center;
            justify-content: end;
            position: relative;
            left: -25px;
            display: none;
          }
          /* Mobil M, Less Than 375px */
          @media screen and (min-width: 321px) and (max-width: 375px) {
            display: flex;
            align-items: center;
            justify-content: end;
            position: relative;
            left: -40px;
          }
          /* Mobil L, Less Than 425px */
          @media screen and (min-width: 376px) and (max-width: 425px) {
            display: flex;
            align-items: center;
            justify-content: end;
            position: relative;
            left: -60px;
          }
          /* Tablet , Less Than 768px */
          @media screen and (min-width: 426px) and (max-width: 768px) {
            display: flex;
            align-items: center;
            justify-content: end;
            position: relative;
            left: -10px;
          }
          /* Laptop , Less Than 1024px */
          @media screen and (min-width: 769px) and (max-width: 1024px) {
          }
          /* Laptop L, Less Than 1440px */
          @media screen and (min-width: 1025px) and (max-width: 1440px) {
          }
          /* 4K , Less Than 2560px */
          @media screen and (min-width: 1441px) and (max-width: 2560px) {
          }
        }
        // Center Section (Navigation Icons)
        .header_center_section {
          height: var(--header-height);
          /* Console Devices */
          /* Mobil S, Less Than 320px */
          @media screen and (max-width: 320px) {
            position: fixed;
            left: 100%;
            top: 0;
            width: 100%;
            height: 100%;
          }
          /* Mobil M, Less Than 375px */
          @media screen and (min-width: 321px) and (max-width: 375px) {
            position: fixed;
            left: 100%;
            top: 0;
            width: 100%;
            height: 100%;
          }
          /* Mobil L, Less Than 425px */
          @media screen and (min-width: 376px) and (max-width: 425px) {
            position: fixed;
            left: 100%;
            top: 0;
            width: 100%;
            height: 100%;
          }
          /* Tablet , Less Than 768px */
          @media screen and (min-width: 426px) and (max-width: 768px) {
          }
          /* Laptop , Less Than 1024px */
          @media screen and (min-width: 769px) and (max-width: 1024px) {
          }
          /* Laptop L, Less Than 1440px */
          @media screen and (min-width: 1025px) and (max-width: 1440px) {
          }
          /* 4K , Less Than 2560px */
          @media screen and (min-width: 1441px) and (max-width: 2560px) {
          }
          .header_center_section_link_home,
          .header_center_section_link_friends,
          .header_center_section_link_videos,
          .header_center_section_link_marketplace,
          .header_center_section_link_groups {
            height: 100%;
            border-bottom: 4px solid transparent;
            display: flex;
            align-items: center;
            justify-content: center;
            &:hover {
              background-color: var(--header_center_section_link_home_hover_bg);
              border-radius: 5px;
            }
            span {
              position: relative;
              display: flex;
              justify-content: center;
              align-items: center;
              svg {
                height: var(--header-center-section-icon-size);
                width: var(--header-center-section-icon-size);
                color: var(--header_center_section_link_home_color);
              }
            }
          }
          .header_center_section_link_home {
            border-bottom: 3px solid var(--header_center_section_link_home_active_color);
            span {
              svg {
                color: var(--header_center_section_link_home_active_color);
              }
            }
          }
        }
        //
        .header_right_section {
          .header_right_section_link {
            border-radius: 50%;
            padding: 10px;

            .header_right_section_link_span {
              .header_right_section_link_svg {
                height: var(--header-center-section-icon-size);
                width: var(--header-center-section-icon-size);
              }
            }
          }
          // Avater
          div.p-avatar {
            img {
              width: 40px;
              height: 40px;
            }
          }
        }
      }
    }
  }
}

// Popup User Option
.div_wrapper_profile {
  a {
    align-items: center;
    margin-bottom: 1rem;
    .user_img {
      margin-right: 12px;
    }
    .user_name {
    }
  }
}
.div_wrapper_logout {
  align-items: center;
  .icon_logout {
    background-color: var(--header-user-option-btn-bg-light);
    border-radius: 50%;
    padding: 5px;
    height: 36px;
    width: 36px;
    margin-right: 12px;
    display: flex;
    justify-items: center;
    align-items: center;
  }
}
.div_wrapper_toggle_theme {
  align-items: center;
  margin-top: 1rem;
  span:first-child {
    margin-right: 12px;
  }
}
```
__________________________________________________
__________________________________________________
__________________________________________________
_____________________ Start Profile ______________
__________________________________________________
__________________________________________________
__________________________________________________
* Create Function Profile In Side Page [ api.py ]
```
# Profile
@api_view(["GET"])
def profile(request, id):
    # (primary key) استرجاع معلومات المستخدم بناءً على معرفه الفريد
    user = User.objects.get(pk=id)
    # تسلسل بيانات المستخدم باستخدام السيريالايزر المخصص
    user_serializer = UserSerializer(user)
    # JSON إرجاع البيانات كاستجابة
    return JsonResponse(
        {
            "user": user_serializer.data,
        },
        safe=False,
    )

```
* Create Url Profile In Side Page [ url.py ]
```
urlpatterns = [
    path("profile/<uuid:id>/", api.profile, name="profile"),
]
```
__________________________________________________
__________________________________________________
__________________________________________________
_____________________ Start Doker ________________
__________________________________________________
__________________________________________________
__________________________________________________

### Start Doker
* 
```
├── 📁 Facebook/
│   ├── 📁 facebook_django/
│   ├── 📁 facebook_virtual_environment/
│   ├── 📁 facebook_vue/
│   ├── 📁 templates/
│   ├── 📝 .gitignore
│   ├── 📝 Build.md
│   ├── 📝 desktop.ini
│   ├── 📝 LICENSE
│   ├── 📝 README.md
```
```
```#   f b  
 