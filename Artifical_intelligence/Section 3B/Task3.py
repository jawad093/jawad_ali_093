class MultiReflexAgent:
    def __init__(self, desired_temp):
        self.desired_temp = desired_temp
        self.actions_log = {} 

    def percept(self, room, temp):
        self.current_temp = temp  
        self.room = room  

    def act(self):
        if self.current_temp > self.desired_temp:
            action = "Get the stove"  
        else:
            action = "Get the heater"  #
        self.actions_log[self.room] = {
            'current_temp': self.current_temp, 
            'action': action  
        }

        return action  

    def report(self):
        print("\nAction executed:")
        for room, info in self.actions_log.items():  
            print(f"In {room}: Current temperature = {info['current_temp']}°C - Action = {info['action']}")


agent = MultiReflexAgent(22)


rooms = {
    "Living Room": 28,
    "Bedroom": 20,
    "Kitchen": 35,
}

for room, temperature in rooms.items():
    agent.percept(room, temperature)
    action = agent.act()  
    print(f"Current temperature in {room} is {temperature}°C: {action}")  

agent.report()  
