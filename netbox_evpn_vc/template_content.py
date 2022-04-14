from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from extras.plugins import PluginTemplateExtension


class EvpnVCVLANStatus(PluginTemplateExtension):
    model = "ipam.vlan"
    def left_page(self):
        vlan = self.context["object"]
        template_filename = "netbox_evpn_vc/vlan_evpn_vc.html"

        try:
            return self.render(
                template_filename, extra_context={"evpnvcvlan": vlan.evpnvcvlan}
            )
        except ObjectDoesNotExist:
            return ""

template_extensions = [EvpnVCVLANStatus]
