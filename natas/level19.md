# Level 19

# Challenge: Need to find a way to log in as admin, similar as level 18 but "session
IDs are not longer sequential"

# Solution:
- Looking at the source code we can see that myhex2bin is new.
- ID is created by a similarly as in level 18, but is made bin2hex.

function createID($user) { /* {{{ */
    global $maxid;
    $idnum = rand(1, $maxid);
    $idstr = "$idnum-$user";
    return bin2hex($idstr);
}

- The $idstr value consists of $idnum (random number between 1-640) and $user.
This string is then hex-encoded.
- We need to make an automation with python that goes through the possible combinations in hex form.
When the correct one hits we should be able to login as admin.
We know admin is $user so we only need to brute-force $idnum (1-640). The server accepts any 
correct form session ID as valid, even if it wasn't the one it gave to us.

# Problems I had
- There was no "view source code" link visible on the page, so I first tried Ctrl+U to see the source,
but that only shows the page's HTML output, not the underlying PHP. Figured out that Natas serves
the PHP source at a separate URL (index-source.html), and opening that directly in the browser
gave me the actual source code, properly rendered.
- In the Python script, didn't realize hexlify() needs bytes, not a normal string — had to .encode()
the string first, then .decode() the result to get a usable string back.

# How could have been prevented:
- Session ID was predictable, which made the attack easier.
- Session IDs should be encrypted and randomized.
- SessionID shouldn't be able to carry over admin authority and should not giveaway that fact.
- Session cookies should be unusable after a certain time, this would prevent later usage
by an attacker.

# Observations and learned:
- Improved understanding of PHP.
- Better grasp on how important it is to protect session keys and use
  proper encryption.
- Predictability is a huge vulnerability in itself.

Password -> slOKYGsjlJhaqKliGvrgWAzln0JyrWao
