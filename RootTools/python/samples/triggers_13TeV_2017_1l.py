##################
## Triggers for HLT_MC_SPRING15 and Run II
## Based on HLT_MC_SPRING15 and /frozen/2015/25ns14e33/v2.1/HLT/V1 and /frozen/2015/50ns_5e33/v2.1/HLT/V5

### ----> for the 1L dPhi analysis

## single lepton
triggers_1mu = ["HLT_IsoMu27_v*"]
triggers_1mu20 = ["HLT_IsoMu20_v*"]
triggers_1mu24 = ["HLT_IsoMu24_v*"]

triggers_1el = ['HLT_Ele32_WPTight_v*','HLT_Ele32_WPTight_L1DoubleEG_v*']
triggers_1el35 = ["HLT_Ele35_WPTight_Gsf_v*"]
triggers_1el27WPTight = ["HLT_Ele27_WPTight_Gsf_v*"]

### non-iso single lepton
trigger_1mu_noiso_r = ['HLT_Mu55_v*']
trigger_1mu_noiso_w = ['HLT_Mu50_v*']


trigger_1el_noiso_115 = ['HLT_Ele115_CaloIdVT_GsfTrkIdT_v*']
trigger_1el_noiso_jet165 = ['HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v*']

## muons
triggers_mu_ht600 = ["HLT_Mu15_IsoVVVL_PFHT600_v*"]
triggers_mu_ht450_met50 = ["HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v*"]
#triggers_mu_ht350_met70 = ["HLT_Mu15_IsoVVVL_PFHT350_PFMET70_v*"]
#triggers_mu_ht350_met50 = ["HLT_Mu15_IsoVVVL_PFHT350_PFMET50_v*"]
triggers_mu_ht450 = ["HLT_Mu15_IsoVVVL_PFHT450_v*"]
#triggers_mu_ht400 = ["HLT_Mu15_IsoVVVL_PFHT400_v*"]
triggers_mu50_ht450 = ["HLT_Mu50_IsoVVVL_PFHT450_v*"]
#triggers_mu_met120 = ["HLT_PFMET120_NoiseCleaned_Mu5_v*"]
triggers_mu_ht450_btag = ["HLT_Mu15_IsoVVVL_PFHT450_CaloBTagCSV_4p5_v*"]

## electrons
triggers_el_ht600 = ["HLT_Ele15_IsoVVVL_PFHT600_v*"]
triggers_el_ht450_met50 = ["HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v*"]
#triggers_el_ht350_met70 = ["HLT_Ele15_IsoVVVL_PFHT350_PFMET70_v*"]
#triggers_el_ht350_met50 = ["HLT_Ele15_IsoVVVL_PFHT350_PFMET50_v*"]
#triggers_el_ht350 = ["HLT_Ele15_IsoVVVL_PFHT350_v*"]
triggers_el_ht450 = ["HLT_Ele15_IsoVVVL_PFHT450_v*"]
triggers_el50_ht450 = ["HLT_Ele50_IsoVVVL_PFHT450_v*"]
#triggers_el_ht200 = ["HLT_Ele27_eta2p1_WP85_Gsf_HT200_v*"]
triggers_el_ht450_btag = ["HLT_Ele15_IsoVVVL_PFHT450_CaloBTagCSV_4p5_v*"]

## hadronic
triggers_HT350 = ["HLT_PFHT350_v*"] # prescaled!
triggers_HT590 = ["HLT_PFHT590_v*"] # prescaled!
triggers_HT780 = ["HLT_PFHT780_v*"] # prescaled in 2016G
triggers_HT890 = ["HLT_PFHT890_v*"]
#triggers_MET170 = ["HLT_PFMET170_NoiseCleaned_v*"]
#triggers_HTMET = ["HLT_PFHT350_PFMET120_*"] # include all noise cleaning options!
#triggers_HT350MET120 = ["HLT_PFHT350_PFMET120_*"] # include all noise cleaning options!
#triggers_HT350MET100 = ["HLT_PFHT350_PFMET100_*"] # include all noise cleaning options!
triggers_MET100MHT100 = ['HLT_PFMET100_PFMHT100_IDTight_*', ]
triggers_MET110MHT110 = ['HLT_PFMET110_PFMHT110_IDTight_*', 'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_*']
triggers_MET120MHT120 = ['HLT_PFMET120_PFMHT120_IDTight_*', 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_*']

triggers_highMHTMET = ["HLT_PFMET100_PFMHT100_IDTight_*","HLT_PFMET110_PFMHT110_IDTight_v*", "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v*", "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v*", "HLT_PFMET120_PFMHT120_IDTight_v*"]

triggers_pfjet450 = ["HLT_PFJet450_v*","HLT_AK8PFJet450_v*"]
triggers_ak4pfjet450 = ["HLT_PFJet450_v*"]
triggers_ak8pfjet450 = ["HLT_AK8PFJet450_v*"]
triggers_calojet500 = ["HLT_CaloJet500_NoJetID_v*"]


#pure MET tests
#triggers_MET170_HBHECleaned = ["HLT_PFMET170_HBHECleaned_v*"]
#triggers_MET170_BeamHaloCleaned = ["HLT_PFMET170_BeamHaloCleaned_v*"] 
#triggers_MET170_HBHE_BeamHaloCleaned = ["HLT_PFMET170_HBHE_BeamHaloCleaned_v*"] 
#triggers_METTypeOne190_HBHE_BeamHaloCleaned = ["HLT_PFMETTypeOne190_HBHE_BeamHaloCleaned_v*"] 


#### Combined paths

triggers_muhad = triggers_mu_ht600 + triggers_mu_ht450_met50 + triggers_mu_ht450_btag
triggers_elhad = triggers_el_ht600 + triggers_el_ht450_met50 + triggers_el_ht450_btag
triggers_had = triggers_HT890 