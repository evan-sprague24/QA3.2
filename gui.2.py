import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import json

# Function to connect to the SQLite database and retrieve questions for the selected topic
def get_questions_for_topic(topic):
    conn = sqlite3.connect('quiz_database.db')
    cursor = conn.cursor()

    # Retrieve 10 questions based on the selected topic
    cursor.execute(f"SELECT * FROM {topic} LIMIT 10")
    questions = cursor.fetchall()
    conn.close()

    return questions

# Function to save the user's responses and grade to the database
def save_user_info(topic, responses, grade):
    conn = sqlite3.connect('quiz_database.db')
    cursor = conn.cursor()

    # Insert the user's responses and grade into the user_info table
    cursor.execute('''
    INSERT INTO user_info (chosen_topic, responses, grade) 
    VALUES (?, ?, ?)
    ''', (topic, json.dumps(responses), grade))

    conn.commit()
    conn.close()

# Function to handle the quiz logic and open the quiz window
def start_quiz_window(selected_topic):
    # Open the second window for the quiz
    quiz_window = tk.Toplevel()
    quiz_window.title(f"{selected_topic} Quiz")

    # Retrieve questions for the selected topic from the database
    questions = get_questions_for_topic(selected_topic)

    # Store the user's responses and score
    responses = []
    score = 0

    # Create the question UI components (Question Label, Answer Choices)
    question_label = tk.Label(quiz_window, text="Question will appear here.", width=50, wraplength=400)
    question_label.pack(pady=20)

    answer_var = tk.StringVar()

    # Create a Combobox (dropdown) for the answer options
    answer_combobox = ttk.Combobox(quiz_window, values=["Option A", "Option B", "Option C", "Option D"], state="readonly", width=30)
    answer_combobox.set("Select an answer")  # Default text
    answer_combobox.pack(pady=10)

    # Create the submit button (disabled initially)
    submit_button = tk.Button(quiz_window, text="Submit Answer", command=None, state="disabled")
    submit_button.pack(pady=10)

    # Function to enable the submit button when an option is selected
    def enable_submit_button(event):
        if answer_combobox.get() != "Select an answer":
            submit_button.config(state="normal")

    # Bind the event when an option is selected from the combobox
    answer_combobox.bind("<<ComboboxSelected>>", enable_submit_button)

    # Function to display the next question
    def next_question(question_index):
        nonlocal score
        question_data = questions[question_index]
        question_text = question_data[1]  # The question text
        options = [question_data[2], question_data[3], question_data[4], question_data[5]]  # option_a, option_b, option_c, option_d
        correct_answer = question_data[6]  # correct_option

        # Display the current question
        question_label.config(text=question_text)

        # Set the combobox values with the answer options from the database
        answer_combobox['values'] = options  # Update combobox with current question's options
        answer_combobox.set("Select an answer")  # Reset combobox selection

        # Function to submit the answer and check it
        def submit_answer():
            nonlocal score

            selected_answer = answer_combobox.get()

            # Check if the answer is correct
            if selected_answer == correct_answer:
                score += 1
                messagebox.showinfo("Correct", "Your answer is correct!")
            else:
                messagebox.showerror("Incorrect", f"Your answer is incorrect! The correct answer is {correct_answer}.")

            # Store the response
            responses.append({
                'question': question_text,
                'user_answer': selected_answer,
                'correct_answer': correct_answer
            })

            # Disable the submit button after the user submits an answer
            submit_button.config(state="disabled")

            # Move to the next question or finish the quiz
            if question_index + 1 < len(questions):
                next_question(question_index + 1)
            else:
                grade = (score / len(questions)) * 100
                messagebox.showinfo("Quiz Completed", f"Your final score is {grade:.2f}%")
                save_user_info(selected_topic, responses, grade)
                quiz_window.destroy()
                root.deiconify()  # Show the main window again

        # Update the submit button's command to call submit_answer
        submit_button.config(command=submit_answer)

    # Start the quiz by displaying the first question
    next_question(0)

# Function to show the first window (topic selection)
def start_topic_selection_window():
    global root
    root = tk.Tk()
    root.title("Quiz Topic Selection")

    # Label to display the prompt
    label = tk.Label(root, text="Select a topic to start the quiz", font=("Arial", 14))
    label.pack(pady=20)

    # Dropdown (ComboBox) for topic selection
    topics = ["NBA", "Criminal_Justice", "Economics", "Early_US_History", "Coding"]
    topic_combobox = ttk.Combobox(root, values=topics, state="readonly", width=20)
    topic_combobox.pack(pady=10)
    topic_combobox.set(topics[0])  # Default to first topic

    def start_quiz():
        selected_topic = topic_combobox.get()
        root.withdraw()  # Hide the first window
        start_quiz_window(selected_topic)  # Open the quiz window for the selected topic

    # Button to start the quiz
    start_button = tk.Button(root, text="Start Quiz", command=start_quiz, width=20)
    start_button.pack(pady=20)

    # Run the GUI
    root.mainloop()

# Start the first window (topic selection)
start_topic_selection_window()