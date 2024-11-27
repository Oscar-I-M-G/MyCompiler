# Writing a small compiler in c

The reason for crating this project is to get a better understanding on how programing languages work , 
and maybe it can land me a job somewhere :)

## References used

Nora Sandler : Writing a C compiler
Robert Nystrom : Crafting Interpreters

helpful links : https://norasandler.com/book/
## Needed things to run

macOS or Linux System with an x64 processor

if apple silicon emulate x64 with Rosetta 2 , clang 


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