import sqlite3

def create_database_with_five_topics():
    # Connect to SQLite database (it will create it if it doesn't exist)
    conn = sqlite3.connect('quiz_database.db')
    cursor = conn.cursor()

    # Create 'Coding' table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Coding (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_option TEXT NOT NULL
    )
    ''')

    # Create 'Early_US_History' table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Early_US_History (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_option TEXT NOT NULL
    )
    ''')

    # Create 'Economics' table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Economics (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_option TEXT NOT NULL
    )
    ''')

    # Create 'Criminal_Justice' table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Criminal_Justice (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_option TEXT NOT NULL
    )
    ''')

    # Create 'NBA' table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS NBA (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_option TEXT NOT NULL
    )
    ''')
      # Create 'user_info' table without username
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_info (
        id INTEGER PRIMARY KEY,
        chosen_topic TEXT NOT NULL,
        responses TEXT NOT NULL,
        grade REAL NOT NULL
    )
    ''')

    # Sample questions for 'Coding' topic
    coding_questions = [
        ("What is the keyword used to create a function in Python?", "function", "def", "create", "method", "B"),
        ("Which of these is a valid variable name in Python?", "2name", "_name", "name@", "name-1", "B"),
        ("Which operator is used for exponentiation in Python?", "+", "-", "*", "**", "D"),
        ("What is the output of 3 + 2 * 2 in Python?", "7", "10", "8", "5", "A"),
        ("What does 'len()' function do in Python?", "Find the length of a list", "Find the largest element", "Find the index of an element", "Find the sum of elements", "A"),
        ("Which of the following is used to handle exceptions in Python?", "try", "catch", "except", "error", "C"),
        ("Which data type is used to store True/False values?", "int", "str", "bool", "float", "C"),
        ("What is the default value of an uninitialized variable in Python?", "0", "None", "False", "undefined", "B"),
        ("Which function is used to get user input in Python?", "input()", "get_input()", "user_input()", "ask()", "A"),
        ("Which of these is a mutable data type in Python?", "str", "int", "list", "tuple", "C")
    ]

    # Sample questions for 'Early US History' topic
    early_us_history_questions = [
        ("Who was the first President of the United States?", "George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams", "A"),
        ("In which year did the Declaration of Independence get signed?", "1776", "1783", "1791", "1800", "A"),
        ("Who was the primary author of the Declaration of Independence?", "George Washington", "Abraham Lincoln", "Thomas Jefferson", "James Madison", "C"),
        ("Which war ended with the Treaty of Paris 1783?", "American Civil War", "World War I", "American Revolutionary War", "War of 1812", "C"),
        ("Who was the King of Great Britain during the American Revolution?", "King George III", "King Henry VIII", "King Charles I", "Queen Elizabeth", "A"),
        ("What was the name of the first permanent English colony in the Americas?", "New York", "Roanoke", "Jamestown", "Plymouth", "C"),
        ("Which event led to the start of the American Revolutionary War?", "Boston Tea Party", "Boston Massacre", "Signing of the Declaration of Independence", "Lexington and Concord", "D"),
        ("Which of these individuals was a leader in the Continental Army?", "Benjamin Franklin", "Thomas Paine", "George Washington", "Alexander Hamilton", "C"),
        ("What was the first major battle of the American Revolution?", "Battle of Lexington", "Battle of Bunker Hill", "Battle of Saratoga", "Battle of Yorktown", "B"),
        ("Which document officially ended the American Revolutionary War?", "Constitution", "Bill of Rights", "Treaty of Paris", "Magna Carta", "C")
    ]

    # Sample questions for 'Economics' topic
    economics_questions = [
        ("What is the basic economic problem?", "Scarcity", "Inflation", "Unemployment", "Recession", "A"),
        ("Which of these is considered a factor of production?", "Money", "Labor", "Stocks", "Interest rates", "B"),
        ("What does GDP stand for?", "Gross Domestic Product", "Gross Domestic Price", "Global Domestic Product", "Global Domestic Price", "A"),
        ("Which type of economy is characterized by private ownership and free markets?", "Socialism", "Communism", "Capitalism", "Feudalism", "C"),
        ("What is inflation?", "Increase in prices", "Increase in unemployment", "Decrease in production", "Decrease in prices", "A"),
        ("Which of these is a function of money?", "Store of value", "Store of goods", "Store of power", "Store of information", "A"),
        ("What does the law of supply state?", "As price rises, supply decreases", "As price rises, supply increases", "Supply is not affected by price", "Supply always stays constant", "B"),
        ("What is fiscal policy?", "Government spending and taxation", "Central bank interest rates", "Market regulation", "Public sector employment", "A"),
        ("What is opportunity cost?", "The cost of the next best alternative", "The cost of labor", "The cost of raw materials", "The cost of government regulation", "A"),
        ("Which of these is an example of a public good?", "National defense", "Private cars", "Personal computers", "Smartphones", "A")
    ]

    # Sample questions for 'Criminal Justice' topic
    criminal_justice_questions = [
        ("What is the primary purpose of criminal law?", "Punishment", "Deterrence", "Rehabilitation", "Protection of society", "D"),
        ("What is the term for a crime that is punishable by imprisonment for more than one year?", "Misdemeanor", "Infraction", "Felony", "Violation", "C"),
        ("What is the name of the legal process to determine if someone committed a crime?", "Trial", "Arrest", "Investigation", "Appeal", "A"),
        ("Which amendment in the U.S. Constitution protects against self-incrimination?", "Fourth Amendment", "Fifth Amendment", "Sixth Amendment", "Eighth Amendment", "B"),
        ("What is the legal term for a defendant's formal response to criminal charges?", "Plea", "Objection", "Motion", "Appeal", "A"),
        ("Which of the following is NOT a part of the criminal justice system?", "Prosecutor", "Defense attorney", "Judge", "School teacher", "D"),
        ("What is probation?", "Prison sentence", "Conditional release", "Community service", "Parole", "B"),
        ("Which of these is the first step in a criminal case?", "Arrest", "Grand jury indictment", "Trial", "Sentencing", "A"),
        ("What is the term for the formal charge of a crime?", "Complaint", "Indictment", "Conviction", "Verdict", "B"),
        ("Which of the following is an example of a white-collar crime?", "Burglary", "Robbery", "Embezzlement", "Murder", "C")
    ]

    # Sample questions for 'NBA' topic
    nba_questions = [
        ("Who is considered the greatest NBA player of all time?", "Michael Jordan", "LeBron James", "Kareem Abdul-Jabbar", "Magic Johnson", "A"),
        ("Which team won the most NBA championships?", "Los Angeles Lakers", "Boston Celtics", "Chicago Bulls", "Golden State Warriors", "B"),
        ("Who holds the record for the most points scored in a single NBA game?", "Kobe Bryant", "Wilt Chamberlain", "Michael Jordan", "LeBron James", "B"),
        ("Which NBA player is known as the 'Greek Freak'?", "Giannis Antetokounmpo", "Khris Middleton", "Nikola Jokic", "Luka Doncic", "A"),
        ("Which team drafted Dirk Nowitzki?", "Chicago Bulls", "Dallas Mavericks", "Milwaukee Bucks", "San Antonio Spurs", "C"),
        ("Who was the first overall pick in the 1996 NBA draft?", "Kobe Bryant", "Shaquille O'Neal", "Allen Iverson", "Steve Nash", "B"),
        ("Which NBA player has won the most MVP awards?", "Michael Jordan", "LeBron James", "Kareem Abdul-Jabbar", "Magic Johnson", "C"),
        ("What is the NBA's all-time leading scorer?", "Kareem Abdul-Jabbar", "LeBron James", "Karl Malone", "Wilt Chamberlain", "B"),
        ("Which team did Michael Jordan retire with?", "Chicago Bulls", "Washington Wizards", "Los Angeles Lakers", "Miami Heat", "B"),
        ("Who was the 2020 NBA Finals MVP?", "LeBron James", "Giannis Antetokounmpo", "Kawhi Leonard", "Jimmy Butler", "A")
    ]

    # Insert coding questions into the 'Coding' table
    cursor.executemany('''
    INSERT INTO Coding (question, option_a, option_b, option_c, option_d, correct_option)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', coding_questions)

    # Insert early US history questions into the 'Early_US_History' table
    cursor.executemany('''
    INSERT INTO Early_US_History (question, option_a, option_b, option_c, option_d, correct_option)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', early_us_history_questions)

    # Insert economics questions into the 'Economics' table
    cursor.executemany('''
    INSERT INTO Economics (question, option_a, option_b, option_c, option_d, correct_option)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', economics_questions)

    # Insert criminal justice questions into the 'Criminal_Justice' table
    cursor.executemany('''
    INSERT INTO Criminal_Justice (question, option_a, option_b, option_c, option_d, correct_option)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', criminal_justice_questions)

    # Insert nba questions into the 'NBA' table
    cursor.executemany('''
    INSERT INTO NBA (question, option_a, option_b, option_c, option_d, correct_option)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', nba_questions)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Create the database and tables
create_database_with_five_topics()
