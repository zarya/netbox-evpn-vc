# NetBox EVPN VC plugin 
[Netbox](https://github.com/netbox-community/netbox) plugin for storing evpn vc configuration (vni-vlan links) 

## Compatibility

|             |     |
|-------------|-----|
| NetBox 3.2  | 0.1 |

## Installation

The plugin can be installed with pip directly from github

```
pip install git+https://github.com/zarya/netbox-evpn-vc.git 
```
Enable the plugin in netbox/configuration.py look for the line starting with PLUGINS:
```
PLUGINS = ['netbox_evpn_vc']
```
Restart NetBox and add `git+https://github.com/zarya/netbox-evpn-vc.git` to your local_requirements.txt

