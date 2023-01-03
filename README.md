# g8

## Why g8 ?
```g8``` is meant to *worldwidely* replace ```wget``` to download a single file. Yep, just that. It doesn't do anything else, but you type 2 letters instead of 4, and it's pretty.

According to **[LiveChat](https://www.livechat.com/)** (which, for sure, looks like a very valid source of information), an **average person** types **190** to **200** characters per minute. That means that typing ```wget``` takes **1.2 to 1.26 seconds**. Typing ```g8``` takes **0.6 to 0.63 seconds**. That's **two times faster**. That's a lot of time saved.

## Output example
![g8 output](img/demo.gif?raw=true "g8 output")

## Installation
Well, first, you need Python. What's funny is that you can download Python with ```g8``` hahaha, but right now you can't.
Do it manually.

Then, just type
```python3 setup.py install```
(You may need to install manually the dependencies, see ```requirements.txt```)

## Usage
Just type ```g8``` followed by the URL of the file you want to download. It will be downloaded in the current directory.

You can specify a path to where you want to download the file. See the following examples.

## Examples
```g8 https://www.python.org/ftp/python/3.11.1/python-3.11.1-macos11.pkg```

```g8 https://www.python.org/ftp/python/3.11.1/python-3.11.1-macos11.pkg .```

```g8 https://www.python.org/ftp/python/3.11.1/python-3.11.1-macos11.pkg ..```

```g8 https://www.python.org/ftp/python/3.11.1/python-3.11.1-macos11.pkg /home/user/Downloads```

```g8 https://www.python.org/ftp/python/3.11.1/python-3.11.1-macos11.pkg file.extension```

```g8 https://www.python.org/ftp/python/3.11.1/python-3.11.1-macos11.pkg /home/user/Downloads/file.extension```

## Help
```g8 -h```
