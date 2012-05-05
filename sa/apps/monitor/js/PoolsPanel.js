//---------------------------------------------------------------------
// sa.monitor PoolsPanel
//---------------------------------------------------------------------
// Copyright (C) 2007-2011 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.sa.monitor.PoolsPanel");

Ext.define("NOC.sa.monitor.PoolsPanel", {
    extend: "Ext.panel.Panel",
    uses: [],
    title: "Pools",
    closable: false,

    initComponent: function() {
        var me = this;

        Ext.apply(me, {
            items: [
                {
                    xtype: "gridpanel",
                    border: false,
                    autoScroll: true,
                    stateful: true,
                    stateId: "sa.monitor-pools-grid",
                    store: me.store,
                    features: [{
                        ftype: "groupingsummary",
                        groupHeaderTpl: "Pool: {name}"
                    }],
                    columns: [
                        {
                            text: "Instance",
                            dataIndex: "instance"
                        },
                        {
                            text: "State",
                            dataIndex: "state"
                        },
                        {
                            text: "Current",
                            dataIndex: "current_scripts",
                            summaryType: "sum",
                            align: "right"
                        },
                        {
                            text: "Max",
                            dataIndex: "max_scripts",
                            summaryType: "sum",
                            align: "right"
                        }
                    ],
                    tbar: [
                        {
                            text: "Refresh",
                            iconCls: "icon_arrow_refresh",
                            scope: me.app,
                            handler: me.app.refreshData
                        }
                    ]
                }
            ]
        });
        me.callParent();
    }
});
