from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval


class OdooPlayground(models.Model):
    _name = "odoo.playground"
    _description = "Odoo Playground"

    DEFAULT_ENV_VARIABLES = """# Availabel variables:
    # - self: Current object \n\n\n\n"""

    model_id = fields.Many2one('ir.model', string='Model')
    code = fields.Text(string='code', default=DEFAULT_ENV_VARIABLES)
    result = fields.Text(string='Result')

    # __________________________________________________________________________________________________________________

    def action_execute(self):
        try:
            if self.model_id:
                model = self.env[self.model_id.model]
            else:
                model = self
            self.result = safe_eval(self.code.strip(), {'self': model})
        except Exception as e:
            self.result = str(e)

    # __________________________________________________________________________________________________________________
