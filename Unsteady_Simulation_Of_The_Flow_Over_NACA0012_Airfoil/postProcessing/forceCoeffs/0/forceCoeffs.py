import matplotlib.pyplot as plt
import numpy as np

# File name (replace with your file path)
filename = "forceCoeffs.dat"

# Initialize lists for time and coefficients
time = []
Cm = []
Cd = []
Cl = []
#Cl_f = []
#Cl_r = []

# Read the file and extract data
with open(filename, 'r') as file:
    for line in file:
        # Skip comment lines
        if line.startswith('#') or not line.strip():
            continue
        # Split the line into columns
        data = line.split()
        # Append values to respective lists
        time.append(float(data[0]))
        Cm.append(float(data[1]))
        Cd.append(float(data[2]))
        Cl.append(float(data[3]))
        #Cl_f.append(float(data[4]))
        #Cl_r.append(float(data[5]))

# Convert lists to numpy arrays
time = np.array(time)
Cm = np.array(Cm)
Cd = np.array(Cd)
Cl = np.array(Cl)
#Cl_f = np.array(Cl_f)
#Cl_r = np.array(Cl_r)

# Plot Cm (Moment Coefficient)
plt.figure(figsize=(8, 5))
plt.plot(time, Cm, label="Cm (Moment Coefficient)", color="blue")
plt.title("Moment Coefficient (Cm) vs Time")
plt.xlabel("Time")
plt.ylabel("Cm")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot Cd (Drag Coefficient)
#plt.figure(figsize=(8, 5))
#plt.plot(time, Cd, label="Cd (Drag Coefficient)", color="red")
#plt.title("Drag Coefficient (Cd) vs Time")
#plt.xlabel("Time")
#plt.ylabel("Cd")
#plt.grid(True)
#plt.legend()
#plt.tight_layout()
#plt.show()

# Plot Cd (Drag Coefficient)
# To get rid of the out layers
time_limit = 0.01  # Exclude time values beyond this point
subset_time = [t for t in time if t > time_limit]
subset_Cd = [cd for t, cd in zip(time, Cd) if t > time_limit]

plt.figure(figsize=(8, 5))
plt.plot(subset_time, subset_Cd, label="Cd (Drag Coefficient)", color="red")
plt.title("Drag Coefficient (Cd) vs Time (Filtered Range)")
plt.xlabel("Time")
plt.ylabel("Cd")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# Plot Cl (Lift Coefficient)
plt.figure(figsize=(8, 5))
plt.plot(time, Cl, label="Cl (Lift Coefficient)", color="green")
plt.title("Lift Coefficient (Cl) vs Time")
plt.xlabel("Time")
plt.ylabel("Cl")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
