from netbox.filtersets import NetBoxModelFilterSet
from .models import EvpnVC, EvpnVCVlan 


class EvpnVCFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = EvpnVC
        fields = ('id', 'name', 'vni')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)

class EvpnVCVlanFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = EvpnVCVlan 
        fields = ('id', 'evpn_vc')

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)
