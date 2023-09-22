# urbackup-telegraf
Quick script to log Urbackup statuses with Telegraf/Influxdb

Requires Urbackup API `pip3 install urbackup-server-web-api-wrapper` and PyTelegraf `pip3 install pytelegraf`. You do not need Keyring but it feels more neat to use over just jamming in raw passwords all willy nilly. 

Script can be modified to grab additional elements from Urbackup, you can run `print(client)` to obtain all available elements. Simply add a new metric for your new element. You can also get more server-related info with `server.get_usage()` by modifying the script as so: 

```
usage = server.get_usage()
for device in usage:
  tgClient.metric('Urbackup Usage', device['used'], tags={'Endpoint': device['name']})
```

Run this script on the same host as Telegraf (I am using Docker personally), ensure you have the relevant ports listening. Script can be run with Cron on a regular basis `crontab -e`. 
