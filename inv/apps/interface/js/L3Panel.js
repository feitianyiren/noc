//---------------------------------------------------------------------
// inv.interface L3 Panel
//---------------------------------------------------------------------
// Copyright (C) 2007-2012 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.inv.interface.L3Panel");

Ext.define("NOC.inv.interface.L3Panel", {
    extend: "Ext.panel.Panel",
    uses: [],
    title: "L3",
    closable: false,
    layout: "fit",

    initComponent: function() {
        var me = this;

        Ext.apply(me, {
            items: [
                {
                    xtype: "gridpanel",
                    border: false,
                    autoScroll: true,
                    stateful: true,
                    stateId: "inv.interface-L3-grid",
                    store: me.store,
                    columns: [
                        {
                            text: "Name",
                            dataIndex: "name"
                        },
                        {
                            text: "IP",
                            dataIndex: "ip"
                        },
                        {
                            text: "IPv4",
                            dataIndex: "ipv4_addresses",
                            hidden: true
                        },
                        {
                            text: "IPv6",
                            dataIndex: "ipv6_addresses",
                            hidden: true
                        },
                        {
                            text: "VLAN",
                            dataIndex: "vlan"
                        },
                        {
                            text: "Description",
                            dataIndex: "description",
                            flex: 1
                        }
                     ]
                }
            ]
        });
        me.callParent();
    }
});
