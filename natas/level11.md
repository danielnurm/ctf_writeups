# Level 11

Challenge: Cookies are protected with XOR encryption. 

Solution: Need to find out cookie value. Typing into devtools console "console.log(document.cookie)", inorder to find out cookie value. 
Cookie value -> data:"EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0%2FGBlgaVVIJDURDSQ1VRY="
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff"); because of this we know that cookie value previously mentioned consists of 'showpassword=no' and bgcolor.
Need to change showpassword=yes.
Cookie value was made -> setcookie("data", base64_encode(xor_encrypt(json_encode($d)))); 
Using $defaultdata in sourcecode, and using echo base64_encode(json_encode($defaultdata)); returns -> eyJzaG93cGFzc3dvcmQiOiJubyIsImJnY29sb3IiOiIjZmZmZmZmIn0

Using CyberChef tool. Using From Base64 and then XOR we can get extract key -> kBSwkBSwkBSwkBSwkBSwkBSwkBZ{ G»vFö²"Rö÷)#
kBSw is repeating so XOR key length is 4. Using this gives -> {"showpassword":"no" ...

Creating a new $defaultdata,and replacing 'no' -> 'yes' as json and then XOR it with the new found kBSw key returns -> EGAgHwQ1IxYYMSQYGSZxTUk7NgRJbnEVDCE8GwQwcU1JYTURDSQ1EUk/
New encrypted cookie can be changed in the browser and password for next level reveals.

Observations and learnt: 
- How encryption and decryption mechanisms work, and how they are reversible operations.
- A more indepth look into XOR. How XOR key can repeat. How short XOR key can be a great risk, making attacker detect it easier.
- How each step is important in getting the correct result. If one step is wrong order, the end result fails.
- What kind of vulnerability unprotected cookies can create. Client shouldn't be able to change them. Validation for change should be asked.
- XOR can be very risky when using short keys and possibly predictable plaintext, which in this case was '$defaultdata'.

Password-> EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng
