from django.urls import path
from demo_test import views

app_name = 'demo'

urlpatterns = [
    path('get/', views.DemoGet.as_view()),
    # path('post/', views.DemoGet.as_view()),
    # path('put/', views.DemoGet.as_view()),
    # path('del/', views.DemoGet.as_view()),
    # path('change/', views.DemoGet.as_view()),
]