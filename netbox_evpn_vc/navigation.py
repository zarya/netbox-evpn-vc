from extras.plugins import PluginMenuItem

evpnvc_buttons = [
    PluginMenuButton(
        link='plugins:netbox_evpn_vc:evpnvc_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

evpnvcvlan_buttons = [
    PluginMenuButton(
        link='plugins:netbox_evpn_vc:evpnvcvlan_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_evpn_vc:evpnvc_list',
        link_text='EVPN VCs',
        buttons=evpnvc_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_evpn_vc:evpnvcvlan_list',
        link_text='EVPN VC-VLANs',
        buttons=evpnvcvlan_buttons
    ),
)
