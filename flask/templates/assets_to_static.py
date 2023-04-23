from bs4 import BeautifulSoup

# Open the original HTML file
with open('index.html', 'r') as f:
    html = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all links, scripts, and images in the HTML
for link in soup.find_all(['a', 'link', 'script']):
    if 'href' in link.attrs:
        link['href'] = link['href'].replace('assets', 'static')
    if 'rel' in link.attrs:
        link['rel'] = link['rel'][0].replace('assets', 'static')
    if 'src' in link.attrs:
        link['src'] = link['src'].replace('assets', 'static')

for img in soup.find_all('img'):
    if 'src' in img.attrs:
        img['src'] = img['src'].replace('assets', 'static')

# Export the modified HTML to a new file
with open('index.html', 'w') as f:
    f.write(str(soup))
