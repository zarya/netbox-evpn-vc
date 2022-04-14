from graphene import ObjectType
from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.fields import ObjectField, ObjectListField
from . import filtersets, models

class EvpnVCType(NetBoxObjectType):

    class Meta:
        model = models.EvpnVC
        fields = '__all__'


class EvpnVCVlanType(NetBoxObjectType):

    class Meta:
        model = models.EvpnVCVlan
        fields = '__all__'
        filterset_class = filtersets.EvpnVCVlanFilterSet


class Query(ObjectType):
    evpn_vc = ObjectField(EvpnVCType)
    evpn_vc_list = ObjectListField(EvpnVCType)

    evpn_vc_vlan = ObjectField(EvpnVCVlanType)
    evpn_vc_vlan_list = ObjectListField(EvpnVCVlanType)
