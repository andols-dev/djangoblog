from django.urls import path
from .views import profile_view,profile_update_view
urlpatterns = [
    path('', profile_view, name='profile'),
    path('update/', profile_update_view, name='update-profile'),

]
