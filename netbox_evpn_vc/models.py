from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel

class EvpnVCType(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=200,
        blank=True
    )

    class Meta:
        ordering = ['name',]
        verbose_name = "VC type"
        verbose_name_plural = "VC types"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_evpn_vc:evpnvctype', args=[self.pk])

class EvpnVC(NetBoxModel):
    vni = models.BigIntegerField(
        verbose_name='VNI',
        validators=[
            MaxValueValidator(16777215),
            MinValueValidator(1),
        ],
    )
    name = models.CharField(
        max_length=100
    )
    vc_type = models.ForeignKey(
        to='EvpnVCType',
        related_name='evpns',
        on_delete=models.PROTECT,
    )
    comments = models.TextField(
        blank=True
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        related_name="evpnvcs",
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('vni',)
        verbose_name = 'EVPN Virtual Circuit'
        verbose_name_plural= 'EVPN Virtual Circuits'
        constraints = (
            models.UniqueConstraint(
                fields=('vni',),
                name='evpn_vc_vni'
            ),
        )

    def __str__(self):
        return f'{self.name} ({self.vni})'

    def get_absolute_url(self):
        return reverse('plugins:netbox_evpn_vc:evpnvc', args=[self.pk])

class EvpnVCVlan(NetBoxModel):
    evpn_vc = models.ForeignKey(
        to=EvpnVC,
        on_delete=models.CASCADE,
        related_name='vlans'
    )
    vlan = models.OneToOneField(
        to='ipam.Vlan',
        on_delete=models.PROTECT,
        related_name='evpnvcvlan',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['evpn_vc', 'vlan']
        verbose_name = "VNI to VLAN connection"
        verbose_name_plural = "VNI to VLAN connections"

    def get_absolute_url(self):
        return reverse('plugins:netbox_evpn_vc:evpnvcvlan', args=[self.pk])

