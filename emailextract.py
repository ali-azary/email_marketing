import requests
from urllib.parse import urlsplit
import re
from tqdm import tqdm

emails=set()
for i in tqdm(range(1,5)):
    

    url='https://www.luxyello.com/category/Architectural_services/'+str(i)
    r=requests.get(url)

    from bs4 import BeautifulSoup
    soup= BeautifulSoup(r.text,'html.parser')
    parts = urlsplit(url)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    if '/' in parts.path:
        path = url[:url.rfind('/')+1]
    else:
        path = url

    pages=set()
    for anchor in soup.find_all("a"): 
            
        # extract linked url from the anchor
        if "href" in anchor.attrs:
            href = anchor.attrs["href"]
            
            
            # resolve relative links (starting with /)
            if href.startswith('/company'):
                link = base_url + href
                
       
                pages.add(link)

    
    for url in list(pages):
        try:
            r=requests.get(url)
            soup= BeautifulSoup(r.text,'html.parser')
            for anchor in soup.find_all('div',{'class':'text weblinks'}): 
                website=anchor.a['href']
                r=requests.get(website)
                soup= BeautifulSoup(r.text,'html.parser')
                emails.update(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", soup.text))
        except:
            pass
f=open('emails.txt','w')
for email in emails:
    f.write(email+'\n')
f.close()
  

