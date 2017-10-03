from __future__ import division

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mbuild import Box
import numpy as np

def visualize(compound, show_bonds=False, box=None, verbose=False):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if not box:
        boundingbox = compound.boundingbox
        longest_side = boundingbox.lengths.max()
        center = (boundingbox.maxs + boundingbox.mins) / 2
        mins = np.array([dim - longest_side/2 for dim in center])
        maxs = np.array([dim + longest_side/2 for dim in center])
        box = Box(mins=mins, maxs=maxs)
    ax.set_xlim([box.mins[0] - 0.125, box.maxs[0] + 0.125])
    ax.set_ylim([box.mins[1] - 0.125, box.maxs[1] + 0.125])
    ax.set_zlim([box.mins[2] - 0.125, box.maxs[2] + 0.125])
    volume = np.linalg.norm(box.lengths)

    colors = {'C': 'cyan', 'H': 'white', 'O': 'red', 'Si': 'yellow'}
    size = {'C': 1250/volume, 'H': 400/volume, 'O': 1300/volume,
            'Si': 2000/volume}

    n_particles = compound.n_particles
    for i, pos in enumerate(compound.xyz):
        if verbose:
            print('Rendering particle {} of {}'.format(i+1, n_particles))
        name = compound[i].name
        name = ''.join([j for j in name if not j.isdigit()])
        ax.scatter(pos[0], pos[1], pos[2], c=colors[name],
                   s=size[name], edgecolors='black')
    if show_bonds:
        for bond in compound.bonds():
            ax.plot(bond[0].pos, bond[1].pos, color='black', alpha=0.5)
    plt.show()
