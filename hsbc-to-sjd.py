#!/usr/bin/env python

import csv
import datetime
import re
import sys

moneypattern = re.compile("[0-9]+\.[0-9]+")

with sys.stdin as csvfile:
    transactions = csv.reader(csvfile)
    for row in transactions:
        if (row[0] != "Date"):
            transdate = datetime.datetime.strptime(row[0], "%d %b %Y").strftime("%d/%m/%Y")

            amount = 0.00
            if moneypattern.match(row[4]):
                amount += float(row[4])
            if moneypattern.match(row[3]):
                amount -= float(row[3])

            out = "%s,%s,%.2f,\r" % (transdate, row[2], amount)
            print out
