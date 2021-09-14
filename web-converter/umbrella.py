#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (c) 2021 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

from __future__ import absolute_import, division, print_function

__author__ = "Josh Ingeniero <jingenie@cisco.com>"
__copyright__ = "Copyright (c) 2021 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


import os
import pandas as pd
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader(os.path.join(os.getcwd(), 'templates')))


if __name__ == '__main__':
    print('*'*30)
    print('Welcome to the Umbrella Report CSV > JSON + XML + HTML Conversion Script')
    # input_file = 'report.csv'
    # output_file_json = 'top.json'
    # output_file_xml = 'top.xml'
    # output_file_html = 'top.html'
    input_file = input('Please enter the input filename: ')
    while not(os.path.exists(input_file)):
        input_file = input("File doesn't exist!!! Enter another input filename: ")
    output_file_json = input('Please enter the json output filename: ')
    while os.path.exists(output_file_json):
        output_file_json = input('File exists!!! Enter another output filename: ')
    output_file_xml= input('Please enter the xml output filename: ')
    while os.path.exists(output_file_xml):
        output_file_xml = input('File exists!!! Enter another output filename: ')
    output_file_html= input('Please enter the html output filename: ')
    while os.path.exists(output_file_html):
        output_file_html = input('File exists!!! Enter another output filename: ')
    print(f'Starting conversion from {input_file} to {output_file_json}, {output_file_xml} and {output_file_html}!')
    print('*'*30)
    csv = pd.read_csv(input_file)
    csv.drop(csv.filter(regex="Unname"), axis=1, inplace=True)
    csv.columns = csv.columns.str.replace(' ', '')
    csv.columns = csv.columns.str.replace(':', '')
    csv.columns = csv.columns.str.lower()
    csv.to_json(path_or_buf=output_file_json, orient='records', indent=2)
    csv.to_xml(path_or_buffer=output_file_xml)
    data = csv.to_dict('records')
    headers = list(csv.columns)
    template = env.get_template('template.html')
    html = template.render(data=data, headers=headers)
    with open(output_file_html, 'w', encoding="utf-8") as file:
        file.write(html)
    print('*'*30)
    print(f'Conversion complete! Check {output_file_json}, {output_file_xml}, and {output_file_html}!')
