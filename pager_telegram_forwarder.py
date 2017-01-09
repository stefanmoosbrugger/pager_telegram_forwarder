#!/usr/bin/python

import sys, getopt
import subprocess
import collections
from time import gmtime, strftime
from pytgbot import Bot

def start_multimon(freq, prot, minlen, tid, rid):
        # replace POCSAG512 with -a POCSAG512
        prot = prot.replace(" ", " -a ")
	# create telegram bot
	bot = Bot(tid)
        # create deque
        d = collections.deque(maxlen=100)
	# call multimon
        call = "rtl_fm -d0 -f "+freq+" -s 22050 | multimon-ng -t raw -a "+prot+" -f alpha -t raw /dev/stdin -"
        print call
	mm = subprocess.Popen(
		call,
		shell=True, 
		stdout=subprocess.PIPE)
	while mm.poll() is None:
		# process new pocsag entry 
    		output = mm.stdout.readline() # read new line
		print output
                if "Alpha" not in output: # check if non alpha element
		    continue # if yes, continue
                output = output.replace("<NUL>", "") # replace terminator sequence
                if output in d: # if the message is already in the list -> skip (pager messages might be sent multiple times)
                    continue
                d.append(output) # add to deque
		msg = output.split("Alpha:",1)[1] # get the message
		if int(len(msg))<int(minlen): # if msg length < minlen skip
			continue;
		time = strftime("%Y-%m-%d %H:%M", gmtime()) # get timestamp
		print msg # print the message
		try:
		    bot.send_message(rid, 'Time: '+time+'\nMessage: '+msg) # send it.
		except :
		    pass

def main(argv):
	print "Pager telegram forwarder"
        freq = "" #f
        protocols = "" #p
        min_len = "" #m
        tel_ID = ""  #t
        rec_ID = "" #r
        usage = 'pager_telegram_forwarder.py --freq="<freq>" --prot="<protocols>" --min="<minimum message length>" --tID="<Telegram API ID>" --rID="<Telegram recipient ID>"' 
        if len(argv) != 5:
            print "#args = " + len(argv)
            print usage
            sys.exit(2)
        try:
            opts, args = getopt.getopt(argv,"hf:p:m:t:r",["freq=","prot=","min=","tID=","rID="])
        except getopt.GetoptError, exc:
            print exc.msg
            print usage
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print usage
                sys.exit()
            elif opt in ("--freq"):
                freq = arg
            elif opt in ("--prot"):
                protocols = arg
            elif opt in ("--min"):
                min_len = arg
            elif opt in ("--tID"):
                tel_ID = arg
            elif opt in ("--rID"):
                rec_ID = arg
        print 'Freq ', freq
        print 'Protocols ', protocols
        print 'Minimum length ', min_len
        print 'Telegram ID ', tel_ID
        print 'Receiver ID ', rec_ID
	# start multimon
	start_multimon(freq, protocols, min_len, tel_ID, rec_ID)	

if __name__ == "__main__":
        main(sys.argv[1:])
