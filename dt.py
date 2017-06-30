from datetime import datetime, timedelta
now= datetime.now()
print (datetime.now())
print now.year
print now
print now.month
print now.day
print now.hour
print now.minute
print now.second

print"1 week ago was it:",now - timedelta(weeks=1)
print"100 days was it:",now - timedelta(days=100)
print"1 week from now is it:", now+timedelta(weeks=1)
print"in 1000 days from now is it ", now+timedelta(days=1000)


# # using strft function..../
# from datetime import datetime
# import time
# now= datetime.now()
# now=now.strftime("%b %d %y")
# print(now)