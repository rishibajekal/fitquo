.PHONY: all init local clean

all: init
	python server.py 8888 --debug=True

init:
	pip install -r requirements.txt

local: clean init
	python server.py 8888 --debug=True --mysql_host=localhost:3306 --mysql_database=fitquo --mysql_user=root --mysql_password=

clean:
	rm -rf dist *egg*
