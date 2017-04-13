#!/bin/bash
import ROOT
from ROOT import TH1D,TFile,TVector3,TH2D
from DataFormats.FWLite import Events, Handle
from os import listdir
import math
from PhysicsTools.HeppyCore.utils.deltar import deltaR2

hAll=TH1D("AllMu","AllMu",5000,0,5000.0)
hPass=TH1D("PassMu","PassMu",5000,0,5000.0)
hPassNew=TH1D("PassNewMu","PassNewMu",5000,0,5000.0)
hPassRPC=TH1D("hPassRPC","hPassRPC",5000,0,5000.0)
hOldPtRes=TH1D("hOldPtRes","hOldPtRes",1000,-5.0,5.0)
hNewPtRes=TH1D("hNewPtRes","hNewPtRes",1000,-5.0,5.0)

hNewPtRes0To500=TH1D("hNewPtRes0To500","hNewPtRes0To500",1000,-5.0,5.0)
hNewPtRes500To1000=TH1D("hNewPtRes500To1000","hNewPtRes500To1000",1000,-5.0,5.0)
hNewPtRes1000To1500=TH1D("hNewPtRes1000To1500","hNewPtRes1000To1500",1000,-5.0,5.0)
hNewPtRes1500Up=TH1D("hNewPtRes1500Up","hNewPtRes1500Up",1000,-5.0,5.0)

hOldPtRes0To500=TH1D("hOldPtRes0To500","hOldPtRes0To500",1000,-5.0,5.0)
hOldPtRes500To1000=TH1D("hOldPtRes500To1000","hOldPtRes500To1000",1000,-5.0,5.0)
hOldPtRes1000To1500=TH1D("hOldPtRes1000To1500","hOldPtRes1000To1500",1000,-5.0,5.0)
hOldPtRes1500Up=TH1D("hOldPtRes1500Up","hOldPtRes1500Up",1000,-5.0,5.0)


handle  = Handle ("std::vector<reco::Muon>")
label = ("muons","","RECO")
vHandle = Handle ("std::vector<reco::Vertex>")
vLabel = ("offlinePrimaryVertices","","RECO")
trigHandle = Handle ("trigger::TriggerEvent")
trigLabel = ("hltTriggerSummaryAOD","","HLT")
genHandle = Handle ("std::vector<reco::GenParticle>")
genLabel = ("genParticles","","HLT")

dirs=['foo']
#files=['/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_4_15/src/Skim/SelectEvents/test/ZPrimeOfInterest_DYMC2300to3500Fail.root']
#files=['/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_4_15/src/Skim/SelectEvents/test/ZPrimeOfInterest_DYMC2300to3500FailAllInfo.root']
#files=[
##        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_4_15/src/Skim/SelectEvents/test/ZPrimeOfInterest_DYMC2300to3500FailAllInfo.root'
#       'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/ZToMuMu_NNPDF30_13TeV-powheg_M_2300_3500/AODSIM/Startup25ns_EXOReReco_74X_Spring15_mcRun2_startup25ns_v0-v1/80000/0412FBD4-567C-E511-AB02-E41D2D08DD60.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/ZToMuMu_NNPDF30_13TeV-powheg_M_2300_3500/AODSIM/Startup25ns_EXOReReco_74X_Spring15_mcRun2_startup25ns_v0-v1/80000/10DFC390-8379-E511-AA77-0025905A6132.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/ZToMuMu_NNPDF30_13TeV-powheg_M_2300_3500/AODSIM/Startup25ns_EXOReReco_74X_Spring15_mcRun2_startup25ns_v0-v1/80000/12D7FAD4-567C-E511-994E-0025907DC9D6.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/ZToMuMu_NNPDF30_13TeV-powheg_M_2300_3500/AODSIM/Startup25ns_EXOReReco_74X_Spring15_mcRun2_startup25ns_v0-v1/80000/420C1AE7-567C-E511-BF1F-00266CFFA704.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/ZToMuMu_NNPDF30_13TeV-powheg_M_2300_3500/AODSIM/Startup25ns_EXOReReco_74X_Spring15_mcRun2_startup25ns_v0-v1/80000/58AA59C1-567C-E511-8D74-E41D2D08DDD0.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/ZToMuMu_NNPDF30_13TeV-powheg_M_2300_3500/AODSIM/Startup25ns_EXOReReco_74X_Spring15_mcRun2_startup25ns_v0-v1/80000/786D6891-8379-E511-AC3D-003048FFD76E.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/ZToMuMu_NNPDF30_13TeV-powheg_M_2300_3500/AODSIM/Startup25ns_EXOReReco_74X_Spring15_mcRun2_startup25ns_v0-v1/80000/AEC11FD4-567C-E511-A1CE-002590DB91C6.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/ZToMuMu_NNPDF30_13TeV-powheg_M_2300_3500/AODSIM/Startup25ns_EXOReReco_74X_Spring15_mcRun2_startup25ns_v0-v1/80000/C82B24D3-567C-E511-9621-F45214938690.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/ZToMuMu_NNPDF30_13TeV-powheg_M_2300_3500/AODSIM/Startup25ns_EXOReReco_74X_Spring15_mcRun2_startup25ns_v0-v1/80000/D43EB0D2-567C-E511-8495-002590AC4C7C.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/ZToMuMu_NNPDF30_13TeV-powheg_M_2300_3500/AODSIM/Startup25ns_EXOReReco_74X_Spring15_mcRun2_startup25ns_v0-v1/80000/DCCE00C2-567C-E511-AF63-E41D2D08E0D0.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/ZToMuMu_NNPDF30_13TeV-powheg_M_2300_3500/AODSIM/Startup25ns_EXOReReco_74X_Spring15_mcRun2_startup25ns_v0-v1/80000/E2858DC8-567C-E511-9A64-0025901D4B22.root'
#]

#files=['ZPrimeOfInterest_QCD.root']
#files=['/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_4_15/src/Skim/SelectEvents/test/ZPrimeOfInterest_DYMC2300to3500ChimneyFailAllInfo.root']
#files=[
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/022BAB77-DA98-E511-8C42-0CC47A78A30E.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/062AA459-E898-E511-9163-003048F5ADF8.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/087795B5-F698-E511-B894-0025907D24E6.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/08C904AD-ED98-E511-BCD9-002590E3A0FC.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/0A5D61DB-5399-E511-BD6F-02163E00F3F5.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/0CC9FB83-DA98-E511-BCF5-20CF3027A61E.root'
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/0E991C69-D598-E511-A187-00221982AF2D.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/0EECB6EF-BA99-E511-B845-002590A831AA.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/100B3902-D498-E511-B3C3-F04DA2770C8E.root'
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/10581071-E698-E511-9782-0025901D08BE.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/14CF8D36-869A-E511-88CA-0025901AF91A.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/16A9030A-1299-E511-A01F-FA163EC1AD93.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/18078128-E498-E511-B709-0CC47A4D7630.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/1A97F799-D898-E511-A128-00221982C62E.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/1C8ACB9E-D398-E511-90DC-0CC47A78A30E.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/1EB95CB7-BB99-E511-8E2E-848F69FD29BB.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/2204FE02-C199-E511-96EE-003048F59728.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/24B2E90A-D398-E511-9273-44A8423CF41F.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/24FDD96B-E698-E511-8CE4-002590743042.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/2C6C0397-149A-E511-9136-00266CFFCD00.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/2E420AD8-DC98-E511-B83B-002590DB9296.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/30ADA59C-8B9A-E511-B56E-0025905964B6.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/30DCB022-EB98-E511-A14C-002590E39D52.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/30DE1A88-E298-E511-BEC0-002590D0AFFC.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/38A45DEF-B999-E511-A540-0CC47A4DEE14.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/38B6CC3B-DE98-E511-A667-3417EBE7051F.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/38EAECA7-F598-E511-967E-FA163E36EAC9.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/3A6D191F-F098-E511-BCEA-00259073E34E.root',
#       'root://xrootd-cms.infn.it//store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/3AF82F6F-DB98-E511-A95A-F45214939730.root'	
#]
files=[
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_1.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_10.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_11.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_12.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_13.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_14.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_15.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_16.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_17.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_18.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_19.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_2.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_20.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_3.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_4.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_5.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_6.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_7.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_8.root',
        'file:/afs/cern.ch/work/b/benjamin/ZPrime/Skimmer/CMSSW_7_6_3/src/Skim/SelectEvents/test/crab_Skim_HighPtMuonsMC_QCD_20160313/results/QCDForBakcground_9.root',
]

from skimMCSignal import source as skimMCSignalFiles
process.source = skimDataCv1Files


talking=False
#talking=True

eventCount=0
count=0
muCount=0
failedCount=0
chimneyCount=0
for d in dirs:
	for fileName in files:
		events = Events(fileName)
		for event in events:
			eventCount=eventCount+1
			if (eventCount%1000==0): print "Event: ",eventCount
			if count>100: break
#			count=count+1
                        try: event.getByLabel (genLabel, genHandle)
                        except RuntimeError: print "No gen info"
                        gens=genHandle.product()
			try: event.getByLabel (label, handle)
			except RuntimeError: print "No muon info"
			muons=handle.product()
			try: event.getByLabel(vLabel, vHandle)
			except RuntimeError: print "No vertex info"
			vertices=vHandle.product()
			try: event.getByLabel(trigLabel,trigHandle)
			except RuntimeError: print "No trigger info"
			trigSummary=trigHandle.product()

                        genMuons=[]
                        for gen in gens:
                                if (abs(gen.pdgId())==13 and gen.pt()>30):
                                        if (talking): print "gen with pT: ",('%.2f' % gen.pt())," eta: ",('%.2f' % gen.eta())," phi: ",('%.2f' % gen.phi())
                                        genMuons.append(gen)

			selectedMuons=[]
#			print "numMuons in event: ",len(muons)
			for muon in muons:
#				if (muon.globalTrack().isNonnull()):
#					print "isnonnull"
#				else:
#					print "failed"
#					continue
                                if (muon.isGlobalMuon() and muon.isTrackerMuon() and
                                        muon.globalTrack().hitPattern().numberOfValidMuonHits() > 0 and
                                        muon.globalTrack().hitPattern().numberOfValidPixelHits() > 0 and
                                        muon.globalTrack().hitPattern().trackerLayersWithMeasurement() > 5 and
                                        muon.muonBestTrack().ptError()/muon.muonBestTrack().pt() < 0.3 and
                                        abs(muon.muonBestTrack().dxy(vertices.at(0).position())) < 0.2 and
                                        muon.pt()>53 and
                                        (muon.isolationR03().sumPt / muon.innerTrack().pt()) <0.1
#                                        and abs(muon.eta())<0.8
#					and muon.numberOfMatchedStations() < 2
                                        ):
					selectedMuons.append(muon)
					count=count+1
			for muon in selectedMuons:
				passesNewSel=False
				passesRPCSel=False
				if (talking): print " "
				if (talking): print "muon[",muCount,"] pT: ",('%.2f' % muon.pt())," eta: ",('%.2f' % muon.eta())," phi: ",('%.2f' % muon.phi()),
				if (talking): print " (",'{0:08b}'.format(muon.stationMask()),") ",
				if (talking): print " muonStations (from ID): ",muon.numberOfMatchedStations(),
				if (talking): print " muonStations (from fit): ",muon.globalTrack().hitPattern().muonStationsWithValidHits()
				if (muon.numberOfMatchedStations() == 1 and not(muon.stationMask()==1 or muon.stationMask()==16)): passesNewSel=True
				if (talking): print " muon.numberOfMatchedStations() == 1 and !(muon.stationMask()==1 or muon.stationMask()==16): ",passesNewSel
				if (talking): print "muon.StationMask()==1: ",muon.stationMask()==1
				if (talking): print "muon.StationMask()==16: ",muon.stationMask()==16
				if (talking): print " Layer:\t\t\t1\t2\t3\t4"
				if (talking): print " numSegments (from ID):\t",muon.numberOfSegments(1,1),"\t",muon.numberOfSegments(2,1),
				if (talking): print "\t",muon.numberOfSegments(3,1),"\t",muon.numberOfSegments(4,1)
#				if (talking): print ""
				p=muon.globalTrack().hitPattern()
				numLayerOne=0
				numLayerTwo=0
				numLayerThree=0
				numLayerFour=0
				for hits in range(p.numberOfHits(0)):
					hit=p.getHitPattern(0,hits)
					if (p.muonHitFilter(hit) and p.validHitFilter(hit) and p.getMuonStation(hit)==1): numLayerOne+=1
					if (p.muonHitFilter(hit) and p.validHitFilter(hit) and p.getMuonStation(hit)==2): numLayerTwo+=1
					if (p.muonHitFilter(hit) and p.validHitFilter(hit) and p.getMuonStation(hit)==3): numLayerThree+=1
					if (p.muonHitFilter(hit) and p.validHitFilter(hit) and p.getMuonStation(hit)==4): numLayerFour+=1
				if (talking): print " numHits (from Reco):\t",numLayerOne,"\t",numLayerTwo,"\t",numLayerThree,"\t",numLayerFour
#				for match in muon.matches():
##					if match.id.det()==DetId::Muon: if (talking): print "match is in mu chambers"
#					if match.id.det()==2:
#						detId=DTChamberId(match.id.rawId())
#						if (talking): print "match id: ",match.id.det()," ",match.id.subdetId()," ",detId.wheel()
				if (talking): print " numberOfMatchedRPCLayers: ",muon.numberOfMatchedRPCLayers()
				if ((muon.numberOfMatchedStations() == 1 and (muon.stationMask()==1 or muon.stationMask()==16)) and muon.numberOfMatchedRPCLayers()>2): passesRPCSel=True
				if (talking): print " passesRPCSel? ",passesRPCSel
				muCount+=1
#				if (muon.numberOfMatchedStations() > 1 and talking): print "\tMuon Passed Matched Stations"
				hAll.Fill(muon.pt())
				if (muon.numberOfMatchedStations() > 1): hPass.Fill(muon.pt())
				if ( (muon.numberOfMatchedStations() > 1) or passesNewSel): hPassNew.Fill(muon.pt())
				if ( (muon.numberOfMatchedStations() > 1) or passesNewSel or passesRPCSel): hPassRPC.Fill(muon.pt())
				if (muon.numberOfMatchedStations()<2):
					failedCount+=1
					if ((muon.eta()>0.2 and muon.eta()<0.3 and muon.phi()>1.0 and muon.phi()<2.0) or
						(muon.eta()>-0.3 and muon.eta()<-0.2 and muon.phi()>0.5 and muon.phi()<1.5)):
						chimneyCount+=1

				for gen in genMuons:
				        if (talking): print "\tdeltaR2(gen,muon): ",deltaR2(gen,muon)
				        if deltaR2(gen,muon)<0.2:
						ptDiff=gen.pt()/muon.pt()-1.0
						if (muon.numberOfMatchedStations() > 1):
							if (talking): print "\tOld Cut Pt diff: ",ptDiff
							hOldPtRes.Fill(ptDiff)
							if (gen.pt()<500.0): hOldPtRes0To500.Fill(ptDiff)
							if (gen.pt()>500.0 and gen.pt()<1000.0): hOldPtRes500To1000.Fill(ptDiff)
							if (gen.pt()>1000.0 and gen.pt()<1500.0): hOldPtRes1000To1500.Fill(ptDiff)
							if (gen.pt()>1500.0): hOldPtRes1500Up.Fill(ptDiff)
						if (passesNewSel or passesRPCSel):
							if (talking): print "\tNew Cut Pt diff: ",ptDiff
							hNewPtRes.Fill(ptDiff)
							if (gen.pt()<500.0): hNewPtRes0To500.Fill(ptDiff)
							if (gen.pt()>500.0 and gen.pt()<1000.0): hNewPtRes500To1000.Fill(ptDiff)
							if (gen.pt()>1000.0 and gen.pt()<1500.0): hNewPtRes1000To1500.Fill(ptDiff)
							if (gen.pt()>1500.0): hNewPtRes1500Up.Fill(ptDiff)
					else:
#						if (talking):
						print "\tDid not find muon next to gen!"
					
print "Found #muon: ",count," by running over ",eventCount," events"
print " chimneyCount: ",chimneyCount,"/failedCount: ",failedCount,"=",chimneyCount/failedCount
outputFile = TFile('/afs/cern.ch/user/b/benjamin/MuonStationTestCut0310b.root','RECREATE')
outputFile.cd()
hAll.Write()
hPass.Write()
hPassNew.Write()
hPassRPC.Write()
hOldPtRes.Write()
hNewPtRes.Write()
hNewPtRes0To500.Write()
hNewPtRes500To1000.Write()
hNewPtRes1000To1500.Write()
hNewPtRes1500Up.Write()
hOldPtRes0To500.Write()
hOldPtRes500To1000.Write()
hOldPtRes1000To1500.Write()
hOldPtRes1500Up.Write()
outputFile.Close()

