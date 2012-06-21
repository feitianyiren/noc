# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Huawei.VRP.get_switchport test
## Auto-generated by ./noc debug-script at 21.06.2012 12:21:05
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Huawei_VRP_get_switchport_Test(ScriptTestCase):
    script = "Huawei.VRP.get_switchport"
    vendor = "Huawei"
    platform = "S5328C-EI-24S"
    version = "5.70"
    input = {}
    result = [{'802.1Q Enabled': False,
  '802.1ad Tunnel': False,
  'description': 'Savchin_DC',
  'interface': 'GigabitEthernet0/0/1',
  'members': [],
  'status': True,
  'tagged': [],
  'untagged': 2111},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'KSF-SoftElegants_DC',
  'interface': 'GigabitEthernet0/0/2',
  'members': [],
  'status': True,
  'tagged': [1, 448, 449]},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'Mihaylovskaya7_I',
  'interface': 'GigabitEthernet0/0/3',
  'members': [],
  'status': True,
  'tagged': [1, 1000, 2010, 2560, 2561, 2562, 2563]},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'Krymskogo4a_I',
  'interface': 'GigabitEthernet0/0/4',
  'members': [],
  'status': True,
  'tagged': [1,
             43,
             1000,
             1001,
             1201,
             1202,
             1203,
             1204,
             1205,
             1206,
             1207,
             1208,
             1999,
             2006,
             2009,
             2010]},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'l9-sw9-gonty7-sw1_I',
  'interface': 'GigabitEthernet0/0/5',
  'members': [],
  'status': True,
  'tagged': [1, 1000, 2009, 2565]},
 {'802.1Q Enabled': False,
  '802.1ad Tunnel': False,
  'description': 'TopNet-Cust-TR_TR',
  'interface': 'GigabitEthernet0/0/6',
  'members': [],
  'status': True,
  'tagged': [],
  'untagged': 2562},
 {'802.1Q Enabled': False,
  '802.1ad Tunnel': False,
  'description': 'FASTY_IPTV',
  'interface': 'GigabitEthernet0/0/7',
  'members': [],
  'status': True,
  'tagged': [],
  'untagged': 2566},
 {'802.1Q Enabled': False,
  '802.1ad Tunnel': False,
  'description': 'USG-Glybochicka40_TR',
  'interface': 'GigabitEthernet0/0/8',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 2567},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'GigabitEthernet0/0/9',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'GigabitEthernet0/0/10',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'GigabitEthernet0/0/11',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'GigabitEthernet0/0/12',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'GigabitEthernet0/0/13',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'GigabitEthernet0/0/14',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'GigabitEthernet0/0/15',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'GigabitEthernet0/0/16',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'GigabitEthernet0/0/17',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'GigabitEthernet0/0/18',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'GigabitEthernet0/0/19',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'GigabitEthernet0/0/20',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'GigabitEthernet0/0/21',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'GigabitEthernet0/0/22',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'GigabitEthernet0/0/23',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'l9-sw9-n1-cr2_I',
  'interface': 'GigabitEthernet0/0/24',
  'members': [],
  'status': True,
  'tagged': [448,
             449,
             1000,
             1201,
             1202,
             1203,
             1204,
             1205,
             1206,
             1207,
             1208,
             1999,
             2006,
             2009,
             2010,
             2111,
             2560,
             2561,
             2562,
             2563,
             2565,
             2566,
             2567]}]
    motd = ''
    cli = {
## 'display interface brief'
'display interface brief': """display interface brief
PHY: Physical
*down: administratively down
^down: standby
(l): loopback
(s): spoofing
(b): BFD down
(e): ETHOAM down
(d): Dampening Suppressed
InUti/OutUti: input utility/output utility
Interface                   PHY   Protocol InUti OutUti   inErrors  outErrors
GigabitEthernet0/0/1        up    up       3.24%    15%          0          0
GigabitEthernet0/0/2        up    up       0.62%  0.97%          0          0
GigabitEthernet0/0/3        up    up       0.27%  0.28%          0          0
GigabitEthernet0/0/4        up    up       0.40%  1.17%         13          0
GigabitEthernet0/0/5        up    up       0.02%  0.59%          0          0
GigabitEthernet0/0/6        up    up       0.01%  0.01%          0          0
GigabitEthernet0/0/7        up    up       0.01%  0.01%          0          0
GigabitEthernet0/0/8        down  down        0%     0%          0          0
GigabitEthernet0/0/9        *down down        0%     0%          0          0
GigabitEthernet0/0/10       *down down        0%     0%          0          0
GigabitEthernet0/0/11       *down down        0%     0%          0          0
GigabitEthernet0/0/12       *down down        0%     0%          0          0
GigabitEthernet0/0/13       *down down        0%     0%          0          0
GigabitEthernet0/0/14       *down down        0%     0%          0          0
GigabitEthernet0/0/15       *down down        0%     0%          0          0
GigabitEthernet0/0/16       *down down        0%     0%          0          0
GigabitEthernet0/0/17       *down down        0%     0%          0          0
GigabitEthernet0/0/18       *down down        0%     0%          0          0
GigabitEthernet0/0/19       *down down        0%     0%          0          0
GigabitEthernet0/0/20       *down down        0%     0%          0          0
GigabitEthernet0/0/21       *down down        0%     0%          0          0
GigabitEthernet0/0/22       *down down        0%     0%          0          0
GigabitEthernet0/0/23       *down down        0%     0%          0          0
GigabitEthernet0/0/24       up    up         18%  4.56%          0          0
MEth0/0/1                   down  down        0%     0%          0          0
NULL0                       up    up(s)       0%     0%          0          0
Vlanif1                     *down down        --     --          0          0
Vlanif1000                  up    up          --     --          0          0""", 
'display eth-trunk':  'display eth-trunk\nInfo: No valid trunk in the system.\n', 
## 'display version'
'display version': """display version
Huawei Versatile Routing Platform Software
VRP (R) software, Version 5.70 (S5300 V100R005C01SPC100)
Copyright (C) 2000-2011 HUAWEI TECH CO., LTD
Quidway S5328C-EI-24S Routing Switch uptime is 0 week, 1 day, 21 hours, 52 minutes

EFGF 0(Master) : uptime is 0 week, 1 day, 21 hours, 52 minutes
256M bytes DDR Memory
32M bytes FLASH
Pcb      Version :  VER B
Basic  BOOTROM  Version :  107 Compiled at Jan 18 2011, 22:52:53
CPLD   Version : 69 
Software Version : VRP (R) Software, Version 5.70 (S5300 V100R005C01SPC100)
FANCARD information
Pcb      Version : FAN VER B
PWRCARD I information
Pcb      Version : PWR VER A
""", 
## 'display interface description'
'display interface description': """display interface description
Interface                   Description                   
GigabitEthernet0/0/1        Savchin_DC                                         
GigabitEthernet0/0/2        KSF-SoftElegants_DC                                
GigabitEthernet0/0/3        Mihaylovskaya7_I                                   
GigabitEthernet0/0/4        Krymskogo4a_I                                      
GigabitEthernet0/0/5        l9-sw9-gonty7-sw1_I                                
GigabitEthernet0/0/6        TopNet-Cust-TR_TR                                  
GigabitEthernet0/0/7        FASTY_IPTV                                         
GigabitEthernet0/0/8        USG-Glybochicka40_TR                               
GigabitEthernet0/0/9        HUAWEI, Quidway Series, GigabitEthernet0/0/9 Interf
                            ace                                                
GigabitEthernet0/0/10       HUAWEI, Quidway Series, GigabitEthernet0/0/10 Inter
                            face                                               
GigabitEthernet0/0/11       HUAWEI, Quidway Series, GigabitEthernet0/0/11 Inter
                            face                                               
GigabitEthernet0/0/12       HUAWEI, Quidway Series, GigabitEthernet0/0/12 Inter
                            face                                               
GigabitEthernet0/0/13       HUAWEI, Quidway Series, GigabitEthernet0/0/13 Inter
                            face                                               
GigabitEthernet0/0/14       HUAWEI, Quidway Series, GigabitEthernet0/0/14 Inter
                            face                                               
GigabitEthernet0/0/15       HUAWEI, Quidway Series, GigabitEthernet0/0/15 Inter
                            face                                               
GigabitEthernet0/0/16       HUAWEI, Quidway Series, GigabitEthernet0/0/16 Inter
                            face                                               
GigabitEthernet0/0/17       HUAWEI, Quidway Series, GigabitEthernet0/0/17 Inter
                            face                                               
GigabitEthernet0/0/18       HUAWEI, Quidway Series, GigabitEthernet0/0/18 Inter
                            face                                               
GigabitEthernet0/0/19       HUAWEI, Quidway Series, GigabitEthernet0/0/19 Inter
                            face                                               
GigabitEthernet0/0/20       HUAWEI, Quidway Series, GigabitEthernet0/0/20 Inter
                            face                                               
GigabitEthernet0/0/21       HUAWEI, Quidway Series, GigabitEthernet0/0/21 Inter
                            face                                               
GigabitEthernet0/0/22       HUAWEI, Quidway Series, GigabitEthernet0/0/22 Inter
                            face                                               
GigabitEthernet0/0/23       HUAWEI, Quidway Series, GigabitEthernet0/0/23 Inter
                            face                                               
GigabitEthernet0/0/24       l9-sw9-n1-cr2_I                                    
MEth0/0/1                   HUAWEI, Quidway Series, MEth0/0/1 Interface        
NULL0                       HUAWEI, Quidway Series, NULL0 Interface            
Vlanif1                     HUAWEI, Quidway Series, Vlanif1 Interface          
Vlanif1000                  HUAWEI, Quidway Series, Vlanif1000 Interface       """, 
## 'display port vlan'
'display port vlan': """display port vlan
Port                    Link Type    PVID  Trunk VLAN List
-------------------------------------------------------------------------------
GigabitEthernet0/0/1    access       2111  -                                   
GigabitEthernet0/0/2    trunk        1     1 448-449
GigabitEthernet0/0/3    trunk        1     1 1000 2010 2560-2564
GigabitEthernet0/0/4    trunk        1     1 43 1000-1001 1201-1208 1999 2006 
                                           2009-2010
GigabitEthernet0/0/5    trunk        1     1 1000 2009 2565
GigabitEthernet0/0/6    access       2562  -                                   
GigabitEthernet0/0/7    access       2566  -                                   
GigabitEthernet0/0/8    access       2567  -                                   
GigabitEthernet0/0/9    hybrid       1     -                                   
GigabitEthernet0/0/10   hybrid       1     -                                   
GigabitEthernet0/0/11   hybrid       1     -                                   
GigabitEthernet0/0/12   hybrid       1     -                                   
GigabitEthernet0/0/13   hybrid       1     -                                   
GigabitEthernet0/0/14   hybrid       1     -                                   
GigabitEthernet0/0/15   hybrid       1     -                                   
GigabitEthernet0/0/16   hybrid       1     -                                   
GigabitEthernet0/0/17   hybrid       1     -                                   
GigabitEthernet0/0/18   hybrid       1     -                                   
GigabitEthernet0/0/19   hybrid       1     -                                   
GigabitEthernet0/0/20   hybrid       1     -                                   
GigabitEthernet0/0/21   hybrid       1     -                                   
GigabitEthernet0/0/22   hybrid       1     -                                   
GigabitEthernet0/0/23   hybrid       1     -                                   
GigabitEthernet0/0/24   trunk        1     448-449 1000 1201-1208 1999 2006 
                                           2009-2010 2111 2560-2579""", 
## 'display vlan'
'display vlan': """display vlan
* : management-vlan
---------------------
The total number of vlans is : 26
VLAN ID Type         Status   MAC Learning Broadcast/Multicast/Unicast Property 
--------------------------------------------------------------------------------
1       common       enable   enable       forward   forward   forward default  
43      common       enable   enable       forward   forward   forward default  
448     common       enable   enable       forward   forward   forward default  
449     common       enable   enable       forward   forward   forward default  
1000    *common      enable   enable       forward   forward   forward default  
1001    common       enable   enable       forward   forward   forward default  
1201    common       enable   enable       forward   forward   forward default  
1202    common       enable   enable       forward   forward   forward default  
1203    common       enable   enable       forward   forward   forward default  
1204    common       enable   enable       forward   forward   forward default  
1205    common       enable   enable       forward   forward   forward default  
1206    common       enable   enable       forward   forward   forward default  
1207    common       enable   enable       forward   forward   forward default  
1208    common       enable   enable       forward   forward   forward default  
1999    common       enable   enable       forward   forward   forward default  
2006    common       enable   enable       forward   forward   forward default  
2009    common       enable   enable       forward   forward   forward default  
2010    common       enable   enable       forward   forward   forward default  
2111    common       enable   enable       forward   forward   forward default  
2560    common       enable   enable       forward   forward   forward default  
2561    common       enable   enable       forward   forward   forward default  
2562    common       enable   enable       forward   forward   forward default  
2563    common       enable   enable       forward   forward   forward default  
2565    common       enable   enable       forward   forward   forward default  
2566    common       enable   enable       forward   forward   forward default  
2567    common       enable   enable       forward   forward   forward default  """, 
'screen-length 0 temporary':  'screen-length 0 temporary\nInfo: The configuration takes effect on the current user terminal interface only.\n', 
}
    snmp_get = {}
    snmp_getnext = {}
    http_get = {}
