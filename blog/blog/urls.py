from django.conf.urls import include, url
from django.contrib import admin
from posts import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_details)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
