from django.http import HttpResponse
from django.shortcuts import render
import re
import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import csv

def index(request):
    return render(request,'app1/index.html')

def emails_text(request):
    return render(request,'app1/emails_text _1.html')

def phone_numbers_text(request):
    return render(request,'app1/phone_number_text.html')

def url_text(request):
    return render(request,'app1/url_text.html')

# def analyze(request):
#     text=request.POST.get("text")
#     check1=request.POST.get('extract_emails',"off")
#     check2=request.POST.get('extract_phone_no.',"off")
#     check3 = request.POST.get('extract_urls.', "off")
#     if check2=='on':
#         phone_number=re.findall('[0-9]+',text)
#         param={'res':phone_number}
#         return render(request,'app1/analyze.html',param)
#     elif check1=='on':
#         emails=re.findall('\S+@\S+',text)
#         param={'res':emails}
#         return render(request,'app1/analyze.html',param)
#     else:
#         url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]| [! * \(\),] | (?: %[0-9a-fA-F][0-9a-fA-F]))+',text)
#         print(url)
#         param={'res':url}
#         return render(request,'app1/analyze.html',param)

def web_scrape(request):
    s = "<button type='button'> <a href = 'http://127.0.0.1:8000/url_scraping'>Extract URLs from the link</a></button> <br> " \
        "<button type='button'> <a href = 'http://127.0.0.1:8000/download_pdf'>Download PDF from the URL</a></button>"
    return HttpResponse(s)
    # return render(request,"app1/web_scrape.html")

def download_pdf(request):
    return render(request,"app1/download_pdf.html")
def download_pdf_result(request):
    if request.method=="POST":
        # urls = ['http://www.edudel.nic.in/welcome_folder/SupportMaterial2019_20/IX/English/9_sm_maths_eng_2019_20.pdf']
        text_urls=request.POST.get("txt1")
        print(text_urls)
        # print(type(text_urls))
        # urls=list(text_urls)
        # print(urls)
        # print(type(urls))
        name=text_urls.split('/')[-1]
        print(name)
        myfile = requests.get(text_urls, allow_redirects=True,stream=True)
        with open(name, 'wb')as pdf:
            for chunk in myfile.iter_content(chunk_size=1024):
                if chunk:
                    pdf.write(chunk)

        return HttpResponse("Your PDF is downloaded")

def url_scrape(request):
    return render(request,"app1/url_scrape.html")
def url_scraping_result(request):
    # text=request.POST.get('text')
    # url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]| [! * \(\),] | (?: %[0-9a-fA-F][0-9a-fA-F]))+', text)
    # first_url=url[0]
    if request.method=="POST":
        # first_url="https://www.aldaily.com"
        first_url=request.POST.get("txt1")
        r=requests.get(first_url)
        htmlcontent=r.content
        # print(htmlcontent)
        soup=BeautifulSoup(htmlcontent,'html.parser')
        links=[]
        for link in soup.find_all('a'):
            links.append(link.get('href'))
            # print("coming links",links)
        # print("final links",links)
        param={'res':links}
        return render(request, 'app1/url_scrape_result.html', param)

def emails_scrape(request):
    return render(request,"app1/email_scrape.html")
def emails_scraping_result(request):
    if request.method=="POST":
        url=request.POST.get('txt1')
        # first_url = "https://www.aldaily.com"
        r=requests.get(url)
        htmlcontent=r.content
        soup=BeautifulSoup(htmlcontent,"html.parser")
        myfile=open("1.txt","w",encoding='utf-8')
        myfile.write(str(soup))
        myfile.close()
        myfile=open("1.txt","r",encoding='utf=8')
        content=myfile.read()
        myfile.close()
        os.remove("1.txt")
        emails = re.findall('\S+@\S+', content)
        # print(emails)
        param = {'res': emails}
        return render(request, 'app1/email_scrape_result.html', param)

def phone_number_scrape(request):
    return render(request,'app1/phone_number_scrape.html')
def phoneNumber_scraping_result(request):
    if request.method=='POST':
        # url = 'https://www.aldaily.com'
        url=request.POST.get("txt1")
        r = requests.get(url)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent,"html.parser")
        myfile = open("1.txt", "w", encoding='utf-8')
        myfile.write(str(soup))
        myfile.close()
        myfile = open("1.txt", "r", encoding='utf=8')
        content = myfile.read()
        myfile.close()
        os.remove("1.txt")
        phone_number = re.findall('[0-9]+', content)
        param = {'res': phone_number}
        return render(request, 'app1/phone_number_scrape_result.html', param)

def google_maps(request):
    return render(request,"app1/gmaps.html")

def google_maps_redirect(request):
    if request.method=="POST":
        text=request.POST.get('text')
        print(text)
        queries=list(text.split('\r\n'))
        print(queries)
        browser = webdriver.Chrome("C:/Users/Divij/Downloads/chromedriver.exe")
        browser.get("https://www.google.com/maps/")
        for i in queries:
            filename=i
            search = browser.find_element_by_id("searchboxinput")
            search.send_keys(i)
            time.sleep(2)
            click_me = browser.find_element_by_id("searchbox-searchbutton")
            click_me.click()
            time.sleep(4)
            fn = open(filename + '.csv', mode='a', encoding="utf-8")
            write_outfile = csv.writer(fn)
            next_page = browser.find_element_by_class_name("n7lv7yjyC35__button-next-icon")
            count = 0
            while True:
                click_me = browser.find_elements_by_xpath("//h3[@class='section-result-title']")
                print(len(click_me))
                click_me1 = click_me
                for i in range(0, len(click_me1)):
                    count = count + 1
                    time.sleep(2)
                    click_me[i].click()
                    time.sleep(2)
                    Name = browser.find_elements_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/h1')
                    Address = browser.find_elements_by_xpath("(//span[@class='widget-pane-link'])[3]")
                    Number = browser.find_elements_by_xpath("(//span[@class='widget-pane-link'])[5]")
                    Website = browser.find_elements_by_xpath("(//span[@class='widget-pane-link'])[6]")
                    if len(Address) > 0 and len(Number) > 0 and len(Website) > 0 and len(Name) > 0:
                        Name = browser.find_element_by_xpath(
                            '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/h1').text
                        Address = browser.find_element_by_xpath("(//span[@class='widget-pane-link'])[3]").text
                        Number = browser.find_element_by_xpath("(//span[@class='widget-pane-link'])[5]").text
                        Website = browser.find_element_by_xpath("(//span[@class='widget-pane-link'])[6]").text
                        # print(Name,Number,Address,Website)
                        write_outfile.writerow([Name, Number, Address, Website])
                        print("done")
                    time.sleep(2)
                    browser.find_element_by_xpath("//*[text()='Back to results']").click()
                    time.sleep(2)
                    click_me = browser.find_elements_by_xpath("//h3[@class='section-result-title']")
                    print(len(click_me))
                    time.sleep(2)
                next_page = browser.find_element_by_class_name("n7lv7yjyC35__button-next-icon")
                if next_page.is_enabled() and count < 20:
                    next_page.click()
                else:
                    break
            search.clear()
        print('finished')
    return HttpResponse("welcome to google maps redirect")


