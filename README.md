Russian Fedora website
======================

Based on [Nikola](http://getnikola.com) static generator with customized [Bootblog-Jinja](https://themes.getnikola.com/#bootblog-jinja) theme.

Build
-----

Create virtualenv and activate:

    $ virtualenv -p /usr/bin/python3 venv
    $ source venv/bin/activate

Install requirements:

    (venv)$ pip install -r requirements.txt

Generate site:

    (venv)$ nikola build

Start the test server and open a browser:

    (venv)$ nikola serve -b

Add new post
------------

Run:

    (venv)$ nikola new_post
