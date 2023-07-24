#Raman shift >> Wavelength

Laser_excitation_wavelength = float(input('Plz input the Laser excitation wavelength, λex (nm): '))
Raman_Shift = float(input('Plz input the Raman shift in wavenumbers (cm^-1): '))
wavelength = 1 / ((1 / Laser_excitation_wavelength) - (Raman_Shift / (1E7)))
print('The Wavelength, λ (nm): ', wavelength)
