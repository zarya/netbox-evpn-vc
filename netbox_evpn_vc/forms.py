from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from .models import EvpnVC, EvpnVCVlan

class EvpnVCForm(NetBoxModelForm):
    comments = CommentField()
    tenant = DynamicModelChoiceField(
        queryset=EvpnVC.objects.all()
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
