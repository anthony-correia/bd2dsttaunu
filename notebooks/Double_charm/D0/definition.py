"""
Global variables used for the :math:`D^+ \\to K^+ \\pi^+ \\pi^-` analyses.
"""

latex_decay = "$D^0 \\to K^{-} \pi^+ \pi^+ \pi^-$"

## DATA NAMES ============================================================

data_names = {
    'data'    : 'BTODstD0X',
    'MC'      : 'BTODstD0X_MC',
    'GBReweight_MC' : 'GBReweighter_BTODstD0X_MC'
}
data_names['reweighted_MC'] = f"bins_reweight_{data_names['MC']}_to_{data_names['data']}"

colors = {
    'data': 'indigo',
    'MC': 'r',
    'bkg':'y',
    'reweighted_MC': 'g'
}

MC_description = 'LHCb simulation \n (15 + 16)'

## LIMITS ================================================================

branch = 'm_Kpipipi'

limits_m_Kpipipi = {}

# MC
limits_m_Kpipipi['MC'] = {
    'low'  : 1775,
    'high' : 1950       
}


# data
limits_m_Kpipipi['data'] = {
    'low'    : 1775,
    'high'   : 1950
}

# # reduced data
# limits_m_Kpipi['red_data'] = {
#     'low'    : 1820,
#     'high'   : 1950
# }


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

column_ranges = {}

# column_ranges = {
#     'q2_reco': [None, None],
#     'isolation_bdt': [None, None],
#     'tau_life_reco': [None, None],
#     'B0_M': [None, 5000],
#     'm_DstKpipi': [None, None],
# }