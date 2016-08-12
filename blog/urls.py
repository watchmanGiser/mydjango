__author__ = 'zhuzhongpeng'
from django.conf.urls import include,url,patterns
from blog.views import hello,fuc_welc



urlpatterns = [
    # Examples:
    # url(r'^$', 'firstdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^hello/',hello),
    url(r'^$',fuc_welc),

    ]

