import re
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup as soup

active = True
url = 'https://www.amazon.com/charts/2018-01-07/mostsold/fiction'

out_file = 'Amazon Book Data.csv'
f = open(out_file,'w+')
headers = 'Title\tAuthor\tStar Rating\tReview Count\tWeeks on List\n'
f.write(headers)
# While loop that gets all the book data then goes to the next page
while active:

    raw_html = urlopen(url).read()
    parser = "html.parser"
    s = soup(raw_html, parser)

    books = []
    for i in range(1,21):
        book = s.find('div', {'id':f'rank{i}'})
        books.append(book)

    # Getting all the data from the books
    for b in books:
        title = b.find('div', {'class':'kc-rank-card-title'})
        title = title.text
        title = title.strip()
        print("Title: ", title)

        author = b.find('div', {'class': 'kc-rank-card-author'})
        author = author['title']
        print("Author: ", author)
        
        rating = b.find('div', {'class': 'numeric-star-data'}).small.text
        try:
            star_rating = re.findall(r'\d\.\d',rating)[0]
        except:
            star_rating = 'N/A'
        print('Rating: ', star_rating)
        try:
            review_count = re.findall(r'\d*\,\d*', rating)[0]
        except:
            review_count = 'N/A'
        print('Number of Reviews: ', review_count)

        try:
            weeks_on_list = b.find('div', {'class': 'kc-wol'}).text
            weeks_on_list = re.findall(r'\d*',weeks_on_list)[0]
        except:
            weeks_on_list = b.find('div', {'class': 'kc-wol-first'}).text
            weeks_on_list = '1'
        print("Weeks on List: ", weeks_on_list)
        f.write(f'{title}\t{author}\t{star_rating}\t{review_count}\t{weeks_on_list}\n')

    # Grabbing the link for the next section
    link = s.find('a',{'class','kc-title-nav-link next'})
    link = link['href']
    next_link = re.findall(r"\d{4}-\d{2}-\d{2}",link)

    # An empty string so that I can add the list item from next_link to it
    # I can also use it later to check for a stopping
    # When I use a while loop to grab other links
    using_link = ""
    for i in next_link:
        using_link += i
    new_url = f'https://www.amazon.com/charts/{using_link}/mostsold/fiction'
    url = new_url
    #url = using_link
    if using_link == False:
        break
    #s = soup()
f.close()


"""
### Using the book link to then scrape the page of that book
# To get more specific data
book_link = s.find('a', {'class': 'kc-cover-link app-specific-display not_app'})['href']
book_link = re.findall(r'/[d][p]/\w*[/]', book_link)[0]

starter_link = 'https://www.amazon.com'

# Figuring out how to open up the book link through amazon when they purposefully
# stop automatic crawling through their site
book_data = starter_link+book_link
book_opener = urllib.request.build_opener()
book_opener.addheaders = [('User-agent', 'Mozilla/5.0')]
book_link_opened = book_opener.open(book_data)
"""