TEMPLATE_SCRIPT = template.py

.PHONY: all

all: create_structure

create_structure:
ifndef DAY
	$(error DAY is not set. Specify the day)
endif

	mkdir -p data/$(DAY)
	touch data/$(DAY)/part1.txt data/$(DAY)/part1-test.txt
	touch data/$(DAY)/part2.txt data/$(DAY)/part2-test.txt
	
	cp $(TEMPLATE_SCRIPT) $(DAY).py

