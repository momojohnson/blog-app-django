from django.test import TestCase
from .. forms import RegistrationForm

class RegistrationFormTest(TestCase):
    def test_form_has_fields(self):
        form = RegistrationForm()
        expected = ['username','first_name', 'last_name', 'email', 'password1', 'password2',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)