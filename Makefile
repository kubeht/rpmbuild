all:
	@echo "Probable Targets:"
	@echo
	@(cd SPECS && ls *.spec) | sed s'/.spec//' 

%:
	echo '%_topdir $(shell pwd)' > ~/.rpmmacros
	echo '%_sourcedir $(shell pwd)/SOURCES/$@' >> ~/.rpmmacros
	rpmbuild --define "date $(shell date +%Y%m%d%H%M%S)" -bb SPECS/$@.spec
	rm -f ~/.rpmmacros

# vim: set noexpandtab
