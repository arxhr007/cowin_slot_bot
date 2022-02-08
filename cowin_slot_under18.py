import requests
from pytz import timezone 
from datetime import datetime

ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%d-%m-%Y')
x=requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=303&date="+ind_time)
dit=x.json()
dit=dit["sessions"]
z={}
sen=""
for i in dit:
    if i["min_age_limit"] < 18:
        sen+="\nname:"+i["name"]
        sen+="\naddress="+i["address"]
        sen+="\nblock="+i["block_name"]
        sen+="\nfee type="+i["fee_type"]
        sen+="\ntime:"
        for j in i["slots"]:
            sen+="\n"+j
        sen+="\n\n"
print(sen)
print("full details:\n\n")
sen2=""
for i in dit:
    if i["min_age_limit"] < 18:
        for j in i:
            sen2+="\n"+j+"="+str(i[j])
        sen2+="\n\n"
print(sen2)
