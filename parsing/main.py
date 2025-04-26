from bs4 import BeautifulSoup as bs 
import requests 

URL = 'https://www.kivano.kg/mobilnye-telefony'

response = requests.get(URL)
html = response.text
soup = bs(html, 'lxml')
telephone_list = soup.find_all('div', class_='item product_listbox oh')

telephones = []
titles = []
desc = []
name_and_desc_odelno = []
name_and_desc_c_radelitelem = []
name_and_desc_bez_lishnih_simvolov = []
name_and_desc = []



for telephone in telephone_list:
    name_and_desc.append(telephone.find('div', class_='product_text pull-left').text)
    print(name_and_desc, '\n\n') # мы стянули информацию(название и описание) с html, при помощи метода find и тега div с классом product_text pull-left

    name_and_desc_bez_lishnih_simvolov.append(name_and_desc[0].strip())
    print(name_and_desc_bez_lishnih_simvolov, '\n\n') # убрали мусор в начале и в конце
    
    name_and_desc_c_radelitelem.append(name_and_desc_bez_lishnih_simvolov[0].replace('\n\n        ', '|||')) # убрали мусор в середине добавив разделитель (|||) 
    print(name_and_desc_c_radelitelem, '\n\n')

    name_and_desc_odelno.append(name_and_desc_c_radelitelem[0].split('|||')) 
    print(name_and_desc_odelno, '\n\n') # разделили большой один текст на 2 маленьких текста - это на название и описание при помощи ||| 

    break
