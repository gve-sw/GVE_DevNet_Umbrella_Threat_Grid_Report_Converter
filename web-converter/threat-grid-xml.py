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
import json
import dicttoxml
from lxml import etree
from io import BytesIO


if __name__ == '__main__':
    print('*'*30)
    print('Welcome to the Threat Grid Report JSON > XML Conversion Script')
    # input_file = 'analysis.json'
    # output_file = 'analysis.xml'
    input_file = input('Please enter the input filename: ')
    while not(os.path.exists(input_file)):
        input_file = input("File doesn't exist!!! Enter another input filename: ")
    output_file = input('Please enter the output filename: ')
    while os.path.exists(output_file):
        output_file = input('File exists!!! Enter another output filename: ')
    print(f'Starting conversion from {input_file} to {output_file}!')
    print('*'*30)
    with open(input_file, encoding="utf8") as in_file:
        string = in_file.read().replace("\\u0000", "")
        data = json.loads(string)
        with open(output_file, 'w', encoding="utf-8") as file:
            xml = dicttoxml.dicttoxml(data, custom_root='analysis')
            root = etree.parse(BytesIO(xml))
            xml_pretty = etree.tostring(root, pretty_print=True).decode()
            file.write(xml_pretty)
    print('*'*30)
    print(f'Conversion complete! Check {output_file}!')
