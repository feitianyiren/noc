###
    Модель конфигурации фильтра.
###
Ext.define 'Report.model.config.Filter',
	extend: 'Ext.data.Model'

	fields: [
		{name: 'type',     type: 'string'}
		{name: 'column',   type: 'string'}
		{name: 'dataType', type: 'string'}
	]