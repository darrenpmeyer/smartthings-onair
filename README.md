# SmartThings Onair-light

A script and minimal implementation of the smartthings API allowing you to
toggle lights and switches on and off from the command line

Make sure that the `smartthings` directory is in your `PYTHONPATH`, and that
the `requests` module is installed for your Python

Get API credentials for SmartThings and put your access token in a file
somewhere convenient (like `~/smartthings_token.secret`). Don't forget to
`chmod 0600` that file to prevent others on the system from reading it!

```
python3 onair-smartthings.py --authfile=$HOME/smartthings_token.secret "On Air=on"
```

This will turn a light named "On Air" on, using the credentials stored in the
file `access_token.secret`. Changing the argument to `"On Air=off"` will turn
the light off.

If the `=on` or `=off` parts of the device name are omitted, will simply
print the status.