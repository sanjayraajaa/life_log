# Copyright (c) 2025, Sanjay Raja S and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MyDiary(Document):
    
    def autoname(self):
        user_email = frappe.session.user_email
        date = frappe.utils.today()  # Get current date
        self.name = f"{date}-{self.title}__{user_email}"