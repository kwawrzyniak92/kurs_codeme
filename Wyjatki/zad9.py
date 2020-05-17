import webbrowser

def check_sufix(user_url):
    alowed_suffixes = ('pl', 'com')
    valid_url = False
    for sufix in alowed_suffixes:
        if user_url.endswith(sufix):
            print ('Prawidlowa koncówka')
            valid_url = True
            break
    if not valid_url:
        raise URLError('Twój URL nie jest obslugiwany')

def with_prefix(url):
    if url.startswith('https://') or url.startswith('http://'):
        return url
    else:
        return 'http://'+ url


user_url = input('podaj strone www ')
user_url = user_url.strip()
user_url = user_url.replace(' ','')

try:
    check_sufix(user_url)
except Exception as e:
    print('Błąd')
    print(e)
else:
    webbrowser.open(with_prefix(user_url))
