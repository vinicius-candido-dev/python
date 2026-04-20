import urllib
import urllib.request
import urllib.error
try: #https://pudim.com.br/
    site = urllib.request.urlopen('https://www.youtube.com/watch?v=8jAykqxIeqw&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=51')
    print('O site youtube está acessivel')
except: #urllib.error.URLError:
    print('O site youtube não está acessivel')
