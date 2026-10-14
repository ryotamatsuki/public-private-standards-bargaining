MAIN=main
LATEXMK=latexmk

all: pdf

pdf:
	$(LATEXMK) -pdf -file-line-error -halt-on-error -interaction=nonstopmode $(MAIN).tex

clean:
	$(LATEXMK) -C $(MAIN).tex

.PHONY: all pdf clean
