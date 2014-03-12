
ALL: example.bed.gz.tbi

example.bed.gz: example.bed
	bgzip $<
	gzip -cd $@ > $<

example.bed.gz.tbi: example.bed.gz
	tabix -p bed example.bed.gz

clean:
	rm -f example.bed.gz example.bed.gz.tbi

.PHONY: clean
