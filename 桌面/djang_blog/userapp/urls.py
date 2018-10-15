from django.conf.urls import url
from userapp import views
urlpatterns=[
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^register1/', views.register1, name='register1'),
    url(r'^zuce/(?P<u>.*)/(?P<c>.*)/', views.zuce, name='zuce'),
]