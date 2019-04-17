# -*- coding: utf-8 -*-
"""main.py

"""
import datetime

from jinja2 import Environment, FileSystemLoader
from configparser import ConfigParser


def generate_markdown(template_filename):
    config = ConfigParser()
    with open('config.ini', 'r', encoding='utf-8') as f:
        config.read_file(f)

    # Init vars
    created_at = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    # Read config.
    plant_ip_addr = config.get('info', 'plant_ip_addr')
    neteco_ip_addr = config.get('info', 'neteco_ip_addr')
    enspire_password = config.get('info', 'enspire_password')
    customer_name = config.get('info', 'customer_name')
    user_name = config.get('info', 'user_name')
    password = config.get('info', 'password')
    author = config.get('info', 'author')
    author_email = config.get('info', 'author_email')

    env = Environment(loader=FileSystemLoader('templates', encoding='utf8'))
    template = env.get_template(template_filename)

    markdown = template.render(
        {
            'plant_ip_addr': plant_ip_addr,
            'neteco_ip_addr': neteco_ip_addr,
            'customer_name': customer_name,
            'enspire_password': enspire_password,
            'user_name': user_name,
            'password': password,
            'author': author,
            'author_email': author_email,
            'created_at': created_at
        }
    )

    destination = 'dest' + '/' + template_filename
    with open(destination, 'w', encoding='utf-8') as dest:
        dest.write(markdown)


def main():

    templates = ['enspire.md', 'neteco.md']
    for template in templates:
        generate_markdown(template)


if __name__ == '__main__':
    main()
