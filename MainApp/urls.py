from django.urls import path

from . import views

app_name = 'MainApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'), # dynamic URL for topic details to load a specific page using the id of the topic
    path('new_topic/', views.new_topic, name='new_topic')
]
