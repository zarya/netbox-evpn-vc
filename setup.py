from setuptools import find_packages, setup

setup(
    name='netbox-evpn-vc',
    version='0.2',
    description='Netbox EVPN Virtual Circuit',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    package_data={
        '': ['*.html']
    },
    exclude_package_data={
        '': ["README.txt"]
    },
)
