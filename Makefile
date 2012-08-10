#.PHONY: clean-pyc

#all: clean-pyc

#test:
#	python runtests.py


clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

