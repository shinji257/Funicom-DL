# -*- coding: utf-8 -*-
# -*- ver: 2.7 -*-
# -*- pro: x32 -*-

import time,sys,os,re
s_inTime = None
s_inUnit = None
f_inTime = None
RunSleep = True

s_inTime = sys.argv[1]
s_inUnit = (re.sub('[^A-Za-z]','',s_inTime)).lower()
try:
	f_inTime = float(re.sub('[^0-9\.]','',s_inTime))
	if (s_inUnit == '') or (s_inUnit == 'ms'):
		f_Time = float(f_inTime/1000.0)
	elif s_inUnit == 's':
		f_Time = float(f_inTime)
	elif s_inUnit == 'm':
		f_Time = float(f_inTime*60.0)
	elif (s_inUnit == 'h') or (s_inUnit == 'hr'):
		f_Time = float(f_inTime*3600.0)
	elif (s_inUnit == 'd') or (s_inUnit == 'days'):
		f_Time = float(f_inTime*86400.0)
	else:
		print 'Error: bad unit given'
		RunSleep = False
		os.system('pause')
	if RunSleep == True:
		time.sleep(f_Time)
except ValueError:
	print 'Error: no number given'
	os.system('pause')