import numpy
import sys
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.FWLiteEnabler.enable()
from DataFormats.FWLite import Events, Handle
from ROOT import TVector3,TLorentzVector,TFile,TH1D,TRandom3
DeltaR = ROOT.Math.VectorUtil.DeltaR
DeltaPhi = ROOT.Math.VectorUtil.DeltaPhi
DeltaR2 = lambda a, b: DeltaR(a.p4(), b.p4())       # for reco::Candidates
DeltaPhi2 = lambda a, b: DeltaPhi(a.p4(), b.p4())   # for reco::Candidates

verbose=False
#verbose=True

inputSplit="Z200To400"
if len(sys.argv)>1:
	inputSplit=sys.argv[1]

print "Running inputSplit:",inputSplit
outName='Hist-20170408MC_'+inputSplit+'.root'
outputFile = TFile(outName,'RECREATE')

DimuonMass=TH1D("DimuonMass","DimuonMass",10000,0.0,10000.0)
DimuonMassBB=TH1D("DimuonMassBB","DimuonMassBB",10000,0.0,10000.0)
DimuonMassNonBB=TH1D("DimuonMassNonBB","DimuonMassNonBB",10000,0.0,10000.0)
DimuonMassBE=TH1D("DimuonMassBE","DimuonMassBE",10000,0.0,10000.0)
DimuonMassEE=TH1D("DimuonMassEE","DimuonMassEE",10000,0.0,10000.0)

DimuonMassPass=TH1D("DimuonMassPass","DimuonMassPass",10000,0.0,10000.0)
DimuonMassPassBB=TH1D("DimuonMassPassBB","DimuonMassPassBB",10000,0.0,10000.0)
DimuonMassPassNonBB=TH1D("DimuonMassPassNonBB","DimuonMassPassNonBB",10000,0.0,10000.0)
DimuonMassPassBE=TH1D("DimuonMassPassBE","DimuonMassPassBE",10000,0.0,10000.0)
DimuonMassPassEE=TH1D("DimuonMassPassEE","DimuonMassPassEE",10000,0.0,10000.0)

MuonPtBB=TH1D("MuonPtBB","MuonPtBB",3000,0.0,3000.0)
MuonPtNonBB=TH1D("MuonPtNonBB","MuonPtNonBB",3000,0.0,3000.0)
MuonPtBE=TH1D("MuonPtBE","MuonPtBE",3000,0.0,3000.0)
MuonPtEE=TH1D("MuonPtEE","MuonPtEE",3000,0.0,3000.0)


muons, muonLabel = Handle("std::vector<pat::Muon>"), "slimmedMuons"
vertices, vertexLabel = Handle("std::vector<reco::Vertex>"), "offlineSlimmedPrimaryVertices"
verticesScore = Handle("edm::ValueMap<float>")
#triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults","","HLT")
#triggerObjects, triggerObjectLabel  = Handle("std::vector<pat::TriggerObjectStandAlone>"), "selectedPatTrigger"
gens, genLabel = Handle("vector<reco::GenParticle>"), "prunedGenParticles"

xrd="root://xrootd-cms.infn.it/"

from MCFileList import *
files=[]
if inputSplit=='Z50To120_1':	files=ZToMuMu50To120_1
elif inputSplit=='Z50To120_2':	files=ZToMuMu50To120_2
elif inputSplit=='Z50To120_3':	files=ZToMuMu50To120_3
elif inputSplit=='Z50To120_4':	files=ZToMuMu50To120_4
elif inputSplit=='Z50To120_5':	files=ZToMuMu50To120_5
elif inputSplit=='Z50To120_6':	files=ZToMuMu50To120_6
elif inputSplit=='Z50To120_7':	files=ZToMuMu50To120_6
elif inputSplit=='Z50To120_8':	files=ZToMuMu50To120_6
elif inputSplit=='Z120To200':	 files=ZToMuMu120To200
elif inputSplit=='Z200To400':	files=ZToMuMu200To400
elif inputSplit=='Z400To800':	files=ZToMuMu400To800
elif inputSplit=='Z800To1400':	files=ZToMuMu800To1400
elif inputSplit=='Z1400To2300':	files=ZToMuMu1400To2300
elif inputSplit=='Z2300To3500':	files=ZToMuMu2300To3500
elif inputSplit=='Z3500To4500':	files=ZToMuMu3500To4500
elif inputSplit=='Z4500To6000':	files=ZToMuMu4500To6000
elif inputSplit=='Z6000ToInf':	files=ZToMuMu6000ToInf

#Efficiencies come from Slide 16 of https://indico.cern.ch/event/615094/contributions/2480967/attachments/1415354/2170520/20022017_Mu50orTkMu50TrgEff_ZPrimeMeeting_schhibra.pdf
#[eta1pt1,eta2pt1,..]
#[eta1pt2,eta2pt2,..]
#keeping 2 lots for last pt bin, in case we want to change the number of pt bins in future

##Data B-H
#muTrigEff=[
#           [0.939,0.827,0.944,0.931,0.922,0.847,0.800],
#           [0.940,0.816,0.941,0.921,0.914,0.841,0.771],
#           [0.935,0.796,0.922,0.899,0.896,0.793,0.707],
#           [0.935,0.796,0.922,0.899,0.896,0.793,0.707]
#           ]

#MC
muTrigEff=[
           [0.961,0.887,0.956,0.973,0.911,0.879,0.856],
           [0.959,0.854,0.948,0.974,0.915,0.886,0.853],
           [0.968,0.776,0.944,0.941,0.896,0.841,0.834],
           [0.968,0.776,0.944,0.941,0.896,0.841,0.834]
           ]


##SF: do not use these as part of this code!
#muTrigEff=[
#           [0.977,0.932,0.987,0.957,1.012,0.964,0.934],
#           [0.981,0.955,0.992,0.946,0.999,0.949,0.904],
#           [0.966,1.026,0.976,0.955,0.999,0.943,0.848],
#           [0.966,1.026,0.976,0.955,0.999,0.943,0.848]
#           ]

def triggerPassed(mu1,mu2):
	eff1=0
	eff2=0
	pT1=100.0
	pT2=200.0
	pT3=500.0
    
	if (abs(mu1.eta())<0.2 and mu1.pt()<pT1):						eff1=muTrigEff[0][0]
	if (abs(mu1.eta())<0.2 and mu1.pt()>pT1 and mu1.pt()<pT2):				eff1=muTrigEff[1][0]
	if (abs(mu1.eta())<0.2 and mu1.pt()>pT2 and mu1.pt()<pT3):				eff1=muTrigEff[2][0]
	if (abs(mu1.eta())<0.2 and mu1.pt()>pT3):						eff1=muTrigEff[3][0]
	
	if (abs(mu1.eta())>0.2 and abs(mu1.eta())<0.3 and mu1.pt()<pT1):			eff1=muTrigEff[0][1]
	if (abs(mu1.eta())>0.2 and abs(mu1.eta())<0.3 and mu1.pt()>pT1 and mu1.pt()<pT2):	eff1=muTrigEff[1][1]
	if (abs(mu1.eta())>0.2 and abs(mu1.eta())<0.3 and mu1.pt()>pT2 and mu1.pt()<pT3):	eff1=muTrigEff[2][1]
	if (abs(mu1.eta())>0.2 and abs(mu1.eta())<0.3 and mu1.pt()>pT3):			eff1=muTrigEff[3][1]

	if (abs(mu1.eta())>0.3 and abs(mu1.eta())<0.9 and mu1.pt()<pT1):			eff1=muTrigEff[0][2]
	if (abs(mu1.eta())>0.3 and abs(mu1.eta())<0.9 and mu1.pt()>pT1 and mu1.pt()<pT2):	eff1=muTrigEff[1][2]
	if (abs(mu1.eta())>0.3 and abs(mu1.eta())<0.9 and mu1.pt()>pT2 and mu1.pt()<pT3):	eff1=muTrigEff[2][2]
	if (abs(mu1.eta())>0.3 and abs(mu1.eta())<0.9 and mu1.pt()>pT3):			eff1=muTrigEff[3][2]

	if (abs(mu1.eta())>0.9 and abs(mu1.eta())<1.2 and mu1.pt()<pT1):			eff1=muTrigEff[0][3]
	if (abs(mu1.eta())>0.9 and abs(mu1.eta())<1.2 and mu1.pt()>pT1 and mu1.pt()<pT2):	eff1=muTrigEff[1][3]
	if (abs(mu1.eta())>0.9 and abs(mu1.eta())<1.2 and mu1.pt()>pT2 and mu1.pt()<pT3):	eff1=muTrigEff[2][3]
	if (abs(mu1.eta())>0.9 and abs(mu1.eta())<1.2 and mu1.pt()>pT3):			eff1=muTrigEff[3][3]

	if (abs(mu1.eta())>1.2 and abs(mu1.eta())<1.6 and mu1.pt()<pT1):			eff1=muTrigEff[0][4]
	if (abs(mu1.eta())>1.2 and abs(mu1.eta())<1.6 and mu1.pt()>pT1 and mu1.pt()<pT2):	eff1=muTrigEff[1][4]
	if (abs(mu1.eta())>1.2 and abs(mu1.eta())<1.6 and mu1.pt()>pT2 and mu1.pt()<pT3):	eff1=muTrigEff[2][4]
	if (abs(mu1.eta())>1.2 and abs(mu1.eta())<1.6 and mu1.pt()>pT3):			eff1=muTrigEff[3][4]

	if (abs(mu1.eta())>1.6 and abs(mu1.eta())<2.1 and mu1.pt()<pT1):			eff1=muTrigEff[0][5]
	if (abs(mu1.eta())>1.6 and abs(mu1.eta())<2.1 and mu1.pt()>pT1 and mu1.pt()<pT2):	eff1=muTrigEff[1][5]
	if (abs(mu1.eta())>1.6 and abs(mu1.eta())<2.1 and mu1.pt()>pT2 and mu1.pt()<pT3):	eff1=muTrigEff[2][5]
	if (abs(mu1.eta())>1.6 and abs(mu1.eta())<2.1 and mu1.pt()>pT3):			eff1=muTrigEff[3][5]

	if (abs(mu1.eta())>2.1 and mu1.pt()<pT1):						eff1=muTrigEff[0][6]
	if (abs(mu1.eta())>2.1 and mu1.pt()>pT1 and mu1.pt()<pT2):				eff1=muTrigEff[1][6]
	if (abs(mu1.eta())>2.1 and mu1.pt()>pT2 and mu1.pt()<pT3):				eff1=muTrigEff[2][6]
	if (abs(mu1.eta())>2.1 and mu1.pt()>pT3):						eff1=muTrigEff[3][6]


	if (abs(mu2.eta())<0.2 and mu2.pt()<pT1):						eff2=muTrigEff[0][0]
	if (abs(mu2.eta())<0.2 and mu2.pt()>pT1 and mu2.pt()<pT2):				eff2=muTrigEff[1][0]
	if (abs(mu2.eta())<0.2 and mu2.pt()>pT2 and mu2.pt()<pT3):				eff2=muTrigEff[2][0]
	if (abs(mu2.eta())<0.2 and mu2.pt()>pT3):						eff2=muTrigEff[3][0]
	
	if (abs(mu2.eta())>0.2 and abs(mu2.eta())<0.3 and mu2.pt()<pT1):			eff2=muTrigEff[0][1]
	if (abs(mu2.eta())>0.2 and abs(mu2.eta())<0.3 and mu2.pt()>pT1 and mu2.pt()<pT2):	eff2=muTrigEff[1][1]
	if (abs(mu2.eta())>0.2 and abs(mu2.eta())<0.3 and mu2.pt()>pT2 and mu2.pt()<pT3):	eff2=muTrigEff[2][1]
	if (abs(mu2.eta())>0.2 and abs(mu2.eta())<0.3 and mu2.pt()>pT3):			eff2=muTrigEff[3][1]

	if (abs(mu2.eta())>0.3 and abs(mu2.eta())<0.9 and mu2.pt()<pT1):			eff2=muTrigEff[0][2]
	if (abs(mu2.eta())>0.3 and abs(mu2.eta())<0.9 and mu2.pt()>pT1 and mu2.pt()<pT2):	eff2=muTrigEff[1][2]
	if (abs(mu2.eta())>0.3 and abs(mu2.eta())<0.9 and mu2.pt()>pT2 and mu2.pt()<pT3):	eff2=muTrigEff[2][2]
	if (abs(mu2.eta())>0.3 and abs(mu2.eta())<0.9 and mu2.pt()>pT3):			eff2=muTrigEff[3][2]

	if (abs(mu2.eta())>0.9 and abs(mu2.eta())<1.2 and mu2.pt()<pT1):			eff2=muTrigEff[0][3]
	if (abs(mu2.eta())>0.9 and abs(mu2.eta())<1.2 and mu2.pt()>pT1 and mu2.pt()<pT2):	eff2=muTrigEff[1][3]
	if (abs(mu2.eta())>0.9 and abs(mu2.eta())<1.2 and mu2.pt()>pT2 and mu2.pt()<pT3):	eff2=muTrigEff[2][3]
	if (abs(mu2.eta())>0.9 and abs(mu2.eta())<1.2 and mu2.pt()>pT3):			eff2=muTrigEff[3][3]

	if (abs(mu2.eta())>1.2 and abs(mu2.eta())<1.6 and mu2.pt()<pT1):			eff2=muTrigEff[0][4]
	if (abs(mu2.eta())>1.2 and abs(mu2.eta())<1.6 and mu2.pt()>pT1 and mu2.pt()<pT2):	eff2=muTrigEff[1][4]
	if (abs(mu2.eta())>1.2 and abs(mu2.eta())<1.6 and mu2.pt()>pT2 and mu2.pt()<pT3):	eff2=muTrigEff[2][4]
	if (abs(mu2.eta())>1.2 and abs(mu2.eta())<1.6 and mu2.pt()>pT3):			eff2=muTrigEff[3][4]

	if (abs(mu2.eta())>1.6 and abs(mu2.eta())<2.1 and mu2.pt()<pT1):			eff2=muTrigEff[0][5]
	if (abs(mu2.eta())>1.6 and abs(mu2.eta())<2.1 and mu2.pt()>pT1 and mu2.pt()<pT2):	eff2=muTrigEff[1][5]
	if (abs(mu2.eta())>1.6 and abs(mu2.eta())<2.1 and mu2.pt()>pT2 and mu2.pt()<pT3):	eff2=muTrigEff[2][5]
	if (abs(mu2.eta())>1.6 and abs(mu2.eta())<2.1 and mu2.pt()>pT3):			eff2=muTrigEff[3][5]

	if (abs(mu2.eta())>2.1 and mu2.pt()<pT1):						eff2=muTrigEff[0][6]
	if (abs(mu2.eta())>2.1 and mu2.pt()>pT1 and mu2.pt()<pT2):				eff2=muTrigEff[1][6]
	if (abs(mu2.eta())>2.1 and mu2.pt()>pT2 and mu2.pt()<pT3):				eff2=muTrigEff[2][6]
	if (abs(mu2.eta())>2.1 and mu2.pt()>pT3):						eff2=muTrigEff[3][6]

	mu1pass=False
	mu2pass=False
	r3=TRandom3()
	r3.SetSeed(0)
	rndNum=r3.Rndm()
	if (eff1>rndNum): mu1pass=True
	if verbose: print "mu1.eta and mu1.pt: ",mu1.eta()," ",mu1.pt(),": eff1: ",eff1," rndNum: ",rndNum, " mu1pass? ",mu1pass
	r3.SetSeed(0)
	rndNum=r3.Rndm()
	if (eff2>rndNum): mu2pass=True
	if verbose: print "mu2.eta and mu2.pt: ",mu2.eta()," ",mu2.pt(),": eff2: ",eff2," rndNum: ",rndNum, " mu2pass? ",mu2pass
	passing=False
	if (mu1pass or mu2pass): passing=True
	if verbose: print "Passed trigger?: ",passing
	return passing
	
BB=0
NonBB=0
BE=0
EE=0

count=0
for f in files:
	print "File: ",f
	events = Events(xrd+f)
	for nEv,event in enumerate(events):
		count+=1
#		if count>=200: break
		if (count%10000==0): print "Event: ",count
		EventNum=str(event.eventAuxiliary().run())+":"+str(event.eventAuxiliary().luminosityBlock())+":"+str(event.eventAuxiliary().event())
		try:
			event.getByLabel(muonLabel,muons)
			event.getByLabel(vertexLabel, vertices)
			event.getByLabel(vertexLabel, verticesScore)
#			event.getByLabel(triggerBitLabel, triggerBits)
#			event.getByLabel(triggerObjectLabel, triggerObjects)
			event.getByLabel(genLabel, gens)
		except RuntimeError:
			print "No muons/vertecies"
		if len(vertices.product()) == 0 or vertices.product()[0].ndof() < 4: continue
		else: PV = vertices.product()[0]
		
		genZMass=0
		for gen in gens.product():
			if (gen.pdgId()==23): genZMass=gen.mass()
		if (genZMass==0):
			print "no gen Z!"
			continue
		if verbose: print "genZMass: ",genZMass
	
		numMuPassed=0
		selectedMuons=[]
		for i,mu in enumerate(muons.product()):
#			if mu.pt() < 53 or not mu.isHighPtMuon(PV): continue #Looking in Signal Region
			if mu.pt() < 53 or not (mu.isGlobalMuon() and mu.isTrackerMuon()): continue
			if abs(mu.dB())>0.2: continue
			if mu.isolationR03().sumPt / mu.innerTrack().pt() > 0.10: continue
			if not(mu.globalTrack().hitPattern().trackerLayersWithMeasurement() > 5): continue
			if not(mu.globalTrack().hitPattern().numberOfValidPixelHits() >= 1): continue
			if not(mu.globalTrack().hitPattern().numberOfValidMuonHits() > 0): continue
			if not( mu.numberOfMatchedStations() > 1 or
				(mu.numberOfMatchedStations() == 1 and not(mu.stationMask() == 1 or mu.stationMask() == 16)) or 
				(mu.numberOfMatchedStations() == 1 and (mu.stationMask() == 1 or mu.stationMask() == 16) and mu.numberOfMatchedRPCLayers()>2)
				): continue
			numMuPassed+=1
			selectedMuons.append(mu)
		if verbose: print "number of muons passing selection in event: ",numMuPassed
		if (numMuPassed<2): continue #need more than 1 muon candidate
		firstMu=selectedMuons[0]
		secondMu=selectedMuons[1]
        
		if (firstMu.charge()*secondMu.charge()>0): continue #failed dimuon charge
        
		lorVec1=TVector3()
		lorVec2=TVector3()
		lorVec1.SetPtEtaPhi(firstMu.pt(),firstMu.eta(),firstMu.phi())
		lorVec2.SetPtEtaPhi(secondMu.pt(),secondMu.eta(),secondMu.phi())
		if (lorVec1.Angle(lorVec2) > 3.1216): continue #failed b2b cut
	
#		Dimuon=TLorentzVector()
#		Muon1=TLorentzVector()
#		Muon2=TLorentzVector()
#		Muon1.SetPtEtaPhiE(firstMu.pt(), firstMu.eta(), firstMu.phi(), firstMu.energy())	
#		Muon2.SetPtEtaPhiE(secondMu.pt(), secondMu.eta(), secondMu.phi(), secondMu.energy())
#		Dimuon=(Muon1+Muon2)

		DimuonMass.Fill(genZMass)
		if (triggerPassed(firstMu,secondMu)): DimuonMassPass.Fill(genZMass)

		if (abs(firstMu.eta())<1.2 and abs(secondMu.eta())<1.2):
			MuonPtBB.Fill(firstMu.pt())
			MuonPtBB.Fill(secondMu.pt())
			DimuonMassBB.Fill(genZMass)
			if (triggerPassed(firstMu,secondMu)):
				DimuonMassPassBB.Fill(genZMass)
				BB+=1
		else:
			MuonPtNonBB.Fill(firstMu.pt())
			MuonPtNonBB.Fill(secondMu.pt())
			DimuonMassNonBB.Fill(genZMass)
			if (triggerPassed(firstMu,secondMu)):
				DimuonMassPassNonBB.Fill(genZMass)
				NonBB+=1
			
        
		if ( (abs(firstMu.eta())<1.2 and abs(secondMu.eta())>1.2) or (abs(secondMu.eta())<1.2 and abs(firstMu.eta())>1.2) ):
			MuonPtBE.Fill(firstMu.pt())
			MuonPtBE.Fill(secondMu.pt())
			DimuonMassBE.Fill(genZMass)
			if (triggerPassed(firstMu,secondMu)):
				DimuonMassPassBE.Fill(genZMass)
				BE+=1

		if (abs(firstMu.eta())>1.2 and abs(secondMu.eta())>1.2):
			MuonPtEE.Fill(firstMu.pt())
			MuonPtEE.Fill(secondMu.pt())
			DimuonMassEE.Fill(genZMass)
			if (triggerPassed(firstMu,secondMu)):
				DimuonMassPassEE.Fill(genZMass)
				EE+=1


outputFile.cd()

DimuonMass.Write()
DimuonMassBB.Write()
DimuonMassNonBB.Write()
DimuonMassBE.Write()
DimuonMassEE.Write()

DimuonMassPass.Write()
DimuonMassPassBB.Write()
DimuonMassPassNonBB.Write()
DimuonMassPassBE.Write()
DimuonMassPassEE.Write()

MuonPtBB.Write()
MuonPtNonBB.Write()
MuonPtBE.Write()
MuonPtEE.Write()

outputFile.Close()
print count," events processed"

print"#BB: ",BB
print"#NonBB: ",NonBB
print"#BE: ",BE
print"#EE: ",EE
