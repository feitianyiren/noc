# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# MPLS-VPN-MIB
#     Compiled MIB
#     Do not modify this file directly
#     Run ./noc mib make_cmib instead
# ----------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# MIB Name
NAME = "MPLS-VPN-MIB"
# Metadata
LAST_UPDATED = "2001-10-15"
COMPILED = "2018-06-23"
# MIB Data: name -> oid
MIB = {
    "MPLS-VPN-MIB::mplsVpnMIB": "1.3.6.1.3.118",
    "MPLS-VPN-MIB::mplsVpnNotifications": "1.3.6.1.3.118.0",
    "MPLS-VPN-MIB::mplsVrfIfUp": "1.3.6.1.3.118.0.1",
    "MPLS-VPN-MIB::mplsVrfIfDown": "1.3.6.1.3.118.0.2",
    "MPLS-VPN-MIB::mplsNumVrfRouteMidThreshExceeded": "1.3.6.1.3.118.0.3",
    "MPLS-VPN-MIB::mplsNumVrfRouteMaxThreshExceeded": "1.3.6.1.3.118.0.4",
    "MPLS-VPN-MIB::mplsNumVrfSecIllegalLabelThreshExceeded": "1.3.6.1.3.118.0.5",
    "MPLS-VPN-MIB::mplsVpnObjects": "1.3.6.1.3.118.1",
    "MPLS-VPN-MIB::mplsVpnScalars": "1.3.6.1.3.118.1.1",
    "MPLS-VPN-MIB::mplsVpnConfiguredVrfs": "1.3.6.1.3.118.1.1.1",
    "MPLS-VPN-MIB::mplsVpnActiveVrfs": "1.3.6.1.3.118.1.1.2",
    "MPLS-VPN-MIB::mplsVpnConnectedInterfaces": "1.3.6.1.3.118.1.1.3",
    "MPLS-VPN-MIB::mplsVpnNotificationEnable": "1.3.6.1.3.118.1.1.4",
    "MPLS-VPN-MIB::mplsVpnVrfConfMaxPossibleRoutes": "1.3.6.1.3.118.1.1.5",
    "MPLS-VPN-MIB::mplsVpnConf": "1.3.6.1.3.118.1.2",
    "MPLS-VPN-MIB::mplsVpnInterfaceConfTable": "1.3.6.1.3.118.1.2.1",
    "MPLS-VPN-MIB::mplsVpnInterfaceConfEntry": "1.3.6.1.3.118.1.2.1.1",
    "MPLS-VPN-MIB::mplsVpnInterfaceConfIndex": "1.3.6.1.3.118.1.2.1.1.1",
    "MPLS-VPN-MIB::mplsVpnInterfaceLabelEdgeType": "1.3.6.1.3.118.1.2.1.1.2",
    "MPLS-VPN-MIB::mplsVpnInterfaceVpnClassification": "1.3.6.1.3.118.1.2.1.1.3",
    "MPLS-VPN-MIB::mplsVpnInterfaceVpnRouteDistProtocol": "1.3.6.1.3.118.1.2.1.1.4",
    "MPLS-VPN-MIB::mplsVpnInterfaceConfStorageType": "1.3.6.1.3.118.1.2.1.1.5",
    "MPLS-VPN-MIB::mplsVpnInterfaceConfRowStatus": "1.3.6.1.3.118.1.2.1.1.6",
    "MPLS-VPN-MIB::mplsVpnVrfTable": "1.3.6.1.3.118.1.2.2",
    "MPLS-VPN-MIB::mplsVpnVrfEntry": "1.3.6.1.3.118.1.2.2.1",
    "MPLS-VPN-MIB::mplsVpnVrfName": "1.3.6.1.3.118.1.2.2.1.1",
    "MPLS-VPN-MIB::mplsVpnVrfDescription": "1.3.6.1.3.118.1.2.2.1.2",
    "MPLS-VPN-MIB::mplsVpnVrfRouteDistinguisher": "1.3.6.1.3.118.1.2.2.1.3",
    "MPLS-VPN-MIB::mplsVpnVrfCreationTime": "1.3.6.1.3.118.1.2.2.1.4",
    "MPLS-VPN-MIB::mplsVpnVrfOperStatus": "1.3.6.1.3.118.1.2.2.1.5",
    "MPLS-VPN-MIB::mplsVpnVrfActiveInterfaces": "1.3.6.1.3.118.1.2.2.1.6",
    "MPLS-VPN-MIB::mplsVpnVrfAssociatedInterfaces": "1.3.6.1.3.118.1.2.2.1.7",
    "MPLS-VPN-MIB::mplsVpnVrfConfMidRouteThreshold": "1.3.6.1.3.118.1.2.2.1.8",
    "MPLS-VPN-MIB::mplsVpnVrfConfHighRouteThreshold": "1.3.6.1.3.118.1.2.2.1.9",
    "MPLS-VPN-MIB::mplsVpnVrfConfMaxRoutes": "1.3.6.1.3.118.1.2.2.1.10",
    "MPLS-VPN-MIB::mplsVpnVrfConfLastChanged": "1.3.6.1.3.118.1.2.2.1.11",
    "MPLS-VPN-MIB::mplsVpnVrfConfRowStatus": "1.3.6.1.3.118.1.2.2.1.12",
    "MPLS-VPN-MIB::mplsVpnVrfConfStorageType": "1.3.6.1.3.118.1.2.2.1.13",
    "MPLS-VPN-MIB::mplsVpnVrfRouteTargetTable": "1.3.6.1.3.118.1.2.3",
    "MPLS-VPN-MIB::mplsVpnVrfRouteTargetEntry": "1.3.6.1.3.118.1.2.3.1",
    "MPLS-VPN-MIB::mplsVpnVrfRouteTargetIndex": "1.3.6.1.3.118.1.2.3.1.2",
    "MPLS-VPN-MIB::mplsVpnVrfRouteTargetType": "1.3.6.1.3.118.1.2.3.1.3",
    "MPLS-VPN-MIB::mplsVpnVrfRouteTarget": "1.3.6.1.3.118.1.2.3.1.4",
    "MPLS-VPN-MIB::mplsVpnVrfRouteTargetDescr": "1.3.6.1.3.118.1.2.3.1.5",
    "MPLS-VPN-MIB::mplsVpnVrfRouteTargetRowStatus": "1.3.6.1.3.118.1.2.3.1.6",
    "MPLS-VPN-MIB::mplsVpnVrfBgpNbrAddrTable": "1.3.6.1.3.118.1.2.4",
    "MPLS-VPN-MIB::mplsVpnVrfBgpNbrAddrEntry": "1.3.6.1.3.118.1.2.4.1",
    "MPLS-VPN-MIB::mplsVpnVrfBgpNbrIndex": "1.3.6.1.3.118.1.2.4.1.1",
    "MPLS-VPN-MIB::mplsVpnVrfBgpNbrRole": "1.3.6.1.3.118.1.2.4.1.2",
    "MPLS-VPN-MIB::mplsVpnVrfBgpNbrType": "1.3.6.1.3.118.1.2.4.1.3",
    "MPLS-VPN-MIB::mplsVpnVrfBgpNbrAddr": "1.3.6.1.3.118.1.2.4.1.4",
    "MPLS-VPN-MIB::mplsVpnVrfBgpNbrRowStatus": "1.3.6.1.3.118.1.2.4.1.5",
    "MPLS-VPN-MIB::mplsVpnVrfBgpNbrStorageType": "1.3.6.1.3.118.1.2.4.1.6",
    "MPLS-VPN-MIB::mplsVpnVrfBgpNbrPrefixTable": "1.3.6.1.3.118.1.2.5",
    "MPLS-VPN-MIB::mplsVpnVrfBgpNbrPrefixEntry": "1.3.6.1.3.118.1.2.5.1",
    "MPLS-VPN-MIB::mplsVpnVrfBgpPathAttrPeer": "1.3.6.1.3.118.1.2.5.1.1",
    "MPLS-VPN-MIB::mplsVpnVrfBgpPathAttrIpAddrPrefixLen": "1.3.6.1.3.118.1.2.5.1.2",
    "MPLS-VPN-MIB::mplsVpnVrfBgpPathAttrIpAddrPrefix": "1.3.6.1.3.118.1.2.5.1.3",
    "MPLS-VPN-MIB::mplsVpnVrfBgpPathAttrOrigin": "1.3.6.1.3.118.1.2.5.1.4",
    "MPLS-VPN-MIB::mplsVpnVrfBgpPathAttrASPathSegment": "1.3.6.1.3.118.1.2.5.1.5",
    "MPLS-VPN-MIB::mplsVpnVrfBgpPathAttrNextHop": "1.3.6.1.3.118.1.2.5.1.6",
    "MPLS-VPN-MIB::mplsVpnVrfBgpPathAttrMultiExitDisc": "1.3.6.1.3.118.1.2.5.1.7",
    "MPLS-VPN-MIB::mplsVpnVrfBgpPathAttrLocalPref": "1.3.6.1.3.118.1.2.5.1.8",
    "MPLS-VPN-MIB::mplsVpnVrfBgpPathAttrAtomicAggregate": "1.3.6.1.3.118.1.2.5.1.9",
    "MPLS-VPN-MIB::mplsVpnVrfBgpPathAttrAggregatorAS": "1.3.6.1.3.118.1.2.5.1.10",
    "MPLS-VPN-MIB::mplsVpnVrfBgpPathAttrAggregatorAddr": "1.3.6.1.3.118.1.2.5.1.11",
    "MPLS-VPN-MIB::mplsVpnVrfBgpPathAttrCalcLocalPref": "1.3.6.1.3.118.1.2.5.1.12",
    "MPLS-VPN-MIB::mplsVpnVrfBgpPathAttrBest": "1.3.6.1.3.118.1.2.5.1.13",
    "MPLS-VPN-MIB::mplsVpnVrfBgpPathAttrUnknown": "1.3.6.1.3.118.1.2.5.1.14",
    "MPLS-VPN-MIB::mplsVpnVrfSecTable": "1.3.6.1.3.118.1.2.6",
    "MPLS-VPN-MIB::mplsVpnVrfSecEntry": "1.3.6.1.3.118.1.2.6.1",
    "MPLS-VPN-MIB::mplsVpnVrfSecIllegalLabelViolations": "1.3.6.1.3.118.1.2.6.1.1",
    "MPLS-VPN-MIB::mplsVpnVrfSecIllegalLabelRcvThresh": "1.3.6.1.3.118.1.2.6.1.2",
    "MPLS-VPN-MIB::mplsVpnPerf": "1.3.6.1.3.118.1.3",
    "MPLS-VPN-MIB::mplsVpnVrfPerfTable": "1.3.6.1.3.118.1.3.1",
    "MPLS-VPN-MIB::mplsVpnVrfPerfEntry": "1.3.6.1.3.118.1.3.1.1",
    "MPLS-VPN-MIB::mplsVpnVrfPerfRoutesAdded": "1.3.6.1.3.118.1.3.1.1.1",
    "MPLS-VPN-MIB::mplsVpnVrfPerfRoutesDeleted": "1.3.6.1.3.118.1.3.1.1.2",
    "MPLS-VPN-MIB::mplsVpnVrfPerfCurrNumRoutes": "1.3.6.1.3.118.1.3.1.1.3",
    "MPLS-VPN-MIB::mplsVpnRoute": "1.3.6.1.3.118.1.4",
    "MPLS-VPN-MIB::mplsVpnVrfRouteTable": "1.3.6.1.3.118.1.4.1",
    "MPLS-VPN-MIB::mplsVpnVrfRouteEntry": "1.3.6.1.3.118.1.4.1.1",
    "MPLS-VPN-MIB::mplsVpnVrfRouteDest": "1.3.6.1.3.118.1.4.1.1.1",
    "MPLS-VPN-MIB::mplsVpnVrfRouteDestAddrType": "1.3.6.1.3.118.1.4.1.1.2",
    "MPLS-VPN-MIB::mplsVpnVrfRouteMask": "1.3.6.1.3.118.1.4.1.1.3",
    "MPLS-VPN-MIB::mplsVpnVrfRouteMaskAddrType": "1.3.6.1.3.118.1.4.1.1.4",
    "MPLS-VPN-MIB::mplsVpnVrfRouteTos": "1.3.6.1.3.118.1.4.1.1.5",
    "MPLS-VPN-MIB::mplsVpnVrfRouteNextHop": "1.3.6.1.3.118.1.4.1.1.6",
    "MPLS-VPN-MIB::mplsVpnVrfRouteNextHopAddrType": "1.3.6.1.3.118.1.4.1.1.7",
    "MPLS-VPN-MIB::mplsVpnVrfRouteIfIndex": "1.3.6.1.3.118.1.4.1.1.8",
    "MPLS-VPN-MIB::mplsVpnVrfRouteType": "1.3.6.1.3.118.1.4.1.1.9",
    "MPLS-VPN-MIB::mplsVpnVrfRouteProto": "1.3.6.1.3.118.1.4.1.1.10",
    "MPLS-VPN-MIB::mplsVpnVrfRouteAge": "1.3.6.1.3.118.1.4.1.1.11",
    "MPLS-VPN-MIB::mplsVpnVrfRouteInfo": "1.3.6.1.3.118.1.4.1.1.12",
    "MPLS-VPN-MIB::mplsVpnVrfRouteNextHopAS": "1.3.6.1.3.118.1.4.1.1.13",
    "MPLS-VPN-MIB::mplsVpnVrfRouteMetric1": "1.3.6.1.3.118.1.4.1.1.14",
    "MPLS-VPN-MIB::mplsVpnVrfRouteMetric2": "1.3.6.1.3.118.1.4.1.1.15",
    "MPLS-VPN-MIB::mplsVpnVrfRouteMetric3": "1.3.6.1.3.118.1.4.1.1.16",
    "MPLS-VPN-MIB::mplsVpnVrfRouteMetric4": "1.3.6.1.3.118.1.4.1.1.17",
    "MPLS-VPN-MIB::mplsVpnVrfRouteMetric5": "1.3.6.1.3.118.1.4.1.1.18",
    "MPLS-VPN-MIB::mplsVpnVrfRouteRowStatus": "1.3.6.1.3.118.1.4.1.1.19",
    "MPLS-VPN-MIB::mplsVpnVrfRouteStorageType": "1.3.6.1.3.118.1.4.1.1.20",
    "MPLS-VPN-MIB::mplsVpnConformance": "1.3.6.1.3.118.3",
    "MPLS-VPN-MIB::mplsVpnGroups": "1.3.6.1.3.118.3.1",
    "MPLS-VPN-MIB::mplsVpnCompliances": "1.3.6.1.3.118.3.2"
}