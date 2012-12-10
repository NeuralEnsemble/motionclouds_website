default: test experiments figures doc
	
report_%.pdf: report_%.py MotionParticles.py
	    pyreport --double $< && open $@

test:
	python test_color.py
	python test_export.py
	python test_grating.py
	python test_radial.py
	python test_speed.py
experiments:
	python experiment_B_sf.py  
	python experiment_competing.py  
	python experiment_smooth.py
	# python experiment_VSDI.py	
figures:
	python fig_ApertureProblem.py     
	python fig_MotionPlaid.py         
	#python fig_artwork_eschercube.py  
	python fig_contrast.py            
	python fig_orientation.py


doc: 
	@(cd doc && $(MAKE))
	
edit: 
	open Makefile &
	spe &

clean:
	touch *py
	rm -f results/* *.pyc


