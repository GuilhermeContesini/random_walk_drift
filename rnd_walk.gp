reset


set terminal eps enhanced
set output "rng_walk.eps"
set encoding iso_8859_1

data_points="walk.dat"
plot data_points u 1:2 lw 0.01

reset