__version__ = "0.0.1"

DEFAULT_LOGO = "/assets/whitelabel/images/whitelabel_logo.jpg"

def get_logo():
	try:
		import frappe
		if getattr(frappe, "conf", None):
			return frappe.conf.get("app_logo_url") or DEFAULT_LOGO
	except Exception:
		pass
	return DEFAULT_LOGO
