"""django_z URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 
from rest_framework.documentation import include_docs_urls # coreapi接口文档
from django_otp.admin import OTPAdminSite # 双因子认证

# admin.site.__class__ = OTPAdminSite # 是否开启双因子认证

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='My API title')),  # coreapi接口文档，可以关闭
    path('api/demo/', include('demo_test.urls', namespace='demo')), # 测试模块，可以拆卸
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)