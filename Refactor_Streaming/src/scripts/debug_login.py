from apps.users.models import User
from rest_framework.test import APIClient

username = 'dbg_debug'
password = 'dbgpass'

# ensure user exists with known password
user = User.objects.filter(username=username).first()
if not user:
    User.objects.create_user(username=username, password=password)
else:
    user.set_password(password)
    user.save()

client = APIClient()
resp = client.post('/api/auth/login/', {'username': username, 'password': password}, format='json')

print('status', resp.status_code)
# print response content safely
try:
    print('data', resp.data)
except Exception:
    try:
        print('content', resp.content.decode())
    except Exception:
        print('content raw', resp.content)
