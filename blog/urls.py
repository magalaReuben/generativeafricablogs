from django.urls import path
from .views import GetBlog, GetAllBlogs

urlpatterns = [
    path('blogs/', GetAllBlogs.as_view(), name='get_all_blogs'),
    path('blogs/<slug:slug>/', GetBlog.as_view(), name='get_blog'),
]