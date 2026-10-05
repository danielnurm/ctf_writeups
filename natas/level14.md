#Level 14

Challenge: Need to find fill in web form inputs: username and password

Solution:
From the sourcecode we can see mysqli_num_rows function requires:
if(mysqli_num_rows(mysqli_query($link, $query)) > 0) {
            echo "Successful login! The password for natas15 is <censored><br>";
We also have the following SQL:
$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
We can use a SQL injection here. The program does not prevent using " which enables us to end the text input area sooner.
By using this phrase in the username: " or "9" = "9" we can return a true value regardless for the username.
But this still needs the correct password to function
, so let's make the username in a # which makes the entire password query a comment: " or "9" = "9" #"
This makes the password a comment. 

Learnt and observations:
- Better idea on how mysqli super variables work and the role of them in a website.
- How important it is to restrict what the user can input.
- Better grasp on how SQL injections are achieved.

Prevention measures to prevent this from happening:
- To prevent a SQL injection, server should use prepared statements to prevent potentially harmful inputs.
- Validate inputs
- Beforehand decide what is allowed, and everything else forbid. (whitelisting)
- Basics on Burbsuite application.

Password -> GB6USCJYJjwLyYhZUNkE1NwDueiTow6g
