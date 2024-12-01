# Writing a small compiler in c

The reason for crating this project is to get a better understanding on how programing languages work , 
and maybe it can land me a job somewhere :)

## References used

Nora Sandler : Writing a C compiler
Robert Nystrom : Crafting Interpreters

### helpful links : 
Website : https://norasandler.com/book/
C (ISO) : https://www.open-std.org/JTC1/SC22/WG14/www/docs/n2310.pdf
Compiler Explorer : https://godbolt.org/
## Needed things to run

macOS or Linux System with an x64 processor

if apple silicon emulate x64 with Rosetta 2 , clang 

## Windows
Use windows subsystem for linux (WSL)
after installing use the terminal to open 
```cmd
wsl -d ubuntu

```
using ubuntu in my case

## MacOs
To install rosetta 2
```cmd

softwareupdate --install-rosetta --agree-to-license

```

to change terminal to a x64
```cmd

arch -x86_64 zsh

```

To view current architecture type 
```cmd

arch

```

To change back
```cmd

arch -arm64 zsh

```
