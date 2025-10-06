from django.contrib import admin
from django.urls import path
from books.api import api
from django.shortcuts import render

def homepage(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def project(request):
    return render(request, "project.html")

def system(request):
    return render(request, "system.html")    

def search(request):
    return render(request, "search.html")   

def create(request):
    return render(request, "create.html") 

def update(request):
    return render(request, "update.html") 

def delete(request):
    return render(request, "delete.html") 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("", homepage),
    path("about/", about),  
    path("project/", project),
    path("system/", system),
    path("search/", search),
    path("create/", create),
    path("update/", update),
    path("delete/", delete)
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
