#!/bin/sh

# runs assets_to_static.py
python assets_to_static.py

# converts html links, scrips and images to jinja2 format
python jinja_format.py
