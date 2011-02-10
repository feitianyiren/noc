# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## DLink.DxS_Cisco_CLI.get_switchport
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""
"""
from noc.sa.script import Script as NOCScript
from noc.sa.interfaces import IGetSwitchport
import re

class Script(NOCScript):
    name="DLink.DxS_Cisco_CLI.get_switchport"
    implements=[IGetSwitchport]
    rx_line=re.compile(r"^(?P<interface>\S*\s*\d+(\/\d+)?)\s+(?P<status>\S+)\s+(?P<mode>ACCESS|TRUNK)\s+\d+\s+(?P<untagged>\d+)\s+\S+\s+(?P<vlans>\S+)", re.MULTILINE)
    def execute(self):
        r=[]
        for match in self.rx_line.finditer(self.cli("show interfaces switchport")):
            trunk = match.group("mode").startswith("TRUNK")
            vlans = match.group("vlans")
            if vlans == "ALL":
                tagged = range(1,4095)
            else:
                tagged = self.expand_rangelist(match.group("vlans"))
            interface = match.group("interface")
            members = []
            if interface.startswith("AggregatePort"):
                shortname = self.profile.convert_interface_name(interface)
                print "\n\n\n %s \n\n\n"%shortname
                for p in self.scripts.get_portchannel():
                    print "\n\n\n %s \n\n\n"%p["interface"]
                    if p["interface"] == shortname:
                        members = p["members"]
            r+=[{
                "interface"      : interface,
                "status"         : True,
                #"description" : "qwe";
                "802.1Q Enabled" : trunk,
                "802.1ad Tunnel" : False,
                "untagged"       : int(match.group("untagged")),
                "tagged"         : tagged,
                "members"        : members,
                }]
        return r
