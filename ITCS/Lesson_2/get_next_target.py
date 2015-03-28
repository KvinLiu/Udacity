def get_next_target (page) :
	start_link = page.find("<a href=")
	if start_link != -1:
		start_quote = page.find('"', start_link)
		end_quote = page.find('"', start_quote + 1)
		url = page[start_quote + 1:end_quote]
		return url, end_quote
	else:
		return None, 0	

url,endpos = get_next_target('This is a')

print url, endpos