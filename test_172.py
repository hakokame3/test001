import re

a="The ghorst that says boo haunts the loo"
b=re.findall(".oo",a,re.IGNORECASE)
print(b)
