# Poppy
### Overview

book_database (or 'poppy') is a small program that takes a book and stores it in a database. it can either be stored as a 'not read yet', or as book that i've already read (in which case the program prompts for rating and thoughts, and if i have a file with book notes/thoughts)

### Objectives

- stop cluttering my google chrome with a bunch of tabs open of books that i want to read
- keep all the books i want to read in one place
- keep all the books i've ever read in one place + all the notes and thoughts i have of them
- learn about postgres and python
- cute project to put on resume/on website

### Usage

command line program. run poppy with a book title as an argument:
	1. checks if book can be found, if not user manually checks in open library website
	2. asks user if they've read the book or not
		1. if yes, then program prompts for a numerical rating and any comments/file of notes
		2. if not, program prompts for where did user get suggestion/idea to read book, and stores it into db
