import re
class WebLinks:
    @staticmethod
    def regular_ex():
        a_link = r'<\s*a\s*href\s*=\s*"[\w./:]+"'
        return a_link

    @staticmethod
    def get_all_links(page):
        links = re.findall(WebLinks.regular_ex(), page)
        return [link[link.find('"')+1:-1] for link in links]
