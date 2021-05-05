import requests
import sys
import itertools
from selenium import webdriver
from time import sleep

path = sys.argv[1]
var = path.split('/')
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

