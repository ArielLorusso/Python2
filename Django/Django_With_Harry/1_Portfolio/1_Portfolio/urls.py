"""
URL configuration for 1_Portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
"""                             # path ('blog/', include('blog.urls'))  <-  modifythis example
from django.contrib import admin
from django.urls import path, include   # include  (APP)
from .import views

# Django Admin customization
admin.site.site_header  = "ADMIN Site"
admin.site.site_title   = "ADMIN TAB title" #
admin.site.index_title  = "index title"

urlpatterns = [
    path("admin/",    admin.site.urls),
    path(""        ,  views.home    ,  name='testt'   ),
    path("about"   ,  views.about   ,  name='testt'   ),
    path("projects" , views.projects  ),        
    path("contact" ,  views.contact ,  name='testt' ),     
]
