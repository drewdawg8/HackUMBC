import urllib

def test():
  link = "https://aba04c67.ngrok.io/text/alice.jpg"
  f = urllib.urlopen(link)
  myfile = f.read()
  print myfile

test()
