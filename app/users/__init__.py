
from .models import security_datastore, ActionLog
from .forms import RegisterFormWithAFuckingPasswordConfirmField

security_forms = {
	'confirm_register_form': RegisterFormWithAFuckingPasswordConfirmField
}
