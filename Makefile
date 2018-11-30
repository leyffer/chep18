DOC = template

$(DOC).pdf: $(DOC).tex
	pdflatex $(DOC)
	bibtex $(DOC)
	pdflatex $(DOC)
	pdflatex $(DOC)
	#dvipdf $(DOC)

clean:
	rm -f $(DOC).pdf $(DOC).aux $(DOC).toc $(DOC).bbl $(DOC).blg $(DOC).log
