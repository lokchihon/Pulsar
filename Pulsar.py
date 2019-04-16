# This script runs by first setting the attributes of a pulsar as it's variables to be used later
# Then, based on variables being input from our GUI will edit the common file and the file corresponding
# to the type of star the user selects on the GUI
# Finally, This script will call the rsp program using the Unix command line
# Created by the Radiation Hydrodynamic Pulsar enthusiasts


class Pulsar:
    # Sets the parameters for a pulsar object
    def __init__(self, m, lum, x, z, crr, maxA, maxP, temp):
        self.mass = m
        self.luminosity = lum
        self.xComp = x
        self.zComp = z
        self.cOrRR = crr
        self.maxAmp = maxA
        self.maxPeriodNum = maxP
        self.temperature = temp


# Variables are to be updated by the GUI. This will automatically update the pulsar1 object variables
# along with the chosen file when the script is run.

# Andrew, this is the area you're concerned with
mass = 42.5
lum = 251.3
x = 45.2
z = 42.3
corr = "C"
maxA = 45.4
maxP = 46.8
temp = 47.9

# Pulsar object
pulsar1 = Pulsar(mass, lum, x, z, corr, maxA, maxP, temp)

# edit common file
filePath = "common.txt"  # File path for Common File here
ogFilePath = "ogCommon.txt"  # Duplicate file path for Common File here
commonFile = open(filePath, "w")
ogCommon = open(ogFilePath, "r")

# Takes input from duplicate file and scans it, then writes it to the file we are editing.
# If we don't do this, then everything leading up to our variables is deleted
for ln in range(0, 11):
    commonScan = ogCommon.readline()
    commonFile.write("%s" % commonScan)
ogCommon.readline()
# This statement processes the equivalent line in ogCommon file to the line we are editing in
# working common file  edit our variables in the common file file
commonFile.write("Max Amplitude %f\n" % pulsar1.maxAmp)
ogCommon.readline()
commonFile.write("Max Period: %f\n" % pulsar1.maxPeriodNum)
ogCommon.readline()
commonFile.write("Star Type: %s\n" % pulsar1.cOrRR)

# Find end of file so I can scan from the original file and write it to the file we are editing
# If we don't do this it will delete everything after our variables
scanned = ogCommon.readline()
while scanned != "":
    commonFile.write("%s" % scanned)
    scanned = ogCommon.readline()

# close files
commonFile.close()
ogCommon.close()


# check which file is used and edit
if pulsar1.cOrRR == "RR":
    filePath = "RR.txt"  # File path for cepheid here
    ogFilePath = "Allstar.txt"  # Duplicate file path for Cepheid here
    file = open(filePath, "w")
    ogFile = open(ogFilePath, "r")

    # Takes input from duplicate file and scans it, then writes it to the file we are editing.
    # If we don't do this, then everything leading up to our variables is deleted
    for line in range(0, 11):
        scanned = ogFile.readline()
        file.write("%s" % scanned)
    ogFile.readline()
    # edit the variables in our RR_Leary file
    file.write("Mass: %f \n" % pulsar1.mass)
    ogFile.readline()  # This statement processes the equivalent line in ogFile to the line we are editing in file
    file.write("Luminosity: %f\n" % pulsar1.luminosity)
    ogFile.readline()
    file.write("X Component: %f\n" % pulsar1.xComp)
    ogFile.readline()
    file.write("Z Component %f\n" % pulsar1.zComp)
    ogFile.readline()
    file.write("Temperature: %f\n" % pulsar1.temperature)

    # Find end of file so I can scan from the original file and write it to the file we are editing
    # If we don't do this it will delete everything after our variables
    scanned = ogFile.readline()
    while scanned != "":
        file.write("%s" % scanned)
        scanned = ogFile.readline()

    # close files
    file.close()
    ogFile.close()
    
elif pulsar1.cOrRR == "C":
    filePath = "C.txt"  # File path for cepheid here
    ogFilePath = "Allstar.txt"  # Duplicate file path for Cepheid here
    file = open(filePath, "w")
    ogFile = open(ogFilePath, "r")

    # Takes input from duplicate file and scans it, then writes it to the file we are editing.
    # If we don't do this, then everything leading up to our variables is deleted
    for line in range(0, 11):
        scanned = ogFile.readline()
        file.write("%s" % scanned)
    ogFile.readline()  # This statement processes the equivalent line in ogFile to the line we are editing in file
    # edit the our variables in the Cepheid files
    file.write("Mass: %f \n" % pulsar1.mass)
    ogFile.readline()
    file.write("Luminosity: %f\n" % pulsar1.luminosity)
    ogFile.readline()
    file.write("X Component: %f\n" % pulsar1.xComp)
    ogFile.readline()
    file.write("Z Component %f\n" % pulsar1.zComp)
    ogFile.readline()
    file.write("Temperature: %f\n" % pulsar1.temperature)

    # Find end of duplicate file so I can scan from the original file and write it to the file we are
    # editing If we don't do this it will delete everything after our variables
    scanned = ogFile.readline()
    while scanned != "":
        file.write("%s" % scanned)
        scanned = ogFile.readline()
    # Close files
    file.close()
    ogFile.close()
    


