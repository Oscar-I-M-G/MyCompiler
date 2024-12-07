# Chapter 1

## Compiler Driver

Compiler Driver , calls the preprocessor, comiler, assembler and linker

```cmd

python3 my_compiler.py <input_file> [--lex | --parse |--codegen]

```

Checks if the input file is valid

Has three special cases that work with the given `./test_compiler` program from the book:

- `--lex`: Directs it to run the lexer, but stop before parsing.
- `--parse`: Directs it to run the lexer and parser, but stops before assembly generation.
- `--codegen`: Directs it to run the lexer, parser, and assembly generation, but stops before code emission.

## Lexer

## Parser

Input: It will recieve a list from the lexer.

Output: It will generate a tree representation called abstract syntax tree (AST)

## Assembly generation

## Code emission
