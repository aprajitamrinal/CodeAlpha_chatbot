from django.shortcuts import render
from django.http import JsonResponse


# =========================================================
# APRAJITA AI CHATBOT
# Rule Based Student Learning Assistant
# =========================================================

CHATBOT_RESPONSES = {

    # =====================================================
    # GREETINGS
    # =====================================================

    "hello":
        "Hello 👋 I am Aprajita. How can I help you today?",

    "hi":
        "Hi 👋 I am Aprajita. Nice to meet you!",

    "hey":
        "Hey 😊 I am Aprajita. What would you like to learn today?",

    "good morning":
        "Good morning ☀️ Have a great day! What would you like to learn?",

    "good afternoon":
        "Good afternoon 😊 How can I help you today?",

    "good evening":
        "Good evening 🌆 What would you like to learn?",

    "how are you":
        "I am doing great 😊 Thanks for asking!",

    "thanks":
        "You're welcome 😊 Happy to help!",

    "thank you":
        "You're welcome 😊 Keep learning and keep practicing!",

    "bye":
        "Goodbye 👋 Have a great day and keep learning!",

    "goodbye":
        "Goodbye 👋 See you again!",


    # =====================================================
    # APRAJITA PROFILE
    # =====================================================

    "what is your name":
        "My name is Aprajita 🤖",

    "who are you":
        "I am Aprajita 🤖 a B.Tech 1st Year student learning assistant created using Python and Django.",

    "tell me about yourself":
        "I am Aprajita a B.Tech 1st Year student from G2 Batch at IIMT University Greater Noida Campus.",

    "where do you study":
        "I study at IIMT University Greater Noida Campus.",

    "which university are you from":
        "I am from IIMT University Greater Noida Campus.",

    "what is your course":
        "I am pursuing B.Tech and currently studying in my first year.",

    "which year are you in":
        "I am a B.Tech 1st Year student.",

    "which batch are you in":
        "I am from G2 Batch.",

    "what do you study":
        "I am studying B.Tech and currently I am in my first year.",

    "what is your purpose":
        "My purpose is to help students understand basic programming computer science AI Machine Learning and web development concepts through an interactive rule based chatbot.",

    "who created you":
        "I was created as a student project using Python and Django.",

    "what can you do":
        "I can answer predefined questions related to Python AI Machine Learning Django programming Data Science databases and basic computer science topics.",

    "what is iimt university":
        "IIMT University is the university where I am currently studying.",

    "where is iimt university":
        "I study at IIMT University Greater Noida Campus.",


    # =====================================================
    # BASIC COMPUTER
    # =====================================================

    "what is computer":
        "A computer is an electronic device that processes data and produces useful information.",

    "what is hardware":
        "Hardware refers to the physical components of a computer such as CPU RAM keyboard mouse and monitor.",

    "what is software":
        "Software is a collection of programs and instructions that tell a computer what to do.",

    "what is cpu":
        "CPU stands for Central Processing Unit. It executes instructions and performs calculations required by a computer.",

    "what is ram":
        "RAM stands for Random Access Memory. It temporarily stores data and programs that are currently being used.",

    "what is rom":
        "ROM stands for Read Only Memory. It stores permanent or firmware related instructions.",

    "what is operating system":
        "An operating system manages computer hardware software resources and provides services for applications.",

    "what is windows":
        "Windows is an operating system developed by Microsoft.",

    "what is linux":
        "Linux is an open source operating system commonly used on computers servers and many other devices.",

    "what is algorithm":
        "An algorithm is a step by step procedure used to solve a problem or perform a task.",

    "what is programming":
        "Programming is the process of writing instructions that a computer can execute.",

    "what is data":
        "Data is a collection of facts observations or information that can be processed by a computer.",


    # =====================================================
    # PYTHON
    # =====================================================

    "what is python":
        "Python is a high level general purpose programming language known for its simple and readable syntax.",

    "why use python":
        "Python is popular because it has simple syntax a large ecosystem and is widely used in AI Machine Learning Data Science automation and web development.",

    "is python easy":
        "Python is generally considered beginner friendly because its syntax is simple readable and easy to understand.",

    "python features":
        "Important Python features include simple syntax readability portability object oriented programming support and a large collection of libraries.",

    "why is python popular":
        "Python is popular because it is easy to learn has a large ecosystem and can be used in many areas such as AI Machine Learning Data Science automation and web development.",

    "python for ai":
        "Python is widely used in Artificial Intelligence because it is easy to learn and provides powerful libraries such as NumPy Pandas Scikit-learn TensorFlow and PyTorch.",

    "can python be used for ai":
        "Yes 😊 Python is one of the most widely used programming languages for Artificial Intelligence and Machine Learning.",

    "can python make websites":
        "Yes 😊 Python can be used for web development through frameworks such as Django and Flask.",

    "how to learn python":
        "Start with variables data types operators conditions loops functions lists dictionaries and then move toward object oriented programming and projects.",


    # =====================================================
    # PYTHON DATA TYPES
    # =====================================================

    "what is variable":
        "A variable is a name used to store a value in a program. For example name = 'Aprajita' stores a string in the variable name.",

    "what is string":
        "A string is a sequence of characters used to represent text.",

    "what is integer":
        "An integer is a whole number without a decimal point such as 10 25 or 100.",

    "what is float":
        "A float is a number that contains a decimal value such as 10.5 or 3.14.",

    "what is boolean":
        "A Boolean value can be either True or False and is commonly used in conditions.",

    "what is list":
        "A list in Python is an ordered and changeable collection used to store multiple values. Example: numbers = [10, 20, 30].",

    "what is list in python":
        "A Python list is an ordered and mutable collection that can store multiple values. Lists can contain duplicate values and different data types.",

    "what is dictionary":
        "A dictionary in Python stores data in key value pairs. Example: student = {'name': 'Aprajita', 'year': '1st Year'}.",

    "what is dictionary in python":
        "A Python dictionary stores data in key value pairs and allows values to be accessed using their keys.",

    "what is tuple":
        "A tuple is an ordered collection in Python that cannot be changed after it is created.",

    "what is tuple in python":
        "A tuple is an ordered and immutable collection in Python.",

    "what is set":
        "A set is an unordered collection of unique elements in Python.",

    "what is set in python":
        "A Python set is an unordered collection that stores only unique elements.",


    # =====================================================
    # PYTHON CONTROL FLOW
    # =====================================================

    "what is if else":
        "If else statements are used to make decisions in a program based on conditions.",

    "what is loop":
        "A loop is used to repeatedly execute a block of code.",

    "what is for loop":
        "A for loop is used to repeat a block of code for each item in a sequence such as a list string or range.",

    "what is while loop":
        "A while loop repeatedly executes a block of code as long as a specified condition remains True.",

    "what is break":
        "The break statement is used to immediately stop a loop.",

    "what is continue":
        "The continue statement skips the current iteration of a loop and moves to the next iteration.",

    "what is pass":
        "The pass statement is used as a placeholder when a statement is syntactically required but no action is needed.",


    # =====================================================
    # PYTHON FUNCTIONS AND OOP
    # =====================================================

    "what is function":
        "A function is a reusable block of code designed to perform a specific task.",

    "why use functions":
        "Functions help organize code reduce repetition improve readability and make programs easier to maintain.",

    "what is oop":
        "OOP stands for Object Oriented Programming. It organizes software around objects and classes.",

    "what is class":
        "A class is a blueprint or template used for creating objects in Object Oriented Programming.",

    "what is object":
        "An object is an instance of a class.",

    "what is inheritance":
        "Inheritance allows one class to acquire properties and methods from another class.",

    "what is encapsulation":
        "Encapsulation means combining data and methods inside a class and controlling how that data is accessed.",

    "what is polymorphism":
        "Polymorphism means that the same interface or method name can behave differently depending on the object.",

    "what is exception":
        "An exception is an error or unexpected event that occurs while a program is running.",

    "what is debugging":
        "Debugging is the process of finding and fixing errors in a program.",


    # =====================================================
    # ARTIFICIAL INTELLIGENCE
    # =====================================================

    "what is ai":
        "Artificial Intelligence or AI is a field of computer science focused on creating systems that can perform tasks requiring human like intelligence.",

    "what is artificial intelligence":
        "Artificial Intelligence enables machines to perform tasks such as learning reasoning problem solving decision making and understanding language.",

    "what is narrow ai":
        "Narrow AI is designed to perform a specific task or a limited set of tasks. Examples include recommendation systems spam filters and voice assistants.",

    "what is weak ai":
        "Weak AI is another term commonly used for Narrow AI. It is designed for specific tasks rather than general human level intelligence.",

    "what is agi":
        "AGI stands for Artificial General Intelligence. It refers to a hypothetical form of AI that could perform a wide range of intellectual tasks across different domains.",

    "what is superintelligence":
        "Artificial Superintelligence refers to a hypothetical AI system whose intellectual capabilities would exceed those of humans across many areas.",

    "types of ai":
        "AI can be discussed using categories such as Narrow AI General AI and Superintelligence. AI systems can also be classified by capabilities or functionality.",


    # =====================================================
    # MACHINE LEARNING
    # =====================================================

    "what is machine learning":
        "Machine Learning is a branch of AI where computers learn patterns from data and use those patterns to make predictions or decisions.",

    "what is supervised learning":
        "Supervised Learning trains a model using labeled data where the expected output is already known.",

    "what is unsupervised learning":
        "Unsupervised Learning works with unlabeled data and tries to discover hidden patterns structures or groups.",

    "what is reinforcement learning":
        "Reinforcement Learning trains an agent through rewards and penalties based on its actions.",

    "what is classification":
        "Classification is a supervised learning technique used to assign data to predefined categories such as spam or not spam.",

    "what is regression":
        "Regression is a supervised learning technique used to predict continuous numerical values such as house prices.",

    "what is clustering":
        "Clustering is an unsupervised learning technique used to group similar data points together.",

    "what is dataset":
        "A dataset is a structured collection of data used for analysis or Machine Learning.",

    "what is feature":
        "A feature is an individual measurable property or characteristic used by a Machine Learning model.",

    "what is model training":
        "Model training is the process of teaching a Machine Learning model using data so that it can learn patterns.",

    "what is overfitting":
        "Overfitting happens when a Machine Learning model learns the training data too closely and performs poorly on new unseen data.",

    "what is underfitting":
        "Underfitting occurs when a Machine Learning model is too simple to capture important patterns in the training data.",


    # =====================================================
    # DEEP LEARNING
    # =====================================================

    "what is deep learning":
        "Deep Learning is a part of Machine Learning that uses artificial neural networks with multiple layers to learn complex patterns.",

    "what is neural network":
        "A neural network is a computational model inspired by the human brain. It contains interconnected neurons that process information.",

    "what is cnn":
        "CNN stands for Convolutional Neural Network and is commonly used for image processing and computer vision tasks.",

    "what is rnn":
        "RNN stands for Recurrent Neural Network. It is designed to process sequential or time dependent data.",

    "what is lstm":
        "LSTM stands for Long Short Term Memory. It is a type of recurrent neural network designed to handle long term dependencies in sequential data.",


    # =====================================================
    # GENERATIVE AI
    # =====================================================

    "what is generative ai":
        "Generative AI refers to AI systems that can create new content such as text images audio video or code.",

    "what is nlp":
        "NLP stands for Natural Language Processing and focuses on enabling computers to understand process and generate human language.",

    "what is natural language processing":
        "Natural Language Processing is a field of AI that helps computers understand and work with human language.",

    "what is llm":
        "LLM stands for Large Language Model. It is an AI model trained on large amounts of text data to understand and generate language.",

    "what is prompt":
        "A prompt is an instruction or input given to an AI system to guide the response or output.",


    # =====================================================
    # COMPUTER VISION
    # =====================================================

    "what is computer vision":
        "Computer Vision is a field of AI that enables computers to analyze and understand images and videos.",

    "what is image recognition":
        "Image recognition is the process of identifying objects patterns or categories within an image using computer vision techniques.",


    # =====================================================
    # DATA SCIENCE
    # =====================================================

    "what is data science":
        "Data Science combines programming statistics mathematics and domain knowledge to extract useful insights from data.",

    "what is data analysis":
        "Data Analysis is the process of examining cleaning transforming and interpreting data to discover useful information and patterns.",

    "what is pandas":
        "Pandas is a popular Python library used for data manipulation and analysis. It provides powerful structures such as DataFrame and Series.",

    "what is numpy":
        "NumPy is a Python library mainly used for numerical computing and working with arrays.",

    "what is tensorflow":
        "TensorFlow is an open source machine learning framework commonly used for building and training Machine Learning and Deep Learning models.",

    "what is keras":
        "Keras is a high level deep learning API used for building and training neural network models.",

    "what is data visualization":
        "Data Visualization means representing data using charts graphs plots and other visual formats so that patterns and trends are easier to understand.",

    "what is big data":
        "Big Data refers to very large and complex datasets that require specialized technologies for storage processing and analysis.",

    "what is accuracy":
        "Accuracy is a classification evaluation metric that represents the proportion of correct predictions among all predictions.",


    # =====================================================
    # DJANGO
    # =====================================================

    "what is django":
        "Django is a high level Python web framework used to build secure and scalable web applications quickly.",

    "is django python":
        "Yes 😊 Django is a web framework written in Python.",

    "django python":
        "Django is built using Python. Python provides the programming language while Django provides the structure and tools for web development.",

    "why use django":
        "Django provides many built in features such as URL routing templates forms database support and security features that make web development faster and organized.",

    "what is web framework":
        "A web framework is a collection of tools and libraries that helps developers build web applications more easily.",

    "what is django app":
        "A Django app is a component of a Django project that handles a specific functionality.",

    "django urls":
        "Django URLs connect web addresses with views or functionality inside a Django application.",

    "django template":
        "A Django template is an HTML file that can contain Django Template Language and display dynamic data from the backend.",

    "what is django project":
        "A Django project is the overall application configuration that can contain one or more Django apps.",


    # =====================================================
    # WEB DEVELOPMENT
    # =====================================================

    "what is html":
        "HTML stands for HyperText Markup Language. It is used to create the structure and content of web pages.",

    "what is css":
        "CSS stands for Cascading Style Sheets. It is used to control the appearance layout colors fonts and design of web pages.",

    "what is javascript":
        "JavaScript is a programming language commonly used to make web pages interactive and dynamic.",

    "what is frontend":
        "Frontend is the part of a web application that users directly see and interact with.",

    "what is backend":
        "Backend is the server side of an application responsible for business logic data processing and communication with databases.",

    "what is full stack":
        "Full stack development involves working with both frontend and backend technologies.",

    "what is web development":
        "Web development is the process of creating and maintaining websites and web applications.",

    "what is api":
        "API stands for Application Programming Interface and allows different software applications to communicate with each other.",

    "what is url":
        "URL stands for Uniform Resource Locator and identifies the location of a resource on the internet.",

    "what is http":
        "HTTP stands for HyperText Transfer Protocol and is used for communication between web browsers and servers.",

    "what is server":
        "A server is a computer or software system that provides services or resources to other computers or applications.",

    "what is client":
        "A client is a device or application that requests services or resources from a server.",


    # =====================================================
    # DATABASE
    # =====================================================

    "what is database":
        "A database is an organized collection of data that can be stored accessed and managed efficiently.",

    "what is mysql":
        "MySQL is a popular relational database management system that uses SQL.",

    "what is sql":
        "SQL stands for Structured Query Language and is used to create manage and query relational databases.",

    "what is json":
        "JSON stands for JavaScript Object Notation and is a lightweight format commonly used for exchanging data between applications.",

    "what is primary key":
        "A primary key is a column or combination of columns that uniquely identifies each record in a database table.",

    "what is foreign key":
        "A foreign key is a field that creates a relationship between two database tables by referring to a primary key in another table.",


    # =====================================================
    # GIT AND GITHUB
    # =====================================================

    "what is git":
        "Git is a distributed version control system used to track changes in source code.",

    "what is github":
        "GitHub is a platform used for hosting managing and collaborating on software projects using Git.",

    "what is git commit":
        "A Git commit records changes made to files in a Git repository.",

    "what is git push":
        "Git push uploads committed changes from a local Git repository to a remote repository such as GitHub.",

    "what is git pull":
        "Git pull downloads and integrates changes from a remote Git repository into the local repository.",


    # =====================================================
    # AUTOMATION
    # =====================================================

    "what is automation":
        "Automation means using technology or software to perform repetitive tasks with minimal human intervention.",

    "what is task automation":
        "Task automation uses programs or scripts to automatically perform repetitive tasks such as file organization data processing or report generation.",


    # =====================================================
    # CYBERSECURITY AND CLOUD
    # =====================================================

    "what is cybersecurity":
        "Cybersecurity focuses on protecting systems networks applications and data from digital threats.",

    "what is encryption":
        "Encryption converts readable data into an encoded form to help protect it from unauthorized access.",

    "what is cloud computing":
        "Cloud computing provides computing resources such as storage servers databases and software over the internet.",

}


# =========================================================
# HOME VIEW
# =========================================================

def home(request):

    return render(
        request,
        "chatbot/index.html"
    )


# =========================================================
# CHAT VIEW
# =========================================================

def chat(request):

    if request.method == "POST":

        user_message = request.POST.get(
            "message",
            ""
        )


        # -------------------------------------------------
        # Normalize user question
        # -------------------------------------------------

        user_message = (
            user_message
            .strip()
            .lower()
        )


        # Remove common punctuation

        for character in [
            "?",
            "!",
            ".",
            ",",
            ";",
            ":"
        ]:

            user_message = user_message.replace(
                character,
                ""
            )


        # Remove extra spaces

        user_message = " ".join(
            user_message.split()
        )


        # -------------------------------------------------
        # Find response
        # -------------------------------------------------

        response = CHATBOT_RESPONSES.get(
            user_message,
            "Sorry 😕 I don't have an answer for that question yet. "
            "Please try another question or choose one of the suggested questions below."
        )


        return JsonResponse({

            "response": response

        })


    # -----------------------------------------------------
    # Non POST request
    # -----------------------------------------------------

    return JsonResponse({

        "response":
            "Please send a message to the chatbot."

    })