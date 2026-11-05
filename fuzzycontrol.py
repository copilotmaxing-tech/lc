import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl




# 1. Define input and output variables


traffic_density = ctrl.Antecedent(
   np.arange(0, 51, 1), 'traffic_density'
)


waiting_time = ctrl.Antecedent(
   np.arange(0, 121, 1), 'waiting_time'
)


green_duration = ctrl.Consequent(
   np.arange(10, 91, 1), 'green_duration'
)




# 2. Define membership functions for traffic density


traffic_density['low'] = fuzz.trapmf(
   traffic_density.universe, [0, 0, 8, 15]
)


traffic_density['medium'] = fuzz.trimf(
   traffic_density.universe, [10, 20, 30]
)


traffic_density['high'] = fuzz.trapmf(
   traffic_density.universe, [25, 35, 50, 50]
)




# 3. Define membership functions for waiting time


waiting_time['short'] = fuzz.trapmf(
   waiting_time.universe, [0, 0, 15, 30]
)


waiting_time['moderate'] = fuzz.trimf(
   waiting_time.universe, [20, 50, 80]
)


waiting_time['long'] = fuzz.trapmf(
   waiting_time.universe, [70, 90, 120, 120]
)




# 4. Define membership functions for green-light duration


green_duration['short'] = fuzz.trapmf(
   green_duration.universe, [10, 10, 20, 30]
)


green_duration['medium'] = fuzz.trimf(
   green_duration.universe, [30, 45, 60]
)


green_duration['long'] = fuzz.trapmf(
   green_duration.universe, [60, 75, 90, 90]
)




# 5. Define fuzzy rules


rule1 = ctrl.Rule(
   traffic_density['low'] & waiting_time['short'],
   green_duration['short']
)


rule2 = ctrl.Rule(
   traffic_density['low'] & waiting_time['moderate'],
   green_duration['medium']
)


rule3 = ctrl.Rule(
   traffic_density['low'] & waiting_time['long'],
   green_duration['medium']
)


rule4 = ctrl.Rule(
   traffic_density['medium'] & waiting_time['short'],
   green_duration['medium']
)


rule5 = ctrl.Rule(
   traffic_density['medium'] & waiting_time['moderate'],
   green_duration['medium']
)


rule6 = ctrl.Rule(
   traffic_density['medium'] & waiting_time['long'],
   green_duration['long']
)


rule7 = ctrl.Rule(
   traffic_density['high'] & waiting_time['short'],
   green_duration['medium']
)


rule8 = ctrl.Rule(
   traffic_density['high'] & waiting_time['moderate'],
   green_duration['long']
)


rule9 = ctrl.Rule(
   traffic_density['high'] & waiting_time['long'],
   green_duration['long']
)




# 6. Create the fuzzy control system


traffic_control = ctrl.ControlSystem([
   rule1, rule2, rule3,
   rule4, rule5, rule6,
   rule7, rule8, rule9
])




# 7. Test the controller with different input conditions


test_cases = [
   ("Low density + Short waiting", 8, 15),
   ("Medium density + Moderate waiting", 20, 50),
   ("High density + Long waiting", 42, 100)
]


first_simulation = None


print("FUZZY LOGIC TRAFFIC LIGHT CONTROLLER")
print("------------------------------------")


for description, density, waiting in test_cases:


   simulation = ctrl.ControlSystemSimulation(
       traffic_control
   )


   simulation.input['traffic_density'] = density
   simulation.input['waiting_time'] = waiting


   simulation.compute()


   duration = simulation.output['green_duration']


   print("\nCondition:", description)
   print("Traffic density:", density, "vehicles/min")
   print("Waiting time:", waiting, "seconds")
   print("Green light duration:", round(duration, 2), "seconds")


   if first_simulation is None:
       first_simulation = simulation




# 8. Plot membership functions


traffic_density.view()
waiting_time.view()
green_duration.view()


# Display the fuzzy output for the first test case
green_duration.view(sim=first_simulation)




# 9. Generate data for the control surface


density_values = np.arange(0, 51, 2)
waiting_values = np.arange(0, 121, 5)


D, W = np.meshgrid(
   density_values,
   waiting_values
)


Z = np.zeros_like(D, dtype=float)


surface_simulation = ctrl.ControlSystemSimulation(
   traffic_control,
   cache=False
)


for i in range(D.shape[0]):
   for j in range(D.shape[1]):


       surface_simulation.input['traffic_density'] = float(D[i, j])
       surface_simulation.input['waiting_time'] = float(W[i, j])


       surface_simulation.compute()


       Z[i, j] = surface_simulation.output['green_duration']




# 10. Plot the control surface


fig = plt.figure(figsize=(10, 7))


ax = fig.add_subplot(111, projection='3d')


ax.plot_surface(
   D, W, Z,
   cmap='viridis',
   edgecolor='none'
)


ax.set_xlabel('Traffic Density (vehicles/min)')
ax.set_ylabel('Waiting Time (seconds)')
ax.set_zlabel('Green Duration (seconds)')


ax.set_title('Fuzzy Logic Traffic Light Control Surface')
plt.tight_layout()
plt.show()
