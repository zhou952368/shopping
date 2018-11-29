from django.conf.urls import url

from search import views

urlpatterns = [
    url('search/', views.search, name='search')
]
