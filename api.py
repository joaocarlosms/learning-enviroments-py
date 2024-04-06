def login(user, password):
    if user == 'pycodebr' and password == '123':
        return 'Login correto, você esta logado!'
    else:
        return 'Login incorreto, você foi desconectado'
    
def send_email_log():
    return 'Email com login enviado'