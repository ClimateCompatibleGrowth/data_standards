import sys
sys.path.append('../..')

from SALib.analyze import sobol
from SALib.sample import saltelli
from SALib.util import read_param_file
from SALib.plotting.bar import plot as barplot
from financial import Model
import matplotlib.pyplot as plt

# Read the parameter range file and generate samples
problem = read_param_file('params.txt')

# Generate samples
param_values = saltelli.sample(problem, 1000, calc_second_order=True)

# Run the "model" and save the output in a text file
# This will happen offline for external models
model = Model()
Y = model.evaluate(param_values)

# Perform the sensitivity analysis using the model output
# Specify which column of the output file to analyze (zero-indexed)
Si = sobol.analyze(problem, Y, calc_second_order=True, conf_level=0.95, print_to_console=True)
# Returns a dictionary with keys 'S1', 'S1_conf', 'ST', and 'ST_conf'
# e.g. Si['S1'] contains the first-order index for each parameter,
# in the same order as the parameter file
# The optional second-order indices are now returned in keys 'S2', 'S2_conf'
# These are both upper triangular DxD matrices with nan's in the duplicate
# entries.
# Optional keyword arguments parallel=True and n_processors=(int) for parallel execution
# using multiprocessing

# First-order indices expected with Saltelli sampling:
# x1: 0.3139
# x2: 0.4424
# x3: 0.0

total, first, second = Si.to_df()

ax = barplot(total)

ax.set_yscale('log')

# Make the plot appear if not in Jupyter notebooks
plt.show()