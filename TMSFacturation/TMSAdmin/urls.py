from django.urls import path
from . import views

urlpatterns = [

    path('services/', views.services, name='services'),
    path('services/<codeS>', views.to_update, name='to_update'),
    path('services/update/<codeS>', views.update, name='update'),
    path('services/ajouter/', views.to_add, name='to_add'),
    path('services/enregistrer/', views.add, name='add'),

    path('operations/', views.operations, name='operations'),
    path('operations/<int:opid>', views.to_update_op, name='to_update_op'),
    path('operations/ajouter/', views.to_add_op, name='add_operation'),
    path('operations/ajouterService/', views.add_op_in, name='add_operation_input'),
    path('operations/modiferOperation/', views.up_service_details, name='up_service_details'),
    path('operations/filterOperations/', views.filter_operations, name='up_filter_details'),
    path('operations/supprimerOI/<int:opID>/<int:opinID>', views.delete_op_in, name='delete_operation_input'),
    path('operations/enregistrer/', views.add_op, name='save_operation'),

]