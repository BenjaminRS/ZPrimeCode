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
from ROOT import TVector3,TLorentzVector,TFile,TH1D
DeltaR = ROOT.Math.VectorUtil.DeltaR
DeltaPhi = ROOT.Math.VectorUtil.DeltaPhi
DeltaR2 = lambda a, b: DeltaR(a.p4(), b.p4())  # for reco::Candidates
DeltaPhi2 = lambda a, b: DeltaPhi(a.p4(), b.p4())  # for reco::Candidates

inputSplit=1
if len(sys.argv)>1:
	inputSplit=sys.argv[1]

print "Running inputSplit:",inputSplit
outName='Hist-20160621-'+inputSplit+'.root'
outListName='ListOfDimuonsFailingMu50PassingTkMu50_'+inputSplit
outputFile = TFile(outName,'RECREATE')
outList=open(outListName,'w')

histAllDimuons=TH1D("histAllDimuons","histAllDimuons",10000,0.0,10000.0)
histMu50PassDimuons=TH1D("histMu50PassDimuons","histMu50PassDimuons",10000,0.0,10000.0)
histTkMu50PassDimuons=TH1D("histTkMu50PassDimuons","histTkMu50PassDimuons",10000,0.0,10000.0)
histMu50OrTkMu50PassDimuons=TH1D("histMu50OrTkMu50PassDimuons","histMu50OrTkMu50PassDimuons",10000,0.0,10000.0)


passedMuonsPt=TH1D("passedMuonsPt","passedMuonsPt",5000,0.0,5000.0)
passedMuonsEta=TH1D("passedMuonsEta","passedMuonsEta",1000,-5.0,5.0)
passedMuonsPhi=TH1D("passedMuonsPhi","passedMuonsPhi",800,-4.0,4.0)

passedMu50Pt=TH1D("passedMu50Pt","passedMu50Pt",5000,0.0,5000.0)
passedMu50Eta=TH1D("passedMu50Eta","passedMu50Eta",1000,-5.0,5.0)
passedMu50Phi=TH1D("passedMu50Phi","passedMu50Phi",800,-4.0,4.0)

passedTkMu50Pt=TH1D("passedTkMu50Pt","passedTkMu50Pt",5000,0.0,5000.0)
passedTkMu50Eta=TH1D("passedTkMu50Eta","passedTkMu50Eta",1000,-5.0,5.0)
passedTkMu50Phi=TH1D("passedTkMu50Phi","passedTkMu50Phi",800,-4.0,4.0)

passedMu27Pt=TH1D("passedMu27Pt","passedMu27Pt",5000,0.0,5000.0)
passedMu27Eta=TH1D("passedMu27Eta","passedMu27Eta",1000,-5.0,5.0)
passedMu27Phi=TH1D("passedMu27Phi","passedMu27Phi",800,-4.0,4.0)


muons, muonLabel = Handle("std::vector<pat::Muon>"), "slimmedMuons"
vertices, vertexLabel = Handle("std::vector<reco::Vertex>"), "offlineSlimmedPrimaryVertices"
verticesScore = Handle("edm::ValueMap<float>")
triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults","","HLT")
triggerObjects, triggerObjectLabel  = Handle("std::vector<pat::TriggerObjectStandAlone>"), "selectedPatTrigger"

xrd="root://xrootd-cms.infn.it/"
#f="02D48D7D-3632-E611-ADA7-02163E014568.root"

from fileList import *
files=[]
if inputSplit=='1':	files=files1
elif inputSplit=='2':	files=files2
elif inputSplit=='3':	files=files3
elif inputSplit=='4':   files=files4
elif inputSplit=='5':   files=files5

count=0
for f in files:
	print "File: ",f
	events = Events(xrd+f)
	for nEv,event in enumerate(events):
		count+=1
#		if count>=100000: break
#		if count>=1000000: break
		if (count%10000==0): print "Event: ",count
		EventNum=str(event.eventAuxiliary().run())+":"+str(event.eventAuxiliary().luminosityBlock())+":"+str(event.eventAuxiliary().event())
#		print "event: ",count,"=",EventNum
#		outList.write(EventNum+'\n')
		try:
			event.getByLabel(muonLabel,muons)
			event.getByLabel(vertexLabel, vertices)
			event.getByLabel(vertexLabel, verticesScore)
			event.getByLabel(triggerBitLabel, triggerBits)
			event.getByLabel(triggerObjectLabel, triggerObjects)
		except RuntimeError:
			print "No muons/vertecies"
		if len(vertices.product()) == 0 or vertices.product()[0].ndof() < 4: continue
		else: PV = vertices.product()[0]
	
		numMuPassed=0
		selectedMuons=[]
		for i,mu in enumerate(muons.product()):
			if mu.pt() < 53 or not mu.isHighPtMuon(PV): continue
			numMuPassed+=1
	#		print "muon %2d: pt %4.1f, dz(PV) %+5.3f, POG loose id %d, tight id %d." % (i, mu.pt(), mu.muonBestTrack().dz(PV.position()), mu.isLooseMuon(), mu.isTightMuon(PV))
			selectedMuons.append(mu)
		if (numMuPassed<2): continue
	#	print "\nEvent %d: run %6d, lumi %4d, event %12d" % (nEv,event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event())	
	#	print "num selected muons = ",len(selectedMuons)
	#	for mu in selectedMuons: print mu.pt()
		firstMu=selectedMuons[0]
		secondMu=selectedMuons[1]
		if (firstMu.charge()*secondMu.charge()>0): continue #failed dimuon charge
		lorVec1=TVector3()
		lorVec2=TVector3()
		lorVec1.SetPtEtaPhi(firstMu.pt(),firstMu.eta(),firstMu.phi())
		lorVec2.SetPtEtaPhi(secondMu.pt(),secondMu.eta(),secondMu.phi())
		if (lorVec1.Angle(lorVec2) > 3.1216): continue #failed b2b cut
	
		Dimuon=TLorentzVector()
		Muon1=TLorentzVector()
		Muon2=TLorentzVector()
		Muon1.SetPtEtaPhiE(firstMu.pt(), firstMu.eta(), firstMu.phi(), firstMu.energy())	
		Muon2.SetPtEtaPhiE(secondMu.pt(), secondMu.eta(), secondMu.phi(), secondMu.energy())
		Dimuon=(Muon1+Muon2)
	#	print "Dimuon.M()=",Dimuon.M()
			
		del selectedMuons[2:] #we only want to keep the two highest pt muons
		for mu in selectedMuons:
			passedMuonsPt.Fill(mu.pt())
			passedMuonsEta.Fill(mu.eta())
			passedMuonsPhi.Fill(mu.phi())

		passedMu50=False
		passedTkMu50=False
#		passedMu27=False
		names = event.object().triggerNames(triggerBits.product())
		for j,to in enumerate(triggerObjects.product()):
			for f in to.filterLabels():
				if f=="hltL3fL1sMu22Or25L1f0L2f10QL3Filtered50Q":
	#				print "passed Mu50! Trigger object pt %6.2f eta %+5.3f phi %+5.3f " % (to.pt(),to.eta(),to.phi())
					for mu in selectedMuons:
						if (DeltaR2(mu,to)<0.2):
							passedMu50Pt.Fill(mu.pt())
							passedMu50Eta.Fill(mu.eta())
							passedMu50Phi.Fill(mu.phi())
	#						print "Mu50Pass: DeltaR2(mu,to)=",DeltaR2(mu,to)
#							if (not passedMu50):  #this is the first pass so take it as firing...
							passedMu50=True
				if f=="hltL3fL1sMu25f0TkFiltered50Q":
	#				print "passed TkMu50! Trigger object pt %6.2f eta %+5.3f phi %+5.3f " % (to.pt(),to.eta(),to.phi())
					for mu in selectedMuons:
						if (DeltaR2(mu,to)<0.2):
							passedTkMu50Pt.Fill(mu.pt())
							passedTkMu50Eta.Fill(mu.eta())
							passedTkMu50Phi.Fill(mu.phi())
	#						print "TkMu50Pass: DeltaR2(mu,to)=",DeltaR2(mu,to)
							passedTkMu50=True
				if f=="hltL3fL1sMu22Or25L1f0L2f10QL3Filtered27Q":
					for mu in selectedMuons:
						if (DeltaR2(mu,to)<0.2):
							passedMu27Pt.Fill(mu.pt())
							passedMu27Eta.Fill(mu.eta())
							passedMu27Phi.Fill(mu.phi())
#							passedMu27=True
	
		histAllDimuons.Fill(Dimuon.M())
		if (passedMu50): histMu50PassDimuons.Fill(Dimuon.M())
		if (passedTkMu50): histTkMu50PassDimuons.Fill(Dimuon.M())
		if (passedMu50 or passedTkMu50): histMu50OrTkMu50PassDimuons.Fill(Dimuon.M())
		if (passedTkMu50 and not passedMu50): outList.write(EventNum)

outputFile.cd()

histAllDimuons.Write()
histMu50PassDimuons.Write()
histTkMu50PassDimuons.Write()
histMu50OrTkMu50PassDimuons.Write()

passedMuonsPt.Write()
passedMuonsEta.Write()
passedMuonsPhi.Write()
passedMu50Pt.Write()
passedMu50Eta.Write()
passedMu50Phi.Write()
passedTkMu50Pt.Write()
passedTkMu50Eta.Write()
passedTkMu50Phi.Write()
passedMu27Pt.Write()
passedMu27Eta.Write()
passedMu27Phi.Write()

outputFile.Close()
outList.close()
print count," events processed"
