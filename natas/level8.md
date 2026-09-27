# Level 8

Challenge: $encodedSecret = "3d3d516343746d4d6d6c315669563362";
		function encodeSecret($secret) {
    		return bin2hex(strrev(base64_encode($secret)));}

Solution: To encode the secret the reverse of the function needs to happen which is hex2bin->strrev->base64_decode which gives the password
bin2hex -> ==QcCtmMml1ViV3b
rev -> b3ViV1lmMmtCcQ==
base64 -d -> oubWYf2kBq

Learned: That % symbol in decoded strings isnt part of the decoded string but signals to showcase ending of the line. Also that bin2hex is xxd -r -p and all together about encoding.
Most importantly sourcefile should not reveal how passwords are formed.

Password -> UdxmI27dTaXmnd1rxKQTfws6jihTdcQ9
