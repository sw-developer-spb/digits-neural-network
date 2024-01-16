# digits-neural-network

## install
python3 -m venv ./env 
./venv/bin/pip3 install -r requirements.txt
or
make install

## run
before every run use
source venv/bin/activate
python3 main.py
or
./run.sh
or
make run

## env
source venv/bin/activate
or
source ./env.sh

## denv
deactivate

## use trained data
uzip data.60000.trained.images.zip to ./data
and run

## use for training
delete ./data
source ./env.sh
python3 main.py -t num-of-images-for-training
