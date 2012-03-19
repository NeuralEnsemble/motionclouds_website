#!/usr/bin/env python

print('launching experiment')
from psychopy import *
import time

try:
    #try to load previous info
    info = misc.fromFile('competing.pickle')
except:
    #if no file use some defaults
    info={}
    info['observer']=''
    info['screen_width']=480
    info['screen_height']=270
    info['nTrials']=50
    info['N_X'] = 256 # size of image
    info['N_Y'] = 256 # size of image
    info['N_frame_total'] = 128 # a full period. in time frames
    info['N_frame'] = 64 # a full period. in time frames
try:
    dlg = gui.DlgFromDict(info)
except:
    print('Could not load gui... running with defaut parameters')
    print(info)
#save to a file for future use (ie storing as defaults)
if dlg.OK:
    misc.toFile('competing.pickle',info)
else:
    print('Could not load gui... running with defaut parameters')
    #core.quit() #user cancelled. quit
info['timeStr']=time.strftime("%b_%d_%H%M", time.localtime())


print('generating data')

import os, numpy
import RandomCloud as mc

fx,fy,ft = mc.get_grids(info['N_X'],info['N_Y'],info['N_frame_total'])
color = mc.envelope_color(fx, fy, ft)
up = 2*mc.rectif(mc.random_cloud(color * mc.envelope_donut(fx,fy,ft, V_X= 0., V_Y=+.5))) - 1
down = 2*mc.rectif(mc.random_cloud(color * mc.envelope_donut(fx,fy,ft, V_X= 0., V_Y=-.5))) - 1

print('go!      ')
win = visual.Window([info['screen_width'],info['screen_height']],fullscr=True)

def getResponse():
    event.clearEvents()#clear the event buffer to start with
    resp=None#initially

    while 1:#forever until we returns
        for key in event.getKeys():
            #quit
            if key in ['escape', 'q']:
                    myWin.close()
                    #myWin.bits.reset()
                    core.quit()
                    return None
            #valid response - check to see if correct
            elif key in ['down','up']:
                    if key in ['down'] :  return -1
                    else:
                            return 1
            else:
                    print "hit DOWN or UP (or Esc) (You hit %s)" %key

def presentStimulus(C_A,C_B):
    """Present stimulus
    """
    phase_up = numpy.floor(numpy.random.rand() *(info['N_frame_total']-info['N_frame']))
    phase_down = numpy.floor(numpy.random.rand() *(info['N_frame_total']-info['N_frame']))
    for i_frame in range(info['N_frame']): # length of the stimulus
        stim = visual.PatchStim(win,
            tex=C_A * up[:,:,i_frame+phase_up]+C_B * down[:,:,i_frame+phase_down],
            size=(info['N_X'],info['N_Y']), units='pix',
            interpolate=False)
        stim.draw()
        stim.clearTextures()
        win.flip()
    win.update()

results=numpy.zeros((2,info['nTrials']))
for i_trial in range(info['nTrials']):
    C_A=numpy.random.rand() # a random number between 0 and 1
    presentStimulus(C_A, 1. - C_A)
    ans=getResponse()
    results[0,i_trial]=ans
    results[1,i_trial]=C_A

win.update()
core.wait(0.5)

win.close()

#save data
fileName= info['observer'] + '_' + info['timeStr']
numpy.save(fileName,results)

import pylab
pylab.scatter(results[1,:],results[0,:])
pylab.axis([0.,1.,-1.1,1.1])
pylab.xlabel('contrast')
pylab.savefig('competing_psychopy.png')
