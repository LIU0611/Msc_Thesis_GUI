# Research Plan

The research plan consists of the following steps:

Step 0: Replicate Hitran Python API example code. (Completed)

Step 1: Plot line intensity and absorption spectra for selected species and isotopologues as a function of user-selected wavenumber/wavelength/frequency. Ensure the vertical axis can be toggled between linear and log scales.

Step 2: Enable plotting of spectra for gas mixtures, displaying individual spectra of different species in varying colors and the total spectrum.

Step 3: Introduce tools to identify spectral regions for target gas detection without spectral interference. This includes plotting the target gas absorption spectrum separately and the ratio of the target gas spectrum to the sum absorption spectrum of all other gases.

Bonus: Create a GIF showing spectral changes with pressure variations.


# Database

Laser spectroscopy databases contain line-specific information, including absorption line positions for species identification, line strength for concentration calculations, and line widths for trace gas quantification. They also include additional parameters for temperature and pressure-dependent corrections. The HITRAN (High-resolution transmission molecular absorption database) is a popular choice, featuring millions of absorption lines for 55 molecules, including different isotopologues, and is regularly updated.

The HITRAN data can be accessed using various tools:
  - The official HITRAN website (https://hitran.org/), where the Data Access tab allows plotting of spectral line positions and intensities (free registration required).
  - The user-friendly, free website (http://hitran.iao.ru/) also allows spectroscopic simulations, with some advanced features requiring registration.
  - Spectralcalc (http://www.spectralcalc.com), is a free portal for plotting spectral line positions and quick simulations, although access to the latest HITRAN edition and advanced features require registration and payment.

Understanding the documentation page of the HITRAN website before database usage is recommended, especially the HITRAN definitions of the line parameters.


