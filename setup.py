#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-balena-wifi-setup.openvoiceos=ovos_skill_balena_wifi_setup:WifiConnectSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-balena-wifi-setup',
    version='0.0.1',
    description='OVOS balena-wifi-setup skill plugin',
    url='https://github.com/OpenVoiceOS/skill-balena-wifi-setup',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"ovos_skill_balena_wifi_setup": ""},
    package_data={'ovos_skill_balena_wifi_setup': ['locale/*', "ui/*"]},
    packages=['ovos_skill_balena_wifi_setup'],
    include_package_data=True,
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
