#!/bin/sh

wget --reject-regex "((.*)\?(.*))" -l1 -m -np -c --content-disposition 'https://mediabiasfactcheck.com/center'
wget --reject-regex "((.*)\?(.*))" -l1 -m -np -c --content-disposition 'https://mediabiasfactcheck.com/left'
wget --reject-regex "((.*)\?(.*))" -l1 -m -np -c --content-disposition 'https://mediabiasfactcheck.com/leftcenter'
wget --reject-regex "((.*)\?(.*))" -l1 -m -np -c --content-disposition 'https://mediabiasfactcheck.com/right'
wget --reject-regex "((.*)\?(.*))" -l1 -m -np -c --content-disposition 'https://mediabiasfactcheck.com/right-center'
wget --reject-regex "((.*)\?(.*))" -l1 -m -np -c --content-disposition 'https://mediabiasfactcheck.com/conspiracy'
wget --reject-regex "((.*)\?(.*))" -l1 -m -np -c --content-disposition 'https://mediabiasfactcheck.com/fake-news'
wget --reject-regex "((.*)\?(.*))" -l1 -m -np -c --content-disposition 'https://mediabiasfactcheck.com/pro-science'
wget --reject-regex "((.*)\?(.*))" -l1 -m -np -c --content-disposition 'https://mediabiasfactcheck.com/satire'
