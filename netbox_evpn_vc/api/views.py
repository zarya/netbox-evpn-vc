from django.db.models import Count

from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import EvpnVCSerializer, EvpnVCVlanSerializer


class EvpnVCViewSet(NetBoxModelViewSet):
    queryset = models.EvpnVC.objects.prefetch_related('tags').annotate(
        vlan_count=Count('vlans')
    )
    serializer_class = EvpnVCSerializer


class EvpnVCVlanViewSet(NetBoxModelViewSet):
    queryset = models.AccessListRule.objects.prefetch_related(
        'vlan', 'tags'
    )
    serializer_class = EvpnVCVlanSerializer
    filterset_class = filtersets.EvpnVCVlanFilterSet
