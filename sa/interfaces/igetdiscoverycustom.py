# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# IGetDiscoveryCustom
# ---------------------------------------------------------------------
# Copyright (C) 2007-2012 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
from __future__ import absolute_import
# NOC Modules
from noc.core.interface.base import BaseInterface
from .base import Parameter, DictParameter


class IGetDiscoveryCustom(BaseInterface):
    instance = Parameter()
    managed_object = Parameter()
    returns = DictParameter()
