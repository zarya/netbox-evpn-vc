import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import EvpnVC, EvpnVCVlan 

class EvpnVCTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    vlan_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = EvpnVC 
        fields = ('pk', 'vni', 'name', 'comments', 'tenant', 'vlan_count')
        default_columns = ('vni','name', 'tenant', 'vlan_count')

class EvpnVCVlanTable(NetBoxTable):
    evpn_vc = tables.Column(
        linkify=True
    )
    index = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = EvpnVCVlan
        fields = (
            'pk','index', 'evpn_vc', 'vlan',
        )
        default_columns = (
            'pk','index', 'evpn_vc', 'vlan',
        )
