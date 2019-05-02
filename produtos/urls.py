from django.urls import path
from produtos.views import ProdutoBulk

urlpatterns = [
    #path('list/', persons_list, name="person_list"),
path('person_bulk/', ProdutoBulk.as_view(), name='person_bulk'),

]