#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'Jophy'
import urllib2
import re
import time
from xml.dom import minidom

try:
    from bs4 import BeautifulSoup
except ImportError:
    print 'This python program need import beautifulsoup \n' \
          'Lear more :http://www.crummy.com/software/BeautifulSoup/'


def tld_list():
    root_zone_url = 'http://www.iana.org/domains/root/db'
    try:
        content = urllib2.urlopen(root_zone_url).read()
    except Exception as e:
        print str(e)
    soup = BeautifulSoup(content)
    tr = soup.find_all(attrs={'class': re.compile(r'iana-group-\d')})
    for group in tr:
        f = open('tldlistnew.txt', 'ab+')
        link = 'http://www.iana.org' + group.a['href'].encode('utf-8')
        tld = group.a.get_text().encode('utf-8')
        idn = ''
        type = group.contents[3].get_text().encode('utf-8')
        if 'xn' in group.a['href']:
            idn = group.a['href'].rstrip('.html').lstrip('/domains/root/db/').encode('utf-8')
        f.write(('%s -- %s -- %s -- %s\n' % (tld, idn, type, link)))
        f.close()


def tld_parser():
    f = open('tldlist.txt', 'r')
    for line in f:
        i = open('tldall.txt', 'ab+')
        line = line.strip()
        tld_url = line.split(' -- ')[-1].strip()
        content = urllib2.urlopen(tld_url).read()
        re_nic = re.compile(r'<b>URL for registration services:</b> <a href="(.*)">.*</a><br/>')
        re_whois = re.compile(r'<b>WHOIS Server:</b>\s*(\S*)')
        nic_result = re_nic.findall(content)
        whois_result = re_whois.findall(content)
        print nic_result
        print whois_result

        if len(nic_result) > 0:
            i.write(line + ' -- ' + nic_result[0])
        else:
            i.write(line + ' -- ' + '')

        if len(whois_result) > 0:
            i.write(' -- ' + whois_result[0] + '\n')
        else:
            i.write(' -- ' + '' + '\n')
        i.close()
    f.close()


def adddom(tld_dic):
    #tld node
    tld = doc.createElement('tld')
    tld.setAttribute('id', str(tld_dic['id']))
    tldlist.appendChild(tld)

    #domain node
    domain = doc.createElement('domain')
    domain.appendChild(doc.createTextNode(tld_dic['domain']))
    tld.appendChild(domain)

    #idn node
    idn = doc.createElement('idn')
    idn.appendChild(doc.createTextNode(tld_dic['idn']))
    tld.appendChild(idn)

    #type node
    type = doc.createElement('type')
    type.appendChild(doc.createTextNode(tld_dic['type']))
    tld.appendChild(type)

    #nic node
    nic = doc.createElement('nic')
    nic.appendChild(doc.createTextNode(tld_dic['nic']))
    tld.appendChild(nic)

    #whois node
    whois = doc.createElement('whois')
    whois.appendChild(doc.createTextNode(tld_dic['whois']))
    tld.appendChild(whois)


def create_xml():
    doc.appendChild(doc.createComment('A tld xml including the whole gTLDs & ccTLDs . '))
    doc.appendChild(doc.createComment('Create time :' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    doc.appendChild(doc.createComment('Author: Jophy (https://github.com/jophy)'))
    #tldlist = doc.createElement('tldlist')
    doc.appendChild(tldlist)
    all = open('tldall.txt', 'r')
    i = 1
    for line in all:
        split = line.strip('\n').split(' -- ')
        print split
        domain = split[0]
        idn = split[1]
        type = split[2]
        nic = split[4]
        whois = split[5]
        iana = split[3]
        adddom({
            'id': str(i),
            'domain': domain,
            'idn': idn,
            'type': type,
            'nic': nic,
            'whois': whois,
            'iana': iana
        })
        i += 1
    all.close()
    xml = open('tldlist.xml', 'w')
    xml.write(doc.toprettyxml())
    xml.close()

if __name__ == '__main__':
    '''

    Due to some unpredictable errors (Mostly Network Errors),

    I recommend you to run ONE function each time.

    You could also use my results directly .

    '''
    #First step : run tld_list() function , get tld list in brief
    #create tldlist.txt
    tld_list()

    #second step : run tld_parser() function , get tld information in details
    #create tldall.txt
    tld_parser()

    #third step : run following codes , get a xml file.
    #create tldlist.xml
    doc = minidom.Document()
    tldlist = doc.createElement('tldlist')
    create_xml()
