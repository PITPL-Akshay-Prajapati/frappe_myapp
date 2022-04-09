# Copyright (c) 2022, akshay and contributors
# For license information, please see license.txt
"""
# import frappe
from frappe.model.document import Document

class changeLogo(Document):
	pass
"""
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import cint
from whitelabel.api import get_frappe_version

class changeLogo(Document):
	def validate(self):
		if cint(get_frappe_version()) >= 13:
			if self.unizone_app_name:
				frappe.db.set_value("System Settings","System Settings","app_name",self.unizone_app_name)
			else:
				if "erpnext" in frappe.get_installed_apps():
					frappe.db.set_value("System Settings","System Settings","app_name","ERPNext")
				else:
					frappe.db.set_value("System Settings","System Settings","app_name","Frappe")

