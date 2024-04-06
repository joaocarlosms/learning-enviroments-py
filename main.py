import api
import os

user = os.environ.get('USER_API')
password = os.environ.get('PASSWORD_API')
enviroment_work = os.environ.get('ENVIROMENT')

login = api.login(user, password)

print(login)

if(enviroment_work == 'dev'):
    print(api.send_email_log())