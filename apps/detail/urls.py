from django.conf.urls import url

from apps.detail import views

urlpatterns = [
    url(r'detail/', views.detail, name='detail')
]
