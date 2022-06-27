# import numpy as np
# import pandas pd
import math

#%% Defining material types:
inconel = 'inconel_slm'
maraging_steel = 'maraging_steel_slm'
ss316l = 'sus316l'
ti_grade2 = 'cp_ti'
ti64 = 'ti6al4V'
mat_cost_kg = 0

#%% Cost of build parameters all in KRW
F=0.15 #an assumed value, it should be obtained by evaluation of ~50 builds in SLM single laser printer
c_machrate = 52246
c_gas = 60000
c_rl = 90000
c_filter_porous = 400000

#%% Post-processing cost
c_mp = 500000
c_wc = 200000 #let it stay as constant for now
c_ht = 100000 #this is an assumed value, it should be different for various materials




#%% Total cost equation
def cost_total (m_type, part_volume, support_vol, number_of_parts, t_build):
    material_type = {
        "inconel": 157300,
        "maraging_steel": 206800,
        "ss316l": 205000,
        "ti_grade2": 601700,
        "ti64": 460000,
    }

    mat_cost = material_type.__getitem__(m_type)

    def cost (part_volume, support_vol, number_of_parts, t_build):
        c_machine = t_build * c_machrate
        # print(part_volume, mat_cost)
        cost_part = part_volume*mat_cost
        cost_sup = support_vol*mat_cost
        # print(cost_part)
        cost_scrap = cost_part*0.15

        if t_build >= 240:
            c_filter = 2*c_filter_porous
        elif t_build < 240:
            c_filter = c_filter_porous

        cp_mat = cost_part + cost_sup + cost_scrap
        c_build = c_machine + c_filter + c_gas + c_rl
        c_post = c_mp + c_wc + c_ht

        return 1/(1-F)*(cp_mat+c_build+c_post)/number_of_parts

    cost_per_part = cost(part_volume, support_vol, number_of_parts, t_build)
    return cost_per_part
print(cost_total("inconel", 100000, 150000, 1, 10))
print(cost_total("inconel", 100000, 150000, 10 , 10))

#%% Material cost



# if material=Inconel:
#     cp_part=N*157300 #N represents how much a part weighs in kg and it is manually input, prices are in KRW/kg
#     c_sup=M*157300 #M represents how much a support structure weighs in kg and it is manually input, prices are in KRW/kg
#     c_scrap=0.15*cp_part #asked Mr Choi, he said it is around 15%
#
# elif material=Inconel:
#     cp_part=N*157300 #N represents how much a part weighs in kg and it is manually input, prices are in KRW/kg
#     c_sup=M*157300 #M represents how much a support structure weighs in kg and it is manually input, prices are in KRW/kg
#     c_scrap=0.15*cp_part #asked Mr Choi, he said it is around 15%

F=0.15 #an assumed value, it should be obtained by evaluation of ~50 builds in SLM single laser printer

