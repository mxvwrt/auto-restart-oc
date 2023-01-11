import os

try:
  import requests
except ImportError:
  print ("Trying to Install required module: requests")
  os.system('python -m pip install requests')
# -- above lines try to install requests module if not present
# -- if all went well, import required module again ( for global access)
import requests
import subprocess

data = "http://ip-api.com/json//?fields=isp"
response = requests.get(data)
jsonresp = response.json()
if response.json().get("isp"):
    isp = response.json().get("isp").lower()
    cty = response.json().get("city")
    cek = "pt" in isp or "pt." in isp and "indonesia" in cty.lower()
    if cek == False:
        os.system('/etc/init.d/openclash restart')
    else:
        print("Injek Berjalan")
