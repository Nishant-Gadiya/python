class vehicle:
    def __init__(self,name,number,status=False):
        self.status=status
        self.name=name
        self.number=number

    def get(self):
        if self.status:
            print("Engine is ON !!!!")
        else:
            print("Engine is OFF !!!!")

    def off(self):
        self.status=False

    def on(self):
        self.status=True

car=vehicle("Maruti",400)
car.get()
car.on()
car.get()
car.off()
car.get()