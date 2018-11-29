import xadmin
from django.conf.urls import url, include
from apps.main import views

urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    url('^$', views.index),
    # url('account', include('account.urls')),
    # url('cate', include('cate.urls')),
    # url('main', include('main.urls')),
    url('shop', include('detail.urls')),
    url('search', include('search.urls'))
]
