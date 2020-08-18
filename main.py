from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import random
import string
import os
import time

#target = 'sara13winter@gmail.com'
target = 'teste.spam.2112@gmail.com'
options = [0,2,4]
SLEEP = 0

class VampetaBot():
	def __init__(self):
		self.driver = webdriver.Chrome(executable_path='./chromedriver')
		self.asciidick = \
		'░░░░█─────────────█──▀──\n'\
		'░░░░▓█───────▄▄▀▀█──────\n'\
		'░░░░▒░█────▄█▒░░▄░█─────\n'\
		'░░░░░░░▀▄─▄▀▒▀▀▀▄▄▀─────\n'\
		'░░░░░░░░░█▒░░░░▄▀───────\n'\
		'▒▒▒░░░░▄▀▒░░░░▄▀────────\n'\
		'▓▓▓▓▒░█▒░░░░░█▄─────────\n'\
		'█████▀▒░░░░░█░▀▄────────\n'\
		'█████▒▒░░░▒█░░░▀▄───────\n'\
		'███▓▓▒▒▒▀▀▀█▄░░░░█──────\n'\
		'▓██▓▒▒▒▒▒▒▒▒▒█░░░░█─────\n'\
		'▓▓█▓▒▒▒▒▒▒▓▒▒█░░░░░█────\n'\
		'░▒▒▀▀▄▄▄▄█▄▄▀░░░░░░░█───\n'


	def run(self):
		self.driver.get('https://www.trash-mail.com/compose-mail/')
		sleep(SLEEP)
		
		while True:
			start = time.time()

			while True:
				try:
					combo_box = Select(self.driver.find_element_by_xpath('//*[@id="form-domain"]'))
					combo_box.select_by_index(random.choice(options))
					sleep(SLEEP)
					break
				except:
					None

			while True:
				try:
					to_input = self.driver.find_element_by_xpath('//*[@id="form-to"]')
					to_input.send_keys(target)
					sleep(SLEEP)
					break
				except:
					None

			while True:
				try:
					subject_input = self.driver.find_element_by_xpath('//*[@id="form-subject"]')
					subject_input.send_keys('the great chain of being')
					sleep(SLEEP)
					break
				except:
					None	

			while True:
				try:
					message_input = self.driver.find_element_by_xpath('//*[@id="editor"]')
					message_input.send_keys(self.asciidick)
					sleep(SLEEP)
					break
				except:
					None

			while True:
				try:
					file_input = self.driver.find_element_by_xpath('//*[@id="file-upload-group"]/div/span/input')
					file_input.send_keys(os.getcwd() + '/vampeta.jpg')
					sleep(SLEEP)
					break
				except:
					None

			while True:
				try:
					from_input = self.driver.find_element_by_xpath('//*[@id="form-from"]')
					from_input.send_keys(''.join(random.choices(string.ascii_uppercase + string.digits, k=12)))
					sleep(SLEEP)
					break
				except:
					None

			while True:
				try:
					send_btn = self.driver.find_element_by_xpath('//*[@id="send-mails"]')
					send_btn.click()
					sleep(0.5)
					break
				except:
					None

			while True:
				try:
					logout_btn = self.driver.find_element_by_xpath('//*[@id="close-mailbox"]')
					logout_btn.click()
					sleep(0.5)
					break
				except:
					None

			end = time.time()

			print('time:', end-start)


VampetaBot().run()