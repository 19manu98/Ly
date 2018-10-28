# Lyrics Finder

A program that returns the lyrics to the given song title.

## Usage
Assuming `/path/to/ly.py` is `$PWD/ly.py` and `python3` is installed, run the following

```bash
$ python3 ly.py song_tile
```

## Feature: error tolerance

#### Scenario 0 : *yeah, the song title is*

```bash 
$ python3 ly.py the man who sold the world
```

#### Output
```
Nirvana - The Man Who Sold The World

We passed upon the stair
... [lyrics continues]

Oh no, not me
We never lost control
You're face to face
With the man who sold the world

... [lyrics continues]
```

#### Scenario 1 : *Erm.. I can't remember the song title, but it's something like..*

```bash 
$ python3 ly.py the woman who sailed the world
```

#### Output
```
Nirvana - The Man Who Sold The World

We passed upon the stair
... [lyrics continues]

Oh no, not me
We never lost control
You're face to face
With the man who sold the world

... [lyrics continues]
```

## Tips

Use `python3 ly.py` with Unix's `less` command 👻

#### Approach 0
in `$HOME/.alias` (alias file [sourced](http://www.theunixschool.com/2012/04/what-is-sourcing-file.html) in my `$HOME/.bashrc`), I added

```bash
function ly() {
	python3 /path/to/ly.py $@ | less
}
```
#### Approach 1
Alternatively I could have done the following

1. Make `ly.py` executable with `chmod 7xx /path/to/ly.py`

2. Add `#!/usr/bin/env python3` as the first line of code in `ly.py`.

3. Create a symbolic link to `ly.py` in a path that exists in the env. variable`$PATH`. (`$HOME/.local/bin` recommended).

   3.0. assuming `$HOME/.local/bin` is in `$PATH`

   verify by running 
   
```bash 
$ echo $PATH | grep -e "[$HOME|~]/.local/bin" --color=always
```
   **if there is match, skip to 3.1** else run the following first
   
```bash 
   $ mkdir -p $HOME/.local/bin && echo "export PATH=$PATH:$HOME/.local/bin" >> ~/.bashrc
```
   3.1. Create the symlink by running 
   
```bash 
$ ln -sf "/path/to/ly.py" "$HOME/.local/bin/ly"`
```
#### Usage

With either approaches `ly.py` should be executed as

```bash
$ ly song_title
```