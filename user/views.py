from django.shortcuts import render, redirect
import os
import sys
import urllib.request


# Create your views here.
def index(request):
    return render(request, 'user/index.html')


# def naver(request):
    # token = "YOUR_ACCESS_TOKEN"
    # header = "Bearer " + token  # Bearer 다음에 공백 추가
    # url = "https://openapi.naver.com/v1/nid/me"
    # request = urllib.request.Request(url)
    # request.add_header("Authorization", header)
    # response = urllib.request.urlopen(request)
    # rescode = response.getcode()
    # if (rescode == 200):
    #     response_body = response.read()
    #     print(response_body.decode('utf-8'))
    # else:
    #     print("Error Code:" + rescode)

# def oauth(request):
#     code = request.GET['code']
#     print('code = ' + str(code))
#
#     client_id = request.session.get('client_id')
#     redirect_uri = request.session.get('redirect_uri')
#
#     access_token_request_uri = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"
#
#     access_token_request_uri += "client_id=" + client_id
#     access_token_request_uri += "&redirect_uri=" + redirect_uri
#     access_token_request_uri += "&code=" + code
#
#     print(access_token_request_uri)
#
#     return redirect('index')
#
# def kakao_login(request):
#     login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'
#     client_id = 'e7dfabcc5fb3299e38be6f6c6af72553'
#     redirect_uri = 'http://127.0.0.1:8000/oauth'
#
#     login_request_uri = \
#         login_request_uri + 'client_id=' + client_id + '&redirect_uri=' + redirect_uri + '&response_type=code'
#
#     request.session['client_id'] = client_id
#     request.session['redirect_uri'] = redirect_uri
#
#     return redirect(login_request_uri)


def logout(request):
    # auth.logout(request)
    return redirect('index')
