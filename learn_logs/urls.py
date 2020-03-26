"""定义learnlogs的url模式"""
from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'learn_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('topics/', views.topics, name='topics'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    ]

# url(r'^$', views.index, name='index'),
# url(r'^topic/$', views.topics, name='topics'),
# url(r'^topics/(?P<topic_id>\d+)/$', views.topics, name='topic'),
# url(r'^new_topic/$', views.new_topic, name='new_topic'),
# url(r'^new_entry/(?P<topic_id>\d+)/$)', views.new_entry, name='new_entry')