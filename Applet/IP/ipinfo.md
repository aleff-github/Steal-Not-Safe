# Lib
OS commands with output
`import subprocess`

# Function
```
def ip_info():
    output = subprocess.check_output("curl ipinfo.io", shell=True)
    return str(output)
```

# Where
Change your email text with something like it
```
text = "\
    Email sent automatically, access from your PC has been detected!\n\nIP Info:\n" + ip_info()
```
