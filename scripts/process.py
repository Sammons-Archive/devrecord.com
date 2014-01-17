#By Ben Sammons
#first python script ever
#haven't really learned python
#whatever
#let's go

import os, fileinput, sys, codecs
assert os.path.abspath
assert os.path.basename 
assert os.path.exists
assert os.walk



from BeautifulSoup import BeautifulSoup
Mode_compile 		= 1
Mode_update_sitemap = 2
Mode_extract_content= 1
Mode = 1
if (len(sys.argv) > 1):
	if (sys.argv[1] == "compile"):
		pass
	if (sys.argv[1] == "sitemap"):
		Mode = 2

parent_directory 	= os.path.abspath("..")
content_directory 	= os.path.abspath("../scripts")

site_map = '<?xml version="1.0" encoding="UTF-8"?>\n'+ \
	  '<urlset\n'+ \
      'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'+ \
      'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n'+ \
      'xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9\n'+ \
            'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n' + \
            '<url><loc>http://devrecord.com/</loc><url>'
def addToSitemap(filepath):
	#print filepath
	global site_map
	site_map += '<url>\n'
	site_map += '\t<loc>\thttp://devrecord.com'+filepath[filepath.rfind('/'):]+'/</loc>\n'
	site_map += '</url>\n'

def processContent(entry):
	#create page
	page= codecs.open('base.html','r','utf-8').read()
	page=	page.replace('{{title}}',entry.title.text)
	page=	page.replace('{{content}}',entry.content.prettify())
	page=   page.replace('{{previous}}',entry.previous_page.text)
	page=   page.replace('{{number}}',entry.number.text)
	page=   page.replace('{{arrow_quip}}',entry.arrow_quip.text)
	page=   page.replace('{{image_quip}}',entry.image_quip.text)
	page=   page.replace('{{title_quip}}',entry.title_quip.text)
	#make dir
	if (not os.path.exists(parent_directory+'/'+entry.number.text)):
		os.mkdir(parent_directory+'/'+entry.number.text)
	#write to dir
	if (os.path.isfile(parent_directory+'/'+entry.number.text+'/index.html')):
		os.remove(parent_directory+'/'+entry.number.text+'/index.html')
	new_file = codecs.open(parent_directory+'/'+entry.number.text+'/index.html',"w+",'utf-8')
	new_file.write(page)

ignore_list = [
	"scripts",
	"content"
]

content = open(content_directory+"/pages.xml").read()
soup = BeautifulSoup(content)
for entry in soup.findAll('entry'):
	processContent(entry)



for thing in os.listdir(parent_directory):
	path = parent_directory+'/'+thing
	if (os.path.isdir(path) and thing.find('.')==-1 and thing not in ignore_list):
		addToSitemap(path)
site_map_file = open(parent_directory+"/sitemap.xml", "w+")
site_map_file.write(site_map);
site_map_file.close()

"""
{
	title:
	number:
	previous:
	directory:
	content:
	arrow_quip:
	title_quip:
	image_quip:
}
"""




