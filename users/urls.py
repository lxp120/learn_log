
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'
urlpatterns = [
    #这是由于在django2.0后不支持使用在urls.py中写
    # url(r'^admin/', include(admin.site.urls)),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

     # path('login/', LoginView.as_view, {'template_name': 'users/login.html'},
     #     name='login'),
    # path('logout/', LoginView.as_view, name='logout'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
