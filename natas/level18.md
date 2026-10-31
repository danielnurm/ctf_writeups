# Level 18
# Challenge:
Need to find a way to login as admin

# Solution: 
We can see code that this reveals:
function print_credentials() { /* {{{ */
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {

This prints out the password we need for the next level.
We need to find a way to make $_SESSION["admin"] equal to 1.
createID() creates a new session ID somewhere in between values 1-640.

function my_session_start() { /* {{{ */
    if(array_key_exists("PHPSESSID", $_COOKIE) and isValidID($_COOKIE["PHPSESSID"])) {

We need both array_key_exists() and isValidID() to be true.
To make both of these true, we need to have in the http request a cookie called “PHPSESSID”,
and its value needs to be numeric and within the values createID() makes, which is 1-640.

Looking further at my_session_start():

if(!array_key_exists("admin", $_SESSION)) {
    $_SESSION["admin"] = 0;
}
This means if we have a admin key our session value, isnt zeroed, which is optimal.

We can automate a program which makes both of these previously mentioned happen,
looping through all 640 possible session IDs,
setting each one as the PHPSESSID cookie, requesting the page without
any form parameters,
and checking the response for “You are an admin” until we find one
where admin is already set to 1.

Using range 1-640 in python code, and running a forloop for different
PHPSESSID via this python code revealed that the admin sessionID was 119.
r = requests.get(url, auth=auth, cookies={"PHPSESSID": "119"})
print(r.text)
Password for next level is extracted.


# Observations and learned:
- Better understanding of PHP code.
- Session and cookie related safety. For example on how cookies and session variables
can be manipulated by requests.
- Importance of proper safety measures like rate limiting, having proper random
session IDs, and invalidating old session cookies after login or logout.

# How could have been prevented:
- SessionID number should have been cryptographically random and huge, and not easily guessable, runnable like numbers 1-640. 
- Should invalidate cookies when user exits site, could be done by a timer or when logout happens.
- Secure flags for cookies
- Rate limiting.

Password -> qvwtMqAcVSBlf7HE3sw9pljhqqPF9MMT
