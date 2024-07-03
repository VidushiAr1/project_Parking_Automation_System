Project on parking system

1. Introduction
  The  Parking System is an innovative solution designed to automate the parking process. This system utilizes OpenCV for license plate recognition, Tesseract-OCR for optical character recognition, and MongoDB for data storage. The project aims to streamline the parking experience, providing convenience and efficient management. The system captures the license plate number of vehicles entering the parking area, stores it in the database, collects the owner's details, and calculates the parking charges based on the duration of stay.


2. System Components

  i) OpenCV for License Plate Recognition
    OpenCV is used for real-time license plate detection and recognition. It captures the license plate image, processes it, and extracts the alphanumeric characters using image processing techniques.

  ii)Tesseract-OCR for Optical Character Recognition
    Tesseract-OCR is employed to recognize the characters from the license plate image obtained from OpenCV. It converts the image data into machine-encoded text.
  
  iii) MongoDB for Data Storage
    MongoDB, a NoSQL database, is used to store the license plate numbers, owner details, and parking duration. It provides a flexible and scalable solution for managing the parking data.
 
 
 3. Workflow

  a) License Plate Recognition:
   - The system captures the license plate image of the vehicle entering the parking area using OpenCV.
   - OpenCV processes the image to extract the license plate region.
   - Tesseract-OCR recognizes the characters from the license plate image.

  b)Data Storage:
   - The recognized license plate number is stored in the MongoDB database.
   - The system prompts the user to enter the car owner's details, including name and phone number, which are also stored in the database along with the license plate number and entry timestamp.

  c) Parking Duration and Charges Calculation:
   - When the vehicle exits the parking area, the system captures the license plate number again and retrieves the entry timestamp from the database.
   - The parking duration is calculated based on the entry and exit timestamps.
   - Parking charges are calculated at a rate of 20 rupees per hour.


4. System Requirements

- OpenCV library for license plate recognition.
- Tesseract-OCR for character recognition.
- MongoDB database for data storage.
- Python programming language for system implementation.


5. Implementation Steps

  1. License Plate Recognition:
   - Implement OpenCV algorithms for license plate detection and extraction.
   - Integrate Tesseract-OCR for character recognition from the license plate image.

  2. Database Integration:
   - Set up MongoDB database to store license plate numbers, owner details, and timestamps.

  3. User Interaction:
   - Implement a user interface to collect car owner's name and phone number.

  4. Parking Duration and Charges Calculation:
   - Calculate the parking duration based on entry and exit timestamps.
   - Compute parking charges using the rate of 20 rupees per hour.


6. Conclusion
    The  Parking System with License Plate Recognition, Tesseract-OCR, and MongoDB integration provides an efficient and user-friendly solution for managing parking spaces. By automating the process of license plate recognition, data storage, and payment calculation, the system enhances the overall parking experience for both users and parking operators. This project demonstrates the seamless integration of various technologies to create a practical and innovative solution for modern parking management.

