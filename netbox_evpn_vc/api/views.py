from django.db.models import Count

from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import EvpnVCSerializer, EvpnVCVlanSerializer, EvpnVCTypeSerializer


class EvpnVCViewSet(NetBoxModelViewSet):
    queryset = models.EvpnVC.objects.prefetch_related('tags', 'vlans').annotate(
        vlan_count=Count('vlans')
    )
    serializer_class = EvpnVCSerializer
    filterset_class = filtersets.EvpnVCFilterSet


class EvpnVCVlanViewSet(NetBoxModelViewSet):
    queryset = models.EvpnVCVlan.objects.prefetch_related(
        'vlan', 'tags', 'evpn_vc'
    )
    serializer_class = EvpnVCVlanSerializer
    filterset_class = filtersets.EvpnVCVlanFilterSet

class EvpnVCTypeViewSet(NetBoxModelViewSet):
    queryset = models.EvpnVCType.objects.prefetch_related(
        'tags',
    )
    serializer_class = EvpnVCTypeSerializer
    filterset_class = filtersets.EvpnVCTypeFilterSet
