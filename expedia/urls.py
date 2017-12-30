
from django.contrib import admin
from django.conf.urls import url, include
from deals.views import find_deal

urlpatterns = [

    url('^admin/', admin.site.urls),
    url('^$', find_deal, name='find'),
]
