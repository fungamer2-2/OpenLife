# OpenLife Alpha 17

# OpenLife is a FOSS replacement for BitLife.
# For years, BitLife has become worse and worse, so I decided to step in and
# replace it with this. It's way better. Trust me.

from random import choice
from random import randint as rng
from time import sleep
from platform import uname
import os, signal, logging

__author__ = "WinFan3672 [winfan3672.000webhostapp.com]"
def exit_script():
    global coworkers
    coworkers = []
    generate_co_workers()
    l = coworkers
    n = 1
    for item in l:
        item.list(n)
        n += 1
class CoWorker:
    def __init__(self):
        self.name="NoName"
        self.age=0
        self.end=0
        self.rel=0
        self.lvl = 0
        ## Level 1 = Co-Worker
        ## Level 2 = HR
        ## Level 3 = Supervisor
        self.intel=0
        self.looks=0
        self.craziness=0
        self.prof=0
        self.cool=0
        self.friskiness=0
        self.gender=0
    def compile(self, gender, level = 1):
        self.gender = gender
        if self.gender == 1:
            self.name = f"{choice(forename_f)} {choice(surnames)}"
        else:
            self.name = f"{choice(forename_m)} {choice(surnames)}"
        self.age = rng(25,65)
        self.rel = rng(1,100)/100
        self.intel = rng(1,100)/100
        self.lvl = level
        self.looks = rng(1,100)/100
        self.craziness = rng(1,100)/100
        self.prof = rng(1,100)/100
        self.cool = rng(1,100)/100
        self.friskiness = rng(1,100)/100
    def list(self, n):
        print(self.name)
        if self.gender == 0:
            prit("Male")
        else:
            print("Female")
        print(f"Age: {self.age}")
        print(f"Relationship:   ",pbar2(self.rel),f"{int(self.rel * 100)}%")
        print(f"Professionalism:",pbar2(self.prof),f"{int(self.prof * 100)}%")
        print(f"Coolness:       ",pbar2(self.cool),f"{int(self.cool * 100)}%")
        print(f"Friskiness:     ",pbar2(self.friskiness),f"{int(self.friskiness * 100)}%")
        if self.lvl == 1:
            print("Co-Worker")
        elif self.lvl == 2:
            print("HR Member")
        elif self.lvl == 3:
            print("Supervisor")
        else:
            raise FeatureNotInGameError
        print(f"[{n}] Interact")
        div()
    def interact(self):
        global gender, happiness, job_id, salary, hours
        if self.rel > 1:
            self.rel = 1
        if self.rel < 0:
            self.rel = 0
        print(self.name)
        if self.gender == 0:
            print("Male")
        else:
            print("Female")
        div()
        print(f"Age: {self.age}")
        print(f"Relationship:   ",pbar2(self.rel),f"{int(self.rel * 100)}%")
        print(f"Professionalism:",pbar2(self.prof),f"{int(self.prof * 100)}%")
        print(f"Coolness:       ",pbar2(self.cool),f"{int(self.cool * 100)}%")
        print(f"Friskiness:     ",pbar2(self.friskiness),f"{int(self.friskiness * 100)}%")
        if self.lvl == 1:
            print("Co-Worker")
        elif self.lvl == 2:
            print("HR Member")
        elif self.lvl == 3:
            print("Supervisor")
        div()
        print("[1] Compliment")
        print("[2] Spend Time")
        print("[3] Conversation")
        print("[4] Insult")
        print("[5] Flirt")
        print("[6] Suck Up To")
        print("[7] Hook Up")
        print("[x] Befriend")
        print("[x] Ask out")
        div()
        try:
            ch = int(input(">"))
        except:
            adult()
        if ch == 1:
            print(f"You called your co-worker, {self.name},{choice(compliments)}.")
            if self.cool <= 0.25:
                self.rel -= 0.25
                print("Receptiveness:")
                pbar(0)
            else:
                self.rel += 0.25
                print("Receptiveness:")
                pbar(0.75)
            if self.prof <= 0.25:
                print(f"Your co-worker, {self.name}, called you {choice(compliments)}!")
            adult()
        elif ch == 2:
            if self.cool >= 0.75 and self.rel >= 0.5:
                print(f"You took your co-worker, {self.name}, {choice(spend_time)}.")
                self.rel += 0.25
            else:
                print(f"You tried to take your co-worker, {self.name}, {choice(spend_time)}, but were refused.")
                self.rel -= 0.25
            adult()
        elif ch == 3:
            if self.cool >= 0.15:
                print(f"You and your co-worker, {self.name}, had a debate about {choice(debates)}.")
                self.rel += 0.25
            else:
                print(f"Your co-worker, {self.name}, told you to get lost.")
                self.rel -=0.25
            adult()
        elif ch == 4:
            print(f"You called your co-worker, {self.name}, {choice(insults)}!")
            self.rel -= 0.45
            adult()
        elif ch == 5:
            if self.prof <= 0.5:
                print("You flirted with your co-worker.")
                self.rel += 0.25
                self.prof = 0
                self.friskiness += 0.5
            else:
                print("You tried flirting with your co-worker.")
                print(f"Your co-worker called you {choice(insults)}!")
                self.rel -= 0.25
                self.prof = 1
                self.friskiness = 0
            adult()
        elif ch == 6:
            print("You sucked up to your co-worker.")
            self.rel += 0.35
            self.prof += 0.35
            adult()
        elif ch == 7:
            if self.prof <= 0.35 and self.friskiness >= 0.5:
                if self.gender == 1 and gender == 0:
                    print("You hooked up with your co-worker.")
                    print(f"Your Enjoyment: {pbar2(rng(1,100))}")
                    print(f"Her Enjoyment: {pbar2(rng(1,100))}")
                    happiness += 0.5
                    self.friskiness, self.prof, self.cool = 1,0,1
                    adult()
                elif self.gender == 0 and gender == 1:
                    print("You hooked up with your co-worker.")
                    print(f"Your Enjoyment: {pbar2(rng(1,100))}")
                    print(f"His Enjoyment: {pbar2(rng(1,100))}")
                    happiness += 0.5
                    self.friskiness, self.prof, self.cool = 1,0,1
                    adult()
                else:
                    print("Your co-worker declined the opportunity.")
            else:
                print("You were reported to HR.")
                sleep(1)
                print("You were fired by HR.")
                job_id, salary, hours = 0,0,0
                adult()
        else:
            adult()
class PlasticSurgeon:
    def __init__(self):
        self.name = "NonePlasticSurgeon"
        self.age = 0
        self.end = 0
        self.rep = 0.5
        self.no = 0
        self.rep_cap = 0
        self.gender = 0
        self.price = 0
        self.is_facelift = 0
        self.is_liposuction = 0
        self.reassignment = 0
        self.botox = 0
        self.nose = 0
        self.open = 0
        self.eyelid = 0
        self.gender_specific = 0
        self.can_sue = 0
        self.fortune = 0
        self.years_served = 0
        self.rep_base = self.rep
    def debug(self):
        t = ""
        t += f"## Plastic Surgeon\n"
        t += f"Name: {self.name}\n"
        t += f"Age: {self.age}\n"
        t += f"Rep: {self.rep}\n"
        t += f"RepBase: {self.rep_base}\n"
        t += f"RepCap: {self.rep_cap}\n"
        if self.gender == 0:
            t += f"Gender: M\n"
        else:
            t += f"Gender: F\n"
        t += f"Price: {self.price}\n"
        t += f"Fortune: {self.fortune}\n"
        t += f"YearServed: {self.years_served}\n"
        t += f"CanSue: {self.can_sue}\n"
        t += f"OpenTreatment: {self.open}\n"
        t += f"Eyelid: {self.eyelid}\n"
        t += f"Botox: {self.botox}\n"
        t += f"GenderSpecific: {self.gender_specific}\n"
        t += f"Liposuction: {self.liposuction}\n"
        t += f"NoseJob: {self.nose}\n\n"   
        return t
    def age_up(self):
        global money, surgeons
        self.age += 1
        if self.end == self.age:
            print(f"{self.name}, your plastic suegeon, died.")
            surgeons.remove(self)
            br()
            return None
        money -= self.price
        self.is_facelift = 0
        self.is_liposuction = 0
        self.botox = 0
        self.nose = 0
        self.open = 0
        self.eyelid = 0
        self.gender_specific = 0
        self.fortune += self.price
        self.years_served += 1
    def bankrupt(self):
        print(f"Your plastic surgeon, {self.name}, has gone bankrupt.")
        print(f"You have sued them to oblivion, and they failed to pay up.")
        print(f"They were sent to prison for fraud.")
        global surgeons
        surgeons.remove(self)
        br()
        adult()
    def compile(self, no):
        self.age = rng(25,65)
        self.end = self.age + rng(10,35)
        self.gender = rng(0,1)
        if self.gender == 0:
            self.name = f"Dr {choice(forename_m)} {choice(surnames)}"
        else:
            self.name = f"Dr {choice(forename_f)} {choice(surnames)}"
        self.rep = rng (1,100) / 100
        self.rep_cap = self.rep + rng(25,75) / 100
        if self.rep_cap > 1:
            self.rep_cap = 1
        self.no = no
        self.price = int(self.rep * 1000000)
        self.fortune = self.price * 10
        self.rep_base = self.rep
    def successful(self):
        chance = rng(1,100) / 100
        if chance <= self.rep_base:
            return True
        else:
            return False
    def list(self, will_choose = 0):
        global allow_debug
        div()
        print(f"{self.name}")
        print(f"Age: {self.age}")
        print(f"Reputation:     {pbar2(self.rep)}")
        if allow_debug == 2:
            print(f"BaseRep:        {pbar2(self.rep_base)}")
        print(f"Max Reputation: {pbar2(self.rep_cap)}")
        print(f"Price: {currency}{'{:,}'.format(self.price)}/Yr.")
        if will_choose == 1:
            print(f"[{self.no}] Hire")
        else:
            print(f"[{self.no}] Interact")
    def rep_down(self):
        self.rep -= 0.35
    def rep_up(self):
        if self.rep_cap - self.rep >= 0.7:
            self.rep += 0.55
            self.rep_base += 0.55
        elif self.rep_cap - self.rep >= 0.5:
            self.rep += 0.45
            self.rep_base += 0.45
        elif self.rep_cap - self.rep >= 0.25:
            self.rep += 0.35
            self.rep_base += 0.35
        else:
            self.rep += 0.25
        if self.rep > self.rep_cap:
            self.rep = self.rep_cap
        if self.rep_base > self.rep_cap:
            self.rep_base = self.rep_cap
    def debug(self):
        print(self.name)
        print(self.age)
        print(self.rep)
        print(self.rep_base)
        print(self.rep_cap)
        
    def interact(self):
        if self.rep < 0:
            self.rep = 0
        if self.rep > 1:
            self.rep = 1
        global looks, gender, is_spouse, forename, surgeons
        div()
        print(f"{self.name}")
        print(f"Reputation:     {pbar2(self.rep)}")
        if allow_debug == 2:
            print(f"BaseRep:        {pbar2(self.rep_base)}")
        print(f"Max Reputation: {pbar2(self.rep_cap)}")
        print(f"Price: {currency}{'{:,}'.format(self.price)}")
        div()
        print("[1] Facelift")
        print("[2] Liposuction")
        if self.reassignment == 0:
            print("[3] Gender Reassignment")
        else:
            print("[ ] Gender Reassignment")
        print("[4] Eyelid Surgery")
        print("[5] Nose Job")
        print("[x] Botox")
        if gender == 0:
            print("[x] Penis Enlargement Surgery")
        else:
            print("[x] Breast Augmentation")
        div()
        print("[8] Fire")
        print("[x] Raise")
        div()
        try:
            ch = int(input(">"))
        except:
            adult()
        if ch == 1:
            print("You had a facelift done.")
            if self.successful() == True:
                self.rep_up()
                print("It was successful.")
                if self.is_facelift == 0:
                    looks += 0.25
            else:
                print("It was botched!")
                self.rep_down()
                looks -= 0.45
            self.is_facelift == 1
            adult()
        elif ch == 2:
            print("You had a liposuction.")
            if self.successful() == True:
                self.rep_up()
                print("It was successful!")
                if self.is_liposuction == 0:
                    looks += 0.25
            else:
                print("It was botched!")
                self.rep_down()
                looks -= 0.45
            self.is_liposuction = 1
            adult()
        elif ch == 3 and self.reassignment == 0:
            print("You had a gender reassignment.")
            if self.successful() == True:
                n = 0
                if gender == 0 and  n == 0:
                    gender = 1
                    forename = f"{choice(forename_f)}"
                    n = 1
                if gender == 1 and n == 0:
                    gender = 0
                    forename = f"{choice(forename_m)}"
                    n = 1
                del(n)
                self.rep_up()
                print("It was successful.")
                if is_spouse == 1:
                    print("Your spouse left you.")
                    is_spouse = 0
                self.reassignment = 1
                adult()
            else:
                print("It was botched!")
                self.rep = 0
                die(7)
        elif ch == 4:
            print("You had an eyelid surgery.")
            if self.successful() == True:
                self.rep_up()
                looks += 0.25
                print("It was successful.")
            else:
                looks -= 0.45
                print("It was botched!")
                self.rep_down()
            adult()
        elif ch == 5:
            print("You had a nose job.")
            if self.successful() == True:
                self.rep_up()
                looks += 0.35
                print("It was successful.")
            else:
                print("It was botched!")
                self.rep_down()
                looks -= 0.75
            adult()
        elif ch == 6:
            adult()
        elif ch == 7:
            adult()
        elif ch == 8:
            print(f"You fired {self.name}.")
            surgeons.remove(self)
        else:
            adult()
class Plane:
    def __init__(self):
        self.type, self.model = 0,0
        self.price = 0
        self.condition = 0.0
        self.is_ride = 0
        self.is_wash = 0
        self.vacation = 0
        self.is_maintenance = 0
    def compile(self, typee, model, price):
        self.type=typee
        self.model=model
        self.condition=1.0
        self.price = price
        self.value=self.price
    def list(self, is_buy, n):
        models = [
            ["Unknown Plane Model"],
            ["Unknown Plane Model","Boing 737","Boing 747","Airbuss A320","Airbuss A340"],
            ["Unknown Plane Model","Cessna 172 Skyhawk","Embracer Predator 520"],
            ["Unknown Plane Model","Gumman F-14 Tompatt"],
        ]
        div()
        if is_buy == 0:
            print(self.name)
        print(models[self.type][self.model])
        if is_buy == 0:
            print(pbar2(self.condition))
        else:
            print(f"{currency}{'{:,}'.format(self.price)}")
        if is_buy == 1:
            print(f"[{n}] Buy")
        elif is_buy == 2:
            pass
        else:
            print(f"[{n}] Interact")
    def name(self,name):
        self.name=name
    def age_up(self):
        self.age += 1
        self.condition *= 0.85
        self.value *= 0.85
    def interact(self):
        global happiness, money
        div()
        print(self.name)
        print(pbar2(self.condition))
        div()
        print("[1] Fly")
        print("[2] Vacation")
        print("[3] Wash")
        print("[4] Maintenance")
        print("[5] Sell")
        print("[6] Scrap")
        div()
        try:
            ch=int(input(">"))
        except:
            adult()
        if ch == 1:
            print("You flew your jet.")
            print("Enjoyment:")
            pbar(0.85)
            if self.is_ride == 0:
                happiness += 0.75
            self.is_ride = 1
            adult()
        elif ch == 2:
            print("You flew your jet on vacation.")
            print("Enjoyment:")
            pbar(0.85)
            if self.is_ride == 0:
                happiness += 0.75
            self.is_ride == 1
            adult()
        elif ch == 3:
            print("You washed your jet.")
            if self.wash == 0:
                self.condition += 0.05
            self.wash = 1
            adult()
        elif ch == 4:
            print("You had regular maintenance done on your jet.")
            if self.maintenance == 0:
                self.condition += 0.1
            self.maintenance = 1
            adult()
        elif ch == 5 or ch == 6:
            if ch == 5:
                print("You sold your jet.")
            else:
                print("You scrapped your jet.")
            if ch == 5:
                money += self.value
            vehicles[2].remove(self)
            adult()
        else:
            adult()
class Boat:
    def __init__(self):
        self.name="NoBoatName"
        self.age=0
        self.price=0
        self.condition = 1
        self.type=0
        self.value=self.price
        self.is_stolen=0
        self.is_wash = 0
        self.is_maintenance = 0
        self.is_broken = 0
    def compile(self, name, typee):
        self.name=name
        self.type=typee
        if self.type == 1:
            self.price = rng(100,200)
        elif self.type == 2:
            self.price == rng(10,45) * 1000
        elif self.type == 3:
            self.price=rng(45,556) * 1000000
        elif self.type == 4:
            self.price = rng(10,12) * 1000000
        elif self.type == 5:
            self.price = rng(5,10) * 1000
        else:
            self.price = rng(100,145) * 1000000000000
        self.value=self.price
    def list(self, no, is_bought=1):
        types = ["Unknown Boat Type","Raft","Speedboat","Yatch","Pirate Ship","Rowing Boat"]
        global currency
        if is_bought == 1:
            print(self.name)
        else:
            print(types[self.type])
        if is_bought == 1:
            print(f"Value: {currency}{'{:,}'.format(self.value)}")
        else:
            print(f"Price: {currency}{'{:,}'.format(self.price)}")
        if is_bought == 1:
            print(f"Type: {types[self.type]}")
            print(f"Condition: {pbar2(self.condition)} {self.condition * 100}%")
        if is_bought == 1:
            print(f"[{no}] Interact")
        else:
            print(f"[{no}] Purchase")
        div()
    def pick_name(self, name):
        choices=["HMS Organic","His Master's Boat","B O T E","RMS Magical","RMS OpenLivian","Ol' Besty","WinBoat3672"]
        self.name = name
        self.name.replace("|","")
        if self.name == "":
            self.name=choice(choices)
    def age_up(self):
        self.condition *= 0.7
        self.value *= 0.7
        self.is_wash = 0
        self.is_maintenance = 0
    def interact(self):
        global currency, happiness, money, vehicles
        if self.condition > 1:
            self.condition = 1
        types = ["Unknown Boat Type","Raft","Speedboat","Yatch","Pirate Ship","Rowing Boat"]
        div()
        print(self.name)
        print(f"Value: {currency}{self.value:,.0f}") # Special thanks to ChatGPT for fixing this
        print(f"Type: {types[self.type]}")
        print(f"Condition: {pbar2(self.condition)} {self.condition * 100}%")
        div()
        print("[1] Ride")
        print("[2] Sell")
        print("[3] Wash")
        print("[4] Maintenance")
        print("[x] Scrap")
        print("[x] Gift")
        div()
        try:
            ch=int(input(">"))
        except:
            self.interact()
        if ch == 1:
            print("You went out with your boat.")
            print(f"Enjoyment: {pbar2(1)}")
            if self.is_ride == 0:
                happiness += 0.5
                self.is_ride = 1
            self.interact()
        elif ch == 2:
            print(f"You sold your {types[self.type]} for {currency}{'{:,}'.format(self.value)}.")
            money += self.value
            vehicles[1].remove(self)
            adult()
        elif ch == 3:
            print("You washed your vehicle.")
            if self.is_wash == 0:
                self.condition += 0.1
                self.happiness += 0.25
                self.is_wash = 1
            self.interact()
        elif ch == 4:
            print("You had routine maintenance done for your boat.")
            if self.is_maintenance == 0:
                self.condition += 0.1
                self.is_maintenance = 1
            self.interact()
        elif ch == 5:
            print("You scrapped your boat.")
            vehicles[1].remove(self)
            adult()
        else:
            adult()
        
class Car:
    def __init__(self):
        self.name="NoCarName"
        self.age=0
        self.price=0
        self.condition=0.5
        self.type=0
        self.model="TestCar"
        self.value = self.price
        self.is_stolen = 0
        self.is_wash = 0
        self.is_maintenance = 0
        self.is_broken = 0
        self.is_stolen = 0
    def render_stolen(self, no):
        models = [["Unknown Car Model"],["Unknown Car Model","BWM Beetle","WV Chiron","Mini Smart","Smart Mini","OpenMotors Model 3000"],["Unknown Car Model","Chervolle Monte Carlo","Holder Accorda","Holder Civil","Handai Santa Fe","Merchant C-Class","Kai Sorrento"],["Unknown Car Model","Totoya GT99","Chervolle Corvette","Dodgem Challenger"],["Unknown Car Model","Mars Rover 3000","Fodr Mustang"],["Unknown Car Model","Nikola Model S","Nikola Model X","Nikola Model Y","Nikola Cybertruck","BWM Electric Beetle","OpenMotors Model 3500"],["Unknown Car Model","McLaid Senna","McLaid 4500","OpenMotors Exotic Mk. III","Fodr Xtra","Holder Xartra","OpenMotors Exotic Mk. II"],["Unknown Car Model","OpenMotors RubberScreecher Mk. VII","Ferry LVXI","Bourgeoise Lavish","Landbp Avegner","Doppelseig Motorworks Silver Claw Mk. 2"],["Unknown Car Model","F1 Mk. II","F1 Mk. II","F1 Mk. III","F1 Mk. IV"]]
        try:
            print(f"[{no}] {models[self.type][self.model]}")
        except:
            print(f"[{no}] Unknown Car Model")
        
    def compile(self, name, price, typee, model, is_stolen = 0):
        self.age = 0
        self.name = name
        self.price = price
        self.type = typee
        self.model = model
        self.condition = 1
        self.value = self.price
        self.is_stolen = is_stolen
    def recompile(self, name, age, price, condition, typee, model, value):
        self.age = age
        self.name = name
        self.price = price
        self.condition = condition
        self.type = typee
        self.model = models
        self.value = value
    def age_up(self):
        self.value = int(self.value * 0.8)
        self.condition *= 0.85
        self.is_wash, self.is_maintenance = 0,0
    def render(self,n):
        global currency
        div()
        models = [["Unknown Car Model"],["Unknown Car Model","BWM Beetle","WV Chiron","Mini Smart","Smart Mini","OpenMotors Model 3000"],["Unknown Car Model","Chervolle Monte Carlo","Holder Accorda","Holder Civil","Handai Santa Fe","Merchant C-Class","Kai Sorrento"],["Unknown Car Model","Totoya GT99","Chervolle Corvette","Dodgem Challenger"],["Unknown Car Model","Mars Rover 3000","Fodr Mustang"],["Unknown Car Model","Nikola Model S","Nikola Model X","Nikola Model Y","Nikola Cybertruck","BWM Electric Beetle","OpenMotors Model 3500"],["Unknown Car Model","McLaid Senna","McLaid 4500","OpenMotors Exotic Mk. III","Fodr Xtra","Holder Xartra","OpenMotors Exotic Mk. II"],["Unknown Car Model","OpenMotors RubberScreecher Mk. VII","Ferry LVXI","Bourgeoise Lavish","Landbp Avegner","Doppelseig Motorworks Silver Claw Mk. 2"],["Unknown Car Model","F1 Mk. II","F1 Mk. II","F1 Mk. III","F1 Mk. IV"]]
        try:
            print(f"{models[self.type][self.model]}")
        except:
            print("Unknown Car Model")
        types = ["Unknown","Standard","Coupe","SUV","EV","Exotic","Sports","F1"]
        print(f"Type: {types[self.type-1]}")
        print(f"Condition: {pbar2(self.condition)}")
        print(f"[{n}] Buy [{currency}{'{:,}'.format(self.price)}]")
    def list(self, n):
        global currency
        div()
        models = [["Unknown Car Model"],["Unknown Car Model","BWM Beetle","WV Chiron","Mini Smart","Smart Mini","OpenMotors Model 3000"],["Unknown Car Model","Chervolle Monte Carlo","Holder Accorda","Holder Civil","Handai Santa Fe","Merchant C-Class","Kai Sorrento"],["Unknown Car Model","Totoya GT99","Chervolle Corvette","Dodgem Challenger"],["Unknown Car Model","Mars Rover 3000","Fodr Mustang"],["Unknown Car Model","Nikola Model S","Nikola Model X","Nikola Model Y","Nikola Cybertruck","BWM Electric Beetle","OpenMotors Model 3500"],["Unknown Car Model","McLaid Senna","McLaid 4500","OpenMotors Exotic Mk. III","Fodr Xtra","Holder Xartra","OpenMotors Exotic Mk. II"],["Unknown Car Model","OpenMotors RubberScreecher Mk. VII","Ferry LVXI","Bourgeoise Lavish","Landbp Avegner","Doppelseig Motorworks Silver Claw Mk. 2"],["Unknown Car Model","F1 Mk. II","F1 Mk. II","F1 Mk. III","F1 Mk. IV"]]
        try:
            print(f"{models[self.type][self.model]}")
        except:
            print("Unknown Car Model")
        if self.is_stolen == 1:
            print("[STOLEN VEHICLE]")
        types = ["Unknown","Standard","Coupe","SUV","EV","Exotic","Sports","F1"]
        print(f"Type: {types[self.type-1]}")
        print(f"Condition: {pbar2(self.condition)}")
        print(f"Value: {currency}{'{:,}'.format(self.value)}")
        print(f"[{n}] Interact")
    def interact(self):
        global happiness, money, vehicles, currency
        models = [["Unknown Car Model"],["Unknown Car Model","BWM Beetle","WV Chiron","Mini Smart","Smart Mini","OpenMotors Model 3000"],["Unknown Car Model","Chervolle Monte Carlo","Holder Accorda","Holder Civil","Handai Santa Fe","Merchant C-Class","Kai Sorrento"],["Unknown Car Model","Totoya GT99","Chervolle Corvette","Dodgem Challenger"],["Unknown Car Model","Mars Rover 3000","Fodr Mustang"],["Unknown Car Model","Nikola Model S","Nikola Model X","Nikola Model Y","Nikola Cybertruck","BWM Electric Beetle","OpenMotors Model 3500"],["Unknown Car Model","McLaid Senna","McLaid 4500","OpenMotors Exotic Mk. III","Fodr Xtra","Holder Xartra","OpenMotors Exotic Mk. II"],["Unknown Car Model","OpenMotors RubberScreecher Mk. VII","Ferry LVXI","Bourgeoise Lavish","Landbp Avegner","Doppelseig Motorworks Silver Claw Mk. 2"],["Unknown Car Model","F1 Mk. II","F1 Mk. II","F1 Mk. III","F1 Mk. IV"]]
        try:
            print(f"{models[self.type][self.model]}")
        except:
            print("Unknown Car Model")
        types = ["Unknown","Standard","Coupe","SUV","EV","Exotic","Sports","F1"]
        print(f"Type: {types[self.type-1]}")
        print(f"Condition: {pbar2(self.condition)}")
        print(f"Value: {currency}{'{:,}'.format(self.value)}")
        div()
        print("[1] Ride")
        print("[2] Wash")
        print("[3] Maintanance")
        print("[4] Sell")
        print("[5] Scrap")
        print("[x] Gift")
        div()
        try:
            ch=int(input(">"))
        except:
            adult()
        if ch == 1 and self.is_broken == 0:
            print("You took your ride out for a ride.")
            print(f"Enjoyment: {pbar2(1)}")
            happiness += 0.55
        elif ch == 2:
            print(f"You went to the car wash and paid {currency}0.")
            if self.is_wash == 0:
                self.condition += 0.45
                self.is_wash = 1
                adult()
            else:
                adult()
        elif ch == 3:
            print("You performed yearly maintenance on your vehicle.")
            if self.is_maintenance == 0:
                self.condition += 0.25
                self.is_maintenance = 1
                adult()
            else:
                adult()
        elif ch == 4 or ch == 5:
            if ch == 4:
                print(f"You sold your car for {currency}{'{:,}'.format(self.value)}")
            else:
                print("You scrapped your car.")
            if ch == 4:
                money += self.value
            vehicles[0].remove(self)
        else:
            adult()
class Anticheat:
    # Source: https://stackoverflow.com/questions/842557/how-to-prevent-a-block-of-code-from-being-interrupted-by-keyboardinterrupt-in-py [Top Answer]

    def __enter__(self):
        self.signal_received = False
        self.old_handler = signal.signal(signal.SIGINT, self.handler)
                
    def handler(self, sig, frame):
        self.signal_received = (sig, frame)
        logging.debug('SIGINT received. Delaying KeyboardInterrupt.')
    
    def __exit__(self, type, value, traceback):
        signal.signal(signal.SIGINT, self.old_handler)
        if self.signal_received:
            self.old_handler(*self.signal_received)
class House:
    def __init__(self):
        self.price=0
        self.value=0
        self.condition=1.0
        self.haunted=0
        self.age=0
    def compile(self, price, haunted, model):
        self.price=price
        self.value=price
        self.model = model
        self.haunted=haunted
    def list(self,n,buy):
        div()
        if self.model == 1:
            print("Manor")
        elif self.model == 2:
            print("Villa")
        elif self.model== 3:
            print("Castle")
        elif self.model == 4:
            print("Equestrian Property")
        else:
            print("Duplex")
        if self.haunted == 1:
            print("Haunted")
        if buy == 0:
            print(f"Condition:",pbar2(self.condition),f"{int(self.condition * 100)}%")
            print(f"Value: {currency}{'{:,}'.format(self.value)}")
        else:
            print(f"Price: {currency}{'{:,}'.format(self.price)}")
        if buy == 1:
            print(f"[{n}] Buy [{currency}{self.price}]")
        else:
            print(f"[{n}] Interact")
    def age_up(self):
        self.value = int(self.value * 1.2)
        self.age += 1
        self.condition *= 0.85
    def interact(self):
        global money, debt, houses
        print(f"Value: {currency}{'{:,}'.format(self.value)}")
        print(f"Condition: {pbar2(self.condition)} {int(self.condition * 100)}%")
        div()
        print("[1] Sell")
        print("[x] Renovate")
        print("[x] Gift")
        if debt > 0:
            print("[x] Pay Debts With")
        if self.haunted == 1:
            print("[5] Exorcise")
        print("[0] Return")
        div()
        try:
            ch=int(input(">"))
        except:
            adult()
        if ch == 1:
            money += self.value
            houses.remove(self)
            print("You sold your house for {currency}{'{:,}'.format(self.value)}.")
            adult()
        elif ch == 5 and self.haunted == 1:
            if job_id == 4:
                print(f"[1] Do it yourself [{currency}0]")
            print("[0] Return")
            try:
                ch=int(input(">"))
            except:
                adult()
            if ch == 1 and job_id == 4:
                self.haunted = 0
                self.value *= 2
                print("Success!")
                adult()
            else:
                adult()
        else:
            adult()
class FriendRecompile:
    # This class is used by load_game() to take raw save data and rebuild it as a proper friend object
    # The normal Friend class cannot be used as it randomises stats
    def __init__(self, name, age, gender, intel, looks, craziness, end, rel):
        self.name = name
        self.age = age
        self.gender = gender
        self.intel = intel
        self.looks = looks
        self.craziness = craziness
        self.end = end
        self.rel = rel


class Friend:
    def __init__(self):
        self.name = "NOFRIENDNAME"
        self.age = 0
        self.gender = 0

        self.intel = 0.0
        self.looks = 0.0
        self.craziness = 0.0

        self.end = 0
        self.rel = 0
    def generate(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

        self.intel = rng(1, 100) / 100
        self.looks = rng(1, 100) / 100
        self.craziness = rng(1, 100) / 100

        self.end = self.age + rng(25, 55)
        self.rel = rng(50, 75) / 100
    def recompile(self, name, age, gender, intel, looks, craziness, end, rel):
        self.name = name
        self.age = age
        self.gender = gender
        self.intel = intel
        self.looks = looks
        self.craziness = craziness
        self.end = end
        self.rel = rel
class Child:
    def __init__(self, no = 1):
        self.name = "NoneValue"
        self.age = 0
        self.rel = 0
        self.end = 0
        self.gender = 0
        self.intel = 0.01
        self.looks = 0.01
        self.craziness = 0.01
        self.no = no
        self.adopted = 0
    def generate_random(self, age = 0, share_surname = 1):
        global surname, children
        self.gender = rng(0,1)
        self.age = age
        if self.gender == 1:
            if share_surname == 1:
                self.name = f"{choice(forename_f)} {surname}"
            else:
                self.name = f"{choice(forename_f)} {choice(surnames)}"
        else:
            if share_surname == 1:
                self.name = f"{choice(forename_m)} {surname}"
            else:
                self.name = f"{choice(forename_m)} {choice(surnames)}"
        self.rel = 1
        self.end = rng(35,85)
        self.intel, self.looks, self.craziness = rng(0,100)/100,rng(0,100)/100,rng(0,100)/100
        self.no = len(children) + 1
        self.price = rng(500,2500)
    def recompile(self, namee, age, rel, end, gender, intel, looks, craziness, no):
        self.name = namee
        self.age = age
        self.rel = rel
        self.end = end
        self.gender = gender
        self.intel = intel
        self.looks = looks
        self.craziness = craziness
        self.no = no
    def render(self, n):
        print(self.name)
        print(f"Age {self.age}")
        if self.gender == 0:
            print("Male")
        elif self.gender == 1:
            print("Female")
        else:
            print("Non-Binary")
        print("Looks:       ",pbar2(self.looks))
        print("Craziness:   ",pbar2(self.craziness))
        print("Intelligence:",pbar2(self.intel))
        div()
        print(f"[{n}] Choose [{currency}{'{:,}'.format(self.price)}]")
        return None
    def interact(self):
        global child_1, child_2, child_3, child_4, child_5, child_6, child_7, child_8, chilld_count
        print(self.name)
        div()
        print("[1] Spend Time With")
        print("[2] Compliment")
        print("[3] Conversation")
        print("[4] Adopt Out")
        print("[5] Abandon")
        print("[6] Insult")
        div()
        try:
            ch = int(input(">"))
        except:
            return None
        if ch == 1:
            print(f"You took your child {choice(spend_time)}.")
            self.rel += 0.25
            if self.rel > 1:
                self.rel = 1
            self.interact()
        elif ch == 2:
            print(f"You called your child {choice(compliments)}")
            self.rel += 0.25
            if self.rel > 1:
                self.rel = 1
            self.interact()
        elif ch == 3:
            print(f"You and your child had a conversation bout {choice(debates)}.")
        elif ch == 4 or ch == 5:
            if ch == 5:
                print(f"You abandoned your child, {self.name}.")
            else:
                print(f"You put your child, {self.name}, out for adoption.")
            global children
            children.remove(self)
            if is_spouse == 1:
                spouse.rel -= 0.75
            return None
        else:
            return None
    def list(self):
        if self.end > self.age:
            print(self.name)
            print(f"[{self.no}] Child #{self.no} [Age {self.age}]")
            print(pbar2(self.rel))
            div()
    def age_up(self):
        self.age += 1
    def show_child(self):
        div()
        print(self.name)
        print(f"Smarts:    {pbar2(self.intel)}")
        print(f"Looks:     {pbar2(self.looks)}")
        print(f"Craziness: {pbar2(self.craziness)}")
class Parent:
    def __init__(self):
        # Calling Parent returns an empty Parent object.
        self.name = "N"
        self.age = 0
        self.end = 0
        self.rel = 0
        self.gender = 0
    def generate(self, gender, rel):
        # Used in life creator.
        global surnames, age
        self.gender = gender
        if self.gender == 1:
            self.name = f"{choice(forename_f)} {surname}"
        else:
            self.name = f"{choice(forename_m)} {surname}"
        if self.gender == 1:
            self.age = age + 32
        else:
            self.age = age + 37
        self.end = self.age + rng(15,55)
        self.rel = rel
    def recompile(self, name, age, gender, end, rel):
        self.name = name
        self.age = age
        self.gender = gender
        self.end = end
        self.rel = rel
    def adjust(self,rel):
        self.rel = rel


class Sibling:
    def __init__(self, name, age, rel):
        self.name = "N"
        self.age = 0
        self.end = 0
        self.rel = 0.0
        self.gender = 0
    def generate(self, gender, rel):
        global age, surname
        self.gender = gender
        self.age = rng(-5,5) + age
        if self.gender == 0:
            self.name = f"{choice(forename_m)} {surname}"
        else:
            self.name = f"{choice(forename_f)} {surname}"
        self.rel = rels
        self.end = self.age + rng(25,65)
    def rebuild(self, name, age, end, gender, rel):
        self.name = name
        self.age = age
        self.end = end
        self.gender = gender
        self.rel = rel
class Spouse:
    def __init__(self):
        # This class is used for creating a spouse.
        # It includes all necessary data.
        # The `your age` parameter refers to the player character's age
        self.name = "N/A"
        self.age = 0
        self.end = 0
        self.rel = 0
        self.gender = 0
        self.lvl = 0
        self.intel = 0
        self.looks = 0
        self.craziness = 0
        self.fortune = 0
        self.pregnant = 0
    def compile(self, name, relation, relationship_level, gender):
        global age
        self.name = name
        self.age = age + rng(-5, 5)
        if self.age < 19:
            self.age = 19
        self.end = self.age + rng(
            10, 35
        )  # This means you will [almost] always outlive your spouse.
        self.rel = relation
        self.gender = gender

        # Level 1 = Girlfriend/Boyfriend
        # Level 2 = Married
        self.lvl = relationship_level

        self.intel = (rng(1, 100)) / 100
        self.looks = (rng(1, 100)) / 100
        self.craziness = (rng(1, 100)) / 100
        self.fortune = rng(0, 10000000)
        self.pregnant = 0
    def die(self):
        pass
    def age_up(self):
        self.age += 1
        if self.age == self.end:
            self.die()
class SpouseDatingApp:
    def __init__(self, name, relation, relationship_level, your_age, gender, age):
        # This class is used for creating a spouse.
        # It includes all necessary data.
        # The `your age` parameter refers to the player character's age
        self.name = name
        self.age = age
        if self.age < 19:
            self.age = 19
        self.end = self.age + rng(10, 35)
        if self.end > 123:
            self.end = 123
        self.rel = relation
        self.gender = gender

        # Level 1 = Girlfriend/Boyfriend
        # Level 2 = Married
        self.lvl = relationship_level

        self.intel = (rng(1, 100)) / 100
        self.looks = (rng(1, 100)) / 100
        self.craziness = (rng(1, 100)) / 100
        self.fortune = rng(0, 10000000)


class Parent:
    def __init__(self, name, gender, end_age, relations, char_age):
        self.gender = gender
        if self.gender == 1:
            self.age = char_age + 32
        else:
            self.age = char_age + 37
        self.name = name
        self.end_age = rng(50, 85)
        self.relations = 0.75


class ExitError(Exception):
    # This one is used to nuke the game by deleting all variables.
    # I had to put everything into an except statement because
    # it would raise 3 errors and not delete anything.
    pass


class reboot(Exception):
    # type raise reboot to reboot the game!
    def __init__(self):
        mainmenu()


class GeneralException(Exception):
    pass


class FeatureNotInGameError(Exception):
    pass


class LifeCreatorError(Exception):
    # used for when an error occurs in the life creation process
    def __init__(self):
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("LifeCreatorError")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("The LifeCreator experienced an error and has exit the program.")
        print("The game will restart.")
        input("Press ENTER to continue.")
        mainmenu()


openlife_dir = "openlife_saves"
try:
    os.chdir(openlife_dir)
except:
    os.mkdir(openlife_dir)
    os.chdir(openlife_dir)
try:
    global has_first_run
    has_first_run = 0

    def first_run():
        global has_first_run, instant_life
        # Configurable data
        # used by me [and potentially you!] to configure how the game works
        # I am putting it at the top for quick and easy access
        # No more CTRL+F :>

        # Debug options
        global allow_debug, allow_test, auto_pay_lab
        # Some debug commands are hidden behind this flag, and ExitError spits out a load of debug info upon exiting
        # Test mode currently adds an experimental Clear Screen function.
        allow_debug = 1
        allow_test = 0

        # 0=Original UI style [Looks kinda bad when you compare it to the others]
        # 1=Experimental UI style [with squares] [Never used] [Ugly]
        # 2=New UI Style [Looks great in cmd]
        # 3= "Throwback Mode" [a tribute to the original theme]

        # It is set to `3` by default

        global alt_ui
        alt_ui = 3

        global alt_logo, game_name, version
        # 0= Original logo [Alphas 1-10]
        # 1= Current logo
        # 2= "Throwback Mode" logo

        # It is set to `2` by default
        alt_logo = 2

        # Set to 1 to instantly create a quick life on first launch
        # Useful development feature
        instant_life = 0

        # End of configurable data
        has_first_run = 1

        auto_pay_lab = 0
    def generate_co_workers():
        global coworkers
        coworkers = []
        # Generate Supervisor
        supervisor = CoWorker()
        supervisor.compile(rng(0,1),3)
        coworkers.append(supervisor)
        # Generate HR
        for i in range(rng(3,5)):
            test = CoWorker()
            test.compile(rng(0,1),2)
            coworkers.append(test)
        # Generate Standard Co-Workers
        for i in range(rng(8,20)):
            test = CoWorker()
            test.compile(rng(0,1))
            coworkers.append(test)
    def game_init():
        
        global has_first_run
        global spouse, houses
        spouse = Spouse()
        houses = []
        if has_first_run == 0:
            first_run()
        # Semi-Configurable Data
        global game_name, version
        game_name = "OpenLife"
        version = "Alpha 17.4 [04 Jan 2023]"

        global app_version, sub_version
        app_version = [0, 0, 17]
        sub_version = 3

        # Set this to 0 to hide the loaded forenames message
        verbose_message = 0

        global flip_profits
        flip_profits = 0

        global driver_license, boat_license, gun_license, pilot_license
        driver_license, boat_license, gun_license, pilot_license = 0, 0, 0, 0

        # Non-configurable data
        global yearly_videos, is_common_cold, is_cancer
        yearly_videos, is_common_cold, is_cancer = 0, 0, 0
        global lottery_wins, is_bandit, book_base, house_count
        lottery_wins, is_bandit, house_count = 0, 0, 0
        book_base = 0  # Decreases every year. Incremented by 3 when you publish a book. Can only publish a book if this value = 0
        global fame, is_wpp, friend_count, is_opentube
        fame = 0
        is_wpp = 0
        is_opentube = 0
        friend_count = 0

        global vehicles, surgeons, coworkers
        vehicles = [[],[],[]] # Index 0 is cars, index 1 is boats, index 2 is planes.
        surgeons = []
        coworkers= []
        
        global degrees
        degrees = ["None","Finance","Journalism","Computer Science","Education","Accounting","Political Science","Nursing","Psychology","Engineering","Art History","Communications","Graphic Design","Data Science","Criminal Justice","Linguistics","Marketing","Anthropology","Biology","Chemistry","Physics","English","Mathematics","History","Information Systems","Music","Economics","Dance","Electrical Engineering","Religious Studies","Dentistry","Law"]
        global country
        country = [
            "OpenLife",
            "United Kingdom",
            "United States of America",
            "China",
            "France",
            "Germany",
            "Poland",
            "Turkey",
            "India",
            "Sweden",
            "Norway",
            "Denmark",
            "UAE",
            "Spain",
        ]

        global is_smartphone, pistol_ammo, chainsaw_count, taser_count
        is_smartphone, pistol_ammo, chainsaw_count, taser_count = 0, 0, 0, 0

        global research_lab, pending_research
        research_lab = [0,0,0,0,0] # [Unlocked lab, unlocked age-down, unlocked cure for cancer, unlocked immortality, unlocked stress resistance]
        pending_research = [0,0] # [Years left, research ID pending]

        global is_fertile
        is_fertile = 1
        global juvie_years, prison_years, sentence
        juvie_years = 0
        prison_years = 0
        sentence = 0
        global is_appeal, behaviour
        is_appeal = 0
        behaviour = 1.5  # If it's 1.5, you have never been to prison :)
        global is_trans
        is_trans = 0
        global is_hbp
        is_hbp = 0  # When you have 75%+ stress, you have a 50% chance of getting high blood pressure.
        global currency
        currency = "£"  # this works across the entire platform
        global child_count
        child_count = 0
        global work_e, work_e_base, promo_base
        work_e = 0  # work experience
        promo_base = 0
        work_e_base = 0  # resets each time you quit your job & is a hidden value
        promo_base = 0
        global is_spouse
        is_spouse = 0
        global part_time_salary, teen_salary, teen_hours
        part_time_salary = 0
        teen_salary = 0
        teen_hours = 0
        global pistol_count, knife_count
        pistol_count, knife_count = 0, 0
        global forename_m, forename_f, surnames, gang_names, compliments, insults, debates, spend_time, job_roles, birthdays
        global auto_deposit
        auto_deposit = 0  # Set to 1 to automatically send all your money to savings account every year
        # Taken from https://github.com/MustafaKermitsSuicide/BitLife
        forename_m = [
            "Oliver",
            "Jacob",
            "Mason",
            "Harry",
            "William",
            "Alfie",
            "Jayden",
            "Charlie",
            "Noah",
            "Thomas",
            "Michael",
            "Ethan",
            "Joshua",
            "Alexander",
            "George",
            "Aiden",
            "James",
            "Daniel",
            "Jack",
            "Bruno",
            "Donald",
            "Nick",
            "Harvey",
            "Alfie",
            "Archie",
            "Ollie",
            "Louie",
            "Jenson",
            "Lewis",
            "Louis",
            "Callum",
            "Freddie",
            "Theo",
            "Toby",
            "Harley",
            "Reuben",
            "Kian",
            "Bobby",
            "Stanley",
        ]
        forename_f = [
            "Olivia",
            "Sophie",
            "Isabella",
            "Emily",
            "Emma",
            "Lily",
            "Amelia",
            "Ava",
            "Jessica",
            "Ruby",
            "Abigail",
            "Chloe",
            "Madison",
            "Grace",
            "Mia",
            "Evie",
            "Laura",
            "Maisie",
            "Poppy",
            "Freya",
            "Imogen",
            "Florence",
            "Rosie",
            "Hollie",
            "Isobel",
            "Niamh",
            "Harriet",
            "Tilly",
            "Maisy",
            "Holly",
            "Matilda",
            "Amelie",
            "Esme",
            "Zara",
            "Tia",
            "Aimee",
            "Martha",
            "Libby",
        ]
        surnames = [
            "Smith",
            "Johnson",
            "Williams",
            "Jones",
            "Brown",
            "Davis",
            "Miller",
            "Wilson",
            "Moore",
            "Taylor",
            "Anderson",
            "Thomas",
            "Jackson",
            "White",
            "Harris",
            "Martin",
            "Thompson",
            "Garcia",
            "Martinez",
            "Robinson",
            "Clark",
            "Rodriguez",
            "Lewis",
            "Lee",
            "Walker",
            "Hall",
            "Allen",
            "Young",
            "Hernandez",
            "King",
            "Wright",
            "Lopez",
            "Hill",
            "Scott",
            "Green",
            "Adams",
            "Baker",
            "Gonzalez",
            "Nelson",
            "Carter",
            "Mitchell",
            "Perez",
            "Roberts",
            "Turner",
            "Phillips",
            "Campbell",
            "Parker",
            "Evans",
            "Edwards",
            "Collins",
            "Stewart",
            "Sanchez",
            "Morris",
            "Rogers",
            "Reed",
            "Cook",
            "Morgan",
            "Bell",
            "Murphy",
            "Bailey",
            "Rivera",
            "Cooper",
            "Richardson",
            "Cox",
            "Howard",
            "Ward",
            "Torres",
            "Peterson",
            "Gray",
            "Ramirez",
            "James",
            "Watson",
            "Brooks",
            "Kelly",
            "Sanders",
            "Price",
            "Bennett",
            "Wood",
            "Barnes",
            "Ross",
            "Henderson",
            "Coleman",
            "Jenkins",
            "Perry",
            "Powell",
            "Log",
            "Patterson",
            "Hughes",
            "Flores",
            "Washington",
            "Butler",
            "Simmons",
            "Foster",
            "Gonzales",
            "Bryant",
            "Alexander",
            "Russell",
            "Griffin",
            "Diaz",
            "Hayes",
        ]
        # The compliments were taken from fungamer2's Life-Simulator1 and edited to make it compatible with OpenLife.
        compliments = [
            "a boss",
            "a bubbly personality",
            "a brilliant mind",
            "a champion",
            "a gem",
            "a genius",
            "a jewel",
            "a legend",
            "a player",
            "a revolutionary",
            "a smart cookie",
            "a treasure",
            "a winner",
            "a wizard",
            "a VIP",
            "a visionary",
            "adorable",
            "admirable",
            "an OG",
            "an eager beaver",
            "brave",
            "bright",
            "brilliant",
            "charming",
            "clever",
            "cool",
            "courageous",
            "cute",
            "dashing",
            "delightful",
            "dope",
            "elite",
            "fascinating",
            "fearless",
            "fine",
            "fresh",
            "gorgeous",
            "golden",
            "groovy",
            "inspiring",
            "intelligent",
            "legendary",
            "lionhearted",
            "magnetic",
            "magnificent",
            "motivating",
            "neat",
            "nifty",
            "one-of-a-kind",
            "a perfect 10",
            "phenomenal",
            "rad",
            "savage",
            "smart",
            "spectatular",
            "stellar",
            "strong",
            "stunning",
            "stylish",
            "swell",
            "the best",
            "the GOAT",
            "the greatest",
            "the life of the party",
            "unparalled",
            "wise",
            "wonderful",
        ]

        # The insults were taken from fungamer2's Life-Simulator1 and edited to make it compatible with OpenLife.
        insults = [
            "a dimwit",
            "a dork",
            "a douchebag",
            "a dummy",
            "a dunce",
            "a fatty",
            "a freak",
            "a goblin",
            "a jerk",
            "a jumpoff",
            "a lamebrain",
            "a loser",
            "a maniac",
            "a mouth-breather",
            "a pig",
            "a pumpkinhead",
            "a punk",
            "a scallywag",
            "a simpleton",
            "a snake",
            "a tool",
            "a tramp",
            "a triple-chin",
            "a twat",
            "a twit",
            "a villain",
            "a vulture",
            "a weasel",
            "an abomination to mankind",
            "an airhead",
            "an idiot",
            "an imbecile",
            "awful",
            "brainless",
            "careless",
            "dumb",
            "evil",
            "foolhardy",
            "mediocre at best",
            "mentally defective",
            "nasty",
            "obtuse",
            "psycho",
            "putrid",
            "skeezy",
            "stupid",
            "trashy",
            "weak",
            "weaksauce",
            "a dickhead",
            "a dickhead",
            "a dickhead",
            "a dickhead",
            "a dickhead",
            "a dickhead",
        ]
        debates = [
            "why cats are better than dogs",
            "why dogs are better than cats",
            "the Russia-Ukraine War",
            "High Fuel Prices",
            "the Metaverse",
            "the Economic crisis of Sri Lanka",
            "Moonlighting",
            "the Pros and Cons of working from home",
            "whether people should invest in cryptocurrency",
            "the Biomedical waste crisis",
            "the impact of 5G on the global economy",
            "how to prevent the next pandemic",
            "the impact of COVID-19 on the global economy",
            "the pros and cons of block chain technology",
            "the role of social media in international politics",
            "how to end the threat of nuclear war",
            "the impact of COVID-19 on the education sector",
            "Taliban rule in Afghanistan",
            "the rise of the gig economy",
            "the harms of passive smoking",
            "the advantages and disadvantages of having a credit card",
            "whether software should be free for everyone",
            "whether gambling should be allowed from the age of 16",
            "problems caused by the economic boycott in Cuba",
            "how international trade barriers work",
            "how the United Nations is based on diplomacy and strengthening relationships",
            "whether or not public schools are safe enough",
            "whether it is necessary to hold value in what you argue",
            "why drink driving is dangerous",
            "how India became such a large milk producer",
            "how to make money with recycling",
            "the decreasing productivity of the Japanese workforce",
            "a business model to help health-conscious customers",
            "what the best technologies are to safeguard the right of free speech on the internet",
            "what the best technologies are to safeguard the right of privacy on the internet",
            "how to check for the signs of burnout",
            "how to overcome the coal crisis in India",
            "the causes of bullying in schools",
            "why we should have a minimum wage",
            "whether universal basic income is a good idea",
            "the leadership changes needed in our country",
            "whether empowering women is the solution to violence against women",
            "the effects of communalism on social cohesion",
            "whether we're becoming too sensitive in society",
            "lessons for the world from the COVID-19 pandemic",
            "whether crime rates increase because of unemployment",
            "causes of poverty around the world",
            "the effects of the Internet of Things on our lives",
            "whether drug abuse is rampant among teenagers",
            "whether anemia effects urban society",
            "gender equality in the workplace",
            "whether the wealthy should be taxed more",
            "whether the poor should be given more assistance",
            "whether it is possible to maintain a work-life balance",
            "whether saying 'women make good managers' is sexist like saying 'asians are good at maths' is racist",
            "whether job creators are needed more than job seekers",
            "whether a borderless world is a myth or a reality",
            "what would happen if Bitcoin crashed to zero and whether it is possible",
            "business ethics in today's market compared with the past and the potential future",
            "whether patience is important in business and management",
            "whether the family-run business is relevant in today's market",
            "whether E-commerce discounts are harmful in the long run and is it the business or customer being harmed",
            "whether globalisation is an opportunity or a threat",
            "how markets are found and not created",
            "whether the world is ready for a cashless society",
            "whether physical infrastructure is the answer to social equality",
            "whether the public sector being a guarantor of job security is a myth",
            "whether a circular economy is key to sustainable development",
            "the contribution of the Indian IT industry to the US and global economy",
            "whether democracy is a hindrance to economic reforms in India",
            "the technology behind Zero Budget Natural Farming",
            "the effects of technological change on jobs",
            "whether pervasive technology is creating a generation of cyber zombies",
            "whether the IT industry will create more or less jobs in the future",
            "whether artificial intelligence can replace human intelligence",
            "the effects of big data on information privacy",
            "whether automation will create more or less jobs",
            "the benefits and challenges of data localisation",
            "whether artifical intelligence will change the future",
            "how technology can be used to tackle financial crimes",
            "whether polythene bags should be completely banned",
            "how to control air pollution levels",
            "whether green jobs are essential for sustainable development",
            "how to manage natural disasters",
            "how to manage financial disasters",
            "methods of disaster recovery",
            "the effects of Coronaviruses on the environment",
            "whether smart farming is the future of agriculture",
            "whether genetic engineering in agriculture is good or bad",
            "the effects of climate on the farming system and food supply",
            "whether automation in farming is good",
            "whether collective farming is a boon or a bane",
            "our views on natural versus factory farming",
            "our views on conventional farming and organic farming",
            "the role of women in agriculture",
            "whether agroforestry destroys the environment",
            "gay marriage and your views on it",
            "whether war is the best option to solve international disputes",
            "whether primary school children should be allowed to own mobile phones",
            "whether using animals for medical research should be allowed",
            "whether men and women will ever be equal, if they already are, and whether equality will last",
            "whether you can have a happy family life and a successful career at the same time",
            "whether marriage is an outdated institution",
            "whether citizens should be allowed to carry guns and other weapons",
            "whether the death penalty is acceptable for any reasons",
            "whether non-citizens and tourists should be allowed to vote in their country of residence",
            "whether sex education should be taught to children under 12",
            "whether or not women are paid the same as men",
            "whether bribery and corruption is acceptable in government",
            "whether bribery and corruption is acceptable in private business",
            "whether music that glorifies violence should be banned",
            "whether condoms should be distributed for free in primary schools",
            "whether nuclear weapons are necessary weapons",
            "whether teachers should be allowed to carry guns",
            "whether professional sports people earn too much money",
            "our views on whether or not beauty contests should be banned",
            "our views on whether or not cosmetic surgery should be outlawed",
            "our views on whether or not abortions are okay",
            "our views on whether or not social deprivation causes crime",
            "our views on whether or not military service should be compulsory",
            "our views on whether or not war is ever an option for solving international disputes",
            "our views on whether or not torture can be acceptable in some cases",
            "our views on whether or not curfews keep teens out of trouble",
            "our views on whether or not we're becoming too dependent on computers",
            "our views on whether or not smoking should be banned worldwide",
            "our views on whether or not it should be illegal to ride a bicycle without a helmet",
            "our views on whether or not single sex schools are bad for childhood development and lead to unhealthy views of the opposite sex",
            "our views on whether or not homework is harmful",
            "our views on whether or not the United Nations is a failed organisation",
            "our views on whether or not intelligence tests should be given before couples can have children",
            "our views on whether or not a woman's place is in the home",
            "our views on whether or not it's a man's world",
            "our views on whether or not money makes you happy",
            "our views on whether or not money can buy you happiness",
            "our views on whether or not the internet must be censored to protect society",
            "our views on whether or not genetically modified foods have no ill health effects",
            "our views on whether a man should have a wife for the family and a paramour for pleasure",
            "our views on whether a woman should have a husband for the family and a paramour for pleasure",
            "our views on whether soft drugs should be legalised",
            "our views on whether or not electric cars help the environment",
            "our views on whether or not staying unmarried leads to a happier life",
            "our views on whether or not software piracy is a real crime",
            "our views on whether or not religion is needed",
            "our views on whether veganism is the key to solving climate change",
            "our views on whether the police force is institutionally racist",
            "our views on whether democracy must be imposed on nations",
            "our views on whether the war in Iraq was justified",
            "our views on whether your race affects your intelligence",
            "our views on whether your race affects your sporting ability",
            "our views on whether the world is over populated and steps must be taken to reduce births",
            "whether or not euthanasia should be illegal",
            "whether or not cloning is a valuable scientific pursuit",
            "whether obesity is a disease and not a lifestyle choice",
            "whether or not video games contribute to youth violence",
            "whether the drinking age should be lowered",
            "whether the drinking age should be raised",
            "whether the smoking age should be lowered",
            "whether the smoking age should be raised",
            "whether the age of consent should be lowered",
            "whether the age of consent should be raised",
            "whether the voting age should be lowered",
            "whether the voting age should be raised",
            "whether the driving age should be lowered",
            "whether the driving age should be raised",
            "whether the gambling age should be lowered",
            "whether the gambling age should be raised",
            "whether the military service age should be lowered",
            "whether the military service age should be raised",
            "whether drugs should be accepted in sports",
            "whether self driving cars are going to make our lives easier",
            "whether climate change exists",
            "whether carbohydrates are more damaging than fats",
            "whether terrorism can be justifed",
            "whether or not street prostitution should be illegal",
            "whether or not prostitution in a brothel should be illegal",
            "whether or not prostituting yourself in your own home should be illegal",
            "whether prisoners should be allowed to vote",
            "whether prenuptual agreements make families stronger",
        ]
        spend_time = [
            "to practice sumo wrestling",
            "to play in the rain",
            "to toilet paper the neighbour's house",
            "to scare random people by jumping out of the bushes at a local park",
            "to make a wish while throwing a coing in a fountain",
            "to watch toy unboxing videos",
            "to a café to play cards",
            "to watch a movie under the stars in the park",
            "to perform in a flash mob at the grocery store",
            "to fly a kite",
            "to a rugby game",
            "to the circus",
            "longboarding",
            "to a Hindu temple",
            "to build a sandcastle in a sandbox at the park",
            "to an escape room",
            "antiquing",
            "to write haikus",
            "to play in the sprinklers at the local park",
            "to play bingo at the community centre",
            "to an arcade",
            "to throw paper aeroplanes off the bleachers at the local high school",
            "to the water park",
            "to the aquarium to look at sharks",
            "to sing P!nk songs at karaoke night",
            "to the movies",
            "axe throwing",
            "to make home made mini pizzas",
            "to a painting class",
            "to have a random dance party in a public plaza",
            "to plant trees in the forest",
            "whale watching",
            "to make and pass out balloon animals at the park",
            "snowboarding",
            "to the park",
            "to graffiti train cars",
            "to learn origami at the community centre",
            "birdwatching",
            "to the shooting range",
            "to do caricature drawings of random people in a public place",
            "yodelling",
            "deep sea fishing",
            "to a carnival",
            "to ding dong ditch the neighbours",
            "to parkour hardcore",
            "to watch a random trial at the municipal court",
            "to a rugby game",
            "to make selfies for Instagram",
            "to the museum",
            "to walk along a scenic vista",
            "to watch toy unboxing videos",
            "to fly a drone",
            "to make a safety evacuation map",
            "horseback riding in the countryside",
            "to dinner",
            "to a puppet-making seminar",
        ]
        job_roles = [
            "Exorcist",
            "Pilot",
            "Lawyer",
            "Monk",
            "Wedding Planner",
            "Soldier",
            "Architect",
            "Cashier",
            "Oohber Driver",
            "Flight Attendant",
            "Hairdresser",
            "Judge",
            "Librarian",
            "Librarian",
            "Nun",
            "Photographer",
            "Translator",
            "Accountant",
            "Teacher",
            "Game Developer",
            "Banker",
            "App Developer",
            "Engineer",
            "College Lecturer",
            "Editor",
            "Exotic Dancer",
            "Stockbroker",
            "P*rnographer",
        ]
        birthdays = [
            "January 1",
            "January 2",
            "January 3",
            "January 4",
            "January 5",
            "January 6",
            "January 7",
            "January 8",
            "January 9",
            "January 10",
            "January 11",
            "January 12",
            "January 13",
            "January 14",
            "January 15",
            "January 16",
            "January 17",
            "January 18",
            "January 19",
            "January 20",
            "January 21",
            "January 22",
            "January 23",
            "January 24",
            "January 25",
            "January 26",
            "January 27",
            "January 28",
            "January 29",
            "January 30",
            "January 31",
            "February 1",
            "February 2",
            "February 3",
            "February 4",
            "February 5",
            "February 6",
            "February 7",
            "February 8",
            "February 9",
            "February 10",
            "February 11",
            "February 12",
            "February 13",
            "February 14",
            "February 15",
            "February 16",
            "February 17",
            "February 18",
            "February 19",
            "February 20",
            "February 21",
            "February 22",
            "February 23",
            "February 24",
            "February 25",
            "February 26",
            "February 27",
            "February 28",
            "March 1",
            "March 2",
            "March 3",
            "March 4",
            "March 5",
            "March 6",
            "March 7",
            "March 8",
            "March 9",
            "March 10",
            "March 11",
            "March 12",
            "March 13",
            "March 14",
            "March 15",
            "March 16",
            "March 17",
            "March 18",
            "March 19",
            "March 20",
            "March 21",
            "March 22",
            "March 23",
            "March 24",
            "March 25",
            "March 26",
            "March 27",
            "March 28",
            "March 29",
            "March 30",
            "March 31",
            "April 1",
            "April 2",
            "April 3",
            "April 4",
            "April 5",
            "April 6",
            "April 7",
            "April 8",
            "April 9",
            "April 10",
            "April 11",
            "April 12",
            "April 13",
            "April 14",
            "April 15",
            "April 16",
            "April 17",
            "April 18",
            "April 19",
            "April 20",
            "April 21",
            "April 22",
            "April 23",
            "April 24",
            "April 25",
            "April 26",
            "April 27",
            "April 28",
            "April 29",
            "April 30",
            "May 1",
            "May 2",
            "May 3",
            "May 4",
            "May 5",
            "May 6",
            "May 7",
            "May 8",
            "May 9",
            "May 10",
            "May 11",
            "May 12",
            "May 13",
            "May 14",
            "May 15",
            "May 16",
            "May 17",
            "May 18",
            "May 19",
            "May 20",
            "May 21",
            "May 22",
            "May 23",
            "May 24",
            "May 25",
            "May 26",
            "May 27",
            "May 28",
            "May 29",
            "May 30",
            "May 31",
            "June 1",
            "June 2",
            "June 3",
            "June 4",
            "June 5",
            "June 6",
            "June 7",
            "June 8",
            "June 9",
            "June 10",
            "June 11",
            "June 12",
            "June 13",
            "June 14",
            "June 15",
            "June 16",
            "June 17",
            "June 18",
            "June 19",
            "June 20",
            "June 21",
            "June 22",
            "June 23",
            "June 24",
            "June 25",
            "June 26",
            "June 27",
            "June 28",
            "June 29",
            "June 30",
            "July 1",
            "July 2",
            "July 3",
            "July 4",
            "July 5",
            "July 6",
            "July 7",
            "July 8",
            "July 9",
            "July 10",
            "July 11",
            "July 12",
            "July 13",
            "July 14",
            "July 15",
            "July 16",
            "July 17",
            "July 18",
            "July 19",
            "July 20",
            "July 21",
            "July 22",
            "July 23",
            "July 24",
            "July 25",
            "July 26",
            "July 27",
            "July 28",
            "July 29",
            "July 30",
            "July 31",
            "August 1",
            "August 2",
            "August 3",
            "August 4",
            "August 5",
            "August 6",
            "August 7",
            "August 8",
            "August 9",
            "August 10",
            "August 11",
            "August 12",
            "August 13",
            "August 14",
            "August 15",
            "August 16",
            "August 17",
            "August 18",
            "August 19",
            "August 20",
            "August 21",
            "August 22",
            "August 23",
            "August 24",
            "August 25",
            "August 26",
            "August 27",
            "August 28",
            "August 29",
            "August 30",
            "August 31",
            "September 1",
            "September 2",
            "September 3",
            "September 4",
            "September 5",
            "September 6",
            "September 7",
            "September 8",
            "September 9",
            "September 10",
            "September 11",
            "September 12",
            "September 13",
            "September 14",
            "September 15",
            "September 16",
            "September 17",
            "September 18",
            "September 19",
            "September 20",
            "September 21",
            "September 22",
            "September 23",
            "September 24",
            "September 25",
            "September 26",
            "September 27",
            "September 28",
            "September 29",
            "September 30",
            "October 1",
            "October 2",
            "October 3",
            "October 4",
            "October 5",
            "October 6",
            "October 7",
            "October 8",
            "October 9",
            "October 10",
            "October 11",
            "October 12",
            "October 13",
            "October 14",
            "October 15",
            "October 16",
            "October 17",
            "October 18",
            "October 19",
            "October 20",
            "October 21",
            "October 22",
            "October 23",
            "October 24",
            "October 25",
            "October 26",
            "October 27",
            "October 28",
            "October 29",
            "October 30",
            "October 31",
            "November 1",
            "November 2",
            "November 3",
            "November 4",
            "November 5",
            "November 6",
            "November 7",
            "November 8",
            "November 9",
            "November 10",
            "November 11",
            "November 12",
            "November 13",
            "November 14",
            "November 15",
            "November 16",
            "November 17",
            "November 18",
            "November 19",
            "November 20",
            "November 21",
            "November 22",
            "November 23",
            "November 24",
            "November 25",
            "November 26",
            "November 27",
            "November 28",
            "November 29",
            "November 30",
            "December 1",
            "December 2",
            "December 3",
            "December 4",
            "December 5",
            "December 6",
            "December 7",
            "December 8",
            "December 9",
            "December 10",
            "December 11",
            "December 12",
            "December 13",
            "December 14",
            "December 15",
            "December 16",
            "December 17",
            "December 18",
            "December 19",
            "December 20",
            "December 21",
            "December 22",
            "December 23",
            "December 24",
            "December 25",
            "December 26",
            "December 27",
            "December 28",
            "December 29",
            "December 30",
            "December 31",
        ]
        gang_names = ["[PLACEHOLDER]"]
        global enemy_gang_name, enemy_gang_rel, enemy_gang_lead
        enemy_gang_name = choice(gang_names)
        enemy_gang_lead = 1
        enemy_gang_rel = 0.5
        try:
            # If you create a file called male.dat in your openlife save folder,
            # You can add custom male forenames. Each forename
            # is split by a new line
            f = open("male.dat", "r")
            data = f.read()
            forename_m = data.split("\n")
            if verbose_message == 1:
                print("--------------------")
                print("Loaded Custom Male Forenames.")
        except:
            pass
        try:
            # If you create a file called female.dat in your openlife save folder,
            # You can add custom female forenames. Each forename
            # is split by a new line
            f = open("female.dat", "r")
            data = f.read()
            forename_f = data.split("\n")
            if verbose_message == 1:
                print("--------------------")
                print("Loaded Custom Female Forenames.")
        except:
            pass
        try:
            # If you create a file called surname.dat in your openlife save folder,
            # You can add custom surnames. Each surname
            # is split by a new line
            f = open("surname.dat", "r")
            data = f.read()
            surname = data.split("\n")
            if verbose_message == 1:
                print("--------------------")
                print("Loaded Custom Surnames.")
        except:
            pass

        global edu_lvl, job_id, job_lvl
        edu_lvl = 1

        global pension
        pension = 0
        job_id = 0
        job_lvl = 1

        from time import strftime

        global year
        year = strftime("%Y")
        year = int(year)

        global debt, savings
        savings = 0
        debt = 0

        global hours, min_hours, salary, expenses
        salary = 0
        hours = 0
        min_hours = 0
        expenses = 800

        global offences
        global is_job
        offences = 0
        global is_depressed
        global degree
        is_depressed = 0
        degree = 0
        global club_count
        global stress
        global is_sch_gang
        is_sch_gang = 0  # teen school gang
        stress = 0
        global fake_id, is_drip
        global is_job
        is_job = 0
        fake_id = 0
        is_drip = 0
        club_count = 0

        return True
    def clear_screen():
        global allow_test
        if allow_test == 1:
            res=uname()
            os.system("cls" if res[0] == "Windows" else "clear")
    def coworker_list(goto=0):
        global coworkers
        div()
        n = 1
        for item in coworkers:
            item.list(n)
            n += 1
        print("[0] Return")
        div()
        try:
            ch = int(input(">"))
        except:
            adult()
        div()
        if ch > 0 and ch <= len(coworkers):
            coworkers[ch-1].interact()
            adult()
    def child_list(goto=0):
        global children
        div()
        for item in children:
            item.list()
        print("[0] Return")
        div()
        try:
            ch = int(input(">"))
        except:
            adult()
        div()
        if ch > 0 and ch <= len(children):
            children[ch-1].interact()
            adult()
        else:
            adult()
    def view_ribbons(reason):
        global money, debt, ethics, intel, age, ethics, looks, age, happiness, health, is_depressed, lottery_wins, fame, is_bandit, is_cancer, flip_profits, subscribers, is_opentube
        has_ribbon = 0
        if money >=100000000:
            print("Ribbon: Rich")
            has_ribbon = 1
        if debt >= money + savings:
            print("Ribbon: Debt Slave")
            is_ribbon = 1
        if lottery_wins >= 50:
            print("Ribbon: Cheater")
            is_ribbon = 1
        if ethics == 0:
            print("Ribbon: Bad Karma King")
            has_ribbon = 1
        if age >= 123:
            print("Ribbon: Geriatric")
            has_ribbon = 1
        if intel <= 0.15:
            print("Ribbon: Stupid")
            has_ribbon = 1
        if flip_profits >= 2000000:
            has_ribbon = 1
            print("Ribbon: Flipper")
        if fame > 0:
            print("Ribbon: Famous")
            has_ribbon = 1
        if intel >= 0.75:
            print("Ribbon: Nerd")
            has_ribbon = 1
        if reason == -1:
            has_ribbon = 1
            print("Ribbon: Wasteful")
        if age < 18:
            has_ribbon = 1
            print("Ribbon: Unlucky")
        if is_bandit == 1:
            print("Ribbon: Bandit")
        if looks >= 0.75:
            has_ribbon = 1
            print("Ribbon: Beautiful")
        if looks == 1 and intel == 1 and happiness == 1 and health == 1:
            has_ribbon = 1
            print("Ribbon: Perfectionist")
        if is_opentube == 1 and subscribers > 1000000:
            has_ribbon = 1
            print("Ribbon: Influencer")
        if is_depressed == 1:
            has_ribbon = 1
            print("Ribbon: Depressed")
        if is_cancer == 1:
            has_ribbon = 1
            print("Ribbon: Carcinogenic")

        if has_ribbon == 0:
            print("Ribbon: Mediocre")
        return True

    def fame_menu():
        global fame, currency, book_base, money
        print(f"[1] Book [{currency}25,000]")
        print(f"[2] Commercial [{currency}{(fame*100)*2500}]")
        print(f"[3] Magazine Cover [{currency}{(fame*100)*5500}]")
        print(f"[4] Talk Show [{currency}0]")
        div()
        try:
            ch = int(input(">"))
        except:
            adult()
        div()
        if ch == 1:
            if book_base == 0:
                if fame >= 0.75:
                    print("You published a book.")
                    print("It became a bestseller.")
                    revenue = int(
                        25000 * (rng(4, 6)) + ((rng(4, 6) / 10)) + ((rng(4, 6) / 100))
                    )
                    base = str("{:,}".format((revenue)))
                    print(f"Your book made {currency}{base}.")
                    money += revenue
                    fame += 0.0001 * revenue
                    book_base += 3
                elif fame >= 0.5:
                    print("You published a book.")
                    print("You just about broke even.")
                    revenue = int(25000 * ((rng(12, 14) / 10)))
                    base = str("{:,}".format((revenue)))
                    print(f"Your book made {currency}{base}.")
                    money += revenue
                    fame += 0.00005 * revenue
                    book_base += 3
                else:
                    print("You published a book.")
                    print("it absolutely bombed.")
                    base = str("{:,}".format((revenue)))
                    revenue = int(rng(4000, 10000))
                    fame -= 0.001 * revenue
                    book_base += 3
                    print(f"Your book made {currency}{base}.")
                adult()
            else:
                print("You were unable to find a publisher for your book.")
        elif ch == 2:
            pay = (fame * 100) * 2500
            print("You did a commerical for [COMPANY NAME HERE]")
            print("Response:", pbar2(0.85))
            print(f"You made {currency}{pay}")
            money += pay
            adult()
        elif ch == 3:
            pay = (fame * 100) * 5500
            print("You posed for Wank Magazine.")
            print("Response:", pbar2(0.55))
            print(f"You made {currency}{pay}")
            money += pay
            adult()
        elif ch == 4:
            if fame >= 0.9:
                chance = rng(1, 3)
                if chance == 1:
                    print(
                        f"You went on the Tonight Show by {choice(forename_m)} {choice(surnames)}."
                    )
                    print("Response:", pbar2(0))
                    if fame > 0.25:
                        fame -= 0.25
                    else:
                        fame -= fame / 4
                    adult()
                else:
                    print(
                        f"You went on the Tonight Show by {choice(forename_m)} {choice(surnames)}."
                    )
                    print("Response:", pbar2(1))
                    if fame < 0.25:
                        fame += 0.25
                    else:
                        fame += fame / 4
                    adult()
        else:
            adult()

    def friend_1_interact(goto):
        global friend_count, friend_1, happiness
        if friend_1.rel > 1:
            friend_1.rel = 1
        if friend_1.rel < 0:
            friend_1.rel = 0
        div()
        print(friend_1.name)
        print("Age:", friend_1.age)
        div()
        print(f"Relationship:", pbar2(friend_1.rel), f"{int(friend_1.rel*100)}%")
        div()
        print(f"Smarts      :", pbar2(friend_1.intel), f"{int(friend_1.intel*100)}%")
        print(f"Looks       :", pbar2(friend_1.looks), f"{int(friend_1.looks*100)}%")
        print(
            "Craziness   :",
            pbar2(friend_1.craziness),
            f"{int(friend_1.craziness*100)}%",
        )
        div()
        print("[1] Spend Time With")
        print("[2] Compliment")
        print("[x] Conversation")
        print("[x] Date")
        print("[5] Unfriend")
        print("[6] Insult")
        print("[x] Make Love")
        print("[x] Movies")
        div()
        try:
            ch = int(input(">"))
        except:
            if goto == 1:
                uni()
            else:
                adult()
        if ch == 1:
            print(f"You took {friend_1.name} {choice(spend_time)}.")
            friend_1.rel += 0.25
            if goto == 1:
                uni()
            else:
                adult()
        elif ch == 2:
            div()
            print(f"You called {friend_1.name} {choice(compliments)}!")
            happiness += 0.25
            friend_1.rel += 0.25
            if friend_1.rel > 0.75:
                print(f"{friend_1.name} called you {choice(compliments)}!")
                happiness += 0.45
            if goto == 1:
                uni()
            else:
                adult()
        elif ch == 5:
            # If there are 3 friends:
            # Friend 3 --> Friend 2
            # Friend 2 --> Friend 1

            # If there are 2 friends:
            # Friend 2 --> Friend 1

            # If there is 1 friend:
            # Delete friend 1
            if friend_count == 1:
                del friend_1
            elif friend_count == 2:
                friend_1 = friend_2
            elif friend_count == 3:
                friend_1 = friend_2
                friend_2 = friend_3
            else:
                print("An error occured.")
                if goto == 1:
                    uni()
                else:
                    adult()
            friend_count -= 1
            print("You unfriended your friend.")
            if goto == 1:
                uni()
            else:
                adult()
        elif ch == 6:
            print(f"You called {friend_1.name}  {choice(insults)}!")
            friend_1.rel -= 0.25
            happiness -= 0.25
            if friend_1.rel <= 0.25:
                print(f"{friend_1.name} called you {choice(insults)}!")
                happiness -= 0.25
                friend_1.rel -= 0.10
            if goto == 1:
                uni()
            else:
                adult()
        else:
            if goto == 1:
                uni()
            else:
                adult()

    def friend_2_interact(goto):
        global friend_count, friend_2, happiness
        if friend_2.rel > 1:
            friend_2.rel = 1
        if friend_2.rel < 0:
            friend_2.rel = 0
        div()
        print(friend_2.name)
        print("Age:", friend_2.age)
        div()
        print(f"Relationship:", pbar2(friend_2.rel), f"{int(friend_2.rel*100)}%")
        div()
        print(f"Smarts      :", pbar2(friend_2.intel), f"{int(friend_2.intel*100)}%")
        print(f"Looks       :", pbar2(friend_2.looks), f"{int(friend_2.looks*100)}%")
        print(
            "Craziness   :",
            pbar2(friend_2.craziness),
            f"{int(friend_2.craziness*100)}%",
        )
        div()
        print("[1] Spend Time With")
        print("[2] Compliment")
        print("[x] Conversation")
        print("[x] Date")
        print("[5] Unfriend")
        print("[6] Insult")
        print("[x] Make Love")
        print("[x] Movies")
        div()
        try:
            ch = int(input(">"))
        except:
            if goto == 1:
                uni()
            else:
                adult()
        if ch == 1:
            print(f"You took {friend_2.name} {choice(spend_time)}.")
            friend_2.rel += 0.25
            if goto == 1:
                uni()
            else:
                adult()
        elif ch == 2:
            div()
            print(f"You called {friend_2.name} {choice(compliments)}!")
            happiness += 0.25
            friend_2.rel += 0.25
            if friend_2.rel > 0.75:
                print(f"{friend_2.name} called you {choice(compliments)}!")
                happiness += 0.45
            if goto == 1:
                uni()
            else:
                adult()
        elif ch == 5:
            # If there are 3 friends:
            # Friend 3 --> Friend 2
            # Friend 2 --> Friend 1

            # If there are 2 friends:
            # Friend 2 --> Friend 1

            # If there is 1 friend:
            # Delete friend 1
            if friend_count == 1:
                del friend_2
            elif friend_count == 2:
                friend_2 = friend_2
            elif friend_count == 3:
                friend_2 = friend_2
                friend_2 = friend_3
            else:
                print("An error occured.")
                if goto == 1:
                    uni()
                else:
                    adult()
            friend_count -= 1
            print("You unfriended your friend.")
            if goto == 1:
                uni()
            else:
                adult()
        elif ch == 6:
            print(f"You called {friend_2.name}  {choice(insults)}!")
            friend_2.rel -= 0.25
            happiness -= 0.25
            if friend_2.rel <= 0.25:
                print(f"{friend_2.name} called you {choice(insults)}!")
                happiness -= 0.25
                friend_2.rel -= 0.10
            if goto == 1:
                uni()
            else:
                adult()
        else:
            if goto == 1:
                uni()
            else:
                adult()

    def friend_3_interact(goto):
        global friend_count, friend_3, happiness
        if friend_3.rel > 1:
            friend_3.rel = 1
        if friend_3.rel < 0:
            friend_3.rel = 0
        div()
        print(friend_3.name)
        print("Age:", friend_3.age)
        div()
        print(f"Relationship:", pbar2(friend_3.rel), f"{int(friend_3.rel*100)}%")
        div()
        print(f"Smarts      :", pbar2(friend_3.intel), f"{int(friend_3.intel*100)}%")
        print(f"Looks       :", pbar2(friend_3.looks), f"{int(friend_3.looks*100)}%")
        print(
            "Craziness   :",
            pbar2(friend_3.craziness),
            f"{int(friend_3.craziness*100)}%",
        )
        div()
        print("[1] Spend Time With")
        print("[2] Compliment")
        print("[x] Conversation")
        print("[x] Date")
        print("[5] Unfriend")
        print("[6] Insult")
        print("[x] Make Love")
        print("[x] Movies")
        div()
        try:
            ch = int(input(">"))
        except:
            if goto == 1:
                uni()
            else:
                adult()
        if ch == 1:
            print(f"You took {friend_3.name} {choice(spend_time)}.")
            friend_3.rel += 0.25
            if goto == 1:
                uni()
            else:
                adult()
        elif ch == 2:
            div()
            print(f"You called {friend_3.name} {choice(compliments)}!")
            happiness += 0.25
            friend_3.rel += 0.25
            if friend_3.rel > 0.75:
                print(f"{friend_3.name} called you {choice(compliments)}!")
                happiness += 0.45
            if goto == 1:
                uni()
            else:
                adult()
        elif ch == 5:
            # If there are 3 friends:
            # Friend 3 --> Friend 2
            # Friend 2 --> Friend 1

            # If there are 2 friends:
            # Friend 2 --> Friend 1

            # If there is 1 friend:
            # Delete friend 1
            if friend_count == 1:
                del friend_3
            elif friend_count == 2:
                friend_3 = friend_3
            elif friend_count == 3:
                friend_3 = friend_3
                friend_3 = friend_3
            else:
                print("An error occured.")
                if goto == 1:
                    uni()
                else:
                    adult()
            friend_count -= 1
            print("You unfriended your friend.")
            if goto == 1:
                uni()
            else:
                adult()
        elif ch == 6:
            print(f"You called {friend_3.name}  {choice(insults)}!")
            friend_3.rel -= 0.25
            happiness -= 0.25
            if friend_3.rel <= 0.25:
                print(f"{friend_3.name} called you {choice(insults)}!")
                happiness -= 0.25
                friend_3.rel -= 0.10
            if goto == 1:
                uni()
            else:
                adult()
        else:
            if goto == 1:
                uni()
            else:
                adult()

    def prison_pause():
        div()
        print("[0] Resume")
        print("[x] Save Game")
        print("[x] Load Game")
        print("[5] Exit Game")
        div()
        try:
            ch = int(input(">"))
        except:
            prison()
        if ch == 5:
            print("[0] Return")
            print("[x] Exit And Save")
            print("[2] Exit Without Saving")
            div()
            try:
                ch = int(input(">"))
            except:
                prison()
            if ch == 2:
                mainmenu()
            else:
                prison()
        else:
            prison()

    def prison_menu():
        global health, behaviour, prison_years, sentence, forename, surname, offences, behaviour, is_appeal, money
        if is_appeal == 0:
            print("[1] Appeal Sentence")
        else:
            print("[x] Appeal Sentence")
        print("[2] Meditate In Cell")
        print("[3] Escape [25% chance]")
        print("[4] Riot [50% chance]")
        print("[5] Surrender")
        print(
            f"[6] Bail Out [{currency}"
            + str("{:,}".format((45000 * prison_years)))
            + "]"
        )
        print("[0] Return")
        div()
        if prison_years < 0:
            print("Years left: Life")
        else:
            print(f"Years left: " + str("{:,}".format((prison_years))))
        print(f"Sentence: " + str("{:,}".format((sentence))), "years")
        print("Behaviour:", pbar2(behaviour))
        div()
        try:
            ch = int(input(">"))
        except:
            prison()
        if ch == 1:
            if is_appeal == 0 and behaviour >= 0.75 and sentence > 2 * prison_years:
                print("Your appeal was approved!")
                prison_years = 1
                prison_age()
            else:
                print("Your appeal was denied.")
                is_appeal = 1  # Only one chance !
                prison()
        elif ch == 2:
            print("You meditated in your cell.")
            behaviour += 0.25
            prison()
        elif ch == 3:
            chance = rng(1, 4)
            if chance == 3:
                print("You escaped.")
                offences += 1
                adult()
            else:
                add_base = rng(2, 5)
                print(
                    f"Your sentence has been extended by {add_base} years for attempted escape."
                )
                prison_years += add_base
                sentence += add_base
                prison()
        elif ch == 4:
            chance = rng(1, 2)
            if chance == 2:
                print("A riot was started.")
                health -= 0.25
                prison()
            else:
                prison()
        elif ch == 5:
            print(f"[1] Surrender {forename} {surname}")
            print("[0] Return")
            div()
            try:
                ch = int(input(">"))
            except:
                prison()
            if ch == 1:
                die(0)
            else:
                prison()
        elif ch == 6:
            if money >= 45000 * prison_years:
                money -= 45000 * prison_years
                print("You have been bailed out of prison.")
                prison_years = 1
                prison_age()
            else:
                print(f"You need {currency}{'{:,}'.format(money * 45000)} to bail out")
                prison()
        else:
            prison()

    def prison_age():
        global sentence, age, prison_years, offences, debt, savings
        debt += int((debt / 5))
        savings += int((savings / 10))
        age += 1
        prison_years -= 1

        # You cannot die in prison yet!

        if prison_years == 0:
            sentence = 0
            offences = 0
            print("You have been released from prison.")
            adult()
        else:
            prison()

    def prison():
        div()
        global happiness, health, intel, looks, forename, surname, behaviour
        if behaviour > 1:
            behaviour = 1
        if behaviour < 0:
            behaviour = 0
        if happiness > 1:
            happiness = 1
        if happiness < 0:
            happiness = 0
        if health > 1:
            health = 1
        if health < 0:
            emergency_room(4)
        if intel > 1:
            intel = 1
        if looks > 1:
            looks = 1
        if intel < 0:
            intel = 0
        if looks < 0:
            looks = 0
        print(forename + " " + surname)
        print("Prisoner")
        if is_depressed == 1:
            div()
            print("Suffers from: Depression")
        print("Age", age)
        print(f"{currency}" + str("{:,}".format((money))))
        div()
        print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "%")
        print("Health:   ", pbar2(health), str(int(health * 100)) + "%")
        print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "%")
        print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "%")
        div()
        print("[1] Prison")
        print("[0] Age Up")
        print("[5] Pause Menu")
        div()
        try:
            ch = int(input(">"))
        except:
            prison()
        if ch == 1:
            prison_menu()
        elif ch == 0:
            prison_age()
        else:
            prison()

    def adult_init_juvie():
        div()
        global clout, socialc
        clout, socialc = 4, 20  # Easter egg :)
        global mother_rel, father_rel
        global stress
        stress = 0.65
        from random import randint

        if mother_rel > 0.8:
            mother_rel = 0.8
        if father_rel > 0.8:
            father_rel = 0.8
        return True

    def transfer_to_prison():
        global sentence, juvie_years, prison_years, behaviour
        behaviour = 0.25
        sentence = juvie_years
        juvie_years = 0
        prison_years = sentence
        adult_init_juvie()
        prison()

    def juvie_age():
        global age, juvie_years, offences
        age += 1
        juvie_years -= 1
        if juvie_years == 0:
            div()
            offences = 0
            print("You have been released from juvie.")
            br()
            teen()
        if age == 18:
            div()
            print("You have been transferred to prison.")
            br()
            transfer_to_prison()
        juvie()

    def juvie_menu():
        global health, behaviour, juvie_years, sentence, forename, surname
        div()
        print("[1] Appeal Sentence")
        print("[2] Meditate In Cell")
        print("[3] Escape [25% chance]")
        print("[4] Riot [50% chance]")
        print("[5] Surrender")
        print("[0] Return")
        div()
        print(f"Years left: " + str("{:,}".format((juvie_years))))
        print(f"Sentence: " + str("{:,}".format((sentence))), "years")
        div()
        try:
            ch = int(input(">"))
        except:
            juvie()
        if ch == 1:
            print("Your appeal was denied.")
            juvie()
        elif ch == 2:
            print("You meditated in your cell.")
            juvie()
        elif ch == 3:
            chance = rng(1, 4)
            if chance == 3:
                print("You escaped.")
                teen()
            else:
                add_base = rng(2, 5)
                print(
                    f"Your sentence has been extended by {add_base} years for attempted escape."
                )
                juvie_years += add_base
                sentence += add_base
                juvie()
        elif ch == 4:
            chance = rng(1, 2)
            if chance == 2:
                print("A riot was started.")
                health -= 0.25
                juvie()
            else:
                juvie()
        elif ch == 5:
            print(f"[1] Surrender {forename} {surname}")
            print("[0] Return")
            div()
            try:
                ch = int(input(">"))
            except:
                juvie()
            if ch == 1:
                die(0)
            else:
                juvie()
        else:
            juvie()

    def juvie():
        global mother_name, father_name
        global offences
        global happiness, health, intel, looks, ethics, grades, clout, socialc
        global mother_rel, father_rel, juvie_years
        global money, is_depressed, is_hbp
        if grades > 1:
            grades = 1
        if grades < 0:
            grades = 0
        if happiness > 1:
            happiness = 1
        if happiness < 0:
            happiness = 0
        if health > 1:
            health = 1
        if health < 0:
            emergency_room(3)
        if intel > 1:
            intel = 1
        if looks > 1:
            looks = 1
        if intel < 0:
            intel = 0
        if looks < 0:
            looks = 0
        if clout > 1:
            clout = 1
        if clout < 0:
            clout = 0
        if socialc > 1:
            socialc = 1
        if socialc < 0:
            socialc = 0
        global forename, surname
        global mother_rel, father_rel
        global money
        div()
        print(forename + " " + surname)
        print("Juvie Prisoner")
        if is_depressed == 1:
            div()
            print("Suffers from: Depression")
            if is_hbp == 0:
                div()
        print("Age", age)
        print(f"{currency}" + str("{:,}".format((money))))
        div()
        print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "%")
        print("Health:   ", pbar2(health), str(int(health * 100)) + "%")
        print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "%")
        print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "%")
        div()
        print("[1] Juvie")
        print("[0] Age Up")
        print("[5] Paue Menu")
        try:
            ch = int(input(">"))
        except:
            juvie()
        if ch == 1:
            juvie_menu()
        elif ch == 0:
            juvie_age()
        else:
            juvie()

    def go_to_prison():
        global prison_years, offences, juvie_years, sentence, behaviour
        beghaviour = 0.25
        if sentence == 0:
            sentence = offences * 2
        elif prison_years > 0:
            offences += 1
            sentence = prison_years * 3 * offences
        else:
            sentence = 69420
        div()
        if prison_years == 1:
            print("You have been sent to prison for a year.")
        else:
            print(f"You have been sent to prison for {sentence} years.")
        if sentence == 0:
            sentence = prison_years
        prison_years = sentence
        prison()

    def go_to_juvie():
        global juvie_years, offences, juvie_years, sentence
        if juvie_years > 0:
            offences += 1
            juvie_years *= offences
        else:
            juvie_years = offences
        div()
        if juvie_years == 1:
            print("You have been sent to juvenile detention for a year.")
        else:
            print(f"You have been sent to juvenile detention for {juvie_years} years.")
        sentence = juvie_years
        juvie()

    def personal_bankrupcy():
        print("You filed for personal bankrupcy.")
        global house_count, house_1, house_2, house_3, debt, is_job, job_id, money, savings, edu_lvl, degree, fame, pension
        try:
            del house_1
        except:
            pass
        try:
            del house_2
        except:
            pass
        try:
            del house_3
        except:
            pass
        house_count = 0
        debt = 0
        is_job, job_id = 0, 0
        money, savings = 0, 0
        if edu_lvl > 1:
            edu_lvl = 1
        fame = 0
        degree = 0
        pension = 0
        adult()

    def sponsor():
        global subscribers, money
        money_paid = int(subscribers / 15)
        print(
            f"The sponsor wants to pay you {currency}"
            + str("{:,}".format(((money_paid))))
        )
        div()
        print("[1] Take Offer")
        print("[2] Negotiate for higher price")
        print("[0] Decline")
        div()
        try:
            ch = int(input(">"))
        except:
            opentube()
        if ch == 1:
            chance = rng(1, 3)
            if chance == 1:
                print("You did the sponsorship deal.")
                print("Reception", pbar2(1))
                money += money_paid
                opentube()
            elif chance == 2:
                print("You did the sponsorship deal.")
                print("Reception", pbar2(0.45))
                money += money_paid
                old_subs = subscribers
                subscribers -= int(subscribers / 10)
                print(f"You lost {old_subs/10} subscribers.")
                opentube()
            elif chance == 3:
                print("You did the sponsorship deal.")
                money += money_paid
                print("Reception", pbar2(0))
                subscribers = int(subscribers / 10)
                print(f"You lost {subscribers*9} subscribers.")
                opentube()
        else:
            opentube()

    def opentube_init():
        div()
        print("Welcome to OpenTube")
        div()
        global channel_name, subscribers, view_count, video_count, is_verif, is_opentube
        global money, is_monetised, watch_time, opentube_year, forename, surname
        print("OpenTube Channel name:")
        try:
            channel_name = input(">")
        except:
            adult()
        if channel_name == "":
            channel_name = f"{forename} {surname}"
        subscribers = 0
        watch_time = 0
        opentube_year = 1
        view_count = 0
        is_verif = 0
        video_count = 0
        money = 0
        is_monetised = 0
        is_opentube = 1
        opentube()

    def opentube_age():
        global opentube_year, video_count, view_count, subscribers, money, is_monetised
        opentube_year += 1
        for i in range(video_count):
            oldsubs = subscribers
            views_gained = int(oldsubs + int((oldsubs / 2)))
            view_count += views_gained
            subs_gained = int(views_gained / 3)
            if subs_gained > 8000000000 - subscribers:
                subs_gained = 8000000000 - subscribers
            subscribers += subs_gained
            if is_monetised == 1:
                cpm = (views_gained / 17) / 100
                money += int(cpm)
        opentube()

    def upload():
        global view_count, subscribers, video_count, money, is_monetised
        div()
        print("CPM= cents per million [measured in kv]")
        print("kv= thousand views")
        print("[-SUB] means you lose subscribers instead of gaining them")
        div()
        print("Choose a video type:")
        print("[0] Return")
        print("[1] OpenTube [CPM=17p/kv]")
        print("[x] BitLife [CPM=10p/kv] [-SUB]")
        print("[3] Gaming [CPM=10p/kv]")
        print("[4] How-To [CPM=7p/kv]")
        print("[5] Educational [CPM=6p/kv]")
        print("[x] Drama [CPM=11] [-SUB]")
        print("[x] Music [CPM=0] [SUB x3]")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            opentube()
        elif ch == 1 or ch == 3 or ch == 4 or ch == 5:
            if ch == 1:
                cpm = 17
            elif ch == 3:
                cpm = 10
            elif ch == 4:
                cpm = 7
            elif ch == 5:
                cpm = 6
            else:
                cpm = 0
            views = (subscribers) + (subscribers / 3)
            chance = rng(1, 40)
            bomb_chance = rng(1, 20)
            if bomb_chance == 20:
                print("Your video wast terrible :(")
                views /= 10
                subs_gained = (-views) * 3
            if chance == 40:
                print("Your video went viral!")
                views *= 11
                subs_gained = views / 9
            if views < 1:
                views = 1
            if chance != 40 or bomb_chance != 20:
                subs_gained = views / 3
            if subs_gained < 1:
                subs_gained = 1
            if subs_gained > 10:
                subs_gained += rng((-(int(subs_gained / 10))), (int(subs_gained / 10)))
            views = int(views)
            subs_gained = int(subs_gained)
            if subs_gained > (8000000000 - subscribers):
                subs_gained = 8000000000 - subscribers
            base = int(views / 1000)
            money_made = int((base * cpm) / 100)
            if views == 1 and subs_gained == 1:
                print("Your video gained 1 view and 1 subscriber.")
            elif views == 1:
                if subs_gained < 0:
                    print(
                        f"Your video gained 1 view and you lost",
                        str("{:,}".format(((-subs_gained)))),
                        "subscribers.",
                    )
                else:
                    print(
                        f"Your video gained 1 view and ",
                        str("{:,}".format((subs_gained))),
                        "subscribers.",
                    )
            elif subs_gained == 1:
                print(
                    f"Your video gained",
                    str("{:,}".format((views))),
                    "views and 1 subscriber.",
                )
            else:
                if subs_gained < 0:
                    print(
                        f"Your video gained",
                        str("{:,}".format((views))),
                        "views and you lost",
                        str("{:,}".format(((-subs_gained)))),
                        "subscribers.",
                    )
                else:
                    print(
                        f"Your video gained",
                        str("{:,}".format((views))),
                        "views and",
                        str("{:,}".format((subs_gained))),
                        "subscribers.",
                    )
            if is_monetised == 1:
                print(f"Your video made {currency}" + str("{:,}".format((money_made))))
                money += money_made
            view_count += views
            subscribers += subs_gained
            if subscribers > 8000000000:
                subscribers = 8000000000
            video_count += 1
            opentube()
        else:
            opentube()

    def delete_channel():
        div()
        global channel_name, subscribers, view_count, video_count, money, is_opentube
        print("Your channel,", channel_name + ", is gone.")
        div()
        print(f"It had", str("{:,}".format((subscribers))), "subscribers.")
        print(f"It had", str("{:,}".format((view_count))), "views.")
        print(f"You uploaded", str("{:,}".format((video_count))), "videos.")
        div()
        print(f"Money: {currency}" + str("{:,}".format((money))))
        is_opentube = 0
        adult()

    def opentube_stats():
        div()
        global channel_name, subscribers, view_count, video_count, is_verif
        global money, is_monetised, watch_time
        print(f"Views:", str("{:,}".format((view_count))))
        print(f"Subscribers:", str("{:,}".format((subscribers))))
        print(f"Video Count:", video_count)
        div()
        print(f"Watch Time: {view_count/4} hours")
        print(
            f"Current Watch Rate: [{int(subscribers+(subscribers/2))}]V [{int((int(subscribers+(subscribers/2)))/3)}]S"
        )
        opentube()

    def opentube():
        div()
        print()
        div()
        global channel_name, subscribers, view_count, video_count, is_verif
        global money, is_monetised, opentube_year
        if is_verif == 1:
            print(channel_name, "[✓]")
        else:
            print(channel_name)
        div()
        print(f"Year: {opentube_year}")
        div()
        print(f"Subscribers:", str("{:,}".format((subscribers))))
        print(f"Views:", str("{:,}".format((view_count))))
        print(f"Video Count:", str("{:,}".format((video_count))))
        print(f"Money: {currency}" + str("{:,}".format((money))))
        div()
        print("[1] Upload Video")
        if is_monetised == 0:
            print("[2] Request Monetisation")
        if is_verif == 0:
            print("[3] Get Verified")
        print(f"[4] Sell Channel [{currency}1 = 15 subs]")
        print("[5] Delete Channel")
        print("[6] Stats")
        print("[7] Sponsorship")
        print("[8] Exit OpenTube")
        print("[9] Set Video Schedule")
        print("[0] Age Up")
        try:
            ch = int(input(">"))
        except:
            ch = 1
        if ch == 1:
            upload()
        elif ch == 8:
            adult()
        elif ch == 9:
            print("[1] No schedule")
            print("[2] Monthy [12 per year] [+10% stress]")
            print("[3] Weekly  [52 yer year] [+25% stress]")
            print("[4] Daily [365 per year [+70% stress]")
            try:
                ch = int(input(">"))
            except:
                opentube()
            global yearly_videos
            if ch == 1:
                yearly_videos = 0
            elif ch == 2:
                yearly_videos = 12
            elif ch == 3:
                yearly_videos = 52
            elif ch == 4:
                yearly_videos = 365
            else:
                pass
            div()
            print("Schedule adjusted.")
            opentube()

        elif ch == 0:
            age_up(1)
        elif ch == 7:
            if subscribers > 1000:
                sponsor()
            else:
                print("You are too small to do a sponsorship :(")
                opentube()
        elif ch == 6:
            opentube_stats()
        elif ch == 2:
            if is_monetised == 1:
                print("You are already monetised.")
                opentube()
            else:
                div()
                if view_count > 100000:
                    print("You have been accepted for monetisation.")
                    is_monetised = 1
                    opentube()
                else:
                    print("Your monetisation request was denied.")
                    opentube()
        elif ch == 5:
            div()
            print("[1] Delete Channel")
            print("[0] Return")
            div()
            try:
                ch = int(input(">"))
            except:
                opentube()
            if ch == 1:
                delete_channel()
            else:
                opentube()
        elif ch == 3:
            if is_verif == 1:
                print("You are already verified.")
                opentube()
            else:
                div()
                if subscribers >= 100000:
                    is_verif = 1
                    print("You have been verified :O")
                    opentube()
                else:
                    print("Your verification request was denied.")
                    opentube()
        elif ch == 4:
            if subscribers >= 10000:
                price = subscribers / 15
                price = int(price)
                print(
                    f"Someone wants to buy your channel for {currency}"
                    + str("{:,}".format((price)))
                )
                print("[1] Take Offer")
                print("[0] Decline Offer")
                try:
                    ch = int(input(">"))
                except:
                    ch = 0
                if ch == 0:
                    opentube()
                else:
                    money += price
                    delete_channel()
            else:
                print("You need 10k subs to sell your channel.")
                opentube()

        else:
            opentube()
    def list_house():
        global houses
        n = 1
        for item in houses:
            item.list(n,0)
            n += 1
        div()
        try:
            ch=int(input(">"))
        except:
            adult()
        div()
        if ch > 0 and ch <= len(houses):
            houses[ch-1].interact()
            adult()
        else:
            adult()
    def house_buy():
        global money, debt, houses
        manor=House()
        villa=House()
        castle=House()
        equestrian=House()
        duplex=House()
        
        manor.compile(rng(10000000,20000000),rng(0,1),1)
        villa.compile(rng(1000000, 5000000),rng(0,1),2)
        castle.compile(rng(5000000, 15000000),rng(0,1),3)
        equestrian.compile(rng(500000, 5000000),rng(0,1),4)
        duplex.compile(rng(2500000, 3000000),rng(0,1),5)
        
        base = str("{:,}".format((money)))
        print(f"Balance: {currency}{base}")
        base = str("{:,}".format((manor.value)))
        if manor.haunted == 1:
            print(f"[1] Manor [{currency}{base}] [Haunted]")
        else:
            print(f"[1] Manor [{currency}{base}]")
        base = str("{:,}".format((villa.value)))
        if villa.haunted == 1:
            print(f"[2] Villa [{currency}{base}] [Haunted]")
        else:
            print(f"[2] Villa [{currency}{base}]")
        base = str("{:,}".format((castle.value)))
        if castle.haunted == 1:
            print(f"[3] Castle [{currency}{base}] [Haunted]")
        else:
            print(f"[3] Castle [{currency}{base}]")
        base = str("{:,}".format((equestrian.value)))
        if equestrian.haunted == 1:
            print(f"[4] Equestrian Property [{currency}{base}] [Haunted]")
        else:
            print(f"[4] Equestrian Property [{currency}{base}]")
        base = str("{:,}".format((duplex.value)))
        if duplex.haunted == 1:
            print(f"[5] Duplex [{currency}{base}] [Haunted]")
        else:
            print(f"[5] Duplex [{currency}{base}]")
        div()
        try:
            ch = int(input(">"))
        except:
            house_buy()
        if ch == 1:
            if money >= manor.price:
                money -= manor.price
            else:
                debt += manor.price
            houses.append(manor)
            adult()
        elif ch == 2:
            if money >= villa.price:
                money -= villa.price
            else:
                debt += villa.price
            houses.append(villa)
            adult()
        elif ch == 3:
            if money >= castle.price:
                money -= castle.price
            else:
                debt += castle.price
            houses.append(castle)
            adult()
        elif ch == 4:
            if money >= equestrian.price:
                money -= equestrian.price
            else:
                debt += equestrian.price
            houses.append(equestrian)
            adult()
        elif ch == 5:
            if money >= duplex.price:
                money -= duplex.price
            else:
                debt += duplex.price
            houses.append(duplex)
            adult()
        else:
            adult()
    def teen_calc_stress():
        global edu_lvl, pension, job_lvl, is_spouse, spouse
        global salary, hours
        global allow_debug
        global mother_age, father_age
        global mother_name, father_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel, part_time_salary
        global money, is_depressed, work_e, is_job
        global job_id, job_lvl, club_count
        global money, stress, teen_hours

        stress = 0.55
        stress += teen_hours * 0.05
        stress += club_count * 0.1
        if happiness >= 0.5:
            stress -= happiness / 2
        if happiness < 0.5:
            stress += happiness
        if stress > 1:
            stress = 1
        if stress < 0:
            stress = 0
        return True

    def calc_stress():
        global edu_lvl, pension, job_lvl, is_spouse, spouse
        global salary, hours, research_lab
        global allow_debug
        global mother_age, father_age
        global mother_name, father_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel, part_time_salary
        global money, is_depressed, work_e, is_job
        global job_id, job_lvl
        global money, stress, yearly_videos
        stress = hours * 0.015
        if part_time_salary > 0:
            stress += 0.2
        if is_depressed == 1:
            stress *= 2
        if yearly_videos == 12:
            stress += 0.1
        if yearly_videos == 52:
            stress += 0.25
        if yearly_videos == 35:
            stress += 0.75
        if happiness <= 0.5:
            stress += happiness
        if happiness >= 0.5 and hours < 40:
            stress -= happiness / 2
        if research_lab[4] == 1:
            stress /= 2
        if stress > 1:
            stress = 1
        if stress < 0:
            stress = 0
        return True

    def wpp_reveal():
        global is_wpp, wpp_name, wpp_year, age, forename, surname, gender
        if gender == 0 or gender == 1:
            was_were = "was"
        else:
            was_were = "were"

        if gender == 0:
            him_her = "him"
        elif gender == 0:
            him_her = "her"
        else:
            him_her = "their"

        if gender == 0:
            he_she = "he"
        elif gender == 1:
            he_she = "she"
        else:
            he_she = "they"

        if gender == 0:
            his_her = "his"
        elif gender == 1:
            his_her = "her"
        else:
            his_her = "their"
        div()
        print(f"{game_name} Times")
        print("The *best* newspaper since 2022 AD")
        div()
        print(
            f"{wpp_name[0]} {wpp_name[1]}'s death was FAKED the whole time; FBI in it for the money"
        )
        div()
        print(
            f"In {wpp_year}, {wpp_name[0]} {wpp_name[1]} sadly passed away as a result of a tragic heart attack. Millions of fans were distraught, with hundreds of flowers sent to {his_her} estate."
        )
        print(f"Or did {he_she}?")
        div()
        print(
            f"Yesterday, we announced that {forename} {surname} had died, touching the heart of {his_her} friends and family."
        )
        print(
            f"Literally this morning, the Federal Bureau of Investigation released the following statement:"
        )
        div()
        print(
            f"NEWS REGARDING {forename.upper()} {surname.upper()} and {wpp_name[0].upper()} {wpp_name[1].upper()}"
        )
        div()
        print(
            f"Yesterday, {forename} {surname} passed away. The {game_name} Times were eager to report on this, leaving it on the front page."
        )
        print(
            f"We would like to announce that {forename} was actually {wpp_name[0]} {wpp_name[1]} under our Witness Protection Program."
        )
        print(
            f"As you have seen over the years {he_she} {was_were} pretty bad at covering their tracks, leading to conspiracy theories that landed on the {game_name} Times's front page."
        )
        print(
            f"Well, those conspiracy theorists were right, and now {wpp_name[0]} {wpp_name[1]} is *actually* dead. We are sorry for the loss, and {his_her} open_casket funeral will be available for the public to either go to or watch on TV."
        )
        print(f"We bid farewell to {wpp_name[0]} {wpp_name[1]}.")
        div()
        print(
            f'Either way, the news is likely to shock fans, with a lot of conspiracy theories saying "I told you so!". Just to clarify, we were never made aware of this, and were taken aback.'
        )
        print(
            f"We hope that fans of {wpp_name[0]} {wpp_name[1]} can respect the decision {he_she} made in {his_her} lifetime to fade away from the public consciousness."
        )
        print(
            f"Being famous is not easy, and can take an incredible toll on the famous person. It's only understandable that {he_she} chose to break away from it, deciding that peace was what {he_she} needed, away from the Paparazzi."
        )
        print(
            f"Either way, you can rest easy knowing that {wpp_name[0]} is resting in Heaven [or in the ground, if you don't believe in that] as we speak."
        )
        div()
        print(f"{wpp_name[0]} {wpp_name[1]}")
        print(f"{year-age} - {wpp_year}")
        print(f"{wpp_year} - {year}")
        br()
        return True

    def die(reason):
        global gender
        if gender == 0:
            he_she = "he"
        elif gender == 1:
            he_she = "she"
        else:
            he_she = "they"
        global age, forename, surname, is_depressed, is_spouse, spouse, is_wpp, research_lab
        if research_lab[3] == 1 and reason != 0:
            print("You suddenly felt a jolt as your vision flies up, allowing you to see the outside of your body.")
            print("Confused, you wonder if you were about to die, but your vision flies back into your body, knocking you out.")
            print("After a visit to A&E*, they reassure you that you are fine, and that it was simply shock that made you hallucinate.")
            print("\nYou wonder how many more near-dath experiences you will experience in future.")
            print("\n* Accident & Emergency, British speak for \"The Emergency Room [ER]\"")
            # If immortality is researched, the only way to die is #0 [suicide]
            # If it detects immortality, 
            return True
        div()
        print(f"{game_name} Times")
        print("The *best* newspaper since 2022 AD")
        if reason == 0:
            div()
            print(f"{forename} {surname} commits suicide, aged {age}")
            div()
            print(
                f"{forename} {surname} recently died of an alleged suicide while at their home."
            )
            print(
                "Family members are reportedly distraght as a result of hearing the news."
            )
            print(
                f"\n{forename} {surname} lived a long, happy life, which they wasted in an instant by performing the act of suicide."
            )
            print(
                "They will be missed by their friends and will simultaneously be known as a coward who threw everything away for no reason."
            )
            print(
                "\nThey could have lived happily for the rest of a potentially long life, but they threw it away anyway."
            )
            if is_depressed == 1:
                print(
                    "\nThey were diagnosed with depression a few years ago, so perhaps that is the underlying cause of their untimely death."
                )
            div()
            view_ribbons(-1)
            div()
            if is_wpp == 1:
                br()
                wpp_reveal()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if age < 130:
                if juvie_years > 0:
                    print("[2] Respawn [Go To Juvie]")
                else:
                    print("[2] Respawn")
            div()
            try:
                ch = int(input(">"))
            except:
                mainmenu()
            if ch == 0:
                raise ExitError
            elif ch == 2 and age < 130:
                if age <= 5:
                    infant()
                elif age >= 6 and age < 12:
                    child()
                elif age >= 12 and age < 18:
                    if juvie_years > 0:
                        juvie()
                    else:
                        teen()
                else:
                    adult()
            else:
                mainmenu()
        elif reason == 1:
            div()
            print(f"{forename} {surname} dies of natural cases aged {age}")
            div()
            print(f"{forename} {surname} has died of natural causes while sleeping.")
            if age > 123:
                print(
                    f"They were {age} years old, making them the oldest person in the world at the time."
                )
            print("\nThey lived a long, happy life, surrounded by great people.")
            print("They will be missed by friends and family.")
            div()
            view_ribbons(reason)
            div()
            if is_wpp == 1:
                br()
                wpp_reveal()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if age < 130:
                if juvie_years > 0:
                    print("[2] Respawn [Go To Juvie]")
                else:
                    print("[2] Respawn")
            div()
            try:
                ch = int(input(">"))
            except:
                mainmenu()
            if ch == 0:
                raise ExitError
            elif ch == 2 and age < 130:
                if age <= 5:
                    infant()
                elif age >= 6 and age < 12:
                    child()
                elif age >= 12 and age < 18:
                    if juvie_years > 0:
                        juvie()
                    else:
                        teen()
                else:
                    adult()
            else:
                mainmenu()
        elif reason == 2:
            div()
            print(f"{forename} {surname} dies of heart attack aged {age}")
            div()
            print(
                f"{forename} {surname} passed away as a result of a tragic heart attack last night."
            )
            print(
                f"Their death was extremely untimely and is a tragic loss that will be felt by the"
            )
            print(f"entire {game_name} community.")
            if is_spouse == 1:
                print(f"\n{spouse.name}, {forename}'s spouse, had this to say:")
                print(
                    f"'I am deeply saddened by this. I remember seeing [{forename}] regularly have mental breakdowns as a result of stress."
                )
                print(f"Stress is no joke. It killed my partner.'")

            print(
                f"\nHopefully such heart attacks are seen less and less in the community and that"
            )
            print(
                f"the players of {game_name} do not overwork themselves like {forename} {surname} did."
            )
            div()
            view_ribbons(reason)
            div()
            if is_wpp == 1:
                br()
                wpp_reveal()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if age < 130:
                if juvie_years > 0:
                    print("[2] Respawn [Go To Juvie]")
                else:
                    print("[2] Respawn")
            div()
            try:
                ch = int(input(">"))
            except:
                mainmenu()
            if ch == 0:
                raise ExitError
            elif ch == 2 and age < 130:
                if age <= 5:
                    infant()
                elif age >= 6 and age < 12:
                    child()
                elif age >= 12 and age < 18:
                    if juvie_years > 0:
                        juvie()
                    else:
                        teen()
                else:
                    adult()
            else:
                mainmenu()
        elif reason == 3:
            div()
            print(f"{forename} {surname} dies of cancer aged {age}")
            div()
            print(
                f"{forename} {surname} has died due to complications as a result of a years-long battle with cancer."
            )
            print(
                f"The {game_name} community will be feeling the loss of {forename} {surname} for many years to come."
            )
            print(f"We will miss you, {forename} {surname}.")
            div()
            view_ribbons(reason)
            div()
            if is_wpp == 1:
                br()
                wpp_reveal()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if juvie_years > 0:
                print("[2] Respawn [Go To Juvie]")
            else:
                print("[2] Respawn")
            div()
            try:
                ch = int(input(">"))
            except:
                mainmenu()
            if ch == 0:
                raise ExitError
            elif ch == 2 and age < 130:
                if age <= 5:
                    infant()
                elif age >= 6 and age < 12:
                    child()
                elif age >= 12 and age < 18:
                    if juvie_years > 0:
                        juvie()
                    else:
                        teen()
                else:
                    adult()
            else:
                mainmenu()
        elif reason == 4:
            print(f"{forename} {surname} dies in hospital aged {age}")
            div()
            print(
                f"{forename} {surname} has died in hospital as a result of health complications."
            )
            print(
                f"They had allegedly suffered from deteriorating physical health for years before this incident."
            )
            print(
                f"They collapsed onto the floor in their home and was immediately rushed to hospital."
            )
            print(f"Unfortunately, attempts to revive them were eventually futile.")
            print(
                f"The community will deeply miss {forename} {surname} for many years to come."
            )
            div()
            view_ribbons(reason)
            div()
            if is_wpp == 1:
                br()
                wpp_reveal()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if juvie_years > 0:
                print("[2] Respawn [Go To Juvie]")
            else:
                print("[2] Respawn")
            div()
            try:
                ch = int(input(">"))
            except:
                mainmenu()
            if ch == 0:
                raise ExitError
            elif ch == 2 and age < 130:
                if age <= 5:
                    infant()
                elif age >= 6 and age < 12:
                    child()
                elif age >= 12 and age < 18:
                    if juvie_years > 0:
                        juvie()
                    else:
                        teen()
                else:
                    adult()
            else:
                mainmenu()
        elif reason == 5:
            div()
            print(f"{forename} {surname} dies of cancer aged {age}")
            div()
            print(
                f"{forename} {surname} has died due to complications as a result of a years-long battle with cancer."
            )
            print(
                f"The {game_name} community will be feeling the loss of {forename} {surname} for many years to come."
            )
            print(f"We will miss you, {forename} {surname}.")
            div()
            view_ribbons(reason)
            div()
            if is_wpp == 1:
                br()
                wpp_reveal()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if juvie_years > 0:
                print("[2] Respawn [Go To Juvie]")
            else:
                print("[2] Respawn")
            div()
            try:
                ch = int(input(">"))
            except:
                mainmenu()
            if ch == 0:
                raise ExitError
            elif ch == 2 and age < 130:
                if age <= 5:
                    infant()
                elif age >= 6 and age < 12:
                    child()
                elif age >= 12 and age < 18:
                    if juvie_years > 0:
                        juvie()
                    else:
                        teen()
                else:
                    adult()
            else:
                mainmenu()
        elif reason == 6:
            if gender == 0:
                he_she = "he"
            elif gender == 1:
                he_she == "she"
            else:
                he_she = "they"
            print(f"{forename} {surname} gets struck by lighting")
            div()
            print(
                f"{forename} {surname}, aged {age}, was struck by lighning in a fatal accident."
            )
            print(
                f"They were walking in the park when a storm hit. According to eyewitnesses,"
            )
            print(
                f"{he_she} tried to run away but instead ran straight into the lightning bolt's path."
            )
            print("Death did the rest.")
            div()
            print(
                f"999 was dialled, but by the time {he_she} was put into the ambulance, they were already dead."
            )
            print(
                f"If you are in a storm, the Met Office has some great advice for what to do:"
            )
            print(
                "https://metoffice.gov.uk/weather/warnings-and-advice/seasonal-advice/your-home/stay-safe-in-a-storm/"
            )
            div()
            view_ribbons(reason)
            div()
            if is_wpp == 1:
                br()
                wpp_reveal()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if juvie_years > 0:
                print("[2] Respawn [Go To Juvie]")
            else:
                print("[2] Respawn")
            div()
            try:
                ch = int(input(">"))
            except:
                mainmenu()
            if ch == 0:
                raise ExitError
            elif ch == 2 and age < 130:
                if age <= 5:
                    infant()
                elif age >= 6 and age < 12:
                    child()
                elif age >= 12 and age < 18:
                    if juvie_years > 0:
                        juvie()
                    else:
                        teen()
                else:
                    adult()
            else:
                mainmenu()
        elif reason == 7:
            global surgeons
            doctor = f"{surgeons[0].name}"
            fine = surgeons[0].price * 45
            div()
            print(f"{forename} {surname} Dies of Botched Plastic Surgery")
            div()
            print(f"{forename} {surname} has died as a result of a botched surgery. {forename} was attempting a gender reassignment surgery, a surgery in which the surgeon swaps the gender of the patient.")
            print(f"The doctor in question, {doctor}, has been charged with manslaughter and will receive a {currency}{'{:,}'.format(fine)} fine and 7 years in prison.")
            if surgeons[0].rep >= 0.75:
                print(f"{doctor} was a well-respected plastic surgeon, until they claimed their first victim.")
                print("They will never see the end of this.")
            print(f"Hopefully, {doctor} never repeats such an incident, and hopefully they never work as a plastic surgeon ever again.")
            div()
            view_ribbons(reason)
            div()
            if is_wpp == 1:
                br()
                wpp_reveal()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if juvie_years > 0:
                print("[2] Respawn [Go To Juvie]")
            else:
                print("[2] Respawn")
            div()
            try:
                ch = int(input(">"))
            except:
                mainmenu()
            if ch == 0:
                raise ExitError
            elif ch == 2 and age < 130:
                if age <= 5:
                    infant()
                elif age >= 6 and age < 12:
                    child()
                elif age >= 12 and age < 18:
                    if juvie_years > 0:
                        juvie()
                    else:
                        teen()
                else:
                    adult()                        
            else:
                mainmenu()    
        else:
            raise FeatureNotInGameError

    def make_child():
        global child_count, child_1, child_2, child_3, child_4, child_5, child_6, child_7, child_8, children
        base = Child()
        base.generate_random()
        print("You had a child!")
        base.show_child()
        children.append(base)
        return True

    def spouse_interact(goto):
        global spouse, happiness, is_spouse, money, debt, currency, compliments, insults, spend_time, gender, intel
        div()
        print(f"{spouse.name}")
        if spouse.lvl == 1:
            if spouse.gender == 1:
                print("Girlfriend")
            else:
                print("Boyfriend")
        elif spouse.lvl == 2:
            if spouse.gender == 1:
                print("Wife")
            else:
                print("Husband")
        print(f"Age: {spouse.age}")
        div()
        print(
            "Smarts      :", pbar2(spouse.intel), str((int(spouse.intel * 100))) + "%"
        )
        print(
            "Looks       :", pbar2(spouse.looks), str((int(spouse.looks * 100))) + "%"
        )
        print(
            "Craziness   :",
            pbar2(spouse.craziness),
            str(int(spouse.craziness * 100)) + "%",
        )
        div()
        print(f"Relationship:", pbar2(spouse.rel), f"{int(spouse.rel*100)}%")
        div()
        print("[0] Return")
        print("[1] Spend Time")
        print("[2] Compliment")
        print("[3] Conversation")
        if spouse.lvl == 1:
            print("[4] Break Up")
        else:
            print("[4] Divorce")
        print("[5] Insult")
        print("[6] Make Love")
        print("[x] Movies")
        if spouse.lvl == 1:
            print(f"[8] Marriage [{currency}75,000]")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 1:
            div()
            print(f"You took {spouse.name} {choice(spend_time)}.")
            spouse.rel += 0.25
            if goto == 1:
                uni()
            else:
                adult()
        elif ch == 6:
            div()
            print("You made love with your spouse.")
            print("Your enjoyment :", pbar2(rng(1, 100) / 100))
            print("Their enjoyment:", pbar2(rng(1, 100) / 100))
            div()
            if is_fertile == 1:
                spouse.rel += 0.55
                happiness += 0.55
                if child_count < 8:
                    if spouse.pregnant == 0:
                        if (
                            gender == 0
                            and spouse.gender == 1
                            or gender == 1
                            and spouse.gender == 0
                        ):
                            spouse.pregnant = 1
                            if gender == 0:
                                print("Your spouse is pregnant with your child!")
                            else:
                                print("You are pregnant with your child!")
                        else:
                            adult()
                else:
                    print("You can only have [8] children.")
                if goto == 1:
                    uni()
                else:
                    adult()
            else:
                spouse.rel += 0.55
                happiness += 0.55
                if goto == 1:
                    uni()
                else:
                    adult()
        elif ch == 2:
            div()
            print(f"You called your spouse {choice(compliments)}!")
            happiness += 0.25
            spouse.rel += 0.25
            if spouse.rel > 0.75:
                print(f"Your spouse called you {choice(compliments)}!")
                happiness += 0.45
            if goto == 1:
                uni()
            else:
                adult()
        elif ch == 8 and spouse.lvl == 1:
            div()
            if spouse.rel >= 0.75:
                if money >= 75000:
                    money -= 75000
                else:
                    debt += 75000
                print("You married your spouse!")
                spouse.lvl = 2
                spouse.rel = 1
                money += spouse.fortune
                if goto == 1:
                    uni()
                else:
                    adult()
            else:
                print("Your spouse refused to marry you.")
                if spouse.rel <= 0.25:
                    print(
                        f"On the way out of the room, they called you {choice(insults)}."
                    )
                if goto == 1:
                    uni()
                else:
                    adult()

        elif ch == 3:
            argument_chance = rng(1, 4)
            if argument_chance == 1:
                div()
                print(f"You had a conversation about {choice(debates)}.")
                print("Agreement: ", pbar2(0))
                spouse.rel -= 0.45
                happiness -= 0.55
                div()
                print("Your conversation soon turns into a shouting match.")
                div()
                print("[1] Agree to disagree")
                print("[2] Ghost your spouse.")
                print("[3] Make a compromise with the agreement.")
                div()
                try:
                    ch = int(input(">"))
                except:
                    ch = 1
                if ch == 1:
                    spouse.rel += 0.2
                    happiness += 0.2
                elif ch == 2:
                    spouse.rel -= 0.45
                    happiness -= 0.55
                elif ch == 3:
                    spouse.rel += 0.4
                    happiness += 0.5
                if goto == 1:
                    uni()
                else:
                    adult()
            else:
                div()
                print(f"You had a conversation about {choice(debates)}.")
                print("Agreement: ", pbar2(0.75))
                spouse.rel += 0.25
                happiness += 0.45
                intel += 0.25
                if goto == 1:
                    uni()
                else:
                    adult()
        elif ch == 4:
            if spouse.lvl == 1:
                div()
                print("You broke up with your spouse.")
                is_spouse = 0
                del spouse
                if goto == 1:
                    uni()
                else:
                    adult()
            elif spouse.lvl == 2:
                div()
                print("You divorced your spouse.")
                money -= int(spouse.fortune / 2)
                is_spouse = 0
                del spouse
                if goto == 1:
                    uni()
                else:
                    adult()
            else:
                spouse_interact()
        elif ch == 5:
            div()
            print(f"You called your spouse {choice(insults)}!")
            spouse.rel -= 0.55
            if spouse.rel < 0.25:
                print(f"Your spouse called you {choice(insults)}!")
                spouse.rel -= 0.25
                happiness -= 0.85
            if goto == 1:
                uni()
            else:
                adult()
        else:
            if goto == 1:
                uni()
            else:
                adult()

    def pickname(gender):
        global forename_m, forename_f, surnames
        from random import choice

        if gender == 0:
            n1 = choice(forename_m)
            n2 = choice(surnames)
            n = n1 + " " + n2
            return n
        else:
            n1 = choice(forename_f)
            n2 = choice(surnames)
            n = n1 + " " + n2
            return n

    def dating_app(opposite):
        global gender, age, spouse, is_spouse, surnames, money, debt
        if opposite == 1:
            if gender == 0:
                gg = 1
            else:
                gg = 0
        else:
            gg = gender
        if money >=100:
            money -= 100
        else:
            debt += 100
        div()
        print("[1] 18-21")
        print("[2] 22-24")
        print("[3] 25-29")
        print("[4] 30-34")
        print("[5] 35-39")
        print("[6] 40-44")
        print("[7] 45-49")
        print("[8] 50-54")
        print("[9] 55-59")
        print("[10] 60-64")
        print("[11] 65-69")
        print("[12] 70+")
        div()
        try:
            ch = int(input(">"))
        except:
            adult()
        if ch == 1:
            rang = [18, 21]
        elif ch == 2:
            rang = [22, 24]
        elif ch == 3:
            rang = [25, 29]
        elif ch == 4:
            rang = [30, 34]
        elif ch == 5:
            rang = [35, 39]
        elif ch == 6:
            rang = [40, 44]
        elif ch == 7:
            rang = [45, 49]
        elif ch == 8:
            rang = [45, 49]
        elif ch == 9:
            rang = [50, 54]
        elif ch == 10:
            rang = [55, 59]
        elif ch == 11:
            rang = [65, 69]
        elif ch == 12:
            rang = [70, 99]
        else:
            rang = [(age - 3), (age + 3)]
        div()
        spouse = SpouseDatingApp(pickname(gg), 0.75, 1, age, gg, rng(rang[0], rang[1]))
        print(f"Name: {spouse.name}")
        print(f"Age: {spouse.age}")
        div()
        print("Smarts   :", pbar2(spouse.intel))
        print("Looks    :", pbar2(spouse.looks))
        print("Craziness:", pbar2(spouse.craziness))
        div()
        print("[1] Ask on date")
        print(f"[2] Find another [{currency}100]")
        print("[0] Ignore")
        div()
        try:
            ch = int(input(">"))
        except:
            return False
        if ch == 1:
            return spouse
        elif ch == 2:
            dating_app(opposite)
        else:
            return False

    def find_love(opposite):
        # def compile(self, name, relation, relationship_level, gender):
        global age, spouse, surnames, gender
        div()
        if opposite == 1:
            if gender == 0:
                gg = 1
            else:
                gg = 0
        else:
            gg = gender
        if gg == 1:
            print("While at the gym, a woman asks you out.")
        else:
            print("While at the gym, a man asks you out.")
        spouse = Spouse()
        spouse.compile(pickname(gg), (rng(50, 75) / 100), 1, gg)
        print(f"Name: {spouse.name}")
        print(f"Age: {spouse.age}")
        div()
        print("Smarts   :", pbar2(spouse.intel))
        print("Looks    :", pbar2(spouse.looks))
        print("Craziness:", pbar2(spouse.craziness))
        div()
        print("[1] Ask on date")
        print("[2] Find another")
        print("[0] Ignore")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 1:
            return spouse
        elif ch == 2:
            find_love(1)
        else:
            return False

    def pension_questions():
        per = rng(1, 4)
        if per == 1:
            print("Why do you want to leave?")
            div()
            print("[1] I would've quit.")
            print("[2] I'm tired of work.")
            print("[3] I have put enough effort into my job already.")
            print("[4] I deserve a break.")
            try:
                ch = int(input(">"))
            except:
                pass
            return True
        if per == 2:
            print("What will you do once you retire?")
            div()
            print("[1] Die.")
            print("[2] Go on permanent holiday.")
            print("[3] Go to another job.")
            print("[4] I don't want to think about it.")
            try:
                ch = int(input(">"))
            except:
                pass
            return True
        if per == 3:
            print("How was working at our company?")
            div()
            print("[1] It was great!")
            print("[2] Average.")
            print("[3] It was shit. I'm glad to go, dickhead")
            print("[4] No comment.")
            try:
                ch = int(input(">"))
            except:
                pass
            return True
        if per == 4:
            print(
                "Are you actually willing to lose your salary for what is essentially a holiday?"
            )
            div()
            print("[1] I wanted to do this from the start.")
            print("[2] I had no choice.")
            print("[3] I deserve a break.")
            try:
                ch = int(input(">"))
            except:
                pass
            return True

    def fake_id_hub():
        global debt, savings, money, currency
        print("[0] Return")
        print("[x] Casino")
        print("[2] Lottery")
        print("[3] Loan")
        print("[4] Access Savings Account")
        print('[5] "Club"')
        try:
            ch = int(input(">"))
        except:
            ch == 0
        if ch == 0:
            teen()
        elif ch == 2:
            lottery(1)
        elif ch == 3:
            try:
                d = int(input("How much to borrow? [Max 10k]>"))
            except:
                d = 0
            if debt >= 10000:
                adult()
            if d > 10000:
                d = 10000
            debt += d
            money += d
            teen()
        elif ch == 4:
            print(f"Savings: {currency}{savings}")
            print("[0] Return")
            print("[1] Take Out Savings")
            try:
                ch = int(input(">"))
            except:
                teen()
            if ch == 1:
                money += savings
                savings = 0
            else:
                teen
            teen()
        else:
            teen()

    def oll_to_oll2():
        global allow_debug, did_tutor, degree, is_spouse, spouse, part_time_salary, friend_1, friend_2, friend_3, friend_count, fame, is_wpp, wpp_name, sentence, prison_years, juvie_years
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary, mother_rel, father_rel, house_count, house_1, house_2, house_3
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age, salary, hours, job_id, gender
        div()
        print("OLL To Alpha 12 Converter")
        div()
        print("Available saves:")
        path = os.getcwd()
        dirlist = os.listdir(path)
        for item in dirlist:
            isFile = os.path.isfile(item)
            if isFile == True and item.endswith(".oll"):
                item = item.replace(".oll", "")
                print(item)
            else:
                continue
        # try:
        div()
        sn = input("Enter File Name >")
        # Windows illegal filename characters removed
        sn = sn.replace("\\", "")
        sn = sn.replace("/", "")
        sn = sn.replace("?", "")
        sn = sn.replace("*", "")
        sn = sn.replace("|", "")
        sn = sn.replace("<", "")
        sn = sn.replace(">", "")
        sn = sn.replace(":", "")
        sn = sn.replace('"', "")
        sn2 = sn
        sn += ".oll"  # file extension
        sn2 += ".oll2"
        try:
            f = open(sn, "rb")
        except:
            div()
            print("FileError: Could not open file.")
            mainmenu()
        import codecs

        ssave = f.read()
        f.close()

        try:
            ssave = codecs.decode(ssave, "base64_codec")
            ssave = ssave.decode("utf-8")
            ssave = ssave.split("|")
            save = ssave
        except:
            print("FileError: File not base64-encoded")
            mainmenu()
        # save=forename+"|"+surname+"|"+str(age)+"|"+str(happiness)+"|"
        # +str(looks)+"|"+str(health)+"|"+str(ethics)+"|"+str(intel)+"|
        # +str(mother_rel)+"|"+str(father_rel)+str(money)+"|"+
        # mother_name+"|"+father_name+"|"+str(mother_age)+"|"+str(father_age)
        try:
            s0 = save[0]
            s1 = save[1]
            s2 = save[2]
            s3 = save[3]
            s4 = save[4]
            s5 = save[5]
            s6 = save[6]
            s7 = save[7]
            s8 = save[8]
            s9 = save[9]
            s10 = save[10]
            s11 = save[11]
            s12 = save[12]
            s13 = save[13]
            s14 = str(int(save[12]) + 5)
            s15 = str(int(save[13]) + 6)
        except:
            print("FileError: File not compatible.")
            mainmenu()
        """
        save= (
            forename #0
            +"|"
            +surname #1
            +"|"
            +str(age)#2
            +"|"
            +str(happiness)#3
            +"|"
            +str(looks)#4
            +"|"
            +str(health)#5
            +"|"
            +str(ethics)#6
            +"|"
            +str(intel)#7
            +"|"
            +str(mother_rel)#8
            +"|"
            +str(father_rel)#9
            +str(money)
            +"|"
            +mother_name#10
            +"|"
            +father_name#11
            +"|"
            +str(mother_age)#12
            +"|"
            +str(father_age)#13

        )
        """
        new_save = [
            "Alpha",
            "12",
            s3,
            s5,
            s7,
            s4,
            s6,
            "0",
            s0,
            s1,
            s2,
            "0",
            "1",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "2022",
            "0",
            "0",
            s10,
            s11,
            s12,
            s13,
            s14,
            s15,
            "1",
            "0.75",
            "0.75",
        ]
        ns2 = ""
        for item in new_save:
            ns2 += str(item)
            ns2 += "|"
        new_save = ns2
        save = ns2
        import codecs

        save = save.encode("utf-8")
        save = codecs.encode(save, "base64_codec")
        f = open(sn2, "wb")
        f.write(save)
        f.close()
        print("Saved as", sn2)
        br()
        div()
        mainmenu()

    def save_game():
        import pickle
        global money, pistol_count, knife_count, is_common_cold, flip_profits, research_lab, pending_research
        global is_smartphone, pistol_ammo, chainsaw_count, taser_count, lottery_wins
        global channel_name, subscribers, view_count, video_count, is_verif, is_opentube
        global money, is_monetised, watch_time, opentube_year, forename, surname
        global allow_debug, spouse, is_spouse, gender, friend_count, friend_1, friend_2, friend_3, is_wpp, wpp_name, fame, sentence, prison_years, juvie_years
        global child_count, child_1, child_2, child_3, child_4, child_5, child_6, child_7, child_8
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary, house_count, house_1, house_2, house_3
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age, mother_rel, father_rel, driver_license, boat_license, gun_license, pilot_license
        print("Save Game")
        div()
        print("Saves that are already taken:")
        path = os.getcwd()
        dirlist = os.listdir(path)
        for item in dirlist:
            isFile = os.path.isfile(item)
            if isFile == True and item.endswith(".oll2"):
                item = item.replace(".oll2", "")
                print(item)
        div()

        tsn = input("Enter File Name >")
        sn = "" + tsn
        # Windows illegal filename characters removed
        sn = sn.replace("\\", "")
        sn = sn.replace("/", "")
        sn = sn.replace("?", "")
        sn = sn.replace("*", "")
        sn = sn.replace("|", "")
        sn = sn.replace("<", "")
        sn = sn.replace(">", "")
        sn = sn.replace(":", "")
        sn = sn.replace('"', "")
        sn += ".oll2"  # filename extension
        if sn == "":
            from time import ctime

            sn = ctime()
            sn = sn.replace(":", "-")
            sn = sn.replace(" ", "_")
        if is_opentube == 0:
            opentube_year = 1
            is_verif = 0
            is_monetised = 0
            watch_time = 0
            channel_name = "No Channel"
            video_count, view_count, subscribers = 0, 0, 0
        if is_wpp == 0:
            wpp_name = ["[N/A]", "[N/A]"]
        if is_spouse == 0:
            spouse = Spouse()
        if friend_count == 0:
            friend_1 = Friend()
            friend_2 = Friend()
            friend_3 = Friend()
        elif friend_count == 1:
            friend_1 = Friend()
            friend_2 = Friend()
        elif friend_count == 2:
            friend_3 = Friend()
        if child_count == 0:
            child_1 = Child(1)
            child_2 = Child(2)
            child_3 = Child(3)
            child_4 = Child(4)
            child_5 = Child(5)
            child_6 = Child(6)
            child_7 = Child(7)
            child_8 = Child(8)
        elif child_count == 1:
            child_2 = Child(2)
            child_3 = Child(3)
            child_4 = Child(4)
            child_5 = Child(5)
            child_6 = Child(6)
            child_7 = Child(7)
            child_8 = Child(8)
        elif child_count == 2:
            child_3 = Child(3)
            child_4 = Child(4)
            child_5 = Child(5)
            child_6 = Child(6)
            child_7 = Child(7)
            child_8 = Child(8)
        elif child_count == 3:
            child_4 = Child(4)
            child_5 = Child(5)
            child_6 = Child(6)
            child_7 = Child(7)
            child_8 = Child(8)
        elif child_count == 4:
            child_5 = Child(5)
            child_6 = Child(6)
            child_7 = Child(7)
            child_8 = Child(8)
        elif child_count == 5:
            child_6 = Child(6)
            child_7 = Child(7)
            child_8 = Child(8)
        elif child_count == 6:
            child_7 = Child(7)
            child_8 = Child(8)
        elif child_count == 7:
            child_8 = Child(8)
        import base64
        ps = pickle.dumps(children)
        s = base64.b64encode(ps).decode('ascii')
        ps2=pickle.dumps(vehicles)
        s2 =base64.b64encode(ps2).decode('ascii')
        ps3 = pickle.dumps(spouse)
        s3 = base64.b64encode(ps3).decode('ascii')
        th = pickle.dumps(houses)
        th=base64.b64encode(th).decode("ascii")
        save = (
            "Alpha|17|"
            + str(happiness)
            + "|"
            + str(health)
            + "|"
            + str(intel)
            + "|"
            + str(looks)
            + "|"
            + str(ethics)
            + "|"
            + str(money)
            + "|"
            + forename
            + "|"
            + surname
            + "|"
            + str(age)
            + "|"
            + str(work_e)
            + "|"
            + str(edu_lvl)
            + "|"
            + str(work_e_base)
            + "|"
            + str(promo_base)
            + "|"
            + str(degree)
            + "|"
            + str(hours)
            + "|"
            + str(salary)
            + "|"
            + str(expenses)
            + "|"
            + str(pension)
            + "|"
            + str(is_depressed)
            + "|"
            + str(debt)
            + "|"
            + str(savings)
            + "|"
            + str(year)
            + "|"
            + str(is_job)
            + "|"
            + str(stress)
            + "|"
            + mother_name
            + "|"
            + father_name
            + "|"
            + str(mother_age)
            + "|"
            + str(father_age)
            + "|"
            + str(mother_end_age)
            + "|"
            + str(father_end_age)
            + "|"
            + str(did_tutor)
            + "|"
            + str(mother_rel)
            + "|"
            + str(father_rel)
            + "|"
            + str(is_spouse)
            + "|"
            + str(s3)
            + "|"
            + str(0)
            + "|"
            + str(0)
            + "|"
            + str(0)
            + "|"
            + str(0)
            + "|"
            + str(enemy_gang_rel)
            + "|"
            + str(enemy_gang_lead)
            + "|"
            + enemy_gang_name
            + "|"
            + str(part_time_salary)
            + "|"
            + str(teen_hours)
            + "|"
            + str(teen_salary)  # 46
            + "|"
            + str(spouse.intel)  # 47
            + "|"
            + str(spouse.looks)  # 48
            + "|"
            + str(spouse.craziness)  # 49
            + "|"
            + str(job_id)  # 50
            + "|"
            + str(spouse.gender)  # 51
            + "|"
            + str(gender)  # 52
            + "|"
            + str(spouse.fortune)  # 53
            + "|"
            + str(friend_count)  # 54
            + "|"
            + str(friend_1.name)  # 55
            + "|"
            + str(friend_1.age)  # 56
            + "|"
            + str(friend_1.gender)  # 57
            + "|"
            + str(friend_1.intel)  # 58
            + "|"
            + str(friend_1.looks)  # 59
            + "|"
            + str(friend_1.craziness)  # 60
            + "|"
            + str(friend_1.end)  # 61
            + "|"
            + str(friend_1.rel)  # 62
            + "|"
            + str(friend_2.name)  # 63
            + "|"
            + str(friend_2.age)  # 64
            + "|"
            + str(friend_2.gender)  # 65
            + "|"
            + str(friend_2.intel)  # 66
            + "|"
            + str(friend_2.looks)  # 67
            + "|"
            + str(friend_2.craziness)  # 68
            + "|"
            + str(friend_2.end)  # 69
            + "|"
            + str(friend_2.rel)  # 70
            + "|"
            + str(friend_3.name)  # 71
            + "|"
            + str(friend_3.age)  # 72
            + "|"
            + str(friend_3.gender)  # 73
            + "|"
            + str(friend_3.intel)  # 74
            + "|"
            + str(friend_3.looks)  # 75
            + "|"
            + str(friend_3.craziness)  # 76
            + "|"
            + str(friend_3.end)  # 77
            + "|"
            + str(friend_3.rel)  # 78
            + "|"
            + str(fame)  # 79
            + "|"
            + str(is_wpp)  # 80
            + "|"
            + str(wpp_name[0])  # 81
            + "|"
            + wpp_name[1]  # 82
            + "|"
            + str(sentence)  # 83
            + "|"
            + str(prison_years)  # 84
            + "|"
            + str(juvie_years)  # 85
            + "|0|" # Challenge ID which was last solved
            + th
            + "|"
            + str("|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0")
            + "|"
            + s  # 106
            + "|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0"
            + str(child_8.craziness)  # 169
            + "|"
            + str(is_opentube)  # 170
            + "|"
            + str(opentube_year)  # 171
            + "|"
            + str(is_verif)  # 172
            + "|"
            + str(is_monetised)  # 173
            + "|"
            + str(watch_time)  # 174
            + "|"
            + str(channel_name)  # 175
            + "|"
            + str(subscribers)  # 176
            + "|"
            + str(video_count)  # 177
            + "|"
            + str(view_count)  # 178
            + "|"
            + str(opentube_year)  # 179
            + "|"
            + str(pistol_count)  # 180
            + "|"
            + str(knife_count)  # 181
            + "|"
            + str(is_smartphone)  # 182
            + "|"
            + str(pistol_ammo)  # 183
            + "|"
            + str(chainsaw_count)  # 184
            + "|"
            + str(taser_count)  # 185
            + "|"
            + str(is_common_cold)  # 186
            + "|"
            + str(child_count)  # 187
            + "|"
            + str(flip_profits)  # 188
            + "|"
            + str("0|0|0")
            + "|"
            + str(lottery_wins)  # 192
            + "|"
            # driver_license, boat_license, gun_license, pilot_license
            + str(driver_license) # 193
            + "|"
            + str(boat_license) # 194
            + "|"
            + str(gun_license) # 195
            + "|"
            + str(pilot_license) # 196
            + "|"
            + str(research_lab[0]) # 197
            + "|"
            + str(research_lab[1]) # 198
            + "|"
            + str(research_lab[2]) # 199
            + "|"
            + str(research_lab[3]) # 200
            + "|"
            + str(research_lab[4]) # 201
            + "|"
            + str(pending_research[0]) # 202
            + "|"
            + str(pending_research[1]) # 203
            + "|"
            + s2
        ) 
        if allow_debug == 2:
            print(save)
            div()
        import codecs

        save = save.encode("utf-7")
        save = codecs.encode(save, "base64_codec")
        f = open(sn, "wb")
        f.write(save)
        f.close()
        print("Saved as", sn)
        br()
        div()
        return True

    def load_game(sn=""):
        print("Save Game not working :(")
        print("I will not fix it.")
        br()
        mainmenu()
        check_version = ["Alpha", "17"]
        import pickle
        import base64
        global money, pistol_count, knife_count, is_common_cold, driver_license, boat_license, gun_license, pilot_license
        global is_smartphone, pistol_ammo, chainsaw_count, taser_count, research_lab, pending_research
        global channel_name, subscribers, view_count, video_count, is_verif, is_opentube
        global money, is_monetised, watch_time, opentube_year, forename, surname, children, houses
        global allow_debug, spouse, is_spouse, gender, friend_count, friend_1, friend_2, friend_3, is_wpp, wpp_name, fame, sentence, prison_years, juvie_years
        global child_count, child_1, child_2, child_3, child_4, child_5, child_6, child_7, child_8
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary, house_count, house_1, house_2, house_3
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age, mother_rel, father_rel
        if sn == "":
            print("Load Game")
            div()
            print("Available saves:")
            path = os.getcwd()
            dirlist = os.listdir(path)
            for item in dirlist:
                isFile = os.path.isfile(item)
                if isFile == True and item.endswith(".oll2"):
                    item = item.replace(".oll2", "")
                    print(item)
                else:
                    continue
            # try:
            div()
            # 0=Alpha|1=12|2=happiness|3=health|4=intel|5=looks|6=ethics|7=money
            # |8=forename|9=surname|10=age|11=work_e|12=edu_lvl|13=work_e_base|14=promo_base
            # |15=degree|16=hours|17=salary|18=expenses|19=pension
            # |20=is_depressed|21=debt|22=savings|23=year|24=is_job|25=stress
            # |26=mother_name|27=father_name|28=mother_age|29=father_age
            # |30=mother_end_age|31=father_end_age
            sn = input("Enter File Name >")
        # Windows illegal filename characters removed
        sn = sn.replace("\\", "")
        sn = sn.replace("/", "")
        sn = sn.replace("?", "")
        sn = sn.replace("*", "")
        sn = sn.replace("|", "")
        sn = sn.replace("<", "")
        sn = sn.replace(">", "")
        sn = sn.replace(":", "")
        sn = sn.replace('"', "")
        sn += ".oll2"  # file extension
        try:
            f = open(sn, "rb")
        except:
            div()
            print("An error occured.")
            mainmenu()
        import codecs

        ssave = f.read()
        f.close()

        ssave = codecs.decode(ssave, "base64_codec")
        ssave = ssave.decode("utf-7")
        ssave = ssave.split("|")
        save = ssave
        if allow_debug != 0:
            print(save)
        if save[0] == check_version[0] and save[1] == check_version[1]:
            happiness = float(save[2])
            health = float(save[3])
            intel = float(save[4])
            looks = float(save[5])
            ethics = float(save[6])
            money = int(save[7])
            forename = save[8]
            surname = save[9]
            age = int(save[10])
            work_e = int(save[11])
            edu_lvl = int(save[12])
            work_e_base = int(save[13])
            promo_base = int(save[14])
            is_depressed = int(save[15])
            debt = int(save[16])
            savings = int(save[17])
            expenses = int(save[18])
            pension = float(save[19])
            pension = int(pension)
            is_depressed = int(save[20])
            debt = int(float(save[21]))
            try:
                savings = int(save[22])
            except:
                savings = float(save[22])
                savings = int(savings)
            year = int(save[23])
            is_job = int(save[24])
            stress = float(save[25])
            mother_name = save[26]
            father_name = save[27]
            mother_age = int(save[28])
            father_age = int(save[29])
            mother_end_age = int(save[30])
            father_end_age = int(save[31])
            did_tutor = int(save[32])
            mother_rel = float(save[33])
            father_rel = float(save[34])
            is_spouse = int(save[35])
            ps = save[36]
            spouse = pickle.loads(base64.b64decode(ps))
            enemy_gang_rel = float(save[41])
            enemy_gang_lead = float(save[42])
            enemy_gang_name = save[43]
            part_time_salary = int(save[44])
            teen_hours = int(save[45])
            teen_salary = int(save[46])
            job_id = int(save[50])
            gender = int(save[52])
            friend_count = int(save[54])
            child_1 = Child()
            child_2 = Child()
            child_3 = Child()
            child_4 = Child()
            child_5 = Child()
            child_6 = Child()
            child_7 = Child()
            child_8 = Child()
            friend_1 = FriendRecompile(
                save[55],
                int(save[56]),
                int(save[57]),
                float(save[58]),
                float(save[59]),
                float(save[60]),
                int(save[61]),
                float(save[62]),
            )
            friend_2 = FriendRecompile(
                save[63],
                int(save[64]),
                int(save[65]),
                float(save[66]),
                float(save[67]),
                float(save[68]),
                int(save[69]),
                float(save[70]),
            )
            friend_3 = FriendRecompile(
                save[71],
                int(save[72]),
                int(save[73]),
                float(save[74]),
                float(save[75]),
                float(save[76]),
                int(save[77]),
                float(save[78]),
            )
            fame = int(save[79])
            is_wpp = int(save[80])
            wpp_name = [save[81], save[82]]
            sentence = int(save[83])
            prison_years = int(save[84])
            juvie_years = int(save[85])
            try:
                houses = pickle.loads(base64.b64decode(save[86]))
            except:
                print("Failed to load houses. House value will be blank.")
                houses=[]
                br()
            s = save[106]
            s2 = save[104]
            children = pickle.loads(base64.b64decode(s))
            vehicles = pickle.loads(base64.b64decode(s2))
            is_opentube = int(save[170])
            opentube_year = int(save[171])
            is_verif = int(save[172])
            is_monetised = int(save[173])
            watch_time = int(save[174])
            channel_name = save[175]
            subscribers = int(save[176])
            video_count = int(save[177])
            view_count = int(save[178])
            opentube_year = int(save[179])

            pistol_count = int(save[180])
            knife_count = int(save[181])
            is_smartphone = int(save[182])
            pistol_ammo = int(save[183])
            chainsaw_count = int(save[184])
            taser_count = int(save[185])
            is_common_cold = int(save[186])
            child_count = int(save[186])
            flip_profits = int(save[187])
            driver_license = int(save[193])
            boat_license = int(save[194])
            gun_license = int(save[195])
            pilot_license = int(save[196])
            research_lab = [int(save[197]),int(save[198]),int(save[199]),int(save[200]),int(save[201])]
            pending_research = [int(save[202]),int(save[203])]
            div()
            print("Successfully loaded life.")
            adult()
        elif save[0] == "Alpha" and save[1] == "12.x":
            div()
            print("The save file cannot be loaded.")
            print("It has been converted from Alpha 11 to Alpha 12.4 using the OOCU.")
            print(
                "Due to some form of conflict, there is no upgrade utility to upgrade OOCU save files to Alpha 13."
            )
            print(
                "As a result, you can only load this save in versions between Alpha 12.4 and Alpha 13 [not inclusive]."
            )
            print("Launch ALpha 12.4+ and try again.")
            print("We apolagise for the inconvenience. This will be resolved soon.")
            br()
            load_game()
        elif save[0] == "Alpha" and save[1] == "15":
            div()
            print("This save file is incompatible with", game_name + ".")
            print("In order to play, you need to convert it to a supported format.")
            print(
                "You can do this automatically, but this will [sadly] require adding default data."
            )
            print(
                "Also, you will not be able to play this save on that older version of",
                game_name,
            )
            div()
            print(f"Note: Your save file will be backed up to `{sn[:-5]}.bak`.")
            div()
            print("[0] Cancel to Main Menu")
            print("[1] Convert")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1:
                load_a15(sn)
            else:
                mainmenu()
        elif save[0] == "Alpha" and save[1] == "14":
            div()
            print("This save file is incompatible with", game_name + ".")
            print("In order to play, you need to convert it to a supported format.")
            print(
                "You can do this automatically, but this will [sadly] require adding default data."
            )
            print(
                "Also, you will not be able to play this save on that older version of",
                game_name,
            )
            div()
            print(f"Note: Your save file will be backed up to `{sn[:-5]}.bak`.")
            div()
            print("[0] Cancel to Main Menu")
            print("[1] Convert")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1:
                load_game_a14(sn)
            else:
                mainmenu()
        elif save[0] == "Alpha" and save[1] == "12":
            div()
            print("This save file is incompatible with", game_name + ".")
            print("In order to play, you need to convert it to a supported format.")
            print(
                "You can do this automatically, but this will [sadly] require adding default data."
            )
            print(
                "Also, you will not be able to play this save on that older version of",
                game_name,
            )
            div()
            print(f"Note: Your save file will be backed up to `{sn[:-5]}.bak`.")
            div()
            print("[0] Cancel to Main Menu")
            print("[1] Convert")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1:
                load_game_a12(sn)
            else:
                mainmenu()
        elif save[0] == "Alpha" and save[1] == "13":
            div()
            print("This save file is incompatible with", game_name + ".")
            print("In order to play, you need to convert it to a supported format.")
            print(
                "You can do this automatically, but this will [sadly] require adding default data."
            )
            print(
                "Also, you will not be able to play this save on that older version of",
                game_name,
            )
            div()
            print(f"Note: Your save file will be backed up to `{sn[:-5]}.bak`.")
            div()
            print("[0] Cancel to Main Menu")
            print("[1] Convert")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1:
                load_game_a13(sn)
            else:
                mainmenu()
        else:
            if allow_debug == 1:
                print(save)
            print(f"This save is incompatible with {game_name}.")
            print(f"Expected Version: {check_version[0]} {check_version[1]}")
            try:
                print(f"Got version:{save[0]} {save[1]}")
            except:
                print("Got version: N/A")
            br()
            mainmenu()

    def encode_save():
        # this INTERNAL function base64 encodes a plaintext save, for revsersing what a backwards compatible conversion did.
        save = [
            "Alpha",
            "12",
            "0.96",
            "0.8000000000000002",
            "0.15999999999999998",
            "1",
            "1",
            "104432268",
            "Rick",
            "Astley",
            "69",
            "22",
            "2",
            "0",
            "22",
            "9",
            "0",
            "0",
            "0",
            "57200.0",
            "0",
            "0",
            "0",
            "2087",
            "0",
            "0.65",
            "Hedda Astley",
            "Emerson Astley",
            "101",
            "106",
            "86",
            "86",
        ]
        base = ""
        for item in save:
            base += item
            base += ""
        print(base)
        br()

    def load_a15(sn):
        print("Convert Save [A15] --> [A16]")
        # load stage
        div()
        f = open(sn, "rb")
        ssave = f.read()
        f.close()
        print(ssave)
        f = open(sn + ".bak", "wb")
        f.write(ssave)
        f.close()
        div()
        print("Backed up as", sn + ".bak")
        div()
        import codecs

        ssave = codecs.decode(ssave, "base64_codec")
        ssave = ssave.decode("utf-8")
        save = ssave
        # convert stage
        # save+="" [This is the part where it adds default stuff]
        save = save.split("|")
        print(save)
        save[0] = "Alpha"
        save[1] = "16"
        base = ""
        for item in save:
            base += item
            base += "|"
        l = len(base)
        base = base[: l - 1]
        print(base)
        base += "|0|0|0|0|0|0"
        save = base
        save = save.encode("utf-8")
        save = codecs.encode(save, "base64_codec")
        f = open(sn, "wb")
        f.write(save)
        f.close()
        print("Converted save successfully.")
        div()
        load_game(sn)

    def load_game_a14(sn):
        print("Convert Save [A14] --> [A15]")
        # load stage
        div()
        f = open(sn, "rb")
        ssave = f.read()
        f.close()
        print(ssave)
        f = open(sn + ".bak", "wb")
        f.write(ssave)
        f.close()
        div()
        print("Backed up as", sn + ".bak")
        div()
        import codecs

        ssave = codecs.decode(ssave, "base64_codec")
        ssave = ssave.decode("utf-8")
        save = ssave
        # convert stage
        # save+="" [This is the part where it adds default stuff]
        save = save.split("|")
        print(save)
        save[0] = "Alpha"
        save[1] = "15"
        base = ""
        for item in save:
            base += item
            base += "|"
        l = len(base)
        base = base[: l - 1]
        print(base)
        base += "|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|0|0|0|0|0|0|0|1|0|0|0|0|0|0|0|1|0|0|0|0|0|0|0|1|0|0|0|0|0|0|0|1|0|0|0|0|0|0|0|1|0|0|0|0|0|0|0|1|0|0|0|0|0|0|0|1|0|0|0|0|0|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0"
        save = base
        save = save.encode("utf-8")
        save = codecs.encode(save, "base64_codec")
        f = open(sn, "wb")
        f.write(save)
        f.close()
        print("Converted save successfully.")
        div()
        load_a15(sn)

    def load_game_a13(sn):
        global allow_debug, did_tutor
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary, mother_rel, father_rel
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age
        print("Convert Save [A13] --> [A14]")
        # load stage
        div()
        f = open(sn, "rb")
        ssave = f.read()
        f.close()
        print(ssave)
        f = open(sn + ".bak", "wb")
        f.write(ssave)
        f.close()
        div()
        print("Backed up as", sn + ".bak")
        div()
        import codecs

        ssave = codecs.decode(ssave, "base64_codec")
        ssave = ssave.decode("utf-8")
        save = ssave
        # convert stage
        # save+="" [This is the part where it adds default stuff]
        save = save.split("|")
        print(save)
        save[0] = "Alpha"
        save[1] = "14"
        base = ""
        for item in save:
            base += item
            base += "|"
        l = len(base)
        base = base[: l - 1]
        print(base)
        base += "|1|1|0|0|1|0|0|0|SGCU Friend #1|18|0|1|1|0|19|1|SGCU Friend #2|18|0|1|1|0|19|1|SGCU Friend #3|18|0|1|1|0|19|1|0|0|SGCU|MAN|0|0|0"
        save = base
        save = save.encode("utf-8")
        save = codecs.encode(save, "base64_codec")
        f = open(sn, "wb")
        f.write(save)
        f.close()
        print("Converted save successfully.")
        div()
        load_game_a14(sn)

    def load_game_a12(sn):
        global allow_debug, did_tutor
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary, mother_rel, father_rel
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age
        print("Convert Save [A12] --> [A13]")
        # load stage
        div()
        f = open(sn, "rb")
        ssave = f.read()
        f.close()
        print(ssave)
        f = open(sn + ".bak", "wb")
        f.write(ssave)
        f.close()
        div()
        print("Backed up as", sn + ".bak")
        div()
        import codecs

        ssave = codecs.decode(ssave, "base64_codec")
        ssave = ssave.decode("utf-8")
        save = ssave
        # convert stage
        # save+="" [This is the part where it adds default stuff]
        save = save.split("|")
        print(save)
        save[0] = "Alpha"
        save[1] = "13"
        base = ""
        for item in save:
            base += item
            base += "|"
        l = len(base)
        base = base[: l - 1]
        base += "|1|0.75|0.75|0|SGCU Converted Imaginary Girlfriend|0|0|0|0|0|0|[PLACEHOLDER]|0|0|0"
        save = base
        save = save.encode("utf-8")
        save = codecs.encode(save, "base64_codec")
        f = open(sn, "wb")
        f.write(save)
        f.close()
        print("Converted save successfully.")
        div()
        load_game_a13(sn)

    def casino_menu():
        global money, winnings, currency
        losses = -(winnings)
        div()
        if winnings < 0:
            print(f"Session Losses:   {currency}{'{:,}'.format(losses)}")
        else:
            print(f"Session earnings: {currency}{'{:,}'.format(winnings)}")
        print(f"Money:            {currency}{money}")
        div()
        print("[1] Play")
        print("[0] Return")
        try:
            ch = int(input(">"))
        except:
            ch = 1
        if ch == 1:
            blackjack()
        else:
            adult()

    def job_centre():
        global edu_lvl, looks, salary, hours, is_job, job_id, currency
        div()
        print("These are all elegible jobs.")
        div()
        if edu_lvl >= 1:
            print(f"[1] Amazon Delivery Driver [{currency}5/h]")
        if edu_lvl >= 2 and degree == 11:
            print(f"[2] Jr Translator [{currency}10/h]")
        if edu_lvl >= 2 and degree == 5:
            print(f"[3] Jr Accountant [{currency}30/h]")
        print(f"[4] Exorcist [{currency}10/h]")
        if edu_lvl >= 2 and degree == 4:
            print(f"Teacher [{currency}20/h]")
        print("[x] Trainee Pilot")
        if edu_lvl >= 2 and degree == 3:
            print(f"[6] Jr Game Developer [{currency}40/h]")
        if edu_lvl >= 2 and degree == 32:
            print(f"[8] Jr Lawyer [{currency}60/h]")
        if edu_lvl >= 2 and degree == 3:
            print(f"[9] App Developer [{currency}45/h]")
        if edu_lvl >= 2 and degree == 1:
            print(f"[10] Jr Banker [{currency}45/h]")
        print(f"[11] Monk [{currency}15/h]")
        print(f"[12] Wedding Planner [{currency}25/h]")
        if edu_lvl >= 2 and degree == 9:
            print(f"[13] Engineer I [{currency}55/h]")
        if edu_lvl >= 2 and degree == 13:
            print(f"[14] Data Scientist [{currency}75/h]")
        if edu_lvl >= 1:
            print(f"[15] Private [Army] [{currency}35/h]")
        print("[x] Architect")
        if edu_lvl >= 1:
            print(f"[17] Cashier [{currency}10/h]")
        if edu_lvl >= 2 and degree == 4:
            print(f"[18] College Lecturer [{currency}45/h]")
        print(f"[19] OOhber Driver [{currency}15/h]")
        if edu_lvl >= 2 and degree == 2:
            print(f"[20] Editor [{currency}25/h]")
        if looks >= 0.8:
            print(f"[21] Exotic Dancer [{currency}15/h]")
        print(f"[22] Flight Attendant [{currency}25/h]")
        if edu_lvl >= 1:
            print(f"[23] Apprentice Hairdresser [{currency}25/h]")
        print("[x] Judge")
        if edu_lvl >= 1:
            print(f"[25] Librarian [{currency}25]")
        if edu_lvl >= 1:
            print(f"[26] Nun [{currency}10/h]")
        print("[x] Photographer")
        if edu_lvl >= 1 and looks >= 0.8:
            print(f"[28] P*rnographer [{currency}35/h]")
        if edu_lvl >= 2 and degree == 1:
            print(f"[29] Stockbroker [{currency}45/h]")
        if edu_lvl >= 2 and degree == 16:
            print(f"[30] Publicity Stuntperson [{currency}35/h]")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        job_id = ch
        if ch == 0:
            adult()
        elif ch == 1 and edu_lvl >= 1:
            if job_interview():
                salary = 5
                hours = 60
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 2 and edu_lvl >= 2 and degree == 11:
            if job_interview():
                salary = 10
                hours = 45
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 3 and edu_lvl >= 2 and degree == 5:
            if job_interview():
                salary = 30
                hours = 45
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 4:
            if job_interview():
                salary = 10
                hours = 40
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 5 and edu_lvl >= 2 and degree == 4:
            if job_interview():
                salary = 20
                hours = 55
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 6 >= 2 and degree == 3:
            if job_interview():
                salary = 40
                hours = 45
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 8 and degree == 32 and edu_lvl >= 2:
            if job_interview():
                salary = 60
                hours = 40
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
            print("You got the job.")
            generate_co_workers()
            br()
            adult()
        elif ch == 9 and edu_lvl >= 2 and degree == 3:
            if job_interview():
                salary = 45
                hours = 40
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 10 and degree == 1 and edu_lvl >= 2:
            if job_interview():
                salary = 45
                hours = 40
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 11:
            if job_interview():
                salary = 15
                hours = 40
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 12:
            if job_interview():
                salary = 25
                hours = 45
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 13 and edu_lvl >= 2 and degree == 9:
            if job_interview():
                salary = 55
                hours = 40
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 14 and edu_lvl >= 2 and degree == 13:
            if job_interview():
                salary = 75
                hours = 50
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 15 and edu_lvl >= 1:
            if job_interview():
                salary = 35
                hours = 40
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 17 and edu_lvl >= 1:
            if job_interview():
                salary = 10
                hours = 40
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 18 and edu_lvl >= 2 and degree == 4:
            if job_interview():
                salary = 45
                hours = 45
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 19:
            if job_interview():
                salary = 15
                hours = 60
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 20 and edu_lvl >= 2 and degree == 2:
            if job_interview():
                salary = 25
                hours = 40
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 21 and looks >= 0.8:
            if job_interview():
                salary = 15
                hours = 45
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 22:
            if job_interview():
                salary = 25
                hours = 40
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 23 and edu_lvl >= 1:
            if job_interview():
                salary = 25
                hours = 40
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 25 and edu_lvl >= 1:
            if job_interview():
                salary = 25
                hours = 40
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 26 and edu_lvl >= 1:
            if job_interview():
                salary = 10
                hours = 40
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 28 and edu_lvl >= 1 and looks >= 0.8:
            if job_interview():
                salary = 35
                hours = 40
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 29 and edu_lvl >= 2 and degree == 1:
            if job_interview():
                salary = 45
                hours = 35
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 30 and edu_lvl >= 2 and degree == 16:
            if job_interview():
                salary = 35
                hours = 40
                is_job = 1
                print("You got the job.")
                generate_co_workers()
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        else:
            job_id = 0
            adult()
        adult()
    def killMethod():
        global vehicles, taser_count, pistol_count, pistol_ammo
        div()
        print("[1] Drive-By")
        print("[x] Club To Death")
        print("[3] Taser")
        print("[4] Shootout")
        print("[5] Poison")
        print("[6] Elephant Laxative")
        print("[7] Scare To Death")
        print("[8] Atomic Wedgie")
        div()
        try:
            ch=int(input(">"))
        except:
            return False
        if ch == 1:
            if len(vehicles[0]) > 0:
                return True
            else:
                return False
        elif ch == 3:
            if taser_count > 0 and rng(1,100) <= 25:
                return True
            else:
                return False
        elif ch == 4:
            if pistol_count > 0 and pistol_ammo - 25 >= 0:
                return True
            else:
                return False
        elif ch == 5 or ch == 6:
            if rng(1,100) <= 5:
                return True
            else:
                return False
        elif ch == 7:
            return True
        elif ch == 8:
            if rng(1,100) <= 75:
                return True
            else:
                return False
        else:
            return False
    def murder():
        global mother_age, father_age, mother_end_age, father_end_age, is_spouse, spouse, offences, age, mother_name, father_name
        if mother_age < mother_end_age:
            print(f"[1] {mother_name} [Mother]")
        if father_age < father_end_age:
            print(f"[2] {father_name} [Father]")
        if is_spouse == 1 and spouse.end > spouse.age:
            print(f"[3] {spouse.name} [Spouse]")
        div()
        try:
            ch=int(input(">"))
        except:
            adult()
        if ch == 1 and mother_age < mother_end_age:
            if killMethod() == True and rng(1,100) <= 50:
                mother_end_age=mother_age + 1
                age -= 1
                age_up(0)
            else:
                print("You were caught!")
                offences += 15
                go_to_prison()
        elif ch == 2 and father_age < father_end_age:
            if killMethod() == True and rng(1,100) <= 50:
                father_end_age=father_age + 1
                age -= 1
                age_up(0)
            else:
                print("You were caught!")
                offences += 15
                go_to_prison()
        elif ch == 3 and is_spouse == 1 and spouse.end > spouse.age:
            if killMethod() == True and rng(1,100) <= 50:
                spouse.end=spouse.age
                age -= 1
                age_up()
            else:
                print("You were caught")
                offences += 20
                go_to_prison()
        else:
            adult()
    def adult_crime():
        global mother_age, age, spouse, is_spouse
        global father_age, offences, is_bandit
        global father_end_age, mother_end_age, money, currency
        print("[0] Return")
        print("[X] Bank Robbery")
        print("[x] Burglary")
        print("[3] GTA")
        print("[4] Hitman")
        print("[5] Murder")
        print("[6] Pickpocketing")
        print("[7] Shoplifting")
        print("[8] Train Robbery")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        elif ch == 3:
            steal_cars()
        elif ch == 5:
            murder()
        elif ch == 7:
            items=[["Gucci handbag",555],["perfume bottle",50],["Chromebook",659],["watch",6550],["carrot",1]]
            item=choice(items)
            div()
            print(f"You stole a {item[0]}.")
            print(f"You got {currency}{'{:,}'.format(item[1])} for it.")
            money += item[1]
            chance=rng(1,2)
            if chance == 2:
                print("You were caught!")
                money -= item[1]
                offences += 3
                go_to_prison()
            else:
                adult()
        elif ch == 4:
            print("[0] Return")
            if mother_age < mother_end_age:
                print(f"[1] Kill Mother [{currency}45,000]")
            if father_age < father_end_age:
                print(f"[2] Kill Father [{currency}45,000]")
            if is_spouse == 1:
                if spouse.end > spouse.age:
                    print(f"[3] Kill {spouse.name} [{currency}56,000]")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            elif ch == 1 and mother_age < mother_end_age:
                if money >= 45000:
                    chance = rng(1, 3)
                    if chance == 1 or chance == 2:
                        print("The hitman was actually an undercover cop!")
                        offences += 25
                        go_to_prison()
                        adult()
                    money -= 45000
                    mother_end_age = mother_age + 1
                    age -= 1
                    div()
                    age_up(0)
                elif money < 45000:
                    div()
                    print("Cannot afford.")
                    adult()
                else:
                    adult()
            elif ch == 2 and father_age < father_end_age:
                if money >= 45000:
                    chance = rng(1, 3)
                    if chance == 1 or chance == 2:
                        print("The hitman was actually an undercover cop!")
                        offences += 25
                        go_to_prison()
                        adult()
                    money -= 45000
                    father_end_age = father_age + 1
                    age -= 1
                    div()
                    age_up(0)
                elif money < 45000:
                    div()
                    print("Cannot afford.")
                    adult()
                else:
                    adult()
            elif ch == 3:
                if is_spouse == 1:
                    if spouse.end > spouse.age:
                        if money >= 56000:
                            chance = rng(1, 3)
                            if chance == 1 or chance == 2:
                                print("The hitman was actually an undercover cop!")
                                offences += 25
                                go_to_prison()
                                adult()
                            money -= 56000
                            div()
                            print("Your spouse was successfully hit.")
                            spouse.end = spouse.age + 1
                            age -= 1
                            age_up(0)
                        else:
                            div()
                            print("Cannot afford.")
                            adult()
                    else:
                        adult()
                else:
                    adult()

        elif ch == 6:
            from random import randint

            base = randint(15, 30)
            print(f"You stole {currency}" + str(base))
            money += base
            adult()
        elif ch == 7:
            print("[0] Return")
            print(f"[x] Phone [{currency}750]")
            print("[x] Beer")
            print("[x] Cigarettes")
            print("[x] Mars Candy Bar")
            print(f"[x] Handbag [{currency}250]")
            print(f"[x] Wallet [{currency}50]")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            else:
                adult()
        elif ch == 8:
            from time import strftime
            from random import randint

            winnings = randint(150, 300)
            winnings *= 100000
            base = strftime("%H:%M")
            print("Choose a time [Note: This should be the real-life time.")
            print("[1] 0:00 [Midnight]")
            print("[2] 07:00 [7AM]")
            print("[3] 12:00 [12AM]")
            print("[4] 16:20 [4:20PM]")
            print("[5] 19:00 [7PM]")
            print("[6] 21:00 [9PM]")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1:
                if base == "00:00":
                    div()
                    is_bandit = 1
                    print(f"You stole {currency}" + str(winnings))
                    money += winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 2:
                if base == "07:00":
                    div()
                    is_bandit = 1
                    print(f"You stole {currency}" + str(winnings))
                    money += winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 3:
                if base == "12:00":
                    div()
                    is_bandit = 1
                    print(f"You stole {currency}" + str(winnings))
                    money += winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 4:
                if base == "16:20":
                    div()
                    print(f"You stole {currency}" + str(winnings))
                    money += winnings
                    br()
                    adult()
                else:
                    is_bandit = 1
                    print("You tried to board the train but was unable to.")
            if ch == 5:
                if base == "19:00":
                    div()
                    print(f"You stole {currency}" + str(winnings))
                    money += winnings
                    br()
                    adult()
                else:
                    is_bandit = 1
                    print("You tried to board the train but was unable to.")
            if ch == 6:
                div()
                if base == "21:00":
                    is_bandit = 1
                    print(f"You stole {currency}" + str(winnings))
                    money += winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            else:
                adult()
        else:
            # Place more options on this indent level
            adult()

    def uni_activities():
        global uni_end_age
        global mother_age, father_age
        global mother_name, father_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel
        global money, is_depressed
        print("[0] Return")
        print("[1] Party")
        print("[2] Do Drugs")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            uni()
        elif ch == 1:
            print("You partied.")
            print("Enjoyment:")
            pbar(0.75)
            happiness += 0.45
            uni()
        elif ch == 2:
            div()
            print("Locked.")
            uni()
        else:
            uni()

    def uni_menu():
        global salary, hours, currency
        print("[1] University")
        print("[2] Part-Time Jobs")
        print("[x] Local Gangs")
        print("[0] Return")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            uni()
        elif ch == 1:
            div()
            print("[1] Drop Out")
            print("[0] Return")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                uni()
            elif ch == 1:
                div()
                print("You dropped out of Uni.")
                adult()
            else:
                uni()
        elif ch == 2:
            print(f"[1] Mall Santa [{currency}15/h] [10h]")
            print(f"[2] Lab Assistant [{currency}19/h] [15h]")
            print(f"[3] Receptionist [{currency}9/h] [22h]")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                uni()
            elif ch == 1:
                salary = 15
                hours = 10
                div()
                uni()
            elif ch == 2:
                salary = 19
                hours = 15
                div()
                uni()
            elif ch == 3:
                salary = 9
                hours = 22
                div()
                uni()
            else:
                uni()
        else:
            uni()

    def adult_rel(goto):
        clear_screen()
        global edu_lvl, pension, job_lvl, is_spouse, spouse
        global salary, hours, fame, friend_count, friend_1
        global allow_debug, allow_debug, friend_2, friend_3
        global mother_age, father_age, is_wpp, is_common_cold
        global mother_name, father_name, wpp_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel, part_time_salary
        global money, is_depressed, work_e, is_job, children
        global job_id, job_lvl, fame, child_count, child_1, child_2, child_3, child_4, child_5, child_6, child_7, child_8
        global money, children
        div()
        if mother_end_age > mother_age:
            print(mother_name)
            print("Mother [Age " + str(mother_age) + "]")
            pbar(mother_rel)
            print("[1] Interact")
            div()
        if father_end_age > father_age:
            print(father_name)
            print("Father [Age " + str(father_age) + "]")
            pbar(father_rel)
            print("[2] Interact")
            div()
        if is_spouse == 1:
            if spouse.end > spouse.age:
                print(spouse.name)
                print(f"[3] Spouse [Age {spouse.age}]")
                pbar(spouse.rel)
                div()
        if friend_count >= 1:
            if friend_1.end > friend_1.age:
                print(friend_1.name)
                print(f"[4] Friend #1 [Age {friend_1.age}]")
                print(pbar2(friend_1.rel))
                pbar(friend_1.rel)
                div()
        if friend_count >= 2:
            if friend_2.end > friend_2.age:
                print(friend_2.name)
                print(f"[5] Friend #2 [Age {friend_1.age}]")
                print(pbar2(friend_2.rel))
                pbar(friend_2.rel)
                div()
        if friend_count >= 3:
            if friend_3.end > friend_3.age:
                print(friend_3.name)
                print(f"[6] Friend #3 [Age {friend_1.age}]")
                print(pbar2(friend_3.rel))
                pbar(friend_3.rel)
                div()
        if len(children) > 0:
            if len(children) == 1:
                print(f"[7] Child List [1 Child]")
            else:
                print(f"[7] Child List [{len(children)} Children]")
            div()
        print("[0] Return")
        div()
        try:
            ch = int(input(">>"))
        except:
            if goto == 1:
                uni()
            else:
                adult()
        if ch == 7 and len(children) > 0:
            child_list(goto)
        elif ch == 1 and mother_end_age > mother_age:
            print(mother_name)
            print("Mother [Age " + str(mother_age) + "]")
            pbar(mother_rel)
            print("[0] Return")
            print("[1] Spend Time")
            print("[2] Disrespect")
            print("[3] Attack")
            try:
                ch = int(input(">>"))
            except:
                ch = 0
            div()
            if ch == 0:
                if goto == 1:
                    uni()
                else:
                    adult()
            elif ch == 1:
                div()
                print("You spent time with your mother.")
                mother_rel += 0.25
                if mother_rel > 1:
                    mother_rel = 1
                pbar(mother_rel)
                div()
                if goto == 1:
                    uni()
                else:
                    adult()
            elif ch == 2:
                print("You disrespected your mother.")
                mother_rel -= 0.25
                happiness -= 0.35
                if mother_rel < 0:
                    mother_rel = 0
                if happiness < 0:
                    happiness = 0
                pbar(mother_rel)
                div()
                if goto == 1:
                    uni()
                else:
                    adult()
            elif ch == 3:
                print("You hit your mother.")
                print("Damage:")
                pbar(0.65)
                div()
                mother_rel -= 0.55
                happiness -= 0.75
                if mother_rel < 0:
                    mother_rel = 0
                if happiness < 0:
                    happiness = 0
                pbar(mother_rel)
                div()
                if goto == 1:
                    uni()
                else:
                    adult()

        elif ch == 2 and father_end_age > father_age:
            print(father_name)
            print("Father [Age " + str(father_age) + "]")
            pbar(father_rel)
            print("[0] Return")
            print("[1] Spend Time")
            print("[2] Disrespect")
            print("[3] Attack")
            try:
                ch = int(input(">>"))
            except:
                ch = 0
            div()
            if ch == 0:
                if goto == 1:
                    uni()
                else:
                    adult()
            elif ch == 1:
                div()
                print("You spent time with your father.")
                father_rel += 0.25
                if father_rel > 1:
                    father_rel = 1
                pbar(father_rel)
                div()
                if goto == 1:
                    uni()
                else:
                    adult()
            elif ch == 2:
                print("You disrespected your father.")
                father_rel -= 0.25
                happiness -= 0.35
                if father_rel < 0:
                    father_rel = 0
                if happiness < 0:
                    happiness = 0
                pbar(father_rel)
                div()
                if goto == 1:
                    uni()
                else:
                    adult()
            elif ch == 3:
                print("You hit your father.")
                print("Damage:")
                pbar(0.25)
                div()
                print("Your father retaliated!")
                print("Damage:")
                pbar(0.75)
                health -= 0.75
                happiness = 0
                div()
                is_depressed = 1
                print("You are now suffering from DEPRESSION.")
                div()
                father_rel -= 0.55
                happiness -= 0.75
                if father_rel < 0:
                    father_rel = 0
                if happiness < 0:
                    happiness = 0
                pbar(father_rel)
                if goto == 1:
                    uni()
                else:
                    adult()
        elif ch == 3 and is_spouse == 1 and spouse.end > spouse.age:
            spouse_interact(goto)
        elif ch == 4 and friend_count >= 1 and friend_1.end > friend_1.age:
            friend_1_interact(goto)
        elif ch == 5 and friend_count >= 2 and friend_2.end > friend_2.age:
            friend_2_interact(goto)
        elif ch == 6 and friend_count >= 2 and friend_3.end > friend_3.age:
            friend_3_interact(goto)
        else:
            if goto == 1:
                uni()
            else:
                adult()

    def uni_pause():
        div()
        print("Game Paused.")
        div()
        print("[0] Resume")
        print("[x] Save Life")
        print("[2] Load Life")
        print("[3] Exit To Main Menu")
        div()
        print("[x] Download Challenge From Web")
        print("[x] Load Challenge From File")
        print("[6] Check For Updates")
        div()
        print("[x] Options")
        print("[x] Create Debug Log [For Bug Reporting]")
        div()
        try:
            ch = int(input(">"))
        except:
            uni()
        if ch == 2:
            print("[1] Exit Without Saving")
            print("[0] Back")
            div()
            try:
                ch = int(input(">"))
            except:
                uni()
            if ch == 1:
                load_game()
            else:
                uni()
        elif ch == 3:
            print("[1] Exit Without Saving")
            print("[0] Back")
            div()
            try:
                ch = int(input(">"))
            except:
                uni()
            if ch == 1:
                mainmenu()
            else:
                uni()
        elif ch == 6:
            import urllib.request

            url = "http://winfan3672.000webhostapp.com/version_check/openlife.version"
            print("Checking for updates...")
            try:
                urllib.request.urlretrieve(url, "openlife.version")
            except:
                div()
                print("Failed to check for updates.")
                div()
                print("You could try:")
                print("[-] Checking that you are connected to the Internet.")
                print(
                    "[-] Checking that winfan3672.000webhostapp.com is still up, since that is the server that provides the version check information."
                )
                print(
                    "[-] Checking that http://winfan3672.000webhostapp.com/version_check/openlife.versio exists, since it may have been deleted."
                )
                print(
                    "[-] Checking that your antivirus or firewall is not blocking winfan3672.000webhostapp.com/"
                )
                print("[-] On Windows, deleting your DNS resolver cache.")
                uni_pause()
            div()
            f = open("openlife.version", "r")
            data = f.read()
            data = data.split("|")
            data = [int(data[0]), int(data[1]), int(data[2])]
            try:
                urllib.request.urlretrieve(
                    "http://winfan3672.000webhostapp.com/latest_v_url/openlife",
                    "openlife.urlcheck",
                )
                f = open("openlife.urlcheck", "r")
                url = f.read()
            except:
                url = "[Could not retrieve URL from server]"
            not_update_text = (
                f"An update for {game_name} is available.\nDownload it from:\n{url}"
            )
            if data[0] > app_version[0]:
                print(not_update_text)
            else:
                if data[1] > app_version[1]:
                    div()
                    print(not_update_text)
                else:
                    if data[2] > app_version[2]:
                        div()
                        print(not_update_text)
                    else:
                        print(f"You are on the latest version of {game_name}.")
            uni_pause()
        else:
            uni()

    def uni():
        calc_stress()
        global uni_end_age
        global mother_age, father_age
        global mother_name, father_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel
        global money, is_depressed, debt, currency
        if happiness > 1:
            happiness = 1
        if happiness < 0:
            happiness = 0
        if health > 1:
            health = 1
        if health < 0:
            emergency_room(2)
        if intel > 1:
            intel = 1
        if looks > 1:
            looks = 1
        if intel < 0:
            intel = 0
        if looks < 0:
            looks = 0
        global forename, surname
        global mother_rel, father_rel
        global money
        div()
        print(forename + " " + surname)
        print("University Student")
        div()
        if is_depressed == 1:
            print("Suffers from: Depression")
        print("Age", age)
        print(f"{currency}" + str("{:,}".format((money))))
        div()
        print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "%")
        print("Health:   ", pbar2(health), str(int(health * 100)) + "%")
        print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "%")
        print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "%")
        div()
        print("Uni end age:", uni_end_age)
        div()
        print("[1] University")
        print("[0] Age Up")
        print("[3] Relationships")
        print("[4] Activities")
        print("[5] Pause Game")
        try:
            ch = int(input(">"))
        except:
            uni()
        if ch == 0:
            age_up(2)
        elif ch == 3:
            adult_rel(1)
        elif ch == 5:
            uni_pause()
        elif ch == 1:
            uni_menu()
        elif ch == 3:
            div()
            print("Locked.")
            div()
            uni()
        elif ch == 4:
            uni_activities()
        else:
            uni()

    def uni_start():
        global uni_end_age, age
        uni_end_age = age + 5
        print("You will end uni at age:", uni_end_age)
        uni()
        br()

    def uni_check():
        global degree, money, debt, currency
        print("Welcome to University.")
        print("Choose a degree:")
        print("[0] Return")
        print("[1] Finance")
        print("[2] Journalism")
        print("[3] Computer Science")
        print("[4] Education")
        print("[5] Accounting")
        print("[6] Political Science")
        print("[7] Nursing")
        print("[8] Psychology")
        print("[9] Engineering")
        print("[10] Art History")
        print("[11] Commuications")
        print("[12] Graphic Design")
        print("[13] Data Science")
        print("[14] Criminal Justice")
        print("[15] Linguistics")
        print("[16] Marketing")
        print("[17] Anthropology")
        print("[18] Archaeology")
        print("[19] Biology")
        print("[20] Chemistry")
        print("[21] Physics")
        print("[22] English")
        print("[23] Mathematics")
        print("[24] History")
        print("[25] Information Systems")
        print("[26] Music")
        print("[27] Economics")
        print("[28] Dance")
        print("[29] Electrical Engineering")
        print("[30] Religious Studies")
        print("[31] Dentistry")
        print("[32] Law")
        div()
        print("The degree you choose influences:")
        print("[-] What job you can get")
        print("[-] What degrees you can get in grad school")
        print("[-] What schools you can get into")
        div()
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        if ch < 1:
            adult()
        if ch > 32:
            adult()
        else:
            if intel >= 0.75:
                global degree
                degree = ch
                div()
                print("You have been selected for Uni!")
                print(f"Price: {currency}25,000")
                print("[1] Buy With Cash")
                print("[2] Scholarship")
                print("[3] Ask your mother to pay")
                print("[4] Apply for a student loan")
                print("[0] Return")
                try:
                    ch = int(input(">"))
                except:
                    ch = 0
                div()
                if ch == 0:
                    adult()
                elif ch == 1:
                    global debt
                    debt += 25000
                    uni_start()
                elif ch == 1:
                    if money >= 25000:
                        money -= 25000
                        print("You bought a university degree.")
                        uni_start()
                    else:
                        print("You cannot afford your degree.")
                        uni_check()
                elif ch == 2:
                    global club_count
                    if club_count >= 2:
                        print("You have been awarded a scholarship!")
                        uni_start()
                elif ch == 3:
                    global mother_rel
                    if mother_rel >= 0.75:
                        print("Your mother agreed to pay for your degree!")
                        uni_start()
                    else:
                        print("Your mother refused to pay for your degree.")
                        uni_check()
                elif ch == 4:
                    debt += 25000
                    uni_start()
                else:
                    adult()
            else:
                div()
                print("Your university application was declined.")
                adult()

    def blackjack_init():
        global money, winnings
        winnings = 0
        casino_menu()

    def get_card():
        global number
        from random import randint

        number += randint(1, 10)

    def enemy_get_card():
        global enemy_number
        from random import randint

        enemy_number += randint(1, 10)

    def decide():
        global money, number, enemy_number, bet, winnings, debt
        if enemy_number > 21:
            print("Enemy bust!")
            money += bet
            winnings += bet
            br()
            casino_menu()
        elif enemy_number > number:
            print("Enemy won")
            debt += bet
            winnings -= bet
            br()
            casino_menu()

    def enemy():
        global money, number, enemy_number, debt
        from time import sleep

        enemy_number = 0
        div()
        print("Your enemy begins.")
        # if enemy_number > number:
        # lose
        # else if enemy busts
        # win
        # else [due to error]
        # win
        enemy_get_card()
        print("Your hand:", number)
        print("Enemy hand:", enemy_number)
        div()
        while True:
            if enemy_number > number:
                break
            elif enemy_number > 21:
                break
            else:
                enemy_get_card()
                print("Your hand:", number)
                print("Enemy hand:", enemy_number)
                sleep(0.45)
                div()
        decide()

    def blackjack():
        global money, number, bet, winnings, allow_debug, debt, currency
        try:
            bet = int(input("Enter Bet >"))
        except:
            bet = money
        if bet > money:
            bet = money
        if bet < 1000:
            div()
            print(f"Bet set to minimum [{currency}1000]")
            div()
            bet = 1000
        elif bet > 10000000:
            div()
            print(f"Bet set to maximum [{currency}10 000 000]")
            div()
            bet = 10000000
        else:
            div()
            print(f"You have {currency}" + str(bet) + " riding on this bet.")
            div()
        number = 0
        get_card()
        while True:
            if number > 21:
                print("Bust!")
                winnings -= bet
                debt += bet
                casino_menu()
            print("Your Hand:", number)
            print("[1] Hit Me")
            print("[2] I'll Stand")
            try:
                ch = int(input(">"))
            except:
                ch = 1
            if ch == 1:
                get_card()
            elif ch == 2:
                enemy()

    def lottery(is_teen,amount=0):
        global money, allow_test, currency, lottery_wins, debt
        from random import randint

        div()
        print("Enter amount of lottery tickets to buy.")
        div()
        print("Warning: Choosing a large amount of tickets [10M+] may result in a large amount of CPU usage. It may also take a long time. Depending on the speed of your CPU, it may take several minutes to process. If you enter an obscene amount of tickets, you CANNOT cancel the operation, meaning you will be unable to do anything. Proceed with caution")
        div()
        print(f"1 ticket = {currency}100")
        base = str("{:,}".format((int(money / 100))))
        print("You can afford", base, "tickets.")
        div()
        losses = 0
        wins = 0
        win_amount = 0
        if amount == 0:
            try:
                ticket_count = int(input(">"))
            except:
                ticket_count = 0
        else:
            ticket_count = amount
        price = ticket_count * 100
        tmw = ticket_count * 1000
        tmw *= 1000000
        debt_mode = 0
        if price > money:
            debt_mode = 1
        if ticket_count == 0:
            if is_teen == 0:
                adult()
            else:
                teen()
        else:
            try:
                for i in range(ticket_count):
                    if debt_mode == 1:
                        debt += 100
                    else:
                        money -= 100
                    chance = randint(1, 100000)
                    if chance == 2345:
                        base = wins + losses
                        base /= ticket_count
                        base *= 100
                        print(
                            "You won! [" + str("{:,}".format((int(losses)))),
                            "losses] [" + str(int(base)) + "%]",
                        )
                        lottery_wins += 1
                        wins += 1
                        base = randint(250, 1000)
                        base *= 1000000
                        money += base
                        win_amount += base
                    else:
                        losses += 1
                if debt_mode == 1:
                    debt += int(debt * 1.2)
            except KeyboardInterrupt:
                pass
            except:
                pass
            print("Tickets Bought:", ticket_count)
            base = str("{:,}".format((int(win_amount))))
            print("Wins:", wins)
            print(f"Lifetime Wins:", str("{:,}".format((int(lottery_wins)))))
            print("Losses:", losses)
            div()
            print(f"Win Amount: {currency}" + str(base))
            base = str("{:,}".format((int(tmw))))
            print(f"Theoretical Maximum Win: {currency}" + base)
            br()
            if is_teen == 0:
                adult()
            else:
                teen()

    def choose_start(verbose):
        global age
        from random import randint

        global start_age
        global mother_rel, father_rel
        global mother_age, father_age
        global grades, intel, money
        global mother_end_age, father_end_age
        global edu_lvl
        age = start_age
        mother_age = age + 32
        father_age = age + 37
        base = randint(15, 55)
        mother_end_age = +32 + base
        base = randint(15, 55)
        father_end_age = 37 + base
        global happiness, intel
        global stress
        if start_age <= 5:
            infant_start()
        elif start_age >= 6 and start_age < 12:
            mother_rel = 1
            father_rel = 1
            stress = 0.5
            child_init()
        elif age >= 12 and age < 18:
            money = 0
            stress = 0.65
            mother_rel = 0.8
            grades = intel
            father_rel = 0.8
            teen_init()
        elif age >= 18:
            global salary, hours
            salary = 0
            hours = 0
            global did_tutor
            did_tutor = 0
            edu_lvl = 1
            money = 0
            stress = 0
            mother_rel = 0.8
            father_rel = 0.8
            adult_init(verbose)
        else:
            raise ExitError

    def fame_increase():
        global job_id, job_lvl, fame, promo_base, money
        if job_id == 6 and job_lvl == 3:
            if promo_base >= 3 and work_e_base >= 10:
                fame += 0.25
        elif job_id == 9 and job_lvl == 3:
            if promo_base >= 3 and work_e_base >= 10:
                fame += 0.25
        elif job_id == 13 and job_lvl == 3:
            if promo_base >= 3 and work_e_base >= 10:
                fame += 0.25
        elif job_id == 28:
            if promo_base >= 3 and work_e_base >= 10:
                fame += 0.25
        elif job_id == 21:
            if promo_base >= 3 and work_e_base >= 15:
                fame += 0.25
        elif money >= 1000000:
            fame += int(money / 1000000) / 100
        else:
            fame -= rng(10, 20) / 100

        return True

    def give_disease():
        global is_common_cold, is_cancer
        chance = rng(1, 3)
        if chance == 1 and is_common_cold == 0:
            div()
            print("You are now suffering from THE COMMON COLD.")
            is_common_cold = 1
            return True
        elif chance == 2 and is_cancer == 0:
            chance = rng(1, 100)
            # chance = 128
            if chance == 128:
                div()
                print("You are now suffering from CANCER.")
                is_cancer = 1
                return True
        else:
            return True

    def age_up(goto):
        global happiness, intel, is_cancer, age, auto_pay_lab, offcences, sentence
        global money, father_rel, allow_test, child_count, child_1, child_2, child_3, child_4, child_5, child_6, child_7, child_8
        global salary, hours, expenses, happiness, health, intel, looks, teen_salary, teen_hours
        global mother_end_age, father_end_age, money, is_spouse, spouse, book_base, uni_end_age, surgeons
        global is_depressed, is_anxiety, savings, debt, is_hbp, juvie_years, is_opentube, research_lab, pending_research
        global year, is_job, work_e_base, pension, promo_base, currency, prison_years, houses
        year += 1
        if len(vehicles[0]) > 0:
            for item in vehicles[0]:
                item.age_up()
            is_arrest = 0
            for item in vehicles[0]:
                if item.is_stolen == 1:
                    is_arrest += 1
            if is_arrest!= 0:
                chance=rng(1,3)
                if chance == 3:
                    try:
                        offences += is_arrest
                    except:
                        offences = is_arrest
                    sentence = 3 * is_arrest
                    go_to_prison()
        if len(vehicles[1]) > 0:
            for item in vehicles[1]:
                item.age_up()
        if len(vehicles[2]) > 0:
            for item in vehicles[2]:
                item.age_up()
        if len(surgeons) > 0 and age >= 18:
            for item in surgeons:
                item.age_up()
        if age >= 18 and auto_pay_lab == 1 and research_lab[0] == 1 and pending_research[1] == -10:
            if money >= 10000000000:
                money -= 10000000000
                pending_research = [0,0]
            else:
                if savings >= 10000000000:
                    savings -= 10000000000
                else:
                    debt += 10000000000
                pending_research = [0,0]
            print("[AUTOPAID FOR LAB]")
        if age >= 18 and research_lab[0] == 1 and pending_research[0] == 0:
            pending_research[1] -= 1
            if pending_research[1] == -15:
                research_lab, pending_research = [0,0,0,0,0], [0,0]
                div()
                print(f"{game_name} Times")
                print("The best newspaper since 2022 AD.")
                div()
                print(f"{forename} {surname} Research Institute Goes Bankrupt")
                div()
                print(f"The {forename} {surname} Research Institute has gone bankrupt. After years of not developing anything whatsoever and acting as a body to protect its own research discoveries,")
                print(f"the body filed for Chapter 7 Bankrupcy [Liquidation of All Assets] last night, leading to general cheering amongst scientists. The facility has been long-hated for not sharing its")
                print(f"discoveries with the world, chooosing to keep them private trade secrets. As a result, when the Institute announced a discovery, they would be mocked by scientists for creating private technology")
                print(f"that only its owner, {forename} {surname}, or billionaires could access. Papers released by the Institute are locked behind safes and decades-long efforts to reverse-engineer the Research Institute's science")
                print(f"have been unsuccessful. Now, the proprietary technology has gone to waste, since all of the {forename[0].upper()}{surname[0].upper()}RI's assets were liquidated, making their discoveries all but lost forever.")
                print(f"On top of this, on the very same day they filed for bankrupcy, the {forename[0].upper()}{surname[0].upper()}RI caught fire and was burnt to the ground, leaving molten steel and glass shards everywhere.")
                print(f"While nobody was hurt, the vaults containing the blueprints to the {forename[0].upper()}{surname[0].upper()}RI's technology blew up. Examination of the charred remains shows that the vaults were equipped with")
                print(f"oxygen bombs that melted the vaults and burnt the papers. This fire was obviously a sabotage, as the OpenLife Inspections Agency [OIA] inspected the facility [3] years ago and found that oxygen bombs were placed inside the steel frame of the building. While a complaint was filed, lobbyists campaigned against further action.")
                print(f"For a Research Institute to burn its work to the ground is a great sign of the amount of evil it possesses. Hopefully, nobody repeats what the {forename[0].upper()}{surname[0].upper()}RI did.")
                br()
        if  age >= 18 and pending_research[0] > 0:
            pending_research[1] -= 1
            if pending_research[1] == 0:
                if pending_research[0] == 1:
                    print("You successfully researched RESEARCH LAB.")
                if pending_research[0] == 2:
                    print("You successfully researched AGE-DOWN.")
                if pending_research[0] == 3:
                    div()
                    if gender == 0:
                        him_her = "himself"
                    elif gender == 1:
                        him_her = "herself"
                    else:
                        him_her = "themselves"
                    print(f"{game_name} Times")
                    print("The best newspaper since 2022 AD.")
                    div()
                    print(f"{forename} {surname} Research Institute Cures Cancer, But It Costs {currency}1,000,000,000 To Get")
                    div()
                    print(f"Scientists at the {forename} {surname} Research Institute have announced that they have discovered a cure for cancer.")
                    print(f"After 11 years of non-stop research, the {forename[0].upper()}{surname[0].upper()}RI have finally done it, beating scientists all around the world.")
                    print(f"The Research Institute is a world-renowned insititute, known for creating huge advancements in science. However, due to conflict of interest relating to its owner,")
                    print(f"the facility is vilified by the scientific community. The owner, {forename} {surname}, expresses no wishes to help anyone other than {him_her}, choosing to develop")
                    print(f"groundbreaking technology and keeping it to {him_her}. Because of this, the Institute was rated \"Worst Scientific Body Ever\" 11 years in a row.")
                    print(f"While this is a great advancement in science, it costs {currency}1,000,000,000 to get the treatment. This is because the technology is in its infancy, and refinements will have")
                    print(f"to be made to make it affordable. \nAllegedly, {currency}55,000,000,000 [55 Billion] was poured in just to fund this project.")
                    print(f"The question remains, what will come of this? Will this technology be refined to make it affordable, making {forename} {surname} the greatest scientist of all time?")
                    print(f"Or will it simply remain behind closed doors for all of the billionaires to take advantage of, lining the Institute's pockets?")
                    print(f"Will cancer patients have to live with the fact that people like Jeff Bezos can easily afford cancer treatment, whereas they struggle to pay for the now-dated chemotherapy?")
                    print(f"\nOnly time will tell. {forename} {surname}, if you can read this, please make the right decision for humanity. If you do the jealous thing and keep it to yourself, we might lose the")
                    print(f"cure to cancer when the Institute shuts down.")
                    br()
                research_lab[pending_research[0] - 1] = 1
                pending_research[0] = 0
        if child_count >= 1:
            child_1.age += 1
        if child_count >= 2:
            child_2.age += 1
        if child_count >= 3:
            child_3.age += 1
        if child_count >= 4:
            child_4.age += 1
        if child_count >= 5:
            child_5.age += 1
        if child_count >= 6:
            child_6.age += 1
        if child_count >= 7:
            child_7.age += 1
        if child_count >= 8:
            child_8.age += 1
        if age >= 18:
            money -= child_count * 6000
        if is_cancer == 1:
            chance = rng(1, 6)
            if chance == 6:
                die(3)
        chance = rng(1, 3)
        if chance == 1:
            give_disease()
        if is_spouse == 1:
            if spouse.pregnant == 1:
                if spouse.craziness >= 0.75:
                    chance = 3
                elif spouse.craziness >= 0.5:
                    chance = rng(1, 3)
                else:
                    chance = rng(1, 5)
                if chance != 3:
                    make_child()
                else:
                    print("You had a miscarriage and lost the baby!")
                    happiness -= 0.8
                    spouse.rel -= 0.4

        if is_opentube == 1:
            global opentube_year, video_count, view_count, subscribers, is_monetised, yearly_videos
            opentube_year += 1
            for i in range(yearly_videos):
                video_count += 1
                oldsubs = subscribers
                views_gained = int(oldsubs + int((oldsubs / 2)))
                view_count += views_gained
                subs_gained = int(views_gained / 3)
                if subs_gained > 8000000000 - subscribers:
                    subs_gained = 8000000000 - subscribers
                subscribers += subs_gained
                if is_monetised == 1:
                    cpm = (views_gained / 17) / 100
                    money += int(cpm)
            for i in range(video_count):
                oldsubs = subscribers
                views_gained = int(oldsubs + int((oldsubs / 2)))
                view_count += views_gained
                subs_gained = int(views_gained / 3)
                if subs_gained > 8000000000 - subscribers:
                    subs_gained = 8000000000 - subscribers
                subscribers += subs_gained
                if is_monetised == 1:
                    cpm = (views_gained / 17) / 100
                    money += int(cpm)
        for item in houses:
            item.age_up()
        if book_base > 0:
            book_base -= 1
        if is_spouse == 1:
            spouse.age += 1
        
        global did_tutor, auto_deposit
        did_tutor = 0
        chance = rng(1, 400)
        chance_2 = rng(1, 2)
        if chance == 400:
            print("You were struck by lightining!")
            if chance_2 == 1:
                print("You survived.")
                happiness = 1
                health = 1
                looks = 1
                intel = 1
            else:
                die(6)
        # random stat change: if you have 10% or less health, you have a chance of dying!
        happiness += rng(-10, 10) / 100
        health += rng(-10, 10) / 100
        intel += rng(-10, 10) / 100
        looks += rng(-10, 10) / 100

        if is_hbp == 1:
            if stress <= 0.45:
                chance = rng(1, 2)
                if chance == 1:
                    is_hbp = 0
                    div()
                    print("You are no longer suffering from HIGH BLOOD PRESSURE.")
            chance = rng(1, 4)
            if chance == 3 and stress >= 0.75:
                die(2)
        if age >= 12 and is_hbp == 0:
            if stress >= 0.75:
                chance = rng(1, 2)
                if chance == 1:
                    is_hbp = 1
                    div()
                    print("You are now suffering from HIGH BLOOD PRESSURE")
        if age >= 12 and age < 18:
            money += (teen_salary * teen_hours) * 52
        if age >= 6:
            basee = savings / 10
            basee = int(basee)
            savings += basee
            base = int(debt / 5)
            debt += base
            base = int(debt / 10)
            money -= base
        if pension > 0:
            money += pension
        global work_e, is_job
        if age >= 18:
            money += part_time_salary * 520
        if is_job == 1:
            work_e += 1
            work_e_base += 1
            promo_base += 1
        if promo_base == 5:
            promo_base = 0
            promotion()
        global mother_age, father_age, edu_lvl
        age += 1
        mother_age += 1
        father_age += 1
        # when parents die
        if age >= 18:
            fame_increase()
        if age >= 18 and is_job == 1:
            base = salary * hours * 52
            money += base
        if age >= 18:
            money -= expenses * 12
        if mother_age == mother_end_age:
            div()
            print("Your mother died.")
            print("It is your responsibility to plan the funeral.")
            print("[0] Skip")
            print(f"[1] Bury [{currency}8500]")
            print(f"[2] Cremate [{currency}1500]")
            print(f"[3] Taxidermy [{currency}15 000]")
            print(f"[4] Donate To Science [{currency}0]")
            try:
                ch = int(input(">"))
            except:
                ch = 4
            if ch == 0:
                print("You skipped the funeral.")
            elif ch == 1:
                print("Your mother was buried.")
                money -= 8500
            elif ch == 2:
                money -= 15000
                print("You cremated your mother.")
                print("Choose what to do with the ashes:")
                print("[1] Sprinkle somewhere special.")
                print("[2] Put in urn")
                print("[0] Throw In Trash")
                ch = input(">")
            elif ch == 3:
                print("You had your mother taxidermied.")
                money -= 15000
            elif ch == 4:
                print("Your mother's body was donated to science.")
            else:
                print("You skipped the funeral.")
            from random import randint

            mother_fortune = randint(1000000, 3000000)
            div()
            print(f"You inherited {currency}" + str(mother_fortune))
            money += mother_fortune
        if father_age == father_end_age:
            div()
            print("Your father died.")
            print("It is your responsibility to plan the funeral.")
            print("[0] Skip")
            print(f"[1] Bury [{currency}8500]")
            print(f"[2] Cremate [{currency}1500]")
            print(f"[3] Taxidermy [{currency}15 000]")
            print(f"[4] Donate To Science [{currency}0]")
            try:
                ch = int(input(">"))
            except:
                ch = 4
            if ch == 0:
                print("You skipped the funeral.")
            elif ch == 1:
                print("Your father was buried.")
                money -= 8500
            elif ch == 2:
                money -= 15000
                print("You cremated your father.")
                print("Choose what to do with the ashes:")
                print("[1] Sprinkle somewhere special.")
                print("[2] Put in urn")
                print("[0] Throw In Trash")
                ch = input(">")
            elif ch == 3:
                print("You had your father taxidermied.")
                money -= 15000
            elif ch == 4:
                print("Your father's body was donated to science.")
            else:
                print("You skipped the funeral.")
            from random import randint

            father_fortune = randint(1000000, 3000000)
            div()
            print(f"You inherited {currency}" + str(father_fortune))
            money += father_fortune
        if is_spouse == 1:
            if spouse.age >= spouse.end:
                div()
                is_spouse = 0
                print("Your spouse died.")
                print("It is your responsibility to plan the funeral.")
                print("[0] Skip")
                print(f"[1] Bury [{currency}8500]")
                print(f"[2] Cremate [{currency}1500]")
                print(f"[3] Taxidermy [{currency}15 000]")
                print(f"[4] Donate To Science [{currency}0]")
                try:
                    ch = int(input(">"))
                except:
                    ch = 4
                if ch == 0:
                    print("You skipped the funeral.")
                elif ch == 1:
                    print("Your spouse was buried.")
                    money -= 8500
                elif ch == 2:
                    money -= 15000
                    print("You cremated your spouse.")
                    print("Choose what to do with the ashes:")
                    print("[1] Sprinkle somewhere special.")
                    print("[2] Put in urn")
                    print("[0] Throw In Trash")
                    ch = input(">")
                elif ch == 3:
                    print("You had your spouse taxidermied.")
                    money -= 15000
                elif ch == 4:
                    print("Your spouse's body was donated to science.")
                else:
                    print("You skipped the funeral.")
        if auto_deposit == 1 and age >= 6:
            savings += money
            money = 0
        # redirect
        if age >= 12 and age < 18:
            if juvie_years > 0:
                chance = rng(1, 2)
                if chance == 2:
                    go_to_juvie()
        if age >= 18:
            if prison_years > 0:
                chance = rng(1, 2)
                if chance == 2:
                    go_to_prison()
        if age <= 5:
            happiness += 0.25
            if intel <= 0.75:
                intel += 0.15
            infant()
        elif age >= 6 and age < 12:
            if age == 6:
                child_init()
            else:
                if father_rel >= 0.75:
                    savings += 520
                elif father_rel < 0.75 and father_rel > 0.25:
                    savings += 260
                if happiness <= 0.1 and is_depressed == 0:
                    is_depressed = 1
                    div()
                    print("You are now suffering from DEPRESSION.")
                if is_depressed == 1:
                    happiness /= 4
                if is_depressed == 1 and happiness >= 0.65:
                    div()
                    print("You are no longer suffering from DEPRESSION.")
                    is_depressed = 0
                    happiness *= 2
                    div()
                child()
        elif age >= 12 and age < 18:
            teen_calc_stress()
            if age == 12:
                teen_init()
            else:
                if happiness <= 0.1 and is_depressed == 0:
                    is_depressed = 1
                    div()
                    print("You are now suffering from DEPRESSION.")
                if is_depressed == 1:
                    if happiness < 0.65:
                        happiness /= 4
                    else:
                        div()
                        print("You are no longer suffering from DEPRESSION!")
                        is_depressed = 0
                teen()
        elif age >= 18:
            calc_stress()
            if juvie_years > 0:
                prison_years = juvie_years
                juvie_years = 0
            if happiness <= 0.1 and is_depressed == 0:
                is_depressed = 1
                div()
                print("You are now suffering from DEPRESSION.")
            if is_depressed == 1 and happiness < 0.65:
                happiness /= 4
            if is_depressed == 1 and happiness >= 0.65:
                div()
                print("You are no longer suffering from DEPRESSION.")
                is_depressed = 0
                happiness *= 2
            from random import randint

            if age == 18:
                salary = 0
                hours = 0
                edu_lvl = 1
                adult_init(1)
            elif age >= 70 and age < 80:
                dc = randint(1, 400)
                if dc != 400 or allow_test == 1:
                    pass
                else:
                    die(1)
            elif age >= 80 and age < 90:
                # print("80")
                dc = randint(1, 20)
                if dc != 20 or allow_test == 1:
                    pass
                else:
                    die(1)
            elif age >= 90:
                # print("AGE TEST")
                dc = randint(1, 3)
                if dc != 3:
                    pass
                else:
                    die(1)
            elif age >= 100 and age < 120:
                dc = randint(1, 2)
                if dc == 1 and allow_test == 0:
                    die(1)
                else:
                    pass
            elif age >= 120:
                div()
                die(1)
            else:
                if goto == 1:
                    opentube()
                elif goto == 2:
                    if age == uni_end_age:
                        div()
                        edu_lvl = 2
                        print("You graduated from University.")
                        salary = 0
                        work_e_base = 0
                        hours = 0
                        br()
                        adult()
                    else:
                        uni()
                else:
                    adult()
        else:
            raise FeatureNotInGameError

    def pbar(percent):
        global alt_ui
        if percent > 1:
            percent = 1
        percent *= 100
        bar = "["
        hash = percent / 5
        global alt_ui
        hash = int(hash)
        dot = 20 - hash
        for i in range(hash):
            if alt_ui == 1 or alt_ui == 2 or alt_ui == 4:
                bar += "|"
            else:
                bar += "#"
        for i in range(dot):
            if alt_ui == 1 or alt_ui == 2 or alt_ui == 3 or alt_ui == 4 or alt_ui == 5:
                bar += " "
            else:
                bar += "."
        bar += "]"
        print(bar)

    def pbar2(percent):
        global alt_ui
        if percent > 1:
            percent = 1
        if percent < 0:
            percent = 0
        percent *= 100
        bar = "["
        hash = percent / 5
        global alt_ui
        hash = int(hash)
        dot = 20 - hash
        for i in range(hash):
            if alt_ui == 1 or alt_ui == 2:
                bar += "|"
            else:
                bar += "#"
        for i in range(dot):
            if alt_ui == 1 or alt_ui == 2 or alt_ui == 3 or alt_ui == 5:
                bar += " "
            else:
                bar += "."
        bar += "]"
        return bar

    def cls():
        # code from https://github.com/fungamer2-2/Life-Simulator1
        res=uname()
        os.system("cls" if res[0] == "Windows" else "clear")
        return True

    def div():
        try:
            global alt_ui
            if alt_ui == 2:
                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            elif alt_ui == 1:
                print("▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢")
            elif alt_ui == 3:
                print("--------------------")
            elif alt_ui == 4:
                print("|------------------|")
            elif alt_ui == 5:
                print("####################")
            else:
                print("====================")
            return True
        except:
            raise ExitError

    def br():
        div()
        print("Press ENTER to continue")
        input()
        return True

    def end():
        div()
        print("This menu is obsolete. This used to be the death screen.")
        print("Now, the anticheat gets triggered.")
        div()
        print("[1] Exit")
        print("[0] Main menu")
        try:
            ch = int(input(">>"))
        except:
            ch = 1
        if ch == 1:
            while True:
                raise ExitError
        else:
            mainmenu()

    def doctor_adult():
        global is_depressed, is_hbp, is_common_cold, is_cancer
        print("You went to visit the doctor.")
        div()
        print(
            "There was no consultation fee, courtesy of OpenLife's free healthcare system [The National Healthcare Organisation]."
        )
        br()
        div()
        if is_depressed == 0 and is_hbp == 0 and is_common_cold == 0 and is_cancer == 0:
            print(
                "The doctor has determined that you are not suffering from any conditions."
            )
            br()
            adult()
        else:
            print(
                "After a brief physical and mental examination, the doctor determined that you are suffering from the following conditions:"
            )
            if is_depressed == 1:
                print("Depression")
            if is_hbp == 1:
                print("High Blood Pressure")
            div()
            if is_depressed == 1:
                print("[0] Return")
                print(f"[1] Treat Depression [{currency}0]")
            if is_hbp == 1:
                print(f"[2] Treat High Blood Pressure [{currency}0]")
            if is_common_cold == 1:
                print(f"[3] Treat Common Cold [{currency}0]")
            if is_cancer == 1:
                print(f"[4] Treat Cancer [{currency}0]")
            div()
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 1 and is_depressed == 1:
                print("You were treated for Depression.")
                print("You continue to suffer from Depression.")
                br()
                adult()
            elif ch == 2 and is_hbp == 1:
                print("You were treated for High Blood Pressure.")
                print("You continue to suffer from High Blood Pressure.")
                br()
                adult()
            elif ch == 3 and is_common_cold == 1:
                print("You were treated for the Common Cold.")
                print("You are no longer suffering from the Common Cold.")
                br()
                is_common_cold = 0
                adult()
            if ch == 4 and is_cancer == 1:
                print("You were treated for Cancer.")
                print("You continue to suffer from Cancer.")
                br()
                adult()
            else:
                adult()

    def emergency_room(might_die):
        global health
        # you get rushed to the ER once your healh is < 0%
        # You have a 50% chance of dying

        # set might_die to 1 for a 50% death chance
        # and 0 for 100% chance of living

        from random import randint

        global health
        if might_die == 1:
            div()
            print("You were rushed to the emergency room.")
            chance = randint(1, 2)
            if chance != 2:
                print("You died.")
                die(4)
            else:
                print("You barely survived.")
                health = 0.1
                br()
                teen()
        elif might_die == 2:
            div()
            print("You were rushed to the emergency room.")
            chance = randint(1, 4)
            if chance == 4:
                print("You died.")
                die(4)
            else:
                print("You barely survived.")
                div()
                health = 0.1
                br()
                adult()
        elif might_die == 3:
            div()
            print("You were rushed to the emergency room.")
            chance = randint(1, 4)
            if chance == 4:
                print("You died.")
                die(4)
            else:
                print("You barely survived.")
                div()
                health = 0.1
                br()
                juvie()
        elif might_die == 4:
            div()
            print("You were rushed to the emergency room.")
            chance = randint(1, 4)
            if chance == 4:
                print("You died.")
                die(4)
            else:
                print("You barely survived.")
                div()
                health = 0.1
                br()
                prison()
        elif might_die == 0:
            div()
            print("You were rushed to the emergency room.")
            print("You barely survived.")
            div()
            health = 0.1
            br()
            teen()
        else:
            raise ExitError

    def job_interview():
        i = rng(1, 12)
        div()
        print("Interview")
        div()
        if i == 1:
            print("Tea or coffee?")
            div()
            print("[1] Tea")
            print("[2] Coffee")
            print("[3] Both")
            print("[4] Neither")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1 or ch == 2:
                return True
            else:
                return False
        elif i == 2:
            print("Any more questions?")
            div()
            print("[1] When do I start?")
            print("[2] What's the company ethos?")
            print("[3] How much is the pay?")
            print("[4] What's the corporate structure?")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 2 or ch == 4:
                return True
            else:
                return False
        elif i == 3:
            print("Which of these elements do you most associate with?")
            div()
            print("[1] Fire")
            print("[2] Earth")
            print("[3] Water")
            print("[4] Wind")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 2 or ch == 4:
                return True
            else:
                return False
        elif i == 4:
            print("Which Yu-Gi-Oh! character do you relate to most?")
            div()
            print("[1] Yugi Moto")
            print("[2] Seto Kaiba")
            print("[3] Maximillion Pegasus")
            print("[4] Mai Valentine")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1 or ch == 2:
                return True
            else:
                return False
        elif i == 5:
            print("Which Harry Potter character do you relate to most?")
            div()
            print("[1] Harry Potter")
            print("[2] Dobby")
            print("[3] Rubeus Hagrid")
            print("[4] Albus Percival Wulfric Brian Dumbledore")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 2 or ch == 4:
                return True
            else:
                return False
        elif i == 6:
            print("Do you like BitLife?")
            div()
            print("[1] Never heard of it.")
            print("[2] It's pay-to-win garbage.")
            print("[3] Yes!")
            print(f"[4] {game_name} is better.")  # Not to blow my own trumpet.
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 2 or ch == 4:
                return True
            else:
                return False
        elif i == 7:
            print("What do you most value in a workplace?")
            div()
            print("[1] Cute female employess.")
            print("[2] A good workplace culture.")
            print("[3] Paid leave.")
            print("[4] Collaboration")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 2 or ch == 4:
                return True
            else:
                return False
        elif i == 8:
            print("What are your salary expectations?")
            div()
            print("[1] They align with my qualifications.")
            print("[2] Top dollar.")
            print("[3] What's a salary?")
            print("[4] I expect what's stated on the job offer.")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1 or ch == 4:
                return True
            else:
                return False
        elif i == 9:
            print("Where do you see yourself in 5 years?")
            div()
            print("[1] Can't even see myself in five minutes!")
            print("[2] In a managerial position here.")
            print("[3] Retired :)")
            print("[4] As your boss.")
            print("[5] Not here!")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 2 or ch == 3:
                return True
            else:
                return False
        elif i == 10:
            print("What are your plans for education?")
            div()
            print("[1] I'll never stop learning.")
            print("[2] I stopped years ago.")
            print("[3] I imagine it'll come as a part of the job.")
            print("[4] I dropped out of primary school.")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1 or ch == 3:
                return True
            else:
                return False
        elif i == 11:
            print("How did you hear about this position?")
            div()
            print("[1] Indeed.com")
            print("[2] I'm not sure")
            print("[3] I saw a posting online")
            print("[4] I heard about it from your competitor.")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1 or ch == 3:
                return True
            else:
                return False
        elif i == 12:
            print("How do you deal with stressful situations?")
            div()
            print("[1] I never stress.")
            print("[2] I don't.")
            print("[3] I meditate.")
            print("[4] I step back and consider my options.")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 3 or ch == 4:
                return True
            else:
                return False
        else:
            return False

    def crime():
        div()
        adult_crime()

    def vacation():
        global money, happiness, debt
        print("[0] Return")
        print(f"[1] Cruise [{currency}4 500]")
        print(f"[2] Vacation [{currency}25 000]")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        elif ch == 1:
            if money >= 4500:
                money -= 4500
            else:
                debt += 4500
            happiness += 0.45
            div()
            print("You went for a cruise.")
            print("Enjoyment:")
            pbar(0.65)
            adult()
        elif ch == 2:
            if money >= 25000:
                money -= 25000
            else:
                debt += 25000
            happiness += 0.85
            div()
            print("You went for a cruise.")
            print("Enjoyment:")
            pbar(0.90)
            adult()
        else:
            adult()

    def identity():
        global forename, surname, money, gender, sexuality, is_trans, spouse, is_trans
        print("[0] Return")
        print(f"[1] Name Change [{currency}150]")
        print(f"[2] Declare Gender")
        print(f"[x] Declare Sexuality")
        try:
            ch = int(input(">"))
        except:
            adult()
        if ch == 1:
            if money >= 150:
                money -= 150
                forename = input("Forename >")
                forename = forename.replace("|", "")
                if len(forename) > 16:
                    while len(forename) > 16:
                        forename = forename[: (len(forename) - 1)]
                surname = input("Surname >")
                if len(surname) > 16:
                    while len(surname) > 16:
                        surname = surname[: (len(forename) - 1)]
                surname = surname.replace("|", "")
                adult()
            else:
                div()
                print("You cannot afford that.")
                adult()
        elif ch == 2:
            print("[1] Male")
            print("[2] Female")
            print("[3] Non-Binary")
            div()
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 1:
                if gender == 0 and is_trans == 0:
                    adult()
                elif gender == 0 and is_trans == 1:
                    is_trans = 0
                    gender = 1
                    adult()
                else:
                    gender = 0
                    is_trans = 1
                    print("You came out of the closet.")
                    if is_spouse == 1:
                        if spouse.gender == 1:
                            print("Your spouse left you.")
                            spouse = 0
                    if mother_end_age > mother_age:
                        print("Your mother said she would support you, no matter what.")
                    if father_end_age > father_age:
                        print("Your father said he would support you, no matter what.")
                    adult()
            if ch == 2:
                if gender == 1 and is_trans == 0:
                    adult()
                elif gender == 1 and is_trans == 1:
                    is_trans = 0
                    gender = 0
                    adult()
                else:
                    gender = 1
                    is_trans = 1
                    print("You came out of the closet.")
                    if is_spouse == 1:
                        if spouse.gender == 0:
                            print("Your spouse left you.")
                            spouse = 0
                    if mother_end_age > mother_age:
                        print("Your mother said she would support you, no matter what.")
                    if father_end_age > father_age:
                        print("Your father said he would support you, no matter what.")
                    adult()
            if ch == 3:
                if gender == 2:
                    adult()
                else:
                    gender = 0
                    is_trans = 1
                    print("You came out of the closet.")
                    if is_spouse == 1:
                        print("Your spouse left you.")
                        spouse = 0
                    if mother_end_age > mother_age:
                        print("Your mother said she would support you, no matter what.")
                    if father_end_age > father_age:
                        print("Your father said he would support you, no matter what.")
                    adult()
        else:
            adult()

    def love():
        global money, happiness, looks, health, intel, debt, spouse, is_spouse, is_smartphone
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age, is_spouse, spouse
        print("[0] Return")
        print("[1] Find Love")
        if is_smartphone == 1:
            print(f"[2] Dating App [{currency}100]")
            print(f"[3] Gay Dating App [{currency}100]")
        else:
            print("[Dating apps require a smartphone; buy one!]")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 1 or ch == 2 or ch == 3:
            if ch == 2 or ch == 3:
                if is_smartphone == 0:
                    adult()
            if ch == 1:
                find_love(1)
            elif ch == 2:
                dating_app(1)
            elif ch == 3:
                dating_app(0)
            if False:
                adult()
            else:
                div()
                is_spouse = 1
                happiness += 0.45
                print(f"You are now dating {spouse.name}.")
                if (
                    mother_end_age > mother_age
                    and father_end_age > father_age
                    and mother_rel >= 0.75
                    and father_rel >= 0.75
                ):
                    div()
                    print("Your mother congratulated you on finding a date.")
                    print("Your father did the same.")
                elif mother_age < mother_end_age:
                    if mother_rel >= 0.75 and mother_rel >= 0.75:
                        div()
                        print("Your mother congratulated you on finding a date.")
                elif father_end_age > father_age and father_rel >= 0.75:
                    div()
                    print("Your father congratulated you on finding a date.")
                adult()
        else:
            adult()

    def openlife_times():
        print("[1] ???")
        print("[2] ???")
        print("[3] ???")
        div()
        try:
            ch = int(input(">"))
        except:
            adult()
    def adoption():
        global money, pistol_count, knife_count, is_common_cold, flip_profits, children
        global is_smartphone, pistol_ammo, chainsaw_count, taser_count, lottery_wins
        global channel_name, subscribers, view_count, video_count, is_verif, is_opentube
        global money, is_monetised, watch_time, opentube_year, forename, surname
        global allow_debug, spouse, is_spouse, gender, friend_count, friend_1, friend_2, friend_3, is_wpp, wpp_name, fame, sentence, prison_years, juvie_years
        global child_count, child_1, child_2, child_3, child_4, child_5, child_6, child_7, child_8
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary, house_count, house_1, house_2, house_3
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age, mother_rel, father_rel
        # def __init__(self, name, age, rel, end, gender, intel, looks, craziness):
        adopt_1=Child()
        adopt_2=Child()
        adopt_3=Child()
        adopt_4=Child()
        adopt_5=Child()
        adopt_1.generate_random(rng(0,12),0)
        adopt_2.generate_random(rng(0,12),0)
        adopt_3.generate_random(rng(0,12),0)
        adopt_4.generate_random(rng(0,12),0)
        adopt_5.generate_random(rng(0,12),0)
        div()
        adopt_1.render(1)
        div()
        adopt_2.render(2)
        div()
        adopt_3.render(3)
        div()
        adopt_4.render(4)
        div()
        adopt_5.render(5)
        try:
            ch=int(input(">"))
        except:
            adult()
        div()
        if ch == 1:
            if money >= adopt_1.price:
                money -= adopt_1.price
                children.append(adopt_1)
                print(f"You are now the proud owner of {adopt_1.name}!")
            else:
                print("Cannot afford.")
        elif ch == 2:
            if money >= adopt_2.price:
                money -= adopt_2.price
                children.append(adopt_2)
                print(f"You are now the proud owner of {adopt_2.name}!")
            else:
                print("Cannot afford.")
        elif ch == 3:
            if money >= adopt_3.price:
                money -= adopt_3.price
                children.append(adopt_3)
                print(f"You are now the proud owner of {adopt_3.name}!")
            else:
                print("Cannot afford.")
        elif ch == 4:
            if money >= adopt_4.price:
                money -= adopt_4.price
                children.append(adopt_4)
                print(f"You are now the proud owner of {adopt_4.name}!")
            else:
                print("Cannot afford.")
        elif ch == 5:
            if money >= adopt_5.price:
                money -= adopt_5.price
                children.append(adopt_5)
                print(f"You are now the proud owner of {adopt_5.name}!")
            else:
                print("Cannot afford.")
        else:
            adult()
        adult()
    def research():
        global research_lab, pending_research, money, age, is_cancer
        # research_lab = [0,0,0,0,0] # [Unlocked lab, unlocked age-down, unlocked cure for cancer, unlocked immortality, unlocked stress resistance]
        if research_lab == [0,0,0,0,0]:
            print(f"[1] Buy Research Lab [{currency}1,000,000,000] [3 Years To Research]")
            print("[0] Return")
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 1:
                if money >= 1000000000:
                    money -= 1000000
                    pending_research = [1,3]
                    adult()
                else:
                    print(f"You need {currency}1,000,000,000 to buy a research lab")
                    adult()
            else:
                adult()
        elif research_lab[0] == 1:
            if research_lab[1] == 0:
                print(f"[1] Age-Down [{currency}45,000,000,000] [5 Years to Research] [If age > 38, pay {currency}1,000,000,000 to age down [20] years")
            if research_lab[1] == 1:
                if age >= 38:
                    print(f"[1] Age-Down [{currency}1,000,000,000] [Ages down [20] years]")
                else:
                    print("[x] [Age up to [38] to age down")
            if research_lab[2] == 0:
                print(f"[2] Cure For Cancer [{currency}55,000,000,000] [10 Years to Research] [Cures cancer if you get it]")
            if research_lab[2] == 1 and is_cancer == 1:
                print(f"[2] Cure Cancer [{currency}2,500,000,000]")
            if research_lab[3] == 0:
                print(f"[3] Immortality [{currency}150,000,000,000,000] [15 Years to Research] [Makes you immortal]")
            if research_lab[4] == 0:
                print(f"[4] Stress Resistance [{currency}150,000,000] [1 Year to Research [Halves your stress every year]")
            if pending_research[0] == 0 and pending_research[1] < 0:
                print(f"[5] Add funding to prevent bankrupcy [{currency}{'{:,}'.format(-(pending_research[1])*1000000000)}]")
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 1:
                if research_lab[1] == 0:
                    if money >= 45000000000:
                        money -= 45000000000
                        pending_research = [2,5]
                        adult()
                    else:
                        print(f"You need {currency}45,000,000,000 to do that!")
                        adult()
                elif research_lab[1] == 1 and age >= 38:
                    if money >= 1000000000:
                        money -= 1000000000
                        age -= 20
                        print(f"You successfully aged down from {age + 20} years old to {age}!")
                        adult()
                    else:
                        print(f"You need {currency}1,000,000,000 to age down!")
                else:
                    adult()
            elif ch == 2:
                if research_lab[2] == 0:
                    if money >= 55000000000:
                        money -= 55000000000
                        pending_research = [3,10]
                        adult()
                    else:
                        print(f"You need {currency}55,000,000,000 to research that!")
                        adult()
                
                elif research_lab[2] == 1 and is_cancer == 1:
                    if money >= 2500000000:
                        money -= 2500000000
                        is_cancer = 0
                        print("Your cancer was cured.")
                        adult()
                    else:
                        print(f"You need {currency}2,500,000,000 to cure cancer!")
                        adult()
                        
                else:
                    adult()
            elif ch == 3:
                if research_lab[3] == 0:
                    if money >= 150000000000000:
                        money -= 150000000000000
                        pending_research = [4,15]
                        print("Started researching IMMORTALITY.")
                        adult()
                    else:
                        print(f"You need {currency}150 Trillion to Research that!")
                        adult()
                else:
                    adult()
            elif ch == 4 and research_lab[4] == 0:
                if money >= 150000000:
                    money -= 150000
                    pending_research = [5,1]
                    print("You began researching STRESS RESISTANCE.")
                    adult()
            elif ch == 5 and pending_research[0] == 0 and pending_research[1] < 0:
                if money >= -(pending_research[1]) * 1000000000:
                    money -= (-(pending_research[1]) * 1000000000)
                    pending_research = [0,0]
                    div()
                    print("Your facility can keep going for 15 years without research.")
                    adult()
                else:
                    div()
                    print("Cannot afford!")
                    adult()
            else:
                # Add more research options
                adult()
        else:
            adult()
    def license_centre():
        global driver_license, boat_license, gun_license, pilot_license, money, debt
        if driver_license == 1 and boat_license == 1 and gun_license and pilot_license == 1:
            adult()
        if driver_license == 0:
            print(f"[1] Driver's License [{currency}55]")
        if boat_license == 0:
            print(f"[2] Boating License [{currency}60]")
        if gun_license == 0:
            print(f"[3] Gun License [{currency}100]")
        if pilot_license == 0:
            print(F"[4] Pilot License [{currency}2,000]")
        try:
            ch=int(input(">"))
        except:
            adult()
        if ch == 1 and driver_license == 0:
            if money >= 55:
                money -= 55
            else:
                debt += 55
            driver_license = 1
            print("You passed your driving test!")
            adult()
        elif ch == 2 and boat_license == 0:
            if money >= 60:
                money -= 60
                boat_license = 1
                print("You passed your boating test!")
            else:
                debt += 60
                boat_license = 1
                print("You passed your boating test!")
            adult()
        elif ch == 3 and gun_license == 0:
            if money >= 100:
                money -= 100
                gun_license = 1
                print("You got a gun license!")
            else:
                print(f"You need {currency}100 to pass a test!")
            adult()
        elif ch == 4 and pilot_license == 0:
            if money >= 2000:
                money -= 2000
                pilot_license = 1
                print("You passed your pilot's test!")
            else:
                debt += 2000
                pilot_license = 1
                print("You passed your pilot's test!")
            adult()
        else:
            adult()
    def hire_surgeons():
        global surgeons, allow_debug
        s1=PlasticSurgeon()
        s2=PlasticSurgeon()
        s3=PlasticSurgeon()
        s1.compile(1)
        s2.compile(2)
        s3.compile(3)
        s1.list(1)
        s2.list(1)
        s3.list(1)
        div()
        try:
            ch=int(input(">"))
        except:
            hire_surgeons()
        if ch == 1:
            surgeons.append(s1)
        elif ch == 2:
            surgeons.append(s2)
        elif ch == 3:
            surgeons.append(s3)
        else:
            adult()
        if allow_debug != 0:
            print(surgeons)
        adult()
    def ol_times():
        url = "https://winfan3672.000webhostapp.com/openlife_times_v1/latest.article"
        import urllib.request
        try:
            print("Downloading...")
            urllib.request.urlretrieve(url, "latest.article")
            f=open("latest.article","r")
            data=f.read()
            f.close()
        except:
            div()
            print("Failed to download news.")
            return None
        cls()
        div()
        print(data)
        br()
    def adult_activities(ch=""):
        clear_screen()
        global money, happiness, looks, health, intel, debt, auto_deposit, allow_debug, job_id, prison_years, sentence, is_wpp, gender, view_count, subscribers, video_count, is_opentube
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary, surgeons, pending_research
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age, fame
        print("[0] Return")
        print(f"[1] Gym [{currency}15]")
        print("[2] Library")
        print("[3] Doctor")
        print("[4] Surrender")
        print("[5] Debug Menu")
        print("[6] Crime")
        print("[7] Adoption")
        print("[8] Hired Services")
        print("[9] Casino")
        print("[10] Identity")
        print("[11] Licenses")
        print("[x] Lawsuit")
        print("[13] Lottery")
        print("[14] Love")
        print("[x] Movies")
        print("[x] Nightlife")
        print("[17] Vacation")
        print("[x] Last Will And Testament")
        if gender == 0:
            print("[19] Fertility")
        if fame > 0:
            print("[20] Fame")
            if is_wpp == 0:
                print("[21] Witness Protection Program")
        print("[22] Make Friends")
        if debt > ((money + savings) * 2):
            print("[23] Personal Banklrupcy")
        print("[24] Research Lab")
        print("[25] OpenLife Times")
        if ch == "":
            try:
                ch = int(input(">"))
            except:
                adult()
        if ch == 0:
            adult()
        elif ch == 20 and fame > 0:
            fame_menu()
        elif ch == 7:
            adoption()
        elif ch == 11:
            license_centre()
        elif ch == 23:
            if debt > (money + savings) * 2:
                print("Are you sure you want to file for personal bankrupcy?")
                print("[-] Your debt will be written off")
                print("[-] You'll lose your job, degree, pension and OpenTube channel.")
                print("[-] You'll lose your house[s]")
                print("[-] Your fame drops to 0%")
                print("[-] You will be broke")
                div()
                print("[1] YES")
                print("[0] GOD NO")
                div()
                try:
                    ch = int(input(">"))
                except:
                    adult()
                if ch == 1:
                    personal_bankrupcy()
                else:
                    adult()
        elif ch == 25:
            ol_times()
            adult()
        elif ch == 8:
            div()
            print("[1] Plastic Surgeon")
            print("[0] Return")
            div()
            try:
                ch=int(input(">"))
            except:
                adult_activities()
            if ch == 1:
                if len(surgeons) == 0:
                    hire_surgeons()
                elif len(surgeons) == 1:
                    surgeons[0].interact()
                else:
                    adult()
            else:
                adult()
        elif ch == 22:
            gg = rng(0, 1)
            friend = Friend()
            friend.generate(pickname(gg), rng(18, age), gg)
            print(friend.name)
            print("Age:", friend.age)
            div()
            print("Smarts   :", pbar2(friend.intel))
            print("Looks    :", pbar2(friend.looks))
            print("Craziness:", pbar2(friend.craziness))
            div()
            print("[1] Make Friend")
            print("[2] Choose Another")
            print("[0] Return")
            div()
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 1:
                global friend_count, friend_1, friend_2, friend_3
                friend_count += 1
                if friend_count == 1:
                    friend_1 = friend
                elif friend_count == 2:
                    friend_2 = friend
                elif friend_count == 3:
                    friend_3 = friend
                else:
                    print("You can only have 3 friends at a time.")
            elif ch == 2:
                adult_activities(22)
            else:
                adult()
        elif ch == 24:
            if pending_research[1] <= 0:
                research()
            else:
                div()
                print("There is currently research ongoing.")
                print(f"Years left: {pending_research[1]}")
                br()
                adult()
        elif ch == 21 and is_wpp == 0 and fame >= 1:
            global forename_m, forename_f, surnames, is_spouse, is_spouse, name, wpp_name, is_depressed, wpp_year, his_her, he_she, him_her, is_opentube
            if fame == 1 and is_wpp == 0:
                print("[1] Enter WPP")
            print("[0] Return")
            div()
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 1 and fame == 1 and is_wpp == 0:
                div()
                wpp_year = year - age
                if gender == 0 or gender == 1:
                    was_were = "was"
                else:
                    was_were = "were"

                if gender == 0:
                    him_her = "him"
                elif gender == 0:
                    him_her = "her"
                else:
                    him_her = "their"

                if gender == 0:
                    he_she = "he"
                elif gender == 1:
                    he_she = "she"
                else:
                    he_she = "they"

                if gender == 0:
                    his_her = "his"
                elif gender == 1:
                    his_her = "her"
                else:
                    his_her = "their"

                print(f"{game_name} Times")
                print("The *best* newspaper since 2022 AD")
                div()
                print(f"{forename} {surname} dies of heart attack aged {age}")
                div()
                print(
                    f"Last night, while lying in bed in {his_her} 12-bedroom hotel room in Vegas,"
                )
                print(
                    f"{forename} {surname} passed away as a result of a heart attack."
                )
                if gender == 0:
                    print(
                        f"He was found by hotel employees when they heard 'a very loud bang sound' and came to investigate."
                    )
                elif gender == 1:
                    print(
                        f"She was found by hotel employees when they heard 'a very loud bang sound' and came to investigate."
                    )
                else:
                    print(
                        f"They were found by hotel employees when they heard 'a very loud bang sound' and came to investigate."
                    )
                print(
                    f"When they found {him_her}, {he_she} {was_were} lying on the floor of the hotel room's master bedroom, and were immediately rushed to hospital."
                )
                print(
                    f"Attempts to revive {him_her} at the Las Vegas {game_name} Hospital were unsuccessful."
                )
                print(
                    f"\nReports have come out that {forename} {surname} was an avid fan of pharmaceuticals,"
                )
                print(
                    f"and a whopping 32 drugs were detected in {his_her} system when {he_she} died."
                )
                print(
                    f"It is obvious that {his_her} heart attack was caused by an overdose on pharmaceutical drugs,"
                )
                print(
                    f"as evident in the fact that over 90x the safe limit of codiene was detected in {his_her} bloodstream."
                )
                print(
                    f"Alongside codeine, various other substances were found in {his_her} blood, such as morphine and demerol, a popular opioid pain medication."
                )
                if is_depressed == 1:
                    print(
                        f"On top of all of the prescription medication in {his_her} blood, Fluoxetine (sold as Prozac), a popular antidepressant, was also found in alarming quantities."
                    )
                    print(
                        f"This suggests that {he_she} {was_were} either depressed or addicted to the substance."
                    )
                print(
                    f"\nMay this be a lesson on the danger of self-medication and not consulting a doctor for medical advice."
                )
                print(
                    f"Speaking of doctors, {forename}'s doctor, Dr. {choice(forename_m)} {choice(surnames)}, is being charged with overprescribing {forename} with dosages of medicines that 'no reasonable doctor would prescribe'."
                )
                print(
                    f"\nMay {he_she} rest in peace, loved by {his_her} millions of adoring fans."
                )
                div()
                print(f"{forename} {surname}")
                print(f"{wpp_year}-{year}")
                br()
                print(
                    "FBI AGENT: You are officially dead. You can now safely retire. We will protect your deceased status, but it is YOUR responsibility to make sure you're not spotted."
                )
                sleep(4)
                print(
                    "FBI AGENT: If you're spotted, we'll do out best to cover it up, but no guarantees."
                )
                sleep(3)
                print(f"{forename.upper()} {surname.upper()}: And if I admit it?")
                sleep(1)
                print("FBI AGENT: We have an NDA. Prepare to get sued.")
                sleep(2)
                print(
                    f"{forename.upper()} {surname.upper()}: And if someone looks at my FBI files?"
                )
                sleep(2)
                print("FBI AGENT: They'll remain classified until you *actually* die.")
                sleep(2)
                print("FBI AGENT: Good luck.")
                sleep(1)
                div()
                print(
                    "You have now entered the Witness Protection Program. You will receive a new name and new life."
                )
                print(
                    "The only people who will be aware of your new identity are your parents."
                )
                print("You will have to leave your spouse.")
                br()
                is_wpp = 1
                fame = 0
                job_id = 0
                sentence = 0
                money += savings
                savings = 0
                money -= int(money / 8)
                savings += money
                money = 0
                prison_years = 0
                is_spouse = 0
                friend_count = 0
                debt = 0
                wpp_name = [forename, surname]
                if gender == 0:
                    forename = choice(forename_m)
                else:
                    forename = choice(forename_f)
                surname = choice(surnames)
                is_spouse = 0
                name = forename + " " + surname
                if is_opentube == 1:
                    delete_channel()
                else:
                    adult()
            else:
                if is_opentube == 1:
                    delete_channel()
                else:
                    adult()
        elif ch == 1:
            div()
            print("You went to the gym.")
            print("Enjoyment:")
            if money >= 15:
                money -= 15
            else:
                debt += 15
            pbar(1)
            happiness += 0.45
            health += 0.25
            adult()
        elif ch == 2:
            div()
            print("You visited the library.")
            print("Enjoyment:")
            pbar(0)
            intel += 0.25
            happiness -= 0.45
            adult()
        elif ch == 3:
            doctor_adult()
        elif ch == 4:
            print("[1] Surrender")
            print("[0] Return")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            elif ch == 1:
                die(0)
            else:
                adult()
        elif ch == 5:
            div()
            print("Hidden ethics value:")
            pbar(ethics)
            div()
            print("[0] Return")
            print("[1] Max out looks")
            if allow_debug == 1:
                print("[2] Set Money")
                print("[x] Max Out Ethics")
            print("[4] Show Death Ages")
            # if allow_debug == 1:
            #    print("[5] Fix Alpha 12 PR3 Save File")
            print("[6] Set AutoDeposit")
            print("[7] AllowDebug3")
            print("[8] Go To Prison")
            print("[9] Generate [10] Children")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            elif ch == 9:
                for i in range(10):
                    global children
                    base=Child()
                    base.generate_random()
                    children.append(base)
            elif ch == 7:
                if allow_debug == 3:
                    allow_debug = 0
                else:
                    allow_debug = 3
            elif ch == 1:
                looks = 1
                adult()
            elif ch == 2:
                if allow_debug == 1:
                    try:
                        money = int(input(">"))
                    except:
                        adult()
                else:
                    adult()
            elif ch == 6:
                try:
                    auto_deposit = int(input(">"))
                except:
                    auto_deposit = 0
                adult()
            elif ch == 5 and allow_debug == 1:
                print("WIP")
                div()
                print("Available saves:")
                path = os.getcwd()
                dirlist = os.listdir(path)
                for item in dirlist:
                    isFile = os.path.isfile(item)
                    if isFile == True and item.endswith(".oll2"):
                        item = item.replace(".oll2", "")
                        print(item)
                    else:
                        continue
                div()
                # 0=Alpha|1=12|2=happiness|3=health|4=intel|5=looks|6=ethics|7=money
                # |8=forename|9=surname|10=age|11=work_e|12=edu_lvl|13=work_e_base|14=promo_base
                # |15=degree|16=hours|17=salary|18=expenses|19=pension
                # |20=is_depressed|21=debt|22=savings|23=year|24=is_job|25=stress
                # |26=mother_name|27=father_name|28=mother_age|29=father_age
                # |30=mother_end_age|31=father_end_age
                sn = input("Enter File Name >")
                # Windows illegal filename characters removed
                sn = sn.replace("\\", "")
                sn = sn.replace("/", "")
                sn = sn.replace("?", "")
                sn = sn.replace("*", "")
                sn = sn.replace("|", "")
                sn = sn.replace("<", "")
                sn = sn.replace(">", "")
                sn = sn.replace(":", "")
                sn = sn.replace('"', "")
                sn += ".oll2"  # file extension
                f = open(sn, "rb")
                try:
                    import codecs

                    ssave = f.read()
                    f.close()
                    ssave = codecs.decode(ssave, "base64_codec")
                    print(save)
                    ssave = ssave.decode("utf-8")
                    print(save)
                    save = ssave
                    print(save)
                    save += "|0"
                    save = save.encode("utf-8")
                    save = codecs.encode(save, "base64_codec")
                    f = open(fn, "wb")
                    f.write(save)
                    f.close()
                    div()
                    print("Save now no longer breaks Freelance section.")
                except:
                    div()
                    print("Failed.")
                    adult()
            elif ch == 3:
                adult()
            elif ch == 4:
                div()
                global mother_end_age, father_end_age, mother_age, father_age
                if mother_age < mother_end_age:
                    print(
                        "Mother will die at age",
                        mother_end_age,
                        "[Current age: " + str(mother_age) + "]",
                    )
                if father_age < father_end_age:
                    print(
                        "Father will die at age",
                        father_end_age,
                        "[Current age: " + str(father_age) + "]",
                    )
                if is_spouse == 1:
                    if spouse.end < spouse.end:
                        print(
                            "Spouse will die at age",
                            spouse.end,
                            "[Current age: " + str(spouse.age) + "]",
                        )

                br()
                adult()
            elif ch == 8:
                global offences
                offences += 1
                go_to_prison()
            else:
                adult()
            adult()
        elif ch == 6:
            crime()
        elif ch == 13:
            lottery(0)
        elif ch == 17:
            vacation()
        elif ch == 10:
            identity()
        elif ch == 9:
            if debt > 0:
                div()
                print("BOUNCER: Sorry. We cannot let in people who owe us money.")
                print("YOU: But I don't owe YOU money, I owe someone else money!")
                print("BOUNCER: Too bad.")
                br()
                adult()
            blackjack_init()
        elif ch == 14:
            love()
        elif ch == 16:
            print("[1] Partying")
            print("[x] One-Night Stand")
            print("[3] Drugs")
            print("[0] Return")
            div()
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            if ch == 1:
                print("You partied.")
                print("Enjoyment:")
                pbar(0.85)
                happiness += 0.65
                health -= 0.15
                intel -= 0.25
                adult()
            elif ch == 3:
                print("[1] Cannabis")
                print("[2] Cocaine")
                print("[3] Heroin")
                print("[4] Gym Candy [Anabolic Stereoids]")
                print("[5] Crack")
                try:
                    ch = int(input(">"))
                except:
                    ch = 0
                if ch == 0:
                    adult()
                else:
                    adult()
            else:
                adult()
        elif ch == 19 and gender == 0:
            print("[0] Return")
            if age < 45:
                print("[1] Sperm Donation")
            print(f"[x] Vascetomy [{currency}25 000]")
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 0:
                adult()
            elif ch == 1 and age < 45:
                div()
                print("You donated sperm :(")
                print(f"You earned {currency}25")
                money += 25
                adult()
            else:
                # this one
                adult()
        else:
            # this one
            adult()

    def promotion():
        global job_id, job_lvl, promo_base, salary
        if (
            job_id == 1
            or job_id == 4
            or job_id == 11
            or job_id == 14
            or job_id == 17
            or job_id == 19
            or job_id == 21
            or job_id == 22
            or job_id == 26
            or job_id == 28
            or job_id == 29
            or job_id == 30
        ):
            job_lvl == 1
            adult()
        elif job_id == 18:
            if job_lvl == 2:
                adult()
            else:
                salary = 65
        elif job_id == 18:
            if job_lvl == 23:
                adult()
            else:
                salary = 35
        elif job_lvl < 3:
            job_lvl += 1
            print("You got promoted.")
            if job_id == 2:
                if job_lvl == 2:
                    salary = 15
                else:
                    salary = 20
            elif job_id == 3:
                if job_lvl == 2:
                    salary = 40
                else:
                    salary = 50
            elif job_id == 6:
                if job_lvl == 2:
                    salary = 50
                else:
                    salary = 70
            elif job_id == 8:
                if job_lvl == 2:
                    salary = 70
                else:
                    salary = 90
            elif job_id == 9:
                if job_lvl == 2:
                    salary = 55
                else:
                    salary = 65
            elif job_id == 10:
                if job_lvl == 2:
                    salary = 45
                else:
                    salary = 55
            elif job_id == 12:
                if job_lvl == 2:
                    salary = 40
                else:
                    salary = 55
            elif job_id == 13:
                if job_lvl == 2:
                    salary = 75
                else:
                    salary = 95
            elif job_id == 15:
                if job_lvl == 2:
                    salary = 45
                else:
                    salary = 65
            elif job_id == 20:
                if job_lvl == 2:
                    salary = 55
                else:
                    salary = 75
            elif job_id == 25:
                if job_lvl == 2:
                    salary = 35
                else:
                    salary = 45
            elif job_id == 0:
                adult()
            print(f"New Salary: {currency}" + str(salary))
            br()
            adult()
        else:
            adult()

    def job_menu():
        global is_job, salary, hours, min_hours, work_e_base, pension
        print("[0] Return")
        print("[1] Resign")
        print("[2] Adjust Hours")
        if work_e_base >= 20:
            print("[3] Retire & Take Pension")
        print("[x] Request Raise")
        print("[x] Request Promotion")
        print("[6] Co-Worker Interaction")
        div()
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        elif ch == 1:
            div()
            print("You resigned :(")
            salary = 0
            is_job = 0
            hours = 0
            work_e_base = 0
        elif ch == 2:
            try:
                hours = int(input(">"))
            except:
                pass
            if hours < min_hours:
                hours = min_hours
            if hours > 70:
                hours = 70
            adult()
        elif ch == 3 and work_e_base >= 20:
            div()
            pension_questions()
            base = salary * hours * 52
            base /= 2
            base = int(base)
            print(
                f"Your pension is {currency}" + str("{:,}".format((base))), "per year."
            )
            pension += base
            salary = 0
            is_job = 0
            hours = 0
            work_e_base = 0
            adult()
        elif ch == 6:
            coworker_list()
        else:
            adult()

    def adult_item_list():
        print("Items:")
        div()
        for i in range(knife_count):
            print("1x Knife")
        for i in range(pistol_count):
            print("1x Pistol")
        if pistol_ammo > 0:
            print(f"{pistol_ammo}x Pistol Ammo")
        for i in range(chainsaw_count):
            print("1x Chainsaw")
        for i in range(taser_count):
            print("1x Taser")
        if is_smartphone == 1:
            print("1x Smartphone")
        if (
            pistol_count == 0
            and knife_count == 0
            and taser_count == 0
            and chainsaw_count == 0
            and is_smartphone == 0
        ):
            print("[No items to show]")
        br()
        adult()

    def adult_shop():
        global money, pistol_count, knife_count
        global is_smartphone, pistol_ammo, chainsaw_count, taser_count
        print(f"[1] 1x Knife [{currency}25]")
        print(f"[2] 1x Pistol [{currency}750]")
        print(f"[3] 100x Pistol Ammo [{currency}250]")
        print(f"[4] 1x Chainaw [{currency}1000]")
        print(f"[5] 1x Taser [{currency}500]")
        if is_smartphone == 0:
            print(f"[6] 1x Smartphone [{currency}750]")
        div()
        try:
            ch = int(input(">"))
        except:
            adult()
        div()
        if ch == 1:
            if money >= 25:
                money -= 25
                knife_count += 1
                print("Purchase successful.")
                adult()
            else:
                print(f"Cannot afford item.")
                adult()
        elif ch == 2:
            if money >= 750:
                money -= 750
                pistol_count += 1
                print("Purchase successful.")
                adult()
            else:
                print(f"Cannot afford item.")
                adult()
        elif ch == 3:
            if money >= 250:
                money -= 250
                pistol_ammo += 100
                print("Purchase successful.")
                adult()
            else:
                print(f"Cannot afford item.")
                adult()
        elif ch == 4:
            if money >= 1000:
                money -= 1000
                chainsaw_count += 1
                print("Purchase successful.")
                adult()
            else:
                print(f"Cannot afford item.")
                adult()
        elif ch == 5:
            if money >= 500:
                money -= 500
                taser_count += 1
                print("Purchase successful.")
                adult()
            else:
                print(f"Cannot afford item.")
                adult()
        elif ch == 6 and is_smartphone == 0:
            if money >= 750:
                money -= 750
                is_smartphone = 1
                print("Purchase successful.")
                adult()
            else:
                print(f"Cannot afford item.")
                adult()
        else:
            adult()
    def plane_hangar():
        global money, vehicles, allow_debug
        # There are 3 types:
        # Type 1: Consumer
        # Type 2: Private
        # type 3: Military

        # Type 1 Models
        ## Boing 737
        ## Boing 747
        ## Airbuss A320
        ## Airbuss A340

        # Type 2 models
        ## Cessna 172 Skyhawk
        ## Embracer Predator 520

        # Type 3 Models
        ## Gumman F-14 Tompatt
        plane_1=Plane()
        plane_2=Plane()
        plane_3=Plane()
        t=rng(1,3)
        if t == 1:
            m=rng(1,4)
        elif t == 2:
            m=rng(1,2)
        else:
            m=1
        models=[
            ["Unknown Plane Model"],
            ["Unknown Plane Model","Boing 737","Boing 747","Airbuss A320","Airbuss A340"],
            ["Unknown Plane Model","Cessna 172 Skyhawk","Embracer Predator 520"],
            ["Unknown Plane Model","Gumman F-14 Tompatt"],
        ]
        if [t,m] == [1,1]:
            p = 150000000
        elif [t,m] == [1,2]:
            p = 250000000
        elif [t,m] == [1,3]:
            p = 175000000
        elif [t,m] == [1,4]:
            p = 275000000
        elif [t,m] == [2,1]:
            p = 15000
        elif [t,m] == [2,2]:
            p = 15000000
        elif [t,m] == [3,1]:
            p = 77777777
        plane_1.compile(t,m,p)
        t=rng(1,3)
        if t == 1:
            m=rng(1,4)
        elif t == 2:
            m=rng(1,2)
        else:
            m=1
        if [t,m] == [1,1]:
            p = 150000000
        elif [t,m] == [1,2]:
            p = 250000000
        elif [t,m] == [1,3]:
            p = 175000000
        elif [t,m] == [1,4]:
            p = 275000000
        elif [t,m] == [2,1]:
            p = 15000
        elif [t,m] == [2,2]:
            p = 15000000
        elif [t,m] == [3,1]:
            p = 77777777
        plane_2.compile(t,m,p)
        t=rng(1,3)
        if t == 1:
            m=rng(1,4)
        elif t == 2:
            m=rng(1,2)
        else:
            m=1
        if [t,m] == [1,1]:
            p = 150000000
        elif [t,m] == [1,2]:
            p = 250000000
        elif [t,m] == [1,3]:
            p = 175000000
        elif [t,m] == [1,4]:
            p = 275000000
        elif [t,m] == [2,1]:
            p = 15000
        elif [t,m] == [2,2]:
            p = 15000000
        elif [t,m] == [3,1]:
            p = 77777777
        plane_3.compile(t,m,p)
        plane_1.list(1,1)
        plane_2.list(1,2)
        plane_3.list(1,3)
        div()
        try:
            ch=int(input(">"))
        except:
            plane_hangar()
        if ch == 1:
            money -= plane_1.price
            plane_1.name(input("Plane Name >>"))
            vehicles[2].append(plane_1)
        elif ch == 2:
            money -= plane_2.price
            plane_2.name(input("Plane Name >>"))
            vehicles[2].append(plane_2)
        elif ch == 3:
            money -= plane_3.price
            plane_3.name(input("Plane Name >>"))
            vehicles[2].append(plane_3)
        print("Purchase Successful!")
        if allow_debug != 0:
            print(vehicles)
        adult()
    def boat_list():
        global vehicles
        n = 1
        for item in vehicles[1]:
            item.list(n)
        try:
            ch=int(input(">"))
        except:
            adult()
        try:
            vehicles[1][ch-1].interact()
        except:
            adult()
    def boat_pier():
        global vehicles, money, debt
        boat_1=Boat()
        boat_2=Boat()
        boat_3=Boat()
        boat_4=Boat()
        boat_5=Boat()
        boat_1.compile("N",rng(1,5))
        boat_2.compile("N",rng(1,5))
        boat_3.compile("N",rng(1,5))
        boat_4.compile("N",rng(1,5))
        boat_5.compile("N",rng(1,5))
        boat_1.list(1,0)
        boat_2.list(2,0)
        boat_3.list(3,0)
        boat_4.list(4,0)
        boat_5.list(5,0)
        print("[0] Return")
        div()
        try:
            ch=int(input(">"))
        except:
            boat_pier()
        if ch == 1:
            if money >= boat_1.price:
                money -= boat_1.price
            else:
                debt += boat_1.price
            vehicles[1].append(boat_1)
            print("Purchase successful.")
            boat_1.pick_name(input("Enter Boat Name >>").replace("|",""))
            adult()
        elif ch == 2:
            if money >= boat_2.price:
                money -= boat_2.price
            else:
                debt += boat_2.price
            vehicles[1].append(boat_2)
            print("Purchase successful.")
            boat_2.pick_name(input("Enter Boat Name >>").replace("|",""))
            adult()
        elif ch == 3:
            if money >= boat_3.price:
                money -= boat_3.price
            else:
                debt += boat_3.price
            vehicles[1].append(boat_3)
            print("Purchase successful.")
            boat_3.pick_name(input("Enter Boat Name >>").replace("|",""))
            adult()
        elif ch == 4:
            if money >= boat_4.price:
                money -= boat_4.price
            else:
                debt += boat_4.price
            vehicles[1].append(boat_4)
            print("Purchase successful.")
            boat_4.pick_name(input("Enter Boat Name >>").replace("|",""))
            adult()
        elif ch == 5:
            if money >= boat_5.price:
                money -= boat_5.price
            else:
                debt += boat_5.price
            vehicles[1].append(boat_5)
            print("Purchase successful.")
            boat_5.pick_name(input("Enter Boat Name >>"))
            adult()
        else:
            adult()
    def steal_cars():
        car_1 = Car()
        car_2 = Car()
        car_3 = Car()
        car_4 = Car()
        car_5 = Car()

        # Compile cars
        for i in range(4):
            typ = rng(1,8)
            if typ == 1:
                model = rng(1,5)
            if typ == 2:
                model = rng(1,6)
            if typ == 3:
                model = rng(1,3)
            if typ == 4:
                model = rng(1,2)
            if typ == 5:
                model = rng(1,6)
            if typ == 6:
                model = rng(1,6)
            if typ == 7:
                model = rng(1,5)
            if typ == 8:
                model = rng(1,4)
            
            if typ == 1:
                if model == 1:
                    price = 45000
                elif model == 2:
                    price = 35000
                elif model == 3:
                    price = 25000
                elif model == 4:
                    price = 20000
                elif model == 5:
                    price = 75000
                else:
                    price = None
            elif typ == 2:
                if model == 1:
                    price = 11000
                elif model == 2:
                    price = 45000
                elif model == 3:
                    price = 30000
                elif model == 4:
                    price = 15000
                elif model == 5:
                    price = 55000
                elif model == 6:
                    price = 16500
            elif typ == 3:
                if model == 1:
                    price = 11000
                elif model == 2:
                    price = 12000
                elif model == 3:
                    price = 14000
            elif typ == 4:
                if model == 1:
                    price = 40000
                else:
                    price = 67000
            elif typ == 5:
                if model == 1:
                    price = 56000
                elif model == 2:
                    price = 67000
                elif model == 3:
                    price = 99000
                elif model == 4:
                    price = 150000
                elif model == 5:
                    price = 45000
                elif model == 6:
                    price = 25000
                else:
                    price = None
            elif typ == 6:
                if model == 1:
                    price = 1250000
                elif model == 2:
                    price = 1000000
                elif model == 3:
                    price = 750000
                elif model == 4 or model == 5:
                    price = 1750000
                elif model == 6:
                    price = 1650000
                else:
                    price = None
            elif typ == 7:
                if model == 1:
                    price = 2500000
                elif model == 2:
                    price = 4500000
                elif model == 3:
                    price = 10000000
                elif model == 4:
                    price = 135000
                elif model == 5:
                    price = 350000
                else:
                    price = None
            else:
                price = model * 25000000
            if i == 1:
                car_1.compile("",price, typ, model,1)
            elif i == 2:
                car_2.compile("",price, typ, model,1)
            elif i == 3:
                car_3.compile("",price, typ, model,1)
            else:
                continue
        div()
        car_1.render_stolen(1)
        car_2.render_stolen(2)
        car_3.render_stolen(3)
        print("[0] Return")
        div()
        try:
            ch = int(input(">"))
        except:
            adult()
        try:
            if ch == 1:
                vehicles[0].append(car_1)
            elif ch == 2:
                vehicles[0].append(car_2)
            elif ch == 3:
                vehicles[0].append(car_3)
            else:
                adult()
        except:
            adult()
    def car_showroom():
        global money, vehicles, debt
        car_1 = Car()
        car_2 = Car()
        car_3 = Car()
        car_4 = Car()
        car_5 = Car()
        # Type 1 = Standard
        # Type 2 = Sedan
        # Type 3 = Coupe
        # Type 4 = SUV
        # Type 5 = EV
        # Type 6 = Exotic
        # Type 7 = Sports
        # Type 8 = F1

        # Type 1 Models:
        ## Model 1 = BWM Beetle
        ## Model 2 = WV Chiron
        ## Model 3 = Mini Smart
        ## Model 4 = Smart Mini
        ## Model 5 = OpenMotors Model 3000

        # Type 2 Models:
        ## Model 1 = Chevollet Monte Carlo
        ## Model 2 = Holder Accorda
        ## Model 3 = Holder Civil
        ## Model 4 = Handai Santa Fe
        ## Model 5 = Merchant C-Class
        ## Model 6 = Kai Sorrento

        # Type 3 Models:
        ## 1 = Totoya GT99
        ## 2 = Chervolle Corvette
        ## 3 = Dodgem Challenger

        # Type 4 Models:
        ## 1 = Mars Rover 3000
        ## 2 = Fodr Mustang

        # Type 5 Models:
        ## Nikola Model S
        ## Nikola Model X
        ## Nikola Model Y
        ## Nikola Cybertruck
        ## BWM Electric Beetle
        ## OpenMotors Model 3500

        # Type 6 Models:
        ## McLaid Senna
        ## McLaid 4500
        ## OpenMotors Exotic Mk. III
        ## Fodr Xtra
        ## Holder Xartra
        ## OpenMotors Electric Mk. II

        # Type 7 Models:
        ## OpenMotors RubberScreech Mk. VII
        ## Ferry LVXI
        ## Bourgeoise  Lavish
        ## Landbp Avenger
        ## Doppelsieg Motorworks Silver Clar Mk. II

        # Type 8 Models:
        ## F1 Mk. I
        ## F1 Mk. II
        ## F1 Mk. III
        ## F1 Mk. I

        # Compile cars
        for i in range(4):
            typ = rng(1,8)
            if typ == 1:
                model = rng(1,5)
            if typ == 2:
                model = rng(1,6)
            if typ == 3:
                model = rng(1,3)
            if typ == 4:
                model = rng(1,2)
            if typ == 5:
                model = rng(1,6)
            if typ == 6:
                model = rng(1,6)
            if typ == 7:
                model = rng(1,5)
            if typ == 8:
                model = rng(1,4)
            
            if typ == 1:
                if model == 1:
                    price = 45000
                elif model == 2:
                    price = 35000
                elif model == 3:
                    price = 25000
                elif model == 4:
                    price = 20000
                elif model == 5:
                    price = 75000
                else:
                    price = None
            elif typ == 2:
                if model == 1:
                    price = 11000
                elif model == 2:
                    price = 45000
                elif model == 3:
                    price = 30000
                elif model == 4:
                    price = 15000
                elif model == 5:
                    price = 55000
                elif model == 6:
                    price = 16500
            elif typ == 3:
                if model == 1:
                    price = 11000
                elif model == 2:
                    price = 12000
                elif model == 3:
                    price = 14000
            elif typ == 4:
                if model == 1:
                    price = 40000
                else:
                    price = 67000
            elif typ == 5:
                if model == 1:
                    price = 56000
                elif model == 2:
                    price = 67000
                elif model == 3:
                    price = 99000
                elif model == 4:
                    price = 150000
                elif model == 5:
                    price = 45000
                elif model == 6:
                    price = 25000
                else:
                    price = None
            elif typ == 6:
                if model == 1:
                    price = 1250000
                elif model == 2:
                    price = 1000000
                elif model == 3:
                    price = 750000
                elif model == 4 or model == 5:
                    price = 1750000
                elif model == 6:
                    price = 1650000
                else:
                    price = None
            elif typ == 7:
                if model == 1:
                    price = 2500000
                elif model == 2:
                    price = 4500000
                elif model == 3:
                    price = 10000000
                elif model == 4:
                    price = 135000
                elif model == 5:
                    price = 350000
                else:
                    price = None
            else:
                price = model * 25000000
            if i == 1:
                car_1.compile("",price, typ, model)
            elif i == 2:
                car_2.compile("",price, typ, model)
            elif i == 3:
                car_3.compile("",price, typ, model)
            else:
                continue
        car_1.render(1)
        car_2.render(2)
        car_3.render(3)
        div()
        try:
            ch=int(input(">"))
        except:
            adult()
        if ch == 1:
            if money >= car_1.price:
                money -= car_1.price
            else:
                debt += car_1.price
            vehicles[0].append(car_1)
            print("Purchase successful.")
        elif ch == 2:
            if money >= car_2.price:
                money -= car_2.price
            else:
                debt += car_2.price
            vehicles[0].append(car_2)
            print("Purchase successful.")
        elif ch == 3:
            if money >= car_3.price:
                money -= car_3.price
            else:
                debt += car_3.price
            vehicles[0].append(car_3)
            print("Purchase successful.")
        if allow_debug != 0:
            print(vehicles)
        adult()
    def plane_list():
        global vehicles
        n = 1
        for item in vehicles[2]:
            item.list(0,n)
            n += 1
        div()
        try:
            ch = int(input(">"))
        except:
            adult()
        if ch > 0 and ch <= len(vehicles[2]):
            vehicles[2][ch-1].interact()
        else:
            adult()
    def car_list():
        global vehicles
        n = 1
        for item in vehicles[0]:
            item.list(n)
            n += 1
        div()
        try:
            ch = int(input(">"))
        except:
            adult()
        if ch > 0 and ch <= len(vehicles[0]):
            vehicles[0][ch-1].interact()
        else:
            adult()
    def adult_assets():
        clear_screen()
        global money, savings, debt, auto_deposit, flip_profits, vehicles, driver_license, pilot_license, boat_license
        print(f"Money:        {currency}" + str("{:,}".format((int(money)))))
        print(f"Debt:         {currency}" + str("{:,}".format((int(debt)))))
        print(f"Savings:      {currency}" + str("{:,}".format((int(savings)))))
        print(f"Flip Profits: {currency}" + str("{:,}".format((int(flip_profits)))))

        div()
        print("[0] Return")
        print("[1] Shop")
        print("[2] Item List")
        print("[3] Loan")
        print("[4] Savings")
        div()
        print("[5] Buy Houses")
        if len(houses) > 0:
            print("[6] House List")
        print("[7] OpenTube")
        div()
        print("[8] Cars")
        if len(vehicles[0]) > 0:
            print("[9] Owned Cars")
        print("[10] Planes")
        if len(vehicles[2]) > 0:
            print("[11] Owned Planes")
        print("[12] Boats")
        if len(vehicles[1]) > 0:
            print("[13] Owned Boats")
        div()
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        elif ch == 5:
            house_buy()
        elif ch == 6 and len(houses) > 0:
            list_house()
        elif ch == 7:
            if is_opentube == 1:
                opentube()
            else:
                opentube_init()
        elif ch == 11 and len(vehicles[2]) > 0:
            plane_list()
        elif ch == 1:
            adult_shop()
        elif ch == 2:
            adult_item_list()
        elif ch == 10:
            if pilot_license == 1:
                plane_hangar()
            else:
                print("You were denied access to the hangar when you failed to present a pilot license.")
                license_centre()
        elif ch == 12:
            if boat_license == 1:
                boat_pier()
            else:
                print("You were denied access to the pier when you failed to present a boating license.")
                license_centre()
        elif ch == 13 and len(vehicles[1]) > 0:
            boat_list()
        elif ch == 8:
            if driver_license == 1:
                car_showroom()
            else:
                print("You were denied access to the showroom when you failed to present a driver's license.")
                license_centre()
        elif ch == 9 and len(vehicles[0]) > 0:
            car_list()
        elif ch == 3:
            div()

            print(f"Debt: {currency}" + str("{:,}".format((int(debt)))))
            print("20% interest, 10% autopaid per year")
            div()
            print("[1] Loan")
            print("[2] Pay Off")
            print("[0] Return")
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 0:
                adult()
            elif ch == 1:
                try:
                    loan = int(input(">"))
                except:
                    adult()
                if loan < 0:
                    loan = 0
                debt += loan
                debt *= 1.2  # Adds interest on loan when you take it out.
                money += loan
                adult()
            elif ch == 2:
                if auto_deposit == 1:
                    money += savings
                    savings = 0
                if money < debt:
                    debt -= money
                    money = 0
                    adult()
                else:
                    money -= debt
                    debt = 0
                    adult()
                if auto_deposit == 1:
                    savings += money
                    money = 0
            else:
                adult()

        elif ch == 4:
            print(f"Savings: {currency}" + str("{:,}".format((savings))))
            print("Interest: 10%")
            div()
            print("[0] Return")
            print("[1] Deposit")
            print("[2] Withdraw")
            print("[3] Deposit All")
            print("[4] Withdraw All")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            elif ch == 1:
                print(f"Money: {currency}" + str("{:,}".format((money))))
                try:
                    dep = int(input(">"))
                except:
                    adult()
                if money < dep:
                    dep = money
                if dep < 0:
                    dep = 0
                money -= dep
                savings += dep
                savings = int(savings)
                adult()
            elif ch == 2:
                print(f"Savings: {currency}" + str("{:,}".format((savings))))
                try:
                    wit = int(input(">"))
                except:
                    adult()
                if wit > savings:
                    wit = savings
                if wit < 0:
                    wit = 0
                money += wit
                savings -= wit
                adult()
            elif ch == 3:
                savings += money
                money = 0
                adult()
            elif ch == 4:
                money += savings
                savings = 0
                adult()
            else:
                adult()
        else:
            adult()
    def go_grad_school():
        global money, edu_lvl
        print("You went to graduate school.")
        print("It lasted [1] year[s].")
        print("You successfully graduated.")
        money -= 75000
        edu_lvl = 3
        br()
        age_up(0)
    def occupation():
        clear_screen()
        global edu_lvl, money, is_job, stress, part_time_salary
        global did_tutor, salary, hours
        div()
        print(f"Salary: {currency}" + str(salary) + "/h")
        print("Hours: " + str(hours))
        print(f"Salary Per Year: {currency}" + str(salary * hours * 52))
        if stress > 0:
            div()
            print("Stress:", pbar2(stress))
        div()
        print("[0] Return")
        print("[1] Education")
        if is_job == 1:
            print("[2] Job Menu")
        print("[3] Part-Time Jobs")
        print("[4] Freelance")
        print("[x] Job Recruiter")
        print("[5] Jobs")
        print("[x] Special Careers")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        elif ch == 5:
            job_centre()
        elif ch == 2 and is_job == 1:
            job_menu()
        elif ch == 1:
            if edu_lvl == 0:
                print(f"[1] GED [{currency}500]")
                try:
                    ch = int(input(">"))
                except:
                    ch = 0
                if ch == 0:
                    adult()
                elif ch == 1:
                    money -= 500
                    print("You got a GED and have high school-equivalent education!")
                    edu_lvl = 1
                    adult()
            elif edu_lvl == 1:
                print(f"[1] University [{currency}25,000]")
                print("[0] Return")
                try:
                    ch = int(input(">"))
                except:
                    ch = 0
                if ch == 0:
                    adult()
                elif ch == 1:
                    div()
                    uni_check()
                    adult()
            elif edu_lvl == 2:
                div()
                print("[0] Return")
                if edu_lvl == 2:
                    print(f"[1] Graduate School [{currency}75,000")
                if edu_lvl >= 3:
                    print("[2] Medical School")
                    print("[3] Music School")
                    print("[4] Art School")
                    print("[5] Law School")
                    print("[6] Dentist School")
                    print("[7] Business School")
                div()
                try:
                    ch = int(input(">"))
                except:
                    adult()
                if ch == 1 and edu_lvl == 2:
                    if intel >= 0.75:
                        print("Your application was accepted!")
                        go_grad_school()
                    else:
                        print("Your application was denied.")
                else:
                    adult()
            else:
                adult()
        elif ch == 3:
            print("[0] Return")
            print(f"[1] Secretary [{currency}15/h] [10h]")
            print(f"[2] Mall Santa [{currency}25/h] [10h]")
            print(f"[3] None [{currency}0/h] [0h]")
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 1:
                div()
                print("You are now a secretary.")
                print(f"Salary: {currency}15/h")
                part_time_salary = 15
                adult()
            elif ch == 2:
                div()
                print("You are now a mall santa.")
                print(f"Salary: {currency}25/h")
                part_time_salary = 25
                adult()
            elif ch == 3:
                div()
                print("No longer working part-time.")
                part_time_salary = 0
                adult()
            else:
                adult()
        elif ch == 4:
            if did_tutor == 0:
                print(f"[1] Tutor [{currency}19/h]")
            print(f"[x] Handyman [{currency}18/h]")
            print(f"[x] Truck Driver [{currency}17/h]")
            print("[0] Return")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            elif ch == 1:
                if did_tutor == 0:
                    div()
                    print("You did tutoring for 30 hours this week.")
                    base = 19 * 30
                    print(f"You made {currency}" + str(base))
                    did_tutor = 1
                    money += base
                    br()
                    adult()
                else:
                    div()
                    print("You did tutoring already.")
                    br()
                    adult()
            elif ch == 2:
                base = 18 * 30
                div()
                adult()
                print("You became a handyman for 30 hours this week.")
                print(f"You made {currency}" + str(base))
                br()
                money += base
                adult()
            elif ch == 3:
                base = 30 * 17
                adult()
                print("You became a truck driver for 30 hours this week.")
                print(f"You made {currency}" + str(base))
                money += base
                br()
                adult()
            else:
                adult()
        else:
            adult()

    def adult_load():
        div()
        print("This is obsolete.")
        mainmenu()
        div()
        #      0             1            2                 3               4                5              6           7                   8                 9                 10         11                 12                13                  14
        # save=forename+"|"+surname+"|"+str(age)+"|"+str(happiness)+"|"+str(looks)+"|"+str(health)+"|"+str(ethics)+"|"+str(intel)+"|"+str(mother_rel)+"|"+str(father_rel)+str(money)+"|"+mother_name+"|"+father_name+"|"+str(mother_age)+"|"+str(father_age)
        # John|Sith|18|1|0.9|0.8|0.7|0.6|1|1|12000|Jill|Shill|32|35
        sn = input("Save Name >")
        sn += ".oll"
        try:
            f = open(sn, "rb")
        except:
            mainmenu()
        import codecs

        save = f.read()
        save = codecs.decode(save, "base64_codec")
        save = save.decode("utf-8")
        save = "John|Sith|18|1|0.9|0.8|0.7|0.6|1|1|12000|Jill|Shill|32|35"
        print(save)
        save = save.replace("||", "|")
        save = save.split("|")
        print(save)
        global mother_age, father_age
        global mother_name, father_name
        global offences
        global happiness, health, intel, looks, ethics, grades, clout, socialc
        global mother_rel, father_rel
        forename = save[2]
        surname = save[3]
        age = int(save[4])
        happiness = float(save[5])
        looks = float(save[6])
        health = float(save[7])
        ethics = float(save[8])
        intel = float(save[9])
        mother_rel = float(save[10])
        father_rel = float(save[11])
        money = int(save[12])
        mother_name = save[13]
        father_name = save[14]
        mother_age = int(save[15])
        father_age = int(save[16])
        br()
        adult()

    def edit_configuration():
        global alt_ui, auto_deposit, allow_debug, alt_logo, currency, auto_pay_lab
        cls()
        div()
        if auto_deposit == 1:
            print("[1] Auto-Deposit [ENABLED]")
        else:
            print("[1] Auto-Deposit [DISABLED]")
        print(
            "Every year, all of your money gets automatically sent to your savings account"
        )
        div()
        print("[2] Change Theme")
        print(f"Change the look of {game_name}.")
        print(f"Different logo, progress bar style and line breaks.")
        if allow_debug != 0:
            div()
            print("[3] Disable Debug Mode")
            print(
                "Debug mode was enabled by editing the main PY file. Choose this to *permanently* disable it."
            )
        div()
        if auto_pay_lab == 1:
            print("[4] Auto-Pay For Lab [ENABLED]")
        else:
            print("[4] Auto-Pay For Lab [DISABLED]")
        print(f"If you have a research lab, it automatically gets funded to avoid bankrupcy. You lose {currency}10,000,000,000 every 10 years.")
        div()
        print("[0] Return")
        try:
            ch = int(input(">"))
        except:
            return True
        if ch == 1:
            if auto_deposit == 0:
                auto_deposit = 1
                edit_configuration()
            else:
                auto_deposit = 0
                edit_configuration()
        elif ch == 2:
            cls()
            div()
            print("[1] Original Theme [Alpha 10]")
            print("[2] Default Theme [Alpha 11]")
            print("[3] Throwback Mode [Alpha 13] [Default]")
            print("[4] Hash Mode [Alpha 17] [Experimental]")
            try:
                ch = int(input(">"))
            except:
                alt_ui = 2
            if ch == 1:
                alt_ui = 0
                alt_logo = 0
            elif ch == 2:
                alt_ui = 2
                alt_logo = 1
            elif ch == 3:
                alt_ui = 3
                alt_logo = 2
            elif ch == 4:
                alt_ui = 5
                alt_logo = 2
            else:
                alt_ui = 3
                alt_logo = 2
            edit_configuration()
        elif ch == 3 and allow_debug != 0:
            allow_debug = 0
            edit_configuration()
        elif ch == 4:
            if auto_pay_lab == 0:
                auto_pay_lab = 1
                edit_configuration()
            else:
                auto_pay_lab = 0
                edit_configuration()
        else:
            return True

    def debug_log(normal=0):
        global app_version, sub_version, game_name, version, is_hbp, driver_license, boat_license, gun_license, pilot_license, research_lab, pending_research, auto_lab_pay
        global allow_debug, is_sppouse, spouse, part_time_salary, sentence, juvie_years, prison_years, friend_count, friend_1, friend_2, friend_3, fame
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary, surgeons
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age, mother_rel, father_rel
        global auto_deposit, child_count, child_1, child_2, child_3, child_4, child_5, child_6, child_7, child_8
        log = ""
        from time import strftime

        print("Creating log...")
        base = strftime("%x %X")
        log += f"{game_name} Debug Log\n"
        log += f"LocalTime={base}\n"
        log += f"LogVersion=6_PR2\n\n"
        log += f"# Game Info\n"
        log += f"Version={version}\n"
        app_v2 = []
        for item in app_version:
            app_v2.append(str(item))
        base = ".".join(app_v2)
        log += f"AppVersion={base}\n"
        if isinstance(sub_version,str) == True:
            log += f"SubVersion=\"{sub_version}\"\n"
        else:
            log += f"SubVersion={sub_version}\n"

        log += f"\n# Basic Information\n"
        log += f"Life Name={forename} {surname}\n"
        log += f"Gender={gender}\n"
        log += f"Age={age}\n"
        log += f"Happiness={happiness}\n"
        log += f"Health={health}\n"
        log += f"Smarts={intel}\n"
        log += f"Looks={looks}\n"
        log += f"Ethics={ethics}\n"
        log += f"Fame={fame}\n"
        log += f"Money={money}\n"
        log += f"Savings={savings}\n"
        log += f"Debt={debt}\n"
        log += f"IsDepressed={is_depressed}\n"
        log += f"IsHBP={is_hbp}\n\n"

        log += f"# General Information\n"
        log += f"Pension={pension}\n"
        log += f"IsJob={is_job}\n"
        log += f"EduLvl={edu_lvl}\n"
        log += f"Degree={degree}\n"
        log += f"Stress={stress}\n"
        log += f"Year={year}\n"
        global fake_id, club_count
        log += f"DidTutor={did_tutor}\n"
        log += f"Fake ID={fake_id}\n"
        log += f"ClubCount={club_count}\n\n"

        log +=f"# Plastic Surgeons\n"
        log += f"Count: {len(surgeons)}\n\n"
        for item in surgeons:
            try:
                log += item.debug()
            except:
                log += f"[Failed to debug]\n\n"


        log += f"# Lab Info\n"
        log += f"ResearchLab={research_lab}\n"
        log += f"Pending=    {pending_research}\n\n"

        log += f"# Relations Information\n"
        log += f"Mother={mother_name}\n"
        log += f"Father={father_name}\n"
        log += f"MotherRel={mother_rel}\n"
        log += f"FatherRel={father_rel}\n"
        log += f"MotherAge={mother_age}\n"
        log += f"FatherAge={father_age}\n"
        log += f"MotherEndAge={mother_end_age}\n"
        log += f"FatherEndAge={father_end_age}\n\n"

        log += f"# Child Information\n"
        log += f"Count: {child_count}\n\n"
        if child_count >= 1:
            log += f"## Child 1\n"
            log += f"Name={child_1.name}\n"
            log += f"Age={child_1.age}\n"
            log += f"Rel={child_1.rel}\n"
            log += f"Intel={child_1.intel}\n"
            log += f"Looks={child_1.looks}\n"
            log += f"Craziness={child_1.craziness}\n"
            log += f"End={child_1.end}\n"
            if child_1.gender == 0:
                log += f"Gender=M\n\n"
            else:
                log += f"Gender=F\n\n"
        if child_count >= 2:
            log += f"## Child 2\n"
            log += f"Name={child_2.name}\n"
            log += f"Age={child_2.age}\n"
            log += f"Rel={child_2.rel}\n"
            log += f"Intel={child_2.intel}\n"
            log += f"Looks={child_2.looks}\n"
            log += f"Craziness={child_2.craziness}\n"
            log += f"End={child_2.end}\n"
            if child_2.gender == 0:
                log += f"Gender=M\n\n"
            else:
                log += f"Gender=F\n\n"
        if child_count >= 3:
            log += f"## Child 3\n"
            log += f"Name={child_3.name}\n"
            log += f"Age={child_3.age}\n"
            log += f"Rel={child_3.rel}\n"
            log += f"Intel={child_3.intel}\n"
            log += f"Looks={child_3.looks}\n"
            log += f"Craziness={child_3.craziness}\n"
            log += f"End={child_3.end}\n"
            if child_3.gender == 0:
                log += f"Gender=M\n\n"
            else:
                log += f"Gender=F\n\n"
        if child_count >= 4:
            log += f"## Child 4\n"
            log += f"Name={child_4.name}\n"
            log += f"Age={child_4.age}\n"
            log += f"Rel={child_4.rel}\n"
            log += f"Intel={child_4.intel}\n"
            log += f"Looks={child_4.looks}\n"
            log += f"Craziness={child_4.craziness}\n"
            log += f"End={child_4.end}\n"
            if child_4.gender == 0:
                log += f"Gender=M\n\n"
            else:
                log += f"Gender=F\n\n"
        if child_count >= 5:
            log += f"## Child 5\n"
            log += f"Name={child_5.name}\n"
            log += f"Age={child_5.age}\n"
            log += f"Rel={child_5.rel}\n"
            log += f"Intel={child_5.intel}\n"
            log += f"Looks={child_5.looks}\n"
            log += f"Craziness={child_5.craziness}\n"
            log += f"End={child_5.end}\n"
            if child_5.gender == 0:
                log += f"Gender=M\n\n"
            else:
                log += f"Gender=F\n\n"
        if child_count >= 6:
            log += f"## Child 6\n"
            log += f"Name={child_6.name}\n"
            log += f"Age={child_6.age}\n"
            log += f"Rel={child_6.rel}\n"
            log += f"Intel={child_6.intel}\n"
            log += f"Looks={child_6.looks}\n"
            log += f"Craziness={child_6.craziness}\n"
            log += f"End={child_6.end}\n"
            if child_6.gender == 0:
                log += f"Gender=M\n\n"
            else:
                log += f"Gender=F\n\n"
        if child_count >= 7:
            log += f"## Child 7\n"
            log += f"Name={child_7.name}\n"
            log += f"Age={child_7.age}\n"
            log += f"Rel={child_7.rel}\n"
            log += f"Intel={child_7.intel}\n"
            log += f"Looks={child_7.looks}\n"
            log += f"Craziness={child_7.craziness}\n"
            log += f"End={child_7.end}\n"
            if child_7.gender == 0:
                log += f"Gender=M\n\n"
            else:
                log += f"Gender=F\n\n"
        if child_count >= 8:
            log += f"## Child 8\n"
            log += f"Name={child_8.name}\n"
            log += f"Age={child_8.age}\n"
            log += f"Rel={child_8.rel}\n"
            log += f"Intel={child_8.intel}\n"
            log += f"Looks={child_8.looks}\n"
            log += f"Craziness={child_8.craziness}\n"
            log += f"End={child_8.end}\n"
            if child_8.gender == 0:
                log += f"Gender=M\n\n"
            else:
                log += f"Gender=F\n\n"
        log += f"# Prison Information\n"
        log += f"Sentence={sentence}\n"
        log += f"PrisonYears={prison_years}\n"
        log += f"JuvieYears={juvie_years}\n\n"

        log += f"# Finance Information\n"
        log += f"Salary={salary}\n"
        log += f"Hours={hours}\n"
        log += f"MinHours={min_hours}\n"
        log += f"Pension={pension}\n"
        log += f"WorkExp={work_e}\n"
        log += f"WorkEB={work_e_base}\n"
        log += f"Promo={promo_base}\n"
        log += f"Expenses={expenses}\n"
        log += f"PartTimeSalry={part_time_salary}\n\n"

        log += f"# License Information\n"
        log += f"DriverLicense={driver_license}\n"
        log += f"BoatLicense={boat_license}\n"
        log += f"GunLicense={gun_license}\n"
        log += f"BoatLicense={boat_license}\n\n"
        

        log += f"# Spouse Information\n"
        log += f"IsSpouse={is_spouse}\n"
        if is_spouse == 1:
            log += f"SpouseName={spouse.name}\n"
            log += f"SpouseAge={spouse.age}\n"
            log += f"SpouseEndAge={spouse.age}\n"
            log += f"SpouseRel={spouse.rel}\n"
            log += f"SpouseLvl={spouse.lvl}\n"
            log += f"Gender={spouse.gender}\n\n"
        else:
            log += f"\n"
        log += f"# Friend Information\n"
        log += f"FriendCount={friend_count}\n\n"
        if friend_count >= 1:
            log += f"## Friend 1\n"
            log += f"Name={friend_1.name}\n"
            log += f"Age={friend_1.age}\n"
            log += f"Gender={friend_1.gender}\n"
            log += f"Intelligence={friend_1.intel}\n"
            log += f"Looks={friend_1.looks}\n"
            log += f"Craziness={friend_1.craziness}\n"
            log += f"EndAge={friend_1.end}\n"
            log += f"Relation={friend_1.rel}\n\n"
        if friend_count >= 2:
            log += f"## Friend 2\n"
            log += f"Name={friend_2.name}\n"
            log += f"Age={friend_2.age}\n"
            log += f"Gender={friend_2.gender}\n"
            log += f"Intelligence={friend_2.intel}\n"
            log += f"Looks={friend_2.looks}\n"
            log += f"Craziness={friend_2.craziness}\n"
            log += f"EndAge={friend_2.end}\n"
            log += f"Relation={friend_2.rel}\n\n"
        if friend_count >= 3:
            log += f"## Friend 1\n"
            log += f"Name={friend_2.name}\n"
            log += f"Age={friend_2.age}\n"
            log += f"Gender={friend_2.gender}\n"
            log += f"Intelligence={friend_2.intel}\n"
            log += f"Looks={friend_2.looks}\n"
            log += f"Craziness={friend_2.craziness}\n"
            log += f"EndAge={friend_2.end}\n"
            log += f"Relation={friend_2.rel}\n\n"
        log += f"# Configuration Information\n"
        log += f"AltUi={alt_ui}\n"
        log += f"AltLogo={alt_logo}\n"
        log += f"AllowDebug={allow_debug}\n"
        log += f"AllowTest={allow_test}\n"
        log += f'Currency="{currency}"\n'
        log += f"AutoDeposit={auto_deposit}\n"
        log += f"AutoPayLab={auto_pay_lab}\n\n"

        log += f"# SysConfig Information\n"
        try:
            import platform

            base = platform.system()
            base2 = platform.uname()[2]
            base3 = platform.architecture()
            base4 = platform.platform()
            base5 = platform.machine()
        except:
            base = "N/A"
            base2 = "N/A"
            base3 = "N/A"
            base4 = "N/A"
            base5 = "N/A"
        try:
            import tkinter as tk

            root = tk.Tk()
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            root.withdraw()
        except:
            screen_width = "N/A"
            screen_height = "N/A"
        try:
            v = platform.python_version()
            th = platform.architecture()
        except:
            v = "N/A"
            th = "N/A"
        cpu = platform.processor()
        log += f"Platform={base} {base2}\n"
        log += f"ScreenResolution={screen_width}x{screen_height}\n"
        log += f"PyVer={v}\n"
        log += f"Architecture={base3}\n"
        log += f"GeneralInfo={base4}\n"
        log += f"Machine={base5}\n"
        log += f"CPU={cpu}\n\n"

        log += f"# This debug log is created automatically using the\n"
        log += f"# {game_name} Debug Log Creation Tool [v6.x]\n"
        log += f"# The tool is (c) 2022 WinFan3672 [MIT License]"
        from time import ctime

        sn = ctime() + ".log"
        sn = sn.replace(":", "-")
        sn = sn.replace(" ", "_")
        if normal == 0:
            f = open(sn, "w")
            f.write(log)
            f.close()
            print(f"Saved as {sn}.")
            br()
            adult()
        else:
            return log
    def console(elevated=0,text=""):
        global allow_debug, salary, hours, job_id
        elev = elevated
        if text == "":
            if elevated == 1:
                ch=input("elev-console >")
            else:
                ch=input("console >")
        else:
            ch = text
        if ch == "help":
            div()
            print("help - this menu")
            print("echo <text> - prints <text> to the terminal")
            print("dlog - Prints a debug log")
            print("save - Saves current life")
            print("cls - Clears console")
            print("sv_cheats <0/1> - enables/disables cheats")
            if elev == 1:
                print("cdebt - clears debt")
                print("rich <int> - sets your money to <int>")
                print("max lab - maxxes out lab")
                print("max license - gives you all licenses")
                print("safemode - restart Console without elevation")
                print("max stat - 100% for all stats")
                print("forgive - Forgive prison sentence")
                print("sentence <int> - sets sentence to <int>")
            print("exit - return to main screen")
            div()
            console(elevated)
        elif "echo " in ch:
            print(ch[5:])
            console(elevated)
        elif ch == "qjob" and elev == 1:
            job_id = 666
            console(elev)
        elif ch == "cls":
            cls()
            console(elev)
        elif ch.startswith("hours ") and elev == 1:
            try:
                hours = int(ch[6:])
            except:
                pass
            console(elev)
        elif ch.startswith("salary ") and elev == 1:
            try:
                salary=int(ch[8:])
            except:
                pass
            console(elev)
        elif ch == "cdebt" and elevated == 1:
            global debt
            debt = 0
            console(elev)
        elif ch == "save":
            save_game()
            console(elev)
        elif ch == "dlog":
            div()
            print(debug_log(1))
            div()
            console(elev)
        elif ch == "sv_cheats 0":
            allow_debug = 0
            console(0)
        elif ch == "sv_cheats 1":
            print("WARNING! Enabling cheats will mean that you cannot earn Achievements.")
            print("It will also mark your save game as cheated, even if you undo the cheats.")
            ch = input("\nTo proceed, type \"Do as I say!\", exactly how it is shown\n[Or, to find out about the consequences of cheating, type \"consequences\"]\n\n>")
            if ch == "Do as I say!":
                allow_debug = 1
            elif ch == "consequences":
                print("[-] You cannot earn Achievements")
                print("[-] The Debug Log will reveal that you are a cheater")
                print("[-] You cannot complete Challenges")
                print("[-] Your save file gets marked as cheated")
                print("[-] etc.")
            console(1)
        elif ch == "forgive" and elev == 1:
            global prison_years
            prison_years = 0
            console(1)
        elif "sentence " in ch and elev == 1:
            try:
                prison_years=int(ch[9:])
            except:
                pass
            console(elev)
        elif "rich " in ch and elev == 1:
            try:
                global money
                money = int(ch[5:])
            except:
                pass
            console(elev)
        elif ch == "exit":
            adult()
        elif ch == "max stat" and elev == 1:
            global happiness, health, intel, looks
            happiness, health, intel, looks = 1,1,1,1
            console(elev)
        elif ch == "max license" and elev == 1:
            global driver_license, boat_license, gun_license, pilot_license
            driver_license, boat_license, gun_license, pilot_license = 1,1,1,1
            console(1)
        elif ch == "max lab" and elev == 1:
            global research_lab
            research_lab = [1,1,1,1,1]
            console(elev)
        elif ch == "safemode":
            console()
        else:
            print("InvalidConsoleCommandError; the Console Command is not valid.")
            console(elevated)
    def adult_pause():
        cls()
        global is_depressed, money, happiness, looks, intel, ethics, health, salary, hours
        global mother_age, father_age
        global mother_name, father_name
        global offences
        global happiness, health, intel, looks, ethics, grades, clout, socialc
        global mother_rel, father_rel, mother_end_age, father_end_age
        global edu_lvl, degree
        div()
        print("Game Paused.")
        div()
        print("[0] Resume")
        print("[1] Save Life")
        print("[2] Load Life")
        print("[3] Exit To Main Menu")
        div()
        print("[x] Download Challenge From Web")
        print("[x] Load Challenge From File")
        print("[6] Check For Updates")
        div()
        print("[7] Console")
        if allow_debug != 0:
            print("[8] Console [Elevated] [Debugging Only]")
        else:
            print("[ ] Console [Elevated] [Debugging Only]")
        div()
        print("[9] Options")
        print("[10] Create Debug Log [For Bug Reporting]")
        div()
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        elif ch == 1:
            save_game()
            adult()
        elif ch == 7:
            console()
        elif ch == 8 and allow_debug != 0:
            console(1)
        elif ch == 10:
            debug_log()
        elif ch == 6:
            import urllib.request

            url = "http://winfan3672.000webhostapp.com/version_check/openlife.version"
            print("Checking for updates...")
            try:
                urllib.request.urlretrieve(url, "openlife.version")
            except:
                div()
                print("Failed to check for updates.")
                div()
                print("You could try:")
                print("[-] Checking that you are connected to the Internet.")
                print(
                    "[-] Checking that winfan3672.000webhostapp.com is still up, since that is the server that provides the version check information."
                )
                print(
                    "[-] Checking that http://winfan3672.000webhostapp.com/version_check/openlife.versio exists, since it may have been deleted."
                )
                print(
                    "[-] Checking that your antivirus or firewall is not blocking winfan3672.000webhostapp.com/"
                )
                print("[-] On Windows, deleting your DNS resolver cache.")
                adult_pause()
            div()
            f = open("openlife.version", "r")
            data = f.read()
            data = data.split("|")
            data = [int(data[0]), int(data[1]), int(data[2])]
            try:
                urllib.request.urlretrieve(
                    "http://winfan3672.000webhostapp.com/latest_v_url/openlife",
                    "openlife.urlcheck",
                )
                f = open("openlife.urlcheck", "r")
                url = f.read()
            except:
                url = "[Could not retrieve URL from server]"
            not_update_text = (
                f"An update for {game_name} is available.\nDownload it from:\n{url}"
            )
            if data[0] > app_version[0]:
                print(not_update_text)
            else:
                if data[1] > app_version[1]:
                    div()
                    print(not_update_text)
                else:
                    if data[2] > app_version[2]:
                        div()
                        print(not_update_text)
                    else:
                        print(f"You are on the latest version of {game_name}.")
            adult_pause()
        elif ch == 9:
            edit_configuration()
        elif ch == 2:
            print("[0] Cancel")
            print("[1] Exit and Save")
            print("[2] Exit Without Saving")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1:
                save_game()
                load_game()
            elif ch == 2:
                load_game()
            else:
                adult_pause()
        elif ch == 3:
            print("[0] Cancel")
            print("[1] Exit and Save")
            print("[2] Exit Without Saving")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult_pause()
            elif ch == 1:
                save_game()
                mainmenu()
            elif ch == 2:
                mainmenu()
            else:
                adult()
        else:
            adult()

    def adult():
        calc_stress()
        global edu_lvl, pension, job_lvl, is_spouse, spouse
        global salary, hours, fame, friend_count, friend_1
        global allow_debug, allow_debug, friend_2, friend_3
        global mother_age, father_age, is_wpp, is_common_cold
        global mother_name, father_name, wpp_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel, part_time_salary
        global money, is_depressed, work_e, is_job, degrees
        global job_id, job_lvl, fame, child_count, child_1, child_2, child_3, child_4, child_5, child_6, child_7, child_8
        global money

        money = int(money)
        if happiness > 1:
            happiness = 1
        if happiness < 0:
            happiness = 0
        if health > 1:
            health = 1
        if health < 0:
            emergency_room(2)
        if intel > 1:
            intel = 1
        if looks > 1:
            looks = 1
        if intel < 0:
            intel = 0
        if looks < 0:
            looks = 0
        if fame > 1:
            fame = 1
        if fame < 0:
            fame = 0
        try:
            if spouse.rel > 1:
                spouse.rel = 1
        except:
            pass
        try:
            if spouse.rel < 0:
                spouse.rel = 0
        except:
            pass
        global forename, surname
        global mother_rel, father_rel
        clear_screen()
        div()
        print(forename + " " + surname)
        try:
            if is_spouse == 1:
                if spouse.lvl == 2:
                    print(f"[Married to {spouse.name}]")
        except:
            pass
        if is_wpp == 1:
            print(f"Under Witness Protection [Formerly {wpp_name[0]} {wpp_name[1]}]")
        elif fame >= 0.25 and is_opentube == 1 and money < 400000000000:
            print("Famous Influencer")
        elif pension > 0 and money < 400000000000:
            print("Pensioner")
        elif money >= 5000000 and is_job == 0 and money < 400000000000:
            print("Independently Wealthy")
        elif is_job == 1:
            if job_id == 1:
                print("Amazon Delivery Driver")
            elif job_id == 2:
                if job_lvl == 1:
                    print("Jr Translator")
                elif job_lvl == 2:
                    print("Translator")
                else:
                    print("Sr. Translator")
            elif job_id == 3:
                if job_lvl == 1:
                    print("Jr Accountant")
                elif job_lvl == 2:
                    print("Accountant")
                else:
                    print("Sr Accountant")
            elif job_id == 4:
                print("Exorcist")
            elif job_id == 5:
                print("Teacher")
            elif job_id == 6:
                if job_lvl == 1:
                    print("Jr Game Developer")
                elif job_lvl == 2:
                    print("Game Developer")
                else:
                    print("Sr Game Developer")
            elif job_id == 8:
                if job_lvl == 1:
                    print("Jr Lawyer")
                elif job_lvl == 2:
                    print("Lawyer")
                else:
                    print("Sr Lawyer")
            elif job_id == 9:
                if job_lvl == 1:
                    print("Jr App Developer")
                elif job_lvl == 2:
                    print("App Developer")
                else:
                    print("Sr App Developer")
            elif job_id == 10:
                if job_lvl == 1:
                    print("Jr Banker")
                elif job_lvl == 2:
                    print("Banker")
                else:
                    print("Sr Banker")
            elif job_id == 11:
                print("Monk")
            elif job_id == 12:
                if job_lvl == 1:
                    print("Jr Wedding Planner")
                elif job_lvl == 2:
                    print("Wedding Planner")
                else:
                    print("Sr Wedding Planner")
            elif job_id == 13:
                if job_lvl == 1:
                    print("Engineer I")
                elif job_lvl == 2:
                    print("Engineer II")
                else:
                    print("Engineer III")
            elif job_id == 14:
                print("Data Scientist")
            elif job_id == 15:
                if job_lvl == 1:
                    print("Private [Army]")
                elif job_lvl == 2:
                    print("Lieutenant [Army")
                else:
                    print("Captain [Army]")
            elif job_id == 17:
                print("Cashier")
            elif job_id == 18:
                print("College Lecturer")
            elif job_id == 19:
                print("Oohber Driver")
            elif job_id == 20:
                if job_lvl == 1:
                    print("Jr Editor")
                elif job_lvl == 2:
                    print("Editor")
                else:
                    print("Sr Editor")
            elif job_id == 21:
                print("Exotic Dancer")
            elif job_id == 22:
                print("Flight Attendant")
            elif job_id == 23:
                if job_lvl == 1:
                    print("Apprentice Hairdresser")
                else:
                    print("Hairdresser")
            elif job_id == 25:
                print("Librarian")
            elif job_id == 26:
                print("Nun")
            elif job_id == 28:
                print("P*rnographer")
            elif job_id == 29:
                print("Jr Stockbroker")
            elif job_id == 30:
                print("Publicity Stuntperson")
            else:
                print("Corporate Slave")
        elif money >= 400000000000 and is_job == 0:
            print("Richest Person In The World")
        elif allow_debug == 1:
            print(f"{game_name} Debugger")
        else:
            if part_time_salary == 0:
                print("Unemployed")
        if part_time_salary > 0:
            print("Working Part-Time")
        div()
        print("Age", age)
        print(f"{currency}" + str("{:,}".format((money))))
        if auto_deposit == 1:
            div()
            print(f"Savings: {currency}" + str("{:,}".format((savings))))
        if pension < 1:
            div()
        if edu_lvl == 1 and pension < 1:
            print("Education: High School")
        elif edu_lvl == 2:
            print(f"Education: University [{degrees[degree]}]")
        elif edu_lvl == 3:
            print(f"Education: Graduate School [{degrees[degree]}]")
        elif edu_lvl == 0:
            print("Education: N/A")
        if pension < 1:
            print("Work Experience:", work_e, "Years")
        global work_e_base
        if is_cancer == 1:
            div()
            print("Suffers from: Cancer")
        if is_common_cold == 1:
            div()
            print("Suffers from: Common Cold")
        if is_depressed == 1:
            div()
            print("Suffers from: Depression")
        if is_hbp == 1:
            if is_depressed == 0:
                div()
            print("Suffers from: High Blood Pressure")

        div()
        if happiness >= 0.9:
            print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "% :D")
        elif happiness <= 0.25:
            print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "% :(")
        else:
            print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "%")
        if health <= 0.25:
            print("Health:   ", pbar2(health), str(int(health * 100)) + "% [!]")
        elif health >= 0.9:
            print("Health:   ", pbar2(health), str(int(health * 100)) + "% <3")
        else:
            print("Health:   ", pbar2(health), str(int(health * 100)) + "%")
        if intel <= 0.25:
            print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "% [!]")
        elif intel >= 0.9:
            print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "% :)")
        else:
            print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "%")
        if looks >= 0.9:
            print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "% :O")
        elif looks <= 0.25:
            print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "% :(")
        else:
            print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "%")
        if fame > 0:
            div()
            print("Fame:     ", pbar2(fame), str(int(fame * 100)) + "%")
        div()
        print("[1] Occupation")
        print("[2] Assets")
        print("[0] Age Up")
        print("[3] Relationships")
        print("[4] Activities")
        print("[5] Pause Menu")
        try:
            ch = int(input(">"))
        except:
            adult()
        if ch == 1:
            occupation()
        elif ch == 2:
            div()
            adult_assets()
        elif ch == 0:
            age_up(0)
        elif ch == 5:
            adult_pause()
        elif ch == 3:
            adult_rel(0)
        elif ch == 4:
            adult_activities()
        elif ch == 89:
            cls()
            adult()
        adult()

    def adult_init(verbose):
        if verbose == 1:
            div()
            print("You are now an adult.")
            print(
                "It is like being a teen but you can go to uni, get a job and live a proper life."
            )
            div()
            print("Press ENTER to continue.")
            wer = input()
        global clout, socialc
        global mother_rel, father_rel
        global stress
        stress = 0.65
        from random import randint

        if mother_rel > 0.8:
            mother_rel = 0.8
        if father_rel > 0.8:
            father_rel = 0.8
        adult()

    def gang_menu():
        global respect, clout, happiness, health, is_drip, money, enemy_gang_name, enemy_gang_rel, enemy_gang_lead
        global is_sch_gang
        div()
        print("Welcome to the top-secret GANG MENU.")
        print("Here you can earn respect and Gang Points to spend")
        div()
        print("Respect:")
        if respect > 1:
            respect = 1
        if respect < 0:
            print("GANGSTER: You have greatly disappointed us.")
            print("YOU: What do you mean?")
            print("GANGSTER: You have broken our Code of Conduct.")
            print("YOU: What are you talking about!")
            print("GANGSTER: You aren't loyal.")
            print("YOU: YES I AM!")
            print("GANGSTER: We're gonna have to kick you out.")
            print("YOU: NO!")
            global is_sch_gang
            is_sch_gang = 0
            happiness = 0
            br()
            teen()
        pbar(respect)
        div()
        print("[0] Return")
        print("[x] Get Fake ID")
        print("[2] Bully Kids")
        print("[3] Enemy Gangs")
        print("[x] Gang War")
        print("[5] Drink With The Gang")
        if is_drip == 0:
            print(f"[6] Gang Drip[{currency}1500]")
        print("[7] Leave gang")
        print("[8] Rob Children")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            teen()
        elif ch == 1:
            div()
            print("Not in game yet.")
            teen()
        elif ch == 3:
            print(enemy_gang_name)
            div()
            print("Relations: ", pbar2(enemy_gang_rel))
            print("Enemy Lead:", pbar2(enemy_gang_lead))
            br()
            teen()
        elif ch == 4:
            print(enemy_gang_name)
            div()
            print("Relations: ", pbar2(enemy_gang_rel))
            print("Enemy Lead:", pbar2(enemy_gang_lead))
            div()
            print(f"You had a gang war with {enemy_gang_name}.")
            enemy_gang_rel -= 0.5
            base = rng(-50, 50) / 100
            base2 = -(base)
            enemy_gang_lead += base
            clout += base2
            respect += base2
            div()
            if enemy_gang_rel < 0:
                enemy_gang_rel = 0
            if enemy_gang_lead > 1:
                enemy_gang_lead = 1
            if enemy_gang_lead < 0:
                enemy_gang_lead = 0
            print("Relations: ", pbar2(enemy_gang_rel))
            print("Enemy Lead:", pbar2(enemy_gang_lead))
            br()
            teen()

        elif ch == 8:
            child_amount = rng(10, 50)
            take = 0
            for i in range(child_amount):
                take += rng(10, 20)
            your_take = int(take / 10)
            print(
                f"You and the gang went on a rampage in the school playground, demanding money from innocent children."
            )
            print(f"You stole {currency}{take} from {child_amount} children.")
            print(f"Since there are 10 of you, you get 10% of the take.")
            print(f"You got {currency}{your_take} as your share.")
            money += your_take
            happiness += 0.45
            respect += 0.2
            br()
            teen()
        elif ch == 2:
            div()
            print("You bullied some kids in the playground.")
            print("You took great pleasure out of doing so.")
            div()
            clout += 0.15
            respect += 0.05
            happiness += 0.25
            br()
            teen()
        elif ch == 5:
            respect += 0.05
            happiness += 0.1
            clout -= 0.05
            div()
            print("You had a few with the mates.")
            div()
            br()
            teen()
        elif ch == 6:
            if money >= 1500 and is_drip == 0:
                print("Gang drip allows you to gain 45% more repect and become")
                print("one with the gang.")
                div()
                print(f"[1] Purchase [{currency}1500]")
                print("[0] Return [Gang Menu")
                div()
                try:
                    ch = int(input(">"))
                except:
                    ch = 0
                if ch == 0:
                    gang_menu()
                elif ch == 1:
                    money -= 1500
                    is_drip = 1
                    respect += 0.45
                    gang_menu()
                else:
                    gang_menu()
            else:
                div()
                print("A requirement was not fulfilled:")
                if money < 1500:
                    print(f"You need {currency}1500.")
                elif is_drip != 0:
                    print("You have bought Gang Drip before.")
                else:
                    print("An error occured.")
                div()
                br()
                teen()
        elif ch == 7:
            div()
            print("[1] Confirm")
            print("[0] Return")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                teen()
            elif ch == 1:
                div()
                print("You left the gang.")
                is_sch_gang = 0
                teen()

    def secondary_school_menu():
        global club_count, is_sch_gang, health, happiness
        global grades, intel, happiness, stress, teen_hours, teen_salary
        div()
        print("[0] Return")
        print("[1] Secondary School")
        print("[2] Freelance")
        print("[x] Jobs")
        print("[x] Military")
        print("[5] Part-Time Jobs")
        if teen_hours > 0:
            print("[6] Edit Job Details")
        print("[x] Special Careers")
        div()
        print(f"Stress:", pbar2(stress), f"[{int(stress*100)}%]")
        div()
        print("In", club_count, "school clubs")
        if is_sch_gang == 1:
            print("In School Gang")
        div()
        print(f"Salary: {currency}{teen_salary}")
        print(f"Hours: {teen_hours}")
        div()
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            div()
            teen()
        elif ch == 5:
            print(f"[0] Return")
            print(f"[1] Pizza Delivery [{currency}10/h] [10h]")
            print(f"[2] Newspaper Delivery [{currency}15/h] [15h]")
            print(f"[3] Lawn Mower [{currency}25/h] [5h]")
            print(f"[4] Car Washer [{currency}35/h] [10h]")
            print(f"[5] Laundrette Worker {currency}15/h] [15h]")
            print(f"[6] Drug Dealer [Local Gang] [{currency}45/h] [10h]")
            print(f"[7] None [{currency}0/h] [0h]")
            try:
                ch = int(input(">"))
            except:
                teen()
            if ch == 1:
                teen_salary = 10
                teen_hours = 10
                teen()
            elif ch == 2:
                teen_salary = 15
                teen_hours = 15
                teen()
            elif ch == 3:
                teen_salary = 25
                teen_hours = 5
                teen()
            elif ch == 4:
                teen_salary = 35
                teen_hours = 10
                teen()
            elif ch == 5:
                teen_salary = 15
                hours = 15
            elif ch == 6:
                teen_salary = 45
                teen_hours = 10
            elif ch == 7:
                teen_salary = 0
                teen_hours = 0
                teen()
            else:
                teen()
        elif ch == 6:
            if teen_hours > 0:
                print("[1] Adjust Hours")
                print("[0] Exit")
                div()
                print(f"Salary: {currency}{teen_salary}")
                print(f"Hours: {teen_hours}")
                div()
                try:
                    ch = int(input(">"))
                except:
                    teen()
                if ch == 1:
                    try:
                        hours = int(input(">"))
                    except:
                        hours = 10
                    if hours > 20:
                        hours = 20
                    if hours < 10:
                        hours = 10
                    teen_hours = hours
                    teen()
                else:
                    teen()
            else:
                teen()
        elif ch == 1:
            div()
            print("Grades:")
            pbar(grades)
            div()
            print("[1] Study Harder")
            print("[2] Skip School")
            print("[3] Join Club")
            if is_sch_gang == 0:
                print("[4] Join School Gang")
            else:
                print("[4] School Gang")
            print("[0] Return")
            div()
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                teen()
            elif ch == 1:
                div()
                print("You studied until you lost your vision.")
                div()
                grades += 0.15
                intel += 0.10
                teen()
            elif ch == 2:
                div()
                print("Insted of going to school, you decided to go bowling instead.")
                div()
                grades -= 0.45
                intel -= 0.55
                happiness += 0.15
                teen()
            elif ch == 3:
                div()
                print("Are you sure?")
                print("[1] Join [+10% stress]")
                print("[0] NO")
                try:
                    ch = int(input(">"))
                except:
                    ch = 0
                if ch == 0:
                    teen()
                elif club_count >= 2:
                    div()
                    print("You cannot join more than 2 clubs.")
                    teen()
                elif ch == 1:
                    club_count += 1
                    stress += 0.1
                    teen()
                else:
                    teen()
            elif ch == 4:
                gang = is_sch_gang
                if gang == 0:
                    div()
                    print("YOU: I'd like to join your gang.")
                    if clout == 1:
                        print("GANGSTER: Sure thing, kid. Come on in.")
                        from time import sleep

                        sleep(1.5)
                        happiness += 0.55
                        print("GANGSTER: I'm sure your input will be valuable.")
                        global respect
                        respect = 0.1
                        is_sch_gang = 1
                        br()
                        teen()
                    elif clout >= 0.75:
                        print("GANGSTER: No, you're not tough enough.")
                        print("YOU: I respect that.")
                        br()
                        teen()
                    else:
                        print("GANGSTER: HA HA! AS IF!")
                        div()
                        print("The gangster beat you up!")
                        print("Damage:")
                        pbar(0.85)
                        div()
                        happiness -= 2.25
                        health -= 0.85
                        br()
                        teen()
                elif gang == 1:
                    gang_menu()

            teen()
        else:
            teen()

    def teen_item_list():
        global knife_count, pistol_count
        print("Items")
        div()
        for i in range(knife_count):
            print("1x Knife [Standard Duty]")
        for i in range(pistol_count):
            print("1x Pistol [Gunshop-Grade]")
        if pistol_count == 0 and knife_count == 0:
            print("[No items to show]")
        br()
        teen()

    def teen_shop():
        div()
        global money, fake_id, happiness, health, pistol_count, knife_count, is_sch_gang
        print(f"{currency}" + str("{:,}".format((money))))
        div()
        print("Welcome. Items labeled with [FID] need a fake ID to be bought.")
        print("Items labeled with [GANG] require you to join the school gang.")
        div()
        print("[0] Return [Assets]")
        print(f"[1] Fake ID [{currency}450]")
        print(f"[2] Beer [{currency}10][FID]")
        print(f"[3] Cigarette pack [{currency}25][FID]")
        print(f"[4] Knife [{currency}25][GANG]")
        print(f"[5] Pistol [{currency}750][GANG]")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            teen_assets()
        elif ch == 1:
            if money >= 450 and fake_id == 0:
                money -= 450
                fake_id = 1
                div()
                print("You bought a fake ID.")
                teen()
            else:
                div()
                print("You cannot afford/already have that!")
                teen()
        elif ch == 2:
            if money >= 10 and fake_id == 1:
                money -= 10
                happiness += 0.25
                health -= 0.55
                div()
                print("You had a beer.")
                teen()
            else:
                div()
                print("You cannot afford this and/or you don't have a fake ID.")
                teen()
        elif ch == 3:
            if money >= 25 and fake_id == 1:
                money -= 25
                happiness += 0.50
                health -= 0.75
                div()
                print("You smoked 20 cigarettes at once. Talk about addiction.")
                teen()
            else:
                div()
                print("You cannot afford this and/or you don't have a fake ID.")
                teen()
        elif ch == 4:
            div()
            if money >= 25 and is_sch_gang == 1:
                money -= 25
                knife_count += 1
                print("You now have a knife.")
                teen()
            else:
                if is_sch_gang == 1:
                    print(f"You need {currency}25 to buy a knife.")
                else:
                    print("You need to join the school gang to buy a knife.")
                teen()
        elif ch == 5:
            div()
            if money >= 750 and is_sch_gang == 1:
                money -= 750
                pistol_count += 1
                print("You now have a pistol.")
                teen()
            else:
                if is_sch_gang == 1:
                    print(f"You need {currency}750 to buy a pistol.")
                else:
                    print("You need to join the school gang to buy a pistol.")
                teen()
        else:
            teen_assets()

    def teen_assets():
        global money, fake_id
        print(f"Money: {currency}" + str(money))
        div()
        print("[1] Buy Items")
        print("[2] Item List")
        if fake_id >= 1:
            print("[3] Fake ID Hub")
        print("[0] Return")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            teen()
        elif ch == 1:
            teen_shop()
        elif ch == 2:
            div()
            teen_item_list()
        elif ch == 3:
            if fake_id >= 1:
                fake_id_hub()
            else:
                div()
                print("Get a fake ID lol")
                teen()
        else:
            teen()

    def teen_activities():
        global happiness, health, intel, looks, ethics, grades, clout, socialc
        global mother_rel, father_rel
        global money
        global offences
        print("[0] Return")
        print("[1] Gym")
        print("[2] Library")
        print("[3] Doctor")
        print("[4] Surrender")
        print("[5] Debug Mode")
        print("[6] Crime")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            teen()
        elif ch == 1:
            div()
            print("You went to the gym.")
            happiness += 0.45
            health += 0.35
            print("Enjoyment:")
            pbar(1)
            teen()
        elif ch == 2:
            div()
            print("You visited the library.")
            print("Enjoyment:")
            pbar(0.25)
            happiness -= 0.1
            intel += 0.15
            teen()
        elif ch == 3:
            div()
            print("No doctor available.")
            teen()
        elif ch == 4:
            print("[0] Return")
            print("[1] Surrender", forename, surname + "?")
            try:
                ch = int(input("<<"))
            except:
                ch = 0
            if ch == 0:
                teen()
            elif ch == 1:
                die(0)
            else:
                teen()
        elif ch == 5:
            div()
            print("Ethics:")
            pbar(ethics)
            div()
            print("[1] Max Out Relationships")
            print("[2] Max Out Looks")
            print("[3] Get Clout")
            print("[4] Get social currency")
            print("[5] Join gang")
            print("[6] Go To Juvie")
            print("[0] Return")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                teen()
            elif ch == 1:
                mother_rel = 1
                father_rel = 1
                teen()
            elif ch == 2:
                looks = 1
                teen()
            elif ch == 3:
                clout += 0.25
                teen()
            elif ch == 4:
                socialc += 0.25
                teen()
            elif ch == 5:
                global is_sch_gang, respect
                respect = 0.1
                is_sch_gang = 1
            elif ch == 6:
                global juvie_years, offences
                if offences == 0:
                    offences = 1
                go_to_juvie()
            else:
                teen()
        elif ch == 6:
            print("Welcome to the NEW Crime menu.")
            print("You can perform some crimes >:)")
            if offences > 0:
                div()
                print("You have committed", offences, "offence[s].")
            div()
            print("[0] Return")
            print("[x] Bank Robbery")
            print("[x] Burglary")
            print("[x] GTA")
            print("[x] Hitman")
            print("[x] Murder")
            print("[1] Loitering")
            print("[2] Delinquence")
            print("[3] Pickpocketing")
            print("[4] Shoplift")
            print("[x] Train Robbery")
            div()
            try:
                ch = int(input("<"))
            except:
                ch = 0
            if ch == 0:
                teen()
            elif ch == 1:
                print("You loitered about.")
                clout += 0.1
                teen()
            elif ch == 2:
                print("You harassed people on the street.")
                clout += 0.25
            elif ch == 3:
                from random import randint

                stolen = randint(10, 25)
                print("You stole", stolen, "money!")
                money += stolen
                teen()
            elif ch == 4:
                print("[0] Return")
                print("[1] Cigarettes")
                print("[2] Beer")
                print("[3] Mars candy bar")
                print(f"[4] Gucci handbag [{currency}150]")
                print(f"[5] Wallet [{currency}50]")
                print(f"[6] Smartphone [{currency}500]")
                try:
                    ch = int(input(">"))
                except:
                    ch = 0
                div()
                if ch == 0:
                    teen_activities()
                from random import randint

                caught = randint(1, 2)
                if ch == 1:
                    if caught == 1:
                        print("You nabbed some cigarettes from the local off-license.")
                        print("That old man had no idea!")
                        print("You enjoyed a nice smoke with your 20 friends.")
                        div()
                        clout += 0.45
                        teen()
                    else:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        offences += 1
                        div()
                        div()
                        clout -= 0.45
                        teen()
                elif ch == 2:
                    if caught == 1:
                        print("You took a Budweiser from the local off-license.")
                        print("Sure does taste better when it's free.")
                        clout += 0.35
                        div()
                        teen()
                    elif caught == 2:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        offences += 1
                        div()
                        clout -= 0.35
                        div()
                        go_to_juvie()
                elif ch == 3:
                    print("Five finger discount, am I right?")
                    div()
                    happiness += 0.15
                    clout += 0.1
                    intel -= 0.2
                    teen()
                elif ch == 4:
                    if caught == 1:
                        money += 150
                        clout += 0.55
                        print(f"You sold the handbag for {currency}150.")
                        div()
                        teen()
                    else:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        offences += 1
                        div()
                        clout -= 0.55
                        br()
                        go_to_juvie()
                elif ch == 5:
                    if caught == 1:
                        print("You got a wallet. Now what?")
                        money += 50
                        clout += 0.15
                        br()
                        teen()
                    else:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        offences += 1
                        div()
                        clout -= 0.15
                        br()
                        go_to_juvie()
                elif ch == 6:
                    if caught == 1:
                        print("Nice phone. Said the person I sold it to XD")
                        money += 500
                        clout += 0.75
                        happiness -= 0.45
                    else:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        offences += 1
                        clout -= 0.35
                        br()
                        go_to_juvie()
                else:
                    teen()
        else:
            teen()

    def teen_pause():
        print("[0] Resume")
        print("[x] Save Life")
        print("[x] Load Life")
        print("[3] Exit To Main Menu")
        div()
        print("[x] Download Challenge From Web")
        print("[x] Load Challenge From File")
        print("[x] Check For Updates")
        div()
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 3:
            print("[x] Exit and Save")
            print("[2] Exit Without Saving")
            print("[0] Resume")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 2:
                mainmenu()
            else:
                teen()
        else:
            teen()

    def child_pause():
        print("[0] Resume")
        print("[x] Save Life")
        print("[x] Load Life")
        print("[3] Exit To Main Menu")
        div()
        print("[x] Download Challenge From Web")
        print("[x] Load Challenge From File")
        print("[x] Check For Updates")
        div()
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 3:
            print("[x] Exit and Save")
            print("[2] Exit Without Saving")
            print("[0] Resume")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 2:
                mainmenu()
            else:
                child()
        else:
            child()

    def teen():
        teen_calc_stress()
        global mother_name, father_name
        global offences
        global happiness, health, intel, looks, ethics, grades, clout, socialc
        global mother_rel, father_rel
        global money, is_depressed, is_hbp
        if grades > 1:
            grades = 1
        if grades < 0:
            grades = 0
        if happiness > 1:
            happiness = 1
        if happiness < 0:
            happiness = 0
        if health > 1:
            health = 1
        if health < 0:
            emergency_room(1)
        if intel > 1:
            intel = 1
        if looks > 1:
            looks = 1
        if intel < 0:
            intel = 0
        if looks < 0:
            looks = 0
        if clout > 1:
            clout = 1
        if clout < 0:
            clout = 0
        if socialc > 1:
            socialc = 1
        if socialc < 0:
            socialc = 0
        global forename, surname
        global mother_rel, father_rel
        global money
        div()
        print(forename + " " + surname)
        if fake_id == 1:
            print("[Fake ID Hub Member]")
            div()
        print("Secondary School Student")
        if is_depressed == 1:
            div()
            print("Suffers from: Depression")
            if is_hbp == 0:
                div()
        if is_hbp == 1:
            if is_depressed == 0:
                div()
            print("Suffers from: High Blood Pressure")
            div()
        print("Age", age)
        print(f"{currency}" + str("{:,}".format((money))))
        div()
        print("Clout:          ", pbar2(clout), str(int(clout * 100)) + "%")
        print("Social Currency:", pbar2(socialc), str(int(socialc * 100)) + "%")
        div()
        print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "%")
        print("Health:   ", pbar2(health), str(int(health * 100)) + "%")
        print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "%")
        print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "%")
        div()
        print("[1] School")
        print("[2] Assets")
        print("[0] Age Up")
        print("[3] Relationships")
        print("[4] Activities")
        print("[5] Paue Menu")
        try:
            ch = int(input(">"))
        except:
            teen()
        if ch == 1:
            secondary_school_menu()
        elif ch == 2:
            div()
            teen_assets()
        elif ch == 0:
            age_up(0)
        elif ch == 5:
            teen_pause()
        elif ch == 3:
            div()
            print(mother_name)
            print("Mother [Age " + str(age + 32) + "]")
            pbar(mother_rel)
            print("[1] Interact")
            div()
            print(father_name)
            print("Father [Age " + str(age + 37) + "]")
            pbar(father_rel)
            print("[2] Interact")
            div()
            print("[0] Return")
            div()
            try:
                ch = int(input(">>"))
            except:
                teen()
            if ch == 1:
                print(mother_name)
                print("Mother [Age " + str(age + 32) + "]")
                pbar(mother_rel)
                print("[0] Return")
                print("[1] Spend Time")
                print("[2] Disrespect")
                print("[3] Attack")
                try:
                    ch = int(input(">>"))
                except:
                    ch = 0
                div()
                if ch == 0:
                    teen()
                elif ch == 1:
                    div()
                    print("You spent time with your mother.")
                    mother_rel += 0.25
                    if mother_rel > 1:
                        mother_rel = 1
                    pbar(mother_rel)
                    div()
                    teen()
                elif ch == 2:
                    print("You disrespected your mother.")
                    mother_rel -= 0.25
                    happiness -= 0.35
                    if mother_rel < 0:
                        mother_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(mother_rel)
                    div()
                    teen()
                elif ch == 3:
                    print("You hit your mother.")
                    print("Damage:")
                    pbar(0.65)
                    div()
                    mother_rel -= 0.55
                    happiness -= 0.75
                    if mother_rel < 0:
                        mother_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(mother_rel)
                    div()
                    teen()

            elif ch == 2:
                print(father_name)
                print("Father [Age " + str(age + 32) + "]")
                pbar(father_rel)
                print("[0] Return")
                print("[1] Spend Time")
                print("[2] Disrespect")
                print("[3] Attack")
                try:
                    ch = int(input(">>"))
                except:
                    ch = 0
                div()
                if ch == 0:
                    teen()
                elif ch == 1:
                    div()
                    print("You spent time with your father.")
                    father_rel += 0.25
                    if father_rel > 1:
                        father_rel = 1
                    pbar(father_rel)
                    div()
                    teen()
                elif ch == 2:
                    print("You disrespected your father.")
                    father_rel -= 0.25
                    happiness -= 0.35
                    if father_rel < 0:
                        father_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(father_rel)
                    div()
                    teen()
                elif ch == 3:
                    print("You hit your father.")
                    print("Damage:")
                    pbar(0.25)
                    div()
                    print("Your father retaliated!")
                    print("Damage:")
                    pbar(0.75)
                    health -= 0.75
                    happiness = 0
                    div()
                    is_depressed = 1
                    print("You are now suffering from DEPRESSION.")
                    div()
                    father_rel -= 0.55
                    happiness -= 0.75
                    if father_rel < 0:
                        father_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(father_rel)
                    teen()

            elif ch == 0:
                teen()
        elif ch == 4:
            teen_activities()
        teen()

    def teen_init():
        div()
        print("You are now a teenager.")
        print("You can now earn money and spend it on certain items.")
        print(
            "You will be able to commit juvenile crimes, but you can't go to prison for them yet. Make the most of it."
        )
        print("Enjoy!")
        div()
        print("TIP: You now have 2 new values: CLOUT and SOCIAL CURRENCY.")
        print("CLOUT is earned through crime and parties")
        print("SOCIAL CURRENCY cannot be earned yet.")
        div()
        print("Press ENTER to continue.")
        wer = input()
        global clout, socialc
        global mother_rel, father_rel
        global stress
        stress = 0.65
        from random import randint

        if mother_rel > 0.8:
            mother_rel = 0.8
        if father_rel > 0.8:
            father_rel = 0.8
        socialc = randint(1, 100)
        socialc /= 100
        clout = 0
        teen()

    def child_activities():
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel
        global money
        div()
        print("Activities:")
        print("[0] Return")
        print("[1] Gym")
        print("[2] Library")
        print("[3] Doctor")
        print("[4] Surrender")
        print("[5] Debug Mode")
        try:
            ch = int(input("<"))
        except:
            ch = 0
        if ch == 0:
            child()
        elif ch == 1:
            div()
            happiness += 0.35
            health += 0.25
            print("You visited the gym.")
            print("Enjoyment:")
            pbar(1)
            div()
            child()
        elif ch == 2:
            div()
            print("You visited the library.")
            print("Enjoyment:")
            pbar(0.8)
            intel += 0.25
            div()
            child()
        elif ch == 3:
            div()
            print("No doctor available.")
            div()
            child()
        elif ch == 4:
            die(0)
        elif ch == 5:
            div()
            print("Hidden ethics value:")
            pbar(ethics)
            div()
            print("[1] Max out Relationships")
            print("[2] Max out looks")
            print("[0] Return")
            div()
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                child()
            elif ch == 1:
                father_rel = 1
                mother_rel = 1
            elif ch == 2:
                looks = 1
            else:
                child()
            child()

    def primary_school_menu():
        global grades, intel, happiness
        global stress
        div()
        print("[0] Return")
        print("[1] Primary School")
        print("[x] Freelance")
        print("[x] Jobs")
        print("[x] Military")
        print("[x] Part-Time Jobs")
        print("[x] Special Careers")
        print("Stress:")
        pbar(0.5)
        div()
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            div()
            child()
        elif ch == 1:
            div()
            print("Grades:")
            pbar(grades)
            div()
            print("[1] Study Harder")
            print("[2] Skip School")
            print("[0] Return")
            div()
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                child()
            elif ch == 1:
                div()
                print("You studied until you lost your vision.")
                div()
                grades += 0.25
                intel += 0.15
                child()
            elif ch == 2:
                div()
                print("Insted of going to school, you decided to go bowling instead.")
                div()
                grades -= 0.25
                intel -= 0.35
                happiness -= 0.45
                child()
            div()
            child()
        else:
            div()
            child()

    def child():
        global mother_name, father_name
        global happiness, health, intel, looks, ethics, grades
        if grades > 1:
            grades = 1
        if grades < 0:
            grades = 0
        if happiness > 1:
            happiness = 1
        if happiness < 0:
            happiness = 0
        if health > 1:
            health = 1
        if health < 0:
            health = 0
        if intel > 1:
            intel = 1
        if looks > 1:
            looks = 1
        if intel < 0:
            intel = 0
        if looks < 0:
            looks = 0
        global forename, surname
        global mother_rel, father_rel
        global money
        print(forename + " " + surname)
        print("Primary School Student")
        print("Age", age)
        print(f"{currency}" + str("{:,}".format((money))))
        div()
        print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "%")
        print("Health:   ", pbar2(health), str(int(health * 100)) + "%")
        print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "%")
        print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "%")
        div()
        print("[1] School")
        print("[2] Assets")
        print("[0] Age Up")
        print("[3] Relationships")
        print("[4] Activities")
        print("[5] Pause Menu")
        try:
            ch = int(input(">"))
        except:
            child()
        if ch == 1:
            primary_school_menu()
        elif ch == 5:
            child_pause()
        elif ch == 2:
            div()
            print("Locked.")
            div()
        elif ch == 0:
            age_up(0)
        elif ch == 3:
            div()
            print(mother_name)
            print("Mother [Age " + str(age + 32) + "]")
            pbar(mother_rel)
            print("[1] Interact")
            div()
            print(father_name)
            print("Father [Age " + str(age + 37) + "]")
            pbar(father_rel)
            print("[2] Interact")
            div()
            print("[0] Return")
            div()
            try:
                ch = int(input(">>"))
            except:
                child()
            if ch == 1:
                print(mother_name)
                print("Mother [Age " + str(age + 32) + "]")
                pbar(mother_rel)
                print("[0] Return")
                print("[1] Spend Time")
                print("[2] Disrespect")
                print("[3] Attack")
                try:
                    ch = int(input(">>"))
                except:
                    ch = 0
                div()
                if ch == 0:
                    child()
                elif ch == 1:
                    div()
                    print("You spent time with your mother.")
                    mother_rel += 0.25
                    if mother_rel > 1:
                        mother_rel = 1
                    pbar(mother_rel)
                    div()
                    child()
                elif ch == 2:
                    print("You disrespected your mother.")
                    mother_rel -= 0.25
                    happiness -= 0.35
                    if mother_rel < 0:
                        mother_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(mother_rel)
                    div()
                    child()
                elif ch == 3:
                    print("You hit your mother.")
                    print("Damage:")
                    pbar(0.65)
                    div()
                    mother_rel -= 0.55
                    happiness -= 0.75
                    if mother_rel < 0:
                        mother_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(mother_rel)
                    div()
                    child()
            elif ch == 2:
                print(father_name)
                print("father [Age " + str(age + 32) + "]")
                pbar(father_rel)
                print("[0] Return")
                print("[1] Spend Time")
                print("[2] Disrespect")
                print("[3] Attack")
                try:
                    ch = int(input(">>"))
                except:
                    ch = 0
                div()
                if ch == 0:
                    child()
                elif ch == 1:
                    div()
                    print("You spent time with your father.")
                    father_rel += 0.25
                    if father_rel > 1:
                        father_rel = 1
                    pbar(father_rel)
                    div()
                    child()
                elif ch == 2:
                    print("You disrespected your father.")
                    father_rel -= 0.25
                    happiness -= 0.35
                    if father_rel < 0:
                        father_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(father_rel)
                    div()
                    child()
                elif ch == 3:
                    div()
                    print("You hit your father.")
                    print("Damage:")
                    pbar(0.25)
                    father_rel -= 0.55
                    happiness -= 0.75
                    if father_rel < 0:
                        father_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(father_rel)
                    child()

                child()
            elif ch == 0:
                child()
        elif ch == 4:
            child_activities()
        child()

    def child_init():
        global mother_rel, father_rel
        print(
            "You are now a child. You have more activities to do and can also use money."
        )
        print("Once you hit 12, you'll be a teen.")
        print("Hint: Don't die")
        mother_rel -= 0.3
        if mother_rel < 0:
            mother_rel = 0
        father_rel -= 0.3
        if father_rel <= 0:
            father_rel = 0
        div()
        global money
        money = 0
        global grades, intel
        grades = intel
        print("You have now joined Primary School")
        div()
        wer = input("Press ENTER to continue. ")
        child()

    def infant_activities():
        print("[1] Surrender")
        print("[2] Return To Menu")
        print("[0] Exit")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            infant()
        elif ch == 1:
            die(0)
        elif ch == 2:
            mainmenu()

    def infant():
        global mother_name, father_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel, age
        if happiness > 1:
            happiness = 1
        if happiness < 0:
            happiness = 0
        if health > 1:
            health = 1
        if health < 0:
            health = 0
        if intel > 1:
            intel = 1
        if looks > 1:
            looks = 1
        if intel < 0:
            intel = 0
        if looks < 0:
            looks = 0
        if age > 5:
            child()
        else:
            div()
            print(forename + " " + surname)
            print("Age:", age)
            div()
            print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "%")
            print("Health:   ", pbar2(health), str(int(health * 100)) + "%")
            print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "%")
            print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "%")
            div()
            print("[0] Age Up")
            print("[1] Relationships")
            print("[2] Activities")
            try:
                ch = int(input(">"))
            except:
                ch = 999
            if ch == 0:
                age_up(0)
            elif ch == 1:
                print(mother_name)
                print("Mother [Age", str(age + 32) + "]")
                pbar(mother_rel)
                print("[1] Interact with")
                div()
                print(father_name)
                print("Father [Age", str(age + 37) + "]")
                pbar(father_rel)
                print("[x] Interact with")
                div()
                print("[0] Return to menu")
                div()
                try:
                    ch = int(input(">"))
                except:
                    ch == 0
                if ch == 0:
                    infant()
                elif ch == 1:
                    print(mother_name)
                    print("Mother [Age ", str(age + 32) + "]")
                    pbar(mother_rel)
                    print("[0] Leave")
                    print("[1] Spend Time With")
                    print("[2] Disobey")
                    print("[3] Attack")
                    try:
                        ch = int(input(">"))
                    except:
                        ch = 0
                    if ch == 0:
                        infant()
                    elif ch == 1:
                        mother_rel += 0.25
                        if mother_rel > 1:
                            mother_rel = 1
                        print("You spent time with your mother.")
                        pbar(mother_rel)
                    elif ch == 2:
                        print("You disobeyed your mother.")
                        mother_rel -= 0.35
                        happiness -= 0.35
                        if happiness < 0:
                            happiness = 0
                        if mother_rel < 0:
                            mother_rel = 0
                        pbar(mother_rel)
                    elif ch == 3:
                        print("You hit your mother!")
                        print("Damage:")
                        pbar(0.15)
                        mother_rel -= 0.35
                        if mother_rel < 0:
                            mother_rel = 0
                        print("Relationship:")
                        pbar(mother_rel)
                    else:
                        infant()
                else:
                    infant()
            elif ch == 2:
                infant_activities()
            else:
                div()
                print("Locked.")
                infant()
                div()
            infant()

    def infant_start():
        global happiness, health, intel, looks, ethics, game_name, forename, surname, mother_name, father_name, mother_age, father_age, job_roles, birthdays, gender
        div()
        global mother_rel, father_rel
        mother_rel = 1
        father_rel = 1
        if gender == 0:
            print("I was born a male in OpenLife, OpenLife.")
        else:
            print("I was born a female in OpenLife, OpenLife.")
        print(f"My name is {forename} {surname}.")
        print(
            f"My mother is {mother_name}, a {mother_age}-year-old {choice(job_roles)}."
        )
        print(
            f"My father is {father_name}, a {father_age}-year-old {choice(job_roles)}."
        )
        div()
        print(f"My birthday is {choice(birthdays)}.")
        div()
        print(f"Welcome to {game_name}.")
        print("You are now a toddler.")
        print("Changes you make will affect your stats and change your life.")
        print("Since life is [literally] a game, you should try to win it.")
        print("'Winning' can be defined as reaching your life goal.")
        print("That goal can be anything. Getting your dream job, becoming rich,")
        print("living a fulfilling life, etc.")
        global age
        br()
        infant()

    def quick_life():
        global forename_m, forename_f, salary, hours, start_age, happiness, health, looks, intel, ethics, forename, surname, gender, children
        children = []
        salary = 0
        hours = 0
        global edu_lvl
        edu_lvl = 0
        global mother_name, father_name
        from random import choice

        global sexuality, is_trans
        sexuality, is_trans = 0, 0

        mother_name = choice(forename_f)
        father_name = choice(forename_m)
        global happiness, health, intel, looks, ethics
        from random import randint

        if allow_debug == 1:
            happiness = 1
            health = 1
            looks = 1
            intel = 1
        else:
            happiness = (rng(1, 100)) / 100
            health = (rng(1, 100)) / 100
            intel = (rng(1, 100)) / 100
            looks = (rng(1, 100)) / 100
        ethics = 1
        start_age = 18
        gender = rng(0, 1)
        if gender == 0:
            forename = choice(forename_m)
        else:
            forename = choice(forename_f)
        surname = choice(surnames)
        mother_name += " " + surname
        father_name += " " + surname
        choose_start(0)

    def life_creator():
        global forename_m, forename_f, salary, hours, gender, car_1, car_2, car_3, children, surnames
        children = []
        salary = 0
        hours = 0
        global edu_lvl
        edu_lvl = 0
        global mother_name, father_name
        from random import choice
        

        mother_name = choice(forename_f)
        father_name = choice(forename_m)
        global happiness, health, intel, looks, ethics
        global sexuality, is_trans
        sexuality = 0  # 1= gay, 2=lesbian, 3=NB, 4=asexual
        is_trans = 0
        from random import randint

        print("[1] Male")
        print("[2] Female")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 1:
            gender = 0
        elif ch == 2:
            gender = 1
        else:
            gender = rng(0, 1)
        print()
        print("[1] Random Life")
        print("[2] Custom Life")
        try:
            ch = int(input(">"))
        except:
            ch = 1
        if ch == 1:
            global forename, surname
            forename = input("Forename >>")
            if forename == "":
                if gender == 0:
                    forename = choice(forename_m)
                else:
                    forename = choice(forename_f)

            surname = input("Surname >>")
            if surname == "":
                surname = choice(surnames)
            forename = forename.replace("|", "")
            surname = surname.replace("|", "")
            if forename == "Tom" and surname == "Parker":
                gender, forename_m, forename_f, surnames, mother_name, father_name = 0, ["Tom"],["Tom"],["Parker"],"Tom","Tom"
            mother_name += " " + surname
            father_name += " " + surname
            happiness = randint(1, 100)
            happiness /= 100
            health = randint(1, 100)
            health /= 100
            intel = randint(1, 100)
            intel /= 100
            looks = randint(1, 100)
            looks /= 100
            ethics = 1
            global start_age
            try:
                start_age = int(input("Enter START AGE >"))
            except:
                start_age = 0
            choose_start(1)
            try:
                start_age = int(input("Enter START AGE >"))
                choose_start(1)
            except:
                start_age = 0
                choose_start(1)
            choose_start(1)
        elif ch == 2:
            print("[1] Maxxed-out Values")
            print("[2] 0% Everything")
            print("[3] Custom Values")
            try:
                wer = int(input(">>"))
            except:
                wer = 1
            # name=input("Name >>")
            forename = input("Forename >>")
            if forename == "":
                forename = choice(forename_m)
            surname = input("Surname >>")
            if surname == "":
                surname = choice(surnames)
            try:
                start_age = int(input(">Start Age >"))
            except:
                start_age = 0
            forename = forename.replace("|", "")
            surname = surname.replace("|", "")
            from random import randint

            if wer == 1:
                happiness = randint(1, 1)
                health = randint(1, 1)
                intel = randint(1, 1)
                looks = randint(1, 1)
                ethics = 1
            elif wer == 2:
                happiness = 0
                health = 0
                intel = 0
                looks = 0
                ethics = 0
            elif wer == 3:
                from random import randint

                print("Enter the percent amount of each value.")
                try:
                    happiness = int(input("Happiness age_up(0)"))
                except:
                    happiness = randint(1, 100)
                happiness /= 100
                try:
                    intel = int(input("Intelligence $"))
                except:
                    intel = randint(1, 100)
                intel /= 100
                try:
                    health = int(input("Health $"))
                except:
                    health = randint(1, 100)
                health /= 100
                try:
                    looks = int(input("Looks  $"))
                except:
                    looks = randit(1, 100)
                looks /= 100
                ethics = 1

            else:
                mainmenu()
            choose_start(1)
        else:
            print("An error occured.")
            raise ExitError

    def mainmenu():
        game_init()
        cls()
        global has_first_run
        global instant_life
        if has_first_run == 1:
            if instant_life == 1:
                has_first_run = 2
                quick_life()
        global alt_logo
        div()
        import os

        startpoint = os.getcwd()
        challenge_site = ""  # change this URL if the location changes / you want to add custom challenges
        if alt_logo == 1:
            logo = [
                " .d88888b.                             888      d8b  .d888         ",
                'd88P" "Y88b                            888      Y8P d88P"          ',
                "888     888                            888          888            ",
                "888     888 88888b.   .d88b.  88888b.  888      888 888888 .d88b.  ",
                '888     888 888 "88b d8P  Y8b 888 "88b 888      888 888   d8P  Y8b ',
                "888     888 888  888 88888888 888  888 888      888 888   88888888 ",
                "Y88b. .d88P 888 d88P Y8b.     888  888 888      888 888   Y8b.     ",
                ' "Y88888P"  88888P"   "Y8888  888  888 88888888 888 888    "Y8888  ',
                "            888                                                    ",
                "            888                                                    ",
                "            888                                                    ",
            ]
        elif alt_logo == 2:
            logo = [
                " #######  ########  ######## ##    ## ##       #### ######## ######## ",
                "##     ## ##     ## ##       ###   ## ##        ##  ##       ##       ",
                "##     ## ##     ## ##       ####  ## ##        ##  ##       ##       ",
                "##     ## ########  ######   ## ## ## ##        ##  ######   ######   ",
                "##     ## ##        ##       ##  #### ##        ##  ##       ##       ",
                "##     ## ##        ##       ##   ### ##        ##  ##       ##       ",
                " #######  ##        ######## ##    ## ######## #### ##       ######## ",
            ]
            # Logo: Old Banner
        else:
            logo = [
                "________                           .____     .__   _____         ",
                "\\_____  \\  ______    ____    ____  |    |    |__|_/ ____\\ ____   ",
                " /   |   \\ \\____ \\ _/ __ \\  /    \\ |    |    |  |\\   __\\_/ __ \\  ",
                "/    |    \\|  |_> >\\  ___/ |   |  \\|    |___ |  | |  |  \\  ___/  ",
                "\\_______  /|   __/  \\___  >|___|  /|_______ \\|__| |__|   \\___  > ",
                "        \\/ |__|         \\/      \\/         \\/                \\/  ",
            ]
        for l in logo:
            if l == "%div%":
                div()
            else:
                print(l)
        div()
        print("[1] New Life")
        print("[2] Load Life")
        print("[3] Credits")
        print(
            "[4] Download Latest Challenge"
        )  # Download Location: http://winfan3672.000webhostapp.com/challenge/latest.zip
        print("[5] Load Challenge From Disk")
        print("[6] Exit")
        print("[7] Changelog [Alpha 16]")
        print("[8] Download Latest Custom Life")  # Download location: N/A
        print("[9] Options")
        print("[10] Quick Create Life")
        print("[11] Check for Updates")
        print("[12] Download Latest OpenLife Times Article")
        print("[0] About Game")
        div()
        print("Version:", version)
        div()
        try:
            ch = int(input(">>"))
        except:
            mainmenu()
        if ch == 1:
            life_creator()
        elif ch == 10:
            quick_life()
        elif ch == 11:
            import urllib.request

            url = "http://winfan3672.000webhostapp.com/version_check/openlife.version"
            print("Checking for updates...")
            print(
                f"Current Version: {app_version[0]}.{app_version[1]}.{app_version[2]} [sub-version {sub_version}]"
            )
            try:
                urllib.request.urlretrieve(url, "openlife.version")
            except:
                div()
                print("Failed to check for updates.")
                div()
                print("You could try:")
                print("[-] Checking that you are connected to the Internet.")
                print(
                    "[-] Checking that winfan3672.000webhostapp.com is still up, since that is the server that provides the version check information."
                )
                print(
                    "[-] Checking that http://winfan3672.000webhostapp.com/version_check/openlife.versio exists, since it may have been deleted."
                )
                print(
                    "[-] Checking that your antivirus or firewall is not blocking winfan3672.000webhostapp.com/"
                )
                print("[-] On Windows, deleting your DNS resolver cache.")
                adult_pause()
            div()
            f = open("openlife.version", "r")
            data = f.read()
            data = data.split("|")
            data = [int(data[0]), int(data[1]), int(data[2])]
            try:
                urllib.request.urlretrieve(
                    "http://winfan3672.000webhostapp.com/latest_v_url/openlife",
                    "openlife.version",
                )
                f = open("openlife.version", "r")
                url = f.read()
            except:
                url = "[Could not retrieve URL from server]"
            not_update_text = f"An update for {game_name} [{data[0]}.{data[1]}.{data[2]}] is available.\nDownload it from:\n{url}"
            if data[0] > app_version[0]:
                print(not_update_text)
            else:
                if data[1] > app_version[1]:
                    print(not_update_text)
                else:
                    if data[2] > app_version[2]:
                        print(not_update_text)
                    else:
                        if data[0] < app_version[0] or data[1] < app_version[1] or data[2] < app_version[2]:
                            print(f"You are on a pre-release build; latest stable build is {data[0]}.{data[1]}.{data[2]}.")
                        else:
                            print(f"You are on the latest version of {game_name}.")
            br()
            mainmenu()
        elif ch == 9:
            div()
            edit_configuration()
            mainmenu()
        elif ch == 8:
            import urllib.request

            url = "https://winfan3672.000webhostapp.com/custom_life/customlife.oll2"
            print("Downloading custom life...")
            try:
                urllib.request.urlretrieve(url, "custom_life.oll2")
            except:
                div()
                print("Failed to download custom life.")
                mainmenu()
            div()
            print("Downloaded custom life as `custom_life.oll2`.")
            mainmenu()
        elif ch == 6:
            raise ExitError
        elif ch == 0:
            div()
            print(game_name, "is a clone of BitLife written in Python3.")
            print(
                "For years, BitLife: Life Simulator has suffered from a lot of issues, including:"
            )
            div()
            print("[-] Lazy Development")
            print("[-] Cash Grabbing")
            print("[-] In-App Purchases that increase in price [$5 --> $20]")
            print("[-] Paywalls for achievements/features/updates/challenges")
            print("[-] No PC Release")
            print("[-] A lack of updates")
            print("[-] A game focused too much on RNG.")
            div()
            print(f"{game_name} will be a version of BitLife with:")
            div()
            print("[-] More features")
            print("[-] 100% FOSS code")
            print("[-] No paywalls")
            print(
                "[-] A multi-platform, multi-architecture system [since it's Python3]"
            )
            print("[-] No lag [since it's a Python script, anyone can run that]")
            div()
            print(
                f"On top of this, {game_name} promises to only use the Python standard library, so you do not need to install anything."
            )
            print(
                f"{game_name} will be better than BitLife by the time 1.0.0 is released."
            )
            div()
            print(
                f"The server for OpenLife is provided by 000webhost, and can be accessed by anyone [https://winfan3672.000webhostapp.com/] in order to navigate its pages."
            )
            print(
                f"The server will only use basic HTML in order to allow for basic things such as challenges [yes!] and update checks."
            )
            div()
            print(f"I hope you enjoy {game_name}.")
            br()
            div()
            mainmenu()
        elif ch == 2:
            load_game()
        elif ch == 3:
            div()
            print("99% of the code was written by WinFan3672 [winfan3672@gmail.com]")
            print(
                "The logo for the game was generated by textkool.com. [Font: Old Banner]"
            )
            div()
            print("Resources:")
            print("The forenames and surnames were created by MufasaKermitsSuicide.")
            print("The hosting for the challenges is provided by 000webhost.")
            div()
            print(
                "Thank you for playing the most ambitious programming project I have taken on."
            )
            div()
            print("And special thanks to fungamer2 for:")
            print("[-] Finding my project")
            print(
                "[-] Allowing me to help out on his one [https://github.com/Fungamer2-2/Life-Simulator1/]"
            )
            print("[-] Generally being a nice guy")
            br()
            div()
            mainmenu()
        elif ch == 4:
            import urllib.request

            url = "https://winfan3672.000webhostapp.com/challenge/latest.zip"
            print("Downloading challenge...")
            try:
                urllib.request.urlretrieve(url, "challenge.zip")
            except:
                div()
                print("Failed to download challenge.")
                mainmenu()
            div()
            print("Downloaded challenge.")
            mainmenu()
        elif ch == 12:
            ol_times()
            mainmenu()
        elif ch == 5:
            import sys

            sys.path.insert(0, "challenge.zip")
            try:
                import challenge

                challenge.init(app_version)
            except:
                div()
                print("The challenge failed to load.")
                div()
                print("Possible fixes:")
                print(
                    '[-] Make sure that a file called "challenge.zip" exists in your /openlife_saves folder'
                )
                print("[-] Download the challenge [main menu option 4]")
                print(
                    "[-] Download the latest version of the game, since the code for running the Challenge may be outdated."
                )
                print(
                    "[-] Check the download server [winfan3672.000webhostapp.com] is up. If not, challenges no longer work."
                )
                print(
                    "[-] Make sure that you can open challenge.zip [in /openlife_saves]. If not, give yourself read access."
                )
                print(
                    "[-] Try again later and download the challenge, it may be updated to work :)"
                )
                br()
            mainmenu()
        elif ch == 7:
            changelog = [
                'Alpha 16- The "Bugfix" Update',
                "====================",
                "Alpha 16 is a rushed update. I feel that if I do not finish it, I will automatically not want to work on the game. ",
                "====================",
                "Additions",
                "====================",
                "[-] Lottery wins",
                "   [-] A value that counts how many times you've won the lottery",
                "[-] New Ribbon- Cheater",
                "   [-] Win the lottery 50+ times",
                "[-] Updated relations menu",
                "   [-] Child list",
                "  [-] A less cluttered way of viewing all of your children.",
                "====================",
                "Bug Fixes",
                "====================",
                "[-] Fixed a double div() element when exiting the game without saving it. ",
                "====================",
                "Delay",
                "====================",
                "Alpha 16 was delayed by about half a week because of SGCU issues. It had trouble converting from Alpha 14 to Alpha 15. ",
            ]
            for l in changelog:
                l = l.replace("{game_name}", game_name)
                l = l.replace("OpenLife", game_name)
                if l == "====================":
                    div()
                else:
                    print(l)
            br()
            mainmenu()
        else:
            mainmenu()
    mainmenu()
except KeyboardInterrupt:
    try:
        div()
        print("The game has self-destructed.")
        print("You now cannot cheat, because there is no game :)")
        div()
        print("If you can see this, close the window or restart the game.")
        div()
        objects = dir()
        for obj in objects:
            if not obj.startswith("__"):
                del globals()[obj]
    except:
        div()
        print("The game has self-destructed.")
        print("You now cannot cheat, because there is no game :)")
        div()
        print("If you can see this, close the window or restart the game.")
        div()
        objects = dir()
        for obj in objects:
            if not obj.startswith("__"):
                del globals()[obj]
except LifeCreatorError:
    pass
except FeatureNotInGameError:
    div()
    print("FeatureNotInGameError")
    div()
    print("Somehow, you activated a choice so invalid that")
    print("you tried to access something not in the game.")
    print("When this happens, the game assumes you're cheating, since")
    print("you're not meant to do that.")
    print("This is one of our many safeguards against that.")
    div()
    print("The game has self-destructed.")
    print("You now cannot cheat, because there is no game :)")
    div()
    print("If you can see this, close the window or restart the game.")
    div()
    objects = dir()
    for obj in objects:
        if not obj.startswith("__"):
            del globals()[obj]
except ExitError:
    if allow_debug == 1 or allow_debug == 3:
        # https://www.geeksforgeeks.org/viewing-all-defined-variables-in-python/
        # This code spits out all variables in memory
        # in a format I can filter using a special program in order to list them by type :) [used when developing save system]
        # Very, very useful and very, very specialised.
        all_variables = dir()

        # Iterate over the whole list where dir()
        # is stored.
        for name in all_variables:

            # Print the item if it doesn't start with '__'
            if not name.startswith("__"):
                myvalue = eval(name)
                base = type(myvalue)
                if allow_debug != 3:
                    print(name, "|", type(myvalue))
                else:
                    print(name, "|", type(myvalue), "|", myvalue)
                # print(name, "is", type(myvalue), "and is equal to ", myvalue)

    # Code from: https://maschituts.com/how-to-clear-variables-in-python-explained/
    if allow_debug != 2:
        div()
        print("The game has self-destructed.")
        print("You now cannot cheat, because there is no game :)")
        div()
        print("If you can see this, close the window or restart the game.")
        div()
        objects = dir()
        for obj in objects:
            if not obj.startswith("__"):
                del globals()[obj]
