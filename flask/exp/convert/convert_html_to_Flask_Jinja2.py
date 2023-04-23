import os
from bs4 import BeautifulSoup

def convert_html_files_to_jinja2(dir_path):
    # Scan the directory recursively for HTML files
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.html'):
                # Open the HTML file
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    html = f.read()

                # Parse the HTML using BeautifulSoup
                soup = BeautifulSoup(html, 'html.parser')

                # Find all links and images in the HTML
                for link in soup.find_all('a'):
                    # Replace the href attribute with a Jinja2-compatible syntax
                    link['href'] = "{{ url_for('" + link['href'] + "') }}"
                for img in soup.find_all('img'):
                    # Replace the src attribute with a Jinja2-compatible syntax
                    img['src'] = "{{ url_for('" + img['src'] + "') }}"

                # Export the modified HTML to a new file
                with open(file_path, 'w') as f:
                    f.write(str(soup))

    print("All HTML files in the directory have been converted to Jinja2-compatible syntax.")

# Example usage: convert all HTML files in the current directory to Jinja2-compatible syntax
convert_html_files_to_jinja2('.')
