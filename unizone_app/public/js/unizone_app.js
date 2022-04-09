$(window).on('load', function() {
    frappe.after_ajax(function () {
        if (frappe.boot.changelogo.show_help_menu) {
            // $('.dropdown-help').css('display','block');
            $('.dropdown-help').attr('style', 'display: block !important');
        }
        if (frappe.boot.changelogo.logo_width) {
            $('.app-logo').css('width',frappe.boot.changelogo.logo_width+'px');
        }
        if (frappe.boot.changelogo.logo_height) {
            $('.app-logo').css('height',frappe.boot.changelogo.logo_height+'px');
        }
        if (frappe.boot.changelogo.navbar_background_color) {
            $('.navbar').css('background-color',frappe.boot.changelogo.navbar_background_color)
        }
        if (frappe.boot.changelogo.custom_navbar_title_style && frappe.boot.changelogo.custom_navbar_title) {
            $(`<span style=${frappe.boot.changelogo.custom_navbar_title_style.replace('\n','')} class="hidden-xs hidden-sm">${frappe.boot.changelogo.custom_navbar_title}</span>`).insertAfter("#navbar-breadcrumbs")
        }
    })
})
