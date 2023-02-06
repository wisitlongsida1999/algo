
#enclose with " " for prevent name was split by space
dirName = "$(n)"

all: createDir CreateFiles
	
createDir:
	@mkdir $(dirName)

CreateFiles:
	@touch $(dirName)/main.py $(dirName)/README.md $(dirName)/tst.py
