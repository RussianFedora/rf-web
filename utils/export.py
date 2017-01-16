#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Export articles from Drupal 7(html) to Nikola 7(rst) format.
"""

import psycopg2
import pypandoc
import datetime
from re import sub, UNICODE


class Article:
    def __init__(self, data):
        self.title = data[0]
        self.name = data[1]
        self.date = datetime.datetime.fromtimestamp(data[2])
        self.content = data[3]
        self.url = data[4]
        self.nid = data[5]
        self.vid = data[6]

        # Sometimes there is no alias in drupal, use dummy node
        # address instead
        if not self.url:
            self.url = "content/node-{0}".format(self.nid)

    def __repr__(self):
        return "{nid}:{vid} {title} by {name}\n created {time}\n published at {url}".format(
            title=self.title,
            nid=self.nid,
            vid=self.vid,
            name=self.name,
            time=self.date,
            url="http://russianfedora.pro/" + self.url,
            )

    def get_header(self):

        header_template = (
            ".. title: {title}\n"
            ".. slug: {slug}\n"
            ".. date: {date}\n"
            ".. tags:\n"
            ".. category:\n"
            ".. link:\n"
            ".. description:\n"
            ".. type: text\n"
            ".. author: {name}\n"
            "\n"
            "**Это архивная статья**\n"
            "\n"
        )

        header = header_template.format(
            title=self.title,
            slug=self.url.split('/')[-1],
            name=self.name,
            date=self.date,
         )

        return header

    def get_content(self):
        output = pypandoc.convert(
            self.content,
            'rst',
            format='html'
        )

        # Additional hacks

        output = sub(u"([\wА-Яа-я\)]{2}\.\n)", "\g<1>\n", output)
        output = sub("\*\*\*\*\n","\n****\n\n", output)

        return output

    def publish(self, path=None):

        if not path:
            path = "{0}.rst".format(self.url)

        with open(path, 'w') as f:
            f.write(self.get_header())
            f.write("\n")
            f.write(self.get_content().encode('utf-8'))

        return path

DB_NAME="rf"

query="""
SELECT
node.title,
users.name,
node.created,
field_data_body.body_value,
url_alias.alias,
node.nid,
node.vid
FROM node
LEFT JOIN field_data_body
ON node.nid=field_data_body.entity_id AND node.vid=field_data_body.revision_id
LEFT JOIN url_alias
ON url_alias.source=concat('node/',node.nid)
LEFT JOIN users
ON node.uid=users.uid
WHERE node.type='project_pulse' and node.status=1
"""

conn = psycopg2.connect(database=DB_NAME)

cur = conn.cursor()

cur.execute(query)

print "Got {count} articles".format(count=cur.rowcount)

for data in cur:
    article = Article(data)
    print "{0}".format(article)
    article.publish()
