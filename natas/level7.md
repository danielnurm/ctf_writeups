# Level 7

Challenge: Viewing source code reveals that "password for webuser natas8 is in /etc/natas_webpass/natas8"

Solution: Changing the url parameter index.php?page=  to index.php?page=/etc/natas_webpass/natas8 revealed
the hidden password. Server didn't require validation for requested files.

Learned: Page parameters shouldn't directly be able to control which files load. Potential attacker could read files he wants to.
