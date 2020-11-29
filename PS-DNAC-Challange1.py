import requests
import json

baseurl = "https://sandboxdnac2.cisco.com"
username = "devnetuser"
password = "Cisco123!"
headers = {'content-type': 'application/json'}



def gettoken(username, password):
    authreq = requests.post(baseurl+"/dna/system/api/v1/auth/token", auth=(username, password), headers=headers, verify=False)
    token = authreq.json()
    return token['Token']

def getdevices(token):
    devicelist = {}
    authheaders = {'x-auth-token': token, 'content-type':'application/json' }
    devreq = requests.get(baseurl+"/dna/intent/api/v1/network-device", headers=authheaders, verify=False).text
    devices = json.loads(devreq)
    for device in devices['response']:
        hostname = device['hostname']
        ipaddr = device['managementIpAddress']
        devicelist[hostname] = [ipaddr]
    return (devicelist)

def main():
    token = (gettoken(username,password))
    for device, ipaddr in getdevices(token).items():
        print (device, ipaddr[0])

if __name__ == '__main__':
    main()
