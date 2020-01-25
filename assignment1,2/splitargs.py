#copyright 2019 Dingjun Bian braybian@bu.edu
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

a=sys.argv
l=len(sys.argv)
for i in a[1:5]:     
      sys.stdout.write(i)
      sys.stdout.write('\n')
for i in a[5:l+1]:
      sys.stderr.write(i)
      sys.stderr.write('\n')
