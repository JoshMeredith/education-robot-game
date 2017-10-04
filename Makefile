all: build/build.js web/static/js/build.js

purescript/purescript.js: $(wildcard purescript/src/**.purs)
	cd purescript; bower install
	cd purescript; pulp build --skip-entry-point -m Interpreter -m Parser --to purescript.js

typescript: ts/tsconfig.json $(wildcard ts/src/**.ts)
	cd ts; bower install
	cd ts; tsc

build/build.js: build purescript/purescript.js typescript
	uglifyjs ts/src/*.js purescript/purescript.js -o build/build.js

web/static/js/build.js: build/build.js web/static/js
	cp build/build.js web/static/js/build.js

web/static/js:
	mkdir -p web/static/js

build:
	mkdir -p build

build/test.js: build/build.js ts/tsconfig-test.json
	tsc -p ts/tsconfig-test.json
	uglifyjs $< ts/tests/*.js -o $@

test: build/test.js
	mocha $<

clean:
	rm -r build
	rm -r purescript/bower_components
	rm -r purescript/output
	rm -r purescript/purescript.js
	rm -r purescript/.pulp-cache
	rm -r ts/src/*.js

.PHONY: all combine typescript clean
