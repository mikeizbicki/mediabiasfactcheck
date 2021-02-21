#/usr/bin/python3

import csv
import glob
import lxml
import lxml.html

images = [
        'MBFCVeryhigh.png',
        'MBFCHigh.png',
        'MBFCMostlyFactual.png',
        'MBFCMixed.png',
        'MBFCLow.png',
        'MBFCVeryLow.png'
        ]

xpaths = {
    'name' : '//h1',
    #'factual2' : '//div[@class="entry-content clearfix"]/p/span/strong',
    #'country2' : '//div[@class="entry-content clearfix"]/p/strong',
    #'freedom_rank2' : '//div[@class="entry-content clearfix"]/p/span[2]/strong',
    #'bias_img' : '//h2/img[1]/@alt',
    #'factual_img' : '//h2/img[2]/@alt',
    #'factual' : "//p[contains(text(),'Factual Reporting')]/span/strong",
    'factual' : "//p[contains(text(),'Factual Reporting')]/span/strong",
    'country' : "//p[contains(text(),'Factual Reporting')]/strong",
    'freedom_rank' : "//p[contains(text(),'Factual Reporting')]/span[2]/strong",
    #'bias' : '//h2/span',
    'bias' : '(//h3/span)|(//h2/span)|(//header/h1/span)|(//h1[contains(text(),\'QUESTIONABLE\')])|(//h1[contains(text(),\'BIAS\')])|(//h2[contains(text(),\'BIAS\')])|(//h2[contains(text(),\'SATIRE\')])|(//h2[contains(text(),\'SCIENCE\')])', 
    'url' : "(//*[contains(text(),'Source:')]/a/@href)|(//a/span[contains(text(),'https://')])|(//a/span[contains(text(),'http://')])",
    #'url' : "//a[contains(text(),'https://')]",
    }
compiled_xpaths = { key : lxml.etree.XPath(xpath) for key,xpath in xpaths.items() }

with open('mediabiasfactcheck.csv', 'w', newline='') as csvfile:
    fieldnames = list(reversed(sorted(['image_bias']+list(xpaths.keys()))))
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i,path in enumerate(glob.glob('mediabiasfactcheck.com/*/index.html', recursive=True)):
        print("i,path=",i,path)
        if path=='mediabiasfactcheck.com/feed/index.html':
            # this breaks lxml, so skip it
            continue
        with open(path) as fin:
            html = fin.read()
        doc = lxml.html.fromstring(html)
        row = {}
        for key,compiled_xpath in compiled_xpaths.items():
            elements = compiled_xpath(doc)
            if len(elements) == 0:
                result_str = ''
                #qq
            else:
                element = elements[0]
                if type(element) is lxml.etree._ElementUnicodeResult:
                    result_str = str(element)
                elif type(element) is lxml.etree._Element:
                    result_str = element.text
                elif type(element) is lxml.html.HtmlElement:
                    result_str = element.text_content()
            row[key] = result_str.strip()
        #import pprint
        #pprint.pprint(row)
        #print()
        #if i>10:
            #asd
        for image in images:
            if image in html:
                row['image_bias']=image
        writer.writerow(row)
