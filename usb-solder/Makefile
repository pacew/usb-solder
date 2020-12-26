PROJ=usb-solder

ZIP=$(PROJ).zip

BOM=$(PROJ)_bom_jlc.csv

all: $(ZIP) $(BOM)

GERBS = $(PROJ)-B_Cu.gbr \
	$(PROJ)-B_Mask.gbr \
	$(PROJ)-B_Paste.gbr \
	$(PROJ)-B_SilkS.gbr \
	$(PROJ).drl \
	$(PROJ)-Edge_Cuts.gbr \
	$(PROJ)-F_Cu.gbr \
	$(PROJ)-F_Mask.gbr \
	$(PROJ)-F_Paste.gbr \
	$(PROJ)-F_SilkS.gbr \
	$(PROJ)-In1_Cu.gbr \
	$(PROJ)-In2_Cu.gbr

.PHONY: $(ZIP)
$(ZIP): $(GERBS)
	rm -f $(ZIP)
	zip $(ZIP) $(GERBS)
	ls -l $(ZIP)

PDIR=~/.pyenv/versions/3.7.8/bin
$(BOM): $(ZIP)
	$(PDIR)/jlc-kicad-tools .
	ls -l $(BOM)
