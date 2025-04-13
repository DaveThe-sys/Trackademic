import datetime

study_log = {}
study_goals = {}

while True:
    print("\nTrackademic: Track Smarter, Learn Faster!")
    print("1. Log Study Hours")
    print("2. View Logged Hours")
    print("3. Analyze Trends")
    print("4. Set Study Goals")
    print("5. Review Goals and Progress")
    print("6. Exit")
    
    choice = input("Choose an option (1-6): ")
    
    if choice == "1":
        print("Log your study hours for today:")
        subject = input("Enter the subject name: ")
        hours = float(input("Enter study hours for this subject: "))
        
        date_today = datetime.date.today().strftime("%Y-%m-%d")
        
        if subject not in study_log:
            study_log[subject] = {}
        
        study_log[subject][date_today] = hours
        print(f"Logged {hours} hours for {subject} on {date_today}")

    elif choice == "2":
        for subject, logs in study_log.items():
            print(f"\nStudy hours for {subject}:")
            for date, hours in logs.items():
                print(f"{date}: {hours} hours")

    elif choice == "3":
        for subject, logs in study_log.items():
            total_hours = sum(logs.values())
            avg_hours = total_hours / len(logs)
            print(f"\n{subject} - Total Hours: {total_hours}, Average per Day: {avg_hours:.2f} hours")

    elif choice == "4":
        subject = input("Enter the subject for your goal: ")
        goal_type = input("Enter goal type (daily/weekly/monthly): ").lower()
        
        if goal_type == "daily":
            goal = float(input("Enter your daily goal (hours): "))
        elif goal_type == "weekly":
            goal = float(input("Enter your weekly goal (hours): "))
        elif goal_type == "monthly":
            goal = float(input("Enter your monthly goal (hours): "))
        else:
            print("Invalid goal type!")
            continue
        
        study_goals[subject] = {"goal": goal, "type": goal_type}
        print(f"Goal set for {subject}: {goal} {goal_type}.")

    elif choice == "5":
        for subject, goal_data in study_goals.items():
            total_hours = sum(study_log.get(subject, {}).values())
            print(f"\n{subject} Goal: {goal_data['goal']} {goal_data['type']}, Total Hours Logged: {total_hours}")
            if total_hours >= goal_data['goal']:
                print(f"Congratulations! You've met your goal for {subject}.")
            else:
                print(f"Keep going! You need {goal_data['goal'] - total_hours} more hours to reach your goal.")

    elif choice == "6":
        print("Exiting program...")
        
        print("\nYour logged study hours:")
        for subject, logs in study_log.items():
            print(f"\n{subject}:")
            for date, hours in logs.items():
                print(f"{date}: {hours} hours")
        
        print("\nThank you for using Trackademic!")
        break

    else:
        print("Invalid choice. Please select a valid option.")

    continue_choice = input("\nDo you want to continue? (yes/no): ").lower()
    
    if continue_choice == "no":
        print("\nExiting program...")
        
        print("\nYour logged study hours:")
        for subject, logs in study_log.items():
            print(f"\n{subject}:")
            for date, hours in logs.items():
                print(f"{date}: {hours} hours")
        
        print("\nThank you for using Trackademic!")
        break
    elif continue_choice != "yes":
        print("Invalid input. Please enter 'yes' or 'no'.")
