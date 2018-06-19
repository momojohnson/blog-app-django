from django.urls import path
from boards import views
app_name='boards'
urlpatterns = [
    path('<int:board_id>/', views.TopicListView.as_view(), name='board_topics'),
    path('<int:board_pk>/new/', views.new_topic, name='new_topic'),
    path('<int:board_pk>/topics/<int:topic_pk>/', views.PostListView.as_view(), name='topic_posts'),
    path('<int:board_pk>/topics/<int:topic_pk>/reply/', views.topic_reply, name='topic_reply'),
    path('<int:board_pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
]
