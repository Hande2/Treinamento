
from django.urls import path


from .views2 import persons_list
from .views2 import persons_new
from .views2 import persons_update
from .views2 import persons_delete
from .views2 import PersonList
from .views2 import PersonDetail
from .views2 import PersonCreate
from .views2 import PersonUpdate
from .views2 import PersonDetele



urlpatterns = [
    path('list/', persons_list, name="person_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="person_update"),
    path('delete/<int:id>/', persons_delete, name="person_delete"),
    path('person_list/', PersonList.as_view(), name="person_list_cb"),
    path('person_detail/<int:pk>/', PersonDetail.as_view(), name="person_detail_cb"),
    path('person_update/<int:pk>/', PersonUpdate.as_view(), name="person_update_cb"),
    path('person_create/', PersonCreate.as_view(), name="person_create"),


]