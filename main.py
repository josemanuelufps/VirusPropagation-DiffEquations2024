import matplotlib.pyplot as plt
from logic import run_sir_simulation
from logic_rickettsiosis import run_rickettsiosis_simulation

def main_sir_model():
    """
    _summary_
    Runs the simulation with the data inside "logic.py"
    and only handles the plotting.
    """
    t, S, I, R = run_sir_simulation()
    
    # Plot the results
    plt.figure(figsize=(10,6))
    plt.plot(t, S, label="Susceptible", color="blue")
    plt.plot(t, I, label="Infected", color="red")
    plt.plot(t, R, label="Recovered", color="green")
    plt.xlabel("Time (days)")
    plt.ylabel("Population Fraction")
    plt.title("SIR Model - 'Corrupted Blood' Epidemic in WoW")
    plt.legend()
    plt.grid(True)
    #plt.show()
    
    
def main_rickettsiosis():
    """
    Runs the Rickettsiosis simulation and plots the results.
    """
    t, SH, IH, RH, SP, IP, SG, IG = run_rickettsiosis_simulation()
    
    # Plotting the results for each population
    plt.figure(num="rickettsiosis complete", figsize=(12, 8))
    
    # humans (Susceptible, Infected, Recovered)
    plt.plot(t, SH, label="Susceptible Humans", color="blue")
    plt.plot(t, IH, label="Infected Humans", color="red")
    plt.plot(t, RH, label="Recovered Humans", color="green")
    
    #dogs (Susceptible, Infected)
    plt.plot(t, SP, label="Susceptible Dogs", color="cyan")
    plt.plot(t, IP, label="Infected Dogs", color="orange")
    
    #ticks (Susceptible, Infected)
    plt.plot(t, SG, label="Susceptible Ticks", color="purple")
    plt.plot(t, IG, label="Infected Ticks", color="brown")
    
    #labels/text
    plt.xlabel("Time (days)")
    plt.ylabel("Population Fraction")
    plt.title("Rickettsiosis Model Simulation")
    
    plt.legend()
    plt.grid(True)
    
    #plt.show()
    
    
def plot_human_population():
    """
    Runs the simulation and plots the population dynamics of humans (Susceptible, Infected, Recovered).
    """
    t, SH, IH, RH, SP, IP, SG, IG = run_rickettsiosis_simulation()
    plt.figure(num="Humans", figsize=(8, 6))
    plt.plot(t, SH, label="Susceptible Humans", color="blue")
    plt.plot(t, IH, label="Infected Humans", color="red")
    plt.plot(t, RH, label="Recovered Humans", color="green")
    plt.xlabel("Time (days)")
    plt.ylabel("Population Fraction")
    plt.title("Human Population Dynamics")
    plt.legend()
    plt.grid(True)


def plot_dog_population():
    """
    Again, Runs the simulation and plots the population dynamics, this time of dogs (Susceptible, Infected).
    """
    t, SH, IH, RH, SP, IP, SG, IG = run_rickettsiosis_simulation()
    plt.figure(num="Dogs", figsize=(8, 6))
    plt.plot(t, SP, label="Susceptible Dogs", color="cyan")
    plt.plot(t, IP, label="Infected Dogs", color="orange")
    plt.xlabel("Time (days)")
    plt.ylabel("Population Fraction")
    plt.title("Dog Population Dynamics")
    plt.legend()
    plt.grid(True)


def plot_tick_population():
    """
    The same, but this time with ticks (Susceptible, Infected).
    """
    t, SH, IH, RH, SP, IP, SG, IG = run_rickettsiosis_simulation()
    plt.figure(num="Ticks", figsize=(8, 6))
    plt.plot(t, SG, label="Susceptible Ticks", color="purple")
    plt.plot(t, IG, label="Infected Ticks", color="brown")
    plt.xlabel("Time (days)")
    plt.ylabel("Population Fraction")
    plt.title("Tick Population Dynamics")
    plt.legend()
    plt.grid(True)
    

if __name__ == "__main__":
    main_rickettsiosis()
    plot_human_population()
    plot_dog_population()
    plot_tick_population()
    plt.show()

