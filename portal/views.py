from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from .forms import Ticket_Form


def home(request):
	if request.user.is_authenticated:
		return render(request, 'portal/home.html')
	else:
		return HttpResponseRedirect('/accounts/login')


def issue_search(request):
	if request.method == 'POST':
		query = request.POST['user_query'].replace(" ", "-")
		url = 'https://support.workspaceone.com/search/' + query + '?contentType=kb-articles&sort=relevance&language=en&page=1'
		print('URL: ', end='')
		print(url)
		
		"""
		Parsing live website
		"""
		options = Options()
		options.headless = True
		driver = webdriver.Chrome(options=options)
		driver.get(url)
		time.sleep(5)
		page_source = driver.page_source
		
		page_source2 = page_source.split('resourceItems listView"><div>')
		page_source3 = page_source2[1].split('showing results')
		page_source4 = BeautifulSoup(page_source3[0], 'html.parser')
		"""
		Parsing fields into respective lists
		"""
		a_elements = page_source4.find_all("div", class_='resourceTitle')
		a_elements2 = page_source4.find_all("div", class_='resourceLabel')

		i=0
		articles = {}
		for a_element in a_elements:
			articles[i] = { 'title': a_element.text, 'url': a_element.a['href'] }
			#articles_dictionary[i]['title'] = a_element.text
			#articles_dictionary[i]['link'] = a_element.a['href']
			i+=1

		article_lastupdate_temp = [a_element.text for a_element in a_elements2]
		to_be_removed = {'ShareShare this linkCopy to Clipboardcopied to clipboard', '  Knowledge Base Article', 'topic: Product Announcements'}
		article_lastupdate = [item for item in article_lastupdate_temp if item not in to_be_removed ]
		print('article_lastupdate: ', end='')
		print(article_lastupdate)
		i=0
		for article in articles:
			articles[i]['update'] = article_lastupdate[i]
			i+=1

		#article_title = [a_element.text for a_element in a_elements]
		#article_links = [a_element.a['href'] for a_element in a_elements]
		
		#article_lastupdate_temp = [a_element.text for a_element in a_elements2]
		#to_be_removed = {'ShareShare this linkCopy to Clipboardcopied to clipboard', '  Knowledge Base Article', 'topic: Product Announcements'}
		#article_lastupdate = [item for item in article_lastupdate_temp if item not in to_be_removed ]

		#print('Articles: ', end='')
		#print(article_title)
		#print('URLs: ', end='')
		#print(article_links)
		#print('Last Updated: ', end='')
		#print(article_lastupdate)

		"""
		Parsing variables into context
		"""
		ticket_form = Ticket_Form()
		context = {
			'user_query': request.POST['user_query'],
			'articles' : articles,
			'ticket_form' : ticket_form,
		}
		print('Articles: ', end='')
		print(articles)
		
		return render(request, 'portal/search.html', context=context)






# https://kb.vmware.com/s/global-search/%40uri#q=Intelligent%20Hub%20Release%20Notes&f:@commonproduct=[Workspace%20ONE%20UEM]&f:@commonlanguage=[English]

#print(request.POST)
#if request.method == 'POST':
#f.close()
#