fullbuild: requirements buildapp

makesetup:
	py2applet --make-setup seleniumapp.py

buildapp:
	python2 setup.py py2app -A

buildportable:
	python2 setup.py py2app

clean:
	rm -rf build/
	rm -rf dist/

requirements:
	pip2 install -r requirements.txt
