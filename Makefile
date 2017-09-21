all: combine

combine: build/build.js

purescript: purescript/purescript.js
	cd purescript; bower install
	cd purescript; pulp build
	cd purescript; purs bundle -o purescript.js -n Purescript output/**/*.js

typescript: ts/tsc.js
	cd ts; bower install
	cd ts; tsc

build/build.js: build purescript/purescript.js ts/tsc.js
	./compressjs.sh purescript/purescript.js ts/tsc.js build/build.js

build:
	mkdir -p build

.PHONY: all combine purescript typescript
