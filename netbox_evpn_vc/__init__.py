from extras.plugins import PluginConfig

class NetBoxEvpnVCConfig(PluginConfig):
    name = 'netbox_evpn_vc'
    verbose_name = 'EVPN Virtual Circuit'
    description = 'Manage EVPN Virtual Circuit'
    version = '0.1'
    base_url = 'evpn-vc'
    min_version = '3.2.0'

config = NetBoxEvpnVCConfig
