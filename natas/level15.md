# Level 15

# Challenge: 
Web form has input for username and a box where client can "Check existance"

# Solution:
The source code is prone to SQL exploit like in previous level.
We need to figure out the password for username natas16.

By testing different inputs with Burbsuite responses using debug state,
we can try to figure out how to exploit the code. 
Input: natas16 gives -> "This user exists".
Let's add a sql injection into the username input.

Here we can see that in users, there exists a password:"something" for every username.
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL

Let's try input: natas16" AND password: "something"
With this we need to get a true value for both inorder to get a --
By this method we can step by step figure out what is the password for that exact username.

After multiple tries using:
Executing query: SELECT * from users where username="natas16"
 AND substring(password,1,1) = "X" -- "<br>
This user exists.<br>
This means both values were true.

We managed to get to find out natas16 password starts with "X" now we just need to add
BINARY into the injection and check whether it's a minor or capital x.
Result was that it was capital X.

Creating a code ourselves for this makes cracking rest of the code easier since there
are always 32 characters in a natas password. 
Which would take very long time doing manually.
This can be done with python.

# Learned and observations:
- How blind SQLi uses true/false values to extract data.
- How to automate exploitation using python.
- A clearer grasp on how to use Burb Suite for SQLi testing.
- The importance of proper validation of user input.

# How the exploit could be prevented:
- To prevent SQLi: prepared statements and whitelisting. Validate the input in the username field.
- The source code should not expose the "debug" mode, because it allows the attacker to see full SQL query.  
 This makes the exploit much easier for the attacker.


# Python code in github
# Password -> Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb
