cmd1:
	echo $@, hello  #this prints the command first before echoing

cmd2:
	@echo "$@" #this only prints the execution of the command

qweall: 
	@echo "This make line will not be printed"
	echo "But this will"

all: cmd1 cmd2
