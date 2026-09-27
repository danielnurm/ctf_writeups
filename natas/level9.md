# Level 9

Challenge: Sourcefile has the following
	$key = "";
	if(array_key_exists("needle", $_REQUEST)) {
    	$key = $_REQUEST["needle"];}
	if($key != "") {
    	passthru("grep -i $key dictionary.txt");}

Solution: passthru function is exploitable. In the natas challenges password is located in the file /etc/natas_webpass/natasx.
So we can replace the key value with from the natas10 file. By insterting "; /etc/natas_webpass/natas10" into the web form, it provides the password back.

Learned: This is a command injection vulnerability which should be fixed for example by having strict filters for what the user can input in to the system. 
Also should make a better safer function which for example could only allow alphabets and numbers.

Password -> EgjlkzB6E8LJyf2Obt4q7q4ewt5ZWSNv 
