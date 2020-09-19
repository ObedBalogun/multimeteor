from django.urls import path
from .views import home, MediaDetail, upload, PostDelete
from user.views import registration_view, login_view,logout_view,account_view

app_name = 'media'

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registration_view, name='signup'),
    path('homepage/', home, name='homepage'),
    path('media/', MediaDetail.as_view(), name='media'),
    path('update/', account_view, name='profile'),
    path('upload/', upload, name='upload'),
    path('<int:id>/delete/', PostDelete.as_view(), name='delete'),
]
