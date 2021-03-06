# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Brocade.ADX.get_chassis_id
# ---------------------------------------------------------------------
# Copyright (C) 2007-2017 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
import re
# NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetchassisid import IGetChassisID


class Script(BaseScript):
    name = 'Brocade.ADX.get_chassis_id'
    interface = IGetChassisID

    rx_mac = re.compile(
        r"([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})", re.IGNORECASE)

    def execute(self):
        v = self.cli('show chassis')
        match = self.re_search(self.rx_mac, v)
        mac = match.group(1)
        return [{
            'first_chassis_mac': mac,
            'last_chassis_mac': mac
        }]
