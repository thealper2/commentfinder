import requests
import argparse
import colorama
from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.parse import urlparse, urljoin
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def comment_finder(url="", file_name="", verbose=False):
	response = requests.get(url)
	html = response.content
	bs = BeautifulSoup(html, 'html.parser')

	with open(file_name, 'a') as file:
		comments = bs.find_all(string=lambda text: isinstance(text, Comment))
		for comment in comments:
			if verbose == True:
				print(f'[*] {Fore.GREEN}{url}{Fore.RESET} - {Fore.YELLOW}{comment}{Fore.RESET}')
			file.write(url + ' - ' + comment + '\n')

def recursive_comment_finder(url="", file_name="", verbose=False):
	response = requests.get(url)
	html = response.content
	bs = BeautifulSoup(html, 'html.parser')

	comment_finder(url=url, file_name=file_name)
	visited = []

	links = bs.find_all('a', href=True)
	for link in links:
		link_url = urljoin(url, link.get('href'))
		if urlparse(link_url).netloc == urlparse(url).netloc:
			if link_url not in visited:
				if verbose == False:
					comment_finder(url=link_url, file_name=file_name)
				else:
					comment_finder(url=link_url, file_name=file_name, verbose=True)
				visited.append(link_url)

argument_parser = argparse.ArgumentParser(description='')
argument_parser.add_argument('--url', required=True, type=str, help='')
argument_parser.add_argument('--out', required=True, type=str, help='')
argument_parser.add_argument('--recursive', required=False, action='store_true', help='')
argument_parser.add_argument('--verbose', required=False, action='store_true', help='')
arg = argument_parser.parse_args()

if(arg.url != None and arg.out != None and not arg.recursive and not arg.verbose):
	comment_finder(url=arg.url, file_name=arg.out)

elif(arg.url != None and arg.out != None and not arg.recursive and arg.verbose):
	comment_finder(url=arg.url, file_name=arg.out, verbose=True)

elif(arg.url != None and arg.out != None and arg.recursive and not arg.verbose):
	recursive_comment_finder(url=arg.url, file_name=arg.out)

elif(arg.url != None and arg.out != None and arg.recursive and arg.verbose):
	recursive_comment_finder(url=arg.url, file_name=arg.out, verbose=True)
