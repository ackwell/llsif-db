
from .forms import RegisterFormWithAFuckingPasswordConfirmField
from .models import security_datastore, ActionLog
from .views import blueprint

security_forms = {
	'confirm_register_form': RegisterFormWithAFuckingPasswordConfirmField
}
