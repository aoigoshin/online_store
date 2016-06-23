from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home'),
    url(r'^item/(?P<alias>[^/]+)', 'main.views.item'),
    url(r'^order/', 'main.views.order'),
    url(r'^(?P<alias>[^/]+)', 'main.views.get_category'),
    url(r'^order/#$', 'views.order_create'),
] 