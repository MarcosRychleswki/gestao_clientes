from django.urls import path
from .views import *



urlpatterns = [
    path('list/', persons_list, name="persons_list"),
    path('new/', persons_new, name="persons_new"),
    path('update/<int:id>', persons_update, name="persons_update"),
    path('delete/<int:id>', persons_delete, name="persons_delete"),
    path('person_list', PersonList.as_view()),
    path('person_detail/<int:pk>/', PersonDetail.as_view()),

]
