from extras.plugins import PluginConfig

class NetBoxEvpnVCConfig(PluginConfig):
    name = 'netbox_evpn_vc'
    verbose_name = ' NetBox EVPN Virtual Curcuit'
    description = 'Manage EVPN Virtual Circuit'
    version = '0.1'
    base_url = 'evpn_vc'

config = NetBoxEvpnVCConfig
