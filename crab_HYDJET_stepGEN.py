from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'MB_HYDJET_5020GeV_Run2_stepGEN_10M_check'
config.General.workArea = 'MB_HYDJET_5020GeV_Run2_stepGEN'
config.General.transferOutputs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../python/fragment_HYDJET_py_GEN.py'

config.Data.outputPrimaryDataset = 'MB_HYDJET_5020GeV_Run2_stepGEN_10M_check'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
#NJOBS = 10000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
NJOBS = 2  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.                                                                                                                                                                                                                                                              
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.JobType.numCores = 8
#config.JobType.maxMemoryMB = 20000
config.JobType.maxMemoryMB = 3500

config.Data.publication = True
#config.Data.outLFNDirBase = '/store/group/phys_heavyions/sayan/'                                                                                                                                                                                                                                                                                                           
config.Data.outputDatasetTag ='MB_HYDJET_5020GeV_Run2_stepGEN_10M_check'
config.Data.outLFNDirBase = '/store/user/sayan/'
config.Site.storageSite ='T2_US_Vanderbilt'
