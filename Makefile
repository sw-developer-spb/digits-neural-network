.ONESHELL:
.PHONY: install env denv run update clean

#ACTIVATE_LINUX:=. ./venv/bin/activate
#ACTIVATE_ENV:=source ./env.sh
venv_activate = venv/bin/activate

install:
	python3 -m venv ./venv; \
	chmod +x ./venv/bin/activate; \
	source $(venv_activate); \
	pip3 install -r requirements.txt
env:
	@echo "Run \nsource ./venv/bin/activate\n in shell"
	#source $(venv_activate);
	#python3 main.py
denv:
	@echo "Run \ndeactivate\n in shell"
run:
	./run.sh
update:
	#. ./venv/bin/activate
	source $(venv_activate);
	python3 -m  pipreqs.pipreqs .
clean:
	rm -rf venv
	find -iname "*.pyc" -delete


