mass_pounds = int(input())
height_inches = int(input())
mass_kg = mass_pounds * 0.453592
height_metres = height_inches * 0.0254
print(round(mass_kg / (height_metres ** 2), 2))