import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create Bayesian Network
model = DiscreteBayesianNetwork([
    ("Rain", "Traffic"),
    ("Accident", "Traffic")
])

# Define Conditional Probability Distributions (CPDs)

# Rain: 0 = No, 1 = Yes
cpd_rain = TabularCPD(
    variable="Rain",
    variable_card=2,
    values=[[0.7], [0.3]]
)

# Accident: 0 = No, 1 = Yes
cpd_accident = TabularCPD(
    variable="Accident",
    variable_card=2,
    values=[[0.9], [0.1]]
)

# Traffic depends on Rain and Accident
# Traffic: 0 = Low, 1 = High
cpd_traffic = TabularCPD(
    variable="Traffic",
    variable_card=2,
    values=[
        [0.9, 0.6, 0.5, 0.1],
        [0.1, 0.4, 0.5, 0.9]
    ],
    evidence=["Rain", "Accident"],
    evidence_card=[2, 2]
)

# Add CPDs to the network
model.add_cpds(cpd_rain, cpd_accident, cpd_traffic)

# Check network validity
print("Bayesian Network Valid:", model.check_model())

# Display network structure
print("\nNetwork Structure:")
print(list(model.edges()))

# Perform probabilistic inference
inference = VariableElimination(model)

# Calculate probability of high traffic
result = inference.query(
    variables=["Traffic"],
    show_progress=False
)

print("\nProbability of Traffic:")
print(result)

# Calculate probability of rain given high traffic
result2 = inference.query(
    variables=["Rain"],
    evidence={"Traffic": 1},
    show_progress=False
)

print("\nProbability of Rain Given High Traffic:")
print(result2)

print("\nBayesian Network Execution Completed!")
