# -*- coding: utf-8 -*-
# -*- ver: 2.7 -*-
# -*- pro: x32 -*-

import cookielib,os,re,sys,urllib,urllib2,fileinput,codecs
from ConfigParser import ConfigParser
from urlparse import urlparse
from collections import deque
try:
	from UserExcept import UserExceptions
	UserExcept_test = True
except:
	UserExcept_test = False
None
try:
	from PikaExcept import PikaExceptions
	PikaExcept_test = True
except:
	PikaExcept_test = False
None
def Exceptions(inAR,inAA,inAL,inSH,inTI,inSN,inEN,inNN,BSNTI):
	outAR = inAR
	outAA = inAA
	outAL = inAL
	outSH = inSH
	outTI = inTI
	outSN = inSN
	outEN = inEN
	outNN = inNN
	outARs = ''
	outAAs = ''
	outALs = ''
	outSHs = ''
	# global exceptions
	if PikaExcept_test == True:
		outAR,outAA,outAL,outSH,outTI,outSN,outEN,outNN,outARs,outAAs,outALs,outSHs = PikaExceptions(outAR,outAA,outAL,outSH,outTI,outSN,outEN,outNN,outARs,outAAs,outALs,outSHs,BSNTI)
	if UserExcept_test == True:
		outAR,outAA,outAL,outSH,outTI,outSN,outEN,outNN,outARs,outAAs,outALs,outSHs = UserExceptions(outAR,outAA,outAL,outSH,outTI,outSN,outEN,outNN,outARs,outAAs,outALs,outSHs,BSNTI)
	# ----------------------------------------------------------------------
	return outAR,outAA,outAL,outSH,outTI,outSN,outEN,outNN,outARs,outAAs,outALs,outSHs
def filedl(dlUrl,authToken,cmd_qq):
	if cmd_fs == False:
		ggg = dlUrl.split('/')[-1]
		ggg = ggg.replace('-480-','-'+cmd_qq+'-')
		dlUrl = dlUrl+'/'+ggg
		u = urllib2.urlopen(dlUrl+authToken)
		file_name = dlUrl.split('/')[-1]
		f = open(file_name, 'wb')
		meta = u.info()
		if cmd_dm == True:
			print str(meta)
		file_size = int(meta.getheaders("Content-Length")[0])
	else:
		u = urllib2.urlopen(dlUrl+authToken)
		file_name = dlUrl.split('/')[-1]
		f = open(file_name, 'wb')
		meta = u.info()
		if cmd_dm == True:
			print str(meta)
		file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)

	file_size_dl = 0
	block_sz = 8192
	while True:
		buffer = u.read(block_sz)
		if not buffer:
			break

		file_size_dl += len(buffer)
		f.write(buffer)
		status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		status = status + chr(8)*(len(status)+1)
		print status,

	f.close()
	return file_name
def updateque():
	fileHandle = open ( 'cur.que', 'r' )
	argqq = fileHandle.read()
	fileHandle.close()
	argqq = re.sub('\n','',argqq)
	argqq = re.sub('\"$','',argqq)
	argqq = re.sub('^\"','',argqq)
	os.system('findstr /C:\"'+argqq+'\" /B /E /V ..\\Funicom-DL.que>Funicom-DL.que.tmp')
	os.system('type Funicom-DL.que.tmp>..\\Funicom-DL.que')
	os.system('del Funicom-DL.que.tmp')
	sys.exit()
def login2(username,password):
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
	opener.addheaders =[('Referer', 'http://www.funimation.com/login'),
						('User-Agent','Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0'),
						('Content-Type','application/x-www-form-urlencoded')]

	url = 'http://www.funimation.com/login'
	data = { 'email_field' : username, 'password_field' : password}
	req = urllib2.Request(url, urllib.urlencode(data))
	res = opener.open(req)
	return
def login ():
	global cookie_jar
	fileHandle = open ( 'cookies.txt', 'w' )
	fileHandle.write('# Netscape HTTP Cookie File\n')
	fileHandle.close()
	cookie_jar = cookielib.MozillaCookieJar('cookies.txt')
	cookie_jar.load()
	login2(username,password)
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
	opener.addheaders =[('User-Agent','Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0'),
						('Connection','keep-alive')]
	url = 'http://www.funimation.com/profile'
	req = opener.open(url)
	site = req.read()

	if re.search(username2+'(?i)',site):
		print 'Login successful.'
		cookie_jar.save()

		for line in fileinput.input('cookies.txt',inplace =1):
			line = line.strip()
			if not 'c_visitor' in line:
				print line
	else:
		print 'Login failed.'
		sys.exit()
	return
def config ():
	config = ConfigParser()
	config.read('..\\Funicom-DL.ini')
	global username
	global username2
	global password
	global nameformat
	global pathformat
	global cmdlang
	global cmddef
	#username2 = config.get('Funicom-DL', 'username')
	#username = config.get('Funicom-DL', 'email')
	#password = config.get('Funicom-DL', 'password')
	nameformat = config.get('Funicom-DL', 'nameformat')
	pathformat = config.get('Funicom-DL', 'pathformat')
	#cmdlang = config.get('Funicom-DL', 'lang')
	#cmddef = config.get('Funicom-DL', 'def')
def error (url,err):
	try:
		fileHandle = open ( '..\\error.log', 'r' )
		errlog = fileHandle.read()
		fileHandle.close()
	except IOError:
		errlog = ''
	errlog = errlog+url+' - '+err+'\n'
	fileHandle = open ( '..\\error.log', 'w' )
	fileHandle.write(errlog)
	fileHandle.close()
def getHTML (url):
	urlparse(url)
	# try:
		# if sys.argv[2] == 'proxy':
			# opener = urllib2.build_opener(urllib2.ProxyHandler({"http" : "127.0.0.1:8118"}))
	# except IndexError:
	# if not username == '':
		# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
	# else:
	opener = urllib2.build_opener()
	opener.addheaders =[('Referer', 'http://funimation.com/'),('Host','www.funimation.com'),('Content-type','application/x-www-form-urlencoded'),('User-Agent','Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0)')]
	res = opener.open(url).read()
	return res
def cmdargsres ():
	exec("cmd_l = None") in globals()
	exec("cmd_q = \'best\'") in globals()
	exec("cmd_B = None") in globals()
	exec("cmd_fb = False") in globals()
	exec("cmd_io = False") in globals()
	exec("cmd_fq = False") in globals()
	exec("cmd_fl = False") in globals()
	exec("cmd_sa = False") in globals()
	exec("cmd_fs = False") in globals()
	exec("cmd_d = False") in globals()
	exec("cmd_du = False") in globals()
	exec("cmd_dl = False") in globals()
	exec("cmd_dw = False") in globals()
	exec("cmd_dd = False") in globals()
	exec("cmd_dm = False") in globals()
	exec("cmd_dc = False") in globals()
	exec("cmd_dp = False") in globals()
	exec("cmd_rl = False") in globals()
def cmdargs ():
	cmdargsres()
	argque = ''
	for arg in sys.argv:
		argque=argque+arg+'\n'
	argque = re.findall('(.+)\n',argque)
	argque = deque(argque)
	global page_url
	global percentzero
	percentzero = argque.popleft()
	page_url = argque.popleft()
	page_url_test = ''
	page_url_test = re.sub('http://(www\.)?funimation.com/shows/[^/]+/videos/(official|promotional)/[^/]+','yes',page_url)
	if page_url_test != 'yes':
		error(page_url,'Not a Funi Url')
		sys.exit()
	while argque != deque([]):
		arg = argque.popleft()
		arg = re.sub('^-','cmd_',arg)
		if arg == 'cmd_l':
			arg2 = argque.popleft()
			arg2 = re.sub('^sub$','jpn',arg2)
			arg2 = re.sub('^su$','jpn',arg2)
			arg2 = re.sub('^s$','jpn',arg2)
			arg2 = re.sub('^dub$','eng',arg2)
			arg2 = re.sub('^du$','eng',arg2)
			arg2 = re.sub('^d$','eng',arg2)
			arg2 = re.sub('^jp$','jpn',arg2)
			arg2 = re.sub('^j$','jpn',arg2)
			arg2 = re.sub('^en$','eng',arg2)
			arg2 = re.sub('^e$','eng',arg2)
			arg2_test = re.sub('eng|jpn','yes',arg2)
			if arg2_test != 'yes':
				error(page_url,'-l 2nd parameter missing or Not valid')
				sys.exit()
			exec(arg+" = \'"+arg2+"\'") in globals()
		elif arg == 'cmd_on':
			arg2 = argque.popleft()
			exec(arg+" = \'"+arg2+"\'") in globals()
		elif arg == 'cmd_od':
			arg2 = argque.popleft()
			exec(arg+" = \'"+arg2+"\'") in globals()
		elif arg == 'cmd_q':
			arg2 = argque.popleft()
			arg2 = re.sub('p','',arg2)
			arg2 = re.sub('1080p','1080',arg2)
			arg2 = re.sub('720p','720',arg2)
			arg2 = re.sub('480p','480',arg2)
			arg2 = re.sub('B','b',arg2)
			arg2 = re.sub('E','e',arg2)
			arg2 = re.sub('S','s',arg2)
			arg2 = re.sub('T','t',arg2)
			arg2 = re.sub('bes','best',arg2)
			arg2 = re.sub('be','best',arg2)
			arg2 = re.sub('b','best',arg2)
			arg2_test = re.sub('best|1080|720|480','yes',arg2)
			if arg2_test != 'yes':
				error(page_url,'-q 2nd parameter missing or Not valid')
				sys.exit()
			exec(arg+" = \'"+arg2+"\'") in globals()
		elif arg == 'cmd_B':
			arg2 = argque.popleft()
			arg2 = re.sub('K','k',arg2)
			arg2 = re.sub('k','',arg2)
			arg2_test = re.sub('\d\d\d\d?','yes',arg2)
			if arg2_test != 'yes':
				error(page_url,'-B 2nd parameter missing or Not valid')
				sys.exit()
			exec(arg+" = \'"+arg2+"\'") in globals()
		elif arg == 'cmd_d':
			exec("cmd_d = True") in globals()
			exec("cmd_du = True") in globals()
			exec("cmd_dl = True") in globals()
			exec("cmd_dw = True") in globals()
			exec("cmd_dd = True") in globals()
			exec("cmd_dm = True") in globals()
			exec("cmd_dc = True") in globals()
			exec("cmd_dp = True") in globals()
		else:
			exec(arg + " = True") in globals()
def uStr (aStr):
	if cmd_du == True:
		print aStr
	aStr = aStr.replace("\'","\\\'")
	aStr = aStr.replace('\"','\\\"')
	aStr = aStr.replace('\n','\\n')
	aStr = aStr.replace('\/','/')
	if cmd_du == True:
		print aStr
	exec("uStr = u\'"+aStr+"\'")
	return uStr
def prohtml ():
	os.system('title '+page_url.replace('http://www.funimation.com/',''))
	globals()
	if cmd_dl == True:
		print cmd_l
	html = getHTML(page_url)
	playersData = re.findall('.*var playersData = (.*);\n',html).pop()
	titleData = re.findall('meta property=\"og:title\" content=\"(.*)\">\n',html).pop()
	titleData = titleData.decode('utf-8')
	descData = re.findall('meta property=\"og:description\" content=\"(.*)\">\n',html).pop()
	descData = descData.decode('utf-8')
	playersData = re.sub('true','True',playersData)
	playersData = re.sub('false','False',playersData)
	playersData = re.sub('null','None',playersData)
	exec('lis_playersData = '+playersData)
	dic_playersData = lis_playersData.pop()
	lis_seasonData = dic_playersData['playlist']
	for iiii in lis_seasonData:
		try:
			lis_itemData = iiii['items']
			dic_seasonData = iiii
		except KeyError:
			x = None
	first = True
	for iii in lis_itemData:
		tmpA = iii
		if first == True:
			try:
				seasonStart = tmpA['number']
			except KeyError:
				try:
					seasonStart = tmpA['videoNumber']
				except KeyError:
					seasonStart = None
			first = False
		try:
			if tmpA['itemAK'] == dic_playersData['selectedItemAK']:
				dic_epiosdeDataCurrent = tmpA
		except KeyError:
			x = None
	if cmd_dd == True:
		print dic_epiosdeDataCurrent
	lis_videoSet = dic_epiosdeDataCurrent['videoSet']
	dic_dubSet = None
	dic_subSet = None
	for iii in lis_videoSet:
		tmpA = iii
		try:
			if tmpA['languageMode'] == 'dub':
				dic_dubSet = tmpA
				if cmd_fl == True:
					dic_subSet = tmpA
			elif tmpA['languageMode'] == 'sub':
				dic_subSet = tmpA
				if cmd_fl == True:
					dic_dubSet = tmpA
		except KeyError:
			x = None
	BADSeasonTitle = False
	if dic_seasonData['title'] == 'Movie':
		int_Snum = 0
	elif dic_seasonData['title'] == 'Extras':
		int_Snum = 0
	elif re.sub('(.+) \d+','\g<1>',dic_seasonData['title']) == 'Season':
		int_Snum = int(re.findall('\d+',dic_seasonData['title']).pop())
	else:
		int_Snum = 77
		BADSeasonTitle = dic_seasonData['title']
	tag_artist = dic_seasonData['artist']
	tag_albumartist = dic_epiosdeDataCurrent['artist']
	tag_album = dic_seasonData['artist']+', Season '+str(int_Snum)
	titleData = re.sub('^'+tag_artist+' - ','',titleData)
	tag_title = titleData
	tag_description = descData
	videoId = ''
	if cmd_dl == True:
		print cmd_l
	if cmd_l == 'eng':
		suby = ''
		if dic_dubSet != None:
			authToken = dic_dubSet['authToken']
			url_sdUrl = re.sub('-480-.*m3u8','-480-2000K.mp4',re.sub('/038C48/','/008C48/',dic_dubSet['sdUrl'].replace('\/','/')))
			url_hdUrl = re.sub('-480-.*m3u8','-480-3500K.mp4',re.sub('/038C48/','/008C48/',dic_dubSet['hdUrl'].replace('\/','/')))
			url_hd1080Url = re.sub('-480-.*m3u8','-480-4000K.mp4',re.sub('/038C48/','/008C48/',dic_dubSet['hd1080Url'].replace('\/','/')))
			str_FUNImationID = dic_dubSet['FUNImationID']
			videoId = dic_dubSet['videoId']
			if cmd_fl == True:
				str_FUNImationID = str_FUNImationID.replace('JPN','ENG')
			if url_sdUrl != '':
				if (re.findall('^....',url_sdUrl).pop()) != 'http':
					url_sdUrl = 'http://wpc.8c48.edgecastcdn.net/008C48/SV/480/'+str_FUNImationID+'/'+str_FUNImationID+'-480-2000K.mp4'
			if url_hdUrl != '':
				if (re.findall('^....',url_hdUrl).pop()) != 'http':
					url_hdUrl = 'http://wpc.8c48.edgecastcdn.net/008C48/SV/480/'+str_FUNImationID+'/'+str_FUNImationID+'-480-3500K.mp4'
			if url_hd1080Url != '':
				if (re.findall('^....',url_hd1080Url).pop()) != 'http':
					url_hd1080Url = 'http://wpc.8c48.edgecastcdn.net/008C48/SV/480/'+str_FUNImationID+'/'+str_FUNImationID+'-480-4000K.mp4'
			if cmd_fq == True:
				if url_sdUrl == '':
					url_sdUrl = 'http://wpc.8c48.edgecastcdn.net/008C48/SV/480/'+str_FUNImationID+'/'+str_FUNImationID+'-480-2000K.mp4'
				if url_hdUrl == '':
					url_hdUrl = 'http://wpc.8c48.edgecastcdn.net/008C48/SV/480/'+str_FUNImationID+'/'+str_FUNImationID+'-480-3500K.mp4'
				if url_hd1080Url == '':
					url_hd1080Url = 'http://wpc.8c48.edgecastcdn.net/008C48/SV/480/'+str_FUNImationID+'/'+str_FUNImationID+'-480-4000K.mp4'
			try:
				str_tmp_Nnum = dic_dubSet['number']
			except KeyError:
				str_tmp_Nnum = dic_dubSet['videoNumber']
			if str_tmp_Nnum == '':
				str_tmp_Nnum = '0.0'
			str_Nnum_dec = ('.'+re.sub('\d+\.(\d+)','\g<1>',str_tmp_Nnum))
			int_Nnum = int(re.sub('(\d+)\.\d+','\g<1>',str_tmp_Nnum))
		else:
			if cmd_fb == True:
				exec("cmd_l = \'jpn\'") in globals()
			else:
				error(page_url,'No dub')
				sys.exit()
	if cmd_l == 'jpn':
		suby = ' [SUB]'
		if dic_subSet != None:
			authToken = dic_subSet['authToken']
			url_sdUrl = re.sub('-480-.*m3u8','-480-2000K.mp4',re.sub('/038C48/','/008C48/',dic_subSet['sdUrl'].replace('\/','/')))
			url_hdUrl = re.sub('-480-.*m3u8','-480-3500K.mp4',re.sub('/038C48/','/008C48/',dic_subSet['hdUrl'].replace('\/','/')))
			url_hd1080Url = re.sub('-480-.*m3u8','-480-4000K.mp4',re.sub('/038C48/','/008C48/',dic_subSet['hd1080Url'].replace('\/','/')))
			str_FUNImationID = dic_subSet['FUNImationID']
			videoId = dic_subSet['videoId']
			if cmd_fl == True:
				str_FUNImationID = str_FUNImationID.replace('ENG','JPN')
			if url_sdUrl != '':
				if (re.findall('^....',url_sdUrl).pop()) != 'http':
					url_sdUrl = 'http://wpc.8c48.edgecastcdn.net/008C48/SV/480/'+str_FUNImationID+'/'+str_FUNImationID+'-480-2000K.mp4'
			if url_hdUrl != '':
				if (re.findall('^....',url_hdUrl).pop()) != 'http':
					url_hdUrl = 'http://wpc.8c48.edgecastcdn.net/008C48/SV/480/'+str_FUNImationID+'/'+str_FUNImationID+'-480-3500K.mp4'
			if url_hd1080Url != '':
				if (re.findall('^....',url_hd1080Url).pop()) != 'http':
					url_hd1080Url = 'http://wpc.8c48.edgecastcdn.net/008C48/SV/480/'+str_FUNImationID+'/'+str_FUNImationID+'-480-4000K.mp4'
			if cmd_fq == True:
				if url_sdUrl == '':
					url_sdUrl = 'http://wpc.8c48.edgecastcdn.net/008C48/SV/480/'+str_FUNImationID+'/'+str_FUNImationID+'-480-2000K.mp4'
				if url_hdUrl == '':
					url_hdUrl = 'http://wpc.8c48.edgecastcdn.net/008C48/SV/480/'+str_FUNImationID+'/'+str_FUNImationID+'-480-3500K.mp4'
				if url_hd1080Url == '':
					url_hd1080Url = 'http://wpc.8c48.edgecastcdn.net/008C48/SV/480/'+str_FUNImationID+'/'+str_FUNImationID+'-480-4000K.mp4'
			try:
				str_tmp_Nnum = dic_subSet['number']
			except KeyError:
				str_tmp_Nnum = dic_subSet['videoNumber']
			if str_tmp_Nnum == '':
				str_tmp_Nnum = '0.0'
			str_Nnum_dec = ('.'+re.sub('\d+\.(\d+)','\g<1>',str_tmp_Nnum))
			int_Nnum = int(re.sub('(\d+)\.\d+','\g<1>',str_tmp_Nnum))
		else:
			error(page_url,'No sub')
			sys.exit()
	if seasonStart == None:
		seasonStart = str(int_Nnum)
	int_seasonStart = int(seasonStart.replace('.0',''))
	int_Enum = int_Nnum-int_seasonStart
	int_Enum = int_Enum+1
	defy = ''
	highy = ''
	if cmd_q == 'best':
		if url_hd1080Url != '':
			dlUrl = url_hd1080Url
			defy = '1080p'
			highy = ' [HIGH]'
			cmd_qq = '1080'
		elif url_hdUrl != '':
			dlUrl = url_hdUrl
			defy = 'HD'
			cmd_qq = '720'
		elif url_sdUrl != '':
			dlUrl = url_sdUrl
			defy = 'SD'
			cmd_qq = '480'
		else:
			error(page_url,'No SD')
			sys.exit()
	if cmd_q == '1080':
		if url_hd1080Url != '':
			dlUrl = url_hd1080Url
			defy = '1080p'
			highy = ' [HIGH]'
			cmd_qq = '1080'
		else:
			error(page_url,'No 1080p')
			sys.exit()
	if cmd_q == '720':
		if url_hdUrl != '':
			dlUrl = url_hdUrl
			defy = 'HD'
			cmd_qq = '720'
		else:
			error(page_url,'No 720p')
			sys.exit()
	if cmd_q == '480':
		if url_sdUrl != '':
			dlUrl = url_sdUrl
			defy = 'SD'
			cmd_qq = '480'
		else:
			error(page_url,'No SD')
			sys.exit()
	if cmd_B != None:
		dlUrl = re.sub('\d\d00K',cmd_B+'K',dlUrl)
	tag_artist = uStr(tag_artist)
	tag_albumartist = uStr(tag_albumartist)
	tag_album = uStr(tag_album)
	# tag_title = uStr(tag_title)
	# tag_description = uStr(tag_description)
	tag_tvshow = tag_albumartist
	tag_artist,tag_albumartist,tag_album,tag_tvshow,tag_title,int_Snum,int_Enum,int_Nnum,tag_artistsort,tag_albumartistsort,tag_albumsort,tag_tvshowsort = Exceptions(tag_artist,tag_albumartist,tag_album,tag_tvshow,tag_title,int_Snum,int_Enum,int_Nnum,BADSeasonTitle)
	tag_Enum = "{0:0>2}".format(int_Enum)
	tag_Nnum = "{0:0>4}".format(int_Nnum)
	tag_Snum = "{0:0>2}".format(int_Snum)
	tag_Dnum = str_Nnum_dec
	if tag_Dnum == '.0':
		tag_Dnum = ''
	rEn = str(int_Enum)
	rNn = str(int_Nnum)
	rSn = str(int_Snum)
	En = tag_Enum
	Nn = tag_Nnum
	Sn = tag_Snum
	Dn = tag_Dnum
	Dn_ = re.sub('\.','_',Dn)
	show = re.sub('[^\.a-zA-Z0-9 ]','_',tag_tvshow)
	show32 = re.sub('^(...............................[^ ]).*','\g<1>',show)
	show16 = re.sub('^(...............[^ ]).*','\g<1>',show)
	title = re.sub('[^\.a-zA-Z0-9 ]','_',tag_title)
	title32 = re.sub('^(...............................[^ ]).*','\g<1>',title)
	title16 = re.sub('^(...............[^ ]).*','\g<1>',title)
	album = re.sub('[^\.a-zA-Z0-9 ]','_',tag_album)
	album32 = re.sub('^(...............................[^ ]).*','\g<1>',album)
	album16 = re.sub('^(...............[^ ]).*','\g<1>',album)
	albumartist = re.sub('[^\.a-zA-Z0-9 ]','_',tag_albumartist)
	albumartist32 = re.sub('^(...............................[^ ]).*','\g<1>',albumartist)
	albumartist16 = re.sub('^(...............[^ ]).*','\g<1>',albumartist)
	artist = re.sub('[^\.a-zA-Z0-9 ]','_',tag_artist)
	artist32 =  re.sub('^(...............................[^ ]).*','\g<1>',artist)
	artist16 = re.sub('^(...............[^ ]).*','\g<1>',artist)
	exec("outFilename = " + nameformat)
	exec("outpath = " + pathformat)
	fileHandle = open ( str(int_Enum)+Dn_+'.funi.info', 'w' )
	fileHandle.write(codecs.BOM_UTF8)
	fileHandle.write((tag_title+';;; '+tag_description).encode('utf-8'))
	fileHandle.close()
	fileHandle = open ('artist.info', 'w' )
	fileHandle.write(codecs.BOM_UTF8)
	fileHandle.write(tag_artist.encode('utf-8'))
	fileHandle.close()
	fileHandle = open ('albumartist.info', 'w' )
	fileHandle.write(codecs.BOM_UTF8)
	fileHandle.write(tag_albumartist.encode('utf-8'))
	fileHandle.close()
	fileHandle = open ('album.info', 'w' )
	fileHandle.write(codecs.BOM_UTF8)
	fileHandle.write(tag_album.encode('utf-8'))
	fileHandle.close()
	fileHandle = open ('tvshow.info', 'w' )
	fileHandle.write(codecs.BOM_UTF8)
	fileHandle.write(tag_tvshow.encode('utf-8'))
	fileHandle.close()
	if tag_artistsort != '':
		fileHandle = open ('artistsort.info', 'w' )
		fileHandle.write(codecs.BOM_UTF8)
		fileHandle.write(tag_artistsort.encode('utf-8'))
		fileHandle.close()
	if tag_albumartistsort != '':
		fileHandle = open ('albumartistsort.info', 'w' )
		fileHandle.write(codecs.BOM_UTF8)
		fileHandle.write(tag_albumartistsort.encode('utf-8'))
		fileHandle.close()
	if tag_albumsort != '':
		fileHandle = open ('albumsort.info', 'w' )
		fileHandle.write(codecs.BOM_UTF8)
		fileHandle.write(tag_albumsort.encode('utf-8'))
		fileHandle.close()
	if tag_tvshowsort != '':
		fileHandle = open ('tvshowsort.info', 'w' )
		fileHandle.write(codecs.BOM_UTF8)
		fileHandle.write(tag_tvshowsort.encode('utf-8'))
		fileHandle.close()
	cmd = 'if not exist \"'+outpath+'\" MD \"'+outpath+'\"'
	os.system(cmd)
	cmd = 'move \"'+str(int_Enum)+Dn_+'.funi.info\" \"'+outpath+str(int_Enum)+Dn_+'.funi.info\"'
	os.system(cmd)
	cmd = 'move \"artist.info\" \"'+outpath+'artist.info\"'
	os.system(cmd)
	cmd = 'move \"albumartist.info\" \"'+outpath+'albumartist.info\"'
	os.system(cmd)
	cmd = 'move \"album.info\" \"'+outpath+'album.info\"'
	os.system(cmd)
	cmd = 'move \"tvshow.info\" \"'+outpath+'tvshow.info\"'
	os.system(cmd)
	cmd = 'if exist \"artistsort.info\" move \"artistsort.info\" \"'+outpath+'artistsort.info\"'
	os.system(cmd)
	cmd = 'if exist \"albumartistsort.info\" move \"albumartistsort.info\" \"'+outpath+'albumartistsort.info\"'
	os.system(cmd)
	cmd = 'if exist \"albumsort.info\" move \"albumsort.info\" \"'+outpath+'albumsort.info\"'
	os.system(cmd)
	cmd = 'if exist \"tvshowsort.info\" move \"tvshowsort.info\" \"'+outpath+'tvshowsort.info\"'
	os.system(cmd)
	if cmd_dc == False:
		os.system('cls')
	if cmd_dw == True:
		print dlUrl
	if cmd_io == True:
		updateque()
	if cmd_fq == True:
		try:
			file_name = filedl(dlUrl,authToken,cmd_qq)
		except urllib2.HTTPError:
			try:
				dlUrl = url_hdUrl
				highy = ''
				defy = 'HD'
				exec("outFilename = " + nameformat)
				file_name = filedl(dlUrl,authToken,cmd_qq)
			except urllib2.HTTPError:
				try:
					highy = ''
					defy = 'SD'
					exec("outFilename = " + nameformat)
					dlUrl = url_sdUrl
					file_name = filedl(dlUrl,authToken,cmd_qq)
				except urllib2.HTTPError:
					error(page_url,'fail to force quality')
					sys.exit()
	else:
		file_name = filedl(dlUrl,authToken,cmd_qq)
	s = 0
	# if cmd_rl == True:
	# 	if defy == '1080p':
	# 		os.system('rl.bat \"'+file_name+'\"')
	cmd = 'move \"'+file_name+'\" \"'+outpath+outFilename+'.mp4\"'
	os.system(cmd)
	if cmd_dc == False:
		os.system('cls')
	if cmd_dp == True:
		os.system('pause')
#----------
print 'Booting up...'

config()
#if not username == '':
#	login()
cmdargs()
prohtml()
updateque()
#----------
