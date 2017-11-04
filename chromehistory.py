import sqlite3
print(sqlite3.sqlite_version)
import os
import sys
import webbrowser as wb
# import urllib2

for path in (
        os.path.expanduser('~/.config/google-chrome/'),
        os.path.expanduser('~/.config/chromium/'),
        'C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\User Data\\' % os.environ.get('USERNAME'),
        'C:\\Documents and Settings\\%s\\Local Settings\\Application Data\\Google\\Chrome\\' % os.environ.get('USERNAME')
        ):
    path += os.path.join('Default', 'History')
    if os.path.exists(path):
        break
else:
    print('Chrome history file not found!')
    sys.exit()

print(path)
conn = sqlite3.connect(path)
#print(conn)
c = conn.cursor()
#print(c)

print("history length", c.execute('SELECT count(1) FROM urls').fetchone()[0])


while True:
    c.execute('select * from urls order by RANDOM() limit 1;')
    try:
        #conn.execute("PRAGMA busy_timeout = 30000")
        #c.execute("PRAGMA foreign_keys=ON")
 
        c.execute('select * from urls')
        url = c.fetchone()[1]
        print(url)
        
        # try:
        #     urllib2.urlopen(url).read()
        # except urllib2.URLError:
        #     pass
        # else:
        #     wb.open(url)
        #     break
    except Exception as e:
        print(e)
# pass