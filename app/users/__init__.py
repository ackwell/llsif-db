
from .models import security_datastore
from .forms import RegisterFormWithAFuckingPasswordConfirmField

security_forms = {
	'confirm_register_form': RegisterFormWithAFuckingPasswordConfirmField
}
