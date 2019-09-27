import random
import arcpy
from arcpy import env
import math
arcpy.env.overwriteOutput = True

min = arcpy.GetParameter(0)
max = arcpy.GetParameter(1)
d = arcpy.GetParameter(2)
n = arcpy.GetParameter(3)
D = int(d)
a = int(min)
b = int(max)
N = int(n)
titik = []
point = []
for i in range (3):
    x = random.randrange(a, b)
    titik.append(x)

point.append(titik)
titik = []
I = 1
J = 0
jarak = []
while I < N :
    for i in range (3):
        x = random.randrange(a, b)
        titik.append(x)
    coba = point[J]
    pg1 = arcpy.PointGeometry(arcpy.Point(coba[0], coba[1], coba[2]))
    pg2 = arcpy.PointGeometry(arcpy.Point(titik[0], titik[1], titik[2]))
    P = pg1.distanceTo(pg2)
        
    if P >= D:
        I += 1
        point.append(titik)
        titik = []
        jarak.append(P)
    else:
        titik = []

Y = len(point)

K = 1
L = 2
while K < Y :
    L = K + 1
    while L < Y :
        coba = point[K]
        banding = point[L] 
        pg1 = arcpy.PointGeometry(arcpy.Point(coba[0], coba[1], coba[2]))
        pg2 = arcpy.PointGeometry(arcpy.Point(banding[0], banding[1], banding[2]))
        P = pg1.distanceTo(pg2)
        if P >= D:
            L += 1
            K += 1
        else:
            for i in range (3):
                x = random.randrange(a, b)
                titik.append(x)
            point[L] = titik
            


    K += 1


    

    


print point
h = 0
koor = point
pglist = []
for x,y,z in koor:
    pt = arcpy.Point(x,y,z)
    pg = arcpy.PointGeometry(pt)
    pglist.append(pg)

out = arcpy.GetParameterAsText(4)
arcpy.CopyFeatures_management(pglist, out)





        
    


     
    