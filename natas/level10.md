# Level 10

Challenge: passthru function which now prohibits from using symbols: if(preg_match('/[;|&]/',$key)) {
        								print "Input contains an illegal character!";, 
which makes command injection harder. Have to find out how to drive passthru function through and get in.

Solution: Using /etc/natas_webpass/natas11 file which has the password. Typing into the input .* /etc/natas_webpass/natas11 # exploits the 
vulnerability into revealing what the entire content of that file is, which we can read the secret input from.

Learned: 
1. At first by looking at the function thought that '/' was prohibited, but learned that it was infact not.
2. How '.*' and '#' can be used in a command injection and their roles.
3. How there are multiple ways of trying command injection and how hard it could be to truly defend against.
4. '.*' makes grep showcase every line and they both have a specific part to play in the combonation. # symbol makes the system not care about the later, which in this case is 'dictionary.txt'. 
5. Making a function which doesnt ever end up for command line would probably be the best and safest option for defending against attacks like this.

Password -> VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd
