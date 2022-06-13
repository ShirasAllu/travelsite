from . import views
from django.urls import path

urlpatterns = [

    path('',views.about,name='about'),
  # path('homepage/',views.homepage,name='homepage'),
    #path('contact/',views.contact,name='contact'),
    #path('detail/',views.detail,name='detail'),
    #path('thankspage/',views.thankspage,name='thankspage')
]