import numpy
import ROOT
from ROOT import *
import argparse
import math

parser = argparse.ArgumentParser(description='Plot Ratio of Trigger Efficiency.')

Title="trigDimuonEff"
ExtraInfo="BB"
#ExtraInfo="MC"

ranges=[
        "Z50To120",
        "Z120To200",
        "Z200To400",
        "Z400To800",
        "Z800To1400",
        "Z1400To2300",
        "Z2300To3500",
        "Z3500To4500",
        "Z4500To6000",
        "Z6000ToInf"
        ]

def plot(canvas,name):
    canvas.Print(name+".pdf","pdf")
#    canvas.Print(name+".png","png")
#    canvas.Print(name+".eps","eps")
#    canvas.Print(name+".root","root")

def setStyle(hist,value):
    hist.SetLineColor(value)
    hist.SetMarkerColor(value)
    if (value==kBlack): hist.SetMarkerStyle(20)
    if (value==kRed): hist.SetMarkerStyle(21)
    if (value==kBlue): hist.SetMarkerStyle(22)
    if (value==kGreen+3): hist.SetMarkerStyle(23)
    hist.SetMarkerSize(0.8)

gStyle.SetOptStat("")
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

masterAllBBMC=ROOT.TH1D("masterAllBBMC","masterAllBBMC",10000,0.0,10000.0)
masterPassBBMC=ROOT.TH1D("masterPassBBMC","masterPassBBMC",10000,0.0,10000.0)
masterAllNonBBMC=ROOT.TH1D("masterAllNonBBMC","masterAllNonBBMC",10000,0.0,10000.0)
masterPassNonBBMC=ROOT.TH1D("masterPassNonBBMC","masterPassNonBBMC",10000,0.0,10000.0)

masterAllBBData=ROOT.TH1D("masterAllBBData","masterAllBBData",10000,0.0,10000.0)
masterPassBBData=ROOT.TH1D("masterPassBBData","masterPassBBData",10000,0.0,10000.0)
masterAllNonBBData=ROOT.TH1D("masterAllNonBBData","masterAllNonBBData",10000,0.0,10000.0)
masterPassNonBBData=ROOT.TH1D("masterPassNonBBData","masterPassNonBBData",10000,0.0,10000.0)

for mass in ranges:
    fileNameMC="Hist-20170408MC_"+mass+".root"
    fMC=ROOT.TFile(fileNameMC)
    allBBMC=ROOT.gDirectory.Get("DimuonMassBB")
    allNonBBMC=ROOT.gDirectory.Get("DimuonMassNonBB")
    allBBDimuonsMC=ROOT.TH1D(allBBMC)
    allNonBBDimuonsMC=ROOT.TH1D(allNonBBMC)
    passingBBMC=ROOT.gDirectory.Get("DimuonMassPassBB")
    passingNonBBMC=ROOT.gDirectory.Get("DimuonMassPassNonBB")
    passBBDimuonsMC=ROOT.TH1D(passingBBMC)
    passNonBBDimuonsMC=ROOT.TH1D(passingNonBBMC)
    masterAllBBMC.Add(allBBDimuonsMC)
    masterPassBBMC.Add(passBBDimuonsMC)
    masterAllNonBBMC.Add(allNonBBDimuonsMC)
    masterPassNonBBMC.Add(passNonBBDimuonsMC)

#    fileNameData="Hist-20170408Data_"+mass+".root"
    fileNameData="Hist-20170416DataOscar_"+mass+".root"
    fData=ROOT.TFile(fileNameData)
    allBBData=ROOT.gDirectory.Get("DimuonMassBB")
    allNonBBData=ROOT.gDirectory.Get("DimuonMassNonBB")
    allBBDimuonsData=ROOT.TH1D(allBBData)
    allNonBBDimuonsData=ROOT.TH1D(allNonBBData)
    passingBBData=ROOT.gDirectory.Get("DimuonMassPassBB")
    passingNonBBData=ROOT.gDirectory.Get("DimuonMassPassNonBB")
    passBBDimuonsData=ROOT.TH1D(passingBBData)
    passNonBBDimuonsData=ROOT.TH1D(passingNonBBData)
    masterAllBBData.Add(allBBDimuonsData)
    masterPassBBData.Add(passBBDimuonsData)
    masterAllNonBBData.Add(allNonBBDimuonsData)
    masterPassNonBBData.Add(passNonBBDimuonsData)

xmax=8000.0
massBins=numpy.array(
[0, 50.0, 120.0,
    200.0, 400.0,
    800.0, 1400.0,
    2300.0, 3500.0,
    4500.0, 6000.0,
    8000.0]
)

nMassBin=len(massBins)-1

masterAllBBMC.Rebin(nMassBin,"MasterAllBBMC",massBins)
allBBMC=ROOT.gDirectory.Get("MasterAllBBMC")
dAllBBMC=ROOT.TH1D(allBBMC)
masterPassBBMC.Rebin(nMassBin,"MasterPassBBMC",massBins)
passedBBMC=ROOT.gDirectory.Get("MasterPassBBMC")
nPassedBBMC=ROOT.TH1D(passedBBMC)

masterAllBBData.Rebin(nMassBin,"MasterAllBBData",massBins)
allBBData=ROOT.gDirectory.Get("MasterAllBBData")
dAllBBData=ROOT.TH1D(allBBData)
masterPassBBData.Rebin(nMassBin,"MasterPassBBData",massBins)
passedBBData=ROOT.gDirectory.Get("MasterPassBBData")
nPassedBBData=ROOT.TH1D(passedBBData)

masterAllNonBBMC.Rebin(nMassBin,"MasterAllNonBBMC",massBins)
allNonBBMC=ROOT.gDirectory.Get("MasterAllNonBBMC")
dAllNonBBMC=ROOT.TH1D(allNonBBMC)
masterPassNonBBMC.Rebin(nMassBin,"MasterPassNonBBMC",massBins)
passedNonBBMC=ROOT.gDirectory.Get("MasterPassNonBBMC")
nPassedNonBBMC=ROOT.TH1D(passedNonBBMC)

masterAllNonBBData.Rebin(nMassBin,"MasterAllNonBBData",massBins)
allNonBBData=ROOT.gDirectory.Get("MasterAllNonBBData")
dAllNonBBData=ROOT.TH1D(allNonBBData)
masterPassNonBBData.Rebin(nMassBin,"MasterPassNonBBData",massBins)
passedNonBBData=ROOT.gDirectory.Get("MasterPassNonBBData")
nPassedNonBBData=ROOT.TH1D(passedNonBBData)

effBBMC = ROOT.TEfficiency(nPassedBBMC,dAllBBMC)
setStyle(effBBMC,kRed)
effNonBBMC = ROOT.TEfficiency(nPassedNonBBMC,dAllNonBBMC)
setStyle(effNonBBMC,kRed)
effBBData = ROOT.TEfficiency(nPassedBBData,dAllBBData)
setStyle(effBBData,kBlack)
effNonBBData = ROOT.TEfficiency(nPassedNonBBData,dAllNonBBData)
setStyle(effNonBBData,kBlack)

cBB = TCanvas("cBB", "cBB", 700, 700)
cBB.Divide(1,2)
padTopBB = TPad("padTopBB", "padTopBB",0,0.3,1.0,1.0)
padBottomBB = TPad("padBottomBB", "padBottomBB",0,0,1.0,0.3)
padTopBB.SetBottomMargin(0)
padTopBB.SetLeftMargin(0.14)
padTopBB.Draw()
padTopBB.cd()

title=";;Trigger Efficiency"
effBBData.SetTitle(title)
effBBData.Draw("")
effBBData.Paint("")
effBBData.GetPaintedGraph().GetXaxis().SetTitleOffset(1.2)
effBBData.GetPaintedGraph().GetYaxis().SetTitleOffset(1.4)
effBBData.GetPaintedGraph().GetYaxis().SetLabelSize(0.045)   #numbers 0.035 for just 1 pad
effBBData.GetPaintedGraph().GetYaxis().SetTitleSize(0.05)   #text 0.04 for just 1 pad
effBBData.GetPaintedGraph().GetXaxis().SetRangeUser(0.0,xmax)
#effBBData.GetPaintedGraph().GetYaxis().SetRangeUser(0.958,1.002)
effBBData.GetPaintedGraph().GetYaxis().SetRangeUser(0.978,1.002)
effBBMC.Draw("same")

legBB = ROOT.TLegend(0.40,0.05,0.85,0.2)
legBB.AddEntry(effBBMC,"BB from MC","pl")
#legBB.AddEntry(effBBData,"BB from Data","pl")
legBB.AddEntry(effBBData,"BB from Data (W')","pl")
legBB.SetTextFont(42)
legBB.SetTextSize(0.04)
legBB.SetMargin(0.15)
legBB.SetFillColor(0)
legBB.SetLineColor(1)
legBB.SetLineStyle(1)
legBB.SetLineWidth(0)
legBB.Draw("hist")

cBB.cd();
padBottomBB.SetTopMargin(0)
padBottomBB.SetLeftMargin(0.14)
padBottomBB.SetBottomMargin(0.3)
padBottomBB.Draw()
padBottomBB.cd()
padBottomBB.SetGrid()


ratioEffBB=ROOT.TH1D("ratioEffBB","ratioEffBB",nMassBin,massBins)
effBB=ROOT.TH1D("effBB","effBB",nMassBin,massBins)
for i in range(2,nMassBin+1):
    SF=effBBData.GetEfficiency(i)/effBBMC.GetEfficiency(i)
    ratioEffBB.SetBinContent(i,SF)
    SigmaData=(effBBData.GetEfficiencyErrorUp(i)+effBBData.GetEfficiencyErrorLow(i))/2.0
    SigmaMC=(effBBMC.GetEfficiencyErrorUp(i)+effBBMC.GetEfficiencyErrorLow(i))/2.0
    RatioData=SigmaData/effBBData.GetEfficiency(i)
    RatioMC=SigmaMC/effBBMC.GetEfficiency(i)
    RatioError=SF*math.sqrt(RatioData*RatioData+RatioMC*RatioMC)
    ratioEffBB.SetBinError(i,RatioError)
    print "bin[",i,"]: Data: ",effBBData.GetEfficiency(i)," MC: ",effBBMC.GetEfficiency(i), " SF = ",SF," SigmaData: ",SigmaData," SigmaMC: ",SigmaMC," RatioError: ",RatioError


ratioEffBB.SetTitle(";Generated Dimuon Mass (GeV); Data/MC")
ratioEffBB.GetXaxis().SetRangeUser(0.0,xmax)
ratioEffBB.GetXaxis().SetLabelFont(42)
ratioEffBB.GetXaxis().SetTitleSize(0.1)
ratioEffBB.GetXaxis().SetLabelSize(0.1)
ratioEffBB.GetXaxis().SetTitleOffset(0.8)
ratioEffBB.GetXaxis().SetTitleOffset(1.3)

ratioEffBB.GetXaxis().SetTitleFont(42)
ratioEffBB.GetYaxis().SetTitleSize(0.12)
ratioEffBB.GetYaxis().SetLabelSize(0.1)
#ratioEffBB.GetYaxis().SetRangeUser(0.9955,1.0005); #Z'
ratioEffBB.GetYaxis().SetRangeUser(0.9965,1.0025); #W'
ratioEffBB.GetYaxis().SetNdivisions(509)
ratioEffBB.GetYaxis().SetLabelFont(42)
ratioEffBB.GetYaxis().SetTitleOffset(0.6)
ratioEffBB.GetYaxis().SetTitleFont(42)

#fcnBB = ROOT.TF1('fcnBB', 'pol1',0.0, xmax) #BB
#fcnBB.SetParameters(0.998, -6.25e-08) #BB
#fcnBB.SetLineColor(ROOT.kRed)
#ratioEffBB.Fit(fcnBB, 'L')
#
#print "fcnBB: ",('%.3e' % fcnBB.GetParameter(0))," ",('%.3e' % fcnBB.GetParameter(1))

setStyle(ratioEffBB,kBlack)
ratioEffBB.Draw("P")
#ratioEff.Draw("PE")

plot(cBB,Title+ExtraInfo)


cNonBB = TCanvas("cNonBB", "cNonBB", 700, 700)
cNonBB.Divide(1,2)
padTopNonBB = TPad("padTopNonBB", "padTopNonBB",0,0.3,1.0,1.0)
padBottomNonBB = TPad("padBottomNonBB", "padBottomNonBB",0,0,1.0,0.3)
padTopNonBB.SetBottomMargin(0)
padTopNonBB.SetLeftMargin(0.14)
padTopNonBB.Draw()
padTopNonBB.cd()

title=";;Trigger Efficiency"
effNonBBData.SetTitle(title)
effNonBBData.Draw("")
effNonBBData.Paint("")
effNonBBData.GetPaintedGraph().GetXaxis().SetTitleOffset(1.2)
effNonBBData.GetPaintedGraph().GetYaxis().SetTitleOffset(1.4)
effNonBBData.GetPaintedGraph().GetYaxis().SetLabelSize(0.045)   #numbers 0.035 for just 1 pad
effNonBBData.GetPaintedGraph().GetYaxis().SetTitleSize(0.05)   #text 0.04 for just 1 pad
effNonBBData.GetPaintedGraph().GetXaxis().SetRangeUser(0.0,xmax)
effNonBBData.GetPaintedGraph().GetYaxis().SetRangeUser(0.978,1.002)
effNonBBMC.Draw("same")

legNonBB = ROOT.TLegend(0.40,0.05,0.85,0.2)
legNonBB.AddEntry(effNonBBMC,"NonBB from MC","pl")
#legNonBB.AddEntry(effNonBBData,"NonBB from Data","pl")
legNonBB.AddEntry(effNonBBData,"NonBB from Data (W')","pl")
legNonBB.SetTextFont(42)
legNonBB.SetTextSize(0.04)
legNonBB.SetMargin(0.15)
legNonBB.SetFillColor(0)
legNonBB.SetLineColor(1)
legNonBB.SetLineStyle(1)
legNonBB.SetLineWidth(0)
legNonBB.Draw("hist")

cNonBB.cd();
padBottomNonBB.SetTopMargin(0)
padBottomNonBB.SetLeftMargin(0.14)
padBottomNonBB.SetBottomMargin(0.3)
padBottomNonBB.Draw()
padBottomNonBB.cd()
padBottomNonBB.SetGrid()

ratioEffNonBB=ROOT.TH1D("ratioEffNonBB","ratioEffNonBB",nMassBin,massBins)
effNonBB=ROOT.TH1D("effNonBB","effNonBB",nMassBin,massBins)
for i in range(2,nMassBin+1):
    SF=effNonBBData.GetEfficiency(i)/effNonBBMC.GetEfficiency(i)
    SigmaData=(effNonBBData.GetEfficiencyErrorUp(i)+effNonBBData.GetEfficiencyErrorLow(i))/2.0
    SigmaMC=(effNonBBMC.GetEfficiencyErrorUp(i)+effNonBBMC.GetEfficiencyErrorLow(i))/2.0
    RatioData=SigmaData/effNonBBData.GetEfficiency(i)
    RatioMC=SigmaMC/effNonBBMC.GetEfficiency(i)
    RatioError=SF*math.sqrt(RatioData*RatioData+RatioMC*RatioMC)
    print "bin[",i,"]: Data: ",effNonBBData.GetEfficiency(i)," MC: ",effNonBBMC.GetEfficiency(i), " SF = ",SF," SigmaData: ",SigmaData," SigmaMC: ",SigmaMC," RatioError: ",RatioError
    ratioEffNonBB.SetBinContent(i,SF)
#    ratioEffNonBB.SetBinError(i, (1./effNonBBMC.GetEfficiency(i)) * TMath.Sqrt(effNonBBData.GetEfficiency(i) * (1 - effNonBBData.GetEfficiency(i)/effNonBBMC.GetEfficiency(i))) )
    ratioEffNonBB.SetBinError(i,RatioError)

ratioEffNonBB.SetTitle(";Generated Dimuon Mass (GeV); Data/MC")
ratioEffNonBB.GetXaxis().SetRangeUser(0.0,xmax)
ratioEffNonBB.GetXaxis().SetLabelFont(42)
ratioEffNonBB.GetXaxis().SetTitleSize(0.1)
ratioEffNonBB.GetXaxis().SetLabelSize(0.1)
ratioEffNonBB.GetXaxis().SetTitleOffset(0.8)
ratioEffNonBB.GetXaxis().SetTitleOffset(1.3)

ratioEffNonBB.GetXaxis().SetTitleFont(42)
ratioEffNonBB.GetYaxis().SetTitleSize(0.12)
ratioEffNonBB.GetYaxis().SetLabelSize(0.1)
#ratioEffNonBB.GetYaxis().SetRangeUser(0.9915,0.9975); #Z'
ratioEffNonBB.GetYaxis().SetRangeUser(0.9965,1.0035); #W'
ratioEffNonBB.GetYaxis().SetNdivisions(509)
ratioEffNonBB.GetYaxis().SetLabelFont(42)
ratioEffNonBB.GetYaxis().SetTitleOffset(0.6)
ratioEffNonBB.GetYaxis().SetTitleFont(42)

#fcnNonBB = ROOT.TF1('fcnNonBB', 'pol1',0.0, xmax) #NonBB
#fcnNonBB.SetParameters(0.998, -6.25e-08) #NonBB
#fcnNonBB.SetLineColor(ROOT.kRed)
#ratioEffNonBB.Fit(fcnNonBB, 'L')
#print "fcnNonBB: ",('%.3e' % fcnNonBB.GetParameter(0))," ",('%.3e' % fcnNonBB.GetParameter(1))

setStyle(ratioEffNonBB,kBlack)
ratioEffNonBB.Draw("P")
#ratioEffNonBB.Draw("PE")

ExtraInfo="NonBB"
plot(cNonBB,Title+ExtraInfo)

