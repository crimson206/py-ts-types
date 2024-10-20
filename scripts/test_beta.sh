#!/bin/bash
set -e

cd beta
pip install --upgrade pip
pip install flake8
pip install setuptools wheel
pip install -r requirements_test.txt
pip install .

flake8

cd ..

pytest
