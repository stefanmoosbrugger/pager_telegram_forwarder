#!/bin/bash
result=`ps aux | grep -i "pager_telegram_forwarder.py" | grep -v "grep" | wc -l`
if [ $result -ge 1 ]
   then
        echo "script is running"
   else
        echo "start the script"
	nohup python ./pager_telegram_forwarder.py --freq='100.15M' --prot='POCSAG512 POCSAG1200' --min='25' --tID='123456789:JKASDHLJASGDjhsagdjhagASasfdA' --rID='-1001004000133'
 > /dev/null 2>&1 &
fi
