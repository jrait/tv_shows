from django.urls import path
from . import views

urlpatterns = [
    path('',views.root),
    path('shows',views.index),
    path('shows/new',views.new),
    path('shows/create',views.create),
    path('shows/<int:info_id>',views.info),
    path('shows/<int:delete_id>/delete',views.delete),
    path('shows/<int:edit_id>/edit',views.edit),
    path('shows/edit_show/<int:edit_id>',views.edit_show),
]