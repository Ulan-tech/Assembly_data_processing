inconel = 'inconel_slm'
maraging_steel = 'maraging_steel_slm'
ss316l = 'sus316l'
ti_grade2 = 'cp_ti'
ti64 = 'ti6al4V'
mat_cost_kg = 0

# %% Cost of build parameters all in KRW
F = 0.15  # an assumed value, it should be obtained by evaluation of ~50 builds in SLM single laser printer
c_machrate = 52246
c_gas = 60000
c_rl = 90000
c_filter_porous = 400000

# %% Post-processing cost
c_mp = 50000
c_wc = 200000  # let it stay as constant for now
c_ht = 100000  # this is an assumed value, it should be different for various materials

# %%Input entries
number_of_parts = int(input("Number of a part-1: "))
t_build = int(input("Total build time from the SLM machine: "))

material_type = {
    "inconel": 157300 * 8e-6,  # WON/kg*kg/m3,
    "maraging_steel": 206800 * 8.0e-6,
    "ss316l": 205000 * 8.0e-6,
    "ti_grade2": 601700 * 4.51e-6,
    "ti64": 460000 * 4.43e-6,
}

m_type, different_parts = 'maraging_steel', 3
mat_cost = material_type.__getitem__(m_type)
c_machine = t_build * c_machrate
cost_part = part_volume * mat_cost
cost_sup = support_vol * mat_cost
cost_scrap = cost_part * 0.15