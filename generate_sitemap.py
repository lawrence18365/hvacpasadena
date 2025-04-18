import os
import datetime
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

def get_html_files(base_dir):
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                full_path = os.path.join(root, file)
                html_files.append(full_path)
    return html_files

def file_lastmod_date(filepath):
    timestamp = os.path.getmtime(filepath)
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

def generate_sitemap(base_dir, base_url, output_file='sitemap.xml'):
    urlset = Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    html_files = get_html_files(base_dir)
    for filepath in html_files:
        url = SubElement(urlset, 'url')
        relative_path = os.path.relpath(filepath, base_dir).replace(os.sep, '/')
        loc = SubElement(url, 'loc')
        loc.text = f"{base_url}/{relative_path}"
        lastmod = SubElement(url, 'lastmod')
        lastmod.text = file_lastmod_date(filepath)
        changefreq = SubElement(url, 'changefreq')
        changefreq.text = 'monthly'
        priority = SubElement(url, 'priority')
        # Set priority based on file type or path (example logic)
        if relative_path == 'index.html':
            priority.text = '1.0'
            changefreq.text = 'weekly'
        elif relative_path.startswith('blog/'):
            priority.text = '0.7'
            changefreq.text = 'weekly'
        else:
            priority.text = '0.8'

    tree = ElementTree(urlset)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    print(f"Sitemap generated and saved to {output_file}")

if __name__ == "__main__":
    # Change base_url to your website's URL
    base_url = "https://hvacpasadena.com"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    generate_sitemap(base_dir, base_url)