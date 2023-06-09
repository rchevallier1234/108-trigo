##
## EPITECH PROJECT, 2022
## Makefile
## File description:
## compile
##

all:
	ln -s 108trigo.py 108trigo
	chmod 777 108trigo
clean:
	rm -f 108trigo

fclean: clean

re:	fclean all
