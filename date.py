# ex 1
from datetime import datetime, timedelta
x = datetime.now() - timedelta(days=5)
print(x)

# ex 2
from datetime import datetime, timedelta
today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today", today.strftime("%Y-%m-%d"))
print("Tomorrow", tomorrow.strftime("%Y-%m-%d"))

# ex 3
from datetime import datetime, timedelta
x = datetime.now()
print(x.strftime("%Y %m %d %H %M %S"))

# ex 4
from datetime import datetime
date = datetime(2024, 2, 7, 12, 0, 0)
date2= datetime(2024, 2, 6, 12, 0, 0)
diff = date - date2
diff = diff.total_seconds()
print(diff)

