# Script for decoding pager messages and forwarding them as Telegram message 
Small python script that decodes pager messages (AFSK, FSK, HAPN, ZVEI, POCSAG, FLEX, and many more) and forwards them to Telegram. The script uses rtl-sdr and multimon-ng (https://github.com/EliasOenal/multimon-ng) to receive and decode the messages and pytgbot (https://github.com/luckydonald/pytgbot) to forward the messages to Telegram (e.g., a Telegram channel)

## Hardware Requirements:
* rtl-sdr compatible device, see http://sdr.osmocom.org/trac/wiki/rtl-sdr#SupportedHardware (e.g., Realtek RTL2832U)
* RaspberryPi (optional)

## Software Requirements:
* Python
* rtl-sdr
* multimon-ng
* pytgbot

For detailed instructions of how to setup a RaspberryPi for pager message decoding see https://www.raspberrypi.org/forums/viewtopic.php?t=45142

## Start the script
Once the prerequisites are met the script can be started 
```
python pager_telegram_forwarder.py --freq="<freq>" --prot="<protocols>" --min="<minimum message length>" --tID"<Telegram API ID>" --rID="<Telegram recipient ID>"
```
Example call to listen at `100.12MHz` for `POCSAG 512/1200/2400` messages with minimum length of 25 characters
and sending them to the telegram recipient with the ID `-1001004000133` (the used Telegram ID and recipient ID is fictitious. So don't use it.): 
```
python pager_telegram_forwarder.py --freq="100.15M" --prot="POCSAG512 POCSAG1200" --min="25" --tID="123456789:JKASDHLJASGDjhsagdjhagASasfdA" --rID="-1001004000133"
```

## Script autostart
For convenience only. If you want the script to be started automatically you can use the provided shell script
and add it to the crontab. It checks if the forwarder script is already active. If not it will be started. This is useful because the script crashes sometimes. 
