"""
Some global variables
* latex and unit of root variables
* latex of particles, specified in the root files
* latex of fitted parameters
"""

################################################################################################
###################################  Specific to the project  ##################################
################################################################################################

# Masses
Dst_M_PDG = 2010.26 #D*+
m_Dplus_PDG = 1869.65 #D+
m_D0_PDG = 1864.83 #D+
m_B0_PDG = 5279.63 #B0
m_B0s_PDG = 5366.84 #B0s


################################################################################################
###########################  Variables necessary to the HEA module  ############################
################################################################################################

## INFORMATION ABOUT THE VARIABLES/PARTICLES ===================================================

units = {
    'm': "MeV/$c^2$",
    'p': "MeV/c"
}

# latex and unit of some variables
definition_quantities = {
    'P' : {
        'latex': "$p$",
        'unit': units['p']
    },
    'PT': 
    {
        'latex': "$p_T$",
        'unit': units['p']
    },
    'M': 
    {
        'latex': "$m$",
        'unit': units['m']
    },
    'flight_z':
    {
        'latex': "$\Delta z$",
        'unit': "mm"
    },
    'flight_zsig':
    {
        'latex': "$\Delta z$ significance",
        'unit': None
    },
    'flight':
    {
        'latex': "flight distance",
        'unit': 'mm'
    },
    'TRACK_CHI2NDOF':
    {
        'latex': '$\\chi^2$ per d.o.f. of the track',
        'unit': None
    },
    'ENDVERTEX_CHI2':
    {
        'latex': '$\\chi^2$ of the EV',
        'unit': None
    },
    'OWNPV_CHI2':
    {
        'latex': '$\\chi^2$ of the PV',
        'unit': None
    },
    'FDCHI2_OWNPV':
    {
        'latex': '$\\chi^2$ of the flight distance w.r.t. the PV',
        'unit': None
    },
    'FD_OWNPV':
    {
        'latex': 'flight distance w.r.t. the PV',
        'unit': None
    },
    'IPCHI2_OWNPV':
    {
        'latex': '$\\chi^2$ of the impact parameter w.r.t. the PV',
        'unit': None
    },
    'IP_OWNPV':
    {
        'latex': 'impact parameter w.r.t. the PV',
        'unit': None
    },
    'DIRA_OWNPV':
    {
        'latex': 'cosine of the DIRA angle w.r.t. the PV',
        'unit': None
    },
    'M_Tau_Pi12pip':
    {
        'latex': 'm',
        'unit': 'GeV/$c^2$'
    },
    'ENDVERTEX_CHI2,ENDVERTEX_NDOF:x/y':{
        'latex': "$\chi^2$ of the EV per d.o.f.",
        'unit': None
    },
    'ETA':{
        'latex': "$\\eta$",
        'unit': None
    },
    'm_Kpipi' :{
        'latex': "$m$($K\pi\pi$)",
        'unit': units['m']        
    },
    'q2_reco' :{
        'latex': "$q^2$",
        'unit': "(MeV/$c^2$)$^2$"       
    },
    'tau_life_reco' :{
        'latex': "$t_{\\tau}$",
        'unit': "fs"       
    },
    'isolation_bdt':{
        'latex': "isolation BDT",
        'unit': None        
    },
    'm_DstKpipi':{
        'latex': "$m$($D^*K\pi\pi$)",
        'unit': units['m']        
    },
    'theta_X_reco':{
        'latex': "$\\theta_X$",
        'unit': None        
    },
    'theta_L_reco':{
        'latex': "$\\theta_L$",
        'unit': None        
    },
    'chi_reco':{
        'latex': "$\\chi$",
        'unit': None        
    },
    'costheta_X_reco':{
        'latex': "cos($\\theta_X$)",
        'unit': None        
    },
    'costheta_L_reco':{
        'latex': "cos($\\theta_L$)",
        'unit': None        
    },
    'coschi_reco':{
        'latex': "cos($\\chi$)",
        'unit': None        
    },
    'm_Kpipipi': {
        'latex': "$m(K\\pi\\pi\\pi)$",
        'unit': units['m']
    }
}

# latex of the particles specified in the root file
latex_particles = {
    'B0'            : '$D^{*}3\pi$',
    'Dst'           : '$D^*$',
    'D0'            : '$D^0$',
    'tau'           : '$3\pi$',
    'tau_pion0'     : '$\pi_0$',
    'tau_pion1'     : '$\pi_1$',
    'tau_pion2'     : '$\pi_2$',
    'Dst_constr_B0' : f'$D^*3\pi|m(D^*)$={Dst_M_PDG} MeV/$c^2$',
    'D0_pion'       : '$\pi$ of $D^0$',
    'D0_kaon'       : '$K$ from $D^0$',
    'Dst_pion'      : '$\pi$ from $D^*$'
}



################################################################################################
##############################  Other variables of the project  ################################
################################################################################################


## latex OF THE PARTICLES ===================================================
# used for the saved latex table as well as the table that contains the result of the fit
# which is shown inside the plot that contains the histogram and the fitted PDF


