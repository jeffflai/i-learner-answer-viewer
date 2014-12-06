#!/usr/bin/env python
import webbrowser
import requests
import json
import sys
import os
os.remove("./output.html")
reload(sys)
sys.setdefaultencoding('UTF8')
f = open("output.html", "w")

aid = raw_input("aid: ")
seqid = raw_input("seqid: ")

args = '<xjxobj><e><k>articleid</k><v>' + aid + '</v></e><e><k>seqid</k><v>' +  seqid + '</v></e></xjxobj>'

headers = {'content-type': 'application/x-www-form-urlencoded'}

#payload = {'xjxargs[]' : '<xjxobj><e><k>articleid</k><v>1007</v></e><e><k>seqid</k><v>16</v></e></xjxobj>' , 'xjxfun' : 'check_answer_fillinblank' , 'xjxr' : '1417342789225' }
payload = {'xjxargs[]' : args , 'xjxfun' : 'check_answer_fillinblank' , 'xjxr' : '1417342789225' }

url = 'http://www.i-learner.com.hk/htmlexercise/exercise_mature_new.php?page=4&aid=1007&subpage=4&part=2'

r = requests.post(url, data=(payload), headers=headers)

a=(r.text)
print a
print >> f ,("<head><base href=http://www.i-learner.com.hk/htmlexercise/></head>")
print >>f, a
f.close()
webbrowser.open("./output.html",new=2)
