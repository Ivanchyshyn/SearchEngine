import re
class WebLinks:
    
    def get_all_links(self, page):
        links = re.findall(r'<\s*a\s*href\s*=\s*"[\w./:]+"', page)
        return [link[link.find('"')+1:-1] for link in links]


"""
    def __init__(self):
        self.links = []
    def get_next_target(self, page):
        start_link = page.find('<a href=')
        if start_link == -1:
            return None, 0
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote+1:end_quote]
        return url, end_quote

    def get_all_links(self, page):
        while True:
            url, endpos = self.get_next_target(page)
            if url:
                self.links.append(url)
                page = page[endpos:]
            else:
                break
        return self.links
"""