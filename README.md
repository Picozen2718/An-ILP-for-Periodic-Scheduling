# An-ILP-for-Periodic-Scheduling
The is the code implementation for the semester project of Applied Optimization course credited as part of the undergrad curriculum at IISER Bhopal in 2025. We refer to the paper by Sina Moradi for the outline.

## Overview
This project focuses on the periodic scheduling of meetings between students and professors across different academic levels (Undergraduate, Master's, PhD). The aim is to minimize a cost function while satisfying various practical scheduling constraints such as:

- Minimum intervals between consecutive meetings.
- Varying time requirements for different student levels.
- Dedicated emergency slots for unplanned visits.

## Key Features
- **Multi-Provider Scheduling**: Our solution supports scheduling across multiple professors, each with their own availability.
- **Priority System**: The model introduces a priority system that ensures higher priority student categories (e.g., PhD students) are scheduled first.
- **Emergency Slots**: Dedicated time slots are reserved for unplanned meetings or urgent requests.
- **Flexibility**: The model can accommodate dynamic changes, such as last-minute scheduling conflicts, and ensure efficiency.

## Problem Statement
We address a scheduling problem where students must meet professors over a fixed number of days. The solution aims to minimize the scheduling cost while handling various practical constraints and ensuring fairness.

## Model Formulation
We model the scheduling problem by treating students as customers and professors as service providers. The framework includes:
- Students grouped by academic level (Undergrad, Master’s, PhD).
- Professors’ availability defined across multiple time slots.
- A cost function that minimizes the overall scheduling cost while prioritizing earlier appointments.

## Numerical Example
We provide a numerical example to illustrate how the model works with given parameters such as the number of students, professors, slots per day, and the number of required meetings for each student type.

## Conclusion
This project presents an innovative solution to a complex scheduling problem, offering a flexible and efficient approach to student-professor meeting allocation while accommodating real-world constraints like emergency slots and varying priorities.

## Code and Slides
The code for the project and slides for the presentation can be found in the repository.

- [Link to paper](https://arxiv.org/abs/2412.11941)
