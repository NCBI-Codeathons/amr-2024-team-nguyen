#!/bin/bash

SDIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd $SDIR

# Download Anaconda
#wget -N https://repo.anaconda.com/archive/Anaconda2-4.4.0-Linux-x86_64.sh
wget -N https://repo.anaconda.com/archive/Anaconda3-4.4.0-Linux-x86_64.sh
#wget -N https://repo.anaconda.com/archive/Anaconda3-2023.03-0-Linux-x86_64.sh

chmod +x Anaconda*.sh

###
# Download KMC
###

cd kmc
wget -N https://github.com/refresh-bio/KMC/releases/download/v3.2.2/KMC3.2.2.linux.x64.tar.gz
tar -xf KMC3.2.2.linux.x64.tar.gz
cd ..

###
# Set up Aytan Conda Environment
###

# Install Anaconda
# ./Anaconda3-4.4.0-Linux-x86_64.sh -b -p $(pwd)/aytan/conda3
# # Activate Anaconda and update packages for Aytan
# source aytan/conda3/bin/activate root
# conda env update -f aytan/conda3_aytan_frHist_min.yml --prune

###
# Set up Zou Conda Environment
###

# Install Anaconda for GPU environment
./Anaconda3-4.4.0-Linux-x86_64.sh -b -p $(pwd)/zou/conda3
# Activate Anaconda and update packages for zou
source zou/conda3/bin/activate root
conda env update -f zou/conda3_zou_frHist_min.yml --prune

sed "s/\.decode('utf-8')//g" zou/conda3/lib/python3.7/site-packages/tensorflow_core/python/keras/saving/hdf5_format.py | sed "s/\.decode('utf8')//g" > zou/conda3/lib/python3.7/site-packages/tensorflow_core/python/keras/saving/hdf5_format_new.py
cp zou/conda3/lib/python3.7/site-packages/tensorflow_core/python/keras/saving/hdf5_format.py zou/conda3/lib/python3.7/site-packages/tensorflow_core/python/keras/saving/hdf5_format_old.py
cp zou/conda3/lib/python3.7/site-packages/tensorflow_core/python/keras/saving/hdf5_format_new.py zou/conda3/lib/python3.7/site-packages/tensorflow_core/python/keras/saving/hdf5_format.py

# Install Anaconda for non-GPU environment
./Anaconda3-4.4.0-Linux-x86_64.sh -b -p $(pwd)/zou/conda3_nogpu
# Activate Anaconda and update packages for zou (no gpu)
source zou/conda3_nogpu/bin/activate root
conda env update -f zou/conda3_nogpu_zou_frHist_min.yml --prune

cp zou/conda3_nogpu/lib/python3.7/site-packages/tensorflow_core/python/keras/saving/hdf5_format.py zou/conda3_nogpu/lib/python3.7/site-packages/tensorflow_core/python/keras/saving/hdf5_format.py_old
sed "s/\.decode('utf-8')//g" zou/conda3_nogpu/lib/python3.7/site-packages/tensorflow_core/python/keras/saving/hdf5_format.py_old | sed "s/\.decode('utf8')//g" > zou/conda3_nogpu/lib/python3.7/site-packages/tensorflow_core/python/keras/saving/hdf5_format.py

###
# Set up Aytan_host Conda Environment
###

# Install Anaconda
# ./Anaconda2-4.4.0-Linux-x86_64.sh -b -p $(pwd)/aytan_plasHost/conda2
# # Activate Anaconda and update packages for Aytan_plasHost
# source aytan_plasHost/conda2/bin/activate root
# conda env update -f aytan_plasHost/conda2_aytan_plasHost_frHist_min.yml

###
# Clone Aytan bitbucket
###

# cd aytan
# git clone https://bitbucket.org/vlagri/sourcefinder.git
# cd ..

###
# Clone Zou github
###

cd zou
git clone https://github.com/BV-BRC-dependencies/zou-plasmid-prediction.git
cd ..

###
# Clone Aytan_host bitbucket
###

# cd aytan_plasHost
# git clone https://bitbucket.org/deaytan/plasmid-host-prediction.git
# cd ..

###
# Download Aytan models
###

# mkdir aytan/models
# cd aytan/models
# wget ftp://ftp.cbs.dtu.dk/public/CGE/databases/OriginFinder/*
# cd ../..

###
# Download Aytan_plasHost models
###

# mkdir aytan_plasHost/models
# cd aytan_plasHost/models
# wget ftp://ftp.cbs.dtu.dk/public/CGE/databases/PlasmidHostFinder/*.pkl
# cd ../..
