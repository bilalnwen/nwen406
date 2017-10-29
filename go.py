# chmod 400 pem.pem ssh -i nwen406.pem ec2-user@
# sudo pip install requests-futures
# go get -u github.com/gorilla/mux
#  sudo yum install golang sudo yum install git 
import requests

from requests_futures.sessions import FuturesSession


apikeyhead = { 'x-api-key': ""}

rea = []
uturesSession = FuturesSession(max_workers=100)
fs = []
for i in range (100) :
    fs.append(uturesSession.get("?max=100&loops=1",headers = apikeyhead))
    #print () 
for  i  in range  (100 )  :
    re  = fs[i].result()
    if re.status_code != 200 :
        print ( re.status_code)
    else :
        rea.append (re.json())
print (rea)








import requests




for i in range (100) :
    r = requests.get('?max='+str(1000000)+'&loops='+ str(1))
    print (r.json())

















