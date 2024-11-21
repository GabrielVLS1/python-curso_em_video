import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())


#import urllib
#import urllib.request




''' ↓↓↓↓↓↓↓↓ ABREM O SITE ↓↓↓↓↓↓↓↓ '''

# import webbrowser
# webbrowser.open('http://example.com')


# import os
# os.system("start \"\" http://www.pudim.com.br")
