from django.urls import path

from . import views # import views so we can use them in urls.


urlpatterns = [

    path('',views.index,name='index'),

    path('^register', views.register,name='register'),
    path(r'^user_login/$',views.user_login,name='user_login'),
    path(r'^logout/$', views.user_logout, name='logout'),
    path('update',views.update_user,name='update'),
]
