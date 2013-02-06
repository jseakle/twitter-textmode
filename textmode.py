#!/usr/bin/python
import twitter, codecs, datetime, re, keys
api = twitter.Api(consumer_key=keys.consumer_key, consumer_secret=keys.consumer_secret, access_token_key=keys.access_token_key, access_token_secret=keys.access_token_secret)

friends = api.GetFriends()
f = open("since", "r")
lines = f.readlines()
since = lines[-1][:-1]
f.close()
statuses = []
for u in friends:
    statuses += api.GetUserTimeline(None, u.id, u.screen_name, since, include_rts=True)

statuses += api.GetUserTimeline(None, None, None, since, include_rts=True)

out = codecs.open(keys.outfile, encoding="utf-8",  mode="a")

statuses.sort(key=lambda x: x.id)

d=datetime.datetime.now()
out.write(str(d) + "<br>")
for s in statuses:
    text = re.sub(r"(\w+://[\w.\-/#]+)", lambda x: "<a href="+x.group(0)+">"+x.group(0)+"</a>", s.text)
    out.write("<a href=http://twitter.com/"+s.user.screen_name+"/status/"+str(s.id)+">"+ s.user.name + "</a> ("+s.user.screen_name+"): " + text + "<br>") 


f = open("since", "w")


f.write(str(statuses[-1].id)+"\n")
f.close()
    
