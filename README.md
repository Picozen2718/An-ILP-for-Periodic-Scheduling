# An-ILP-for-Periodic-Scheduling
The is the code implementation for the semester project of Applied Optimization course credited as part of the undergrad curriculum at IISER Bhopal in 2025.

This project focuses on solving the problem of scheduling student-professor meetings in an academic environment, considering students of different academic levels (Undergraduate, Master's, and PhD) and the specific requirements they have for meetings. We aim to develop an optimization model that can handle scheduling while incorporating various constraints and practical elements, such as emergency slots, priority-based scheduling, and meeting duration flexibility.

Problem Statement:
The core challenge is to assign student visits to professors across a fixed number of days and time slots, while ensuring:

Minimum intervals between consecutive meetings,

Time requirements for different student categories,

Emergency slots for unplanned visits.

Our Contribution:
We introduce a novel approach that improves upon existing solutions by:

Refining the scheduling model with cleaner formulations and priority mechanisms for student categories,

Extending the model to multiple service providers (professors),

Modifying the objective function to prioritize earlier slots for efficiency,

Integrating flexibility for emergencies in the scheduling process.

Key Features:
Multi-Provider Environment: Our framework supports scheduling across multiple professors with shared responsibilities, ensuring fair and balanced meeting allocations.

Fairness & Operational Efficiency: The model reduces conflicts and maximizes time slot utilization, ensuring the smooth operation of scheduling.

Emergency Flexibility: Emergency slots are reserved for unplanned meetings, ensuring the system can accommodate last-minute requests without disrupting regular schedules.

Foundation for Intelligent Scheduling: This approach provides a foundation for future enhancements, such as machine learning integration for predictive scheduling.

The solution is demonstrated through the formulation of a mathematical model, constraints, and an objective function aimed at optimizing the scheduling process. The project also includes numerical examples to validate the model's applicability.

This repository contains the implementation of the model along with supporting slides that outline the approach, methodology, and results.
