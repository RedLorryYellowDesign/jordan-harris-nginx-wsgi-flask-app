from bs4 import BeautifulSoup

# Open the original HTML file
with open('index.html', 'r') as f:
    html = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all links, scripts, and images in the HTML
for link in soup.find_all(['a', 'link']):
    # Replace the href attribute with a Jinja2-compatible syntax
    if 'href' in link.attrs:
        if not link['href'].startswith('#'):
            href = link['href'].split('/')
            href_path = '/'.join(href[1:])
            link['href'] = "{{ url_for('" + href[0] + "', filename='/" + href_path + "') }}"

for script in soup.find_all('script'):
    # Replace the src attribute or script content with a Jinja2-compatible syntax
    if 'src' in script.attrs:
        if not script['src'].startswith('#'):
          script_src = script['src'].split('/')
          script_src_path = '/'.join(script_src[1:])
          script['src'] = "{{ url_for('" + script_src[0] + "', filename='/" + script_src_path + "') }}"

          #script['src'] = "{{ url_for('static', filename='/" + script['src'] + "') }}"
    else:
        script.string = "{{ " + script.string.strip() + " }}"

for img in soup.find_all('img'):
    # Replace the src attribute with a Jinja2-compatible syntax
    img_src = img['src'].split('/')
    img_src_path = '/'.join(img_src[1:])
    img['src'] = "{{ url_for('" + img_src[0] + "', filename='/" + img_src_path + "') }}"



    #img['src'] = "{{ url_for('static', filename='/" + img['src'] + "') }}"


# Export the modified HTML to a new file
with open('index.html', 'w') as f:
    f.write(str(soup))
