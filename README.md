# pi2open

a pishock to openshock api translation layer

## usage

on integrations that allow you to change the pishock url, simply change it to localhost

in other cases, you'll need to use setup your system to redirect requests from do.pishock.com to localhost
on linux, this can be achieved by adding `127.0.0.1 do.pishock.com` to your /etc/hosts file

once you've done that, make sure to provide both the shocker id and api key for openshock via either an environment variable like so
```
OPENSHOCK_TOKEN=your-token-here
OPENSHOCK_SHOCKER=your-device-id-here
```
or by editing to variables in main.py of the same names

good luck, have fun! :3
