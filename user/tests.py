import json, jwt
import bcrypt
import requests

from user.models    import User
from room.models    import Room, Category, Image, Amenity, DisableDate, AbleTime
                            
from django.test    import TestCase
from django.test    import Client
from unittest.mock  import patch, MagicMock
from my_settings    import SECRET_KEY

class HostUserTest(TestCase):
    def setUp(self):
        password         = "12345678"
        hashed_password  = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        User.objects.create(
                id           = 1,
                email        = 'abc@gmail.com',
                password     = hashed_password,
                first_name   = 'test_user_first_name',
                last_name    = 'test_user_last_name',
                sex          = 'M',
                is_allowed   = True,
                birthday     = '0000-00-00',
                phone_number = 1012345678
            )
        Category.objects.create(name="test_type")

        Amenity.objects.create(name="test_amenity", image="i'm url")
        Amenity.objects.create(name="test2_amenity", image="i'm url2")

    def tearDown(self):
        User.objects.all().delete()

        Category.objects.all().delete()

        Amenity.objects.all().delete()

    def test_host_registrate_success(self, mocked_requests):
        client = Client()

        token = jwt.encode({'id': 1}, SECRET_KEY, algorithm = 'HS256')

        headers = {"HTTP_Authorization": token}
        class MockedResponse:
            def json(self):
                return {
                        "id"          : 1,
                        "name"        : "room",
                        "min_date"    : "123",
                        "city"        : "test_type",
                        "category"    : "test_type",
                        "capacity"    : "123",
                        "is_refund"   : true,
                        "price"       : "40000",
                        "able_time"   : ["11:00",
                                        "13:00"
                                        ],
                        "disable_date" : ["2021-12-31",
                                         "2022-1-1"
                        ],
                        "amenity"      : [['test_amenity',"i'm url"], ["test2_amenity","i'm url2"]],
                        "address"      : "서울특별시 강남구 테헤란로 427 위워크 선릉역2"
                        }
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        response            = client.get("/user/host", **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                'message': 'success',
                'room_id': 1
            }
        )
class SocialUserTest(TestCase):
    @patch("user.views.requests")
    def test_kakao_signin_new_user_success(self, mocked_requests):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
                    'id' : 1,
                    'kakao_account':{'email':'abc@gmail.com',
                                     'gender':'M',
                                     'birthday':'2021-05-31'
                                    }
                }
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {'HTTP_Authorization':'token'}
        response            = client.get("/user/kakao", **headers)
        user_id             = MockedResponse().json()['id']
        access_token        = jwt.encode({'id':user_id}, SECRET_KEY, algorithm='HS256')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                'message': 'existing user',
                'access_token': access_token
            }
        )
                        
    @patch("user.views.requests")
    def test_kakao_signin_new_user_token_required(self, mocked_requests):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
                    'id' : 1,
                    'kakao_account':{'email':'abc@gmail.com',
                                     'gender':'M',
                                     'birthday':'2021-05-31'
                                    }
                }
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {'HTTP_Authorization':''}
        response            = client.get("/user/kakao", **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'TOKEN REQUIRED'
            }
        )
    @patch("user.views.requests")
    def test_kakao_signin_new_user_email_required(self, mocked_requests):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
                    'id' : 1,
                    'kakao_account':{
                                     'gender':'M',
                                     'birthday':'2021-05-31'
                                    }
                }
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {'HTTP_Authorization':'token'}
        response            = client.get("/user/kakao", **headers)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json(),
            {
                'message' : 'EMAIL REQUIRED'
            }
        )

class UserSignUpTest(TestCase):
    def setUp(self):
        User.objects.create(
                email        = 'abc@gmail.com',
                password     = '123456789',
                first_name   = 'test_user_first_name',
                last_name    = 'test_user_last_name',
                sex          = 'M',
                birthday     = '0000-00-00',
                phone_number = 1012345678
            )
    def test_user_post_view(self):
        client   = Client()
        user     = {
                    'email'        : 'abcd@gmail.com',
                    'password'     : '1234567891',
                    'first_name'   : 'test_user_first1_name',
                    'last_name'    : 'test_user_last1_name',
                    'sex'          : 'M',
                    'birthday'     : '0000-00-00',
                    'phone_number' : 1043215678
                    }
        response = client.post('/user/signup', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 
            {
                'message' : 'SUCCESS'
            }
        )

    def test_user_post_duplicated_name(self):
        client = Client()
        user = {
                    'email'        : 'abcd@abc.com',
                    'password'     : '123456789',
                    'first_name'   : 'test_user_first_name',
                    'last_name'    : 'test_user_last_name',
                    'sex'          : 'M',
                    'birthday'     : '0000-00-00',
                    'phone_number' : 1012345479
                }
        response = client.post('/user/signup', json.dumps(user), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'DUPLICATE NAME'
            }
        )

    def test_user_post_duplicated_email(self):
        client = Client()
        user = {
                    'email'        : 'abc@gmail.com',
                    'password'     : '12345678',
                    'first_name'   : 'test_user_first_name',
                    'last_name'    : 'test_last_name',
                    'sex'          : 'M',
                    'birthday'     : '0000-00-00',
                    'phone_number' : 101363587
                }
        response = client.post('/user/signup', json.dumps(user), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'DUPLICATE EMAIL'
            }
        )

    def test_user_post_duplicated_phone_number(self):
        client = Client()
        user = {
                    'email'        : 'abcdc@gmail.com',
                    'password'     : '12345678',
                    'first_name'   : 'test_user_first_name',
                    'last_name'    : 'test_last_name',
                    'sex'          : 'M',
                    'birthday'     : '0000-00-00',
                    'phone_number' : 1012345678
                }
        response = client.post('/user/signup', json.dumps(user), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'DUPLICATE PHONE_NUMBER'
            }
        )

    def test_user_post_invalid_password(self):
        client = Client()
        user = {
                    'email'        : 'dnstks0204@gmail.com',
                    'password'     : '12348',
                    'first_name'   : 'test_user_first_name',
                    'last_name'    : 'test_last_name',
                    'sex'          : 'M',
                    'birthday'     : '0000-00-00',
                    'phone_number' : 101363587
                }
        response = client.post('/user/signup', json.dumps(user), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message':'INVALID PASSWORD'
            }
        )

    def test_user_post_invalid_email(self):
        client = Client()
        user = {
                    'email'        : 'dnstks0204gmail.com',
                    'password'     : '12348',
                    'first_name'   : 'test_user_first_name',
                    'last_name'    : 'test_last_name',
                    'sex'          : 'M',
                    'birthday'     : '0000-00-00',
                    'phone_number' : 101363587
                }
        response = client.post('/user/signup', json.dumps(user), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message':'INVALID EMAIL'
            }
        )

    def test_user_post_invalid_phone_number(self):
        client = Client()
        user = {
                    'email'        : '0204@gmail.com',
                    'password'     : '1234821239',
                    'first_name'   : 'test_user_first_name',
                    'last_name'    : 'test_last_name',
                    'sex'          : 'M',
                    'birthday'     : '0000-00-00',
                    'phone_number' : 1013635871332321
                }
        response = client.post('/user/signup', json.dumps(user), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message':'INVALID PHONE NUMBER'
            }
        )

class UserSignInTest(TestCase):
    def setUp(self):
        password         = "12345678"
        hashed_password  = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        User.objects.create(
                email        = 'abc@gmail.com',
                password     = hashed_password,
                first_name   = 'test_user_first_name',
                last_name    = 'test_user_last_name',
                sex          = 'M',
                is_allowed   = True,
                birthday     = '0000-00-00',
                phone_number = 1012345678
            )

    def tearDown(self):
        User.objects.all().delete()

    def test_login_post_invalid_user(self):
        client   = Client()
        user     = {
                    "email"        : "abc@gmail.com",
                    "password"     : "123456789",
                    "is_allowed"   : True
                    }
        
        response = client.post('/user/signin', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), 
            {
                'message' : 'INVALID_USER'
            }
        )
    
