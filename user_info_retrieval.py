import sqlite3
import json

# Function to retrieve information from the user_info table
def get_user_info(user_id=None):
    conn = sqlite3.connect('quiz_database.db')
    cursor = conn.cursor()

    # If a user_id is provided, retrieve only the record for that user
    if user_id:
        cursor.execute('''
        SELECT id, chosen_topic, responses, grade 
        FROM user_info 
        WHERE id = ?
        ''', (user_id,))
    else:
        # Otherwise, retrieve all records from the user_info table
        cursor.execute('''
        SELECT id, chosen_topic, responses, grade 
        FROM user_info
        ''')

    # Fetch all results (or a single result if filtered by user_id)
    records = cursor.fetchall()

    conn.close()

    # Process the responses stored as JSON in the database
    user_info = []
    for record in records:
        user_data = {
            'id': record[0],
            'chosen_topic': record[1],
            'responses': json.loads(record[2]),  # Convert JSON string back to a Python list/dict
            'grade': record[3]
        }
        user_info.append(user_data)

    return user_info

# Example usage:

# Fetch all user info records
all_user_info = get_user_info()
print("All User Info:")
for user in all_user_info:
    print(user)

# Fetch info for a specific user by id (e.g., user with id = 1)
specific_user_info = get_user_info(user_id=1)
print("\nSpecific User Info:")
print(specific_user_info)