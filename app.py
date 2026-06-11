import gradio as gr

def greeting(greeting,start):
    greeting = input()
    if greeting == "start":
        start=True
        return "Chatbot started!",start
    elif greeting=="stop":
        start=False
        return "Bye byee!",start
        
    
 
            

        #defining a function for random joke   
def randomjoke():
    import random
    joke=["Why do skeletons don't fight each other? Because they don't have the guts.","How do pirates kill someone? They seas them.","What do you call fake spaghetti? An impasta.","How do dyslexic poets write? With verse mistakes.","How does a computer get drunk? It takes screenshots.","Why don’t graveyards ever get overcrowded? Because people are just dying to get in."]
    return random.choice(joke)
            


        #defining a function for song recommendation
def songrecommendation(emotion, language):
    import random
    emotion=emotion.lower()
    language=language.lower()
    Match=False
    while not Match:
        if emotion not in ["happy","sad","romantic","nostalgic"]:
            Match=False
            return "Please enter an emotion from happy, sad, romantic, nostalgic"
        elif language!="hindi" and language.lower()!="english":
            Match=False
            return "Please enter a language from hindi or english"
        else: 
            Match=True
            
            
    if emotion=="happy":
        happyenglishsongs=["Walking on Sunshine — Katrina and the Waves ☀️","Happy — Pharrell Williams 😄","Shut Up and Dance — WALK THE MOON 💃","Best Day of My Life — American Authors 🌈","Can’t Stop the Feeling! — Justin Timberlake 🕺","Good as Hell — Lizzo 💅","Sugar — Maroon 5 🍭","Uptown Funk — Mark Ronson ft. Bruno Mars 🎷","Count on Me — Bruno Mars 🌻","On Top of the World — Imagine Dragons ☁️","Firework — Katy Perry 🎆","Dance Monkey — Tones and I 🐒","Good Time — Owl City & Carly Rae Jepsen 🎡","Best Song Ever — One Direction 🎤","Shake It Off — Taylor Swift 💫"]
        happyhindisongs=["Gallan Goodiyan – Dil Dhadakne Do","Kar Gayi Chull – Kapoor & Sons","London Thumakda – Queen","Badtameez Dil – Yeh Jawaani Hai Deewani","Ilahi – Yeh Jawaani Hai Deewani","Dil Dhadakne Do (Title Track) – Zindagi Na Milegi Dobara","Zinda – Bhaag Milkha Bhaag","Desi Girl – Dostana","Koi Kahe Kehta Rahe – Dil Chahta Hai","Phir Se Ud Chala – Rockstar","Aal Izz Well – 3 Idiots","Senorita – Zindagi Na Milegi Dobara","Sooraj Dooba Hai – Roy"]
                
        if language=="english":
            
            song_choice=random.sample(happyenglishsongs,3)
            return "\n".join(song_choice)+"\nThese are some songs I chose for you!!"
                
        elif language=="hindi":
            
            song_choice=random.sample(happyhindisongs,3)
            return "\n".join(song_choice)+"\nThese are some songs I chose for you!!"
            
    elif emotion=="sad":
            sadenglishsongs=["Someone Like You - Adele","Fix You - Coldplay","Hurt - Johnny Cash","Everybody Hurts - R.E.M.","The Night We Met - Lord Huron","Say You Love Me - Jessie Ware","Skinny Love - Bon Iver","Tears Dry On Their Own - Amy Winehouse","All I Want - Kodaline","Let Her Go - Passenger","Creep - Radiohead","Lost - Michael Bublé","Back to December - Taylor Swift","I Will Remember You - Sarah McLachlan","Hallelujah - Jeff Buckley"]
            sadhindisongs=["Channa Mereya - Ae Dil Hai Mushkil", "Tadap Tadap - Hum Dil De Chuke Sanam", "Agar Tum Saath Ho - Tamasha", "Kabira - Yeh Jawaani Hai Deewani", "Tujhe Kitna Chahne Lage - Kabir Singh", "Phir Le Aaya Dil - Barfi!", "Humari Adhuri Kahani - Humari Adhuri Kahani", "Tum Hi Ho - Aashiqui 2", "Ae Dil Hai Mushkil - Ae Dil Hai Mushkil", "Bhula Dena - Aashiqui 2", "Hawayein - Jab Harry Met Sejal", "Main Phir Bhi Tumko Chahunga - Half Girlfriend", "Kaise Hua - Kabir Singh", "Judaai - Badlapur", "Mann Bharryaa - Shershaah"]
                
            if language== "english":
                
                song_choice=random.sample(sadenglishsongs,3)
                return "\n".join(song_choice)+"\nThese are some songs I chose for you!!"
            elif language=="hindi":
                
                song_choice=random.sample(sadhindisongs,3)
                return "\n".join(song_choice)+"\nThese are some songs I chose for you!!"  
                
           
            
            
    elif emotion=="romantic":
            englishromanticsongs = ["Perfect - Ed Sheeran", "All of Me - John Legend", "Thinking Out Loud - Ed Sheeran", "I Don't Want to Miss a Thing - Aerosmith", "Can't Help Falling in Love - Elvis Presley", "You Are the Reason - Calum Scott", "A Thousand Years - Christina Perri", "Make You Feel My Love - Adele", "Love Me Like You Do - Ellie Goulding", "Everything - Michael Bublé", "Just the Way You Are - Bruno Mars", "My Heart Will Go On - Celine Dion", "Stay With Me - Sam Smith", "Something - The Beatles", "Kiss Me - Sixpence None The Richer"]
            hindiromanticsongs= ["Tum Hi Ho - Aashiqui 2", "Raabta - Agent Vinod", "Tera Ban Jaunga - Kabir Singh", "Jeene Laga Hoon - Ramaiya Vastavaiya", "Pee Loon - Once Upon a Time in Mumbaai", "Tum Se Hi - Jab We Met", "Sun Saathiya - ABCD 2", "Hawayein - Jab Harry Met Sejal", "Janam Janam - Dilwale", "Kaun Tujhe - M.S. Dhoni", "Gerua - Dilwale", "Roke Na Ruke Naina - Badrinath Ki Dulhania", "Samjhawan - Humpty Sharma Ki Dulhania", "Enna Sona - Ok Jaanu", "Bolna - Kapoor & Sons"]
            language=input("Enter the language you prefer, Hindi or English")
            if language=="english":
                
                song_choice=random.sample(englishromanticsongs,3)
                return "\n".join(song_choice)+"\nThese are some songs I chose for you!!"
            elif language=="hindi":
                
                song_choice=random.sample(hindiromanticsongs,3)
                return "\n".join(song_choice)+"\nThese are some songs I chose for you!!"
            
    elif emotion=="nostalgic":
            nostaligicenglishsongs=["Yesterday - The Beatles", "Summer of '69 - Bryan Adams", "Time After Time - Cyndi Lauper", "With or Without You - U2", "Landslide - Fleetwood Mac", "Hotel California - Eagles", "Tears in Heaven - Eric Clapton", "Don't Stop Believin' - Journey", "Fix You - Coldplay", "Somewhere I Belong - Linkin Park", "My Immortal - Evanescence", "Everybody Wants to Rule the World - Tears for Fears", "Iris - Goo Goo Dolls", "The Scientist - Coldplay", "Fast Car - Tracy Chapman"]
            nostaligichindisongs=["Tujhse Naraz Nahin Zindagi - Masoom", "Chura Liya Hai Tumne Jo Dil Ko - Yaadon Ki Baaraat", "Lag Jaa Gale - Woh Kaun Thi?", "Kabhi Kabhi Mere Dil Mein - Kabhi Kabhie", "Pal Pal Dil Ke Paas - Blackmail", "Chingari Koi Bhadke - Amar Prem", "Ae Mere Humsafar - Baazigar", "Mere Sapno Ki Rani - Aradhana", "Yeh Shaam Mastani - Kati Patang", "Roop Tera Mastana - Aradhana", "Tere Bina Zindagi Se - Aandhi", "Kya Hua Tera Wada - Hum Kisise Kum Naheen", "Pyar Hua Ikrar Hua - Shree 420", "Ajeeb Dastan Hai Yeh - Dil Apna Aur Preet Parai", "Baharon Phool Barsao - Suraj"]
            if language== "english":
                song_choice=random.sample(nostaligicenglishsongs,3)
                return "\n".join(song_choice)+"\nThese are some songs I chose for you!!"
            elif language=="hindi":
                
                song_choice=random.sample(nostaligichindisongs,3)
                return "\n".join(song_choice)+"\nThese are some songs I chose for you!!"    
                

def quotes():
            import random 
            quotes=["Stars can’t shine without darkness.","Fall seven times, stand up eight.","Your only limit is your mind.","The wound is where the light enters.","Do it scared, but do it anyway.", "Even the moon is alone, but still shines.","Grow through what you go through.","Silence is sometimes the loudest scream.","You’re stronger than you think.","Dreams don’t work unless you do."]
            print(random.choice(quotes))       

        
            
                
def rps_logic(userchance,Yourpoints,Mypoints):
    chance=["rock","paper","scissors"]
                    

    import random
    computer_choice = random.choice(chance)
    if userchance==computer_choice:
                         result= "draw"
    elif (userchance=="rock" and computer_choice=="scissors") or (userchance=="paper" and computer_choice=="rock") or (userchance=="scissors" and computer_choice=="paper"):
                         
                         Yourpoints+=1
                         result= "Your point"
    else:
                         Mypoints+=1
                         result= "My point"
    return result, computer_choice, Yourpoints, Mypoints
            
    Yourpoints= 0
    Mypoints=0 
    Chance=["rock","paper","scissors"]
            
            
def rps_play(userchance, Mypoints, Yourpoints):
                   result, computer_choice, Yourpoints, Mypoints=rps_logic(
                        userchance, Yourpoints, Mypoints)
                   output = f"""
            Computer chose{computer_choice}   
            You chose: {userchance} 
            Result= {result} 
            Score= You: {Yourpoints}  Me:{Mypoints}
            """
                   return output, Yourpoints, Mypoints
                  
            


import random      
def guess_the_number(userguess,secretnumber):
                userguess=int(userguess)
                if secretnumber is None:
                     secretnumber= random.randint(1,100)
                
                if userguess==secretnumber:    
                    message=("You guessed it! ")
                
                elif userguess>secretnumber:
                     message=("The number is lower than your guess")
                else:
                     message=("The number is greater than your guess ")
                return message, secretnumber
            
            

                     
def getword(category):
                import random
                category=category.strip().lower()
                if category=="fruits" or category=="fruits " or category=="fruit":
                    fruits=["apple","banana","grapes","watermelon","raspberry","mango","pineapple","blueberry","kiwi","orange"]
                    word=random.choice(fruits)
                    return word
                elif category=="animals" or category=="animal " or category=="animal":
                    
                    animals=["leopard","goat","buffalo","cheetah","deer","wolf","penguin","octopus","jellyfish","panther"]
                    word=random.choice(animals)
                    return word
                elif category=="sports" or category=="sport":
                    sports=["tennis","badminton","hockey","skateboarding","squash","handball","fencing","archery","polo","lacrosse"]
                    word=random.choice(sports)
                    return word
                elif category=="vehicles" or category=="vehicle":
                    vehicles=["bulldozer","dumptruck","excavator","tram","cargo","ferry","rickshaw","kayak","tractor","minibus"]
                    word=random.choice(vehicles)
                    return word
                else:
                     return None



stage1="""
                    +----+
                    │    │
                         │
                         │
                         │
                         │
                    ========


                            """
stage2= """
                    +----+
                    │    │
                    O    │
                         │
                         │
                         │
                         │
                    ========
                            """
stage3="""
                    +----+
                    │    │
                    O    │
                    │    │
                         │
                         │
                         │
                    ========
                    """
stage4="""
                    +----+
                    │    │
                    O    │
                    │    │
                   /     │
                         │
                         │
                    ========
                    """
stage5="""
                    +----+
                    │    │
                    O    │
                    │    │
                   / \   │
                         │
                         │
                    ========
                    """
stage6="""
                    +----+
                    │    │
                    O    │
                   /│    │
                   / \   │
                         │
                         │
                    ========
                    """
stage7="""
                    +----+
                    │    │
                    O    │
                   /│\   │
                   / \   │
                         │
                         │
                    ========
                    """
hangmanstages=[stage1,stage2,stage3,stage4,stage5,stage6,stage7]  
                
def hgame(word_state, blank_state,letterguess,wrong_state):
                print("hgame input", word_state,blank_state,wrong_state)
                print("type blanks",type(blank_state))
                wrong=wrong_state
                
                hangmanstages=[stage1,stage2,stage3,stage4,stage5,stage6,stage7]
                blanks=blank_state
                blanks=list(blanks)
                correct=False               
                for i in range(0,len(word_state)):
                            if letterguess==word_state[i]:
                                blanks[i]=letterguess
                                correct=True 
                if correct==False:
                            wrong=wrong+1
                won="_" not in blanks
                lost= wrong==6
                print("wrong",wrong)
                display=hangmanstages[wrong]
                return word_state, ("".join(blanks)),wrong,display,wrong, won,lost
                

word_state=gr.State()
blank_state=gr.State()
wrong_state=gr.State()

inputs=[
        word_state, 
        blank_state,
                    
        gr.Textbox(label="Letter"),
                    wrong_state]    


             
outputs=[word_state, blank_state, wrong_state,
                    gr.Textbox(label="Word Progress"),
                     gr.Number(label="Wrong Guesses"),
                    
                     gr.Textbox(label="Hangman"),
                     gr.Textbox(label="Won"),
                     gr.Textbox(label="Lost") ]
mode_state=gr.State()
                   

def getresponse(userinput):
    userinput=userinput.lower()
    print("Input received", userinput)
    if userinput=="start":
        return ("Type 'song recommendation' for song recommendations\n Type 'joke' for jokes\n Type 'quotes' for quotes\n Type'games' for games.")
        
    if userinput in ["jokes","joke","joke ","jokes "]:
        return randomjoke()
    elif userinput in ["song recommendation","songs","song recommendations","songrecommendation"]:
           
        return "How are you feeling? (happy, sad, romantic, nostalgic)"
    elif userinput in ["quotes","quote"]:
        return quotes()
    elif userinput in ["game","games"]:
        return "Which game? Hangman/ Rock Paper Scissors/ Guess The Number"
    elif userinput=="stop":
        return "Great to meet you! Bye byee!"
           
            
    else:
        return "I did not get you- LOL!"

          
     

quote_state = gr.State("Motivational Quotess!")
joke_state = gr.State("Jokess?")
song_state= gr.State("SONG RECOMMENDATIONSSS")
game_state= gr.State("WANNA PLAYY?")


def reply(message,history,state):
     print("STATE DEBUG:", state)
     print("MESSAGE DEBUG:", message)
     print("STATE:",state)
     print(type(state))
     message=message.lower()
     response= ("Something went wrong. Please try again.")
     if state=="waiting_for_start":
          if message=="start":
           response=getresponse("start")
           state="active"
          else:
           response="Please enter 'start' to begin"
               
     elif state=="active":
           
    # ["start", "song recommendation", "quotes", "joke","songs","song", "stop", "game","quote","jokes","games","songs","song recommendations"]
           if message.lower() in ["quotes", "joke","quote","jokes"]:
                response=getresponse(message)
           elif message.lower() in ["song recommendation","songs","song","song recommendations","songrecommendation"]:
                response= "How are you feeling? (happy, sad, romantic, nostalgic)"
                state="waiting_for_emotion"
           
           elif message.lower() in ["games","game"]:
                response="Which game? (Hangman, guess the number, rock paper scissors)"
                state="waiting_for_game"
           else:
                response="I did not get you- LOL"
     
     elif state=="waiting_for_emotion":
          emotion=message
          response="Which language? (hindi or english)"
          state=("waiting_for_language",emotion)
     
     elif isinstance(state,tuple) and state[0]=="waiting_for_language":
          print("STATE RECEIVED:", state) 
          emotion=state[1]
          language=message
          response=songrecommendation(emotion,language)
          state="active"
     
     elif state=="waiting_for_game":
        if message=="hangman":
                state="waiting_for_category"
                response="Choose category: fruits, animal, vehicles, sports"
    
            
        

        elif message=="rock paper scissors":
                state=("rps",0,0)
                response="Rock Paper Scissors started, type rock/paper/scissors"
        
        elif message=="guess the number":
                secret_number=random.randint(1,100)
                state=("guess_number",secret_number)
                response="Guess the number started, guess a number between 1 to 100!"
        elif state=="guess_number":
           response, secret_number=guess_the_number(message,secret_number)     
       

        else:
                response="Invalid game"
     elif isinstance(state,tuple) and state[0]=="guess_number":
              secret_number=state[1]
              response, secret_number=guess_the_number(message,secret_number)
              state=("guess_number",secret_number)  
     elif state=="waiting_for_category": 
           print("entered category block") 
           category_word=getword(message)
           print("category word is",category_word)
           if not category_word:
                 response="Invalid category. Try: fruits, sports, vehicles, animals"
                 
           else:
                 blanks=["_"]* len(category_word)
                 wrong=0
                 state=("hangman",category_word,blanks,wrong)
                 response="Hangman started! Guess a letter"
     
     elif isinstance(state,tuple) and state[0]=="hangman":
           word, blanks, wrong= state[1], state[2], state[3]
           print("DEBUG BEFORE HANGMAN:", word, blanks, wrong)
           print(type(blanks))
           word, blanks, wrong,_,_, won, lost, =hgame(word, blanks, message, wrong) 
           state= ("hangman",word,blanks,wrong) 
           wrong=min(wrong, len(hangmanstages)-1)    
           response=(
                 f"{''.join(blanks)}\n"
                 f"wrong guesses:{wrong}\n"
                 f"{hangmanstages[wrong]}\n"
                 f"{'You won' if won else''}"
                 f"{'You lost'if lost else''}"
           )     
     elif isinstance(state,tuple) and state[0]=="rps":
           Yourpoints=state[1]
           Mypoints=state[2]
           response, Yourpoints, Mypoints=rps_play(message, Mypoints, Yourpoints)
           state=("rps",Yourpoints, Mypoints)
     
     history.append({"role":"user","content":message})
     history.append({"role":"assistant","content":response})
     return history, "", state
     


with gr.Blocks() as demo:
     conversation_state=gr.State("waiting_for_start")
     gr.Markdown("<h1 style='text-align:center;color:#A020F0;'>anushka 2.0 <3 </h1>")
     chatbot= gr.Chatbot(
          value=[{"role":"assistant","content": "Heyy! Enter 'start' to interact with me!"}],
          height=500)
     msg=gr.Textbox(placeholder="Type something",label="Your message")
     msg.submit(reply,[msg,chatbot,conversation_state],[chatbot,msg,conversation_state])
demo.launch(share=True)
