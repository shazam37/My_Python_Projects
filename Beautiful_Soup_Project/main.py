from bs4 import BeautifulSoup
import requests

import lxml

# with open("website.html", encoding='utf8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'lxml')
# # anchor_tags = soup.find_all(name='a')
# #
# # for tag in anchor_tags:
# #     print(tag.get('href'))
#
# heading = soup.find(name='h3', class_='heading')
# print(heading)

# site = requests.get('https://news.ycombinator.com/')
# soup = BeautifulSoup(site.text, 'lxml')
# article_tage = soup.find_all(name='span', class_='titleline')
# article_score = soup.find_all(name='span', class_='score')
# tag_list = [article.getText() for article in article_tage]
# link_list = [article.find('a').get('href') for article in article_tage]
# point_list = [int(article.getText().split()[0]) for article in article_score]
# # print(tag_list)
# # print(link_list)
# max_number_list = point_list.index(max(point_list))
# print(tag_list[max_number_list])
# print(link_list[max_number_list])
# print(max(point_list))
# # for article in article_tage:
#     print(article.getText())
#     print(article.find('a').get('href'))

# print(article_score.getText())
site = requests.get('https://web.archive.org/web/20200518073855/'
                    'https://www.empireonline.com/movies/features/best-movies-2/')

soup = BeautifulSoup(site.text, 'lxml')

movie_title = soup.find_all(name='h3', class_='title')

all_list = [article.getText() for article in movie_title]

with open('movie.txt', 'a') as file:

    for article in all_list[::-1]:

        try:
            file.writelines(f'{article}\n')
        except UnicodeEncodeError:
            pass


