# Following https://hypernews.cern.ch/HyperNews/CMS/get/luminosity/613/2/1/1/1.html
#json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
#pileup=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/pileup_latest.txt
json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt
pileup=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PileUp/pileup_latest.txt
#bins=100
bins=100
minBias="69200"
uncert="1.046"

pileupCalc.py \
  -i $json \
  --inputLumiJSON $pileup \
  --calcMode true \
  --minBiasXsec $minBias \
  --maxPileupBin $bins \
  --numPileupBins $bins \
  dataPileup17.root

# variations
pileupCalc.py \
  -i $json \
  --inputLumiJSON $pileup \
  --calcMode true \
  --minBiasXsec $(echo "$minBias * $uncert"|bc) \
  --maxPileupBin $bins \
  --numPileupBins $bins \
  dataPileup_minBiasUP17.root

pileupCalc.py \
  -i $json \
  --inputLumiJSON $pileup \
  --calcMode true \
  --minBiasXsec $(echo "$minBias * (2-$uncert)"|bc) \
  --maxPileupBin $bins \
  --numPileupBins $bins \
  dataPileup_minBiasDOWN17.root
