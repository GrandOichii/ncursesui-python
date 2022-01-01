start:
	@python3 setup.py bdist_wheel
	@pip3 install -e .
	@echo Added module locally!