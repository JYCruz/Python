class Motorcycle:
    def start(self):
        print("Motorcycle started.")

    def stop(self):
        print("Motorcycle stopped.")

    def throttle(self):
        print("Motorcycle accelerating.")

    def brake(self):
        print("Motorcycle braking.")

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
    def brand(self):
        return "Triumph"
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

zx6r = NinjaZX6R()
zx6r.start()
zx6r.throttle()
zx6r.brake()
zx6r.stop()
print(f"{zx6r.brand()} {zx6r.model()} - {zx6r.engine_type()}")

r1 = R1()
print(f"{r1.brand()} {r1.model()} - {r1.engine_type()}")

r3 = R3()
print(f"{r3.brand()} {r3.model()} - {r3.engine_type()}")

mt09 = MT09()
print(f"{mt09.brand()} {mt09.model()} - {mt09.engine_type()}")

cf450 = CFMoto450SR()
print(f"{cf450.brand()} {cf450.model()} - {cf450.engine_type()}")

daytona = Daytona600()
print(f"{daytona.brand()} {daytona.model()} - {daytona.engine_type()}")
