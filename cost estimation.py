import numpy as np
import pandas pd

#%% Asking for input values



#%% Total cost equation
def cost_total:
    c_machine=T_build*c_machrate
    cp_mat=c_part+ c_sup+c_scrap
    c_build=c_machine + c_filter + c_gas + c_rl
    c_post=c_mp+c_wc+c_ht
    if T_build>=240:
        c_filter=2*c_filter_porous
    elif T_build<240
        c_filter=c_filter_porous
    return 1/(1-F)*(cp_mat+c_build+c_post)



#%% Material cost
materials= [inconel,
            maraging_steel,
            ss316l,
            ti_grade2,
            ti64
]

cost_material = [
            cp_part,
            c_sup,
            c_scrap
]

inconel={
    c_part:part_in_kg*157300,
    c_sup:sup_in_kg*157300,
    scrap:c_part*0.15
}

maraging_steel={
    c_part: part_in_kg * 206800,
    c_sup: sup_in_kg * 206800,
    scrap: c_part * 0.15
}

ss316l={
    c_part: part_in_kg * 205000,
    c_sup: sup_in_kg * 205000,
    scrap: c_part * 0.15
}
ti_grade2={
    c_part: part_in_kg * 601700,
    c_sup: sup_in_kg * 601700,
    scrap: c_part * 0.15
}

ti64={
    c_part: part_in_kg * 460000,
    c_sup: sup_in_kg * 460000,
    scrap: c_part * 0.15
}

if material=Inconel:
    cp_part=N*157300 #N represents how much a part weighs in kg and it is manually input, prices are in KRW/kg
    c_sup=M*157300 #M represents how much a support structure weighs in kg and it is manually input, prices are in KRW/kg
    c_scrap=0.15*cp_part #asked Mr Choi, he said it is around 15%

elif material=Inconel:
    cp_part=N*157300 #N represents how much a part weighs in kg and it is manually input, prices are in KRW/kg
    c_sup=M*157300 #M represents how much a support structure weighs in kg and it is manually input, prices are in KRW/kg
    c_scrap=0.15*cp_part #asked Mr Choi, he said it is around 15%

F=0.15 #an assumed value, it should be obtained by evaluation of ~50 builds in SLM single laser printer
#%% Cost of build parameters all in KRW

c_machrate=52246
c_gas=60000
c_rl=90000
c_filter_porous=400000

#%% Post-processing cost
c_mp=500000
c_wc=200000 #let it stay as constant for now
c_ht=100000 #this is an assumed value, it should be different for various materials

