from django.conf.urls import include, url, static
from django.contrib import admin
from mis import settings
import workflow.views
import invent.urls
import basedata.urls
import selfhelp.urls
import mis.views

# from django.contrib.staticfiles.views import serve
# from django.urls import re_path
#
#
# def return_static(request, path, insecure=True, **kwargs):
#     return serve(request, path, insecure, **kwargs)
#
#
# def return_upload(request, path, insecure=True, **kwargs):
#     return serve(request, path, insecure, **kwargs)


urlpatterns = [
    url(r'^$', mis.views.home),
    url(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/change/start", workflow.views.start),
    url(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/change/approve/(?P<operation>\d+)", workflow.views.approve),
    url(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/change/restart/(?P<instance>\d+)", workflow.views.restart),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/invent/', include(invent.urls)),
    url(r'^admin/basedata/', include(basedata.urls)),
    url(r'^admin/selfhelp/', include(selfhelp.urls)),

    # re_path(r'^static/(?P<path>.*)$', return_static, name='static'),
    # re_path(r'^upload/(?P<path>.*)$', return_upload, name='upload'),

]
urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






