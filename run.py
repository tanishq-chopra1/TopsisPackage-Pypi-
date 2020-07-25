from Topsis_package import pro
import sys
file=sys.argv[1]
wt=sys.argv[2].split(",")
im=sys.argv[3].split(",")
pro.topsis(file,wt,im)