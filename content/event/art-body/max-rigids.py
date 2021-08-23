import pygame as pg
import numpy as np
import random
import math
import sys

pg.init()

screen_width = 1080
screen_height = 640
screen = pg.display.set_mode([1080, 640])


n_rigid = 3
density = np.ones(n_rigid)
M = np.ones(n_rigid)
I = np.ones(n_rigid)
X = np.zeros([n_rigid, 2])
V = np.zeros([n_rigid, 2])
F = np.zeros([n_rigid, 2])
W = np.zeros(n_rigid)
angle = np.zeros(n_rigid)
tau = np.zeros(n_rigid)

rigid_shape = [[0.1, 0.3], [0.1, 0.1], [0.1, 0.2]]
rigid_type = [0, 1, 2] # 0=rect, 1=circle, 2=triangle

n_joint = 2
joint_pair = [[0, 1], [1, 2]]
joint_type = [1, 2] # 0=fixed 3, 1=revolute 2, 2=sphere 1
joint_cons_offset = [0, 2]
n_cons = 3
joint_rel_pos = [[[.0, -0.15],[.0, 0.1]], [[.0, -0.1],[.0, 0.4/3]]]
joint_param = [[], [0.1]]

J = np.zeros([n_cons, 3*n_rigid])

grav = np.array([0, -20.0])
dt = 1e-4
enable_force = False
force_center = np.zeros(2)
force_coef = 100

# helper functions
def rotation2d(_angle):
    c, s = math.cos(_angle), math.sin(_angle)
    return np.array([[c, -s],[s, c]])

def coord_to_pixel(pos):
    ratio = min(screen_width, screen_height)
    return (screen_width // 2 + int(pos[0]*ratio), screen_height // 2 - int(pos[1]*ratio))

def pixel_to_coord(pixel):
    ratio = min(screen_width, screen_height) 
    return np.array([(pixel[0] - screen_width // 2) / ratio, (screen_height // 2 - pixel[1]) / ratio])

def to_pixel(x):
    ratio = min(screen_width, screen_height)
    return ratio * x


# core function
def init(case=0):
    global n_rigid, rigid_shape, rigid_type, density, M, I, X, V, F, W, angle, tau
    global n_joint, joint_pair, joint_type, joint_cons_offset, n_cons,\
         joint_rel_pos, joint_param, J
    if case == 0:
        n_rigid = 3
        rigid_shape = [[0.1, 0.3], [0.1, 0.1], [0.1, 0.2]]
        rigid_type = [0, 1, 2]
        density = np.ones(n_rigid)
        M = np.ones(n_rigid)
        I = np.ones(n_rigid)
        X = np.zeros([n_rigid, 2])
        V = np.zeros([n_rigid, 2])
        F = np.zeros([n_rigid, 2])
        W = np.zeros(n_rigid)
        angle = np.zeros(n_rigid)
        tau = np.zeros(n_rigid)

        n_joint = 2
        joint_pair = [[0, 1], [1, 2]]
        joint_type = [1, 2]
        joint_cons_offset = [0, 2]
        n_cons = 3
        joint_rel_pos = [[[.0, -0.15],[.0, 0.1]], [[.0, -0.1],[.0, 0.4/3]]]
        joint_param = [[], [0.1]]

        X[0] = 0.4*np.array([random.random() - 0.5, random.random() - 0.5])
        angle[0] = math.pi * random.random()
        for i in range(n_joint):
            ra, rb = joint_pair[i]
            if joint_type[i] == 0:
                xa = X[ra] + rotation2d(angle[ra]) @ np.array(joint_rel_pos[i][0])
                angle[rb] = angle[ra]
                X[rb] = xa - rotation2d(angle[rb]) @ np.array(joint_rel_pos[i][1])
            elif joint_type[i] == 1:
                xa = X[ra] + rotation2d(angle[ra]) @ np.array(joint_rel_pos[i][0])
                angle[rb] = math.pi * random.random()
                X[rb] = xa - rotation2d(angle[rb]) @ np.array(joint_rel_pos[i][1])
            elif joint_type[i] == 2:
                xa = X[ra] + rotation2d(angle[ra]) @ np.array(joint_rel_pos[i][0])
                angle[rb] = angle[ra]
                X[rb] = xa - rotation2d(angle[rb]) @ np.array(joint_rel_pos[i][1])
    if case == 1:
        n_rigid = 3
        rigid_shape = [[0.1, 0.3], [0.1, 0.1], [0.1, 0.2]]
        rigid_type = [0, 1, 2]
        density = np.ones(n_rigid)
        M = np.ones(n_rigid)
        I = np.ones(n_rigid)
        X = np.zeros([n_rigid, 2])
        V = np.zeros([n_rigid, 2])
        F = np.zeros([n_rigid, 2])
        W = np.zeros(n_rigid)
        angle = np.zeros(n_rigid)
        tau = np.zeros(n_rigid)

        n_joint = 2
        joint_pair = [[0, 1], [1, 2]]
        joint_type = [1, 0]
        joint_cons_offset = [0, 2]
        n_cons = 5
        joint_rel_pos = [[[.0, -0.15],[.0, 0.1]], [[.0, -0.1],[.0, 0.4/3]]]
        joint_param = [[], []]

        X[0] = 0.4*np.array([random.random() - 0.5, random.random() - 0.5])
        angle[0] = math.pi * random.random()
        for i in range(n_joint):
            ra, rb = joint_pair[i]
            if joint_type[i] == 0:
                xa = X[ra] + rotation2d(angle[ra]) @ np.array(joint_rel_pos[i][0])
                angle[rb] = angle[ra]
                X[rb] = xa - rotation2d(angle[rb]) @ np.array(joint_rel_pos[i][1])
            elif joint_type[i] == 1:
                xa = X[ra] + rotation2d(angle[ra]) @ np.array(joint_rel_pos[i][0])
                angle[rb] = math.pi * random.random()
                X[rb] = xa - rotation2d(angle[rb]) @ np.array(joint_rel_pos[i][1])
            elif joint_type[i] == 2:
                xa = X[ra] + rotation2d(angle[ra]) @ np.array(joint_rel_pos[i][0])
                angle[rb] = angle[ra]
                X[rb] = xa - rotation2d(angle[rb]) @ np.array(joint_rel_pos[i][1])
    if case == 2:
        n_rigid = 4
        rigid_shape = [[0.05, 0.3], [0.05, 0.3], [0.05, 0.3], [0.05, 0.3]]
        rigid_type = [0, 2, 0, 2]
        density = np.ones(n_rigid)
        M = np.ones(n_rigid)
        I = np.ones(n_rigid)
        X = np.zeros([n_rigid, 2])
        V = np.zeros([n_rigid, 2])
        F = np.zeros([n_rigid, 2])
        W = np.zeros(n_rigid)
        angle = np.zeros(n_rigid)
        tau = np.zeros(n_rigid)

        n_joint = 4
        joint_pair = [[0, 1], [1, 2], [2, 3], [3, 0]]
        joint_type = [1, 1, 1, 1]
        joint_cons_offset = [0, 2, 4, 6]
        n_cons = 8
        joint_rel_pos = [[[.0, -0.15],[.0, 0.2]], [[.0, -0.1],[.0, 0.15]], [[.0, -0.15],[.0, 0.2]], [[.0, -0.1],[.0, 0.15]]]
        joint_param = [[], [], [], []]

        theta = 0.2
        X[0] = rotation2d(theta) @ [-0.15, 0]
        angle[0] = theta
        X[1] = rotation2d(theta) @ [0.05, -0.15]
        angle[1] = theta + math.pi / 2
        X[2] = rotation2d(theta) @ [0.15, 0]
        angle[2] = theta + math.pi
        X[3] = rotation2d(theta) @ [-0.05, 0.15]
        angle[3] = theta + 3 * math.pi / 2
    
    for i in range(n_rigid):
        if rigid_type[i] == 0:
            a, b = rigid_shape[i][0], rigid_shape[i][1]
            M[i] = density[i] * a * b
            I[i] = 1 / 12 * M[i] * (a**2 + b**2)
        elif rigid_type[i] == 1:
            r = rigid_shape[i][0]
            M[i] = density[i] * math.pi * (r**2)
            I[i] = 1 / 2 * M[i] * (r**2)
        elif rigid_type[i] == 2:
            l, h = rigid_shape[i][0], rigid_shape[i][1]
            M[i] = density[i] * l * h / 2
            I[i] = 1 / 24 * M[i] * (l**2) + 1 / 18 * M[i] * (h**2)
    J = np.zeros([n_cons, 3*n_rigid])

def apply_force(f, pos, i):
    F[i] += f
    dr = pos - X[i]
    tau[i] += dr[0]*f[1] - dr[1]*f[0]


def soft_boundary_collision():
    coef = 1e4
    beta = 1e1
    for i in range(n_rigid):
        if rigid_type[i] == 0: # rect
            for dir in [[-1, -1], [1, -1], [-1, 1], [1, 1]]:
                dr = 0.5 * rotation2d(angle[i]) @ np.array([dir[0] * rigid_shape[i][0], dir[1] * rigid_shape[i][1]])
                corner = X[i] + dr
                vel_corner = V[i] + W[i] * np.array([-dr[1], dr[0]])
                if corner[0] < -0.5:
                    apply_force([coef * (-0.5 - corner[0]) - beta * vel_corner[0], 0], corner, i)
                if corner[0] > 0.5:
                    apply_force([coef * (0.5 - corner[0]) - beta * vel_corner[0], 0], corner, i)
                if corner[1] < -0.5:
                    apply_force([0, coef * (-0.5 - corner[1]) - beta * vel_corner[1]], corner, i)
                if corner[1] > 0.5:
                    apply_force([0, coef * (0.5 - corner[1]) - beta * vel_corner[1]], corner, i)
        if rigid_type[i] == 1:
            r = rigid_shape[i][0]
            if X[i][0] + 0.5 < r:
                apply_force( [coef * (-0.5 + r - X[i][0]) - beta * V[i][0], 0], X[i], i)
            if 0.5 - X[i][0] < r:
                apply_force([coef * (0.5 - X[i][0] - r) - beta * V[i][0], 0], X[i], i)
            if X[i][1] + 0.5 < r:
                apply_force([0, coef * (-0.5 + r - X[i][1]) - beta * V[i][1]], X[i], i)
            if 0.5 - X[i][1] < r:
                apply_force([0, coef * (0.5 - X[i][1] - r) - beta * V[i][1]], X[i], i)
        if rigid_type[i] == 2:
            dh = 1 / 3 * rotation2d(angle[i]) @ np.array([0, rigid_shape[i][1]])
            dl = 0.5 * rotation2d(angle[i]) @ np.array([rigid_shape[i][0], 0])
            corners = [X[i] + 2 * dh, X[i] - dh - dl, X[i] - dh + dl]
            vel_corners = [V[i] + W[i] * 2 * np.array([-dh[1], dh[0]]), \
                V[i] + W[i] * np.array([dh[1]+dl[1], -dh[0]-dl[0]]), V[i] + W[i] * np.array([dh[1]-dl[1], -dh[0]+dl[0]])]
            for c in range(3):
                corner = corners[c]
                vel_corner = vel_corners[c]
                if corner[0] < -0.5:
                    apply_force([coef * (-0.5 - corner[0]) - beta * vel_corner[0], 0], corner, i)
                if corner[0] > 0.5:
                    apply_force([coef * (0.5 - corner[0]) - beta * vel_corner[0], 0], corner, i)
                if corner[1] < -0.5:
                    apply_force([0, coef * (-0.5 - corner[1]) - beta * vel_corner[1]], corner, i)
                if corner[1] > 0.5:
                    apply_force([0, coef * (0.5 - corner[1]) - beta * vel_corner[1]], corner, i)

def compute_jacobian():
    global J
    J = np.zeros([n_cons, 3*n_rigid])
    for i in range(n_joint):
        ra, rb = joint_pair[i]
        offset = joint_cons_offset[i]
        if joint_type[i] == 0: # fixed
            J[offset:offset+2, 3*ra:3*ra+2] = np.eye(2)
            J[offset:offset+2, 3*ra+2] = rotation2d(math.pi / 2 + angle[ra]) @ joint_rel_pos[i][0]
            J[offset:offset+2, 3*rb:3*rb+2] = -np.eye(2)
            J[offset:offset+2, 3*rb+2] = - rotation2d(math.pi / 2 + angle[rb]) @ joint_rel_pos[i][1]
            J[offset+2, 3*ra+2] = 1
            J[offset+2, 3*rb+2] = -1
        elif joint_type[i] == 1: # revolute
            J[offset:offset+2, 3*ra:3*ra+2] = np.eye(2)
            J[offset:offset+2, 3*ra+2] = rotation2d(math.pi / 2 + angle[ra]) @ joint_rel_pos[i][0]
            J[offset:offset+2, 3*rb:3*rb+2] = -np.eye(2)
            J[offset:offset+2, 3*rb+2] = - rotation2d(math.pi / 2 + angle[rb]) @ joint_rel_pos[i][1]
        elif joint_type[i] == 2: # sphere
            n = X[rb] + rotation2d(angle[rb]) @ joint_rel_pos[i][1] - X[ra]
            J[offset, 3*ra:3*ra+2] = - n.transpose()
            J[offset, 3*rb:3*rb+2] = n.transpose()
            J[offset, 3*rb+2] = (rotation2d(math.pi / 2 + angle[rb]) @ joint_rel_pos[i][1]).dot(n)
    return

def advance():
    global F, tau
    F = np.zeros([n_rigid, 2])
    tau = np.zeros(n_rigid)
    soft_boundary_collision()
    compute_jacobian()
    Mt_inv = np.zeros([3*n_rigid, 3*n_rigid])
    Ft = np.zeros(3*n_rigid)
    Vt = np.zeros(3*n_rigid)
    for i in range(n_rigid):
        Mt_inv[3*i:3*i+2, 3*i:3*i+2] = 1 / M[i] * np.eye(2)
        Mt_inv[3*i+2, 3*i+2] = 1 / I[i]
        Ft[3*i:3*i+2] = F[i] + (grav + enable_force * force_coef * (force_center - X[i])) * M[i]
        Ft[3*i+2] = tau[i]
        Vt[3*i:3*i+2] = V[i]
        Vt[3*i+2] = W[i]
    LHS = J @ Mt_inv @ J.transpose()
    RHS = - dt * J @ Mt_inv @ Ft - J @ Vt
    lmbd = np.linalg.solve(LHS, RHS)
    Vt += dt * Mt_inv @ Ft + Mt_inv @ J.transpose() @ lmbd
    for i in range(n_rigid):
        V[i] = Vt[3*i:3*i+2]
        W[i] = Vt[3*i+2]
        X[i] +=  V[i] * dt
        angle[i] += W[i] * dt 

def draw():
    pg.draw.rect(screen, 0x458985, [coord_to_pixel([-0.5,0.5]), (to_pixel(1), to_pixel(1))], 2)
    for i in range(n_rigid):
        if rigid_type[i] == 0:
            dtl = 0.5 * rotation2d(angle[i]) @ np.array([-rigid_shape[i][0], rigid_shape[i][1]])
            dtr = 0.5 * rotation2d(angle[i]) @ np.array(rigid_shape[i])
            pg.draw.polygon(screen, 0xDBA67B, \
                [coord_to_pixel(X[i] + dtl), coord_to_pixel(X[i] - dtr), coord_to_pixel(X[i] - dtl), coord_to_pixel(X[i] + dtr)])
        elif rigid_type[i] == 1:
            pg.draw.circle(screen, 0xDFDFC9, coord_to_pixel(X[i]), to_pixel(rigid_shape[i][0]))
        elif rigid_type[i] == 2:
            dh = 1 / 3 * rotation2d(angle[i]) @ np.array([0, rigid_shape[i][1]])
            dl = 0.5 * rotation2d(angle[i]) @ np.array([rigid_shape[i][0], 0])
            pg.draw.polygon(screen, 0xA55C55, \
                [coord_to_pixel(X[i] + 2 * dh), coord_to_pixel(X[i] - dh - dl), coord_to_pixel(X[i] - dh + dl)])
    for i in range(n_joint):
        for j in range(2):
            r = joint_pair[i][j]
            dr = rotation2d(angle[r]) @ np.array(joint_rel_pos[i][j])
            pg.draw.circle(screen, 0xEFFFFF, coord_to_pixel(X[r]+dr), 4)

# main loop
case = 0
if len(sys.argv) > 1:
    case = int(sys.argv[1])
print('case: ', case)
running = True
init(case)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEMOTION:
            mouse_pos = pg.mouse.get_pos()
            force_center = pixel_to_coord(mouse_pos)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                enable_force = not enable_force
    advance()
    screen.fill(0x063647)
    draw()
    pg.display.flip()
pg.quit()