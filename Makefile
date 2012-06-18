default: run doc
	
report_%.pdf: report_%.py MotionParticles.py
	    pyreport --double $< && open $@

test:
	python test_color.py
	python test_export.py
	python test_orientation.py
	python test_radial.py
	python test_speed.py
run:
	for f in experiments_*.py; do python $(f); done
figures:
	for f in fig_*.py; do python $(f); done

doc: 
	@(cd doc && $(MAKE))
	
edit: 
	open Makefile &
	spe &

clean:
	touch *py
	rm -f results/* *.pyc

.PHONY: clean dist-clean all clean_white clean_sc clean_dist clean_tex

