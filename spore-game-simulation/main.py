from simulation import Simulation


def main() -> None:
    results = {"prey_escaped": 0, "prey_dead": 0, "predator_dead": 0}

    for i in range(1, 101):
        print(f"\n=== Simulation {i} ===")
        sim = Simulation(i)
        outcome = sim.run()
        results[outcome] += 1
        print(f"[SIMULATION {i} RESULT] {outcome}")
        print(f"Current totals: {results}")

    print("\n=== All simulations complete ===")
    print(results)


if __name__ == "__main__":
    main()
