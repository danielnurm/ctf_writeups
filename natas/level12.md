# Level 12

Challenge: Browser only accepts JPG files with max size of 1KB. 

Solution: Creating a PHP file, which uses shell_exec($_GET['x']) makes possible for client to
use commands from the url. The vulnerability exists because the server doesn't validate $_POST["filename"].
It trusts the filename from the client input and doesn't check the file type. By editing html in DevTools inspector
we can change the .jpg -> .php and finish uploading our own php file. Then we have our own php file in the system which 
allows us to execute commands via url.
?x=cat /etc/natas_webpass/natas13 extracts the password for the next level.

Observations and learnt:
- How editing html can be used for manipulating files.
- Importance of server side never trusting client-side.
- Always needing to validate files on the server side.
- Understanding php langauge better and the role of shell_exec.


Password -> g8ba0olAzaSJuyS4gnmbdVVigAICLG1k
