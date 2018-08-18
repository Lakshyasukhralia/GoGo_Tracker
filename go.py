import bs4 as bs
import urllib.request
import re
import urllib.request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

user_email = ["xxxxxxxxxx@email.com","xxxxxxxxx@email.com"]

def SetMail(body,toaddr):

    fromaddr = "uuuuuuuuuuuu@email.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Your daily Episode is up online!"
    body = "Dear user,\n" + "Enjoy streaming of "+body+"\n\nRegards,\nTeam SxC "
    msg.attach(MIMEText(body, 'plain'))
    SendMail(fromaddr, toaddr, msg)

def SendMail(fromaddr, toaddr, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("uussrr_nnaammee", "ppaass")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)


user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = "https://gogoanime.sh/"
headers={'User-Agent':user_agent,}

request=urllib.request.Request(url,None,headers)
response = urllib.request.urlopen(request)
data = response.read()
soup = bs.BeautifulSoup(data,'lxml')


Latest = {}

for div in soup.find('div', class_='last_episodes loaddub').find_all('li'):

    for name in div.find_all('p', class_='name'):
        title = name.text
        links = name.findAll('a')
        for i in links:
            link = "https://gogoanime.sh"+i.get('href')
    for episode in div.find_all('p', class_='episode'):
        episode_num = episode.text


    Latest[title]= [episode_num,link]


for i,j in Latest.items():
    z = re.match("(G\w+)",i)
    msg = i
    for k in j:
        msg = msg +" " + k

    if z:
        localtime = time.asctime( time.localtime(time.time()) )
        print("Found |",i,"| at ",localtime)
        for i in user_email:
            SetMail(msg,i)
