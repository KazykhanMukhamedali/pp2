import datetime

# # 1
# data = datetime.datetime.now()-datetime.timedelta(days=5)
# print(data)

# # #2
data = datetime.datetime.now()
yes = datetime.datetime.now() - datetime.timedelta(days=1)
tod = datetime.datetime.now()
tom = datetime.datetime.now() + datetime.timedelta(days=1)
print(yes,tod,tom)

# #3
now = datetime.datetime.now() 
print(now.strftime("%"))

# #4
# dat= datetime.datetime.now()
# print(dat*84600)
