#!/usr/bin/python
# -*- coding: utf-8 -*-
import struct

count = 0
with open('missingptable.img', 'rb') as f:
    while True:
        data = f.read(512)
        if data[3:7] == 'NTFS':
            print 'Match NTFS| Sector = ', count
            size = struct.unpack('<L', data[40:44])
            print 'Size =', size[0]
        elif data[56:58] == "\x53\xEF":
            print 'Match Linux| Sector = ', count
        elif data[510:512] == "\x55\xAA":
            print 'Match MBR| Sector = ', count

        count += 1

			
