# chmod 400 pem.pem ssh -i nwen406.pem ec2-user@
# sudo pip install requests-futures
# go get -u github.com/gorilla/mux
#  sudo yum install golang sudo yum install git 
import requests

from requests_futures.sessions import FuturesSession


apikeyhead = { 'x-api-key': "rZK9Xecrrl5iu7at8wmhB2krq8xyxhvM7rzOLb4i"}

rea = []
uturesSession = FuturesSession(max_workers=100)
fs = []
for i in range (100) :
    fs.append(uturesSession.get("https://trxe4leo0g.execute-api.us-west-1.amazonaws.com/prod/api1024?max=100&loops=1",headers = apikeyhead))

    
stcode =None     
for  i  in range  (100 )  :
    re  = fs[i].result()
    if re.status_code != 200 :
        print ( re.status_code)
        stcode = re.status_code
    else :
        rea.append (re.json())
        print ( re.status_code)
print (rea)


if stcode == 200 :
    print ("Challenge A is working and the API key is")

    print (apikeyhead)
else :
    
    print ("wrong API KEY")




import requests




for i in range (100) :
    r = requests.get('https://trxe4leo0g.execute-api.us-west-1.amazonaws.com/prod/api1024'+'?max='+str(1000000)+'&loops='+ str(1),headers = apikeyhead)
    print (r.json())

















