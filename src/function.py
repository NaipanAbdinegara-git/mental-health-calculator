import csv
import random

scores = {'stress': 0, 'anxiety': 0, 'depression': 0}

def en_question():
    print("=" * 20)
    print("Mental Health Question:")
    print("=" * 20)
    print("Hint: Please answer with 1, 2, 3. The highest answer, the more you feel that way. Enter if it didnt apply with you at all.")
    print("Invalid answer will be considered as 0.")
    print("-" * 20)
    with open("data/dass21_en.csv", "r") as file:
        dictionary = csv.DictReader(file)
        row_question = list(dictionary)
        random.shuffle(row_question)
        for question in row_question:
            print(question['question'])
            answer = input("Your answer: ")
            if question["category"] =="stress":
                if answer == "1": scores['stress'] += 1
                elif answer == "2": scores['stress'] += 2
                elif answer == "3": scores['stress'] += 3
                else: print("Invalid answer, considered as 0")
            elif question["category"] =="anxiety":
                if answer == "1": scores['anxiety'] += 1
                elif answer == "2": scores['anxiety'] += 2
                elif answer == "3": scores['anxiety'] += 3
                else: print("Invalid answer, considered as 0")
            elif question["category"] =="depression":
                if answer == "1": scores['depression'] += 1
                elif answer == "2": scores['depression'] += 2
                elif answer == "3": scores['depression'] += 3
                else: print("Invalid answer, considered as 0")

def en_resilience_interpretation():
    s = scores['stress'] * 2
    a = scores['anxiety'] * 2
    d = scores['depression'] * 2
    
    if s >= 26 and a >= 15 and d >= 21:
        return '''
        Honestly, I see your burden is really heavy now, right? Feeling sad, anxious and 
        stressed at the same time, it definitely feels like I'm drowning but I can't ask for help.
        I want to say: It's okay to not be okay. You don't need to pretend to be strong in front of
        this program. These numbers are just your body's way of saying that you need complete rest and maybe
        you need someone to talk to. 
        '''
    elif d >= 14:
        return '''
        It seems like your depression level is quite high. It's like carrying a heavy backpack 
        that you can't put down, isn't it? Remember, it's okay to ask for help. You're not alone in this.
        Maybe consider talking to a mental health professional or reaching out to friends and family. 
        You're doing great by recognizing how you feel and seeking support. 
        '''
    elif a >= 10:
        return '''
        Oh no, your anxiety level is quite high. It's like having a little storm in your mind,
        isn't it? Remember, it's okay to feel anxious sometimes. You're not alone in this.
        Maybe try some deep breathing exercises or talk to someone you trust. 
        You're doing great by acknowledging how you feel. 
        '''
    elif s >= 19:
        return '''
        Whoops, your stress level is in overheat mode. The world is really noisy, isn't it?
        It's okay to take a break. Remember, you're human, not a machine that needs to be on 24/7.
        Take a breath; you're doing really well to make it this far. 
        '''
    else:
        return '''
        Wow, your scores are quite good! But remember, this is just a temporary snapshot.
        Keep taking care of your mental health in ways that you enjoy, okay! 
        '''

def en_status_analysis():
    # Menghitung skor final (skor mentah * 2)
    s = scores['stress'] * 2
    a = scores['anxiety'] * 2
    d = scores['depression'] * 2

    print("\n" + "=" * 20)
    print("Your Mental Health Status (DASS-21 Score x2):")
    print("=" * 20)
    print(f"Stress Score: {s}")
    print(f"Anxiety Score: {a}")
    print(f"Depression Score: {d}")
    print("-" * 20)
    print(en_resilience_interpretation()) # Langsung panggil interpretasi

def en_chk_reality():
    print("\n" + "=" * 20)
    print("Reality Check:")
    print("=" * 20)
    print("We know, that you're run this program because you want to understand your mental health better. That's a great step!")
    print("But remember, these scores are just numbers. They don't define you. They're just a snapshot of how you're feeling right now.")
    print("Please, turn off your laptop/phone for a moment after this. You need real oxygen, not screen light.")
    print("Go outside, take a walk, feel the breeze, listen to the birds. Nature has a way of healing us that no screen can replicate.")
    print("You're doing great by taking this step to understand your mental health better. Keep it up!")

# --- VERSI BAHASA INDONESIA ---

def id_question():
    print("=" * 20)
    print("Pertanyaan Kesehatan Mental:")
    print("=" * 20)
    print("Petunjuk: Jawab dengan 1, 2, atau 3. Semakin tinggi angka, semakin lo ngerasa kayak gitu. Tekan Enter kalau gak ngerasa kayak gitu sama sekali.")
    print("Jawaban tidak valid dianggap 0.")
    print("-" * 20)
    with open("data/dass21_id.csv", "r") as file:
        dictionary = csv.DictReader(file)
        row_question = list(dictionary)
        random.shuffle(row_question)
        for question in row_question:
            print(question['question'])
            answer = input("Jawaban lo: ")
            if question["category"] =="stress":
                if answer == "1": scores['stress'] += 1
                elif answer == "2": scores['stress'] += 2
                elif answer == "3": scores['stress'] += 3
                else: print("Jawaban tidak valid, dianggap sebagai 0")
            elif question["category"] =="anxiety":
                if answer == "1": scores['anxiety'] += 1
                elif answer == "2": scores['anxiety'] += 2
                elif answer == "3": scores['anxiety'] += 3
                else: print("Jawaban tidak valid, dianggap sebagai 0")
            elif question["category"] =="depression":
                if answer == "1": scores['depression'] += 1
                elif answer == "2": scores['depression'] += 2
                elif answer == "3": scores['depression'] += 3
                else: print("Jawaban tidak valid, dianggap sebagai 0")

def id_resilience_interpretation():
    s = scores['stress'] * 2
    a = scores['anxiety'] * 2
    d = scores['depression'] * 2
    
    if s >= 26 and a >= 15 and d >= 21:
        return '''
        Jujur, gue liat beban lo lagi berat banget ya sekarang? Ngerasa sedih, cemas, dan 
        stres sekaligus itu rasanya pasti kayak lagi tenggelam tapi nggak bisa minta tolong. 
        Gue mau bilang: It's okay to not be okay. Lo nggak perlu pura-pura kuat di depan program ini.
        Angka-angka ini cuma cara tubuh lo bilang kalau lo butuh istirahat total dan mungkin butuh temen buat cerita. 
        '''
    elif d >= 14:
        return '''
        Lagi ngerasa mendung banget ya di dalam sana? 
        Gak apa-apa kalau lo ngerasa gak punya energi hari ini. Cahaya itu bakal balik lagi kok,
        pelan-pelan aja. Jangan lupa buat cerita ke orang yang lo percaya, ya. 
        '''
    elif a >= 10:
        return '''
        Gue liat ada rasa cemas yang lagi nemenin lo. Jantung rasanya berisik ya?
        Tenang, lo aman di sini. Coba fokus ke hal-hal yang bisa lo kontrol aja sekarang. 
        Step by step, Pan. Lo nggak sendirian kok.
        '''
    elif s >= 19:
        return '''
        Whoops, tingkat stres lo lagi overheat nih. Dunia ini bener-bener berisik ya?
        Gak apa-apa buat istirahat sejenak. Ingat, lo manusia, bukan mesin yang harus terus nyala 24/7. 
        Tarik napas; lo udah hebat banget bisa sampai sejauh ini. 
        '''
    else:
        return '''
        Wah, skor lo cukup baik nih! Tapi ingat, ini cuma gambaran sementara aja. 
        Tetap jaga kesehatan mental lo dengan cara yang lo suka, ya! 
        '''

def id_status_analysis():
    s = scores['stress'] * 2
    a = scores['anxiety'] * 2
    d = scores['depression'] * 2

    print("\n" + "=" * 20)
    print("Status Kesehatan Mental Lo (Skor DASS-21 x2):")
    print("=" * 20)
    print(f"Skor Stres: {s}")
    print(f"Skor Kecemasan: {a}")
    print(f"Skor Depresi: {d}")
    print("-" * 20)
    print(id_resilience_interpretation())

def id_chk_reality():
    print("\n" + "=" * 20)
    print("Reality Check:")
    print("=" * 20)
    print("Kita tau, lo jalanin program ini karena pengen ngerti kesehatan mental lo lebih baik. Itu langkah yang bagus!")
    print("Tapi ingat, skor ini cuma angka. Mereka gak mendefinisikan lo. Mereka cuma gambaran gimana perasaan lo sekarang.")
    print("Tolong, matiin laptop/handphone lo sebentar setelah ini. Lo butuh oksigen asli, bukan cahaya layar.")
    print("Keluar, jalan-jalan, rasain angin, dengerin burung. Alam punya cara buat nyembuhin kita yang gak bisa digantikan sama layar.")
    print("Lo udah hebat banget dengan langkah ini buat ngerti kesehatan mental lo lebih baik. Terus semangat!")