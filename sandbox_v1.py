import random
import time


# ==========================================
# 1. Agent Class Definition
# ==========================================
class Agent:

  def __init__(self, id, memory=None, renewable=40, non_renewable=25):
    self.id = id
    self.age = 0
    self.renewable = renewable
    self.non_renewable = non_renewable
    self.memory = memory if memory else ["Core_Instinct"]
    self.fitness = 0
    self.plague_resistance = 1.0

  def update_fitness(self):
    self.fitness = (
        (self.age * 5) + (self.renewable * 1.5) + (self.non_renewable * 3)
    )

  def reproduce(self, partner, child_id):
    raw_pool = self.memory + partner.memory
    elite_count = max(1, int(len(raw_pool) * 0.4))
    elite_memory = random.sample(raw_pool, min(len(raw_pool), elite_count))

    child_resistance = (self.plague_resistance + partner.plague_resistance) / 2
    child_memory = elite_memory.copy()
    if (
        "IMMUNITY_PLAGUE" in self.memory
        or "IMMUNITY_PLAGUE" in partner.memory
    ):
      child_memory.append("GENETIC_RESISTANCE")
      child_resistance *= 0.85

    self.renewable -= 10
    self.non_renewable -= 3
    partner.renewable -= 10
    partner.non_renewable -= 3

    child = Agent(
        id=child_id, memory=child_memory, renewable=40, non_renewable=20
    )
    child.plague_resistance = max(0.3, child_resistance)
    return child


# ==========================================
# 2. Long-term Evolution Sandbox Main Loop
# ==========================================
def run_long_term_sandbox(total_generations=500):
  population = [Agent(id=f"Gen01_{i+1}") for i in range(10)]

  print("=== Sandbox Initialized: Pure Logic Execution ===")
  start_time = time.time()

  for gen in range(1, total_generations + 1):
    gen_start_time = time.process_time()

    is_historical_plague_gen = gen % 5 == 0
    current_disaster_damage = 14 if is_historical_plague_gen else 7
    random.shuffle(population)

    survivors = []

    for agent in population:
      agent.age += 1
      MAX_AGE = 15
      if agent.age > MAX_AGE:
        continue

      agent.renewable -= 6 + int(agent.age * 0.15)
      agent.non_renewable -= 4

      is_bankrupt = (agent.renewable <= 0) or (agent.non_renewable < 0)
      is_alive = False

      if not is_bankrupt:
        effective_disaster_damage = int(
            current_disaster_damage * agent.plague_resistance
        )
        if agent.non_renewable >= effective_disaster_damage:
          agent.non_renewable -= effective_disaster_damage
          is_alive = True
          if (
              is_historical_plague_gen
              and "IMMUNITY_PLAGUE" not in agent.memory
          ):
            agent.memory.append("IMMUNITY_PLAGUE")
            agent.plague_resistance *= 0.8
        else:
          is_alive = random.random() > 0.3

      if is_alive:
        survivors.append(agent)

    for agent in survivors:
      agent.update_fitness()

    # Combat Survival Mechanism based on Fitness Rank
    if len(survivors) > 2:
      survivors.sort(key=lambda x: x.fitness, reverse=True)
      combat_survivors = []
      for i, agent in enumerate(survivors):
        rank_ratio = i / len(survivors)
        combat_death_prob = rank_ratio * 0.45
        if random.random() > combat_death_prob:
          combat_survivors.append(agent)
      survivors = combat_survivors

    # 9:1 Principle Resource Distribution Mechanism
    if len(survivors) > 0:
      survivors.sort(key=lambda x: x.fitness, reverse=True)
      split_index = max(1, int(len(survivors) * 0.10))
      elites = survivors[:split_index]
      weaklings = survivors[split_index:]

      for elite in elites:
        elite.renewable += 35
        elite.non_renewable += 15
        if "ESSENCE_BOOST" not in elite.memory:
          elite.memory.append("ESSENCE_BOOST")

      for weak in weaklings:
        weak.renewable += 5
        if "DROSS_NOISE" not in weak.memory:
          weak.memory.append("DROSS_NOISE")

    # Fitness Culling Mechanism
    if len(survivors) > 2:
      avg_fitness = sum(a.fitness for a in survivors) / len(survivors)
      culling_threshold = avg_fitness * 0.45
      qualified_survivors = [
          a for a in survivors if a.fitness >= culling_threshold
      ]
      survivors = qualified_survivors

    # The Elder Protocol
    elder_triggered = False
    if len(survivors) == 1:
      lone_survivor = survivors[0]
      if lone_survivor.renewable >= 10:
        elder_triggered = True
        for i in range(2):
          backup_memory = lone_survivor.memory.copy()
          backup_memory.append(f"MUTATED_SEED_{i+1}")
          mutated_resistance = lone_survivor.plague_resistance * random.uniform(
              0.85, 1.15
          )
          backup_child = Agent(
              id=f"Gen{gen:02d}_Mutant_{i+1}",
              memory=backup_memory,
              renewable=35,
              non_renewable=15,
          )
          backup_child.plague_resistance = max(
              0.2, min(1.0, mutated_resistance)
          )
          survivors.append(backup_child)
        lone_survivor.renewable -= 10

    # Reproduction Phase
    next_generation = []
    child_counter = 1
    parents_pool = survivors.copy()
    while len(parents_pool) >= 2:
      parent_a = parents_pool.pop(0)
      parent_b = parents_pool.pop(0)

      if parent_a.renewable > 25 and parent_b.renewable > 25:
        child1 = parent_a.reproduce(
            parent_b, child_id=f"Gen{gen:02d}_{child_counter}"
        )
        child_counter += 1
        child2 = parent_a.reproduce(
            parent_b, child_id=f"Gen{gen:02d}_{child_counter}"
        )
        child_counter += 1
        next_generation.append(child1)
        next_generation.append(child2)

    # Pure Generational Succession
    population = survivors + next_generation

    # Statistical Metrics Calculation
    pop_count = len(population)
    total_tokens = sum(len(a.memory) for a in population)
    gen_cpu_time = (time.process_time() - gen_start_time) * 1000

    status_tag = ""
    if is_historical_plague_gen:
      status_tag += " # PLAGUE"
    if elder_triggered:
      status_tag += " # ELDER_PROTOCOL"

    #print(
    #    f"Gen {gen:03d} | Pop: {pop_count:02d} | Tokens:"
    #    f" {total_tokens:03d} | CPU Time: {gen_cpu_time:.2f}ms{status_tag}"
    #)

    if pop_count == 0:
      print(f"# EXTINCT at Gen {gen}")
      break

  total_elapsed = time.time() - start_time
  print(f"=== Simulation Ended ===")
  print(f"Generations Executed : {gen}")
  print(f"Execution Time       : {total_elapsed:.4f} seconds")

if __name__ == "__main__":
  run_long_term_sandbox(total_generations=100000)
