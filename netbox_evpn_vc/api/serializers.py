from rest_framework import serializers
from ipam.api.serializers import NestedPrefixSerializer
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import EvpnVC, EvpnVCVlan 

class NestedEvpnVCSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_evpn_vc-api:evpnvc-detail'
    )

    class Meta:
        model = EvpnVC 
        fields = ('id', 'url', 'display', 'name')


class NestedEvpnVCVlanSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_evpn_vc-api:evpnvcvlan-detail'
    )

    class Meta:
        model = EvpnVCVlan 
        fields = ('id', 'url', 'display', 'index')

class EvpnVCSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_evpn_vc-api:evpnvc-detail'
    )
    vlan_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = EvpnVC
        fields = (
            'id', 'display', 'name', 'default_action', 'comments', 'vlan_count', 'tags', 'custom_fields', 'created',
            'last_updated',
        )

class EvpnVCVlanSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_evpn_vc-api:evpnvcvlan-detail'
    )
    vlan = NestedPrefixSerializer()

    class Meta:
        model = EvpnVCVlan
        fields = (
            'id', 'evpn_vc', 'vlan', 
            'tags', 'custom_fields', 'created',
            'last_updated',
        )
