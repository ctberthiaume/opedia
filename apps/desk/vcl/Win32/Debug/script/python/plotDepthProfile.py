import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import db
from datetime import datetime, timedelta
import time
from math import pi
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.models import DatetimeTickFormatter
from bokeh.palettes import all_palettes
from bokeh.models import HoverTool
from bokeh.embed import components


def depthLevels(depth1, depth2):
    #piscesDepths
    levels = [0.494024991989, 1.54137504101, 2.64566898346, 3.81949496269, 5.07822418213, 6.44061422348, 7.92956018448, 9.5729970932, 11.404999733, 13.4671401978, 15.8100700378, 18.4955596924, 21.5988197327, 25.2114105225, 29.4447307587, 34.4341506958, 40.3440513611, 47.3736915588, 55.764289856, 65.8072662354, 77.8538513184, 92.3260726929, 109.729301453, 130.666000366, 155.850692749, 186.125595093, 222.475204468, 266.040313721, 318.127410889, 380.213012695, 453.937713623, 541.088928223, 643.566772461, 763.333129883, 902.339294434, 1062.43994141, 1245.29101562, 1452.25097656, 1684.28405762, 1941.89294434, 2225.07788086, 2533.3359375, 2865.70288086, 3220.82006836, 3597.03198242, 3992.48388672, 4405.22412109, 4833.29101562, 5274.78417969, 5727.91699219]
    ind1 = levels.index(depth1)
    ind2 = levels.index(depth2)
    levels = levels[ind1:ind2+1]
    return levels

def embedComponents(fname, data):
    f = open(fname, 'w')
    f.write(data)
    f.close()
    return

def prepareTimeSpaceQuery(table, date1, date2, lat1, lat2, lon1, lon2):
    query = "SELECT AVG(sla) AS sla, AVG(sst) AS sst, AVG(u) AS u, AVG(v) as v FROM %s WHERE "
    #query = query + "[time]>='%s' AND [time]<='%s' AND "
    query = query + "[time]='%s' AND "
    query = query + "lat>=%f AND lat<=%f AND "
    query = query + "lon>=%f AND lon<=%f "
    #query = query % (table, date1, date2, lat1, lat2, lon1, lon2)
    query = query % (table, date1, lat1, lat2, lon1, lon2)
    return query



def depthProfile(table, field, dt, lat1, lat2, lon1, lon2, depth1, depth2):
    y = np.array([])
    y_std = np.array([])
    depths = depthLevels(depth1, depth2)
    
    
    for depth in depths:
        #dtStamp = dt.strftime('%Y-%m-%d')
        '''
        ############# App-Level Query #############
        query = prepareTimeSpaceQuery(table, dtStamp, dtStamp, lat1, lat2, lon1, lon2)
        df = db.dbFetch(query)
        ###########################################
        '''
        
        ######### Stored Procedure Query ##########
        query = 'EXEC uspDepthProfile ?, ?, ?, ?, ?, ?, ?, ?'
        args = [table, field, dt, str(lat1), str(lat2), str(lon1), str(lon2), str(depth)]        
        df = db.dbFetchStoredProc(query, args)
        df = pd.DataFrame.from_records(df, columns=['lat', 'lon', 'depth', field])
        ###########################################
        

        try:
            if len(df[field]) > 0:                
                tempY = np.nanmean(df[field])
            else:
                tempY = np.nan
        except:
            tempY = np.nan   

        if abs(tempY) > 1e30:       ## remove outliers (extremes)
            tempY = np.nan   
            
        y = np.append(y, tempY)

        try:
            if len(df[field]) > 0:
                tempY_std = np.nanstd(df[field])
            else:
                tempY_std = np.nan
        except:
            tempY_std = np.nan        

        if abs(tempY_std) > 1e30:       ## remove outliers (extremes)
            tempY_std = np.nan   

        y_std = np.append(y_std, tempY_std)
    return depths, y, y_std

def plotDepthProfile(tables, variables, dt, lat1, lat2, lon1, lon2, depth1, depth2, fname, marker='-', msize=30, clr='orangered'):
    p = []
    lw = 2
    w = 800
    h = 400
    TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'
    for i in range(len(tables)):
        depths, y, yErr = depthProfile(tables[i], variables[i], dt, lat1, lat2, lon1, lon2, depth1, depth2)
        p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
        #p1.xaxis.axis_label = 'Depth'
        p1.yaxis.axis_label = variables[i] + ' [' + db.getVar(tables[i], variables[i]).iloc[0]['Unit'] + ']'
        leg = variables[i]
        cr = p1.circle(depths, y, fill_color="grey", hover_fill_color="firebrick", fill_alpha=0.07, hover_alpha=0.3, line_color=None, hover_line_color="white", legend=leg, size=msize)
        p1.line(depths, y, line_color=clr, line_width=lw, legend=leg)
        p1.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))
        p.append(p1)


    output_file("embed/" + fname + ".html", title="Depth Profile")
    show(column(p))
    
    '''
    p1_script, p1_div = components(p1)
    embedComponents('embed/scriptDP1.js', p1_script)
    embedComponents('embed/divDP1.js', p1_div)

    p2_script, p2_div = components(p2)
    embedComponents('embed/scriptDP2.js', p1_script)
    embedComponents('embed/divDP2.js', p1_div)

    p3_script, p3_div = components(p3)
    embedComponents('embed/scriptDP3.js', p1_script)
    embedComponents('embed/divDP3.js', p1_div)
    '''
    return




tables = sys.argv[1].split(',')      #tables
variables = sys.argv[2].split(',')      #variables
dt = sys.argv[3]      #dt
lat1 = float(sys.argv[4])      #lat1
lat2 = float(sys.argv[5])      #lat2
lon1 = float(sys.argv[6])      #lon1
lon2 = float(sys.argv[7])      #lon2
fname = sys.argv[8]
depth1 = float(sys.argv[9])      #depth1
depth2 = float(sys.argv[10])      #depth2



if float(lat1)>float(lat2):
    temp = lat1
    lat1 = lat2
    lat2 = temp

if float(lon1)>float(lon2):
    temp = lon1
    lon1 = lon2
    lon2 = temp

if float(depth1)>float(depth2):
    temp = depth1
    depth1 = depth2
    depth2 = temp


tic = time.clock()
plotDepthProfile(tables, variables, dt, lat1, lat2, lon1, lon2, depth1, depth2, fname)
toc = time.clock()
print('Fetch time: %2.2f s' % (toc-tic))