from PIL import Image
import csv
import sunmath
import random
import sys

fieldnames = []
alpha = [34.7,68.9]

print(sys.argv[1])
im = Image.open(sunmath.calc(sys.argv[1],alpha))
width, height = im.size
rgb_im = im.convert('RGB')

with open('names.csv', 'w', newline='') as csvfile:

	for k in range(1,width):
		fieldnames.append('V'+str(k)) 
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

	for j in range(1,height):
		wer = {}
		for i in range(1,width):
			r, g, b = rgb_im.getpixel((i, j))
			wer['V'+str(i)] = 255-g
		writer.writerow(wer)