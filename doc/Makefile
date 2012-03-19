#default: pdf
#default: run pdf
default: pdf diff figures_png
################################################
figures:
	python fig_Sanz12JNP.py
	cd results/; echo "Creating figure 1 in results/"; montage figure1A.png figure1B.png figure1C.png morphing-B_angle-0_1.png morphing-B_angle-1_0.png morphing-B_angle-10_0.png -geometry 564x512 ../figure1.pdf
	cd results/; echo "Creating figure 2 in results/"; montage figure2A.png figure2B.png figure2C.png -geometry 564x512 ../figure2.pdf
	cd results/; echo "Creating figure 3 in results/"; montage figure3A.png figure3B.png figure3C.png grating.png aperture.png grating-rdk.png -geometry 564x512 ../figure3.pdf
	cd results/; echo "Creating figure 4 in ../results/"; montage figure4A.png figure4B.png figure4C.png grating-B_sf-0_05.png grating-B_sf-0_15.png grating-B_sf-0_4.png -geometry 564x512 ../figure4.pdf
	cd results/; echo "Creating figure 5 in results/"; montage figure5A.png figure5B.png figure5C.png grating-noise.png plaid.png counterphase_grating.png -geometry 564x512 ../figure5.pdf

################################################
%.jpg: %.pdf
	convert $< $@
%.png: %.pdf
	convert $< $@

################################################
# LaTeX stuff
SRC = MotionClouds

bib_citeulike:
	wget "http://www.citeulike.org/bibtex/user/LaurentPerrinet/tag/sanz12jnp?fieldmap=posted-at:date-added&do_username_prefix=0&key_type=4" -O MotionClouds.bib

edit_linux: linux_edit
linux_edit: 
	texmaker $(SRC).tex &
	gedit Makefile &

edit_mac: mac_edit
mac_edit: 
	open $(SRC).tex
	open Makefile 


pdf: $(SRC).pdf
LATEXMK = latexmk -pdf

$(SRC).pdf: $(SRC).tex bib_citeulike figures
	$(LATEXMK) $(SRC)

################################################
# post-production

diff: $(SRC).tex
	latexdiff /Users/lup/Desktop/RTC/12-03-07_MotionClouds\ resubmission/MotionClouds.tex  $(SRC).tex > diff.tex
	# latexdiff /Users/lup/Desktop/RTC/12-01-31_MotionClouds\ resubmission/main_MotionClouds.tex /Users/lup/Desktop/12-03-07_MotionClouds\ resubmission/MotionClouds.tex   > diff.tex
	latexmk -pdf diff.tex

figures_png: figure1.png figure2.png figure3.png figure4.png figure5.png

################################################
# cleaning macros

touch:
	touch *.tex *py
clean: # careful! this is quite radical!
	rm -fr *.fff *.lof *.dvi *.ps  *.pdf  *.bib *.out *.log *.aux *.bbl *.blg *.snm *.nav *.toc *.synctex.gz *.fdb_latexmk diff* results

.PHONY: clean

