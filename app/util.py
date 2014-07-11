
from flask.ext.wtf import Form
from wtforms.widgets import HTMLString, SubmitInput
from wtforms.fields import SubmitField
from PIL import Image

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


# Resize and crop an image to specified size
def resize_image(infile, outfile, new_size, format_='JPEG', **image_options):
	image = Image.open(infile)

	cur_ratio = image.size[0] / float(image.size[1])
	new_ratio = new_size[0] / float(new_size[1])

	if new_ratio > cur_ratio:
		image = image.resize(
			(new_size[0], int(round(new_size[0] * image.size[1] / image.size[0]))),
			Image.ANTIALIAS)

		image = image.crop((
			0,
			int(round((image.size[1] - new_size[1]) / 2)),
			image.size[0],
			int(round((image.size[1] + new_size[1]) / 2))))

	elif new_ratio < cur_ratio:
		image = image.resize(
			(int(round(new_size[1] * image.size[0] / image.size[1])), new_size[1]),
			Image.ANTIALIAS)

		image = image.crop((
			int(round((image.size[0] - new_size[0]) / 2)),
			0,
			int(round((image.size[0] + new_size[0]) / 2)),
			image.size[1]))
		
	else:
		image = image.resize(new_size, Image.ANTIALIAS)

	image.save(outfile, format_, **image_options)
