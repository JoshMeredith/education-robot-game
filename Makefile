all: build/build.js

purescript/purescript.js: $(wildcard purescript/src/**/*.purs)
	cd purescript; bower install
	cd purescript; pulp build
	cd purescript; purs bundle -o purescript.js -n Purescript output/**/*.js

typescript:
	cd ts; bower install
	cd ts; tsc

build/build.js: build purescript/purescript.js typescript
	./compressjs.sh purescript/purescript.js ts/src/*.js build/build.js

build:
	mkdir -p build

clean:
	rm -r build
	rm -r purescript/bower_components
	rm -r purescript/output
	rm -r purescript/purescript.js
	rm -r purescript/.pulp-cache
	rm -r ts/tsc.js

.PHONY: all combine typescript clean
