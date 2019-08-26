import numpy as np 
import scipy as sp

import random as rng

def main():

	num_steps_int = 10000
	step_size_dbl_tpl = (1.0,1.0)
	drift_dbl_tpl = (0.7, 0.5)
	init_pos_dbl_tpl = (0.0,0.0)


	sum_x_pos_dbl = 0.0
	sum_x2_pos_dbl = 0.0
	sum_y_pos_dbl = 0.0
	sum_y2_pos_dbl = 0.0

	final_pos_dbl_tpl, transient_dbl_tpl_ary = \
	rng_2_d_walk(
		num_steps_int,
		step_size_dbl_tpl,
		drift_dbl_tpl
	)

	# print( final_pos_dbl_tpl )
	for i_int in np.arange(num_steps_int):

		sum_x_pos_dbl +=\
			transient_dbl_tpl_ary[i_int][0]

		sum_x2_pos_dbl +=\
			transient_dbl_tpl_ary[i_int][0]*transient_dbl_tpl_ary[i_int][0]

		sum_y_pos_dbl +=\
			transient_dbl_tpl_ary[i_int][1]

		sum_y2_pos_dbl +=\
			transient_dbl_tpl_ary[i_int][1]*transient_dbl_tpl_ary[i_int][1]

		print(transient_dbl_tpl_ary[i_int][0],"\t",transient_dbl_tpl_ary[i_int][1],)

	avg_x_dbl = sum_x_pos_dbl/num_steps_int
	avg_x2_dbl = sum_x2_pos_dbl/num_steps_int
	var_x_dbl = (avg_x2_dbl - avg_x_dbl*avg_x_dbl)/num_steps_int

	avg_y_dbl = sum_y_pos_dbl/num_steps_int
	avg_y2_dbl = sum_y2_pos_dbl/num_steps_int
	var_y_dbl = (avg_y2_dbl - avg_y_dbl*avg_y_dbl)/num_steps_int

	# print(
	# 	"\nMean(x): %0.3f" %avg_x_dbl,
	# 	# "\n<x2>:", avg_x2_dbl,
	# 	"\nVar(x): %0.3f" %var_x_dbl,
	# 	"\nMean(y): %0.3f" %avg_y_dbl,
	# 	# "\n<y2>:",avg_y2_dbl,
	# 	"\nVar(y): %0.3f" %var_y_dbl
	# )

def rng_2_d_walk(
	num_steps_int_,
	step_size_dbl_tpl = (1.0,1.0),
	drift_dbl_tpl_=(0.5,0.5),
	init_pos_dbl_tpl_=(0.0,0.0)
	):

	'''
	Return a 2-d random walk with n_steps_int_
	'''

	no_drift_dbl = 0.5
	( x_pos_dbl, y_pos_dbl ) = init_pos_dbl_tpl_[0], init_pos_dbl_tpl_[1]

	transient_dbl_tpl_ary = num_steps_int_*[(0.0,0.0)]

	for i_int in np.arange( 0, num_steps_int_ ):

		if( drift_dbl_tpl_[0] < rng.random() ):

			x_pos_dbl += step_size_dbl_tpl[0]

		else:

			x_pos_dbl += (-1)*step_size_dbl_tpl[0]

		if( drift_dbl_tpl_[1] < rng.random() ):

			y_pos_dbl += step_size_dbl_tpl[1]

		else:

			y_pos_dbl += (-1)*step_size_dbl_tpl[1]

		transient_dbl_tpl_ary[i_int] = (x_pos_dbl, y_pos_dbl)

	return( (x_pos_dbl, y_pos_dbl), transient_dbl_tpl_ary )

if __name__ == '__main__':
	main()