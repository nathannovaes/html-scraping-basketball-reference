from lxml import html
import requests
from tabulate import tabulate


page = requests.get('https://www.basketball-reference.com/boxscores/202403220SAS.html')

tree = html.fromstring(page._content)

table_element = tree.xpath('//table[@id="box-MEM-game-basic"]')[0]

headers = []
for header in table_element.xpath('.//thead//th'):
    headers.append(header.text_content().strip())


content = []
data_rows = table_element.xpath('.//tbody//tr')
for row in data_rows:
    row_data = [data.text_content().strip() for data in row.xpath('.//th')]
    content.append(row_data)

    row_data = [data.text_content().strip() for data in row.xpath('.//td')]
    content.append(row_data)


print(tabulate(content, headers=headers))