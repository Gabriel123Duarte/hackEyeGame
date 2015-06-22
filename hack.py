# http://wvw.igame.com/eye-test/

import pyscreenshot as ImageGrab
import pyautogui
import math
from PIL import Image
from time import sleep

rect = [788, 342, 1107, 659]
cont = 0
divisor = 2

maximo = int(input("Digite quantos pontos deseja: "))

while cont < maximo:
	im = ImageGrab.grab(bbox = rect).convert('L')
	im.show()

	print im
	pixels = list(im.getdata())
	width, height = im.size
	pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

	#print len(pixels)

	pixelMaior = []
	ultimo = []
	aux = 0			
	maior = 0
	
	total = [0] * 256
	
	for i in range(0, height - 1):
		for j in range(0, width - 1):
			if pixels[i][j] >= 250:
				continue
			total[pixels[i][j]] += 1
			if total[pixels[i][j]] > maior:
				maior = total[pixels[i][j]]
				pixelMaior = pixels[i][j]
					
	segundoMaior = xClique = yClique = 0
	
	for i in range(0, height - 1):
		for j in range(0, width - 1):
			if total[pixels[i][j]] > segundoMaior and total[pixels[i][j]] <= maior / divisor:
				#pixelMaior = pixels[i][j]
				if pixels[i][j - 1] == pixels[i][j + 1] == pixels[i][j]: 
					segundoMaior = total[pixels[i][j]]
					xClique = j
					yClique = i
					
	print "Segundo " + str(segundoMaior)
	
	#pyautogui.click(x = xClique + rect[0], y = yClique + rect[1])	
	pyautogui.moveTo(xClique + rect[0], yClique + rect[1])	
	sleep(.1)
	pyautogui.click()
	sleep(.1)
	pyautogui.moveTo(100, 100)	
	sleep(.1)
	cont += 1
	if cont % 3 == 0:
		divisor += 1
	if cont % 20 == 0:
		divisor = 2
		sleep(1)
