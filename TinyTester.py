""" this program tests shortend urls for actual content behind them.
it also saves the content url to a file """
import string
import random
import datetime
import urllib
import sys
import getopt


def generatePath(length=7, charset=string.ascii_letters + string.digits):
	""" generate paths part of urls to check """
	return ''.join(random.choice(charset) for _ in range(length))

def generateTimestring():
	""" return formatted time """
	return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def testOneUrl(host='http://bit.ly/', path='1234567'):
	""" test a single URL+path """
	try:
		url = urllib.urlopen(host+path)
		if url.geturl() != (host+path):
			return url.geturl()
		else:
			return host + path + ' found nothing'
	except Exception as e:
		return host + path + ' error'


def logSingleResponse(entry='placeholder'):
	""" appends a single entry to a log """
	with open('log', 'a') as logfile:
		logfile.write(generateTimestring() + ' ' + entry + '\n')

def handleArguements(argv):
	""" handles commandline arguments """
	try:
		opts, args = getopt.getopt(argv, )
	except getopt.GetoptError:
		print('tinytester.py -u <URL>')
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('-u', '--url'):
			return arg
		elif opt in ('-h', '--help'):
			print('Use -u <URL> to specify URL')
			sys.exit()

def main(argv):
	""" starting """
	#handleArguements(argv)
	for counter in range(100):
		tested = testOneUrl('http://tinyurl.com/', generatePath(6,))
		if ' ' not in tested:
			logSingleResponse(tested)
		print(str(counter) + ' done')


if __name__ == '__main__':
	main(sys.argv[1:])
