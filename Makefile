clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

test: clean
	py.test -x --cov-config .coveragerc --cov-report html --cov-report xml --cov-report term --cov drf_pdf/ tests/

test-debug: clean
	py.test -x --ipdb drf_pdf/ tests/

requirements: clean
	pip install -r requirements-dev.txt

release-patch:
	bumpversion patch

release-minor:
	bumpversion minor

release-major:
	bumpversion major
