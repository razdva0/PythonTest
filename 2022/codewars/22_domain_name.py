def domain_name(url):
    url = url.replace('http://', '')
    url = url.replace('https://', '')
    url = url.replace('www.', '')
    return url.split('.')[0]


if domain_name("http://google.com") == "google":
    print('OK')
else:
    print(domain_name("http://google.com"))
if domain_name("http://google.co.jp") == "google":
    print('OK')
else:
    print(domain_name("http://google.com"))
if domain_name("www.xakep.ru") == "xakep":
    print('OK')
else:
    print(domain_name("http://google.com"))
if domain_name("https://youtube.com") == "youtube":
    print('OK')
else:
    print(domain_name("http://google.com"))
