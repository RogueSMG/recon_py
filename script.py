import requests
import sys
import itertools
from selenium import webdriver
from time import sleep
import argparse
import select
import os


def brute():
	if len(sys.argv) > 1:
		filename = sys.argv[1]

		with open(filename) as f:
			lines = f.readlines()
		for x in range(len(lines)):
			url_cut = lines[x].replace("https://www.","")
			var = url_cut.split('/')
			url =  var[0]
			del var[0]
			perm = list(itertools.permutations(var))
			res = [ '/'.join(x) for x in perm ]
			final_list = []
			for x in range(len(res)):
				final_list.append(url+"/"+res[x])
			for y in range(len(final_list)):
				req = requests.get("https://"+final_list[y])
				if(req == '200'):
					driver = webdriver.Firefox()
					driver.get("https://"+final_list[y])
					sleep(1)
					driver.get_screenshot_as_file(final_list[y])
					driver.quit()

	elif select.select([sys.stdin,],[],[],0.0)[0]:
		for lines in sys.stdin:
			url_cut = lines.replace("https://www.","")
			var = url_cut.split('/')
			url =  var[0]
			del var[0]
			perm = list(itertools.permutations(var))
			res = [ '/'.join(x) for x in perm ]
			final_list = []
			for x in range(len(res)):
				final_list.append(url+"/"+res[x])
			for y in range(len(final_list)):
				req = requests.get("https://"+final_list[y])
				if(req == '200'):
					driver = webdriver.Firefox()
					driver.get("https://"+final_list[y])
					sleep(1)
					driver.get_screenshot_as_file(final_list[y])
					driver.quit()



