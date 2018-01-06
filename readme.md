# dadsay

A [cowsay](https://en.wikipedia.org/wiki/Cowsay)-like program that turns a given string into a dad joke.

```
$ dadsay water you talking about
 __________________________________________________________
/ How do you make holy water?                              \
\ You boil the hell out of it.                             /
 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
      \       _____
       \     /---- \
        \   [&]/ [&]
            ( (c   /)
              ===; |
             _\__/ |____
            /  < >      |
           /   / \   /  /
          /  / | |  /  /
 ___/)___/  /_/)___/  /
'--;______'--;_______/
            |  | /   ]
            /  \/    \

```

Brought to you by [chr](https://cybre.space/@chr) who gave it to [garbados](https://toot.cat/@garbados) for [Sneepsnop 2017](https://octodon.social/@sneepsnop)

## Install & Usage

Dadsay is just one file: `dadsay.py`. You will need [Python 3](https://www.python.org/) to use it. Here's how to create an alias for dadsay:

```bash
# get the source
git clone https://github.com/garbados/dadsay

# add an alias for dadsay to .bash_aliases
echo "alias dadsay='$(pwd)/dadsay/dadsay.py'" >> ~/.bash_aliases

# re-initialize the terminal environment
exec bash

# LET THE PUNS FLOW
dadsay see you next fall
```

## Contributing

Contributions welcome! Please [file an issue](https://github.com/garbados/dadsay/issues) for bug reports, feature requests, and usage questions. If you'd like to add more jokes, send us a [pull request](https://github.com/garbados/dadsay/pulls)! Thanks for trying dadsay :)

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
