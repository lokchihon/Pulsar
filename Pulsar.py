
class Pulsar:


	def __init__(self, m = 42, lum=43, x=44, z=45, crr= 'RR', maxA=47, maxP= 48, temp= 49):
		self.mass = m
		self.luminosity = lum
		self.xComp= x
		self.zComp = z
		self.cOrRR = crr
		self.maxAmp = maxA
		self.maxPeriodNum = maxP
		self.temperature = temp


	def getMass(self):
		return self.mass

	def getLum(self):
		return self.luminosity

	def getX(self):
		return self.xComp

	def getCRR(self):
		return self.cOrRR

	def getTemp(self):
		return self.temp

	def getMaxAmp(self):
		return self.maxAmp

	def getMaxPeriodNum(self):
		return self.maxPeriodNum

	def editRRFile(self, mass, lum, x,z, temp, maxA, maxP):
		lines[7]={0,1,2,3,4,5,6}

	def editCommonFile(self, mass, lum, x,z, temp, maxA, maxP):
		lines[7] = {0, 1, 2, 3, 4, 5, 6}

	def editCepheidFile(self, mass, lum, x,z, temp, maxA, maxP):
		lines[7] = {0, 1, 2, 3, 4, 5, 6}
		return lines

	def main(self):
		lines = editCepheidFile()
		for x in lines:
			print(x)
	



		

