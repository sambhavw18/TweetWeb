from . import views
from django.urls import path
from django.conf.urls import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('edit/<int:tweet_id>/',views.edit,name="edit"),
    path('delete/<int:tweet_id>',views.delete,name="delete"),
    path('register/',views.register,name="register"),
    path('mytweet/',views.mytweet,name="mytweet"),
    path('search/',views.search,name="search")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)