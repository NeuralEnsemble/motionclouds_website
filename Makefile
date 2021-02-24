default: build deploy

build:
	nikola build

deploy:
	nikola deploy

clean:
	sh clean.sh
