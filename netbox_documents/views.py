from netbox.views import generic
from . import forms, models, tables, filtersets


### SiteDocument
class SiteDocumentView(generic.ObjectView):
    queryset = models.SiteDocument.objects.all()

class SiteDocumentListView(generic.ObjectListView):
    queryset = models.SiteDocument.objects.all()
    table = tables.SiteDocumentTable
    filterset = filtersets.SiteDocumentFilterSet
    filterset_form = forms.SiteDocumentFilterForm

class SiteDocumentEditView(generic.ObjectEditView):
    queryset = models.SiteDocument.objects.all()
    form = forms.SiteDocumentForm

    template_name = 'netbox_documents/sitedocument_edit.html'

class SiteDocumentDeleteView(generic.ObjectDeleteView):
    queryset = models.SiteDocument.objects.all()


### LocationDocument
class LocationDocumentView(generic.ObjectView):
    queryset = models.LocationDocument.objects.all()

class LocationDocumentListView(generic.ObjectListView):
    queryset = models.LocationDocument.objects.all()
    table = tables.LocationDocumentTable
    filterset = filtersets.LocationDocumentFilterSet
    filterset_form = forms.LocationDocumentFilterForm

class LocationDocumentEditView(generic.ObjectEditView):
    queryset = models.LocationDocument.objects.all()
    form = forms.LocationDocumentForm

    template_name = 'netbox_documents/locationdocument_edit.html'

class LocationDocumentDeleteView(generic.ObjectDeleteView):
    queryset = models.LocationDocument.objects.all()


### DeviceDocument
class DeviceDocumentView(generic.ObjectView):
    queryset = models.DeviceDocument.objects.all()

class DeviceDocumentListView(generic.ObjectListView):
    queryset = models.DeviceDocument.objects.all()
    table = tables.DeviceDocumentTable
    filterset = filtersets.DeviceDocumentFilterSet
    filterset_form = forms.DeviceDocumentFilterForm

class DeviceDocumentEditView(generic.ObjectEditView):
    queryset = models.DeviceDocument.objects.all()
    form = forms.DeviceDocumentForm

    template_name = 'netbox_documents/devicedocument_edit.html'

class DeviceDocumentDeleteView(generic.ObjectDeleteView):
    queryset = models.DeviceDocument.objects.all()


### VirtualMachineDocument
class VirtualMachineDocumentView(generic.ObjectView):
    queryset = models.VirtualMachineDocument.objects.all()

class VirtualMachineDocumentListView(generic.ObjectListView):
    queryset = models.VirtualMachineDocument.objects.all()
    table = tables.VirtualMachineDocumentTable
    filterset = filtersets.VirtualMachineDocumentFilterSet
    filterset_form = forms.VirtualMachineDocumentFilterForm

class VirtualMachineDocumentEditView(generic.ObjectEditView):
    queryset = models.VirtualMachineDocument.objects.all()
    form = forms.VirtualMachineDocumentForm

    template_name = 'netbox_documents/virtualmachinedocument_edit.html'

class VirtualMachineDocumentDeleteView(generic.ObjectDeleteView):
    queryset = models.VirtualMachineDocument.objects.all()

### DeviceTypeDocument
class DeviceTypeDocumentView(generic.ObjectView):
    queryset = models.DeviceTypeDocument.objects.all()

class DeviceTypeDocumentListView(generic.ObjectListView):
    queryset = models.DeviceTypeDocument.objects.all()
    table = tables.DeviceTypeDocumentTable
    filterset = filtersets.DeviceTypeDocumentFilterSet
    filterset_form = forms.DeviceTypeDocumentFilterForm

class DeviceTypeDocumentEditView(generic.ObjectEditView):
    queryset = models.DeviceTypeDocument.objects.all()
    form = forms.DeviceTypeDocumentForm

    template_name = 'netbox_documents/devicetypedocument_edit.html'

class DeviceTypeDocumentDeleteView(generic.ObjectDeleteView):
    queryset = models.DeviceTypeDocument.objects.all()

### CircuitDocument
class CircuitDocumentView(generic.ObjectView):
    queryset = models.CircuitDocument.objects.all()

class CircuitDocumentListView(generic.ObjectListView):
    queryset = models.CircuitDocument.objects.all()
    table = tables.CircuitDocumentTable
    filterset = filtersets.CircuitDocumentFilterSet
    filterset_form = forms.CircuitDocumentFilterForm

class CircuitDocumentEditView(generic.ObjectEditView):
    queryset = models.CircuitDocument.objects.all()
    form = forms.CircuitDocumentForm

    template_name = 'netbox_documents/circuitdocument_edit.html'

class CircuitDocumentDeleteView(generic.ObjectDeleteView):
    queryset = models.CircuitDocument.objects.all()