default: run doc
	
report_%.pdf: report_%.py MotionParticles.py
	    pyreport --double $< && open $@

run:
	for f in test_*.py; do python $(f); done
	for f in experiments_*.py; do python $(f); done
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

