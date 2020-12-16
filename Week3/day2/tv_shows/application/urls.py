from django.urls import path
from . import views

urlpatterns = [
    # render routes
    path('', views.dashboard),
    path('shows', views.dashboard),
    path('shows/new', views.new_page),
    path('shows/<int:show_id>/edit', views.edit_page),
    path('shows/<int:show_id>', views.show_page),

    # actions routes
    path('shows/<int:show_id>/delete', views.delete),
    path('shows/create', views.create_show)
]