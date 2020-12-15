from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def oauth(request):
    code = request.GET['code']
    print('code = ' + str(code))

    client_id = request.session.get('client_id')
    redirect_uri = request.session.get('redirect_uri')

    access_token_request_uri = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"

    access_token_request_uri += "client_id=" + client_id
    access_token_request_uri += "&redirect_uri=" + redirect_uri
    access_token_request_uri += "&code=" + code

    print(access_token_request_uri)

    return redirect('index')

def kakao_login(request):
    login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'
    client_id = 'e7dfabcc5fb3299e38be6f6c6af72553'
    redirect_uri = 'http://127.0.0.1:8000/oauth'

    login_request_uri = \
        login_request_uri + 'client_id=' + client_id + '&redirect_uri=' + redirect_uri + '&response_type=code'

    request.session['client_id'] = client_id
    request.session['redirect_uri'] = redirect_uri

    return redirect(login_request_uri)

def logout(request):
    del(request.session['client_id'])
    del(request.session['redirect_uri'])
    return redirect('index')
