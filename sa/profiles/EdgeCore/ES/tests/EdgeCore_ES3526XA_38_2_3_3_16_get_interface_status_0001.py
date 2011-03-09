# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## EdgeCore.ES.get_interface_status test
## Auto-generated by manage.py debug-script at 2011-03-04 21:23:46
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
from noc.lib.test import ScriptTestCase
class EdgeCore_ES_get_interface_status_Test(ScriptTestCase):
    script="EdgeCore.ES.get_interface_status"
    vendor="EdgeCore"
    platform='ES3526XA-38'
    version='2.3.3.16'
    input={}
    result=[{'interface': 'Eth 1/1', 'status': True},
 {'interface': 'Eth 1/2', 'status': True},
 {'interface': 'Eth 1/3', 'status': False},
 {'interface': 'Eth 1/4', 'status': True},
 {'interface': 'Eth 1/5', 'status': False},
 {'interface': 'Eth 1/6', 'status': False},
 {'interface': 'Eth 1/7', 'status': False},
 {'interface': 'Eth 1/8', 'status': False},
 {'interface': 'Eth 1/9', 'status': False},
 {'interface': 'Eth 1/10', 'status': True},
 {'interface': 'Eth 1/11', 'status': True},
 {'interface': 'Eth 1/12', 'status': False},
 {'interface': 'Eth 1/13', 'status': False},
 {'interface': 'Eth 1/14', 'status': False},
 {'interface': 'Eth 1/15', 'status': False},
 {'interface': 'Eth 1/16', 'status': False},
 {'interface': 'Eth 1/17', 'status': True},
 {'interface': 'Eth 1/18', 'status': True},
 {'interface': 'Eth 1/19', 'status': True},
 {'interface': 'Eth 1/20', 'status': False},
 {'interface': 'Eth 1/21', 'status': False},
 {'interface': 'Eth 1/22', 'status': False},
 {'interface': 'Eth 1/23', 'status': True},
 {'interface': 'Eth 1/24', 'status': False},
 {'interface': 'Eth 1/25', 'status': False},
 {'interface': 'Eth 1/26', 'status': True},
 {'interface': 'Console61', 'status': True},
 {'interface': 'VLAN113', 'status': True},
 {'interface': 'VLAN4093', 'status': True},
 {'interface': 'VLAN1', 'status': False},
 {'interface': 'VLAN900', 'status': True}]
    motd=' \n\n      CLI session with the Standalone Intelligent Switch is opened.\n      To end the CLI session, enter [Exit].\n\n'
    cli={
}
    snmp_get={}
    snmp_getnext={'1.3.6.1.2.1.2.2.1.8': [('1.3.6.1.2.1.2.2.1.8.1', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.2', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.3', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.4', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.5', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.6', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.7', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.8', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.9', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.10', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.11', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.12', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.13', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.14', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.15', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.16', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.17', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.18', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.19', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.20', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.21', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.22', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.23', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.24', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.25', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.26', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.61', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.1001', '2'),
                         ('1.3.6.1.2.1.2.2.1.8.1113', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.1900', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.5093', '1')],
 '1.3.6.1.2.1.31.1.1.1.1': [('1.3.6.1.2.1.31.1.1.1.1.1', 'Port1'),
                            ('1.3.6.1.2.1.31.1.1.1.1.2', 'Port2'),
                            ('1.3.6.1.2.1.31.1.1.1.1.3', 'Port3'),
                            ('1.3.6.1.2.1.31.1.1.1.1.4', 'Port4'),
                            ('1.3.6.1.2.1.31.1.1.1.1.5', 'Port5'),
                            ('1.3.6.1.2.1.31.1.1.1.1.6', 'Port6'),
                            ('1.3.6.1.2.1.31.1.1.1.1.7', 'Port7'),
                            ('1.3.6.1.2.1.31.1.1.1.1.8', 'Port8'),
                            ('1.3.6.1.2.1.31.1.1.1.1.9', 'Port9'),
                            ('1.3.6.1.2.1.31.1.1.1.1.10', 'Port10'),
                            ('1.3.6.1.2.1.31.1.1.1.1.11', 'Port11'),
                            ('1.3.6.1.2.1.31.1.1.1.1.12', 'Port12'),
                            ('1.3.6.1.2.1.31.1.1.1.1.13', 'Port13'),
                            ('1.3.6.1.2.1.31.1.1.1.1.14', 'Port14'),
                            ('1.3.6.1.2.1.31.1.1.1.1.15', 'Port15'),
                            ('1.3.6.1.2.1.31.1.1.1.1.16', 'Port16'),
                            ('1.3.6.1.2.1.31.1.1.1.1.17', 'Port17'),
                            ('1.3.6.1.2.1.31.1.1.1.1.18', 'Port18'),
                            ('1.3.6.1.2.1.31.1.1.1.1.19', 'Port19'),
                            ('1.3.6.1.2.1.31.1.1.1.1.20', 'Port20'),
                            ('1.3.6.1.2.1.31.1.1.1.1.21', 'Port21'),
                            ('1.3.6.1.2.1.31.1.1.1.1.22', 'Port22'),
                            ('1.3.6.1.2.1.31.1.1.1.1.23', 'Port23'),
                            ('1.3.6.1.2.1.31.1.1.1.1.24', 'Port24'),
                            ('1.3.6.1.2.1.31.1.1.1.1.25', 'Port25'),
                            ('1.3.6.1.2.1.31.1.1.1.1.26', 'Port26'),
                            ('1.3.6.1.2.1.31.1.1.1.1.61', 'Console61'),
                            ('1.3.6.1.2.1.31.1.1.1.1.1001', 'VLAN1'),
                            ('1.3.6.1.2.1.31.1.1.1.1.1113', 'VLAN113'),
                            ('1.3.6.1.2.1.31.1.1.1.1.1900', 'VLAN900'),
                            ('1.3.6.1.2.1.31.1.1.1.1.5093', 'VLAN4093')]}
