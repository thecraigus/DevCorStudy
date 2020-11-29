import requests
import json

baseurl = "https://sandboxdnac2.cisco.com"
username = "devnetuser"
password = "Cisco123!"
headers = {'content-type': 'application/json'}

devid = "72dc1f0a-e4da-4ec3-a055-822416894dd5"

def gettoken(username, password):
    authreq = requests.post(baseurl+"/dna/system/api/v1/auth/token", auth=(username, password), headers=headers, verify=False)
    token = authreq.json()
    return token['Token']

def deldevice(token, devid):
    authheaders = {"x-auth-token": token, "content-type":"application/json" }
    delreq = requests.delete(baseurl+"{}/dna/intent/api/v1/network-device/{}".format(baseurl,devid), headers=authheaders, verify=False)
    print (delreq.status_code)

def main():
    token = (gettoken(username,password))
    deldevice(token, devid)

if __name__ == '__main__':
    main()