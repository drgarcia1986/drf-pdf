clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

test: clean
	py.test

requirements: clean
	pip install -r requirements-dev.txt

release-patch:
	bumpversion patch

release-minor:
	bumpversion minor

release-major:
	bumpversion major
