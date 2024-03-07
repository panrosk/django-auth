
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import AccessToken,AuthUser,RefreshToken


URL = reverse("users:register")



# Create your tests here.

# Get an instance of a  
def create_user( email, password):
    return get_user_model().objects.create_user(email, password)


test_user = {
    'email': "test@example.com",
    'password': "testpassword",
    'name': 'Test User',
    'phone': '1234567890',
    'address': 'Test Address',
    'last_name': 'Test Last Name',
    'is_active': 'True',
    'is_bussiness': 'False',
    }


test_user2 = {
    'email': "test@example.com",
    'password': "testpassword",
    'name': 'Updated User',
    'phone': '1234567890',
    'address': 'Test Address',
    'last_name': 'Test Last Name',
    'is_active': 'True',
    'is_bussiness': 'False',
    }


class DbUserTests(TestCase):
    def test_create_user(self):
        user = create_user(test_user['email'], test_user['password'])
        self.assertEqual(user.email, test_user['email'])
        self.assertTrue(user.check_password(test_user['password']))

        

    def test_create_user_no_email(self):
        with self.assertRaises(ValueError):
            create_user(None, test_user['password'])


    def test_create_user_no_password(self):
        with self.assertRaises(ValueError):
            create_user(test_user['email'], None)

    def test_normalize_email(self):
        user = create_user(test_user['email'].upper(), test_user['password'])
        self.assertEqual(user.email,"TEST@example.com")

class RegisterUserTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        response = self.client.post(URL, test_user, format='json')
        status_code = response.status_code
        self.assertEqual(status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.get().email, test_user['email'])

    def test_create_existing_user(self):
        self.client.post(URL, test_user, format='json')
        response = self.client.post(URL, test_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(get_user_model().objects.count(), 1)


class LoginUserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(test_user['email'], test_user['password'])

    def test_login_user(self):
        response = self.client.post(reverse("users:login"), test_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)

        access = response.data['access']
        access_token = AccessToken(access)
        self.assertTrue(access_token['email'] == test_user['email'])
    
    def test_login_user_wrong_password(self):
        response = self.client.post(reverse("users:login"), {'email': test_user['email'], 'password': 'wrongpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue('detail' in response.data)
        self.assertTrue(response.data['detail'] == 'No active account found with the given credentials')
  


class UpdateUserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(test_user['email'], test_user['password'])
        print(self.user)
        self.client.force_authenticate(user=self.user)


    def test_update_user(self):
        response = self.client.put(reverse("users:detail"), test_user2, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

