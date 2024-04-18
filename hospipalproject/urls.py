"""
URL configuration for hospipalproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from hospitalapp import views
from hospipalproject import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.index,name='home'),
    path('abo',views.about,name='abo'),
    path('dep',views.dep,name='dep'),
    path('doct',views.doc,name='doct'),
    path('home/<str:pk>',views.showmsg,name='page'),
    path('book',views.booking,name='book'),
    path('call',views.contactme,name='call')


]
if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

