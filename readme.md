# Lyrics Finder

A program that returns the lyrics to the given song title.

## Dependencies

[python3](https://www.python.org/downloads/)

```bash
$ my_platform_package_manager install python3.x
```

[bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

```bash
$ sudo pip3.x install bs4
```

Where `x` can take the value of the preferred python3 version.

## Usage

```bash
$ python3 /path/to/ly.py song_tile
```

## Features

`NS`: Not Started,`S`: Started, `W`: Works/Workaround, `WAA`: Works As intended, `B`: Broken.

| Name                                                                          | NS     | S   | W   | WAA | B |   |
|:------------------------------------------------------------------------------|:------:|:---:|-----|:---:|:-:|---|
| Output the lyrics of given song title                                         |        |     |     | [X] |   |   |
| Error tolerance in title name                                                 |        |     |     | [X] |   |   |
| Only display the text surrounding a specific keyword                          |        |     | [X] |     |   |   |
| Search the lyrics elsewhere on 404                                            | [X]    |     |     |     |   |   |

Error tolerance examples
### case _0_: *yeah, the song title is..*

```bash 
$ python3 ly.py the man who sold the world
```

### Output
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

### case _1_: *Erm.. can't remember the song title, but it's something like..*

```bash 
$ python3 ly.py the woman who sailed the world
```

### Output
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

Use `ly.py` with Unix's `less` command 👻 using the following bash function.
```bash
function ly() {
	python3 /path/to/ly.py $@ | less
}
```
### Result

```bash
$ ly song_title
```

Use  Unix's `grep` with [lyf](https://github.com/tati-z/.dotfiles/blob/9095247f54d12280a3118600d65598ee78191ab9/.alias#L62) to only output the lyrics surrounding a given keyword.

e.g: I only want the lyrics surrounding the keyword **beautiful** in _Pearl Jam's Black_.

```bash
$ lyf beautiful black pearl
```

#### Result

```

Uh huh... uh huh... ooh...

I know someday you'll have a beautiful life,
I know you'll be a star in somebody else's sky,
But why, why, why can't it be, can't it be mine?

Aah... uuh..

Too doo doo too, too doo doo [many times until fade]


```

## How ly.py works
_is typing..._
