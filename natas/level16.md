# Level 16

# Challenge:
Web form as a user input, filters certain characters. Input box for "Find words containing:"
Characters: [;|&`\'"] disallowed. We can see from the source code that it uses user given input as a key to find
value from the dictionary.txt
We need to get access into /etc/natas_webpass/natas17 for the password.
passthru("grep -i \"$key\" dictionary.txt");
User input is treated as a single string.


# Solution:
$ symbol isn't forbidden.
With empty user input the site returns the entire dictionary. Because the input would be:
passthru("grep -i "" dictionary.txt"); -> the whole dictionary.
Let's use $() in our input. $(grep -i <numeral or alphabet here> /etc/natas_webpass/natas17)
With x -> empty page
with p -> whole dictionary
From this we can conclude x is in the natas17 password.

We could do this manually, but again like in level 15 it is wiser to automate through
python code. Let's edit the python code.

# Problems I had:
- Didn't have a clear check system for whether the word resulted in a non-dict output,
which symbolizes that the character was in the password.
- Used -i in the input at first, which didn't differentiate between minor and capital letters.
- The code stopped working at the 14-15 character point. The brute-force attack resulted in
"aG5KtYjI77tfx", which ended up being the end of the password, not the start.
This was because I didn't anchor the input with ^, which forces the match to start
from the beginning of the line. Without it, the order of the password came out wrong.

# Learnt and observations:
- Problem points previously mentioned
- Better understanding of shell command usage
- An easy way to validate output: append a known dictionary word to the subshell result,
so a match (character correct) and no-match (character wrong) both give a clear,
checkable difference in the response, instead of comparing page length. Which would have
been much more complex.

# What could have been done to prevent this:
- The input was wrapped in double quotes ("$key"), which blocked word-splitting
(the input couldn't be broken into separate shell arguments). But $ itself was
never disallowed, so $() command substitution still worked inside the quotes.
- escapeshellarg() would force the entire input inside single quotes ('...'),
which would make a symbol like $ just a literal string instead of a shell command

# Python code in github
Password -> KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx
