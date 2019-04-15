class Pulsar:

    def __init__(self, m, lum, x, z, crr, maxA, maxP, temp):
        self.mass = m
        self.luminosity = lum
        self.xComp = x
        self.zComp = z
        self.cOrRR = crr
        self.maxAmp = maxA
        self.maxPeriodNum = maxP
        self.temperature = temp


pulsar1 = Pulsar(44, 201, 42, 42.3, "C", 45, 46, 47)  # sample pulsar that has nothing in common with a real one

if pulsar1.cOrRR == "RR":
    print("RR")
elif pulsar1.cOrRR == "C":
    print("C")
