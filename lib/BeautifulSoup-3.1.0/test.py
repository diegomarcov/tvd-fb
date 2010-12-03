from BeautifulSoup import BeautifulSoup
a = "<a>foo" * 10000
soup = BeautifulSoup(a)
soup.findAll("a")
soup.findAll("a", recursive=False)
