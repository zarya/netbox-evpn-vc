import django_filters
from netbox.filtersets import NetBoxModelFilterSet
from .models import EvpnVC, EvpnVCVlan 
from django.db.models import Q


class EvpnVCFilterSet(NetBoxModelFilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )

    class Meta:
        model = EvpnVC
        fields = ('id', 'name', 'vni', 'tenant')

    def search(self, queryset, name, value):
        qs_filter = (
                  Q(id__icontains=value)
                | Q(name__icontains=value)
                | Q(vni__icontains=value)
        )
        return queryset.filter(qs_filter)

class EvpnVCVlanFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = EvpnVCVlan 
        fields = ('id', 'evpn_vc')

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)
