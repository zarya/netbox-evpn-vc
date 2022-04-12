from netbox.api.routers import NetBoxRouter
from . import views


app_name = 'netbox_evpn_vc'

router = NetBoxRouter()
router.register('evpn-vcs', views.EvpnVCViewSet)
router.register('evpn-vc-vlans', views.EvpnVCVlanViewSet)

urlpatterns = router.urls
