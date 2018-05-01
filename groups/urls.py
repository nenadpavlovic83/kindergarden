from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('groupa/', views.groupa, name='groupa'),
    path("groupb/", views.groupb, name='groupb'),
    path("groupc/", views.groupc, name='groupc'),
    path("groupd/", views.groupd, name='groupd'),
]
