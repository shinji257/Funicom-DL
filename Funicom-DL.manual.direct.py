import os,re,sys,urllib,urllib2,fileinput,codecs
from ConfigParser import ConfigParser
from urlparse import urlparse
from collections import deque
from random import randint
import time

def config ():
	config = ConfigParser()
	config.read('..\\Funicom-DL.ini')
	global outdir
	outdir = config.get('Funicom-DL-Manual', 'outdir')


def filedl(dlUrl,authToken,cmd_qq,o_pth,o_fn):
	file_size1 = 0
	file_size2 = 0
	tmpA_o_pth = '\"'+o_pth+'\"'
	tmpB_o_pth = ''
	firstrun = True
	while True:
		if tmpA_o_pth == '':
			break;
		else:
			if firstrun == False:
				tmpB_o_pth = tmpB_o_pth+'\n               '
			else:
				firstrun = False
			tmpB_o_pth = tmpB_o_pth+tmpA_o_pth[:64]
			tmpA_o_pth = tmpA_o_pth[64:]
	o_pth = tmpB_o_pth
	tmpA_o_fn = '\"'+o_fn+'\"'
	tmpB_o_fn = ''
	firstrun = True
	while True:
		if tmpA_o_fn == '':
			break;
		else:
			if firstrun == False:
				tmpB_o_fn = tmpB_o_fn+'\n               '
			else:
				firstrun = False
			tmpB_o_fn = tmpB_o_fn+tmpA_o_fn[:64]
			tmpA_o_fn = tmpA_o_fn[64:]
	o_fn = tmpB_o_fn
	y = 0-1
	x = str(int(time.time()))
	check = False
	trynum = ''
	ggg = dlUrl.split('/')[-1]
	ggg = ggg.replace('-480-','-'+cmd_qq+'-')
	print 'Downloading File: \n    Time     = '+x+'\n    Name     = '+ggg+'\n    Out Path = '+o_pth+'\n    Out Name = '+o_fn+'\n =============================================================================='
	while True:
		if check == False:
			y = y+1
			if y > 0:
				trynum = '.try_'+str(y)
				print 'Try '+str(y)+':'
			dlUrl2 = dlUrl+'/'+ggg+'.time_'+x+trynum+'.mp4'
		else:
			dlUrl2 = dlUrl+'/'+ggg+'.time_'+x+trynum+'.checked.mp4'
		u = urllib2.urlopen(dlUrl2+authToken)
		file_name = dlUrl2.split('/')[-1]
		f = open(file_name, 'wb')
		meta = u.info()
		file_size2 = file_size1
		file_size1 = int(meta.getheaders("Content-Length")[0])
		if str(file_size1) == 0:
			break;
		elif file_size1 == file_size2:
			if check == True:
				print '            '+str(file_size1)+' == '+str(file_size2)+' Bytes'
				break
			else:
				u.close()
				print '    '+str(file_size1)+' == '+str(file_size2)+' Bytes'
				check = True
				print '        Double Checking:'
		else:
			check = False
			u.close()
			if y > 0:
				print '    '+str(file_size1)+' != '+str(file_size2)+' Bytes'
		if (y > 0) and (check != True):
			time.sleep(30)
		if check == True:
			time.sleep(2)
	file_size = file_size1
	print "Downloading: %s\n    Bytes: %s" % (file_name, file_size)

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
config()
os.system('title Funicom-DL Manual Mode')
response = urllib2.urlopen('http://www.funimation.com/shows/heroic-age/videos/official/age/anime')
html = response.read()
auth = re.findall('\"authToken\":\"([^\"]+)\"',html).pop()


url = sys.argv[1]

url = 'http://wpc.8c48.edgecastcdn.net/008C48/SV/480/'+re.sub('(.+)-(.+)-(.+)','\g<1>',url)+'/'+re.sub('(.+)-(.+)-(.+)','\g<1>-480-\g<3>',url)+'.mp4/'+url+'.mp4'

ofn = url.split('/')[-1]

qq = re.sub('.+-(.+)-.+','\g<1>',ofn)

iurl = re.sub('/'+ofn+'$','',url)

filer = filedl(iurl,auth,qq,'\\',ofn)
outdir1 = outdir
otudir1 = re.sub('\\$','',outdir1)
if outdir1 == '':
	outdir2 = '..'
elif re.sub('^[A-Za-z]:.*$','yes',outdir1) == 'yes':
	outdir2 = outdir1
	os.system('if not exist \"'+outdir2+'\" mkdir \"'+outdir2+'\"')
else:
	outdir2 = '..\\'+outdir1
	os.system('if not exist \"'+outdir2+'\" mkdir \"'+outdir2+'\"')


os.system('move '+filer+' \"'+outdir2+'\\'+ofn+'\"')
fileHandle = open ( '..\\Funicom-DL.manual.direct.py.que', 'r' )
quein = fileHandle.read()
fileHandle.close()
quein = quein+'\n'
queout = re.sub(str(sys.argv[1])+'\n','',quein)
queout = re.sub('\n\n','\n',queout)

fileHandle = open ( '..\\Funicom-DL.manual.direct.py.que', 'w' )
fileHandle.write(queout)
fileHandle.close()