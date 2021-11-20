# MsNB-MCNP-AutoDeck
This is a PYTHON script that automatically generates the MCNP input deck that models the MsNB that I am studying for my M.S. Thesis. You may copy, edit, etc. for your own purposes without requesting permission.  This script is optimized for use in Windows, as it writes .bat files rather than .sh files. If you run a unix based OS, you may wish to edit the master file to write .sh files instead.

Adjust the control drum orientations you are interested in by changing the list DEG. Adjust the mole fraction of fuel salt in the fuel salt-coolant salt mixture and fuel salt enrichment by changing the floats frac and enrich respectively.

I reccomend using the build.bat file to generate your input decks, as it automatically deletes obsolete directories, but you can run the master file (deck.py) directly if you first delete all subdirectories. 

I reccomend using run.bat (generated in main directory to automatically run ALL of your input decks one after another) which also deletes obsolete files, to run the criticality model. 

I reccomend using plot.bat (generated in each subdirectory) to run the MCNP Plotter for each control drum orientation, as it deletes the obsolete files when you are done viewing the plotter.
