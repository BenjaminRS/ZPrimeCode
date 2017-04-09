import sys
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.FWLiteEnabler.enable()

ZToMuMu50To120_1=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/243D09B4-90D1-E611-B0FA-001E674DA347.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/26A971E3-E4D1-E611-BF72-001E67457E36.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/5016AADD-6BD1-E611-A765-001E674FB149.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/66F7AFAC-63D1-E611-BA88-001E673476AA.root"
]

ZToMuMu50To120_2=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/7ECFED80-8ED1-E611-A5E5-001E67457E36.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C2FBA64E-38D1-E611-9A18-0CC47A546E5E.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CE9ED593-B0D1-E611-88E2-0242AC130007.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E0F827A2-2AD1-E611-8FF0-001E674DA1AD.root"
]

ZToMuMu50To120_3=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E8BD94EF-F8D0-E611-85C4-ECF4BBE16610.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/06603908-EBCF-E611-92F4-001E674FAF23.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1606844C-D8CF-E611-AA6F-001E674FCAE9.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1E62F2A4-D5CF-E611-A239-001E67348055.root"
]

ZToMuMu50To120_4=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1ECBD442-B0CF-E611-8C31-0CC47A546E5E.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/26EBCB8D-D2CF-E611-BD35-001E674FCAE9.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/32CCC0AE-E8CF-E611-A2B9-001E674FB207.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4C465FEE-D5CF-E611-A112-001E67456F68.root"
]

ZToMuMu50To120_5=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/58B93B60-E0CF-E611-BCA6-001E674440E2.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6CFB551B-F1CF-E611-96E6-001E674FB207.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/701163A6-D5CF-E611-84D2-001E674FAF23.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/80D7BF56-D4CF-E611-B4ED-001E67397AF3.root"
]

ZToMuMu50To120_6=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A2682694-D2CF-E611-8100-001E674FB207.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A43285A2-D5CF-E611-BC47-0CC47A546E5E.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AC55C84D-DACF-E611-8C82-0CC47A537688.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B49F4FBB-EDCF-E611-B974-001E67456F68.root"
]

ZToMuMu50To120_7=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C25A6DFB-E4CF-E611-A535-0CC47A537688.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D0BE6485-E2CF-E611-B7D1-001E674FCAE9.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D22A0AB0-F4CF-E611-98C5-001E67456F68.root"
]

ZToMuMu50To120_8=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E21EB799-D7CF-E611-9473-001E674FB24D.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E412A19B-DCCF-E611-8050-0CC47A546E5E.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F4380BF8-CBCF-E611-8891-0CC47A546E5E.root"
]

ZToMuMu120To200=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_120_200/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2810A5DC-03C8-E611-B20C-001E67504B25.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_120_200/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/824C363B-0AC8-E611-B4A5-20CF3027A580.root"
]

ZToMuMu200To400=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_200_400/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/04DC8BA1-29CC-E611-80AC-001E67586A2F.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_200_400/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/24040450-33CC-E611-A077-001E67346BA1.root"
]

ZToMuMu400To800=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_400_800/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/42155244-66C8-E611-9372-003048FFD798.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_400_800/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/802E4B3F-66C8-E611-9DF5-0CC47A745298.root"
]

ZToMuMu800To1400=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_800_1400/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/12A01361-AFC8-E611-B581-28924A33B8AE.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_800_1400/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/64D02879-AFC8-E611-BD56-7CD30ABD2EEA.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_800_1400/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7E5B98DD-AEC8-E611-A144-008CFAFBF6CC.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_800_1400/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A812B511-AFC8-E611-8066-00266CFFBF80.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_800_1400/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D2974B85-AFC8-E611-BDE6-001D0967D9EF.root"
]

ZToMuMu1400To2300=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_1400_2300/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/082AF542-52E2-E611-8ED8-24BE05CEFB31.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_1400_2300/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3E503B46-52E2-E611-8F14-02163E0176B1.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_1400_2300/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/62365537-51E2-E611-9DF9-001E674DA347.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_1400_2300/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C680F4B6-51E2-E611-9E0E-0CC47A78A458.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_1400_2300/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C8E8DDBD-51E2-E611-981E-0025905B85D6.root"
]

ZToMuMu2300To3500=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_2300_3500/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/782E31FB-9FC7-E611-BE65-008CFA11134C.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_2300_3500/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B8815FAA-93C7-E611-BDC8-008CFA111270.root"
]

ZToMuMu3500To4500=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_3500_4500/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/06BD3929-EDC7-E611-8EC3-02163E019C96.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_3500_4500/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/88E1539B-0AC8-E611-B36F-02163E0140DC.root"
]

ZToMuMu4500To6000=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_4500_6000/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0A222CC8-16C7-E611-BFC2-FA163E39B5B6.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_4500_6000/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/52FEE967-17C7-E611-9A69-FA163E2EED86.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_4500_6000/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A4999F0B-17C7-E611-A246-1866DAEA6D0C.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_4500_6000/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A8CCA36B-17C7-E611-8E4A-0090FAA57D64.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_4500_6000/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B86337F0-16C7-E611-BA6A-24BE05C44B91.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_4500_6000/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EA325C83-17C7-E611-AFA4-001E67E5E8B6.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_4500_6000/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F214122A-17C7-E611-9134-001E674FC800.root"
]

ZToMuMu6000ToInf=[
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_6000_Inf/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/087A263A-F5D0-E611-97C3-0025904AC2C4.root",
"/store/mc/RunIISummer16MiniAODv2/ZToMuMu_NNPDF30_13TeV-powheg_M_6000_Inf/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/408086F7-57D1-E611-97A5-90B11C2CA412.root"
]

