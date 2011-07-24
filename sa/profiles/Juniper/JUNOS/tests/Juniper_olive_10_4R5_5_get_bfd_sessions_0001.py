# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Juniper.JUNOS.get_bfd_sessions test
## Auto-generated by ./noc debug-script at 2011-07-25 01:19:02
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Juniper_JUNOS_get_bfd_sessions_Test(ScriptTestCase):
    script = "Juniper.JUNOS.get_bfd_sessions"
    vendor = "Juniper"
    platform = 'olive'
    version = '10.4R5.5'
    input = {}
    result = [{'detect_time': 600000,
  'interface': 'em1.0',
  'multiplier': 3,
  'peer': '10.99.2.2',
  'state': True,
  'tx_interval': 200000}]
    motd = '--- JUNOS 10.4R5.5 built 2011-06-14 02:02:06 UTC\n'
    cli = {
'set cli screen-length 0':  ' set cli screen-length 0 \nScreen length set to 0\n\n', 
## 'show bfd session'
'show bfd session': """ show bfd session 
                                                  Detect   Transmit
Address                  State     Interface      Time     Interval  Multiplier
10.99.2.2                Up        em1.0          0.600     0.200        3   

1 sessions, 1 clients
Cumulative transmit rate 5.0 pps, cumulative receive rate 5.0 pps
""", 
}
    snmp_get = {}
    snmp_getnext = {}
