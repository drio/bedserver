ALL: index

index:
	@for b in *.bed;do make -f ../Makefile $$b.gz.tbi; done

%.bed.gz: %.bed
	bgzip $<
	gzip -cd $@ > $<

%.bed.gz.tbi: %.bed.gz
	tabix -p bed $<

clean:
	rm -f *.bed.gz *.bed.gz.tbi

.PRECIOUS: %.bed.gz
.PHONY: clean index
