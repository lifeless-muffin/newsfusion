import requests
from bs4 import BeautifulSoup
import language as language

# collect and parse data
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


# function to parse xml content
def parse_xml(file_path):   

    articles_list_json = []
    articles_list_text = []

    ## static xml page content
    xml_content = read_file(file_path=file_path)
    content_soup = BeautifulSoup(xml_content, 'xml')
    articles = content_soup.find_all('item')

    ## loop through and parse
    for article in articles:
        title = article.find('title').text
        description = article.find('description').text
        link = article.find('link').text
        pub_date = article.find('pubDate').text
        
        json_article = {'title': title, 'description': description, 'link': link, 'pub-date': pub_date}
        text_article = title + '\n' + description

        articles_list_json.append(json_article)
        articles_list_text.append(text_article)
    
    return {'articles_json': articles_list_json, 'articles_text': articles_list_text}


# map entities to individual news items
def batch_entities_processing(entities, articles_text, articles_json):

    # Preprocess the items list
    articles_json_dup = articles_json
    articles_lowerd = [item.lower() for item in articles_text]

    # Iterate over each key in entities
    for entity in entities:
        for index, item in enumerate(articles_lowerd):
            if entity['name'].lower() in item:
                articles_json_dup[index]['']
                print(f"Match found! {entity['name']} in {index}")
                break  # Exit the inner loop once a match is found


# saved the result in archive


if __name__ == '__main__':

    # collect and parse data
    result = parse_xml(file_path='input/nyt-world.xml')
    articles_json = result['articles_json']    
    articles_text = result['articles_text']    

    # process data through "language.py" module
    batch_entities = language.main(articles_text, 'PLAIN_TEXT')
    batch_entities_processing(batch_entities, articles_text)

