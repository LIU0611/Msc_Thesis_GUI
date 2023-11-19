<img width="454" alt="image" src="https://github.com/LIU0611/Msc_Thesis_GUI/assets/80951587/1473599e-1f77-4744-9dc8-d1f0fc768dc7"># GUI Applications

Line_Intensity_GUI_4.0.py is the graphical user interface (GUI) code for Line Intensity Analysis. This is used to investigate the line intensity as a function of wavenumber, wavelength, and frequency for selected molecular species and isotopologies, and the user chooses whether the vertical axis is plotted in linear or log scale.
![Uploading image.png…]()

Absorption_Spectra_Voigt_GUI_4.0.py is the graphical user interface (GUI) code for Absorption Spectra Voigt for Mixed Gases. This GUI was developed to analyze absorption spectra using the Voigt profile for mixed gases, ensuring compatibility with the volume mixing ratio (VMR) in the original function (spectra of different molecular species on the same plots, such that shown are (i) individual spectra of different species in different colors and (ii) the total spectrum, which is the sum of individual spectra.), considering user-defined parameters such as volume mixing ratio, temperature, pressure, and path length for selected molecular species and isotopologies.

# Database

Laser spectroscopy databases contain line-specific information, including absorption line positions for species identification, line strength for concentration calculations, and line widths for trace gas quantification. They also include additional parameters for temperature and pressure-dependent corrections. The HITRAN (High-resolution transmission molecular absorption database) is a popular choice, featuring millions of absorption lines for 55 molecules, including different isotopologues, and is regularly updated.

The HITRAN data can be accessed using various tools:
  - The official HITRAN website (https://hitran.org/), where the Data Access tab allows plotting of spectral line positions and intensities (free registration required).
  - The user-friendly, free website (http://hitran.iao.ru/) also allows spectroscopic simulations, with some advanced features requiring registration.
  - Spectralcalc (http://www.spectralcalc.com), is a free portal for plotting spectral line positions and quick simulations, although access to the latest HITRAN edition and advanced features require registration and payment.

Understanding the documentation page of the HITRAN website before database usage is recommended, especially the HITRAN definitions of the line parameters.


