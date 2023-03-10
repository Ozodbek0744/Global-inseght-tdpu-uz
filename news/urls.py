from django.urls import path
from .views import news_post, news_detail_view, news_list_view, news_update_delete

app_name = 'news'

urlpatterns = [
    path('post', news_post, name='news_post'),
    path('list', news_list_view, name='news_list'),
    path('detail/<slug:slug>', news_detail_view, name='news_detail'),
    path('update_delete/<slug:slug>', news_update_delete, name='news_update_delete')
]

