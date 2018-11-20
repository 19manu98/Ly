import sys
import re
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup,SoupStrainer
import logging

FORMAT = '%(asctime)-15s %(message)s'
formatter = logging.Formatter(FORMAT)

lookup = {
	'azlyrics.com/lyrics': ('<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->', '<!-- MxM banner -->', 4096),
	'azlyrics.com.az/lyrics': ('<!-- Azlyrics.com.az - Top Post -->\n</div>','<!-- WP QUADS Content Ad Plugin v. 1.8.1 -->', 1024)
}

def set_logger(name, log_file ):

	handler = logging.FileHandler(log_file)
	handler.setFormatter(formatter)

	logger = logging.getLogger(name)
	logger.setLevel('INFO')
	logger.addHandler(handler)

	return logger


def get_lyrics(url_info):
	try:
		url, info = url_info
		response = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(response, 'html.parser')
		l = str(soup)
		# Moves away arbitrary bytes as lyrics start far down the page.
		start = l.find(info[0],info[2], len(l))
		end = l.find(info[1], start+len(info[0]))

		if start > 0 and end > 0:
			lyrics = '\n' + re.sub('(\|\sAZ\w.*)|(AZ\w.*\|\s?)', '',soup.title.string) + '\n' + l[start + len(info[0]):end]
			return BeautifulSoup(lyrics, 'html.parser').get_text()
		return 'No results found.'
	except:
		raise

def writeGood(name,logger):
    logger.info("this is the song: %s",name)

def writeBad(name,logger):
	logger.info("these are the links:")
	i=0
	for e in name:
		i = i+1
		logger.info("%d: %s"%(i,e))

if __name__ == '__main__':
	try:
		if len(sys.argv) < 2:
			print('Usage: '+ sys.argv[0]+' song title', file= sys.stderr)
		else:
			# get the first 7 links from DuckDuckGo search engine.
			res = urllib.request.urlopen('https://duckduckgo.com/html/?q='+'+'.join(sys.argv[1:])+'+lyrics azlyrics').read()
			soup = BeautifulSoup(res,'html.parser', parse_only=SoupStrainer('a',{'class': 'result__snippet'}))
			results = soup.find_all('a', limit=7)

			# get the recontructed 'https://www.azlyrics.com*' url if available.
			url_info = None
			for tag in results:
				parsed = urllib.parse.urlparse(tag['href'])
				temp = urllib.parse.parse_qs(parsed.query)['uddg'][0]
				match = re.search('azlyrics..*\/lyrics',temp)
				if match:
						url_info = temp, lookup[match.group()]

						break

			if url_info:
				print(get_lyrics(url_info))
				loggerG = set_logger('fistLogger','FileSearch.log')
				writeGood(sys.argv[1:],loggerG)
			else:
				print('Sorry, No fast results found!\n', file=sys.stderr)
				loggerB =set_logger('secondLogger','Error.log')
				writeBad(results,loggerB)
	except:
	        raise
