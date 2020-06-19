import os
result = os.popen("ping github.com")
r = result.read()
print(r)
print(result.read())
if "100%" in r:
    print(123)