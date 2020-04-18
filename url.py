import urllib.request;
import urllib.parse;

try: 
  with urllib.request.urlopen("http://www.networksciencelab.com") as doc:
    html = doc.read()
    print(html)
except:
  print("Could not open %s" % doc, file=sys.err)

URL = "http://networksciencelab.com/index.html;param?fo=bar#content"
print(urllib.parse.urlparse(URL))