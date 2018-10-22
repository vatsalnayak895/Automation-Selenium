from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import shutil
import os.path



#LOGIN

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'G:\Fractal\Europe PSC (15-SPG-1056)\Automation\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Inventory\\chromedriver.exe")

browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Dashboard")

browser.find_element_by_id('sawlogonuser').send_keys('karri.k')
browser.find_element_by_id('sawlogonpwd').send_keys('Ravitej2')
browser.find_element_by_id('idlogon').click()




#Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_1


try :
	browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Answers&path=%2Fshared%2FCase%20Fill%20Rate%2F_filters%2FCFREIMEA%2FGroups%20and%20Calculated%20Items%2FOther%2FEPSC_CFR_CEEME_WE%2FCFR%20Oral%20Care_Trupti%2FDaily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_1")
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
				if(os.path.exists("G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Downloads\\Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_1.csv")):
					browser.close()
					shutil.move("G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Downloads\\Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_1.csv","G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Oralcare\\Regular files\\Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_1.csv")
					break
				else:
					print("waiting for file to download")
					continue
		

except :
	print("NO FILES UPDATED FOR Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_1")
	browser.close()
	with open("G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Oralcare\\Regular files\\Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_1.csv", "w") as my_empty_csv:
		pass



#LOGIN

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'G:\Fractal\Europe PSC (15-SPG-1056)\Automation\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Inventory\\chromedriver.exe")

browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Dashboard")

browser.find_element_by_id('sawlogonuser').send_keys('karri.k')
browser.find_element_by_id('sawlogonpwd').send_keys('Ravitej2')
browser.find_element_by_id('idlogon').click()




#Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_2


try :
	browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Answers&path=%2Fshared%2FCase%20Fill%20Rate%2F_filters%2FCFREIMEA%2FGroups%20and%20Calculated%20Items%2FOther%2FEPSC_CFR_CEEME_WE%2FCFR%20Oral%20Care_Trupti%2FDaily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_2")
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
				if(os.path.exists("G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Downloads\\Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_2.csv")):
					browser.close()
					shutil.move("G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Downloads\\Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_2.csv","G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Oralcare\\Regular files\\Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_2.csv")
					break
				else:
					print("waiting for file to download")
					continue
		

except :
	print("NO FILES UPDATED FOR Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_2")
	browser.close()
	with open("G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Oralcare\\Regular files\\Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_2.csv", "w") as my_empty_csv:
		pass




#LOGIN

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'G:\Fractal\Europe PSC (15-SPG-1056)\Automation\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Inventory\\chromedriver.exe")

browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Dashboard")

browser.find_element_by_id('sawlogonuser').send_keys('karri.k')
browser.find_element_by_id('sawlogonpwd').send_keys('Ravitej2')
browser.find_element_by_id('idlogon').click()




#Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_3


try :
	browser.get("https://sdl2.na.pg.com:4443/analytics/saw.dll?Answers&path=%2Fshared%2FCase%20Fill%20Rate%2F_filters%2FCFREIMEA%2FGroups%20and%20Calculated%20Items%2FOther%2FEPSC_CFR_CEEME_WE%2FCFR%20Oral%20Care_Trupti%2FDaily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_3")
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
				if(os.path.exists("G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Downloads\\Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_3.csv")):
					browser.close()
					shutil.move("G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Downloads\\Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_3.csv","G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Oralcare\\Regular files\\Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_3.csv")
					break
				else:
					print("waiting for file to download")
					continue
		

except :
	print("NO FILES UPDATED FOR Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_3")
	browser.close()
	with open("G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Oralcare\\Regular files\\Daily_Cuts-CEEMEA_WE_ASIA_(Oral_Care)_3.csv", "w") as my_empty_csv:
		pass

