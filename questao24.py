from datetime import datetime

id1 = datetime.strptime('2001-05-18', '%Y-%m-%d')

id2 = datetime.strptime('2022-08-23', '%Y-%m-%d')

total = abs((id2 - id1).days)
print (total) 