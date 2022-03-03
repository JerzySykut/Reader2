import pathlib
import json
import csv
import pickle
from os import path

class Reader(object):
	data: list
	def __init__(self) -> None:
		self.data = list()
	#zwraca true jeśli udało się załadować plik, false jeśli nie
	def loadFromFile(self, pathToFile: str) -> bool:
		# Sprawdzamy czy istnieje katalog/plik
		if path.exists(pathToFile):
			# sprawadzamy czy to jest plik
			if path.isfile(pathToFile):
				# otwieramy plik
				splitName = path.splitext(pathToFile)
				if splitName[1] == '.csv':
					with open(pathToFile, newline="") as f:
						rdr = csv.reader(f,delimiter=';')
						for line in rdr:
							self.data.append(line)
						return True
				elif splitName[1] == '.json':
					with open(pathToFile, newline="") as f:
						self.data = json.load(f)
					return True
				elif splitName[1] == '.pickle':
					with open(pathToFile, 'rb') as f:
						self.data = pickle.load(f)
					return True
				else:
					print('Nieznane/nieobsługiwane rozszerzenie pliku!!!')
					return False
			else:
				# istnieje a to nie jest plik czyli katalog
				folder = pathlib.Path(pathToFile)
				for f in folder.glob('*.csv'):
					print(f)
				for f in folder.glob('*.json'):
					print(f)
				for f in folder.glob('*.pickle'):
					print(f)
				return False
		else:
			# wyciągamy nazwe katalogu (Folderu)
			pathDir = path.dirname(pathToFile)
			# sprawdzamy czy istnieje i czy jest folderem(nie jest plikien)
			if path.exists(pathDir) and path.isfile(pathDir) == False:
				folder = pathlib.Path(pathToFile)
				# wyswietlamy wszystkie pliki w Katalogu (Folderze)
				for f in folder.glob('*.csv'):
					print(f)
				for f in folder.glob('*.json'):
					print(f)
				for f in folder.glob('*.pickle'):
					print(f)
			else:
				print("Nie istnieje plik lub folder pod podana sciezka")	#nie istnieje
			return False
	def printData(self) -> None:
		print(*self.data, sep='\n')
	def setValue(self, x: int, y: int, val: str) -> None:
		if y >= len(self.data) or x >= len(self.data[y]):
				print("Wspolrzedne poza rozmiaru tablicy")
		else:
			self.data[y][x] = val
	def saveToFile(self, pathToFile: str):
		splitName = path.splitext(pathToFile)
		if splitName[1] == '.csv':
			with open(pathToFile, "w", newline="") as f:
				wrtr = csv.writer(f,delimiter=';')
				for line in self.data:
					wrtr.writerow(line)
		elif splitName[1] == '.json':
			with open(pathToFile, "w", newline="") as f:
				json.dump(self.data, f, indent=4)
		elif splitName[1] == '.pickle':
			with open(pathToFile, "wb") as f:
				pickle.dump(self.data, f)
		else:
			print('Nieznane/nieobsługiwane rozszerzenie pliku!!!')







