"""
Experiment 10: Unification in First Order Logic
Objective: Implement the Unification algorithm for logic expressions.
"""

def is_variable(exp):
    """
    Checks if the expression is a variable.
    Variables are represented as single lowercase strings.
    """
    return isinstance(exp, str) and exp.islower() and len(exp) == 1

def unify_var(var, x, theta):
    """
    Unifies a variable with an expression.
    """
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        # Create a new substitution
        theta[var] = x
        return theta

def unify(x, y, theta):
    """
    The main unification algorithm.
    x and y can be variables, constants, or lists (representing functions/predicates).
    """
    if theta is None:
        return None
    elif x == y:
        return theta
    elif is_variable(x):
        return unify_var(x, y, theta)
    elif is_variable(y):
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return None
        if len(x) == 0:
            return theta
        # Recursively unify the first elements, then the rest
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None

if __name__ == "__main__":
    # Variables are single lowercase letters (e.g., 'x', 'y', 'z', 'u')
    # Constants/Predicates/Functions are strings of length > 1 or uppercase
    
    # Expression 1: P(a, X, f(g(Y))) -> ['P', 'A', 'x', ['f', ['g', 'y']]]
    expr1 = ['P', 'A', 'x', ['f', ['g', 'y']]]
    
    # Expression 2: P(Z, f(Z), f(U)) -> ['P', 'z', ['f', 'z'], ['f', 'u']]
    expr2 = ['P', 'z', ['f', 'z'], ['f', 'u']]
    
    print("--- Unification Algorithm ---")
    print(f"Expression 1: {expr1}")
    print(f"Expression 2: {expr2}")
    
    # Empty dictionary for initial substitutions
    theta = unify(expr1, expr2, {})
    
    if theta is None:
        print("\nResult: Unification Failed")
    else:
        print("\nResult: Unification Successful")
        print("Substitution Set (Theta):")
        for var, sub in theta.items():
            print(f"  {var} / {sub}")
