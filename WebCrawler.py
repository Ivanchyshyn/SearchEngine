from WebLinks import WebLinks
from WebIndex import WebIndex
from WebRank import WebRank
class WebCrawler:
    def get_page(self, page):
        try:
            import requests
            return requests.get(page).text
            #import urllib.request as url
            #return url.urlopen(page).read()
        except:
            print('Unsuccessfull')
            return ""

    def crawl_web(self, seed, max_depth):
        tocrawl = [seed]
        crawled = []
        next_depth = []
        depth = 0
        Index = WebIndex()
        graph = {}
        while tocrawl and depth <= max_depth:
            page = tocrawl.pop()
            if page not in crawled:
                content = self.get_page(page)
                Index.add_page_to_index(content, page)
                outlinks = WebLinks().get_all_links(content)
                next_depth += outlinks
                graph[page] = outlinks
                crawled.append(page)
            if not tocrawl:
                 tocrawl, next_depth = next_depth, []
                 depth += 1
        return Index, graph

crawler = WebCrawler()
Index, graph = crawler.crawl_web('https://udacity.github.io/cs101x/urank/', 3)
ranks = WebRank.compute_ranks(graph, 1)
print(Index.ordered_search(ranks, 'Hummus'))