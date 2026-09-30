# Level 13

Challenge: Can only upload an image file (max 1KB)

Solution: 

Function makeRandomPathFromFilename($dir, $fn) does not check filetype ending, but
automatically returns in variable $ext .
Line: "else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name']))" provides the vulnerability.
Function exif_imagetype checks if there exits a certain magic bytes in the beginning of the file which represent an image file.
By using image magic bytes in the beginning of the file, we can get return a true value for the function and get our file in the system.
For image can be chosen GIF or JPEG. Using gif is more functional for this php file because it reads as ASCII.
GIF magic bytes in ASCII are GIF87a and GIF89a. Let's use one in our PHP file to get through the validation.
By choosing the file to upload, we can then edit html in a similar way like level 12. ".jpg" -> ".php" and hit upload.

Once our PHP file is in the system, we can execute command in the url ->
...?x=cat%20/etc/natas_webpass/natas13 and extract our password.

Observations and learned: 
- $_FILES has premade error scenarios which are represented by specific numbers. 
- How a file can seem to be one thing, allwhile being completely different. 
In this case PHP file, which read as an image by a certain function. 
- How bad function choices can lead to vulnerabilities. 
- How magic bytes can be written into a PHP file and what role magic bytes play.
- JPEG magic bytes are in binary and GIF in ASCII
- Using JPEG magic bytes in PHP file compared to GIF is significantly harder to execute.

What could fix and help solve the vulnerability in the code:
- Clients upload is forcefully painted as an image before saving. Making the php code useless.
- Loading the image to a dir that is unusable by the client.
- Replace the bad function with a more secure one.

Password -> GIF87ag8ba0olAzaSJuyS4gnmbdVVigAICLG1k 
