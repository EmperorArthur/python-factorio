# These are some convenient Python tools for working with blueprints

## bp_archiver.py
### What:
This is a utility to convert blueprints and blueprint books into a convenient json archive.

### Why:
It's perfect for storing all your blueprints in git and having line by line change tracking.
It's also useful if you want to do some light editing (like changing a constant combinator's contents) without having to plop down a huge blueprint in game.

### How to use:
Simply create a file named 'Exchange Strings.txt', and put the exchange string for everything you want archived in it.  One string per line.
The program will create a `.json` file for each blueprint.  Blueprint books will be turned into directories with each blueprint inside them being a `.json` file.

## archive_to_exchange.py
### What / Why:
A program to convert all those archived blueprints and books back into exchange strings

### How to use:
Simply run the program wherever you ran `bp_archiver.py`.  It will create a file named 'Exchange Strings.txt' which contains all the blueprints and blueprint books.