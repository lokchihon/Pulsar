class Pulsar:
	def _init_ (star, m, lum, x, z, crr,maxA,maxP, temp):
		star.mass = m
		star.luminosity = lum
		star.xComp= x
		star.zComp = z
		star.cOrRR = crr
		star.maxAmp = maxA
		star.maxPeriodNum = maxP
		star.temperature = temp
	def getMass():
		return mass
	def getLum():
		return luminosity
	def getX():
		return xComp
	def getCRR():
		return cOrRR
	def getTemp():
		return temp
	def getMaxAmp():
		return maxAmp
	def getMaxPeriodNum():
		return maxPeriodNum
	def toString():
		string toStr = " mass: " + mass + " luminosity " + luminosity + " X: " + xComp +" Z: " + zComp
		return toStr