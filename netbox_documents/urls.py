from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (

    # SiteDocument
    path('site-document/', views.SiteDocumentListView.as_view(), name='sitedocument_list'),
    path('site-document/add/', views.SiteDocumentEditView.as_view(), name='sitedocument_add'),
    path('site-document/<int:pk>/', views.SiteDocumentView.as_view(), name='sitedocument'),
    path('site-document/<int:pk>/edit/', views.SiteDocumentEditView.as_view(), name='sitedocument_edit'),
    path('site-document/<int:pk>/delete/', views.SiteDocumentDeleteView.as_view(), name='sitedocument_delete'),
    path('site-document/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='sitedocument_changelog', kwargs={
        'model': models.SiteDocument
    }),

    # LocationDocument
    path('location-document/', views.LocationDocumentListView.as_view(), name='locationdocument_list'),
    path('location-document/add/', views.LocationDocumentEditView.as_view(), name='locationdocument_add'),
    path('location-document/<int:pk>/', views.LocationDocumentView.as_view(), name='locationdocument'),
    path('location-document/<int:pk>/edit/', views.LocationDocumentEditView.as_view(), name='locationdocument_edit'),
    path('location-document/<int:pk>/delete/', views.LocationDocumentDeleteView.as_view(), name='locationdocument_delete'),
    path('location-document/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='locationdocument_changelog', kwargs={
        'model': models.LocationDocument
    }),

    # DeviceDocument
    path('device-document/', views.DeviceDocumentListView.as_view(), name='devicedocument_list'),
    path('device-document/add/', views.DeviceDocumentEditView.as_view(), name='devicedocument_add'),
    path('device-document/<int:pk>/', views.DeviceDocumentView.as_view(), name='devicedocument'),
    path('device-document/<int:pk>/edit/', views.DeviceDocumentEditView.as_view(), name='devicedocument_edit'),
    path('device-document/<int:pk>/delete/', views.DeviceDocumentDeleteView.as_view(), name='devicedocument_delete'),
    path('device-document/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='devicedocument_changelog', kwargs={
        'model': models.DeviceDocument
    }),

    # VMDocument
    path('virtual-machine-document/', views.VirtualMachineDocumentListView.as_view(), name='virtualmachinedocument_list'),
    path('virtual-machine-document/add/', views.VirtualMachineDocumentEditView.as_view(), name='virtualmachinedocument_add'),
    path('virtual-machine-document/<int:pk>/', views.VirtualMachineDocumentView.as_view(), name='virtualmachinedocument'),
    path('virtual-machine-document/<int:pk>/edit/', views.VirtualMachineDocumentEditView.as_view(), name='virtualmachinedocument_edit'),
    path('virtual-machine-document/<int:pk>/delete/', views.VirtualMachineDocumentDeleteView.as_view(), name='virtualmachinedocument_delete'),
    path('virtual-machine-document/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='virtualmachinedocument_changelog', kwargs={
        'model': models.VirtualMachineDocument
    }),

    
    # DeviceTypeDocument
    path('device-type-document/', views.DeviceTypeDocumentListView.as_view(), name='devicetypedocument_list'),
    path('device-type-document/add/', views.DeviceTypeDocumentEditView.as_view(), name='devicetypedocument_add'),
    path('device-type-document/<int:pk>/', views.DeviceTypeDocumentView.as_view(), name='devicetypedocument'),
    path('device-type-document/<int:pk>/edit/', views.DeviceTypeDocumentEditView.as_view(), name='devicetypedocument_edit'),
    path('device-type-document/<int:pk>/delete/', views.DeviceTypeDocumentDeleteView.as_view(), name='devicetypedocument_delete'),
    path('device-type-document/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='devicetypedocument_changelog', kwargs={
        'model': models.DeviceTypeDocument
    }),

    # CircuitDocument
    path('circuit-document/', views.CircuitDocumentListView.as_view(), name='circuitdocument_list'),
    path('circuit-document/add/', views.CircuitDocumentEditView.as_view(), name='circuitdocument_add'),
    path('circuit-document/<int:pk>/', views.CircuitDocumentView.as_view(), name='circuitdocument'),
    path('circuit-document/<int:pk>/edit/', views.CircuitDocumentEditView.as_view(), name='circuitdocument_edit'),
    path('circuit-document/<int:pk>/delete/', views.CircuitDocumentDeleteView.as_view(), name='circuitdocument_delete'),
    path('circuit-document/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='circuitdocument_changelog', kwargs={
        'model': models.CircuitDocument
    }), 
    

)