import urllib.request

url = str(input())
try:
    site = urllib.request.urlopen(f"https://{url}/")
except urllib.error.URLError:
    print('O acesso está offline!')
else:
    print('Site acessado com sucesso!')