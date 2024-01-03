cyl_radius = float(input("Enter the radius of cylinder: "))
cyl_height = float(input("Enter the height of cylinder: "))
cyl_sarea = (2 * (22/7) * cyl_radius * cyl_height) + (2 * (22/7) * (cyl_radius ** 2))
cyl_volume = (22/7) * (cyl_radius ** 2) * cyl_height
print("Surface area of cylinder =", cyl_sarea)
print("Volume of cylinder =", cyl_volume)
