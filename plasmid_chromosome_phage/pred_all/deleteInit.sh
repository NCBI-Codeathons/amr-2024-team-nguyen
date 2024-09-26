###
#
# THIS SCRIPT WILL DELETE EVERYTHING IN THE INIT SCRIPT!
#
###

# get script directory and change directory to it
SDIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SDIR

# remove Anaconda installation scripts
rm Anaconda*.sh

# remove aytan conda3 install
rm -rf aytan/conda3

# remove zou conda3 install
rm -rf zou/conda3 zou/conda3_nogpu

# remove aytan_plasHost conda2 install
rm -rf aytan_plasHost/conda2

# remove aytan bitbucket
rm -rf aytan/sourcefinder

# remove zou github
rm -rf zou/zou-plasmid-prediction

# remove aytan_plasHost bitbucket
rm -rf aytan_plasHost/plasmid-host-prediction

# remove aytan models
rm -rf aytan/models

# remove aytan_plasHost models
rm -rf aytan_plasHost/models
rm -rf kmc/KMC3.2.2.linux.x64.tar.gz kmc/bin kmc/include