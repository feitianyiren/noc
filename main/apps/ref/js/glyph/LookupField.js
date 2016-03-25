//---------------------------------------------------------------------
// NOC.main.ref.glyph.LookupField
//---------------------------------------------------------------------
// Copyright (C) 2007-2013 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.main.ref.glyph.LookupField");

Ext.define("NOC.main.ref.glyph.LookupField", {
    extend: "NOC.core.LookupField",
    alias: "widget.main.ref.glyph.LookupField",
    requires: ["NOC.main.ref.glyph.Lookup"],
    listConfig: {
        tpl: '<tpl for="."><div class="x-boundlist-item"><i class="{id}"></i> {label}</div></tpl>'
    },
    uiStyle: "medium"
});
