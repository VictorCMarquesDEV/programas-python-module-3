import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.request.URLError:
    print('O site não está acessível no momento')
else:
    print('Consegui abrir o site com sucesso!')
