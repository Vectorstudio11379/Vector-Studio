from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    s_orig = BeautifulSoup(f.read(), 'html.parser')

with open('test_index.html', 'r', encoding='utf-8', errors='ignore') as f:
    s_test = BeautifulSoup(f.read(), 'html.parser')

print("Original scripts:", len(s_orig.find_all('script')), "Test scripts:", len(s_test.find_all('script')))
print("Original canvas:", len(s_orig.find_all('canvas')), "Test canvas:", len(s_test.find_all('canvas')))
print("Original sections:", len(s_orig.find_all('section')), "Test sections:", len(s_test.find_all('section')))
print("Original divs:", len(s_orig.find_all('div')), "Test divs:", len(s_test.find_all('div')))
print("Test header:", bool(s_test.find('header', class_='vs-navbar')))
print("Test footer:", bool(s_test.find('footer', class_='site-footer')))
