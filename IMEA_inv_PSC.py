from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
from datetime import datetime as dt 
import os

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'G:\Fractal\Europe PSC (15-SPG-1056)\Automation\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"G:\\Fractal\\Europe PSC (15-SPG-1056)\\Automation\\Inventory\\chromedriver.exe")

browser.get("https://k8p.na.pg.com/irj/servlet/prt/portal/prtroot/pcd!3aportal_content!2fcom.sap.pct!2fplatform_add_ons!2fcom.sap.ip.bi!2fiViews!2fcom.sap.ip.bi.bex?BOOKMARK=00O2TO0R8PTK73RWJB2NYJL4M&VARIABLE_SCREEN=X")
time.sleep(10)
browser.switch_to_frame("iframe_Roundtrip_9223372036563636042")
browser.find_element_by_id("DLG_VARIABLE_vsc_DropdownVariants_combobox-btn")
browser.find_element_by_id('DLG_VARIABLE_vsc_cvl_VAR_1_INPUT_inp').clear()
now=datetime.datetime.now()


def Tuesday_UPI():												#Foe Last Friday Data
	browser.get("https://k8p.na.pg.com/irj/servlet/prt/portal/prtroot/pcd!3aportal_content!2fcom.sap.pct!2fplatform_add_ons!2fcom.sap.ip.bi!2fiViews!2fcom.sap.ip.bi.bex?BOOKMARK=00O2TO0R8PTK73RX0DXG16BVJ&VARIABLE_SCREEN=X")
	time.sleep(10)
	browser.switch_to_frame("iframe_Roundtrip_9223372036563636042")
	browser.find_element_by_id('DLG_VARIABLE_vsc_cvl_VAR_1_INPUT_inp').clear()
	now=datetime.datetime.now()
	Last_Friday=now+datetime.timedelta(days=-4)
	Last_Friday=Last_Friday.strftime("%d.%m.%Y")   								#Taking Yesterdays.
	browser.find_element_by_name('DLG_VARIABLE_vsc_cvl_VAR_1_INPUT_inp').send_keys(Last_Friday)
	browser.find_element_by_id('DLG_VARIABLE_dlgBase_BTNOK').click()   					#Page will Load

	#browser.switch_to_frame("iframe_Roundtrip_9223372036563636042")
	browser.find_element_by_id('MENU_ITEM_1_menu_unid16-btn').click()
	browser.switch_to_frame("sapPopupMainId_X0")
	browser.find_element_by_id('MENU_ITEM_1_menu_unid21').click()
	time.sleep(10)
	browser.close()

today=dt.today().weekday()  

if(today == 1):  												#Checking for tuesday
	Yest_1=now+datetime.timedelta(days=-1)
	Yest_1=Yest_1.strftime("%d.%m.%Y")   #Taking Yesterdays.
	browser.find_element_by_name('DLG_VARIABLE_vsc_cvl_VAR_1_INPUT_inp').send_keys(Yest_1)
	browser.find_element_by_id('DLG_VARIABLE_dlgBase_BTNOK').click()   						#Page will Load


	browser.find_element_by_id('MENU_ITEM_1_menu_unid16-btn').click()
	browser.switch_to_frame("sapPopupMainId_X0")
	browser.find_element_by_id('MENU_ITEM_1_menu_unid21').click()
	time.sleep(10)
	
	Tuesday_UPI()
	
else :
	Yest_1=now+datetime.timedelta(days=-1)
	Yest_1=Yest_1.strftime("%d.%m.%Y")   #Taking Yesterdays.
	browser.find_element_by_name('DLG_VARIABLE_vsc_cvl_VAR_1_INPUT_inp').send_keys(Yest_1)
	
	browser.find_element_by_id('DLG_VARIABLE_dlgBase_BTNOK').click()   						#Page will Load


	browser.find_element_by_id('MENU_ITEM_1_menu_unid16-btn').click()
	browser.switch_to_frame("sapPopupMainId_X0")
	browser.find_element_by_id('MENU_ITEM_1_menu_unid21').click()
	time.sleep(10)

	browser.close()

