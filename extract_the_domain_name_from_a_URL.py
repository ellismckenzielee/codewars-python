#Extract the domain name from a URL kata
#https://www.codewars.com/kata/514a024011ea4fb54200004b

def domain_name(url):
    for itm in ['http://', 'www.', 'https://']:
        if itm in url:
            url = url.split(itm)[1]
    return url.split('.')[0]
    
    