import re
def remove_url_anchor(url):
    '''Remove the anchor from a URL'''
    return re.sub(r'[#]\w*$','', url)
