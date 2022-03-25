from functions import *

class State():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class InitialState(State):
    def __init__(self, phonenumber):
        super().__init__("initial")
        self.phonenumber = phonenumber

    def on_event(self, event):
        if str(event).lower() in ["hi", "hello", "hey", "yo"]:
            return WelcomeState(self.phonenumber)      

        return self

class WelcomeState(State):
    def __init__(self, phonenumber):
        super().__init__("Welcome")
        self.phonenumber = phonenumber
        self.run()
    
    def run(self):
        menu = "Welcome to Christ embassy help desk\n\nZechariah 10:1 - Ask the LORD for rain in the springtime; it is the LORD who makes the storm clouds\n\nPlease choose\n\n1️⃣ Sermons\n2️⃣ Ministry News \n3️⃣ Christ Emabassy \n4️⃣Give/Donate \n5️⃣ Daily Devotional \n6️⃣Contact us \n\n*2022 \"Our Year Of The Gathering Clouds\"—Pastor Chris Oyakhilome*"

        send_sms(self.phonenumber, menu, "https://drive.google.com/uc?id=1qjg_VI2nNk7NJhOc9x4R-Dz_NCnPfeGA&export=download")

    def on_event(self, event):
        try:
            if int(event) ==1:
                return SermonsState(self.phonenumber)
            
            elif int(event) ==2:
                return NewsState(self.phonenumber)
            
            elif int(event) ==3:
                return EmbassyState(self.phonenumber)

            elif int(event) ==4:
                return DonateState(self.phonenumber)

            elif int(event) ==5:
                return SyllabusState(self.phonenumber)

            elif int(event) ==6:
                return SyllabusState(self.phonenumber)
            
            raise Exception("Invalid input")

        except Exception as e:
            send_sms(self.phonenumber, "Please enter a valid option")

            return self

class SyllabusState(State):
    def __init__(self, phonenumber):
        super().__init__("Syllabus")
        self.phonenumber = phonenumber
        self.run()
    
    def run(self):
        menu = "Nothing here\n\nSend #️⃣ - menu"

        send_sms(self.phonenumber, menu)

    def on_event(self, event):

        if str(event) == "#":
            return WelcomeState(self.phonenumber)
        
        return self

class EmbassyState(State):
    def __init__(self, phonenumber):
        super().__init__("Syllabus")
        self.phonenumber = phonenumber
        self.run()
    
    def run(self):
        menu = "Please select\n\n1️⃣ Find Church\n\nSend #️⃣ - menu"

        send_sms(self.phonenumber, menu)

    def on_event(self, event):
        if str(event) == "#":
            return WelcomeState(self.phonenumber)
        
        return SyllabusState(self.phonenumber)

class SermonsState(State):
    def __init__(self, phonenumber):
        super().__init__("Syllabus")
        self.phonenumber = phonenumber
        self.run()
    
    def run(self):
        menu = "Please select\n\na. pdfs\nb. audios\nc. videos\n\nSend #️⃣ - menu"

        send_sms(self.phonenumber, menu)

    def on_event(self, event):
        if str(event) == "#":
            return WelcomeState(self.phonenumber)
        
        return SyllabusState(self.phonenumber)

class NewsState(State):
    def __init__(self, phonenumber):
        super().__init__("Syllabus")
        self.phonenumber = phonenumber
        self.run()
    
    def run(self):
        menu = "Please select\n\na. Events\nb. Current\n \n\nSend #️⃣ - menu"

        send_sms(self.phonenumber, menu)

    def on_event(self, event):
        if str(event) == "#":
            return WelcomeState(self.phonenumber)
        
        return SyllabusState(self.phonenumber)
        
class DonateState(State):
    def __init__(self, phonenumber):
        super().__init__("Syllabus")
        self.phonenumber = phonenumber
        self.run()
    
    def run(self):
        menu = "Please select\n\na. Bank details\nb. Ecocash \n\nSend #️⃣ - menu"

        send_sms(self.phonenumber, menu)

    def on_event(self, event):
        if str(event) == "#":
            return WelcomeState(self.phonenumber)
        
        return SyllabusState(self.phonenumber)

class FindState(State):
    def __init__(self, phonenumber):
        super().__init__("Syllabus")
        self.phonenumber = phonenumber
        self.run()
    
    def run(self):
        menu = "Please select\n\na. Whatsapp group links\nb. Location \nc. Facebook \nd. Website \ne. Instagram \ng. Twitter \n\nSend #️⃣ - menu"

        send_sms(self.phonenumber, menu)

    def on_event(self, event):

        if str(event) == "#":
            return WelcomeState(self.phonenumber)
        
        return SyllabusState(self.phonenumber)

class Machine():
    def __init__(self, phone_num):
        self.phone_num = phone_num
        self.state = InitialState(phone_num)

    def on_event(self, event):

        self.state = self.state.on_event(event)

class Environment():
    machines = {}

    def recv(self, number, action):
        print(f"{number} - {action}")
        print(self.machines)

        if number in self.machines:
            state_machine = self.machines[number]

            state_machine.on_event(action)
            
        else:   
           new_machine = Machine(number)
           new_machine.on_event(action)
           self.machines[number] = new_machine

        return self.machines