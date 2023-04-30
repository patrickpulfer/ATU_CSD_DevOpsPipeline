from bs4 import BeautifulSoup
import requests

# HTML From File
with open("output.txt", "r") as f:
	doc = BeautifulSoup(f, "html.parser")


# tags = doc.find_all("div", "resourceTitle")

a_elements = doc.find_all("div", class_='resourceTitle')
article_title = [a_element.text for a_element in a_elements]
article_links = [a_element.a['href'] for a_element in a_elements]


a_elements2 = doc.find_all("div", class_='resourceLabel')
article_lastupdate = [a_element.text for a_element in a_elements2]

# article_link = links.find("a")
# article_title

to_be_removed = {'ShareShare this linkCopy to Clipboardcopied to clipboard', '  Knowledge Base Article'}
article_lastupdate2 = [item for item in article_lastupdate if item not in to_be_removed ]


print(article_lastupdate2)

# HTML From Website
#url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

#result = requests.get(url)
#doc = BeautifulSoup(result.text, "html.parser")

#prices = doc.find_all(text="$")
#parent = prices[0].parent
#strong = parent.find("strong")
#print(strong.string)