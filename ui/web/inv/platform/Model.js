//---------------------------------------------------------------------
// inv.platform Model
//---------------------------------------------------------------------
// Copyright (C) 2007-2017 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.inv.platform.Model");

Ext.define("NOC.inv.platform.Model", {
    extend: "Ext.data.Model",
    rest_url: "/inv/platform/",

    fields: [
        {
            name: "id",
            type: "string"
        },
        {
            name: "vendor",
            type: "string"
        },
        {
            name: "name",
            type: "string"
        },
        {
            name: "uuid",
            type: "string"
        }
    ]
});
