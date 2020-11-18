class Horse:
    def __init__(self,n,r):
        self.h_name=n
        self.h_rider=r

class Rider:
    def __init__(self,n):
        self.r_name=n


a_rider=Rider("Nakayama")
a_horse=Horse("tsubasa",a_rider)

print(a_horse.h_rider.r_name)


b_rider=Rider("Tokita")
b_horse=Horse("riki",b_rider)
print(b_horse.h_rider.r_name)


