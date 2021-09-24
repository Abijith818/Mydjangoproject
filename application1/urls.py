from django.urls import path
from .import views

urlpatterns = [
    path('test',views.testfun,name='test'),
    path('test1',views.testfun1,name='test1'),

]