"""iqnaax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_header = "IQNAAX Admin"
admin.site.site_title = "IQNAAX Admin Panel"
admin.site.index_title = "Welcome to Iqnaax Admin Panel"


urlpatterns = [
    path('', include("home.urls")),
    path('about/', include("about.urls")),
    path('blog/', include("blog.urls")),
    path('gallery/', include("gallery.urls")),
    path('shop/', include("shop.urls")),
    path('contact/', include("contact.urls")),
    path('', include("account.urls")),
    path('admin/', admin.site.urls),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()