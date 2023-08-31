# String functions

In SQL, functions like `LEFT()` are often referred to as **string functions** or **string manipulation functions**. These functions are used to manipulate and work with textual data stored in string columns. They allow you to perform operations like extracting a portion of a string, concatenating strings, changing the case of characters, and more.

Here are some common categories of string functions in SQL:

## Text Extraction and Manipulation Functions:

- `LEFT()`: Returns a specified number of characters from the left side of a string.
- `RIGHT()`: Returns a specified number of characters from the right side of a string.
- `SUBSTRING()` or `SUBSTR()`: Returns a portion of a string.
- `CONCAT()`: Concatenates two or more strings together.

## Text Case Functions:

- `UPPER()`: Converts a string to uppercase.
- `LOWER()`: Converts a string to lowercase.
- `INITCAP()`: Capitalizes the first letter of each word.

## Text Search and Replace Functions:

- `CHARINDEX()` or `INSTR()`: Returns the starting position of a substring within a string.
- `REPLACE()`: Replaces occurrences of a substring with another substring.
- `TRANSLATE()`: Replaces characters in a string based on a mapping provided.

## Whitespace Trimming Functions:

- `LTRIM()`: Removes leading spaces from a string.
- `RTRIM()`: Removes trailing spaces from a string.
- `TRIM()`: Removes leading and trailing spaces from a string.

## String Length Functions:

- `LEN()` or `LENGTH()`: Returns the length (number of characters) of a string.

These functions make it easier to perform various operations on text data within SQL queries and are an essential part of working with string columns and values.
