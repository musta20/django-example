from django.urls import path
from fristpy_app import views
app_name = 'fristpy_app'

urlpatterns = [
            path('',views.index),

    path('forms/',views.forms_view),
    path('base/',views.base,name= 'base'),
    path('sinup/',views.sinup,name= 'sinup'),
    path('other/',views.other, name = 'other'),
    path('login/',views.ulogin, name = 'login'),
    path('logout/',views.ulogout, name = 'logout'),
    path('realtiv_url/',views.realtiv_url, name = 'realtiv_url'),

]
