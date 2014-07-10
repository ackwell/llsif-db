
from flask.ext.uploads import UploadSet, IMAGES
import os

class OverwriteUploadSet(UploadSet):
	def resolve_conflict(self, target_folder, basename):
		path = os.path.join(target_folder, basename)
		if os.path.exists(path):
			os.remove(path)
		return path

card_thumbs = OverwriteUploadSet('cardthumbs', IMAGES)

upload_sets = (card_thumbs,)
