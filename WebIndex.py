import re
class WebIndex:
    """
    Indexing pages in form keyword - URLs
    """
    def __init__(self):
        self.index = {}
    def add_to_index(self, keyword, url):
        if not keyword:
            return
        if keyword in self.index:
            if url not in self.index[keyword]:
                self.index[keyword].append(url)
        else:
            self.index[keyword] = [url]

    def add_page_to_index(self, html, url):
        #remove tags
        start = html.find('<')
        while start != -1:
            end = html.find('>', start+1)
            html = html[:start] + " " + html[end+1:]
            start = html.find('<')
        
        for word in html.split():
            self.add_to_index(word.lower(), url)

    #Looking for the URLs where element was found
    def lookup(self, keyword):
        return self.index.get(keyword)

    def ordered_search(self, ranks, keyword):
        urls = self.lookup(keyword.lower())
        if urls:
            sort_ranks = sorted(ranks, key=lambda x:ranks[x], reverse=True)
            result = []
            for url in sort_ranks:
                if url in urls:
                    result.append(url)
            return result

#web_index = WebIndex()
#web_index.add_page_to_index('udacity$ is the best.', 'http://udacity.com')
#web_index.add_page_to_index('abc are', 'http://abc.com')
#web_index.add_page_to_index('udacity', 'http://xxx.com')
#print(web_index.index)
#print(web_index.lookup('udacity'))