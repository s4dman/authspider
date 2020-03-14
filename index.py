import mechanize
from bs4 import BeautifulSoup


def to_scrape():
    
    browser = mechanize.Browser()
    
    # Ignore robots.txt.  Do not do this without thought and consideration
    browser.set_handle_robots(False)
    
    # Pass a browser agent to show that the request is coming form a browser
    browser.addheaders = [
        ('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0)Gecko/20100101 Firefox/18.0 (compatible;)'),
        ('Accept', '*/*')]
    
    # Browsing the home page
    browser.open("http://quotes.toscrape.com/")
    
    # Finding the login link
    for login_link in browser.links(url_regex="/login"):
        browser.open("http://quotes.toscrape.com" + login_link.url)
        # Authorization Starts
        browser.select_form(nr=0)  # Selecting the login form
        browser.form['username'] = 'King'  # Setting username for the input field
        browser.form['password'] = 'password'  # Setting password for the input field
        browser.submit()
        print (browser.geturl())  # On submit getting the redirected URL

        html = browser.open(browser.geturl())
        
        # If logged in, there should have a logout link available
        for logout_link in browser.links(url_regex="/logout"):
            print ("http://quotes.toscrape.com" + logout_link.url)

        soup = BeautifulSoup(html, "html.parser")  # Converting webpage to BeautifulSoup object
        for parent_div in soup.findAll('div', {'class': 'quote'}):
            quote = parent_div.span.text
            author = parent_div.small.text
            print (quote + "\n - by: " + author)


to_scrape()
