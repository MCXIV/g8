# -*- coding: utf-8 -*-
# --------------------------------------------------
# Test file for g8 module
# Quentin Dufournet, 2023
# --------------------------------------------------
# Built-in
import sys
import subprocess as sp
import os

# 3rd party
import pytest

# --------------------------------------------------


def test_missing_url():
    """ Scenario
    * Running the script without arguments
    * Checking the output
    """

    output = sp.getoutput('python3 src/g8.py')
    assert output == 'usage: g8.py [-h] [-a A] url [outputpath]\ng8.py: error: the following arguments are required: url'


def test_invalid_url():
    """ Scenario
    * Running the script with an invalid URL
    * Checking the output
    """

    output = sp.getoutput('python3 src/g8.py www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz')
    assert output == 'Invalid URL :('


def test_http_url():
    """ Scenario
    * Running the script with an http URL
    * Checking the output
    """

    output = sp.getoutput(
        'python3 src/g8.py http://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz')
    assert output == 'HTTP is not safe, add the optionnal argument -a allow-http'


def test_http_url_with_allow_http():
    """ Scenario
    * Running the script with an http URL and the --allow-http argument
    * Checking the output
    """

    output = sp.getoutput(
        'python3 src/g8.py http://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz -a allow-http')
    assert output.startswith('⥊ Python-3.11.1.tar.xz')


def test_https_url():
    """ Scenario
    * Running the script with an https URL
    * Checking the output
    """

    output = sp.getoutput(
        'python3 src/g8.py https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz')
    assert 'downloaded successfully' in output


def test_https_url_path_previous():
    """ Scenario
    * Changing the current directory to ./tests
    * Running the script with an https URL and a path of ..
    * Changing the current directory back to the root
    * Checking the output
    * Checking the file is downloaded in the previous directory
    """

    os.chdir('./tests')
    output = sp.getoutput(
        'python3 ../src/g8.py https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz ..')
    os.chdir('..')
    if 'downloaded successfully' not in output:
        pytest.fail('Download failed', output)
    assert os.path.isfile('./Python-3.11.1.tar.xz')


def test_https_url_current_path():
    """ Scenario
    * Running the script with an https URL and a path of .
    * Checking the output
    * Checking the file is downloaded in the current directory
    """

    output = sp.getoutput(
        'python3 src/g8.py https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz .')
    if 'downloaded successfully' not in output:
        pytest.fail('Download failed', output)
    assert os.path.isfile('./Python-3.11.1.tar.xz')


def test_https_url_path():
    """ Scenario
    * Running the script with an https URL and a path of ./tests/
    * Checking the output
    * Checking the file is downloaded in ./tests/
    """

    output = sp.getoutput(
        'python3 src/g8.py https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz tests/')
    if 'downloaded successfully' not in output:
        pytest.fail('Download failed', output)
    assert os.path.isfile('./tests/Python-3.11.1.tar.xz')


def test_https_url_filename():
    """ Scenario
    * Running the script with an https URL and a filename
    * Checking the output
    * Checking the file is downloaded and has the correct name
    """

    output = sp.getoutput(
        'python3 src/g8.py https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz pytest.tar.xz')
    if 'downloaded successfully' not in output:
        pytest.fail('Download failed', output)
    assert os.path.isfile('./pytest.tar.xz')


def test_https_url_filename():
    """ Scenario
    * Running the script with an https URL, a path, and a filename
    * Checking the output
    * Checking the file is downloaded and has the correct name in the correct path
    """

    output = sp.getoutput(
        'python3 src/g8.py https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz tests/pytest.tar.xz')
    if 'downloaded successfully' not in output:
        pytest.fail('Download failed', output)
    assert os.path.isfile('./tests/pytest.tar.xz')


def test_clean_downloads():
    """ Scenario
    * Deleting every downloaded file
    """

    os.remove('./Python-3.11.1.tar.xz')
    assert not os.path.isfile('./Python-3.11.1.tar.xz')
    os.remove('./tests/pytest.tar.xz')
    assert not os.path.isfile('./tests/pytest.tar.xz')
    os.remove('./tests/Python-3.11.1.tar.xz')
    assert not os.path.isfile('./tests/Python-3.11.1.tar.xz')

# TODO: Find a way to test a content length of 0
