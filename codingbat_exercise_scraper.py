"""
This script gets all the exercises in codingbat and creates a base file in the appropriate folder to edit.

You need to install requests and bs4.

You can do the following to install:
pip install bs4
pip install requests

Author: Ha Min Ko
"""

import requests, bs4
import os
from os.path import exists

urlbase = 'https://codingbat.com'
url = urlbase + '/python'

cwd = os.getcwd()
res = requests.get(url)
res.raise_for_status()

html = bs4.BeautifulSoup(res.text, features='html.parser')

# We get the link for each main page.
for link in html.select('div[class=summ] > a'):
    name = link.text.lower()
    folder = cwd + '\\' + name
    os.chdir(folder)

    url1 = urlbase + link['href']

    res1 = requests.get(url1)
    html1 = bs4.BeautifulSoup(res1.text, features='html.parser')

    # We get the link for each exercise.
    for link1 in html1.select('td[width="200"] > a'):
        # print(link1.text)
        name1 = link1.text

        url2 = urlbase + link1['href']
        res2 = requests.get(url2)

        html2 = bs4.BeautifulSoup(res2.text, features='html.parser')
        # print(html2)

        title = name1 + '.py'

        # Check if file already exists.
        if (exists(title)):
            print(title, 'exists already.')
        else:
            function_definer = html2.select('div[id=ace_div]')[0].text.strip()
            function_description = html2.select('p[class=max2]')[0].text.strip()
            function_test = []
            for br in html2.find_all('br'):
                following = br.nextSibling
                if name1 in following:
                    function_test.append(following)

            # Create a file that can be written to.
            print('Creating file', title, 'in folder', name )
            outputfile = open(title, 'w')

            # Write data to the file:
            outputfile.write(function_definer)
            outputfile.write('\n\t"""')
            outputfile.write('\n\t' + function_description)
            outputfile.write('\n\t"""')
            outputfile.write('\n\tpass')
            outputfile.write('\n')
            for test in function_test:
                test = test.split('→')[0].strip()
                outputfile.write('\nprint(' + test + ')')
            outputfile.write('\n')

            # Close the file after writing to it
            outputfile.close()
