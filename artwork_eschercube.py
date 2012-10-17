# coding: utf-8
"""

Cover Art for the Journal of Neurophysiology


"""

# modified version: test_cubsets.py
# Author: Paula Sanz Leon

# numeric
import numpy as np
# visualizers
from enthought.tvtk.api import tvtk
from enthought.mayavi.sources.vtk_data_source import VTKDataSource
from enthought.mayavi import mlab

#ours
import MotionClouds as mc

size = 2**4
size = 2**5
# size = 2**6
size=50

def source(dim, bwd):
    """
    Create motion cloud source
    """
    z = mc.envelope_gabor(fx, fy, ft, B_sf=bwd[0], B_V=bwd[1], B_theta=bwd[2])
    data = mc.rectif(mc.random_cloud(z))
    return data


#def random_source(dim):
#    """
#    Create random data 
#    """
#    #data = random.random(dim                                                                                                               )
#    fx, fy, ft = np.mgrid[0:1:size*6j, 0:1:size*6j, 0:1:size*6j]
#    R = np.sqrt(fx**2 + fy**2 + ft**2 )
#    #R[0 , 0 , 0] = inf 
#    data = R
#    return data
#

def image_data(dim=(size, size, size), sp=(1, 1, 1), orig=(0, 0, 0), bwd=(.01, .1, .4)):#, rsrc=False):
    """
    Create Image Data for the surface from a data source. 
    If rsrc == True, it generates random data.
    """
#    if rsrc:
#        data = random_source(dim)
#    else:
    data = source(dim, bwd)
    i = tvtk.ImageData(spacing=sp, origin=orig)
    i.point_data.scalars = data.ravel()
    i.point_data.scalars.name = 'scalars'
    i.dimensions = data.shape
    return i


def view(dataset):
    """ 
    Open up a mayavi scene and display the cubeset in it.
    """
    engine = mlab.get_engine()
    #fig = mlab.figure(bgcolor=(0, 0, 0), fgcolor=(1, 1, 1),
    #                  figure=dataset.class_name[3:])
    src = VTKDataSource(data=dataset)
    engine.add_source(src)
    # TODO : make some cubes more redish to show some "activity"
    mlab.pipeline.surface(src, colormap='gray')

def main(dim=(size, size, size), sp=(1, 1, 1), orig=(0, 0, 0), B=(.01, .1, .4)):
    view(image_data(dim=dim, sp=sp, orig=orig, bwd=B))
#
#def cube_outline(dim, rsrc):
#    """
#    Draw an outer cube to add outline and labels
#    """
#    main(dim=dim, rsrc=rsrc)
    
    
# The code for the pdb-like file.
def get_nodes_and_edges():
    protein_code = 'mc0612'
    import gzip
    infile = gzip.GzipFile('%s.ent.gz' % protein_code, 'rb')
    
    # A graph represented by a dictionary associating nodes with keys
    # (numbers), and edges (pairs of node keys).
    nodes = dict()
    edges = list()
    atoms = set()
    
    # Build the graph from the PDB information
    for line in infile:
        line = line.split()
        if line[0] in ('ATOM', 'HETATM'):
            nodes[line[1]] = (line[2], line[6], line[7], line[8])
            atoms.add(line[2])
        elif line[0] == 'CONECT':
            for start, stop in zip(line[1:-1], line[2:]):
                edges.append((start, stop))
    
    atoms = list(atoms)
    atoms.sort()
    atoms = dict(zip(atoms, range(len(atoms))))
    
    # Turn the graph into 3D positions, and a connection list.
    labels = dict()
    
    x       = list()
    y       = list()
    z       = list()
    scalars = list()
    
    for index, label in enumerate(nodes):
        labels[label] = index
        this_scalar, this_x, this_y, this_z= nodes[label]
        scalars.append(atoms[this_scalar])
        x.append(float(this_x))
        y.append(float(this_y))
        z.append(float(this_z))
    
    connections = list()
    
    for start, stop in edges:
        #import pdb; pdb.set_trace()
        connections.append((labels[start], labels[stop]))
    
    x       = np.array(x)
    y       = np.array(y)
    z       = np.array(z)
    scalars = np.array(scalars)
    return x, y, z, connections, scalars    



if __name__ == '__main__':

    #legend
    """
    
   Motion Clouds are a set of stimuli designed to explore in a systematic 
    way the functional response of a sensory system to a natural-like motion 
    stimulus. These are optimized for translating, full-field motion and are by 
    construction textures synthesized from randomly placed similar motion 
    patches with characteristics spatial parameters. The object of such an 
    endeavor is to systematically test a system to varying the parameters by 
    testing the response to a series of such textures. We show here for a fixed 
    set of central parameters (mean speed, direction, orientation and spatial 
    frequency) a cube constituted by a family of such Motion Clouds when varying 
    the bandwidth parameters for speed (left panel), frequency (right panel) and
     orientation (top panel). Each elementary cube in the larger cube denoting 
    the parameter space represents a Motion Cloud and is shown as a cube to 
    represent the corresponding movie, with time flowing from lower left to 
    upper right in the right and top facets. Overlaid hue gives a measure of a 
    typical response for a sensory response (here a motion energy model) which 
    gives a complete characterization of the sensory system at hand.
    """

    import itertools
    
    space = 1.5 * size # space between 2 cubes
    N = 5
    idx = np.arange(N)
    pos = idx * space
    Bf = np.logspace(-2., 0.1, 5)
    Bv = [0.01, 0.1, 0.5, 1.0, 10.0]
    sigma_div = [2, 3, 5, 8, 13]
    Bo = np.pi/np.array(sigma_div)

    fx, fy, ft = mc.get_grids(size, size, size)

    # x-axis = B_f
    # y-axis = B_V
    # z_axis = B_o
    downscale = 2
    downscale = 1
    mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(1600/downscale,1200/downscale))
    mlab.clf()
    
    do_grid, do_splatter, do_MCs = False, True, False
    do_grid, do_splatter, do_MCs = True, True, True
    ################################################################################
    ##  Generate the cubical graph structure to connect each individual cube      ##
    ################################################################################
    if do_grid:
        x, y, z, connections, scalars = get_nodes_and_edges()
        
        x = x * space + size / 2.
        y = y * space + size / 2.
        z = z * space + size / 2.
        scalars = np.random.uniform(low=0.3, high=0.55, size=x.shape)
        
        pts = mlab.points3d(x, y, z, scalars, colormap = 'Blues', scale_factor=5.0, resolution=10)
        pts.mlab_source.dataset.lines = np.array(connections)
    
        # Use a tube filter to plot tubes on the link, varying the radius with the
        # scalar value
        tube = mlab.pipeline.tube(pts, tube_radius=1.5)
        tube.filter.radius_factor = 1.
        tube.filter.vary_radius = 'vary_radius_by_scalar'
        mlab.pipeline.surface(tube, colormap = 'gray')
    
    ################################################################################
    ##                      Gaussian Splatter                                     ##
    ################################################################################
    if do_splatter:
   
    # Visualize the local atomic density
    #mlab.pipeline.volume(mlab.pipeline.gaussian_splatter(pts))
#    gs = mlab.pipeline.gaussian_splatter(pts)
#    gs.filter.radius = 0.95
#    iso=mlab.pipeline.iso_surface(gs, colormap = 'RdBu', opacity=0.03)
#    iso.contour.number_of_contours = 50
#    gsvol = mlab.pipeline.volume(gs)
        x_, y_, z_ = np.mgrid[0:(N*space), 0:(N*space), 0:(N*space)]
#        response = np.exp(-(  ((x_-2*space) + (y_-3*space))**2 +((y_-3*space))**2 +((z_-2*space)/2.)**2)/2/(3.*space)**2)#-1/2.*np.exp(-(x_ + y_  +z_/2.- 5.)**2/2/(2.*space)**2)
        response = np.exp(-(((x_-4*space))**2 +((y_- 1*space))**2 +((z_-3.4*space)/2.)**2)/2/(3.*space)**2)#-1/2.*np.exp(-(x_ + y_  +z_/2.- 5.)**2/2/(2.*space)**2)
        sf = mlab.pipeline.scalar_field(x_, y_, z_, response)
        vol = mlab.pipeline.volume(sf, vmin=0, vmax = 4.)#, color='red')#, colormap = 'RdBu') #response.min()+0.65*(response.max()-response.min()),  vmax=min+0.9*(max-min))
#        # Changing the ctf:
#        from tvtk.util.ctf import ColorTransferFunction
#        ctf = ColorTransferFunction()
#        ctf.add_rgb_point(0., 0., 0., 1.) # r, g, and b are float between 0 and 1
#        ctf.add_rgb_point(1., 1., 0., 0.) # r, g, and b are float between 0 and 1
##        ctf.add_hsv_point(value, h, s, v)
#        # ...
#        vol._volume_property.set_color(ctf)
#        vol._ctf = ctf
#        vol.update_ctf = True
#        
#        # Changing the otf:
#        from tvtk.util.ctf import PiecewiseFunction
#        otf = PiecewiseFunction()
#        otf.add_point(0., 0.)
#        otf.add_point(1., 1.)
#        vol._otf = otf
#        vol._volume_property.set_scalar_opacity(otf)
    ################################################################################
    ##  Generate a second layer of points to switch on and off some cubes         ##
    ################################################################################

#    # on_off = np.array(np.random.random_integers(low=0, high=1, size=125), dtype=float)
#    #  values = on_off * scalars
#    x_, y_, z_ = np.mgrid[0:N, 0:N, 0:N]
##    values = np.exp(-(x_ -x_.mean())**2/x_.std()**2 - (y_ - y_.mean())**2/y_.std()**2)-.5
#    values = 2.* np.exp(-(x_ + y_  +z_/2.- 5.)**2/2/4)-1.
#    print(values.shape)
#    on_off_pts = mlab.points3d(x, y, z, values.ravel()*9.1803399, colormap = 'RdBu', 
#                               scale_factor=size/5.0, mode='sphere', resolution = 32,
#                               transparent=True, opacity=0.25)#*np.abs(values)/np.abs(values).max())

#    ################################################################################
#    ##                      Generate the Motion Clouds cubes                      ##
#    ################################################################################
    if do_MCs:
        for i, j, k in list(itertools.product(idx, idx, idx)):
            main(orig=(pos[i], pos[j], pos[k]), B=(Bf[i], Bv[j], Bo[k]))
        
    mlab.view( azimuth=290., elevation=45., distance='auto', focalpoint='auto')
#    mlab.show(stop=True)
    mlab.savefig('MCartwork.png')
