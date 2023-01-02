# -*- coding: utf-8 -*-
# --------------------------------------------------
# Test file for g8 module
# Quentin Dufournet, 2023
# --------------------------------------------------
# Built-in
import sys
import subprocess as sp

# 3rd party

# --------------------------------------------------

def test_missing_url():
    output = sp.getoutput('python3 src/g8.py')
    assert output == 'Missing URL :('
    
def test_invalid_url():
    output = sp.getoutput('python3 src/g8.py www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz')
    assert output == 'Invalid URL :('

def test_http_url():
    output = sp.getoutput('python3 src/g8.py http://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz')
    assert output == 'HTTP is not safe, add the argument --allow-http'
    
def test_http_url_with_allow_http():
    output = sp.getoutput('python3 src/g8.py http://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz --allow-http')
    assert output.startswith('~/Python-3.11.1.tar.xz ⥊')
    
def test_https_url():
    output = sp.getoutput('python3 src/g8.py https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz')
    assert 'downloaded successfully' in output

# TODO: Find a way to test a content length of 0