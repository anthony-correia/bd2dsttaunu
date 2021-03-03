"""
Global variables used for the :math:`D^+ \\to K^- \\pi^+ \\pi^+` analyses.
"""

latex_decay = "$D^+ \\to K^{-} \\pi^{+} \\pi^{+}$"

## DATA NAMES ============================================================

data_names = {
    'data'    : 'BTODstDpX',
    'MC'      : 'BTODstDpX_MC',
    'GBReweight_MC': 'GBReweighter_BTODstDpX_MC'
}

MC_description = 'LHCb simulation \n (15 + 16)'

## LIMITS ================================================================

branch = 'm_Kpipi'

limits_m_Kpipi = {}

# MC
from bd2dsttaunu.definition import m_Dplus_PDG
window_MC = 50

limits_m_Kpipi['MC'] = {
    'low'  : m_Dplus_PDG - window_MC,
    'high' : 1912       
}


# data
limits_m_Kpipi['data'] = {
    'low'    : 1820,
    'high'   : 1950
}



# COLUMNS TO LOAD ========================================================
columns = [branch]
columns += ['q2_reco', 'isolation_bdt', 'tau_life_reco', 'm_DstKpipi']
# angles
columns += ['theta_X_reco', 'theta_L_reco', 'chi_reco']
columns += ['costheta_X_reco', 'costheta_L_reco', 'coschi_reco']
# Invariant masses
columns += ['tau_M', 'B0_M']

# RANGES OF THE VARIABLES =================================================

# column_ranges = {
#     'q2_reco': [2., None],
#     'isolation_bdt': [None, 0.95],
#     'tau_life_reco': [None, 0.003],
#     'B0_M': [3150, None],
#     'm_DstKpipi': [None, 5450],
# }

column_ranges = {
    'q2_reco': [None, None],
    'isolation_bdt': [None, None],
    'tau_life_reco': [None, None],
    'B0_M': [None, 5000],
    'm_DstKpipi': [None, None],
}