**HACK FOR GOOD 2018**

**TEAM VISIONEERS**

**PROJECT REPORT**

**SMART GLASS AND WALKING AID**



**TEAM MEMBERS**

_JOSHUA JOHN_

_OLUBUNMI TALABI_

_JANE ORAGWE_

_FARINU TAIWO_

**MOTIVATION AND JUSTIFICATION OF PROBLEM**

Globally the number of visually impaired people is estimated to be 253 million of which 36 million are permanently blind. Of people over 40 years, 42 out of every 1000 people are visually impaired which is about 8.3 million people in Nigeria. The major cause of visual impairment are uncorrected refractive errors, cataract and aging. 
The motivation behind our idea is the basic necessity for the visually impaired to be properly involved in the society and the ability to learn like every other person, to be able to be seated in class like other pupils, to read newspapers, etc. The visually impaired people are stigmatized because they cannot do anything on their own without the help of people around. This reduces their self-confidence and interaction within the society, take University of Lagos for example where they have a dedicated library, dorms and exams for the visually impaired, what more could they be lacking but a comfortable, reliable and safe means of going to and fro from the lecture hall, to the library, to fellowships and then to their various dorms? A major problem for a blind or visually impaired person (BVI) is to interact with the world to share knowledge. For them information has to be in a special tactile language or in voice format.
The concise problem statement of this project is to create a solution that helps the visually impaired people read and move around without human aid.

PROJECT DESCRIPTION AND WORKING PRINCIPLE

We have designed “THE SMART GLASS” (and affiliated walking aid) which will enable the visually impaired to become more mobile and independent in a safe, economic and reliable manner. 
The Smart glass comes with just a camera and a raspberry pi(micro-computer). The camera is mounted in front of the glass with the raspberry pi connected at the back using a headband. The camera reads to the user via an earpiece connected to the micro-computer documents placed in front from a distance range of 25cm (near point) to about 5m. The camera also detects when there is an obstacle and tells the user. While the walking aid is a handheld device which notifies the users via vibration when there is a close range obstacle (from about 4cm – 50cm) in front of him.

 
Solution Model

![image](https://user-images.githubusercontent.com/22997856/145222853-e1dcb807-610e-410f-899e-069a3ed021b1.png)


FEATURES OF THE SMART GLASS:

•	Scanning and reading documents.
•	Text to speech (Reading Capability)
•	Obstacle detection.
Scanning and reading documents: The smart glass consists of a camera which acts as the “eye” of our minicomputer (raspberry pi). It sends real time images to the minicomputer for processing.
The image processing involves:
•	Two-colour Intelligent binarization routines: this converts color and greyscale images into black-and-white images. Reducing the image to black and white is therefore the first stage in figuring out the text that needs processing. 
•	Page analysis: These are the zones of interest to be recognized are marked on the scanned page. A page may contain a big title, several text columns, two photos, a table and a footer.
•	Optical Character Recognition (OCR): All OCR programs are slightly different, but generally they process the image of each page by recognizing the text character by character, word by word, and line by line. The OCR algorithm extracts text information from the black-and-white pixels of the selected zones: it recognizes the shapes and assigns characters.
•	Basic error correction: the program then reviews and correct the result from the OCR using a built-in spellchecker to highlight any apparently misspelled words that may indicate a misrecognition. This is achieved by using near-neighbour analysis to find words that are likely to occur nearby, so text incorrectly recognized as "the barking bog" might be automatically changed to "the barking dog" (because "barking" and "dog" are two words that very often run together).
Text to Speech: The final text is then read aloud to the visually impaired person by another machine learning technique which involves conversion of text to speech.  The text to speech engine is trained using artificial intelligence. The processed text is then read out to the visually impaired loud via the ear piece connected to the minicomputer.
Obstacle detection: The camera with the aid of our obstacle detection algorithm sends signal to the minicomputer when it detects objects in front of the user.
These process requires data analysis and artificial intelligence (Deep neural networks, Convolutional neural networks and machine learning techniques) which will be constantly feed to our server to be trained and improved upon for the smart glass to function properly.

FEATURES OF THE WALKING AID

•	Near distance obstacle detection
•	Notification via vibration
Near distance obstacle detection: The walking aid is comprising of an ultrasonic sensor which detects close obstacles in the range of 5cm to 50cm. This is sent to the Arduino micro controller embedded in the walking aid.
Notification via vibration: upon obstacle detection, the microcontroller sends to the vibrator notifying the user that there is an object around him.

FUTURE ADDITIONS:

1.	Obstacles recognition (i.e. Shape recognition, e.t.c)
2.	Navigation and directions using GPRS and IOT implementation
3.	Real time tracking and monitoring of user by care taker using the Internet of things (IoT)
4.	Miniaturization of the walking aid and smart glass minicomputer

TECHNOLOGY USED:
1.	Artificial intelligence
2.	Internet of Things (IoT)
3.	3D printing.

