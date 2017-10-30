# chmod 400 pem.pem ssh -i nwen406.pem ec2-user@
# sudo pip install requests-futures
# go get -u github.com/gorilla/mux
#  sudo yum install golang sudo yum install git 
import requests

from requests_futures.sessions import FuturesSession

apikeyhead = { 'x-api-key': "wrongapikey"}
times = 10 
rea = []
uturesSession = FuturesSession(max_workers=100)
fs = []
stcode =None  
for i in range (times) :
    fs.append(uturesSession.get("https://trxe4leo0g.execute-api.us-west-1.amazonaws.com/prod/api1024?max=100&loops=1",headers = apikeyhead))

    
   
for  i  in range  (times )  :
    re  = fs[i].result()
    if re.status_code != 200 :
        #print ( re.status_code)
        stcode = re.status_code
    else :
        rea.append (re.json())
        stcode = re.status_code
        
print ("Concurrent 100 times :")        
print (rea)







import requests



nonConArray = [] 
for i in range (times) :
    r = requests.get('https://trxe4leo0g.execute-api.us-west-1.amazonaws.com/prod/api1024'+'?max='+str(1000000)+'&loops='+ str(1),headers = apikeyhead)
    nonConArray.append (r.json())
    #print (r.json())
    
print (" non Concurrent 100 times: ")         
print (nonConArray)



if stcode == 200 :
    print ("Challenge A is working and the API key is")

    print (apikeyhead)
else :
    
    print ("wrong API KEY")














