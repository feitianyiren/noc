# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# VLAN Profile
# ----------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
from threading import Lock
import operator
# Third-party modules
from mongoengine.document import Document
from mongoengine.fields import StringField, LongField, ListField, BooleanField
import cachetools
# NOC modules
from noc.main.models.remotesystem import RemoteSystem
from noc.main.models.style import Style
from noc.wf.models.workflow import Workflow
from noc.lib.nosql import PlainReferenceField, ForeignKeyField
from noc.core.bi.decorator import bi_sync
from noc.core.model.decorator import on_delete_check

id_lock = Lock()


@bi_sync
@on_delete_check(check=[
    ("vc.VLAN", "profile"),
    ("inv.NetworkSegmentProfile", "default_vlan_profile")
])
class VLANProfile(Document):
    meta = {
        "collection": "vlanprofiles",
        "strict": False,
        "auto_create_index": False
    }

    name = StringField(unique=True)
    description = StringField()
    # VLAN is management VLAN
    enable_management = BooleanField(default=False)
    # VLAN is multicast VLAN
    enable_multicast = BooleanField(default=False)
    # VLAN should be automatically provisioned
    enable_provisioning = BooleanField(default=False)
    # VLAN workflow
    workflow = PlainReferenceField(Workflow)
    style = ForeignKeyField(Style)
    tags = ListField(StringField())
    # Integration with external NRI and TT systems
    # Reference to remote system object has been imported from
    remote_system = PlainReferenceField(RemoteSystem)
    # Object id in remote system
    remote_id = StringField()
    # Object id in BI
    bi_id = LongField(unique=True)

    _id_cache = cachetools.TTLCache(maxsize=100, ttl=60)
    _bi_id_cache = cachetools.TTLCache(maxsize=100, ttl=60)

    def __unicode__(self):
        return self.name

    @classmethod
    @cachetools.cachedmethod(operator.attrgetter("_id_cache"), lock=lambda _: id_lock)
    def get_by_id(cls, id):
        return VLANProfile.objects.filter(id=id).first()

    @classmethod
    @cachetools.cachedmethod(operator.attrgetter("_bi_id_cache"), lock=lambda _: id_lock)
    def get_by_bi_id(cls, id):
        return VLANProfile.objects.filter(bi_id=id).first()
