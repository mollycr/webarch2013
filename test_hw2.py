#!/usr/bin/env python

from os import path
from urllib import urlencode
from urllib2 import urlopen

from bs4 import Comment


css_validator = 'http://jigsaw.w3.org/css-validator/validator?'


def create_url(base, url):
    if url.startswith("http"):
        return url
    elif url.startswith("/"):
        return '/'.join(base.split('/')[:3]) + url
    else:
        return path.join('/'.join(base.split('/')[:-1]), url)


def test_len(soup):
    assert len(soup.title.string)


def test_head(soup):
    assert soup.head


def test_css_links(soup, url):
    assert soup.head.link

    css_links = [l['href'] for l in soup.find_all('link') if "css" in l.get('href')]
    assert len(css_links) >= 2
    for link in css_links:
        assert any("No Error Found" in line for line in urlopen(css_validator + urlencode({'uri': create_url(url, link)})).readlines()), "Error found in %s" % link


def test_body(soup):
    assert soup.body


def test_div(soup):
    assert soup.div


def test_a(soup):
    assert soup.a


def test_list(soup):
    assert (soup.ul or soup.ol)
    assert soup.li


def test_img(soup, url):
    imgs = soup.find_all('img')
    assert imgs
    assert all(urlopen(create_url(url, img['src'])) for img in imgs)


def test_p(soup):
    assert soup.p


def test_header(soup):
    assert (soup.h1 or soup.h2 or soup.h3 or soup.h4)


def test_comment(soup):
    assert soup.findAll(text=lambda text: isinstance(text, Comment))


def test_id(soup):
    assert [e['id'] for e in soup.find_all() if e.get('id')]
    print  [e['id'] for e in soup.find_all() if e.get('id')]


def test_class(soup):
    assert [e['class'] for e in soup.find_all() if e.get('class')]
    print  [e['class'] for e in soup.find_all() if e.get('class')]


def test_style(soup):
    assert [e['style'] for e in soup.find_all() if e.get('style')]
    print  [e['style'] for e in soup.find_all() if e.get('style')]
