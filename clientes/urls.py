
from django.urls import path


from .views2 import persons_list
from .views2 import persons_new
from .views2 import persons_update
from .views2 import persons_delete


urlpatterns = [
    path('list/', persons_list, name="person_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="person_update"),
    path('delete/<int:id>/', persons_delete, name="person_delete"),

]