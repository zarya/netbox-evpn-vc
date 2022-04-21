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
    table = tables.EvpnVCTable
    filterset = filtersets.EvpnVCFilterSet
    filterset_form = forms.EvpnVCFilterSetForm
    queryset = models.EvpnVC.objects.annotate(
        vlan_count=Count('vlans')
    )

class EvpnVCEditView(generic.ObjectEditView):
    queryset = models.EvpnVC.objects.all()
    form = forms.EvpnVCForm

class EvpnVCBulkEditView(generic.BulkEditView):
    queryset = models.EvpnVC.objects.all()
    filterset = filtersets.EvpnVCFilterSet 
    table = tables.EvpnVCTable
    form = forms.EvpnVCBulkEditForm

class EvpnVCDeleteView(generic.ObjectDeleteView):
    queryset = models.EvpnVC.objects.all()

class EvpnVCBulkDeleteView(generic.BulkDeleteView):
    queryset = models.EvpnVC.objects.annotate()
    filterset = filtersets.EvpnVCFilterSet
    table = tables.EvpnVCTable

class EvpnVCVlanView(generic.ObjectView):
    queryset = models.EvpnVCVlan.objects.all()

class EvpnVCVlanListView(generic.ObjectListView):
    table = tables.EvpnVCVlanListTable
    filterset = filtersets.EvpnVCVlanFilterSet
    filterset_form = forms.EvpnVCVlanFilterSetForm
    queryset = models.EvpnVCVlan.objects.all()

class EvpnVCVlanEditView(generic.ObjectEditView):
    queryset = models.EvpnVCVlan.objects.all()
    form = forms.EvpnVCVlanForm

class EvpnVCVlanDeleteView(generic.ObjectDeleteView):
    queryset = models.EvpnVCVlan.objects.all()

class EvpnVCVlanBulkDeleteView(generic.BulkDeleteView):
    queryset = models.EvpnVCVlan.objects.annotate()
    filterset = filtersets.EvpnVCVlanFilterSet
    table = tables.EvpnVCVlanListTable
