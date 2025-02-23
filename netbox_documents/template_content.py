from extras.plugins import PluginTemplateExtension
from django.conf import settings
from .models import SiteDocument, LocationDocument, DeviceDocument, VirtualMachineDocument, DeviceTypeDocument, CircuitDocument 

plugin_settings = settings.PLUGINS_CONFIG.get('netbox_documents', {})

class SiteDocumentList(PluginTemplateExtension):
    model = 'dcim.site'

    def left_page(self):

        if plugin_settings.get('enable_site_documents') and plugin_settings.get('site_documents_location') == 'left':

            return self.render('netbox_documents/sitedocument_include.html', extra_context={
                'site_documents': SiteDocument.objects.filter(site=self.context['object']),
            })

        else:
            return ""

    def right_page(self):

        if plugin_settings.get('enable_site_documents') and plugin_settings.get('site_documents_location') == 'right':

            return self.render('netbox_documents/sitedocument_include.html', extra_context={
                'site_documents': SiteDocument.objects.filter(site=self.context['object']),
            })

        else:
            return ""


class LocationDocumentList(PluginTemplateExtension):
    model = 'dcim.location'

    def left_page(self):

        if plugin_settings.get('enable_location_documents') and plugin_settings.get('location_documents_location') == 'left':

            return self.render('netbox_documents/locationdocument_include.html', extra_context={
                'location_documents': LocationDocument.objects.filter(location=self.context['object']),
            })

        else:
            return ""

    def right_page(self):

        if plugin_settings.get('enable_location_documents') and plugin_settings.get('location_documents_location') == 'right':

            return self.render('netbox_documents/locationdocument_include.html', extra_context={
                'location_documents': LocationDocument.objects.filter(location=self.context['object']),
            })

        else:
            return ""


class DeviceDocumentList(PluginTemplateExtension):
    model = 'dcim.device'

    def left_page(self):

        if plugin_settings.get('enable_device_documents') and plugin_settings.get('device_documents_location') == 'left':

            return self.render('netbox_documents/devicedocument_include.html', extra_context={
                'device_documents': DeviceDocument.objects.filter(device=self.context['object']),
            })

        else:
            return ""

    def right_page(self):

        if plugin_settings.get('enable_device_documents') and plugin_settings.get('device_documents_location') == 'right':

            return self.render('netbox_documents/devicedocument_include.html', extra_context={
                'device_documents': DeviceDocument.objects.filter(device=self.context['object']),
            })

        else:
            return ""


class VirtualMachineDocumentList(PluginTemplateExtension):
    model = 'virtualization.virtualmachine'

    def left_page(self):

        if plugin_settings.get('enable_virtual_machine_documents') and plugin_settings.get('virtual_machine_documents_location') == 'left':

            return self.render('netbox_documents/virtualmachinedocument_include.html', extra_context={
                'virtual_machine_documents': VirtualMachineDocument.objects.filter(virtual_machine=self.context['object']),
            })

        else:
            return ""

    def right_page(self):

        if plugin_settings.get('enable_virtual_machine_documents') and plugin_settings.get('virtual_machine_documents_location') == 'right':

            return self.render('netbox_documents/virtualmachinedocument_include.html', extra_context={
                'virtual_machine_documents': VirtualMachineDocument.objects.filter(virtual_machine=self.context['object']),
            })

        else:
            return ""


class DeviceTypeDocumentList(PluginTemplateExtension):
    model = 'dcim.devicetype'

    def left_page(self):

        if plugin_settings.get('enable_device_type_documents') and plugin_settings.get('device_type_documents_location') == 'left':

            return self.render('netbox_documents/devicetypedocument_include.html', extra_context={
                'device_type_documents': DeviceTypeDocument.objects.filter(device_type=self.context['object']),
            })

        else:
            return ""

    def right_page(self):

        if plugin_settings.get('enable_device_type_documents') and plugin_settings.get('device_type_documents_location') == 'right':

            return self.render('netbox_documents/devicetypedocument_include.html', extra_context={
                'device_type_documents': DeviceTypeDocument.objects.filter(device_type=self.context['object']),
            })

        else:
            return ""

class CircuitDocumentList(PluginTemplateExtension):
    model = 'circuits.circuit'

    def left_page(self):

        if plugin_settings.get('enable_circuit_documents') and plugin_settings.get('circuit_documents_location') == 'left':

            return self.render('netbox_documents/circuitdocument_include.html', extra_context={
                'circuit_documents': CircuitDocument.objects.filter(circuit=self.context['object']),
            })

        else:
            return ""

    def right_page(self):

        if plugin_settings.get('enable_circuit_documents') and plugin_settings.get('circuit_documents_location') == 'right':

            return self.render('netbox_documents/circuitdocument_include.html', extra_context={
                'circuit_documents': CircuitDocument.objects.filter(circuit=self.context['object']),
            })

        else:
            return ""

template_extensions = [SiteDocumentList, LocationDocumentList, DeviceDocumentList, DeviceTypeDocumentList, CircuitDocumentList, VirtualMachineDocumentList]