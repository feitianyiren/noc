# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Alcatel.OS62xx.get_version test
## Auto-generated by ./noc debug-script at 2011-10-24 15:53:37
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Alcatel_OS62xx_get_version_Test(ScriptTestCase):
    script = "Alcatel.OS62xx.get_version"
    vendor = "Alcatel"
    platform = 'OmniStack LS 6224'
    version = '1.0.0.13'
    input = {}
    result = {'attributes': {'Boot PROM': '1.0.0.13',
                'HW version': '00.00.01',
                'Serial Number': 'H2282837'},
 'platform': 'OmniStack LS 6224',
 'vendor': 'Alcatel',
 'version': '1.7.1.7'}
    motd = '********\n\n'
    cli = {
'terminal datadump':  ' terminal datadump\n', 
}
    snmp_get = {'1.3.6.1.2.1.47.1.1.1.1.10.67108992': '1.7.1.7',
 '1.3.6.1.2.1.47.1.1.1.1.11.67108992': 'H2282837',
 '1.3.6.1.2.1.47.1.1.1.1.7.68420352': 'OmniStack LS 6224',
 '1.3.6.1.2.1.47.1.1.1.1.8.67108992': '00.00.01',
 '1.3.6.1.2.1.47.1.1.1.1.9.67108992': '1.0.0.13'}
    snmp_getnext = {}
