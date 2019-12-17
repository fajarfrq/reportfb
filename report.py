#!/usr/bin/python2.7
import mechanize,sys,bs4,os
banner ="""
\033[1;33m __  __                 ____                       _ 
|  \/  | __ _ ___ ___  |  _ \ ___ _ __   ___  _ __| |_ 
| |\/| |/ _` / __/ __| | |_) / _ \ '_ \ / _ \| '__| __| 
| |  | | (_| \__ \__ \ |  _ <  __/ |_) | (_) | |  | |_ 
|_|  |_|\__,_|___/___/ |_| \_\___| .__/ \___/|_|   \__| 
\033[1;31mCoded By.VRX       ThX.Deray     \033[1;33m|_|\033[1;31mESBUK       (C)2019\033[1;37m
"""
os.system('clear')
print banner
class report:
	def __init__(self):
		self.b=0
		self.c=0
		self.a()
		
	def a(self):
		try:
			self.aa=open(raw_input("[?] Account list file: ")).read().splitlines()
		except Exception as e:
			print "[!] File Tidak Ada%s"%(e);self.a()
		self.target()
		
	def target(self):
		self.t=raw_input("[?] target id: ")
		if self.t =="":self.target()
		else:
			map(self.report,self.aa)
	
	def report(self,a):
		try:
			m=mechanize.Browser()
			m.set_handle_robots(False)
			m.open("https://mbasic.facebook.com/login")
			m._factory.is_html=True
			m.select_form(nr=0)
			m["email"]=a.split("|")[-0]
			m["pass"]=a.split("|")[-1]
			mm=m.submit().geturl()
			if "save-device" in mm or "m_sess" in mm or "home.php" in mm:
				print 
				self.tray(m,a)
			else:
				print "[!] \033[1;31mlogin gagal\033[1;37m: %s\n"%(a)
		except Exception as e:
			print "[!] report gagal karena: %s\n"%e
			
	def tray(self,m,a):
		m.open("https://mbasic.facebook.com/"+self.t)
		m._factory.is_html=True
		print "[+] %s -> sedang mereport: %s"%(a,m.title())
		m.open(m.click_link(text="Lainnya"))
		m._factory.is_html=True
		m.open(m.click_link(text="Cari Dukungan atau Laporkan Profil"))
		m._factory.is_html=True
		m.select_form(nr=0)
		m["tag"]=["profile_fake_account"]
		m.submit()
		m._factory.is_html=True
		m.select_form(nr=0)
		m["action_key"]=["FRX_PROFILE_REPORT_CONFIRMATION"]
		m.submit()
		m._factory.is_html=True
		m.select_form(nr=0)
		m["checked"]=["yes"]
		m.submit()
		m._factory.is_html=True
		if "untuk Ditinjau" in m.response().read():
			print "[+] \033[1;32msukses dilaporkan!\033[1;37m\n"
report()
			