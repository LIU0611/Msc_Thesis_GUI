# Line Intensity GUI

Line_Intensity_GUI_4.0.py is the graphical user interface (GUI) code for Line Intensity Analysis. This is used to investigate the line intensity as a function of wavenumber, wavelength, and frequency for selected molecular species and isotopologies, and the user chooses whether the vertical axis is plotted in linear or log scale.

  <img width="410" alt="image" src="https://github.com/LIU0611/Msc_Thesis_GUI/assets/80951587/84da69e2-33fa-4337-a2a6-047cf21726b9">
  
  Figure 1: Line Intensity GUI Window
  
  <img width="362" alt="image" src="https://github.com/LIU0611/Msc_Thesis_GUI/assets/80951587/a8169136-0937-4364-a292-787783f07af3">
  
  Figure 2: Project Workflow for Line Intensity GUI Code
  
  <img width="454" alt="image" src="https://github.com/LIU0611/Msc_Thesis_GUI/assets/80951587/ed490291-6d0e-4a0b-a4c0-5d02212b4e09">
  
  Figure 3: Simulated HITRAN molecular absorption line Intensity of carbon monoxide. The P-branch is to the left of the gap at 2140(cm^-1), and the R-branch is on the right. (Plot by my Line Intensity GUI code)

# Absorption Spectra Voigt GUI

Absorption_Spectra_Voigt_GUI_4.0.py is the graphical user interface (GUI) code for Absorption Spectra Voigt for Mixed Gases. This GUI was developed to analyze absorption spectra using the Voigt profile for mixed gases, ensuring compatibility with the volume mixing ratio (VMR) in the original function (spectra of different molecular species on the same plots, such that shown are (i) individual spectra of different species in different colors and (ii) the total spectrum, which is the sum of individual spectra.), considering user-defined parameters such as volume mixing ratio, temperature, pressure, and path length for selected molecular species and isotopologies. Absorption_Spectra_Voigt_GUI_download_data.py is the graphical user interface (GUI) code for data download.

  <img width="542" alt="image" src="https://github.com/LIU0611/Msc_Thesis_GUI/assets/80951587/17c3529e-b26d-49c1-8505-a9e2d8957434">
  
  Figure 4: Absorption Spectra Voigt GUI Main Window
  
  <img width="471" alt="image" src="https://github.com/LIU0611/Msc_Thesis_GUI/assets/80951587/71db3226-07b5-4347-9f16-d3b53d7d851c">
  
  Figure 5: Absorption Spectra Voigt GUI Window for Adding a New Gas

  <img width="410" alt="image" src="https://github.com/LIU0611/Msc_Thesis_GUI/assets/80951587/96f40521-93cd-4adc-8b6a-eb28947a1027">

  Figure 6: Absorption Spectra Voigt GUI Window for Downloading Data
  
  <img width="455" alt="image" src="https://github.com/LIU0611/Msc_Thesis_GUI/assets/80951587/35bd5318-c069-4ee9-b443-a4d6cb8096f2">
  
  Figure 7: Comparison of Absorption Spectra Using Voigt Profiles for a Gas Mixture in the Range 929.5-932.0 cm^-1
  - Gases: H₂¹⁶O (VMR: 2.5×10^-3), ¹²C¹⁶O₂ (VMR: 4×10^-4), ¹⁴NH₃ (VMR: 1.5×10^-7)
  - Conditions: Path Length - 10 cm; Pressure - 1013.25 mbar; Temperature - 296 K


# Database

Laser spectroscopy databases contain line-specific information, including absorption line positions for species identification, line strength for concentration calculations, and line widths for trace gas quantification. They also include additional parameters for temperature and pressure-dependent corrections. The HITRAN (High-resolution transmission molecular absorption database) is a popular choice, featuring millions of absorption lines for 55 molecules, including different isotopologues, and is regularly updated.

The HITRAN data can be accessed using various tools:
  - The official HITRAN website (https://hitran.org/), where the Data Access tab allows plotting of spectral line positions and intensities (free registration required).
  - The user-friendly, free website (http://hitran.iao.ru/) also allows spectroscopic simulations, with some advanced features requiring registration.
  - Spectralcalc (http://www.spectralcalc.com), is a free portal for plotting spectral line positions and quick simulations, although access to the latest HITRAN edition and advanced features require registration and payment.

Understanding the documentation page of the HITRAN website before database usage is recommended, especially the HITRAN definitions of the line parameters.


