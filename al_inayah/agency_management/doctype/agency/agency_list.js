frappe.listview_settings['Agency'] = {
    get_indicator: function(doc) {
        if (!doc.is_active) {
            return ['Inactive', 'red', 'is_active,=,0'];
        } else {
            return ['Active', 'green', 'is_active,=,1'];
        }
    }
};
