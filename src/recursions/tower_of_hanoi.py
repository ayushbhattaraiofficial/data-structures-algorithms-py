class TowerOfHanoi:
    def getNumberOfDisk(self):
        return int(input("Enter the number of disks "))

    def getPole(self, pole_name):
        return str(input(f"Enter the pole name for {pole_name} "))

    def moveDisks(self, disks, pole1, pole2, pole3):
        if disks > 0:
            self.moveDisks(disks - 1, pole1, pole3, pole2)
            print(f"Move disk {disks} from {pole1} to {pole2}")
            self.moveDisks(disks - 1, pole3, pole2, pole1)

    def run(self):
        disks = self.getNumberOfDisk()
        origin = self.getPole("origin")
        destination = self.getPole("destination")
        intermediate = self.getPole("intermediate")
        self.moveDisks(disks, origin, destination, intermediate)
