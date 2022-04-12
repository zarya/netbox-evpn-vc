from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    path('evpn-vcs/', views.EvpnVCListView.as_view(), name='evpnvc_list'),
    path('evpn-vcs/add/', views.EvpnVCEditView.as_view(), name='evpnvc_add'),
    path('evpn-vcs/<int:pk>/', views.EvpnVCView.as_view(), name='evpnvc'),
    path('evpn-vcs/<int:pk>/edit/', views.EvpnVCEditView.as_view(), name='evpnvc_edit'),
    path('evpn-vcs/<int:pk>/delete/', views.EvpnVCDeleteView.as_view(), name='evpnvc_delete'),
    path('evpn-vcs/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='evpnvc_changelog', kwargs={
        'model': models.EvpnVC
    }),
    # VLAN rules
    path('evpn-vc-vlan/', views.EvpnVCVlanListView.as_view(), name='evpnvcvlan_list'),
    path('evpn-vc-vlan/add/', views.EvpnVCVlanEditView.as_view(), name='evpnvcvlan_add'),
    path('evpn-vc-vlan/<int:pk>/', views.EvpnVCVlanView.as_view(), name='evpnvcvlan'),
    path('evpn-vc-vlan/<int:pk>/edit/', views.EvpnVCVlanEditView.as_view(), name='evpnvcvlan_edit'),
    path('evpn-vc-vlan/<int:pk>/delete/', views.EvpnVCVlanDeleteView.as_view(), name='evpnvcvlan_delete'),
    path('evpn-vc-vlan/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='evpnvc_changelog', kwargs={
        'model': models.EvpnVCVlan
    }),

    )
