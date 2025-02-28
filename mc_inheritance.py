class Motorcycle:
    def start(self):
        print("Motorcycle start.")

    def stop(self):
        print("Motorcycle off.")

    def throttle(self):
        print("Motorcycle moving.")

    def brake(self):
        print("Motorcycle stopping.")

class InlineEngine:
    pass

class Inline4(InlineEngine):
    def engine_type(self):
        return "Inline 4"

class Inline3(InlineEngine):
    def engine_type(self):
        return "Inline 3"

class Inline2(InlineEngine):
    def engine_type(self):
        return "Inline 2"

class Kawasaki:
    def brand(self):
        return "Kawasaki"

class Honda:
    def brand(self):
        return "Honda"

class Yamaha:
    def brand(self):
        return "Yamaha"

class BMW:
    def brand(self):
        return "BMW"

class CFMoto:
    def brand(self):
        return "CFMoto"

class Triumph:
    def brand(self):
        return "Triumph"

class NinjaZX6R(Motorcycle, Inline4, Kawasaki):
    def model(self):
        return "Ninja ZX-6R"

class NinjaZX10R(Motorcycle, Inline4, Kawasaki):
    def model(self):
        return "Ninja ZX-10R"

class CBR1000(Motorcycle, Inline4, Honda):
    def model(self):
        return "CBR 1000"

class M1000RR(Motorcycle, Inline4, BMW):
    def model(self):
        return "M 1000 RR"

class R1(Motorcycle, Inline4, Yamaha):
    def model(self):
        return "R1"

class Daytona600(Motorcycle, Inline3, Triumph):
    def model(self):
        return "Daytona 600"

class MT09(Motorcycle, Inline3, Yamaha):
    def model(self):
        return "MT-09"

class R9(Motorcycle, Inline3, Yamaha):
    def model(self):
        return "R9"

class Ninja400(Motorcycle, Inline2, Kawasaki):
    def model(self):
        return "Ninja 400"

class R3(Motorcycle, Inline2, Yamaha):
    def model(self):
        return "R3"

class CFMoto450SR(Motorcycle, Inline2, CFMoto):
    def model(self):
        return "450SR"

class CFMotoNK400(Motorcycle, Inline2, CFMoto):
    def model(self):
        return "NK400"

class Ninja300(Motorcycle, Inline2, Kawasaki):
    def model(self):
        return "Ninja 300"

motorcycles = {
    "zx6r": NinjaZX6R(),
    "r1": R1(),
    "r3": R3(),
    "mt09": MT09(),
    "cf450": CFMoto450SR(),
    "daytona": Daytona600(),
    "zx10r": NinjaZX10R(),
    "cbr1000": CBR1000(),
    "m1000rr": M1000RR(),
    "r9":R9(),
    "ninja400":Ninja400(),
    "cf400":CFMotoNK400(),
    "ninja300":Ninja300(),
}

def display_motorcycles():
    print("Available Motorcycles:")
    for key, motorcycle in motorcycles.items():
        print(f"- {key}: {motorcycle.brand()} {motorcycle.model()} - {motorcycle.engine_type()}")

def get_motorcycle_choice():
    display_motorcycles()
    while True:
        choice = input("Enter motorcycle name (or 'exit' to quit): ").lower()
        if choice == "exit":
            return None
        if choice in motorcycles:
            return motorcycles[choice]
        else:
            print("Invalid choice. Please try again.")

def motorcycle_actions(motorcycle):
    while True:
        print("\nMotorcycle Actions:")
        print("1. Start")
        print("2. Throttle")
        print("3. Brake")
        print("4. Stop")
        print("5. Display Info")
        print("6. Choose another motorcycle")
        print("7. Exit")
        action = input("Choice: ")

        if action == "1":
            motorcycle.start()
        elif action == "2":
            motorcycle.throttle()
        elif action == "3":
            motorcycle.brake()
        elif action == "4":
            motorcycle.stop()
        elif action == "5":
            print(f"{motorcycle.brand()} {motorcycle.model()} - {motorcycle.engine_type()}")
        elif action == "6":
            return True
        elif action == "7":
            return False
        else:
            print("Invalid action.")

while True:
    motorcycle = get_motorcycle_choice()
    if motorcycle is None:
        break
    if not motorcycle_actions(motorcycle):
        break
