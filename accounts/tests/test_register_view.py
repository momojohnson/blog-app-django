from django.test import TestCase
from django.urls import reverse, resolve
from django.test import TestCase
from django.contrib.auth.models import User
from .. views import register
from .. forms import RegistrationForm

class RegisterTests(TestCase):
    
    def setUp(self):
        url = reverse('accounts:register')
        self.response = self.client.get(url)
    
    def test_register_status_code(self):
        url = reverse('accounts:register')
        self.assertEquals(self.response.status_code, 200)

    def test_register_url_resolves_register_view(self):
        view = resolve('/accounts/register/')
        self.assertEquals(view.func, register)
    
    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_contains_form(self):
        register_form  = self.response.context.get('form')
        self.assertIsInstance(register_form, RegistrationForm)

class UserSuccessfullyRegister(TestCase):
    def setUp(self):
        url = reverse('accounts:register')
        data = {
            'username'  : 'john',
            'first_name':'james',
            'last_name': 'brown',
            'email':   'momo@go.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')
    
    def test_redirection(self):
        '''
        A valid form submission should redirect the user to the home page
        '''
        self.assertRedirects(self.response, self.home_url)
    
    def test_user_created(self):
        self.assertTrue(User.objects.exists())
    
    def test_user_authentication(self):
        '''
        Create a new request to an arbitrary page.
        The resulting response should now have a `user` to its context,
        after a successful sign up.
        '''
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

class InvalidRegisterTest(TestCase):
    def setUp(self):
        url = reverse('accounts:register')
        self.response = self.client.post(url, {})
    
    def test_signup_status_code(self):
        '''
        An invalid form submission should return to the same page
        '''
        self.assertEquals(self.response.status_code, 200)
    
    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)
        
    def test_dont_user_not_created(self):
        self.assertFalse(User.objects.exists())
        
    def test_form_inputs(self):
        '''
        The view must contain five inputs: csrf, username, email,
        password1, password2
        '''
        self.assertContains(self.response, '<input', 7)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)
