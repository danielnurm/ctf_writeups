# Level 17

# Challenge:
Web form has a input for an username. Input is interpreted with SQL.
When trying different kind of inputs no result is shown, because the query outcomes
are made comments in the source code. We need to find a
way to get a identicator on how the program handles our input.

# Solution:
In level 15 we could simply work by the query prints. Now we can't. 
Because we can't intepret data straight from the responses, we can use time as a method of ture
and false outcomes combined with our own SQL query. For this we need to use SQL command: "SLEEP()".
Let's implement this into the python code we made in level 15.

# Problems I had:
- Tried doing the program without header value, resulted in error.
- Ended up fetching just the username, because of faulty SQL query.
- Different sleep times provided very different results.
SLEEP(1) resulted in: "fDGn2ACababeb" which is obviously too short first of all.
So the 32 digit long took abit of testing with different times.
- Using "SLEEP(0.5)" and "elapsed time > 0.3" resulted in 28 char password.
When we run the python code, we can see when the "wrong" chars take around 0.05s which 
doesn't activate SLEEP(0.5). When we have a correct one they jump to around 2s. 
Which is well over 0.37s and we have a correct char.

# Learnt and observations:
- How response time can be used to commit SQLi
- How important is to have a code structure which doesn't leak info through response times
- SQL querys can be tricky to implement and from server perspective is to restrict attacker
from doing SQLi's
- Blind SQLi can be done even without visible output
- Finally SLEEP(0.5) and response.elapsed.total_seconds()>0.37 worked. 
Which gave fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op9, which is 1 character over 32.
The 1 value over 32 means that the timing was a little off but close enough to get 32
characters.

# How the exploit could have been prevented:
- Restrict SQLi with prepared statements.
The user input $_REQUEST should not be implemented directly into the SQL query.
Instead it should be put in a placeholder. This would make the SQL query "locked in",
for example via bind_param().
- Rate limiting. Server should automatically do something about this many login attempts,
preventing the attacker from continuing the exploit.
Password -> fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op
