"""
Experiment 11: Knowledge Base System (Expert System)
Objective: Implement a rule-based expert system using forward chaining.
"""

class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = set()

    def add_rule(self, conditions, conclusion):
        """
        Adds a rule to the knowledge base.
        conditions: A list of strings representing facts that must be true.
        conclusion: A string representing the inferred fact.
        """
        self.rules.append((conditions, conclusion))

    def add_fact(self, fact):
        """
        Adds a known fact to the knowledge base.
        """
        self.facts.add(fact)

    def infer(self):
        """
        Runs the forward chaining inference engine to deduce new facts.
        """
        new_facts_inferred = True
        iteration = 1
        
        while new_facts_inferred:
            new_facts_inferred = False
            print(f"\n--- Inference Iteration {iteration} ---")
            
            for conditions, conclusion in self.rules:
                # If all conditions are present in the current facts, and the conclusion is not
                if all(c in self.facts for c in conditions) and conclusion not in self.facts:
                    print(f"Rule Matched: IF {conditions} THEN {conclusion}")
                    self.facts.add(conclusion)
                    new_facts_inferred = True
                    print(f"-> Inferred new fact: '{conclusion}'")
            
            if not new_facts_inferred:
                print("No new facts inferred. Inference complete.")
            iteration += 1

if __name__ == "__main__":
    es = ExpertSystem()
    
    # Adding rules to the knowledge base
    es.add_rule(["has_feathers", "lays_eggs"], "is_bird")
    es.add_rule(["is_bird", "cannot_fly", "swims"], "is_penguin")
    es.add_rule(["is_bird", "can_fly"], "is_sparrow")
    es.add_rule(["has_hair", "gives_milk"], "is_mammal")
    
    # Adding initial known facts
    print("Initializing Knowledge Base...")
    es.add_fact("has_feathers")
    es.add_fact("lays_eggs")
    es.add_fact("cannot_fly")
    es.add_fact("swims")
    
    print("\nInitial Facts:", es.facts)
    
    # Run the inference engine
    es.infer()
    
    print("\nFinal Knowledge Base Facts:")
    for f in sorted(es.facts):
        print(f"- {f}")
