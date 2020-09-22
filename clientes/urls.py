from django.urls import path
from .views import *



urlpatterns = [
    path('list/', persons_list, name="persons_list"),
    path('new/', persons_new, name="persons_new"),
    path('update/<int:id>', persons_update, name="persons_update"),
    path('delete/<int:id>', persons_delete, name="persons_delete"),
    path('person_list', PersonList.as_view(), name="person_list_cbv"),
    path('person_detail/<int:pk>/', PersonDetail.as_view(), name="detail_view_cbv"),
    path('person_update/<int:pk>/', PersonUpdate.as_view(), name="update_view_cbv"),
    path('person_delete/<int:pk>/', PersonDelete.as_view(), name="delete_view_cbv"),
    path('person_create/', PersonCreate.as_view(), name="person_create_cbv"),

]
