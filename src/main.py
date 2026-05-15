from datetime import datetime 
import function

while True:
    print("=" * 20)
    print("Welcome to Mental Health Calculator")
    print("=" * 20)
    print("Please select your language / Pilih bahasa Anda:")
    print("1. English")
    print("2. Bahasa Indonesia")
    language = input("Your choice: ")
    
    if language == "1":
        function.en_question()
        print("\nCalculating your mental health status...")
        function.en_status_analysis()
        function.en_chk_reality()
        with open("results/results.txt", "a") as file:
            file.write(f"{datetime.now().strftime("%d-%m-%Y")} || {datetime.now().strftime("%H:%M:%S")} || Stress Score: {function.scores['stress']} || Anxiety Score: {function.scores['anxiety']} || Depression Score: {function.scores['depression']} \n")
        break
    elif language == "2":
        function.id_question()
        print("\nMenghitung status kesehatan mental Anda...")
        function.id_status_analysis()
        function.id_chk_reality()
        with open("results/results.txt", "a") as file:
            file.write(f"{datetime.now().strftime("%d-%m-%Y")} || {datetime.now().strftime("%H:%M:%S")} || Skor Stres: {function.scores['stress']} || Skor Anxiety: {function.scores['anxiety']} || Skor Depresi: {function.scores['depression']} \n")
        break
    else:
        print("Invalid choice, please try again.")