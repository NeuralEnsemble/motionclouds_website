default: test experiments doc
	
report_%.pdf: report_%.py MotionParticles.py
	    pyreport --double $< && open $@

test:
	python test_color.py
	python test_grating.py
	python test_radial.py
	python test_speed.py
experiments:
	python experiment_B_sf.py
	python experiment_competing.py
	python experiment_smooth.py
	# python experiment_VSDI.py
figures:
	python fig_artwork_eschercube.py
	python fig_contrast.py
wiki:
	python fig_orientation.py
	python fig_ApertureProblem.py
	python fig_MotionPlaid.py

doc:
	@(cd doc && $(MAKE))
edit:
	open Makefile &
	spe &

# https://docs.python.org/2/distutils/packageindex.html
pypi_tags:
	git tag 0.1.1 -m "Adds a tag so that we can put this on PyPI."
	git push --tags origin master

pypi_push:
	python setup.py register

pypi_upload:
	python setup.py sdist bdist_wininst upload

pypi_docs: index.html
	zip web.zip index.html
	open http://pypi.python.org/pypi?action=pkg_edit&name=LogGabor

clean:
	touch *py
	rm -f results/* *.pyc


