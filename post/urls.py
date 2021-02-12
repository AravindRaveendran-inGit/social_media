from django.urls import path
from .views import post_comment_create_and_list_view, like_unlike_post, PostDeleteView, PostUpdateView

app_name = 'post'

urlpatterns = [
    path('', post_comment_create_and_list_view, name='post-view'),
    path('liked/', like_unlike_post, name='post-liked'),
    path('<pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
    path('<pk>/update/', PostUpdateView.as_view(), name='post-update'),

]
