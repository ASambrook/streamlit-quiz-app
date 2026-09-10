# IBM Business Conduct Guidlines Quiz

## Introduction 

This Business Conduct Guidelines (BCG’s) Quiz App is a minimum viable product (MVP) developed for IBM employees. IBM is an organisation that specialises in technology and consulting. Therefore, due to the handling of sensitive data and work with rapidly developing artificial intelligence, it is increasingly important for the employees to be aware of the organisation’s ethical values and principles.

The BCG’s Quiz App is a web application [Python](https://docs.python.org/3/) and [Streamlit](https://pypi.org/project/streamlit/). It collects an employee’s name and their answers to a series of single-answer multiple-choice questions around key themes in the official [Business Conduct Guidelines](https://www-api.ibm.com/adobe/assets/urn:aaid:aem:81857c4c-3c6f-43ec-b0a0-1b78d394b348/original/as/ibm_business_conduct_guidelines.pdf) of IBM. The purpose of the app is to provide a more interactive method of learning the organisation’s values, it is intended to be sent out to all employees, ensuring they have sufficient knowledge of the guidelines, and supporting the theme of integrity for IBM.

The application will calculate the employee’s score and immediately display their score. This lets the quiz support its learning focused purpose, allowing employees to see when they need to review the guidelines or when they have a sufficient level of knowledge. 

To ensure data quality, the participant’s name is cleaned and validated before submission. If any rule is not met, the application will display an error message and prevent submission, ensuring that is transparent and accurate data stored, available for review at any time. A valid submission will ensure the participant’s name, selected answers, and a timestamp are written to a [CSV](https://docs.python.org/3/library/csv.html) file. This aligns with common workplace practices, as CSV files allow for simple portability and accessibility, and they can be processed using standard software, such as [MS Excel](https://www.microsoft.com/en-gb/microsoft-365/excel) or [Google Sheets](https://developers.google.com/workspace/sheets), without the need for additional systems.

Being an MVP, the application focuses on core functionality: input collection, validation, question delivery, and data storage. More advanced features are not implemented at this stage but provide clear opportunities for future enhancement.


## Design

### GUI Design 

The first stage of this project was to begin the design process. I began this using [Figma](https://www.figma.com) , a design tool that enabled me to create an initial wireframe, shown in **Figure 1**.  This wireframe displays the user journey throughout the quiz, with the blue arrows representing the planned navigation flow from the welcome screen in frame 1 to the results screen in frame 5. It set out the intended structure and user interaction of my web application.

![GUI Flow](gui_flow.png)
**Figure 1:** Wireframe


### Functional and Non-functional Requirements

#### Functional requirements

Next, I set out my Functional and Non-Functional of what I wanted this web application to provide. **Figure 2** sets out the Functional Requirements, these are general, core behaviours which describe what the application should do.

![Functional Requirements](app_fr.png)  
**Figure 2:** Functional Requirements

#### Non-Functional Requirements
**Figure 3** shows the Non-Functional Requirements, these are more precise and describe how well the application should perform.

![Non-functional Requirements](app_nfr.png)
 **Figure 3:** Non-functional Requirements

### Tech Stack Outline

The Tech Stack outline below provides the various tools, frameworks, and programming languages I have used throughout the project to build and run the web application.


[Python](https://docs.python.org/3/) - core programming language   
[Streamlit](https://pypi.org/project/streamlit/) - user interface framework for building the quiz screens  
[CSV](https://docs.python.org/3/library/csv.html) - local data storage in CSV format  
[Figma](https://www.figma.com) - wireframing tool used to design the GUI layout and user flow  
[Virtual Studio Code](https://code.visualstudio.com) - primary development environment for writing and testing code  
[GitHub](https://github.com) - repository hosting for the project  
[Pytest](https://docs.pytest.org/en/stable/) - Development testing framework  
[Draw.io](https://app.diagrams.net) - Diagramming tool used to create the class diagram  

### Code Design

The final stage of the design process was to create a code design document. **Figure 4** shows the class diagram I created using [Draw.io](https://app.diagrams.net), a tool useful for creating professional diagrams. The class diagram uses [UML](https://www.omg.org/uml/) to visually represent the structure of a system, including its classes and how they relate to each other, such as the dark filled arrow representing inheritance between parent and child classes in **Figure 4**.

![Class Diagram](class_diagram.png)
**Figure 4:** Quiz application Class Diagram

## Development

I began the development of the project by creating a python virtual environment. This allowed me to isolate the project’s dependencies and run the web application with [Streamlit](https://pypi.org/project/streamlit/) without any interference with global python packages.

I began by setting up `main.py`, which acted as the central file for my project where I planned to import the rest of the [modules](https://docs.python.org/3/tutorial/modules.html). This allowed me to keep the code neat and structured, with 6 modules making up different sections of the quiz: `main.py`, `welcome_screen.py`, `questions.py`, `quiz_screen.py`, `end_screen.py`, and `storage.py`.



## Testing

### Manual Testing

I did manual testing continuously throughout each stage of my development process. This allowed me to ensure each section was fully complete and worked correctly with Streamlit before progressing the project. For example, I would not move onto the `questions.py` module before my manual tests for the `welcome_screen` file were successfully passing.

My manual tests can be seen in **Figure 5** below, this displays my method for each test, the expected result and whether the tests eventually passed. These were important as they allowed me to observe the web applications behaviour against the intended user navigation I created in the design section. There were often errors at first with each test, which is a key justification for why I decided to not develop any further stages of the quiz before my manual tests passed for the current stage.

Test Case ID 3, the Screen navigation test, was a slight anomaly. This is because it was repeated each time I added a new module of code to my quiz, ensuring that the GUI continued to display everything in the intended order.

![manual tests](manual_tests.png)  
**Figure 5:** Table of Manual tests


### Automated Unit testing

I then carried out automated unit testing after all my manual tests were completed, as a final check before deploying my web application to the Streamlit community cloud. I decided to use the [Pytest](https://docs.pytest.org/en/stable/)
Framework as it allowed me to write isolated unit tests by creating a virtual environment and then running `pip install pytest`in the terminal. 

I began with a smoke test which can be seen at the top of **Figure 6**, this ensured the pytest framework was functioning correctly. I then went through some and tested some of the key functions and classes, such as the `NameValidator` class, these tests focused on checking the lengths and allowed character types for the user inputs. **Figure 6** shows that two tests failed, this is because of there being 31 characters in one input and an `!` in another input. This is then changed to 30 characters and removing the `!` in **Figure 7 which is why the tests all passed successfully.

The automated testing was important as it allowed for quick checks at the end of my project, ensuring the key functions and classes were consistent, structured and importantly, correct.


![invalid name](validator_fail.png)
**Figure 6:** Pytest fail for invalid name

-------------------------------------------------------------------------------------------------------------------------------

![valid name](validator_pass.png)  
**Figure 7:** Pytest pass for valid name  




## Documentation

### User Documentation

**Step 1:**
Click [This Link](https://app-quiz-app-w6bmfvcpflejdfuzzgca3a.streamlit.app) to launch the streamlit web application in your browser.

**Step 2:**
Read the introduction to gain an understanding of the importance of this quiz, proceed to follow instructions by writing your name in the indicated box. This name will have to meet certain requirements, an error messaged will explain if your inputted name does not meet this criteria, as shown in **Figure 8** below.

**Step 3:**
After pressing begin quiz you will be faced with the first of ten questions, these will be a mixture of mutliple-choice and true or false questions. Read the questions and options carefully, and select one answer to each question before selecting 'Next Question' to save your answer and continue the quiz.

**Step 4:**
See your score out of ten. You will not be able to see which questions you answered incorrectly as this is a test of your knowledge of the Business Conduct Guidllines and the questions do not change.

**Step 5:**
If you are not satisfied with yoru score you may select the 'Play again' button to restart the quiz. If you are satisfied then please prcoeed to step 6.

**Step 6:**
You may download your results locally to [Excel](https://excel.cloud.microsoft/en-us/) by selecting the 'Download results CSV' button, and then the 'Download CSV' button which will display your name and score.

![Error message](error_message.png)  
**Figure 8:** Name validation error message


### Technical Documentation


## Evaluation

