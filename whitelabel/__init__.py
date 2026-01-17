__version__ = "0.0.1"

__logo__ = "/assets/whitelabel/images/whitelabel_logo.jpg"

def get_logo():
    try:
        import frappe
        if getattr(frappe, "conf", None):
            return frappe.conf.get("app_logo_url") or __logo__
    except Exception:
        pass
    return __logo__
