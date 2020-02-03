VERSION := 0.0.1

build:
	python3 setup.py build

clean:
	rm -rf build dist eljef_file_create.egg-info \
		eljef/__pycache__ eljef/file_create/__pycache__  \
		eljef/file_create/files/__pycache__  \
		eljef/file_create/licenses/__pycache__ \
		tests/__pycache__ tests/_trial_temp \
		.pytest_cache .coverage

depsinstall:
	pip install -r requirements.txt

depsupdate:
	pip install --upgrade -r requirements.txt

install:
	python3 setup.py install

lint:
	flake8 eljef/file_create
	pylint eljef/file_create

versionget:
	@echo $(VERSION)

versionset:
	@$(eval OLDVERSION=$(shell cat setup.py | awk -F"[=,]" '/version=/{gsub("\047", ""); print $$2}'))
	@sed -i -e "s/$(OLDVERSION)/$(VERSION)/" eljef/file_create/__version__.py
	@sed -i -e "s/version='$(OLDVERSION)'/version='$(VERSION)'/" setup.py
