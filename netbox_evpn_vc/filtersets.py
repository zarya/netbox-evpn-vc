from netbox.filtersets import NetBoxModelFilterSet
from .models import EvpnVCVlan 


class EvpnVCVlanFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = EvpnVCVlan 
        fields = ('id', 'evpn_vc', 'index')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
