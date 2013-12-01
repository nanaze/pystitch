#!/bin/bash

set -ex

# move to this directory
cd `dirname $0`

# Run all tests
python -m unittest discover -p '*_test.py' -s pystitch
