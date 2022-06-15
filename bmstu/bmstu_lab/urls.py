from django.urls import path
from . import views


app_name = 'master'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>', views.detail, name='detail')

]