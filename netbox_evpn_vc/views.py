from netbox.views import generic
from django.db.models import Count
from . import forms, models, tables, filtersets

class EvpnVCView(generic.ObjectView):
    queryset = models.EvpnVC.objects.all()
        
    def get_extra_context(self, request, instance):
        table = tables.EvpnVCVlanTable(instance.vlans.all())
        table.configure(request)

        return {
            'vlans_table': table,
        }

class EvpnVCListView(generic.ObjectListView):
    queryset = models.EvpnVC.objects.all()
    table = tables.EvpnVCTable
    queryset = models.EvpnVC.objects.annotate(
        vlan_count=Count('vlans')
    )

class EvpnVCEditView(generic.ObjectEditView):
    queryset = models.EvpnVC.objects.all()
    form = forms.EvpnVCForm

class EvpnVCDeleteView(generic.ObjectDeleteView):
    queryset = models.EvpnVC.objects.all()

class EvpnVCBulkDeleteView(generic.BulkDeleteView):
    queryset = models.EvpnVC.objects.annotate()
    filterset = filtersets.EvpnVCFilterSet
    table = tables.EvpnVCTable

class EvpnVCVlanView(generic.ObjectView):
    queryset = models.EvpnVCVlan.objects.all()

class EvpnVCVlanListView(generic.ObjectListView):
    queryset = models.EvpnVCVlan.objects.all()
    table = tables.EvpnVCVlanTable

class EvpnVCVlanEditView(generic.ObjectEditView):
    queryset = models.EvpnVCVlan.objects.all()
    form = forms.EvpnVCVlanForm

class EvpnVCVlanDeleteView(generic.ObjectDeleteView):
    queryset = models.EvpnVCVlan.objects.all()
