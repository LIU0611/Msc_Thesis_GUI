from hapi.hapi import *
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import os
import csv
import ttkthemes as ttkth

from datetime import datetime

# Get the current date and time
current_time = datetime.now()

print(f"The HITRAN database current date is {current_time}") # database current date

# Define the molecules and their corresponding IDs for demonstration purposes
MOLECULES = {
    "H2O": 1,
    "CO2": 2,
    "O3": 3,
    "N2O": 4,
    "CO": 5,
    "CH4": 6,
    "O2": 7,
    "NO": 8,
    "SO2": 9,
    "NO2": 10,
    "NH3": 11,
    "HNO3": 12,
    "OH": 13,
    "HF": 14,
    "HCl": 15,
    "HBr": 16,
    "HI": 17,
    "ClO": 18,
    "OCS": 19,
    "H2CO": 20,
    "HOCl": 21,
    "N2": 22,
    "HCN": 23,
    "CH3Cl": 24,
    "H2O2": 25,
    "C2H2": 26,
    "C2H6": 27,
    "PH3": 28,
    "COF2": 29,
    "SF6": 30,
    "H2S": 31,
    "HCOOH": 32,
    "HO2": 33,
    "O": 34,
    "ClONO2": 35,
    "NO+": 36,
    "HOBr": 37,
    "C2H4": 38,
    "CH3OH": 39,
    "CH3Br": 40,
    "CH3CN": 41,
    "CF4": 42,
    "C4H2": 43,
    "HC3N": 44,
    "H2": 45,
    "CS": 46,
    "SO3": 47,
    "C2N2": 48,
    "COCl2": 49,
    "SO": 50,
    "CH3F": 51,
    "GeH4": 52,
    "CS2": 53,
    "CH3I": 54,
    "NF3": 55
}

ISOTOPOLOGUES = {
    "H2O": {
        "H216O": {"id": 1, "abundance": 0.997317},
        "H218O": {"id": 2, "abundance": 0.002000},
        "H217O": {"id": 3, "abundance": 3.718840e-4},
        "HD16O": {"id": 4, "abundance": 3.106930e-4},
        "HD18O": {"id": 5, "abundance": 6.230030e-7},
        "HD17O": {"id": 6, "abundance": 1.158530e-7},
        "D216O": {"id": 7, "abundance": 2.419740e-8}
    },
    "CO2": {
        "12C16O2": {"id": 1, "abundance": 0.984204},
        "13C16O2": {"id": 2, "abundance": 0.011057},
        "16O12C18O": {"id": 3, "abundance": 0.003947},
        "16O12C17O": {"id": 4, "abundance": 7.339890e-4},
        "16O13C18O": {"id": 5, "abundance": 4.434460e-5},
        "16O13C17O": {"id": 6, "abundance": 8.246230e-6},
        "12C18O2": {"id": 7, "abundance": 3.957340e-6},
        "17O12C18O": {"id": 8, "abundance": 1.471800e-6},
        "12C17O2": {"id": 9, "abundance": 1.368470e-7},
        "13C18O2": {"id": 10, "abundance": 4.446000e-8},
        "18O13C17O": {"id": 11, "abundance": 1.653540e-8},
        "13C17O2": {"id": 12, "abundance": 1.537450e-9}
    },
    "O3": {
        "16O3": {"id": 1, "abundance": 0.992901},
        "16O16O18O": {"id": 2, "abundance": 0.003982},
        "16O18O16O": {"id": 3, "abundance": 0.001991},
        "16O16O17O": {"id": 4, "abundance": 7.404750e-4},
        "16O17O16O": {"id": 5, "abundance": 3.702370e-4}
    },
    "N2O": {
        "14N216O": {"id": 1, "abundance": 0.990333},
        "14N15N16O": {"id": 2, "abundance": 0.003641},
        "15N14N16O": {"id": 3, "abundance": 0.003641},
        "14N218O": {"id": 4, "abundance": 0.001986},
        "14N217O": {"id": 5, "abundance": 3.692800e-4}
    },
    "CO": {
        "12C16O": {"id": 1, "abundance": 0.986544},
        "13C16O": {"id": 2, "abundance": 0.011084},
        "12C18O": {"id": 3, "abundance": 0.001978},
        "12C17O": {"id": 4, "abundance": 3.678670e-4},
        "13C18O": {"id": 5, "abundance": 2.222500e-5},
        "13C17O": {"id": 6, "abundance": 4.132920e-6}
    },

    "CH4": {
        "12CH4": {"id": 1, "abundance": 0.988274},
        "13CH4": {"id": 2, "abundance": 0.011103},
        "12CH3D": {"id": 3, "abundance": 6.157510e-4},
        "13CH3D": {"id": 4, "abundance": 6.917850e-6}
    },
    "O2": {
        "16O2": {"id": 1, "abundance": 0.995262},
        "16O18O": {"id": 2, "abundance": 0.003991},
        "16O17O": {"id": 3, "abundance": 7.422350e-4}
    },
    "NO": {
        "14N16O": {"id": 1, "abundance": 0.993974},
        "15N16O": {"id": 2, "abundance": 0.003654},
        "14N18O": {"id": 3, "abundance": 0.001993}
    },
    "SO2": {
        "32S16O2": {"id": 1, "abundance": 0.945678},
        "34S16O2": {"id": 2, "abundance": 0.041950},
        "33S16O2": {"id": 3, "abundance": 0.007464},
        "16O32S18O": {"id": 4, "abundance": 0.003793}
    },
    "NO2": {
        "14N16O2": {"id": 1, "abundance": 0.991616},
        "15N16O2": {"id": 2, "abundance": 0.003646}
    },
    "NH3": {
        "14NH3": {"id": 1, "abundance": 0.995872},
        "15NH3": {"id": 2, "abundance": 0.003661}
    },
    "HNO3": {
        "H14N16O3": {"id": 1, "abundance": 0.989110},
        "H15N16O3": {"id": 2, "abundance": 0.003636}
    },
    "OH": {
        "16OH": {"id": 1, "abundance": 0.997473},
        "18OH": {"id": 2, "abundance": 0.002000},
        "16OD": {"id": 3, "abundance": 1.553710e-4}
    },
    "HF": {
        "H19F": {"id": 1, "abundance": 0.999844},
        "D19F": {"id": 2, "abundance": 1.557410e-4}
    },
    "HCl": {
        "H35Cl": {"id": 1, "abundance": 0.757587},
        "H37Cl": {"id": 2, "abundance": 0.242257},
        "D35Cl": {"id": 3, "abundance": 1.180050e-4},
        "D37Cl": {"id": 4, "abundance": 3.773500e-5}
    },
    "HBr": {
        "H79Br": {"id": 1, "abundance": 0.506781},
        "H81Br": {"id": 2, "abundance": 0.493063},
        "D79Br": {"id": 3, "abundance": 7.893840e-5},
        "D81Br": {"id": 4, "abundance": 7.680160e-5}
    },
    "HI": {
        "H127I": {"id": 1, "abundance": 0.999844},
        "D127I": {"id": 2, "abundance": 1.557410e-4}
    },
    "ClO": {
        "35Cl16O": {"id": 1, "abundance": 0.755908},
        "37Cl16O": {"id": 2, "abundance": 0.241720}
    },
    "OCS": {
        "16O12C32S": {"id": 1, "abundance": 0.937395},
        "16O12C34S": {"id": 2, "abundance": 0.041583},
        "16O13C32S": {"id": 3, "abundance": 0.010531},
        "16O12C33S": {"id": 4, "abundance": 0.007399},
        "18O12C32S": {"id": 5, "abundance": 0.001880},
        "16O13C34S": {"id": 6, "abundance": 4.671760e-4}
    },
    "H2CO": {
        "H212C16O": {"id": 1, "abundance": 0.986237}
    },
    "HOCl": {
        "H16O35Cl": {"id": 1, "abundance": 0.755790},
        "H16O37Cl": {"id": 2, "abundance": 0.241683}
    },
    "N2": {
        "14N2": {"id": 1, "abundance": 0.992687},
        "14N15N": {"id": 2, "abundance": 0.007299}
    },
    "HCN": {
        "H12C14N": {"id": 1, "abundance": 0.985114},
        "H13C14N": {"id": 2, "abundance": 0.011068},
        "H12C15N": {"id": 3, "abundance": 0.003622}
    },
    "CH3Cl": {
        "12CH335Cl": {"id": 1, "abundance": 0.748937},
        "12CH337Cl": {"id": 2, "abundance": 0.239491}
    },
    "H2O2": {
        "H216O2": {"id": 1, "abundance": 0.994952}
    },
    "C2H2": {
        "12C2H2": {"id": 1, "abundance": 0.977599},
        "H12C13CH": {"id": 2, "abundance": 0.021966},
        "H12C12CD": {"id": 3, "abundance": 3.045500e-4}
    },
    "C2H6": {
        "12C2H6": {"id": 1, "abundance": 0.976990},
        "12CH313CH3": {"id": 2, "abundance": 0.021953}
    },
    "PH3": {
        "31PH3": {"id": 1, "abundance": 0.999533}
    },
    "COF2": {
        "12C16O19F2": {"id": 1, "abundance": 0.986544},
        "13C16O19F2": {"id": 2, "abundance": 0.011084}
    },
    "H2S": {
        "H232S": {"id": 1, "abundance": 0.949884},
        "H234S": {"id": 2, "abundance": 0.042137},
        "H233S": {"id": 3, "abundance": 0.007498}
    },
    "HCOOH": {
        "H12C16O16OH": {"id": 1, "abundance": 0.983898}
    },
    "HO2": {
        "H16O2": {"id": 1, "abundance": 0.995107}
    },
    "O": {
        "16O": {"id": 1, "abundance": 0.997628}
    },
    "NO+": {
        "14N16O+": {"id": 1, "abundance": 0.993974}
    },
    "HOBr": {
        "H16O79Br": {"id": 1, "abundance": 0.505579},
        "H16O81Br": {"id": 2, "abundance": 0.491894}
    },
    "C2H4": {
        "12C2H4": {"id": 1, "abundance": 0.977294},
        "12CH213CH2": {"id": 2, "abundance": 0.021959}
    },
    "CH3OH": {
        "12CH316OH": {"id": 1, "abundance": 0.985930}
    },
    "CH3Br": {
        "12CH379Br": {"id": 1, "abundance": 0.500995},
        "12CH381Br": {"id": 2, "abundance": 0.487433}
    },
    "CH3CN": {
        "12CH312C14N": {"id": 1, "abundance": 0.973866}
    },
    "C4H2": {
        "12C4H2": {"id": 1, "abundance": 0.955998}
    },
    "HC3N": {
        "H12C314N": {"id": 1, "abundance": 0.963346}
    },
    "H2": {
        "H2": {"id": 1, "abundance": 0.999688},
        "HD": {"id": 2, "abundance": 3.114320e-4}
    },
    "CS": {
        "12C32S": {"id": 1, "abundance": 0.939624},
        "12C34S": {"id": 2, "abundance": 0.041682},
        "13C32S": {"id": 3, "abundance": 0.010556},
        "12C33S": {"id": 4, "abundance": 0.007417}
    },
    "SO3": {
        "32S16O3": {"id": 1, "abundance": 0.943434}
    },
    "C2N2": {
        "12C214N2": {"id": 1, "abundance": 0.970752}
    },
    "COCl2": {
        "12C16O35Cl2": {"id": 1, "abundance": 0.566392},
        "12C16O35Cl37Cl": {"id": 2, "abundance": 0.362235}
    },
    "SO": {
        "32S16O": {"id": 1, "abundance": 0.947926},
        "34S16O": {"id": 2, "abundance": 0.042050},
        "32S18O": {"id": 3, "abundance": 0.001901}
    },
    "CH3F": {
        "12CH319F": {"id": 1, "abundance": 0.988428}
    },
    "GeH4": {
        "74GeH4": {"id": 1, "abundance": 0.365172},
        "72GeH4": {"id": 2, "abundance": 0.274129},
        "70GeH4": {"id": 3, "abundance": 0.205072},
        "73GeH4": {"id": 4, "abundance": 0.077552},
        "76GeH4": {"id": 5, "abundance": 0.077552}
    },
    "CS2": {
        "12C32S2": {"id": 1, "abundance": 0.892811},
        "32S12C34S": {"id": 2, "abundance": 0.079210},
        "32S12C33S": {"id": 3, "abundance": 0.014094},
        "13C32S2": {"id": 4, "abundance": 0.010031}
    },
    "CH3I": {
        "12CH3127I": {"id": 1, "abundance": 0.988428}
    }
}

def wavenumber_to_wavenumber(lower, upper):
    return lower, upper, lambda x: x  # No conversion needed for wavenumber

def wavelength_to_wavenumber(lower, upper):
    return 1e4 / upper, 1e4 / lower, lambda x: 1e4 / np.array(x)  # Convert wavenumber to wavelength

def frequency_to_wavenumber(lower, upper):
    return lower * 1e9 / (3e10), upper * 1e9 / (3e10), lambda x: np.array(x) * 3e10 / 1e9  # Convert wavenumber to frequency

unit_conversion_map = {
    "Wavenumber (cm-1)": wavenumber_to_wavenumber,
    "Wavelength (μm)": wavelength_to_wavenumber,
    "Frequency (GHz)": frequency_to_wavenumber
}

def on_molecule_selected(*args):
    # Clear the isotopologue dropdown
    print(f'Molecule selected: {molecule_var.get()}')
    isotopologue_dropdown['values'] = []
    isotopologue_var.set('')

    # Update the isotopologue dropdown based on the selected molecule
    molecule = molecule_var.get()
    if molecule in ISOTOPOLOGUES:
        isotopologues = list(ISOTOPOLOGUES[molecule].keys())
        isotopologue_dropdown['values'] = isotopologues
    root.update()


def download_data(*args):
    molecule = molecule_var.get()
    isotopologue = isotopologue_var.get()

    lower_bound = float(lower_bound_var.get())
    upper_bound = float(upper_bound_var.get())

    unit_conversion_func = unit_conversion_map[unit_var.get()]
    lower_bound, upper_bound, x_conversion_func = unit_conversion_func(lower_bound, upper_bound)

    db_begin('data')

    try:
        filename = f'{molecule}_{isotopologue}_{lower_bound}_{upper_bound}.csv'
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['X', 'Y'])  # header row
            if isotopologue == "All":
                x_common = np.linspace(lower_bound, upper_bound, 1000)  # Common x-values
                y_total = np.zeros_like(x_common)

                for iso, data in ISOTOPOLOGUES[molecule].items():
                    try:
                        fetch(molecule, MOLECULES[molecule], data["id"], lower_bound, upper_bound)
                        x, y = getStickXY(molecule)
                        x = x_conversion_func(x)
                        y_interp = np.interp(x_common, x, y, left=0, right=0)  # Interpolate y-values to common x-values
                        y_total += y_interp * data["abundance"]
                    except:
                        # If data retrieval fails for an isotopologue, skip it and continue
                        continue
                for x_val, y_val in zip(x_common, y_total):
                    writer.writerow([x_val, y_val])
            else:
                isotopologue_group = ISOTOPOLOGUES[molecule][isotopologue]["id"]
                fetch(molecule, MOLECULES[molecule], isotopologue_group, lower_bound, upper_bound)
                x, y = getStickXY(molecule)
                x = x_conversion_func(x)
                for x_val, y_val in zip(x, y):
                    writer.writerow([x_val, y_val])
        messagebox.showinfo("Data Downloaded", f"Data has been downloaded to {os.path.abspath(filename)}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def fetch_and_plot():
    molecule = molecule_var.get()
    isotopologue = isotopologue_var.get()

    lower_bound = float(lower_bound_var.get())
    upper_bound = float(upper_bound_var.get())
    y_axis = y_axis_var.get()

    unit_conversion_func = unit_conversion_map[unit_var.get()]
    lower_bound, upper_bound, x_conversion_func = unit_conversion_func(lower_bound, upper_bound)

    db_begin('data')

    try:
        if isotopologue == "All":
            x_common = np.linspace(lower_bound, upper_bound, 1000)  # Common x-values
            y_total = np.zeros_like(x_common)

            for iso, data in ISOTOPOLOGUES[molecule].items():
                try:
                    fetch(molecule, MOLECULES[molecule], data["id"], lower_bound, upper_bound)
                    x, y = getStickXY(molecule)
                    x = x_conversion_func(x)
                    y_interp = np.interp(x_common, x, y, left=0, right=0)  # Interpolate y-values to common x-values
                    y_total += y_interp * data["abundance"]

                    # TODO: Use VMR to replace the abundance, or make a new table column para when Choosing ALL)
                except:
                    # If data retrieval fails for an isotopologue, skip it and continue
                    continue

            plt.plot(x_common, y_total)
        else:
            isotopologue_group = ISOTOPOLOGUES[molecule][isotopologue]["id"]
            fetch(molecule, MOLECULES[molecule], isotopologue_group, lower_bound, upper_bound)
            x, y = getStickXY(molecule)
            x = x_conversion_func(x)
            plt.plot(x, y)

        plt.title(f"Stick Spectrum of {molecule}")
        plt.xlabel(unit_var.get())
        plt.ylabel("Intensity (cm-1 mol-1 cm2)")
        if y_axis.lower() == 'log':
            plt.yscale('log')
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = ttkth.ThemedTk(theme="Arc")
root.title("Line Intensity GUI 4.0")

# Create and set variables
molecule_var = tk.StringVar()
isotopologue_var = tk.StringVar()
lower_bound_var = tk.StringVar()
upper_bound_var = tk.StringVar()
y_axis_var = tk.StringVar(value="Linear")
unit_var = tk.StringVar(value="Wavenumber (cm-1)")

# Create widgets
ttk.Label(root, text="Choose your molecule:").grid(row=0, column=0, padx=10, pady=5)
molecule_dropdown = ttk.Combobox(root, textvariable=molecule_var, values=list(MOLECULES.keys()))
molecule_dropdown.grid(row=0, column=1, padx=10, pady=5)
molecule_dropdown.bind("<<ComboboxSelected>>", on_molecule_selected)

ttk.Label(root, text="Choose Isotopologue:").grid(row=1, column=0, padx=10, pady=5)
isotopologue_dropdown = ttk.Combobox(root, textvariable=isotopologue_var)
isotopologue_dropdown.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Choose your lower bound:").grid(row=2, column=0, padx=10, pady=5)
ttk.Entry(root, textvariable=lower_bound_var).grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Choose your upper bound:").grid(row=3, column=0, padx=10, pady=5)
ttk.Entry(root, textvariable=upper_bound_var).grid(row=3, column=1, padx=10, pady=5)

ttk.Label(root, text="Scale:").grid(row=4, column=0, padx=10, pady=5)
ttk.Combobox(root, textvariable=y_axis_var, values=["Linear", "Log"]).grid(row=4, column=1, padx=10, pady=5)

ttk.Label(root, text="Choose unit type:").grid(row=5, column=0, padx=10, pady=5)
ttk.Combobox(root, textvariable=unit_var, values=["Wavenumber (cm-1)", "Wavelength (μm)", "Frequency (GHz)"]).grid(row=5, column=1, padx=10, pady=5)

ttk.Button(root, text="Fetch and Plot", command=fetch_and_plot).grid(row=6, column=0, columnspan=2, pady=20)

ttk.Button(root, text="Download Data", command=download_data).grid(row=7, column=0, columnspan=2, pady=20)

molecule_var.trace("w", on_molecule_selected)

root.mainloop()
