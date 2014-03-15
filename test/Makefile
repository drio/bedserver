ALL: index

index:
	@for b in *.bed;do make -f ../Makefile $$b.gz.tbi; done

%.bed.gz: %.bed
	bgzip $<
	gzip -cd $@ > $<

%.bed.gz.tbi: %.bed.gz
	tabix -p bed $<

curl:
	curl 'http://localhost:5000/bedserver/api/v1.0/projects'
	@echo ""
	curl 'http://localhost:5000/bedserver/api/v1.0/samples/depth/18277?start=1100000&stop=1102000&chrm=Chr17&step=1&size=44'
	@echo ""
	curl 'http://localhost:5000/bedserver/api/v1.0/samples/snp_density/18277.YNPRC.Indian.chr1?start=2000000&stop=3000000&chrm=Chr1&step=1&size=44'
	@echo ""
	curl 'http://localhost:5000/bedserver/api/v1.0/samples/snp_density/18277.YNPRC.Indian.chr1?start=1&stop=240000000&chrm=Chr1&step=1&size=44'
	@echo ""


clean:
	rm -f *.bed.gz *.bed.gz.tbi

.PRECIOUS: %.bed.gz
.PHONY: clean index curl
