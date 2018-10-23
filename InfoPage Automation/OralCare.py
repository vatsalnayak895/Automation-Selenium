from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import shutil
import os.path
import os
import sys



#LOGIN

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"path\\chromedriver.exe")

browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Dashboard")

browser.find_element_by_id('sawlogonuser').send_keys('username')
browser.find_element_by_id('sawlogonpwd').send_keys('password')
browser.find_element_by_id('idlogon').click()




#Asia MTD

try :
	browser.get("link")
	#time.sleep(20)
	while(True):
		try :
			if(browser.find_element_by_xpath('//*[@id="d:dashboard~p:j813vgf7fc76knjo~r:lvdiv915qrmtejroLinks"]/tbody/tr/td/a[@title="Refresh the results of the current analysis"]')):
				print("Element found")
				break
		except:
			print("Still finding")
			continue
	
	for i in range(0,1):
		if(browser.find_elements_by_class_name("ErrorInfo")):
			print("No Data available and i love my life")
			raise Exception('i love my life')
			break
		else :
			while(True):
				try :	
					if(browser.find_element_by_xpath('//*[@title="Export to different format"][1]')):
						browser.find_element_by_xpath('//*[@title="Export to different format"][1]').click()
						browser.find_element_by_xpath('//*[@aria-label="Excel"]').click()
	
						browser.find_element_by_xpath('//*[@aria-label="Excel 2007+"]').click()
						time.sleep(10)
				
						break
				except :
					print("waiting for Export Tab")
					pass
			while (True):
				if(os.path.exists("path\\CFR DYNAMIC By Level.xlsx")):
					browser.close()
					shutil.move("path\\CFR DYNAMIC By Level.xlsx","path\\Asia MTD.xlsx")
					break
				else:
					print("waiting for file to download")
					continue
		

except :
	print("NO FILES UPDATED FOR Asia MTD")
	browser.close()
	with open("path\\Asia MTD.csv", "w") as my_empty_csv:
		pass






#LOGIN

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"path\\chromedriver.exe")

browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Dashboard")

browser.find_element_by_id('sawlogonuser').send_keys('username')
browser.find_element_by_id('sawlogonpwd').send_keys('password')
browser.find_element_by_id('idlogon').click()




#Asia L3D

try :
	browser.get("link")
	#time.sleep(20)
	while(True):
		try :
			if(browser.find_element_by_xpath('//*[@id="d:dashboard~p:j813vgf7fc76knjo~r:lvdiv915qrmtejroLinks"]/tbody/tr/td/a[@title="Refresh the results of the current analysis"]')):
				print("Element found")
				break
		except:
			print("Still finding")
			continue
	
	for i in range(0,1):
		if(browser.find_elements_by_class_name("ErrorInfo")):
			print("No Data available and i love my life")
			raise Exception('i love my life')
			break
		else :
			while(True):
				try :	
					if(browser.find_element_by_xpath('//*[@title="Export to different format"][1]')):
						browser.find_element_by_xpath('//*[@title="Export to different format"][1]').click()
						browser.find_element_by_xpath('//*[@aria-label="Excel"]').click()
	
						browser.find_element_by_xpath('//*[@aria-label="Excel 2007+"]').click()
						time.sleep(10)
				
						break
				except :
					print("waiting for Export Tab")
					pass
			while (True):
				if(os.path.exists("path\\CFR DYNAMIC By Level.xlsx")):
					browser.close()
					shutil.move("path\\CFR DYNAMIC By Level.xlsx","path\\Asia L3D.xlsx")
					break
				else:
					print("waiting for file to download")
					continue
		

except :
	print("NO FILES UPDATED FOR Asia L3D")
	browser.close()
	with open("path\\Asia L3D.csv", "w") as my_empty_csv:
		pass






#LOGIN

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"path\\chromedriver.exe")

browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Dashboard")

browser.find_element_by_id('sawlogonuser').send_keys('username')
browser.find_element_by_id('sawlogonpwd').send_keys('password')
browser.find_element_by_id('idlogon').click()




#ASIA Yesterday

try :
	browser.get("link")
	#time.sleep(20)
	while(True):
		try :
			if(browser.find_element_by_xpath('//*[@id="d:dashboard~p:j813vgf7fc76knjo~r:lvdiv915qrmtejroLinks"]/tbody/tr/td/a[@title="Refresh the results of the current analysis"][1]')):
				print("Element found")
				break
		except:
			print("Still finding")
			continue
	
	for i in range(0,1):
		if(browser.find_elements_by_class_name("ErrorInfo")):
			print("No Data available and i love my life")
			raise Exception('i love my life')
			break
		else :
			while(True):
				try :	
					if(browser.find_element_by_xpath('//*[@title="Export to different format"][1]')):
						browser.find_element_by_xpath('//*[@title="Export to different format"][1]').click()
						browser.find_element_by_xpath('//*[@aria-label="Excel"]').click()
	
						browser.find_element_by_xpath('//*[@aria-label="Excel 2007+"]').click()
						time.sleep(10)
				
						break
				except :
					print("waiting for Export Tab")
					pass
			while (True):
				if(os.path.exists("path\\CFR DYNAMIC By Level.xlsx")):
					browser.close()
					shutil.move("path\\CFR DYNAMIC By Level.xlsx","path\\ASIA Yesterday.xlsx")
					break
				else:
					print("waiting for file to download")
					continue
		

except :
	print("NO FILES UPDATED FOR ASIA Yesterday")
	browser.close()
	with open("path\\ASIA Yesterday.csv", "w") as my_empty_csv:
		pass


#LOGIN

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"path\\chromedriver.exe")

browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Dashboard")

browser.find_element_by_id('sawlogonuser').send_keys('username')
browser.find_element_by_id('sawlogonpwd').send_keys('password')
browser.find_element_by_id('idlogon').click()




#CEEMEA MTD

try :
	browser.get("link")
	#time.sleep(20)
	while(True):
		try :
			if(browser.find_element_by_xpath('//*[@id="d:dashboard~p:j813vgf7fc76knjo~r:lvdiv915qrmtejroLinks"]/tbody/tr/td/a[@title="Refresh the results of the current analysis"][1]')):
				print("Element found")
				break
		except:
			print("Still finding")
			continue
	
	for i in range(0,1):
		if(browser.find_elements_by_class_name("ErrorInfo")):
			print("No Data available and i love my life")
			raise Exception('i love my life')
			break
		else :
			while(True):
				try :	
					if(browser.find_element_by_xpath('//*[@title="Export to different format"][1]')):
						browser.find_element_by_xpath('//*[@title="Export to different format"][1]').click()
						browser.find_element_by_xpath('//*[@aria-label="Excel"]').click()
	
						browser.find_element_by_xpath('//*[@aria-label="Excel 2007+"]').click()
						time.sleep(10)
				
						break
				except :
					print("waiting for Export Tab")
					pass
			while (True):
				if(os.path.exists("path\\CFR DYNAMIC By Level.xlsx")):
					browser.close()
					shutil.move("path\\CFR DYNAMIC By Level.xlsx","path\\CEEMEA MTD.xlsx")
					break
				else:
					print("waiting for file to download")
					continue
		

except :
	print("NO FILES UPDATED FOR CEEMEA MTD")
	browser.close()
	with open("path\\CEEMEA MTD.csv", "w") as my_empty_csv:
		pass




#LOGIN

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"path\\chromedriver.exe")

browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Dashboard")

browser.find_element_by_id('sawlogonuser').send_keys('username')
browser.find_element_by_id('sawlogonpwd').send_keys('password')
browser.find_element_by_id('idlogon').click()




#CEEMEA L3D

try :
	browser.get("link")
	#time.sleep(20)
	while(True):
		try :
			if(browser.find_element_by_xpath('//*[@id="d:dashboard~p:j813vgf7fc76knjo~r:lvdiv915qrmtejroLinks"]/tbody/tr/td/a[@title="Refresh the results of the current analysis"]')):
				print("Element found")
				break
		except:
			print("Still finding")
			continue
	
	for i in range(0,1):
		if(browser.find_elements_by_class_name("ErrorInfo")):
			print("No Data available and i love my life")
			raise Exception('i love my life')
			break
		else :
			while(True):
				try :	
					if(browser.find_element_by_xpath('//*[@title="Export to different format"][1]')):
						browser.find_element_by_xpath('//*[@title="Export to different format"][1]').click()
						browser.find_element_by_xpath('//*[@aria-label="Excel"]').click()
	
						browser.find_element_by_xpath('//*[@aria-label="Excel 2007+"]').click()
						time.sleep(10)
				
						break
				except :
					print("waiting for Export Tab")
					pass
			while (True):
				if(os.path.exists("path\\CFR DYNAMIC By Level.xlsx")):
					browser.close()
					shutil.move("path\\CFR DYNAMIC By Level.xlsx","path\\CEEMEA L3D.xlsx")
					break
				else:
					print("waiting for file to download")
					continue
		

except :
	print("NO FILES UPDATED FOR CEEMEA L3D")
	browser.close()
	with open("path\\CEEMEA L3D.csv", "w") as my_empty_csv:
		pass




#LOGIN

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"path\\chromedriver.exe")

browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Dashboard")

browser.find_element_by_id('sawlogonuser').send_keys('username')
browser.find_element_by_id('sawlogonpwd').send_keys('password')
browser.find_element_by_id('idlogon').click()




#CEEMEA Yesterday

try :
	browser.get("link")
	#time.sleep(20)
	while(True):
		try :
			if(browser.find_element_by_xpath('//*[@id="d:dashboard~p:j813vgf7fc76knjo~r:lvdiv915qrmtejroLinks"]/tbody/tr/td/a[@title="Refresh the results of the current analysis"]')):
				print("Element found")
				break
		except:
			print("Still finding")
			continue
	
	for i in range(0,1):
		if(browser.find_elements_by_class_name("ErrorInfo")):
			print("No Data available and i love my life")
			raise Exception('i love my life')
			break
		else :
			while(True):
				try :	
					if(browser.find_element_by_xpath('//*[@title="Export to different format"][1]')):
						browser.find_element_by_xpath('//*[@title="Export to different format"][1]').click()
						browser.find_element_by_xpath('//*[@aria-label="Excel"]').click()
	
						browser.find_element_by_xpath('//*[@aria-label="Excel 2007+"]').click()
						time.sleep(10)
				
						break
				except :
					print("waiting for Export Tab")
					pass
			while (True):
				if(os.path.exists("path\\CFR DYNAMIC By Level.xlsx")):
					browser.close()
					shutil.move("path\\CFR DYNAMIC By Level.xlsx","path\\CEEMEA Yesterday.xlsx")
					break
				else:
					print("waiting for file to download")
					continue
		

except :
	print("NO FILES UPDATED FOR CEEMEA Yesterday")
	browser.close()
	with open("path\\CEEMEA Yesterday.csv", "w") as my_empty_csv:
		pass


	

#LOGIN

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"path\\chromedriver.exe")

browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Dashboard")

browser.find_element_by_id('sawlogonuser').send_keys('username')
browser.find_element_by_id('sawlogonpwd').send_keys('password')
browser.find_element_by_id('idlogon').click()




#Excluded MTD

try :
	browser.get("link")
	#time.sleep(20)
	while(True):
		try :
			if(browser.find_element_by_xpath('//*[@id="d:dashboard~p:j813vgf7fc76knjo~r:lvdiv915qrmtejroLinks"]/tbody/tr/td/a[@title="Refresh the results of the current analysis"]')):
				print("Element found")
				break
		except:
			print("Still finding")
			continue
	
	for i in range(0,1):
		if(browser.find_elements_by_class_name("ErrorInfo")):
			print("No Data available and i love my life")
			raise Exception('i love my life')
			break
		else :
			while(True):
				try :	
					if(browser.find_element_by_xpath('//*[@title="Export to different format"][1]')):
						browser.find_element_by_xpath('//*[@title="Export to different format"][1]').click()
						browser.find_element_by_xpath('//*[@aria-label="Excel"]').click()
	
						browser.find_element_by_xpath('//*[@aria-label="Excel 2007+"]').click()
						time.sleep(10)
				
						break
				except :
					print("waiting for Export Tab")
					pass
			while (True):
				if(os.path.exists("path\\CFR DYNAMIC By Level.xlsx")):
					browser.close()
					shutil.move("path\\CFR DYNAMIC By Level.xlsx","path\\Excluded MTD.xlsx")
					break
				else:
					print("waiting for file to download")
					continue
		

except :
	print("NO FILES UPDATED FOR Excluded MTD")
	browser.close()
	with open("path\\Excluded MTD.csv", "w") as my_empty_csv:
		pass

#LOGIN

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"path\\chromedriver.exe")

browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Dashboard")

browser.find_element_by_id('sawlogonuser').send_keys('username')
browser.find_element_by_id('sawlogonpwd').send_keys('password')
browser.find_element_by_id('idlogon').click()




#Excluded L3D

try :
	browser.get("link")
	#time.sleep(20)
	while(True):
		try :
			if(browser.find_element_by_xpath('//*[@id="d:dashboard~p:j813vgf7fc76knjo~r:lvdiv915qrmtejroLinks"]/tbody/tr/td/a[@title="Refresh the results of the current analysis"]')):
				print("Element found")
				break
		except:
			print("Still finding")
			continue
	
	for i in range(0,1):
		if(browser.find_elements_by_class_name("ErrorInfo")):
			print("No Data available and i love my life")
			raise Exception('i love my life')
			break
		else :
			while(True):
				try :	
					if(browser.find_element_by_xpath('//*[@title="Export to different format"][1]')):
						browser.find_element_by_xpath('//*[@title="Export to different format"][1]').click()
						browser.find_element_by_xpath('//*[@aria-label="Excel"]').click()
	
						browser.find_element_by_xpath('//*[@aria-label="Excel 2007+"]').click()
						time.sleep(10)
				
						break
				except :
					print("waiting for Export Tab")
					pass
			while (True):
				if(os.path.exists("path\\CFR DYNAMIC By Level.xlsx")):
					browser.close()
					shutil.move("path\\CFR DYNAMIC By Level.xlsx","path\\Excluded L3D.xlsx")
					break
				else:
					print("waiting for file to download")
					continue
		

except :
	print("NO FILES UPDATED FOR Excluded L3D")
	browser.close()
	with open("path\\Excluded L3D.csv", "w") as my_empty_csv:
		pass
	

#LOGIN

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"path\\chromedriver.exe")

browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Dashboard")

browser.find_element_by_id('sawlogonuser').send_keys('username')
browser.find_element_by_id('sawlogonpwd').send_keys('password')
browser.find_element_by_id('idlogon').click()




#Excluded Yesterday

try :
	browser.get("link")
	#time.sleep(20)
	while(True):
		try :
			if(browser.find_element_by_xpath('//*[@id="d:dashboard~p:j813vgf7fc76knjo~r:lvdiv915qrmtejroLinks"]/tbody/tr/td/a[@title="Refresh the results of the current analysis"]')):
				print("Element found")
				break
		except:
			print("Still finding")
			continue
	
	for i in range(0,1):
		if(browser.find_elements_by_class_name("ErrorInfo")):
			print("No Data available and i love my life")
			raise Exception('i love my life')
			break
		else :
			while(True):
				try :	
					if(browser.find_element_by_xpath('//*[@title="Export to different format"][1]')):
						browser.find_element_by_xpath('//*[@title="Export to different format"][1]').click()
						browser.find_element_by_xpath('//*[@aria-label="Excel"]').click()
	
						browser.find_element_by_xpath('//*[@aria-label="Excel 2007+"]').click()
						time.sleep(10)
				
						break
				except :
					print("waiting for Export Tab")
					pass
			while (True):
				if(os.path.exists("path\\CFR DYNAMIC By Level.xlsx")):
					browser.close()
					shutil.move("path\\CFR DYNAMIC By Level.xlsx","path\\Excluded Yesterday.xlsx")
					break
				else:
					print("waiting for file to download")
					continue
		

except :
	print("NO FILES UPDATED FOR Excluded Yesterday")
	browser.close()
	with open("path\\Excluded Yesterday.csv", "w") as my_empty_csv:
		pass
	
	


os.system(r'"path\\csv2xlsx.vbs"')  # to convert csv to xlsx

time.sleep(30)

import OralDailyCut

time.sleep(30)

os.system(r'"path\\OralCare.vbs"') #to run the macro