from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = "http://e-psm.net:8091/report/route.php?idcard=VFVSRk5VNVVaekk9"
post_fields = {"hdnCmd":"OK","select":1,"period":"1/18/2020+-+10/18/2020","txtdep":22}     # Set POST fields here

request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)