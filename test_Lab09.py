import pytest
import requests

query = 'presidents of the united states'
ddg_url = f'http://api.duckduckgo.com/?q={query}&format=json'
ddg = requests.get(ddg_url)
ddg_json = ddg.json()
related_topics = ddg_json['RelatedTopics']
related_topics_text = ''
for topic in related_topics:
    related_topics_text += topic['Text']
pres_last_name_list = ['Adams', 'Arthur', 'Biden', 'Buchanan', 'Buren', 'Bush', 'Carter', 'Cleveland',
                       'Clinton', 'Coolidge', 'Eisenhower', 'Fillmore', 'Ford', 'Garfield', 'Grant',
                       'Harding', 'Harrison', 'Hayes', 'Hoover', 'Jackson', 'Jefferson', 'Johnson',
                       'Kennedy', 'Lincoln', 'Madison', 'McKinley', 'Monroe', 'Nixon', 'Obama', 'Pierce',
                       'Polk', 'Reagan', 'Roosevelt', 'Taft', 'Taylor', 'Truman', 'Trump', 'Tyler',
                       'Washington', 'Wilson']


@pytest.mark.parametrize("president_list", pres_last_name_list)
def test_presidents_last_name(president_list):
    assert president_list in related_topics_text
