import mechanize
from bs4 import BeautifulSoup


def to_scrape():
    br = mechanize.Browser()
    # Ignore robots.txt.  Do not do this without thought and consideration
    br.set_handle_robots(False)
    # Pass a browser agent to show that the request is coming form a browser
    br.addheaders = [
        ('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0)Gecko/20100101 Firefox/18.0 (compatible;)'),
        ('Accept', '*/*')]
    # Browsing the home
    br.open("http://quotes.toscrape.com/")
    # Finding the login link
    for login_link in br.links(url_regex="/login"):
        br.open("http://quotes.toscrape.com" + login_link.url)
        # Authorization Starts
        br.select_form(nr=0)  # Selecting the login form
        br.form['username'] = 'King'  # Setting username for the input field
        br.form['password'] = 'password'  # Setting password for the input field
        br.submit()
        print (br.geturl())  # On submit getting the redirected URL

        html = br.open(br.geturl())
        # If logged in, there should have a logout link available
        for logout_link in br.links(url_regex="/logout"):
            print ("http://quotes.toscrape.com" + logout_link.url)

        soup = BeautifulSoup(html, "html.parser")  # Converting to BeautifulSoup object
        for parent_div in soup.findAll('div', {'class': 'quote'}):
            quote = parent_div.span.text
            author = parent_div.small.text
            print (quote + "\n - by: " + author)


to_scrape()
