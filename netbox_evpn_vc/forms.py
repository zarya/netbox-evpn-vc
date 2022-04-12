from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from ipam.models import VLAN
from tenancy.models import Tenant
from .models import EvpnVC, EvpnVCVlan

class EvpnVCForm(NetBoxModelForm):
    comments = CommentField()
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False
    )

    class Meta:
        model = EvpnVC 
        fields = ('vni', 'name', 'comments', 'tenant')

class EvpnVCVlanForm(NetBoxModelForm):
    evpn_vc = DynamicModelChoiceField(
        queryset=EvpnVC.objects.all()
    )
    vlan = DynamicModelChoiceField(
        queryset=VLAN.objects.all()
    )

    class Meta:
        model = EvpnVCVlan
        fields = ('evpn_vc', 'vlan',)
