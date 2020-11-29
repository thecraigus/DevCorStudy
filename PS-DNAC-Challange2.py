import requests
import json

baseurl = "https://sandboxdnac2.cisco.com"
username = "devnetuser"
password = "Cisco123!"
headers = {'content-type': 'application/json'}

newdevice = {
    "computeDevice": True,
    "enablePassword": "string",
    "extendedDiscoveryInfo": "string",
    "httpPassword": "lolszzo",
    "httpPort": "string",
    "httpSecure": True,
    "httpUserName": "string",
    "ipAddress": "192.168.1.34",
    "merakiOrgId": "string",
    "netconfPort": "string",
    "password": "string",
    "serialNumber": "string",
    "snmpAuthPassphrase": "string",
    "snmpAuthProtocol": "string",
    "snmpMode": "string",
    "snmpPrivPassphrase": "string",
    "snmpPrivProtocol": "string",
    "snmpROCommunity": "string",
    "snmpRWCommunity": "string",
    "snmpRetry": 0,
    "snmpTimeout": 0,
    "snmpUserName": "string",
    "snmpVersion": "string",
    "type": "COMPUTE_DEVICE",
    "updateMgmtIPaddressList": [
        {
            "existMgmtIpAddress": "string",
            "newMgmtIpAddress": "string"
        }
    ],
    "userName": "string"
}

def gettoken(username, password):
    authreq = requests.post(baseurl+"/dna/system/api/v1/auth/token", auth=(username, password), headers=headers, verify=False)
    token = authreq.json()
    return token['Token']

def adddevices(token, newdevice):
    authheaders = {'x-auth-token': token, 'content-type':'application/json' }
    addreq = requests.post(baseurl+"/dna/intent/api/v1/network-device", headers=authheaders, verify=False, data=json.dumps(newdevice))
    print (addreq.status_code)

def main():
    token = (gettoken(username,password))
    adddevices(token, newdevice)

if __name__ == '__main__':
    main()