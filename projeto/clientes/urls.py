from django.urls import path
from .views import perssons_list, perssons_new, perssons_update, perssons_delete

urlpatterns = [
    path('list/', perssons_list, name='person_list'),
    path('new/', perssons_new, name='person_new'),
    path('update/<int:id>', perssons_update, name='person_update'),
    path('delete/<int:id>', perssons_delete, name='person_delete')
]