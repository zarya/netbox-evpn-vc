import django_filters
from netbox.filtersets import NetBoxModelFilterSet
from .models import EvpnVC, EvpnVCVlan, EvpnVCType 
from django.db.models import Q


class EvpnVCTypeFilterSet(NetBoxModelFilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )

    class Meta:
        model = EvpnVCType
        fields = ('id', 'name', 'description',)

    def search(self, queryset, name, value):
        qs_filter = (Q(name__icontains=value))
        return queryset.filter(qs_filter)

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
        fields = ('id', 'evpn_vc', 'vlan')

    def search(self, queryset, name, value):
        qs_filter = (
                  Q(id__icontains=value)
                | Q(vlan__name__icontains=value)
                | Q(evpn_vc__name__icontains=value)
        )
        return queryset.filter(qs_filter)
