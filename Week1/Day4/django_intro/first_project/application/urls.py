from django.urls import path
from . import views

urlpatterns = [

    # path('admin/', admin.site.urls),
    path('', views.root),
    path('blogs', views.index),
    path('blogs/<int:blog_id>', views.showBlog),
]