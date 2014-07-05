
from flask.ext.wtf import Form
from wtforms.widgets import HTMLString, SubmitInput
from wtforms.fields import SubmitField

class ChangeableSubmitInput(SubmitInput):
	def __call__(self, field, **kwargs):
		super(ChangeableSubmitInput, self).__call__(field, **kwargs)
		label = kwargs.pop('label', field.label.text)
		return HTMLString('<button %s>%s</button>' % (
			self.html_params(name=field.name, **kwargs),
			label))

# Used for CSRF protection for deletetion
class DeleteForm(Form):
	submit = SubmitField('Delete', widget=ChangeableSubmitInput())
