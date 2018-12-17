import sys
import re
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup,SoupStrainer

URLS = {
	'azlyrics.com/lyrics': ('<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->', '<!-- MxM banner -->', 4096),
	'azlyrics.com.az/lyrics': ('<!-- Azlyrics.com.az - Top Post -->\n</div>','<!-- WP QUADS Content Ad Plugin v. 1.8.1 -->', 1024)
}

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
		return None
	except:
		raise

if __name__ == '__main__':
	try:
		if len(sys.argv) < 2:
			print('Usage: '+ sys.argv[0]+' song title', file= sys.stderr)
		else:
			# get the first 7 links from DuckDuckGo
			res = urllib.request.urlopen('https://duckduckgo.com/html/?q='+'+'.join(sys.argv[1:])+'+lyrics azlyrics').read()
			soup = BeautifulSoup(res,'html.parser', parse_only=SoupStrainer('a',{'class': 'result__snippet'}))
			results = soup.find_all('a', limit=7)
			
			# retrieve the recontructed lyrics url if available.
			url_info = None
			for tag in results:
				parsed = urllib.parse.urlparse(tag['href'])
				temp = urllib.parse.parse_qs(parsed.query)['uddg'][0]
				match = re.search('azlyrics..*\/lyrics',temp)
				if match:
					url_info = temp, URLS[match.group()]
					break
			if url_info:
				lyrics = get_lyrics(url_info)
				if lyrics:
					print(lyrics); exit(0)
				exit(2)
			else:
				exit(1)
	except:
		raise
