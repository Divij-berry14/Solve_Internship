from django.http import HttpResponse
from django.shortcuts import render
import re
import requests
from bs4 import BeautifulSoup
import os

def index(request):
    return render(request,'app1/index.html')

def analyze(request):
    text=request.POST.get("text")
    check1=request.POST.get('extract_emails',"off")
    check2=request.POST.get('extract_phone_no.',"off")
    check3 = request.POST.get('extract_urls.', "off")
    if check2=='on':
        phone_number=re.findall('[0-9]+',text)
        param={'res':phone_number}
        return render(request,'app1/analyze.html',param)
    elif check1=='on':
        emails=re.findall('\S+@\S+',text)
        param={'res':emails}
        return render(request,'app1/analyze.html',param)
    else:
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]| [! * \(\),] | (?: %[0-9a-fA-F][0-9a-fA-F]))+',text)
        print(url)
        param={'res':url}
        return render(request,'app1/analyze.html',param)

def web_scrape(request):
    s = "<button type='button'> <a href = 'http://127.0.0.1:8000/url_scraping'>Extract URLs from the link</a></button> <br> " \
        "<button type='button'> <a href = 'http://127.0.0.1:8000/download_pdf'>Download PDF from the URL</a></button>"
    return HttpResponse(s)
    # return render(request,"app1/web_scrape.html")

def download_pdf(request):
    urls = ['http://www.edudel.nic.in/welcome_folder/SupportMaterial2019_20/IX/English/9_sm_maths_eng_2019_20.pdf']
    for url in urls:
        name = url.split('/')[-1]
    print(name)
    myfile = requests.get(url, allow_redirects=True,stream=True)
    with open(name, 'wb')as pdf:
        for chunk in myfile.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)

    return HttpResponse("Your PDF is downloaded")

def url_scraping(request):
    # text=request.POST.get('text')
    # url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]| [! * \(\),] | (?: %[0-9a-fA-F][0-9a-fA-F]))+', text)
    # first_url=url[0]
    first_url="https://www.aldaily.com"
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
    return render(request, 'app1/url_scrape.html', param)

def emails_scraping(request):
    url='https://www.aldaily.com'
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
    param = {'res': emails}
    return render(request, 'app1/analyze.html', param)

def phoneNumber_scraping(request):
    url = 'https://www.aldaily.com'
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
    return render(request, 'app1/analyze.html', param)



