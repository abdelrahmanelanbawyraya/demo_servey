# from odoo import models, api, exceptions


# class ResUsers(models.Model):
#     _inherit = 'res.users'

#     def _login_redirect(self, uid, redirect=None):
#         user = self.browse(uid)
#         # If the user is portal-only (no internal access), force redirect to your custom page
#         if not user.has_group('base.group_user'):  # not internal user
#             if not redirect:
#                 redirect = '/portal/survey'  # ← your desired page
#             return redirect

#         return super()._login_redirect(uid, redirect=redirect)

#     @api.model
#     def authenticate_user(self, login, password):
#         user = self.search([('login', '=', login)], limit=1)
#         print('backend')
#         print(user)
#         if not user:
#             return False
        
#         try:
#             user.with_user(user)._check_credentials({'type': 'password', 'password': password}, {'interactive': False})
#             return user
#         except exceptions.AccessDenied as e:
#             print(f"Access Denied: {e}")
#         except Exception as e:
#             print(f"Unexpected error: {e}")
