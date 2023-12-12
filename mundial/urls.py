"""
URL configuration for mundial project.

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
"""
from django.contrib import admin
from django.urls import path, include
from album import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'author_rest', views.AuthorViewSet)
router.register(r'publisher_rest', views.PublisherViewSet)
router.register(r'book_rest', views.BookViewSet)

urlpatterns = [
    #Auth
    path('admin/', admin.site.urls),

    #Dashboard
    #path('', views.dashboard, name='dashboard'),

    # Autores
    path('author/', views.AuthorListView.as_view(), name='author-list'),
    # Update
    path('author/<int:pk>/update/',views.AuthorUpdate.as_view(),name='author-update'), 
    #Create
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    #Delete
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),

    #Editoriales
    path('publisher/', views.PublisherListView.as_view(), name='publisher-list'),
    # Update
    path('publisher/<int:pk>/update/',views.PublisherUpdate.as_view(),name='publisher-update'), 
    #Create
    path('publisher/create/', views.PublisherCreate.as_view(), name='publisher-create'),
    #Delete
    path('publisher/<int:pk>/delete/', views.PublisherDelete.as_view(), name='publisher-delete'),

    #Libros
    path('book/', views.BookListView.as_view(), name='book-list'),
    # Update
    path('book/<int:pk>/update/',views.BookUpdate.as_view(),name='book-update'), 
    #Create
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    #Delete
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),

    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
