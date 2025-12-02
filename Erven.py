users = {
    "admin": "Admin123",
    "Francis": "Gikapoynako",
    "Jhamer": "Paragoso2006",
    "Erven": "Erven125",
    "Bolanio": "Maria111",
    "Christine": "33442"
}

requests = []

def login():
    print("LOGIN")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
        return username
    else:
        print("Invalid username or password.")
        return None

def student_portal(username):
    while True:
        print(f"Student Portal ({username})")
        print("1. Request a Document")
        print("2. View My Requests")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Select a document to request:")
            documents = ["School ID", "Good Moral", "Form 137", "Diploma"]

            for i, doc in enumerate(documents, 1):
                print(f"{i}. {doc}")

            doc_choice = input("Enter number: ")

            if doc_choice.isdigit() and 1 <= int(doc_choice) <= len(documents):
                selected_doc = documents[int(doc_choice) - 1]
                requests.append({
                    "student": username,
                    "document": selected_doc,
                    "status": "Pending"
                })
                print(f"Request for '{selected_doc}' submitted successfully!")
            else:
                print("Invalid choice.")

        elif choice == "2":
            print("My Requests")
            found = False
            for r in requests:
                if r["student"] == username:
                    print(f"- {r['document']} [Status: {r['status']}]")
                    found = True
            if not found:
                print("No requests yet.")

        elif choice == "3":
            print("Logging out")
            break

        else:
            print("Invalid option. Try again.")

def admin_portal(username):
    while True:
        print(f"Admin Portal ({username})")
        print("1. View All Requests")
        print("2. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            if not requests:
                print("No student requests yet.")
            else:
                print("Student Requests")
                for i, req in enumerate(requests, 1):
                    print(f"{i}. {req['student']} - {req['document']} [Status: {req['status']}]")

                action = input("Enter request number to approve/disapprove or 'b' to go back: ")

                if action.isdigit():
                    index = int(action) - 1
                    if 0 <= index < len(requests):
                        print(f"Selected: {requests[index]['student']} - {requests[index]['document']}")
                        print("1. Approve")
                        print("2. Disapprove")
                        act = input("Enter choice: ")

                        if act == "1":
                            requests[index]["status"] = "Approved"
                            print("Request approved!")
                        elif act == "2":
                            requests[index]["status"] = "Disapproved"
                            print("Request disapproved.")
                        else:
                            print("Invalid choice.")
                    else:
                        print("Invalid request number.")

        elif choice == "2":
            print("Logging out.")
            break
        else:
            print("Invalid choice.")

while True:
    print("SCHOOL DOCUMENT REQUEST SYSTEM")
    user = login()

    if user:
        if user == "admin":
            admin_portal(user)
        else:
            student_portal(user)

    again = input("Do you want to log in again? (y/n): ")
    if again != "y":
        print("Goodbye!")
        break
