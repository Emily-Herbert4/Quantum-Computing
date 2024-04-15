Code used in my senior project regarding the Deutsch–Jozsa algorithm using quantum optics

plotting - just python program to deal with data from runs
  1) reads in data (txt files) from folder data
  2) plots raw data and places pngs in plots
  3) removes data when we shift the waveplates, then plots and normalizes AB and AC coincidences. All saved in plots_cleaned
gates - used to guess oppeators that corspond to optical instruments
  1) gates.py - all opperators are there and used in other programs
  2) checking.py - accounts for rounding errors and checks if results are balanced, constant or neither
  3) any .ipynb me trying to guess different orders or gates 
