# Lyrics Finder

A program that returns the lyrics to the given song title.

## Dependencies (IMPORTANT)

If you don't have these dependencies, install them first. else, continue to [Usage](#Usage).

[python3.x.x](https://www.python.org/downloads/)

```bash
$ command to install python3.x.x goes here
```

[BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) ensure for python3.x.x, and not python2.x.x.

```bash
$ sudo pip install bs4
```

## Usage

```bash
$ python3 /path/to/ly.py song title goes here
```

## Features

`NS`: Not Started,`S`: Started, `W`: Works(partially)/Workaround, `WAI`: Works As Intended, `B`: Broken/Bug, `A`: Assignee.

| Name                                                    | NS | S   | W   | WAI | B   | A                                        |
|:--------------------------------------------------------|:--:|:---:|-----|:---:|:---:|------------------------------------------|
| Output the lyrics of given song title                   |    |     |     | [X] |     |                                          |
| Error tolerance in title name                           |    |     |     | [X] |     |                                          |
| Only display the text surrounding a specific keyword    |    |     | [X] |     |     |                                          |
| Search the lyrics elsewhere on 404                      |    |     | [X] |     |     |                                          |
| Catches false positives when the song title is giberish |    |     |     |     | [X] |                                          |
| Log indexed urls to a file, e.g /tmp/ly/log/fail.log    |    | [X] |     |     |     | [@19manu98](https://github.com/19manu98) |



### Error tolerance examples
### case _0_: *yeah, the song title is..*

```bash 
$ python3 ly.py the man who sold the world
```

### Output
```
Nirvana - The Man Who Sold The World Lyrics 

We passed upon the stair
We spoke of was and when
Although I wasn't there
He said I was his friend
Which came as a surprise

etc.
```

### case _1_: *Erm.. can't remember the title.. erm?.. it's something like..*

```bash 
$ python3 ly.py the woman who sailed the world
```

### Output
```
Nirvana - The Man Who Sold The World Lyrics 

We passed upon the stair
We spoke of was and when
Although I wasn't there
He said I was his friend
Which came as a surprise

etc.
```

## Tips

Create [a function](https://github.com/tati-z/.dotfiles/blob/577c4d310f86aea17908ec4c01372a456345b5f6/.alias#L54 "change to correct path") that pipes the output of `ly.py` to Unix's `less` command to extend its features. 👻
### Result

```bash
$ ly song title goes here
```

Use  Unix's `grep` with [lyf](https://github.com/tati-z/.dotfiles/blob/9095247f54d12280a3118600d65598ee78191ab9/.alias#L62) to only output lyrics surrounding a given keyword.

e.g: I only want sentenses surrounding the keyword **froid** in Louane's [Immobile](https://youtu.be/1MVl9uzdl8k "Play").

```bash
$ lyf froid immobile
```

### Result

```
C'est comme prendre une autoroute
Oublier ce que l'on redoute
C'est quand je me retrouve seul
Que j'ai froid

J'avance au plus près de ce gouffre
Et je sens le vent qui me pousse
Je sais que je ne suis pas encore prête
J'essaye d'effacer mes angoisses
Ces peines, ces horreurs qui me passent
Et s'enfoncent au plus profond de mon être
Mais c'est pas si facile
Et face à toi je pile
Oui je reste immobile
```

## How ly.py works
_is typing..._
