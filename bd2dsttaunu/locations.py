import os.path as op
repo = op.join(op.dirname(__file__), '..')

class loc : pass

########################################################################################
###################################### ROOT files ######################################
########################################################################################


YY = [11, 12, 15, 16, 17, 18] # years
MM = ['up', 'down'] # magnet polarisation

loc.luke_data = '/data/lhcb/users/scantlebury-smead/angular_analysis/'

loc.data            = loc.luke_data + "data/"
loc.double_charm_MC = loc.luke_data + "double_charm/"

## B -> D* D+ X
loc.B2DstDplusX      = loc.data + "data_{YY}_{MM}_final_ds_selection.root"
loc.B2DstDplusX_list = [loc.B2DstDplusX.format(YY=yy, MM=mm) for mm in MM for yy in YY]
loc.B2DstDplusX_MC   = loc.double_charm_MC + "final_ds_selection_B_DstDpX_Kpipi_truth_matched.root"
loc.B2DstD0X_MC   = loc.double_charm_MC + "final_ds_selection_B_DstD0X_Kpipipi_truth_matched.root"
