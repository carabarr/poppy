import requests
import click

@click.command()
@click.argument('title')
@click.argument('author', required=False)
@click.option('--read', default=False)
def search(title, read, author):
    book_data = {}
    
    url = urlify_title(title, author)
    response = requests.get(url).json()
    search_results = response.get('docs')
    try:
        first_result = search_results[0]
    except:
        print('Nothing matches the search! Check manually on open library.')
        exit()
    
    confirmation = (f"Is this accurate? {first_result.get('title')}"
                    f" by {', '.join(str(x) for x in first_result.get('author_name'))}")
    click.confirm(confirmation, abort=True)

    # adds author and cover id data (harder to get from actual work page)
    parse_data(book_data, first_result)

    # gets the unique key associated with the work for searching 
    work_key = first_result.get('key')
    work = search_by_work(work_key)
    book_data['description'] = work.get('description').get('value')
    
    print(book_data)

def parse_data(book_data, result):
    book_data['title'] = result.get('title')
    book_data['subtitle'] = result.get('subtitle')
    book_data['author'] = result.get('author_name')
    book_data['cover_id'] = result.get('cover_i')


def urlify_title(title, author):
    base = "https://openlibrary.org/search.json?"
    search_title = title.replace(" ", "+").lower()
    url = base + 'title=' + search_title
    if author:
        search_author = author.replace(" ", "+").lower()
        url = url + '&author=' + search_author
    return url

def search_by_work(work):
    url = 'https://openlibrary.org' + work + '.json'
    r = requests.get(url)
    data = r.json()
    return data

if __name__ == '__main__':
    search()




