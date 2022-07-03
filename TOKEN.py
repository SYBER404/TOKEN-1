#!/usr/bin/python2
#coding=utf-8


import requests, re, os, time

logo = ('''\033[1;32m
 ___________  ______    __   ___  _______  _____  ___   
("     _   ")/    " \  |/"| /  ")/"     "|(\"   \|"  \  
 )__/  \\__/// ____  \ (: |/   /(: ______)|.\\   \    | 
    \\_ /  /  /    ) :)|    __/  \/    |  |: \.   \\  | 
    |.  | (: (____/ // (// _  \  // ___)_ |.  \    \. | 
    \:  |  \        /  |: | \  \(:      "||    \    \ | 
     \__|   \"_____/   (__|  \__)\_______) \___|\____\) 

\033[1;37mCoding By : Pahrul Aguspriana XD.
''')

os.system('clear')
print(logo)
         
urls="https://business.facebook.com/business_locations"
_ses=requests.Session()

def real_time():
	from time import time
	return str(time()).split('.')[0]

def convert(cok):
	__for=(
			'datr='+cok['datr']
		)+';'+(
			'c_user='+cok['c_user']
		)+';'+(
			'fr='+cok['fr']
		)+';'+(
			'xs='+cok['xs'] )
	return __for
	

def email():
	os.system('clear')
	print(logo)
	try:
		_agent=open('agent.txt').read()
	except:
		try:
			_agent=raw_input("\033[1;97m(+) enter your user agent :\033[1;92m ")
			open("agent.txt", 'a').write(_agent)
		except:
			_agent=input("\033[1;97m(+) enter your user agent :\033[1;92m ")
			open("agent.txt", 'a').write(_agent)
	try:
		user=raw_input("\033[1;97m(+) email/username :\033[1;92m ")
		pw=raw_input("\033[1;97m(+) password       :\033[1;92m ")
	except:
		user=input("\033[1;97m(+) email/username :\033[1;92m ")
		pw=input("\033[1;97m(+) password       :\033[1;92m ")
	try:
		_head={
			'Host':'m.facebook.com',
				'cache-control':'max-age=0',
			'upgrade-insecure-requests':'1',
				'user-agent':_agent,
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'sec-fetch-mode':'navigate',
				'sec-fetch-user':'?1',
			'sec-fetch-dest':'document',
				'accept-encoding':'gzip, deflate',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
		}
		try:
			r=_ses.get("https://m.facebook.com/", headers=_head).text.encode('utf-8')
		except:
			r=_ses.get("https://m.facebook.com/", headers=_head).text
		_head2={
			'Host':'m.facebook.com',
				'user-agent':_agent,
			'content-type':'application/x-www-form-urlencoded',
				'x-fb-lsd':re.search('name="lsd" value="(.*?)"', str(r)).group(1),
			'accept':'*/*',
				'origin':'https://m.facebook.com',
			'sec-fetch-site':'same-origin',
				'sec-fetch-mode':'cors',
			'sec-fetch-dest':'empty',
				'referer':'https://m.facebook.com/',
			'accept-encoding':'gzip, deflate',
				'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
		}
		payload={
			"fb_dtsg":re.search('{"token":"(.*?)"', str(r)).group(1).encode('utf-8'),
				"lsd":re.search('name="lsd" value="(.*?)"', str(r)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(r)).group(1),
				"m_ts":re.search('name="m_ts" value="(.*?)"', str(r)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(r)).group(1),
				"try_number":"0",
			"unrecognized_tries":"0",
				"prefill_contact_point":user,
			"prefill_source":"browser_dropdown",
				"prefill_type":"contact_point",
			"first_prefill_source":"browser_dropdown",
				"first_prefill_type":"contact_point",
			"had_cp_prefilled":True,
				"had_password_prefilled":False,
			"is_smart_lock":False,
				"bi_xrwh":"0",
			"__dyn":"",
				"__csr":"",
			"__req":"2",
				"__a":"",
			"__user":"0",
				"email":user,
			"encpass":"#PWD_BROWSER:0:"+real_time()+":"+pw
		}
		_ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", headers=_head2, data=payload)
		cok=_ses.cookies.get_dict()
		if 'c_user' in (cok):
			_head={
				'Host':'business.facebook.com',
					'cache-control':'max-age=0',
				'upgrade-insecure-requests':'1',
					'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
				'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
					'content-type' : 'text/html; charset=utf-8',
				'accept-encoding':'gzip, deflate',
					'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}    
			_r=_ses.get(urls, headers=_head)
			_p=re.search('(EAAG\w+)', _r.text)
			_token=_p.group(1)
			if 'EAA' in _token:
				print('\n\033[1;97m(+) cookie :\033[1;92m '+convert(cok))
				open("cookie.txt", 'a').write(convert(cok))
				print('\n\033[1;97m(+) token  :\033[1;92m '+_token )
				open("token.txt", 'a').write(_token)
				print('\033[1;97m')
				exit()
		elif 'checkpoint' in (cok):
			exit('\033[1;93m(×) Akun terkena checkpoint !')
		else:
			print('\033[1;91m(×) email/password salah !')
			time.sleep(3)
			masuk()
	except AttributeError:
		print('\033[1;91m(×) email/password salah !')
		time.sleep(3)
		masuk()

def cookie():
	os.system('clear')
	print(logo)
	try:
		_cookie=raw_input('\033[1;97m(+) cookie :\033[1;92m ')
	except:
		_cookie=input('\033[1;97m(+) cookie :\033[1;92m ')
	try:
		_head={
			'Host':'business.facebook.com',
				'cache-control':'max-age=0',
			'upgrade-insecure-requests':'1',
				'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
			'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
				'content-type' : 'text/html; charset=utf-8',
			'accept-encoding':'gzip, deflate',
				'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			'cookie': _cookie
		}         
		_r=_ses.get(urls, headers=_head)
		_p=re.search('(EAAG\w+)', _r.text)
		_h=_p.group(1)
		if 'EAA' in _h:
			exit('\033[1;97m(+) Token :\033[1;92m '+_h)
	except (AttributeError, requests.exceptions.TooManyRedirects):
		print('\033[1;97m(×) cookie salah !')
		time.sleep(3)
		masuk()
		
def masuk():
	os.system("clear")
	print(logo)
	print("\033[1;97m(1) email/password to cookie & token")
	print("(2) cookie to token")
	print("(0) log out\n")
	while True:
		try:
			pahrul=raw_input("(+) choose : ")
		except:
			pahrul=input("(+) choose : ")
		if pahrul in ['01', '1']:
			exit(email())
		elif pahrul in ['02', '2']:
			exit(cookie())
		elif pahrul in ['00', '0']:
			exit()
		else:
			continue

if __name__ == '__main__':
	masuk()

# mau ngapain cuk ?