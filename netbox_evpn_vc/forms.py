from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
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
    vlan = DynamicModelChoiceField(
        queryset=EvpnVC.objects.all()
    )

    class Meta:
        model = EvpnVCVlan
        fields = ('evpn_vc', 'vlan',)
