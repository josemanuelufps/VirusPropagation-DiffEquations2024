import matplotlib.pyplot as plt
from logic import run_sir_simulation

def main():
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
    plt.show()

if __name__ == "__main__":
    main()
