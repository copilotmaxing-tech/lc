class AmbulanceAgent:

    def readSensorData(self):
        self.speed = int(input("Enter Current Speed (km/h): "))
        self.signal = input("Enter Traffic Signal (RED/YELLOW/GREEN): ").upper()
        self.vehicleDistance = int(input("Enter Vehicle Distance Ahead (m): "))
        self.congestion = input("Enter Congestion Level (LOW/MEDIUM/HEAVY): ").upper()
        self.pedestrian = input("Pedestrian Crossing (YES/NO): ").upper()
        self.pedestrianDistance = int(input("Pedestrian Distance (m): "))
        self.priority = input("Enter Emergency Priority (LOW/MEDIUM/HIGH): ").upper()
        self.hospitalDistance = int(input("Enter Distance to Hospital (km): "))
        self.alternateLane = input("Alternate Lane Available (YES/NO): ").upper()

    # Safety rules
    def checkSafety(self):
        if self.hospitalDistance == 0:
            return "STOP"
        if self.vehicleDistance < 5:
            return "BRAKE"
        if self.pedestrian == "YES" and self.pedestrianDistance < 10:
            return "STOP"
        return "NONE"

    # Traffic signal rules
    def evaluateTraffic(self):
        if self.signal == "RED":
            if self.priority == "HIGH":
                return "SLOW_DOWN"
            else:
                return "STOP"

        if self.signal == "YELLOW":
            return "SLOW_DOWN"

        if self.signal == "GREEN":
            if self.speed < 30:
                return "ACCELERATE"
            elif self.speed <= 60:
                return "MAINTAIN_SPEED"
            else:
                return "SLOW_DOWN"

        return "SLOW_DOWN"

    # Congestion rules
    def evaluateCongestion(self):
        if self.congestion == "HEAVY":
            if self.alternateLane == "YES":
                return "CHANGE_LANE"
            else:
                return "SLOW_DOWN"
        return "NONE"

    # Final decision
    def decideAction(self):
        result = self.checkSafety()

        if result == "NONE":
            if self.signal == "RED":
                result = self.evaluateTraffic()
            else:
                result = self.evaluateCongestion()

                if result == "NONE":
                    result = self.evaluateTraffic()

        self.finalAction = result
        self.riskScore = self.calculateRiskScore()

        if self.riskScore <= 20:
            self.riskLevel = "LOW"
        elif self.riskScore <= 50:
            self.riskLevel = "MEDIUM"
        else:
            self.riskLevel = "HIGH"

        return self.finalAction

    # Calculate risk score
    def calculateRiskScore(self):
        score = 0

        if self.speed > 60:
            score += 20
        elif self.speed >= 30:
            score += 10
        else:
            score += 5

        if self.vehicleDistance < 5:
            score += 10
        elif self.vehicleDistance < 15:
            score += 5
        elif self.vehicleDistance < 30:
            score += 2

        if self.congestion == "HEAVY":
            score += 20
        elif self.congestion == "MEDIUM":
            score += 15
        elif self.congestion == "LOW":
            score += 5

        if self.pedestrian == "YES":
            if self.pedestrianDistance < 10:
                score += 20
            elif self.pedestrianDistance < 20:
                score += 10
            else:
                score += 5

        return score

    # Display status
    def displayStatus(self):
        print("\n--------- AMBULANCE AGENT ---------")
        print("Current Speed:", self.speed, "km/h")
        print("Traffic Signal:", self.signal)
        print("Vehicle Distance:", self.vehicleDistance, "m")
        print("Congestion:", self.congestion)
        print("Pedestrian:", self.pedestrian)
        print("Pedestrian Distance:", self.pedestrianDistance, "m")
        print("Priority:", self.priority)
        print("Hospital Distance:", self.hospitalDistance, "km")
        print("Risk Score:", self.riskScore)
        print("Risk Level:", self.riskLevel)
        print("Final Action:", self.finalAction)

    # Check hospital arrival
    def hasArrived(self):
        return self.finalAction == "STOP" and self.hospitalDistance == 0


# Main program
agent = AmbulanceAgent()

steps = 5

for t in range(1, steps + 1):
    print("\n===== TIME STEP", t, "=====")

    agent.readSensorData()
    agent.decideAction()
    agent.displayStatus()

    if agent.hasArrived():
        print("\nHospital reached, stopping simulation.")
        break