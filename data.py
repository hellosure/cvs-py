# coding: utf-8

import csv
import matplotlib.pyplot as plt
import numpy as np

readfile = file('data.csv', 'rb')
reader = csv.reader(readfile)

writefile = file('delta_user_num.csv','wb')
writer = csv.writer(writefile)
writer.writerow(['date','delta_user_num'])

for line in reader:
	writer.writerow([line[0],str(int(line[3])-int(line[4]))])

readfile.close() 