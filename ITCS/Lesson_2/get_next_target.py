def get_next_target (page) :
	start_link = page.find("<a href=")
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1:end_quote]
	return url, end_quote

url,endpos = get_next_target('This is a <a href="http://udacity.com">link!</a>')

print url