from django.conf.urls import include,url,patterns
from django.contrib import admin
from blog.views import hello,fuc_welc




urlpatterns = [
    # Examples:
    # url(r'^$', 'firstdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/',include('polls.urls')),
    url(r'^$',fuc_welc),

]
