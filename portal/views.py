from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from .forms import Ticket_Form
from .models import *


def home(request):
	if request.user.is_authenticated:
		return render(request, 'portal/home.html')
	else:
		return HttpResponseRedirect('/accounts/login')


def ticket(request, param_ticket):
	ticket = get_object_or_404(Ticket, id=param_ticket)
	ticket2 = Ticket.objects.filter(id=param_ticket)
	ticket3 = ticket.created_at
	print('ticket: ', end='')
	print(ticket)
	print('ticket2: ', end='')
	print(ticket2)
	print('ticket3: ', end='')
	print(ticket3)
	ticket_context = {}
	ticket_context = {'ticket': ticket2, }
	return render(request, 'portal/ticket.html', context=ticket_context)


def dashboard(request):
	if request.user.is_authenticated:
		tickets = Ticket.objects.all()
		dashboard_context = {'tickets': tickets}
		return render(request, 'portal/dashboard.html', context=dashboard_context)
	else:
		return HttpResponseRedirect('/accounts/login')


def create_ticket(request):
	if request.method == 'POST' and request.user.is_authenticated:
		ticket_form = Ticket_Form(request.POST)
		if ticket_form.is_valid():
			obj = ticket_form.save(commit=False)
			obj.user = request.user
			obj.agent_id = 1
			obj.status = 'open'
			obj.save()
			ticket_id = obj.id
		print('done!')
	return HttpResponseRedirect('/ticket/%s' % obj.id)



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
			i+=1

		article_lastupdate_temp = [a_element.text for a_element in a_elements2]
		to_be_removed = {'ShareShare this linkCopy to Clipboardcopied to clipboard', '  Knowledge Base Article', 'topic: Product Announcements'}
		article_lastupdate = [item for item in article_lastupdate_temp if item not in to_be_removed ]
		i=0
		for article in articles:
			articles[i]['update'] = article_lastupdate[i]
			i+=1
		"""
		Parsing variables into context
		"""
		ticket_form = Ticket_Form()
		context = {
			'user_query': request.POST['user_query'],
			'articles' : articles,
			'ticket_form' : ticket_form,
		}
		#print('Articles: ', end='')
		#print(articles)
		
		return render(request, 'portal/search.html', context=context)
