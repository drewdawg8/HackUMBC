#! /usr/bin/python
#Easton E. 2011
#Geekness.eu

import sys
import urllib
import os.path
def main():
    if os.path.isdir(sys.argv[1]) == False:
            if os.path.isfile(sys.argv[1]):
                code = open(sys.argv[1], 'r').read()
            else:
                code = sys.argv[1]
            params = urllib.urlencode({'paste_code': code})
            url = urllib.urlopen("http://pastebin.com/api_public.php", params)
            return url.read()
            print url.read()
    else:
            print "no directories!"
            return "no directories!"

if __name__ == '__main__':
    status = main()
    sys.exit(status)

print main()
