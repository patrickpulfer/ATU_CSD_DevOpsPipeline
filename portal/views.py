from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .forms import Ticket_Form, Ticket_History_Form
from .models import *
import time, re
from .classes.diagnostics import WS1_Diagnostics_Module


def home(request):
	if request.user.is_authenticated:
		return render(request, 'portal/home.html')
	else:
		return HttpResponseRedirect('/accounts/login')


def ticket(request, param_ticket):
	if not request.user.is_authenticated:
		return HttpResponseRedirect('/accounts/login')
	else:
		if request.method == 'GET':
			tickets = Ticket.objects.filter(id=param_ticket)
			ticket_history = Ticket_History.objects.filter(ticket=param_ticket)
			ticket_history_form = Ticket_History_Form(instance=request.user)
			ticket_context = {'tickets': tickets, 'ticket_history': ticket_history, 'ticket_history_form': ticket_history_form}
		if request.method == 'POST':
			tickets = get_object_or_404(Ticket, id=param_ticket)
			ticket_history_form = Ticket_History_Form(request.POST)
			if ticket_history_form.is_valid():
				print(tickets)
				obj = ticket_history_form.save(commit=False)
				obj.user = request.user
				obj.ticket = tickets
				obj.save()
				tickets = Ticket.objects.filter(id=param_ticket)
				ticket_instance = get_object_or_404(Ticket, id=param_ticket)
				ticket_instance.status=obj.action
				ticket_instance.save()
				ticket_history = Ticket_History.objects.filter(ticket=param_ticket)
				ticket_context = {'tickets': tickets, 'ticket_history': ticket_history, 'ticket_history_form': ticket_history_form}
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

			diagnostics = WS1_Diagnostics_Module()
			diagnostics_report = Diagnostics_Report()
			diagnostics_report.ticket = get_object_or_404(Ticket, id=ticket_id)
			diagnostics_report.app_catalog = diagnostics.app_catalog_status
			diagnostics_report.awcm_status = diagnostics.awcm_status
			diagnostics_report.cn_status = diagnostics.console_status
			diagnostics_report.ds_status = diagnostics.devices_status
			diagnostics_report.awcm_link = diagnostics.url_awcm_statistics
			diagnostics_report.enrollment_url = diagnostics.discover['EnrollmentUrl']
			diagnostics_report.enrollment_group = diagnostics.discover['GroupId']
			diagnostics_report.service_status_indicator = diagnostics.service_status['status']['indicator']
			diagnostics_report.service_status_description = diagnostics.service_status['status']['description']
			diagnostics_report.save()
	return HttpResponseRedirect('/ticket/%s' % obj.id)



def issue_search(request):
	if request.method == 'POST':
		query = request.POST['user_query'].replace(" ", "-").replace("'", "")
		
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
