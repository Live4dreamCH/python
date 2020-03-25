from requests import post, get
my_url1 = "http://45.199.55.87/sop/youxiang.php"
my_headers1 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Host": "45.199.55.87",
    "Proxy-Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
response1 = get(my_url1, headers=my_headers1)
print(response1.status_code)
print(response1.headers)
print(response1.cookies)
isitamap = response1.headers
print(isitamap)
