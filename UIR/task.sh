#!bin/bash
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --time=1000:00:00

/home/SHARED/Serpent/sss2_32 -omp 20 test
