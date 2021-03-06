from CMGTools.TTHAnalysis.treeReAnalyzer import *
from ROOT import TLorentzVector, TVector2, std
import ROOT
import time
import itertools
import PhysicsTools.Heppy.loadlibs
import array
import operator
import math

# mc to data pu weight
def getPUdict(fname, puHistName = "pileup"):
    puDict = {}

    puFile = ROOT.TFile(fname,"READ")
    hPUw = puFile.Get(puHistName)

    if not hPUw:
        print "PU hist not found!"
        exit(0)

    for ibin in range(1,hPUw.GetNbinsX()):

        #npv = hPUw.GetXaxis().GetBinLowEdge(ibin)
        npv = int(hPUw.GetXaxis().GetBinCenter(ibin))
        rat = hPUw.GetBinContent(ibin)

        puDict[npv] = rat

    puFile.Close()

    return puDict


# 2017 UL
puFileName = "../python/PileupWeights/puWeights_Run2.root"

puNorm =  getPUdict(puFileName,puHistName = "puWeight2017" )
puUp =  getPUdict(puFileName,puHistName = "puWeight2017Up")
puDown =  getPUdict(puFileName,puHistName = "puWeight2017Down")

print 80*"#"
print "Loaded PU weights!"
print puNorm

class EventVars1L_pileup:
    def __init__(self):
        self.branches = [
            'nVtx', 'nTrueInt',
            'puRatio','puRatio_up','puRatio_down'
            ]

    def listBranches(self):
        return self.branches[:]

    def __call__(self,event,base):

        # output dict:
        ret = {}
        ret['nVtx'] = event.nVert
        if not event.isData:

            nTrueInt = event.nTrueInt
            ret['nTrueInt'] = nTrueInt

            floornTrueInt = math.floor(nTrueInt)

            if floornTrueInt in puNorm:
                ret['puRatio'] = puNorm[floornTrueInt]
                ret['puRatio_up'] = puUp[floornTrueInt]
                ret['puRatio_down'] = puDown[floornTrueInt]
            else:
                ret['puRatio'] = 0
                ret['puRatio_up'] = 0
                ret['puRatio_down'] = 0
        else:
            ret['puRatio'] = 1
            ret['puRatio_up'] = 1
            ret['puRatio_down'] = 1


        return ret

if __name__ == '__main__':
    from sys import argv
    file = ROOT.TFile(argv[1])
    tree = file.Get("tree")
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf = EventVars1L()
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d: leps %d" % (ev.run, ev.lumi, ev.evt, ev.nLepGood)
            print self.sf(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)
