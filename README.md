# Umbrella and Threat Grid Report Converter
Tool for converting reports from Umbrella or Threat Grid to appropriate formats

## Contacts
* Josh Ingeniero (jingenie@cisco.com)

## Solution Components
* Umbrella
* Threat Grid
* Python

## Installation:

#### Clone the repo
```console
git clone https://github.com/gve-sw/gve_devnet_umbrella_threat_grid_report_converter
```
#### Set up a Python venv
First make sure that you have Python 3 installed on your machine. We will then be using venv to create
an isolated environment with only the necessary packages.

##### Install virtualenv via pip
```
$ pip install virtualenv
```

##### Create a new venv
```
Change to your project folder
$ cd gve_devnet_umbrella_threat_grid_report_converter

Create the venv
$ virtualenv venv

Activate your venv
$ source venv/bin/activate
```

#### Install dependencies
```
$ pip install -r requirements.txt
```

## Usage

This repository contains three scripts:
* [threat-grid-pdf.py](web-converter/threat-grid-pdf.py) - Converts a Threat Grid .json report or analysis to .pdf
* [threat-grid-xml.py](web-converter/threat-grid-xml.py) - Converts a Threat Grid .json report or analysis to .xml
* [umbrella.py](web-converter/umbrella.py)  - Converts an Umbrella .csv report to .json, .xml, and .html


### Python
Run the required script and follow the prompts
```
$ cd web-converter
$ python script_name.py
```


### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.