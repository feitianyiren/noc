# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## EdgeCore.ES.get_portchannel test
## Auto-generated by manage.py debug-script at 2011-02-07 17:51:30
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
from noc.lib.test import ScriptTestCase
class EdgeCore_ES_get_portchannel_Test(ScriptTestCase):
    script="EdgeCore.ES.get_portchannel"
    vendor="EdgeCore"
    platform='ES4626-SFP'
    version='5.4.156.0'
    input={}
    result=[{'interface': 'Port-Channel1',
  'members': ['Ethernet1/3', 'Ethernet1/1', 'Ethernet1/6'],
  'type': 'S'},
 {'interface': 'Port-Channel2', 'members': [], 'type': 'S'},
 {'interface': 'Port-Channel3',
  'members': ['Ethernet1/5', 'Ethernet1/7', 'Ethernet1/8'],
  'type': 'S'}]
    motd='********\n'
    cli={
## 'show version 1'
'show version 1': """show version 1
  ES4626-SFP Device, Compiled Mar 19 13:40:24 2009
  SoftWare Package Version ES4626-SFP_5.4.156.0
  BootRom Version ES4626-SFP_1.6.5
  HardWare Version 3.0
  Copyright (C) 2001-2007 by Accton Technology Corp.
  All rights reserved.
  Last reboot is cold reset.
  Uptime is 9 weeks, 6 days, 9 hours, 55 minutes.""",
## 'show port-group 1 port-channel'
'show port-group 1 port-channel': """show port-group 1 port-channel
Port channels in the group 1:
-----------------------------------------------------------
Port-Channel: port-channel1
Number of port : 3      Standby port : NULL

Port in the port-channel : 

Index         Port           Mode
---------------------------------------
1             Ethernet1/3    on
2             Ethernet1/1    on
3             Ethernet1/6    on

""",
'show port-group 2 port-channel':  "show port-group 2 port-channel\nThe port-group 2 hasn't formed any port-channel.\n\n",
## 'show port-group 3 port-channel'
'show port-group 3 port-channel': """show port-group 3 port-channel
Port channels in the group 3:
-----------------------------------------------------------
Port-Channel: port-channel3
Number of port : 3      Standby port : NULL

Port in the port-channel : 

Index         Port           Mode
---------------------------------------
1             Ethernet1/5    on
2             Ethernet1/7    on
3             Ethernet1/8    on

""",
## 'show port-group brief'
'show port-group brief': """show port-group brief
Port-group number : 1 
the attributes of the port-group are as follows:

Number of ports in port-group : 3   Maxports in port-channel = 8
Number of port-channels : 1   Max port-channels : 1

Port-group number : 2 
Number of ports in port-group : 2   Maxports in port-channel = 8
Number of port-channels : 0   Max port-channels : 1

Port-group number : 3 
the attributes of the port-group are as follows:

Number of ports in port-group : 3   Maxports in port-channel = 8
Number of port-channels : 1   Max port-channels : 1
""",
## 'show system'
'show system': """show system
                   ^
% Invalid input detected at '^' marker.
""",
}
    snmp_get={}
    snmp_getnext={}
