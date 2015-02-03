def read_url(filename):
	f = open(filename)
	name = f.open()	
	dict={}
	url_dict={}
	for line in name:
		m_val = re.search(r'"GET \S+', line)
		if m_val:
			url1 = match.group(1)
			url2 = match.group(2)
			if 'puzzle' in url1:
				dict['http://' + url2 + url1] = 1
	 url_dict=sorted(dict)
	 return sorted(url_dict)
