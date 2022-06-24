#%% Asking for physics input values (database collection)
customer_name=input("Enter customer name:")

hatch_distance_str=input("Enter hatch distance:")
hatch_distance=int(hatch_distance_str)

layer_thickness_str=input("Enter layer thickness in um:")
layer_thickness=int(layer_thickness_str)

number_of_layers_str=input("Enter number of layers:")
number_of_layers=int(number_of_layers_str)

scan_speed_str=(input("Enter scan speed in mm/s")
scan_speed=int(scan_speed_str)
#%% Asking for physics input values (actually used for cost estimation & database collection)
part_volume_str=input("Enter part volume in mm3:")
part_volume=int(part_volume_str)

support_vol_str=input("Enter support volume in mm3:")
support_vol=int(support_vol_str)

bounding_box_str=input("Enter bounding box volume in mm3:")
bounding_box=int(bounding_box_str)

part_surface_area_str=input("Enter part surface area in mm2")
part_surface_area=int(part_surface_area_str)

material_type=input