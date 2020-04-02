"""
 portfolio_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings #this is done to import our setting file
from django.conf.urls.static import static #this is done to import static
from . import views
import blog.views
import projects.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('blog/', blog.views.home),
    path('projects/', projects.views.home)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #this is done as our image was not able to show as no url was defined for that,
#so we created a static media which shows that we want to show a static media
#this is actually done to give the static url of the image which we want to show
#media_root here means the root media folder, so this  gives the url of media
#pip install mysqlclient
#pip install Pillow(done before for image insertion)


