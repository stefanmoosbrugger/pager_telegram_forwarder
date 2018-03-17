#!/bin/bash
result=`ps aux | grep -i "pager_telegram_forwarder.py" | grep -v "grep" | wc -l`
if [ $result -ge 1 ]
   then
        echo "script is running"
   else
        echo "start the script"
	dir=`dirname $0`
	nohup python $dir/pager_telegram_forwarder.py --freq='123.456M' --prot='POCSAG512 POCSAG1200' --min='25' --tID='322975229:BBEWq8JtAWY6QrogQJfqjePZwZTE_SWHSVk' --rID='-1001085080629'
 > /dev/null 2>&1 &
fi
