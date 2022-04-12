from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel

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
    comments = models.TextField(
        blank=True
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('vni',)
        verbose_name = 'EVPN Virtual Circuit'
        verbose_name_plural= 'EVPN Virtual Circuits'

    def __str__(self):
        return f'{self.vni} (){self.name})'

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
        related_name='+',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['evpn_vc']
        verbose_name = "VNI to VLAN connection"
        verbose_name_plural = "VNI to VLAN connections"

    def get_absolute_url(self):
        return reverse('plugins:netbox_evpn_vc:evpnvcvlan', args=[self.pk])


