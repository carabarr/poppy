import requests
import click

@click.command()
@click.argument('title')
@click.option('--read', default=False)
def search(title, read):
    book_data = {}
    
    url = urlify_title(title)
    response = requests.get(url).json()
    search_results = response.get('docs')
    try:
        first_result = search_results[0]
    except:
        print('no results')
        exit()

    click.confirm('Is this accurate? ' + first_result.get('title'), abort=True)

    # adds author and cover id data (harder to get from actual work page)
    parse_data(book_data, first_result)

    # gets the unique key associated with the work for searching 
    work_key = first_result.get('key')
    work = search_by_work(work_key)

    add_description(book_data, work)
    print(book_data)

def parse_data(book_data, result):
    book_data['title'] = result.get('title')
    book_data['subtitle'] = result.get('subtitle')
    book_data['author'] = result.get('author_name')
    book_data['cover_id'] = result.get('cover_i')


def urlify_title(title):
    base = "https://openlibrary.org/search.json?title="
    # make sure title is lowercase and separated by +
    search_title = title.replace(" ", "+").lower()
    url = base + search_title
    return url

def search_by_work(work):
    url = 'https://openlibrary.org' + work + '.json'
    r = requests.get(url)
    data = r.json()
    return data

def add_description(book_data, result):
    # book_data['title'] = result.get('title')
    # book_data['subtitle'] = result.get('subtitle')
    book_data['description'] = result.get('description').get('value')

if __name__ == '__main__':
    search()




