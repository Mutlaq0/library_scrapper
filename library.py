'''
Imports that You need in order to do the task
'''
# to install packages : 
# pip install selenium
# pip install beautifulsoup4
from bs4 import BeautifulSoup #helps you find elements in webpage in order to scrape/crawl it.. read more about web scrapping/crawling
import os
from selenium import webdriver # a package that helps you navigate the web as a web driver, I use chrome(in the code), not a big deal
import time
# helper method(others may call it function) that gets the 'href'
# which is a link in a html element and returns the link, we will use it in the other helper method.
def get_link(element):
    link = element['href']
    return link
# helper method that takes 'soup', we'll discuss it later,
# and finds all 'a' elements in html web page that contain '[1]' text written in them.
# then, uses the above method to extract all the book's links from the 'a' elements,
# these links we'll use later to download the books.
def get_page_links(soup):
    a_list = soup.find_all("a", string="[1]")
    links = list(map(get_link,a_list))
    return links

# the url we are going to begin scrapping
url = 'https://libgen.is/search.php?req=%D8%A7%D9%84%D8%BA%D8%B2%D8%A7%D9%84%D9%8A&open=0&res=25&view=simple&phrase=1&column=def'
#specifying the name of the web driver that we are using,
#-- the name of the file of the driver, the driver is downloaded I'll show you how later -- 
chromrdriver = "chromedriver"
os.environ["webdriver.chrome.driver"] = chromrdriver
# setting up the selenium.webdriver to use chrome driver
driver = webdriver.Chrome(chromrdriver)
# now the driver is running, when the compilation is here, 
# you should see that a new google chrome session has opened.
# getting the url means that the driver requests the url that we specefied above.
driver.get(url)
# starting a beautifulSoup session using the driver, setting it up as follows:
soup = BeautifulSoup(driver.page_source, 'lxml')
# empty list, I'll use to keep track of the book's links in
links = []
# while loop will execute until a condition is met, and then break the loop(stopping it) is possible
while True:
    # get the page's links using above method, and add all links in the page to the links list.
    links.extend(get_page_links(soup))
    try:
        # try is a feature in programming, that you simply tell the IDE/Compiler to try do the code inside the try clause.
        # in this example we are trying to execute the line that comes before 'except'.
        # in this try: and the line of code, we basically are trying to find an element that contains
        # certain text, and then click it, so we go from current page to the last page for every search.
        # the purpose of try is to try and execute the code inside the try and check if there's an error, so we can then ignore it.
        driver.find_element_by_xpath("//a[contains( text( ), '►')]").click()
    # we are looking for an element in the html that contains '►' text inside it, 
    # but there is one case that if we look for it, the driver will not find the element, 
    # and that's because obviously it is not there!,and therefore the code will be inturrupted
    # and the code will not continue to execute, the solution is to try and find it, if there's an error/ also called exception
    # do the following: (in the except clause)
    except:
        # except clause is what is used to tell the IDE/Compiler/Code editor what to do in 
        # case of exception, in this code, the exception will be an element that contains '►'
        # not found and we are trying to click it, which means that we're trying to click something that doesn't exist.
        break
    # time.sleep is for waiting in seconds, after each page it waits two seconds and then go to the next
    # not necessary but to be sure that it had enough time to do whatever whatever whatever whatever
    time.sleep(2)
# previously we saved links inside a list, which is a datastructure( we use various datastructures to save data in a way that we desire)    
links = set(links) # set is a datastructures, the good thing in it that it doesn't save duplicate elements,
# simply one of every single element, it can be two elements with the same value in it.
for l in links:   # looping on the links to do the following 
    driver.get(l) # changing the page to the book's page in the driver
    driver.find_element_by_xpath("//a[contains( text( ), 'GET')]").click() # finding element that contains 'GET' in it and click it
    time.sleep(5) # sleep for 5 secs because I can and I love it.