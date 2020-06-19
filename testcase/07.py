import os
result = os.popen("ping 192.168.0.126:801")
r = result.read()
print(r)
print(result.read())
if "100%" in r:
    print(123)