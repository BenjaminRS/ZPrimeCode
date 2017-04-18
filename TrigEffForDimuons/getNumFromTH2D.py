import numpy
import ROOT
from ROOT import *
import argparse

f=ROOT.TFile("/afs/cern.ch/user/b/benjamin/public/ZPrime/eff_absetaptpog2D_massbinned.root")"
#f=ROOT.TFile("eff_absetaptpog2D_massbinned.root")

plot=ROOT.gDirectory.Get("sf_2d")
xrange=plot.GetNbinsX()+1
yrange=plot.GetNbinsY()+1

#z'
#eta bins: 0, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4
#pt bins: 0, 100, 200, 500, inf

#w'
#eta bins: 0, 0.9, 1.2, 2.1, 2.4
#pt bins: 0, 300, 800, inf

#for y in range(1,yrange): #eta
#    for x in range(1,xrange): #pt
#        print "(x",x,",y",y,"): ",plot.GetBinContent(x,y)
#    print ""

matrix=[]

row1=[] #53-120 GeV
#for y in range(1,yrange): #eta
ptBin1Temp=0.0
for x in range(1,5): #pt bin1
    ptBin1Temp+=plot.GetBinContent(x,1)
ptBin1=ptBin1Temp/4.0
#print "ptBin1 eta(",y,"):",ptBin1
row1.append(ptBin1)
row1.append(ptBin1)
row1.append(ptBin1)

ptBin1Temp=ptBin1=0.0
for x in range(1,5): #pt bin1
    ptBin1Temp+=plot.GetBinContent(x,2)
ptBin1=ptBin1Temp/4.0
row1.append(ptBin1)

ptBin1Temp=ptBin1=0.0
for x in range(1,5): #pt bin1
    ptBin1Temp+=plot.GetBinContent(x,3)
ptBin1=ptBin1Temp/4.0
row1.append(ptBin1)
row1.append(ptBin1)

ptBin1Temp=ptBin1=0.0
for x in range(1,5): #pt bin1
    ptBin1Temp+=plot.GetBinContent(x,4)
ptBin1=ptBin1Temp/4.0
row1.append(ptBin1)
#print row1

matrix.append(row1)

row2=[] #120-200 GeV
row2.append(plot.GetBinContent(5,1))
row2.append(plot.GetBinContent(5,1))
row2.append(plot.GetBinContent(5,1))
row2.append(plot.GetBinContent(5,2))
row2.append(plot.GetBinContent(5,3))
row2.append(plot.GetBinContent(5,3))
row2.append(plot.GetBinContent(5,4))
matrix.append(row2)

row3=[] #200-400 GeV
ptBin3Temp=0.0
for x in range(6,8): #pt bin3
    ptBin3Temp+=plot.GetBinContent(x,1)
ptBin3=ptBin3Temp/2.0
row3.append(ptBin3)
row3.append(ptBin3)
row3.append(ptBin3)

ptBin3Temp=0.0
for x in range(6,8): #pt bin3
    ptBin3Temp+=plot.GetBinContent(x,2)
ptBin3=ptBin3Temp/2.0
row3.append(ptBin3)

ptBin3Temp=0.0
for x in range(6,8): #pt bin3
    ptBin3Temp+=plot.GetBinContent(x,3)
ptBin3=ptBin3Temp/2.0
row3.append(ptBin3)
row3.append(ptBin3)

ptBin3Temp=0.0
for x in range(6,8): #pt bin3
    ptBin3Temp+=plot.GetBinContent(x,4)
ptBin3=ptBin3Temp/2.0
row3.append(ptBin3)
matrix.append(row3)


row4=[] #400- GeV
ptBin4Temp=0.0
for x in range(8,10): #pt bin4
    ptBin4Temp+=plot.GetBinContent(x,1)
ptBin4=ptBin4Temp/2.0
row4.append(ptBin4)
row4.append(ptBin4)
row4.append(ptBin4)

ptBin4Temp=0.0
for x in range(8,10): #pt bin4
    ptBin4Temp+=plot.GetBinContent(x,2)
ptBin4=ptBin4Temp/2.0
row4.append(ptBin4)

ptBin4Temp=0.0
for x in range(8,10): #pt bin4
    ptBin4Temp+=plot.GetBinContent(x,3)
ptBin4=ptBin4Temp/2.0
row4.append(ptBin4)
row4.append(ptBin4)

ptBin4Temp=0.0
for x in range(8,10): #pt bin4
    ptBin4Temp+=plot.GetBinContent(x,4)
ptBin4=ptBin4Temp/2.0
row4.append(ptBin4)
matrix.append(row4)

print matrix
#for row in matrix:
#    print row
