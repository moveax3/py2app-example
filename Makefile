fullbuild: requirements clean makesetup buildapp

makesetup:
	py2applet --make-setup seleniumapp.py

buildapp:
	python3 setup.py py2app -A

clean:
	rm -rf build/
	rm -rf dist/

requirements:
	pip3 install -r requirements.txt
