from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelBulkEditForm 
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

class EvpnVCBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=EvpnVC.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False
    )

    model = EvpnVC
    fieldsets = (
        (None, ('tenant',)),
    )

    class Meta:
        nullable_fields = [
            'tenant',
        ]

class EvpnVCVlanForm(NetBoxModelForm):
    evpn_vc = DynamicModelChoiceField(
        queryset=EvpnVC.objects.all()
    )
    vlan = DynamicModelChoiceField(
        queryset=VLAN.objects.all(),
        required=False
    )

    class Meta:
        model = EvpnVCVlan
        fields = ('evpn_vc', 'vlan',)

class EvpnVCFilterSetForm(NetBoxModelFilterSetForm):
    model = EvpnVC

    q = forms.CharField(
        required=False,
        label='Search'
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False
    )

class EvpnVCVlanFilterSetForm(NetBoxModelFilterSetForm):
    model = EvpnVCVlan

    evpn_vc = DynamicModelChoiceField(
        queryset=EvpnVC.objects.all(),
        required=False
    )
    vlan = DynamicModelChoiceField(
        queryset=VLAN.objects.all(),
        required=False
    )
