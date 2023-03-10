from django.urls import path
from .views import post_comment, comment_list, comment_list_author, comment_update

app_name = 'comment'


urlpatterns = [
    path('api/<int:pk>', post_comment),
    path('api/list/<int:pk>', comment_list),
    path('api/update/<int:pk>', comment_update),
    path('api/list/author', comment_list_author),
]

