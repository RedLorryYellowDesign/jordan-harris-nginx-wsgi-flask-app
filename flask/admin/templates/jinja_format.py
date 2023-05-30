import re
from bs4 import BeautifulSoup

# Open the original HTML file
with open('index.html', 'r') as f:
    html = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all links, scripts, and images in the HTML
for element in soup.find_all(['a', 'link', 'script', 'img']):
    if 'href' in element.attrs and element['href'].startswith(('http', 'https')):
        element['href'] = "{{ '" + element['href'] + "' }}"
    elif 'src' in element.attrs and element['src'].startswith(('http', 'https')):
        element['src'] = "{{ '" + element['src'] + "' }}"

    # Replace the href attribute with a Jinja2-compatible syntax
    elif 'href' in element.attrs:
        if not element['href'].startswith('#'):
            href = element['href'].split('/')
            href_path = '/'.join(href[1:])
            element['href'] = "{{ url_for('" + href[0] + "', filename='/" + href_path + "') }}"

    # Replace the src attribute or script content with a Jinja2-compatible syntax
    elif element.name == 'script' and element.string:
        element.string = "{{ " + element.string.strip() + " }}"

    elif 'src' in element.attrs:
        if not element['src'].startswith('#'):
            script_src = element['src'].split('/')
            script_src_path = '/'.join(script_src[1:])
            element['src'] = "{{ url_for('" + script_src[0] + "', filename='/" + script_src_path + "') }}"

# Check for double curly braces
modified_html = str(soup)
if re.search(r'{{\s*url_for\(\'{{\s*url_for\(', modified_html):
    raise ValueError("Double curly braces detected: {{ url_for('{{ url_for(...) }}'")

# Export the modified HTML to a new file
with open('index.html', 'w') as f:
    f.write(modified_html)
