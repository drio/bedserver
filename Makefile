
publish:
	rm -rf *.egg* dist
	cp $$HOME/.pypirc.drio $$HOME/.pypirc
	python setup.py sdist upload

.PHONY: publish
