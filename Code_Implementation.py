# Here's the updated version of the code for 4 professors

from pulp import *
import time
import numpy as np
import pandas as pd

model = LpProblem("Student_Visit_Scheduling", LpMinimize)
model.constraints.clear()
for var in model.variables():
    var.setInitialValue(0)

Nx, Ny, Nz = 2, 3, 2        # numbers of undergrad, master’s, PhD students
Tx, Ty, Tz = 3, 2, 1        # required visits per student per professor
Bx, By, Bz = 1, 2, 3        # minimum day‐gaps between visits
Rx, Ry, Rz = 1, 2, 3        # consecutive slots per visit
N = 7  #number of students
D = 7   #number of days
P = 6   #number of intervals per day
L = 1   #emergency time intervals in a day
Mx, My, Mz = 1, 2, 3
Q = 4              # Update for 4 professors
professors = range(Q)
F = np.ones((Q, D, P), dtype=int)  # Availability of each professor

p_x = [[0], [1]]
p_y = [[1], [2], [3]]
p_z = [[2], [0, 3]]

X = LpVariable.dicts("X", ((i, j, k, p) for i in range(Nx) for j in range(D) for k in range(P) for p in p_x[i]), cat='Binary')
Y = LpVariable.dicts("Y", ((i, j, k, p) for i in range(Ny) for j in range(D) for k in range(P) for p in p_y[i]), cat='Binary')
Z = LpVariable.dicts("Z", ((i, j, k, p) for i in range(Nz) for j in range(D) for k in range(P) for p in p_z[i]), cat='Binary')
E = LpVariable.dicts("E", ((j, k, p) for j in range(D) for k in range(P) for p in professors), cat='Binary')

W_x = LpVariable.dicts('W_x', (range(Nx), range(D), professors), cat='Binary')
W_y = LpVariable.dicts('W_y', (range(Ny), range(D), professors), cat='Binary')
W_z = LpVariable.dicts('W_z', (range(Nz), range(D), professors), cat='Binary')

model += (
    2 * (
        lpSum(Mx*(j*P + k + 1) * X[i,j,k,p] for i in range(Nx) for j in range(D) for k in range(P) for p in p_x[i]) +
        lpSum(My*(j*P + k + 1) * Y[i,j,k,p] for i in range(Ny) for j in range(D) for k in range(P) for p in p_y[i]) +
        lpSum(Mz*(j*P + k + 1) * Z[i,j,k,p] for i in range(Nz) for j in range(D) for k in range(P) for p in p_z[i])
    )
    + lpSum((j*P + k + 1) * E[j,k,p] for j in range(D) for k in range(P) for p in professors)
), 'Objective'

for j in range(D):
    for p in professors:
        model += lpSum(E[j, k, p] for k in range(P)) == L, f"emergency_slots_p{p}_d{j}"

for p in professors:
    for j in range(D):
        for k in range(P):
            model += (
                lpSum(X[i,j,k,p] for i in range(Nx) if p in p_x[i]) +
                lpSum(Y[i,j,k,p] for i in range(Ny) if p in p_y[i]) +
                lpSum(Z[i,j,k,p] for i in range(Nz) if p in p_z[i]) +
                E[j,k,p]
                <= F[p, j, k]
            ), f'prof_avail_{p}_{j}_{k}'

for i in range(Nx):
    for p in p_x[i]:
        for j in range(D):
            model += lpSum(X[i,j,k,p] for k in range(P)) == Rx * W_x[i][j][p], f"ug_time_{i}_{j}_{p}"
            for k in range(P):
                for h in range(k + Rx, P):
                    model += X[i,j,k,p] + X[i,j,h,p] <= 1, f"ug_consec_{i}_{j}_{k}_{h}_{p}"
        model += lpSum(X[i,j,k,p] for j in range(D) for k in range(P)) == Rx * Tx, f"ug_total_{i}_{p}"
        for t in range(D - Bx):
            model += lpSum(X[i,j,k,p] for j in range(t, t + Bx) for k in range(P)) <= Rx, f"ug_gap_{i}_{t}_{p}"

for i in range(Ny):
    for p in p_y[i]:
        for j in range(D):
            model += lpSum(Y[i,j,k,p] for k in range(P)) == Ry * W_y[i][j][p], f"ms_time_{i}_{j}_{p}"
            for k in range(P):
                for h in range(k + Ry, P):
                    model += Y[i,j,k,p] + Y[i,j,h,p] <= 1, f"ms_consec_{i}_{j}_{k}_{h}_{p}"
        model += lpSum(Y[i,j,k,p] for j in range(D) for k in range(P)) == Ry * Ty, f"ms_total_{i}_{p}"
        for t in range(D - By):
            model += lpSum(Y[i,j,k,p] for j in range(t, t + By) for k in range(P)) <= Ry, f"ms_gap_{i}_{t}_{p}"

for i in range(Nz):
    for p in p_z[i]:
        for j in range(D):
            model += lpSum(Z[i,j,k,p] for k in range(P)) == Rz * W_z[i][j][p], f"phd_time_{i}_{j}_{p}"
            for k in range(P):
                for h in range(k + Rz, P):
                    model += Z[i,j,k,p] + Z[i,j,h,p] <= 1, f"phd_consec_{i}_{j}_{k}_{h}_{p}"
        model += lpSum(Z[i,j,k,p] for j in range(D) for k in range(P)) == Rz * Tz, f"phd_total_{i}_{p}"
        for t in range(D - Bz):
            model += lpSum(Z[i,j,k,p] for j in range(t, t + Bz) for k in range(P)) <= Rz, f"phd_gap_{i}_{t}_{p}"

model.solve()

print("\n--- Summary ---")
print("status:", LpStatus[model.status])
print("Number of constraints:", len(model.constraints))
print("Number of variables:", len(model.variables()))
print("Objective value:", value(model.objective))

for v in model.variables():
    if v.varValue == 1:
        print(v.name, "=", v.varValue)

# --- build Table 6 ---
day_names = ['Monday','Tuesday','Wednesday','Thursday','Friday','Monday','Tuesday']
schedule = []
for p in professors:
    print(f"\n--- Schedule for Professor {p+1} ---")
    schedule = []
    for j in range(D):
        row = []
        for k in range(P):
            if E[j,k,p].value() > 0.5:
                row.append('E'); continue
            placed = False
            for i in range(Nx):
                if p in p_x[i] and X[i,j,k,p].value() > 0.5:
                    row.append(f'U{i+1}'); placed=True; break
            if placed: continue
            for i in range(Ny):
                if p in p_y[i] and Y[i,j,k,p].value() > 0.5:
                    row.append(f'M{i+1}'); placed=True; break
            if placed: continue
            for i in range(Nz):
                if p in p_z[i] and Z[i,j,k,p].value() > 0.5:
                    row.append(f'P{i+1}'); placed=True; break
            if not placed:
                row.append('')
        schedule.append(row)

    df = pd.DataFrame(schedule, index=day_names[:D], columns=[str(c+1) for c in range(P)])
    print(df.to_markdown())
