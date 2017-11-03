import sys
import os
from splinter import Browser
from  model.pageObject import Page 
from  model.testObject import Test
from colorama import init,Fore, Back, Style
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from random import randint

##colorama init
init()


######################################
######################################
##########Website variables############
######################################
######################################

email = "emailTEST"

######################################
######################################
##########Global variables############
######################################
######################################
globalEnv = ""
globalBrowser = ""
globalLang =""
globalErrors = "None"
mobile_emulation = {
				"deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
				"userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
######################################
######################################
########Function Declaration##########
######################################
######################################



########     Util functions    #######
def printError(browser,function):
	browser.driver.save_screenshot(function +'_'+globalEnv +'_'+globalBrowser+'_'+globalLang+'.png')
	print(Fore.RED+"Error : " + function)
	global  globalErrors
	globalErrors= "yes"


def removeLangModal(browser):	
	try:
		browser.execute_script("$('.countryPickerPopup').remove();")
	except:		
		printError(browser,sys._getframe().f_code.co_name)
		
def removeSaleModal(browser):
	try:
		
		browser.execute_script("$('#cboxClose').click();")
	except:		
		printError(browser,sys._getframe().f_code.co_name)
		
def removeModals(browser):

	try:
		removeSaleModal(browser)
		removeLangModal(browser)
	except:		
		printError(browser,sys._getframe().f_code.co_name)
		
		
def printFunction(function,beginOrEnd ):
	print (Fore.CYAN+"*"+beginOrEnd+" of "+function)
	
	
########    End  Util functions    #######


########   Test functions    #######

def visitUrl(browser,url):
	printFunction(sys._getframe().f_code.co_name,"Begin" )
	browser.visit(url)
	printFunction(sys._getframe().f_code.co_name,"End" )
	
def goToLoginPage(browser,language):
	printFunction(sys._getframe().f_code.co_name,"Begin" )
	try:
		button = browser.find_link_by_href('/'+language+'/profile/login.jsp?h=true')	
		removeModals(browser)
		button.click()		
	except:		
		printError(browser,sys._getframe().f_code.co_name)
	printFunction(sys._getframe().f_code.co_name,"End" )
	
	
def clickRegisterButton(browser):
	printFunction(sys._getframe().f_code.co_name,"Begin" )
	try:
		#removeModals(browser)
		browser.execute_script("$('#signupBtn').click();")
		#button = browser.find_by_id('signupBtn')	
		#button.click()		
	except:		
		printError(browser,sys._getframe().f_code.co_name)
	printFunction(sys._getframe().f_code.co_name,"End" )




def setFirstForm(browser):
	browser.fill("loginEmail",str(randint(0, 100))+"email"+str(randint(0, 100))+"@gmail.com")
	browser.fill("/atg/userprofiling/ProfileFormHandler.value.password","Dynamite1!")
	
	
########    End  Test functions    #######

def beginTest(testUrl,browserType,language):
	if browserType == 'chrome':
		print (Fore.WHITE+"------------------------")
		print (Fore.WHITE+"Begin test")
		print (Fore.WHITE+"------------------------")
		with Browser('chrome') as browser:
			
			#Setup browser
			if globalEnv == "Mobile":
				chrome_options = Options()
				chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
				driver = webdriver.Chrome(chrome_options = chrome_options)
				browser.driver = driver
				
			# Visit URL
			url = testUrl+"/"+language+"/"
			visitUrl(browser,url)
			goToLoginPage(browser,language)			
			clickRegisterButton(browser)
			setFirstForm(browser)
			
			#Make sure program doesnt close too soon
			os.system("pause")
			
		print (Fore.WHITE+"------------------------")
		print (Fore.WHITE+"End of the test")
		print (Fore.WHITE+"------------------------")
		if globalErrors != "yes":
			print (Fore.GREEN+"No errors")
		else:
			print(Fore.RED+"Finished with errors, check the screenshots")
		
######################################
######################################
############Variable init#############
######################################
######################################

testPage= Page(["https://uat3.dynamiteclothing.com","https://muat3.dynamiteclothing.com"])
##testPage= Page(["https://uat3.dynamiteclothing.com"])
testObject = Test("achat", testPage)

print (Fore.WHITE+"Original page url : "+testObject.page.pageUrls[0])
for browserName in testObject.browsers:
	compter = 0
	globalEnv = "Desktop"
	for pageUrl in testObject.page.pageUrls:
		if compter != 0 :
			globalEnv = "Mobile"
		
		for language in testObject.page.pageLanguages: 
			print (Fore.WHITE+"Url : "+ pageUrl+ " - Browser : "+browserName+" - Lang : "+language +"- Env : "+globalEnv);
			globalLang = language
			globalBrowser = browserName
			beginTest(pageUrl,browserName,language)
			
		compter += 1

		
			
			
