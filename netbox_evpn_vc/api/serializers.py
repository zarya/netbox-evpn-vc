from rest_framework import serializers
from ipam.api.serializers import NestedVLANSerializer
from tenancy.api.nested_serializers import NestedTenantSerializer
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import EvpnVC, EvpnVCVlan 

class NestedEvpnVCSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_evpn_vc-api:evpnvc-detail'
    )
    tenant = NestedTenantSerializer(read_only=True)

    class Meta:
        model = EvpnVC 
        fields = ('id', 'url', 'display', 'name', 'tenant', 'vni')


class NestedEvpnVCVlanSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_evpn_vc-api:evpnvcvlan-detail'
    )
    vlan = NestedVLANSerializer(read_only=True)

    class Meta:
        model = EvpnVCVlan 
        fields = ('id', 'url', 'display', 'vlan', 'created', 'last_updated')

class EvpnVCSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_evpn_vc-api:evpnvc-detail'
    )

    vlan_count = serializers.IntegerField(read_only=True)
    vlans = NestedEvpnVCVlanSerializer(many=True, read_only=True) 
    tenant = NestedTenantSerializer(read_only=True)

    class Meta:
        model = EvpnVC
        fields = (
            'id', 'url', 'display', 'name', 'tenant', 'comments', 'vni', 'vlan_count', 'vlans', 'tags', 'custom_fields', 'created',
            'last_updated',
        )

class EvpnVCVlanSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_evpn_vc-api:evpnvcvlan-detail'
    )
    vlan = NestedVLANSerializer()
    evpn_vc = NestedEvpnVCSerializer()

    class Meta:
        model = EvpnVCVlan
        fields = (
            'id', 'url', 'display', 'evpn_vc', 'vlan', 
            'tags', 'custom_fields', 'created',
            'last_updated',
        )
