from django.urls import path
from .views import blog_video_list_view, blog_video_detail_view, blog_video_post, \
    blog_update_delete_view, myblog_list

app_name = 'blog'

urlpatterns = [
    path("list", blog_video_list_view),
    path("list/<slug:slug>", blog_video_detail_view),
    path("post", blog_video_post),
    path("update-delete/<slug:slug>", blog_update_delete_view),
    path("myblog/list", myblog_list)
]
