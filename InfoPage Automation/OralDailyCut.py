from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import shutil
import os.path



#LOGIN

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"path\\chromedriver.exe")

browser.get("Login link")

browser.find_element_by_id('sawlogonuser').send_keys('username')
browser.find_element_by_id('sawlogonpwd').send_keys('Password')
browser.find_element_by_id('idlogon').click()




#Daily_Cuts-file_1


try :
	browser.get("link")
	#time.sleep(20)
	while(True):
		try :
			browser.find_element_by_xpath('//*[@title="Display and edit views of results"]').click()
			if(browser.find_elements_by_class_name("CVUICell")):
				print("Element found")
				break
		except:
			print("Still finding")
			continued
	
	for i in range(0,1):
		if(browser.find_elements_by_class_name("ErrorInfo")):
			print("No Data available and i love my life")
			raise Exception('i love my life')
			break
		else :
			while(True):
				try :	
					if(browser.find_element_by_xpath('//*[@title="Export this analysis"]')):
						browser.find_element_by_xpath('//*[@title="Export this analysis"]').click()
						browser.find_element_by_xpath('//*[@aria-label="Data                        "]').click()
						browser.find_element_by_xpath('//*[@aria-label="CSV Format"]').click()
						#time.sleep(10)
				
						break
				except :
					print("waiting for Export Tab")
					pass
			while (True):
				if(os.path.exists("path\\Daily_Cuts-file_1.csv")):
					browser.close()
					shutil.move("path\\Daily_Cuts-file_1.csv","path\\Daily_Cuts-file_1.csv")
					break
				else:
					print("waiting for file to download")
					continue
		

except :
	print("NO FILES UPDATED FOR Daily_Cuts-file_1")
	browser.close()
	with open("path\\Daily_Cuts-file_1.csv", "w") as my_empty_csv:
		pass



#LOGIN

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"path\\chromedriver.exe")

browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Dashboard")

browser.find_element_by_id('sawlogonuser').send_keys('username')
browser.find_element_by_id('sawlogonpwd').send_keys('Password')
browser.find_element_by_id('idlogon').click()




#Daily_Cuts-file_2


try :
	browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Answers&path=%2Fshared%2FCase%20Fill%20Rate%2F_filters%2FCFREIMEA%2FGroups%20and%20Calculated%20Items%2FOther%2FEPSC_CFR_CEEME_WE%2FCFR%20Oral%20Care_Trupti%2FDaily_Cuts-file_2")
	#time.sleep(20)
	while(True):
		try :
			browser.find_element_by_xpath('//*[@title="Display and edit views of results"]').click()
			if(browser.find_elements_by_class_name("CVUICell")):
				print("Element found")
				break
		except:
			print("Still finding")
			continued
	
	for i in range(0,1):
		if(browser.find_elements_by_class_name("ErrorInfo")):
			print("No Data available and i love my life")
			raise Exception('i love my life')
			break
		else :
			while(True):
				try :	
					if(browser.find_element_by_xpath('//*[@title="Export this analysis"]')):
						browser.find_element_by_xpath('//*[@title="Export this analysis"]').click()
						browser.find_element_by_xpath('//*[@aria-label="Data                        "]').click()
						browser.find_element_by_xpath('//*[@aria-label="CSV Format"]').click()
						#time.sleep(10)
				
						break
				except :
					print("waiting for Export Tab")
					pass
			while (True):
				if(os.path.exists("path\\Daily_Cuts-file_2.csv")):
					browser.close()
					shutil.move("path\\Daily_Cuts-file_2.csv","path\\Daily_Cuts-file_2.csv")
					break
				else:
					print("waiting for file to download")
					continue
		

except :
	print("NO FILES UPDATED FOR Daily_Cuts-file_2")
	browser.close()
	with open("path\\Daily_Cuts-file_2.csv", "w") as my_empty_csv:
		pass




#LOGIN

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"path\\chromedriver.exe")

browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Dashboard")

browser.find_element_by_id('sawlogonuser').send_keys('username')
browser.find_element_by_id('sawlogonpwd').send_keys('Password')
browser.find_element_by_id('idlogon').click()




#Daily_Cuts-file_3


try :
	browser.get("link")
	#time.sleep(20)
	while(True):
		try :
			browser.find_element_by_xpath('//*[@title="Display and edit views of results"]').click()
			if(browser.find_elements_by_class_name("CVUICell")):
				print("Element found")
				break
		except:
			print("Still finding")
			continued
	
	for i in range(0,1):
		if(browser.find_elements_by_class_name("ErrorInfo")):
			print("No Data available and i love my life")
			raise Exception('i love my life')
			break
		else :
			while(True):
				try :	
					if(browser.find_element_by_xpath('//*[@title="Export this analysis"]')):
						browser.find_element_by_xpath('//*[@title="Export this analysis"]').click()
						browser.find_element_by_xpath('//*[@aria-label="Data                        "]').click()
						browser.find_element_by_xpath('//*[@aria-label="CSV Format"]').click()
						#time.sleep(10)
				
						break
				except :
					print("waiting for Export Tab")
					pass
			while (True):
				if(os.path.exists("path\\Daily_Cuts-file_3.csv")):
					browser.close()
					shutil.move("path\\Daily_Cuts-file_3.csv","path\\Daily_Cuts-file_3.csv")
					break
				else:
					print("waiting for file to download")
					continue
		

except :
	print("NO FILES UPDATED FOR Daily_Cuts-file_3")
	browser.close()
	with open("path\\Daily_Cuts-file_3.csv", "w") as my_empty_csv:
		pass

