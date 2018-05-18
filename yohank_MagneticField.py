from vpython import *
#GlowScript 2.5 VPython
#Yohanes Kurnia
#University of Washington 2017
#A simulation for magnetic force on a charged particle due to a current-carrying wire
#The simulation is made on a 3D canvas where the wire is placed along the z-axis
#Users can place a charge any where in the 3D space. The canvas can be rotated
#up, down and left, right directions. However, users can only place
#a charge in the plane perpendicular to the line of sight (i.e. if the user is looking at
#the origin from the point (1, 1, 1), users can only place points on the surface
#x + y + z = 1). Users can choose to show/hide velocity, magnetic field, magnetic force
#vector on the charged particle. Users can also choose from 5 different velocities
#Users can also quickly change perspective to top view and side view and also reset view
#if they wish to go back to the initial view. Magnetic field strength is calculated
#using ampere's law.

#IMPORTANT NOTE:
#Positive X takes in negative y parameters, Positive Y takes in positive y parameters.
#This is done so that the axes will have a right-handed coordinate axes
# A point with a position vector <3, -2, 1> will be located at x = 2, y = 3, z = 1 on the canvas
# A point with a position vector <2, 1,  0> will be located at x = -1, y= 2, z = 0 on the canvas

#-------------------------------------------------------------------------------
#------------------------------Canvas Setting-----------------------------------
#-------------------------------------------------------------------------------

$('<div id = "title" style = "overflow: scroll; clear:both; text-align:middle">').prependTo('body')
$('<h2> Magnetic force exerted on a charged particle near a current-carrying wire</h2>').appendTo('#title')
$('<h5 id="Message"> This program is intended to help you visualize the velocity, B-field, and magnetic force for a moving charged particle near a current carrying wire.</h5>').appendTo('#title')
scene = canvas(width = 600, height = 600, align  = "left", background = color.black)
light1 = distant_light(color = color.gray(0.4), direction =vec(1,1,1))
light2 = distant_light(color = color.gray(0.4), direction = vec(-1,-1,-1))
light3 = distant_light(color = color.gray(0.4), direction = vec(1,-1,1))
light4 = distant_light(color = color.gray(0.4), direction = vec(-1,1,1))
scene.forward = vec(-1,1,-1)
scene.up = vec(0,0,1)
scene.title = ""
scene.caption = ""
justLoad = True

#-------------------------------------------------------------------------------
#|-----------------------Instructions and Buttons-------------------------------
#-------------------------------------------------------------------------------
pageNum = 1     #Initialize page number
maxPage = 2     #Maximum instructin page number.
mobile = window.orientation > -1    #Check if mobile device is used

#Hide message notifying that the program does not work properly with iOS devices
def hideBrowser():
    $('#Message').hide()
    $('#browser').hide()

$('<p id = "browser"><b>Note</b>: Landscape mode is not fully compatible with mobile devices. '
+ '(Some of the instructions and figure may be cut off on the top and/or sides.) <br> '
+ 'Use of full-size computers (desktop or laptop) are recommended. '
+ 'Computers are available at various locations on campus, including in the Physics Study Center.</p>').appendTo('#title')
$('<button type = "arrow" />').text("Dismiss").appendTo('#browser').on('click', def fun():
    hideBrowser()
)

#Sets where the instruction box appears on the window depending on computers/mobile devices
if(!mobile):
    $('<div id = "overallPage" style="position:absolute;left:640px;width:550px; height:500px">').appendTo('body')
    clearType = 'none'
else:
    $('<div id = "overallPage" style="width:600px; height:500px">').appendTo('body')
    clearType = 'both'

#--------------------------------------------------------------------------
# Instructions written in jQuery
# I apologize sincerely for the mixture of glowscript and jquery in the code
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
# Area for instructions
$('<div id = "instructions" style="float: left; overflow-y:auto; white-space:normal; clear:' + clearType + ';
            width: 550px; height: 240px; padding: 0cm 0.5cm 0cm 0.5cm; border:1px solid black">').appendTo('#overallPage')

#-------------------------------------------          
#------------ Page 1 instructions ---------
#------------------------------------------- 
$('<div class = "pg1instruct" id = "pg1ins" style = "clear: none; text-align:justify">').appendTo('#instructions')
$('<span><b>Page 1 Instructions (scroll down) </b><br><br></span>').appendTo('#pg1ins')
$('<span><b>Familiarize yourself with the program</b><br></span>').appendTo('#pg1ins')
$('<p> The diagram at left shows a wire of infinite length (part of which is shown in white) that lies along the z-axis.'
    + ' The wire has a constant current in the +z-direction of I = 0.5 A.'
    + ' Initially, the x, y, and z coordinate axes are shown.'
    + ' A charge, q = +1 µC (purple) is shown near the wire.<br></p>').appendTo('#pg1ins')
$('<span> <b> Instructions: </b><br><br></span>').appendTo('#pg1ins')
$('<span id = "cp"><b> To relocate the charge: </b><br></span>').appendTo('#pg1ins')

$('<li> Computer: Left-click at the desired location.<br></li>').appendTo('#pg1ins')
$('<li> Mobile device: Touch the screen at the desired location.<br>'
+ '(You can drag the charge by moving the mouse/your finger while clicking/touching.)</li>').appendTo('#pg1ins')
$('<span id = "mc"><br><b> To change perspective: </b></span>').appendTo('#pg1ins')
$('<li> Computer: press right-click (or control-left click) and move your mouse while holding the mouse button.<br> </li>'
+ '<li>Mobile device: press on the screen and immediately move fingers until a desired view is obtained. </li>').appendTo('#mc')

$('<span><b><br>To zoom in and out: </b></span>').appendTo('#pg1ins')
$('<li>Computer: use the scroll wheel or pinch the trackpad. </li>').appendTo('#pg1ins')
$('<li>Mobile device: pinch the screen or use the appropriate magnification gesture for your device. </li>').appendTo('#pg1ins')

$('<span><b><br>To quickly change perspective: <br> </b></span>').appendTo('#pg1ins')
$('<span>The buttons below will quickly change to top and side view perspectives. The “Reset View” button will return to the'
+ ' original view.<br><br></span>').appendTo('#pg1ins')

$('<span><b>Show/hide various elements:</b><br></span>').appendTo('#pg1ins')
$('<span>You can toggle on and off the coordinate axes and velocity, B-field, and magnetic force using the show/hide buttons'
+ ' below. (If you choose to show the velocity, no arrows will show if the velocity is zero.)<br><br></span>').appendTo('#pg1ins')

$('<p> Familiarize yourself with the features above and then proceed to page 2.</p>').appendTo('#pg1ins')

#------------------------------------------- 
#------------- Page 2 instructions --------
#------------------------------------------- 
$('<div class = "pg2instruct" id = "pg2ins" style = "overflow: scroll; clear:none; text-align:justify">').appendTo('#instructions').hide()
$('<p><span><b>Page 2: Practice<br><br> </b></span>'
+ '<span>Now, a charge is placed to the right of the wire as shown in the program. The magnetic field is shown at that location.<br><br><span>'
+ '<span><b>Predicting the direction of the magnetic field</b></span>'
+ '<ol><li>Suppose you were looking at this situation using the top-view diagram.(<i>i.e.,</i> looking down at the wire from the top). <i>Predict</i> the direction of the magnetic field due to the wire at the charge location. (<i>e.g.,</i> Would it be into the page, out of the page, <i>etc.</i>?) Then, check your prediction'
+ ' by clicking on the Top View button.</li><br>'
+ '<li><i>Predict</i> the direction of the magnetic field due to the wire at the charge location in the side view (<i>i.e.,</i> looking at the wire from the side). Then, '
+ 'check your prediction by clicking on the Side View button. (It may be useful to hide the axes when you check your answer.)</li><br>'
+ '<li>Does your prediction agree with the vector you see on the screen?</li></ol>'
+ '<span><b>Predicting the direction of the magnetic force on the particle</b></span>'
+ '<ol><li>Imagine that the charge had a velocity <b>v<sub>3</sub></b> at its current location. Determine the direction of the magnetic <b>force</b> exerted on the charge in the side-view diagram at the instant shown.<br></li><br>'
+ '<li><i>Predict</i> the direction of the magnetic force exerted on the charge at that same location in the <i><b>top</b></i> view.<br></li><br>'
+ '<li>Click on "Side view" and "Top view" buttons and use the "Show magnetic force on the particle" button to verify your answers.</li><br>'
+ '<li>Repeat the steps above using different velocities from the choices below.</li></ol>').appendTo('#pg2ins')

$('<p><span>After you are comfortable making these predictions, return to the pretest and finish answering the remaining questions.</span></p>').appendTo('#pg2ins')


#-------------------------------------------------------------------------------------- 
#------------- Page 3 instructions (update maxPage to include page 3) --------
#------------------------------------------------------------------------------------- 
#$('<div class = "pg3instruct" id = "pg3ins" style = "overflow: scroll; clear:none; text-align:justify">').appendTo('#instructions').hide()
#$('<p><span><b>Page 3 Instructions </b></span>'
#+ '<li>Click on "Side View" button and place a charged particle to the left of the wire.</li>'
#+ '<li>Determine the direction of the magnetic force on the particle moving with velocity <b>v<sub>2</sub></b> at that location by observing the magnetic force vector '
#+ 'from different perspectives.</li>'
#+ '<li>Determine the direction of the magnetic force on a particle moving with velocities <b>v<sub>3</sub></b> and <b>v<sub>4</sub></b> at that same location.</li>'
#+ '<li>Now, determine the direction of the magnetic force on a particle moving with velocity <b>v<sub>5</sub></b> at that same location.</li>'
#+ '<li>How is the direction of the magnetic force on the particle moving with velocity <b>v<sub>5</sub></b> related to the magnetic forces exerted on '
#+ 'the same particle moving with velocities <b>v<sub>2</sub></b>, <b>v<sub>3</sub></b>, and <b>v<sub>4</sub></b>? (Think superposition principle).</li>'
#+ '<li>Make a prediction on the direction of the force on the particle at that location'
#+ ', if the particle has a velocity <b>v<sub>7</sub></b> = <5, 5, -5>. Use <b>v<sub>6</sub></b> to help you make '
#+ 'your prediction and answer this question on the pretest.</li>').appendTo('#pg3ins')

#------------------------------------------- 
#---------- AREA HOLDER FOR BUTTONS --------
#------------------------------------------- 
$('<div id = "buttons" style = "overflow: hidden; clear:' + clearType + '; width: 600px; height: 220; padding: 0.25cm 0cm 0cm 0cm">').appendTo('#overallPage')

#------------------------------------------- 
#------------ Change Perspective -----------
#------------------------------------------- 
$('<span class = "perspectiveButtons" style="text-align: left"><b>Change perspective: <br></span>').appendTo('#buttons')
$('<button id = "view1"/>').text('Top View').appendTo('.perspectiveButtons').on('click', def fun():
    scene.up = vec(0,1,0)
    scene.forward = vec(0,0,-1)
)
$('<button id = "view3"/>').text('Side View').appendTo('.perspectiveButtons').on('click', def fun():
    #scene.up = vec(1,0,0)
    scene.forward = vec(0,1,0)
    scene.up = vec(0,0,1)
)
$('<button id = "resetView"/>').text('Reset View').appendTo('.perspectiveButtons').on('click', def fun():
    scene.forward = vec(-1,1,-1)
    scene.up = vec(0,0,1)
    scene.range = 55
    scene.center = vec(0,0,0)
)

#------------------------------------------- 
#----------- Show/Hide buttons -------------
#------------------------------------------- 
$('<span class = "hideButtons" style = "text-align: left"><br><br><b>Show/Hide: </b><br></span>').appendTo('#buttons')
$('<button id = "b1"/>').text('Hide Axes').appendTo('.hideButtons').on('click', def fun():
    coordShow()
)
$('<button id = "b2"/>').text('Show Velocity').appendTo('.hideButtons').on('click', def fun():
    showVel()
)
$('<button id = "b3"/>').text('Show Magnetic Field at Location').appendTo('.hideButtons').on('click', def fun():
    showB()
)
$('<button id = "b4"/>').text('Show Magnetic Force on Particle').appendTo('.hideButtons').on('click', def fun():
    showF()
)


#--------------------------------------------------------
#------------ Radio Buttons to pick velocity ------------
#--------------------------------------------------------
#Y-axis to points positive in the negative-y direction i.e. v3 = <0,5,0>  is actually <0,-5,0>
$('<div id = "radioButtons" style = "overflow: scroll; clear: none; width 400px; height: 300; padding: 0cm 0cm 0cm 0cm">').appendTo('#buttons')
$('<p><b> Pick a velocity: </b></p>').appendTo('#radioButtons')
$('<input type = "radio" name = "vel" value = "v1"/><b>v<sub>1</sub></b> = <0,0,0> &nbsp;&nbsp;</input>').appendTo('#radioButtons').attr('checked', True).on('click', def fun():
    pickVel()
)
$('<input type = "radio" name = "vel" value = "v2"/><b>v<sub>2</sub></b> = <5,0,0> &nbsp;&nbsp;</input>').appendTo('#radioButtons').on('click', def fun():
    pickVel()
)
$('<input type = "radio" name = "vel" value = "v3"/><b>v<sub>3</sub></b> = <0,5,0> &nbsp;&nbsp;<br></input>').appendTo('#radioButtons').on('click', def fun():
    pickVel()
)
$('<input type = "radio" name = "vel" value = "v4"/><b>v<sub>4</sub></b> = <0,0,5> &nbsp;&nbsp;</input>').appendTo('#radioButtons').on('click', def fun():
    pickVel()
)
$('<input type = "radio" name = "vel" value = "v5"/><b>v<sub>5</sub></b> = <5,5,5> &nbsp;&nbsp;</input>').appendTo('#radioButtons').on('click', def fun():
    pickVel()
)


#-------------------------------------------------------
#---------------- Legends/Key Table --------------------
#-------------------------------------------------------
$('<div class = "legends" id = "legendDiv" style = "display: inline-block; clear: none;
                width = 130px; height = 100px; padding: 0cm 0cm 0cm 0cm">').appendTo('#overallPage')
$('<p><b>Key</b></p>').appendTo('#legendDiv')
$('<colgroup span="5" id = "titleCol" style="background-color:black; width:50px"/>').appendTo('#legendDiv')
$('<tr><th><font color="white">Axes</font></th><th></th><th style="border-right: 1px solid white"> </th>'
    +'<th><font color="white"> &nbsp;&nbsp;Arrows</font></th><th></th></tr>').appendTo('#legendDiv')
$('<colgroup span="5" id = "keyCol" style="background-color:black; width:50px"/>').appendTo('#legendDiv')
$('<tr><td width = 50px><font color="red"> Red:</font></td> <td width = 50px><font color="red">x-axis </font></td> <td style="border-right: 1px solid white"> </td> '
    +'<td width = 50px><font color="magenta"> &nbsp;&nbsp;Purple:</font> </td width = 150px> <td><font color="magenta">charge</font></td></tr>').appendTo('#legendDiv')
$('<tr><td width = 50px><font color="yellow"> Yellow:</font></td> <td width = 50px> <font color="yellow"> y-axis </font></td> <td style="border-right: 1px solid white">  </td>'
    +'<td width = 50px><font color="cyan">  &nbsp;&nbsp;Cyan:</font></td> <td width = 150px><font color="cyan"> B-Field</font></td></tr>').appendTo('#legendDiv')
$('<tr><td width = 50px><font color="green">  Green:</font></td>  <td width = 50px><font color="green">z-axis</font></td> <td style="border-right: 1px solid white"> </td>'
    +'<td width = 50px><font color="white"> &nbsp;&nbsp;White:</font></td> <td width = 150px><font color="white">velocity</font></td></tr>').appendTo('#legendDiv')
$('<tr><td width = 50px></td> <td width = 50px></td> <td style="border-right: 1px solid white"> </td>'
    +'<td width = 50px><font color="orange"> &nbsp;&nbsp;Orange:</font></td>  <td width = 150px><font color="orange">magnetic force</font></td></tr>').appendTo('#legendDiv')
$('<tr><td width = 50px><font color ="#f2ecec"> Wire:</font></td>  <td width = 50px><font color="#f2ecec"> white</font></td> <td style="border-right: 1px solid white"> </td>'
    + '<td width = 50px></td> <td width = 150px><font color="orange">  on particle</font></td></tr>').appendTo('#legendDiv')

#--------------------------------------------------------
#------------- Change Page (Instructions) ---------------
#--------------------------------------------------------
$('<div class = "changePage" id = "chgPageDiv" style = "float:right;display:inline; clear: none; 
                    width: 300; height: 50px; padding: 0cm 0cm 0cm 0cm">').appendTo('#overallPage')
$('<input type = "button" id = "backPg" name="pages" value = "Back"></input>').appendTo('#chgPageDiv').on('click', def fun():
    nonlocal pageNum
    if (pageNum > 1):
        str = pageInst()
        $("div." + str).hide()
        pageNum -= 1
        $('#pgNum').text(pageNum)
        str = pageInst()
        $("div." + str).show()
        $('#instructions').scrollTop(0)
)
$('<span id = "pgs"> page  </span>').appendTo('#chgPageDiv')
$('<span id = "pgNum"></span>').appendTo('#pgs')
$('#pgNum').append(pageNum)
$('#pgs').append(" of ")
$('#pgs').append(maxPage)
$('<input type = "button" name="pages" value = "Next"></input>').appendTo('#chgPageDiv').on('click', def fun():
    nonlocal pageNum
    #This is specific for current page 2 instruction
    #If user had show velocity and force on from page 1, changing to page 2
    #will automatically switch to hide velocity and hide force
    #Puts a new charge at x = 0, y = 10, z = 0
    if (pageNum < maxPage):
        if !showBArrow:
            showB()
        if showVArrow:
            showVel()
        if showFArrow:
            showF()
        $('#resetView').click()
        bind = down(vec(10,0,0))
        drawCoordinateLocator()
        str = pageInst()
        $("div." + str).hide()
        pageNum += 1
        $('#pgNum').text(pageNum)
        str = pageInst()
        $("div." + str).show()
        $('#instructions').scrollTop(0)
)

#Returns current page instruction class. 
def pageInst():
    nonlocal pageNum
    str = "pg"
    str += pageNum
    str += "instruct"
    return str



#-------------------------------------------------------------------------------
#------------------------------Draw Axes----------------------------------------
#-------------------------------------------------------------------------------

#Note: Axes rotations are still wonky due to glowscript's canvas.up()
#REFER TO IMPORTANT NOTE at the top of the page
X_axis  = arrow(pos = vec(-50, 0, 0), axis = vec(100, 0, 0), color = color.yellow, 
                opacity = .3, shaftwidth = 1, headwidth = 2)

Y_axis  = arrow(pos = vec(0, 50, 0), axis = vec(0, -100, 0), color = color.red, 
                opacity = .3, shaftwidth = 1, headwidth = 2)

Z_axis  = arrow(pos = vec(0, 0, -50), axis = vec(0, 0, 100), color = color.green, 
                opacity = .3, shaftwidth = 1, headwidth = 2)

#Draw current-carrying wire and dots and cross to signify into/out of page
rod = cylinder(pos = vec(0, 0, -40), axis = vec(0, 0, 1), 
               size = vec(80, 2, 2), color = color.white)
dot1 = cylinder(pos = vec(0,0,39), axis = vector(0,0,1), size = vec(1,1,1) , color = color.black)
line1 = arrow(pos=vector(.5,-.5,-40), axis = vec(-1,1,0), headwidth = 0.1, headlength = 0.1, color = color.black)
line2 = arrow(pos=vector(-.5,-.5,-40),axis = vec(1,1,0), headwidth = 0.1, headlength = 0.1, color = color.black)
                        

#-------------------------------------------------------------------------------
#-----------------------Functions for Calculations------------------------------
#-------------------------------------------------------------------------------


# Functions to calculate Magnetic Force at a given point with charge q = +1
def calculateBForce(vel, magneticField):
    BForce2 = cross(vel, magneticField) # F = qvxB,  q = 1C
    return BForce2

# Function to calculate Magnetic Field at a given point with current >> 1 A
def calculateBField(rx,ry):
    if (rx == 0 & ry == 0):
        rx += 1
        ry += 1
    mu_0 = 4 * pi * 10**(-7)
    current = 2000 / mu_0 # mu_0 * I = 1000
    radius = sqrt((rx)**2 + (ry)**2)
    magneticField = mu_0 * current / (2 * pi * radius)
    unitVector = vec(-ry / radius, rx / radius, 0)
    return magneticField * unitVector

## Calculates angle between two vectors
#def calculateAngle(v1, v2):
#    n = acos((dot(v1, v2)/(mag(v1)*mag(v2))))
#    n = round(n / pi * 180)
#    return n

    
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#--------------------Variable Initialization for interactivity------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#Arrays are used so that each time a new point is picked, the old value is replaced
#by the new value (n2 % 2) is always 0.

drag = False
a = []
n2 = 0      #n2 is for index (becomes two after first particle is picked)
ax = []
ay = []
az = []
BFieldArrow = []
BForceArrow = []
velArrow = []
BForce = []
BField = []
vel = []
angle = []
CurrentVel = None
showBArrow = False
showVArrow = False
showFArrow = False
showCoord = True

#-------------------------------------------------------------------------------
#---------------------------Drawing Functions-----------------------------------
#-------------------------------------------------------------------------------

# Returns the position of the charge.
def chargePos():
    nonlocal a, n2
    return a[n2 % 2].pos

#Draw a point and show the velocity, magnetic field, and magnetic force vector about that point
#Norm for drawing vectors is not used to illustrate the decreasing field strength as it gets further away from the wire
#param: r is a position vector at which the charge will be drawn. r needs to be specified for function calls without click events
def down(r):
    nonlocal drag, a, n2, justLoad
    if n2 > 0:
        #index -1 is allowed in python to access the last element
        a[(n2 % 2) - 1].visible = False
        removeOldArrows()
    if r != None:
        a[n2 % 2] = sphere(pos = r, size = vec(3, 3, 3), color = color.magenta)
        drawCoordinateLocator()
        drawArrows()
        n2 += 2
    else:
        a[n2 % 2] = sphere(pos = scene.mouse.pos, size = vec(3, 3, 3), color = color.magenta)
    drag = True

# Draws dotted lines to pinpoint the the location with respect to the axes
# Everytime a new point is clicked, lines are redrawn
def drawCoordinateLocator():
    nonlocal ax, ay, az, n2, a, showCoord
    if n2 > 0:
        ax[(n2 % 2) - 1].visible = False
        ay[(n2 % 2) - 1].visible = False
        az[(n2 % 2) - 1].visible = False
    ax[n2 % 2] = arrow(pos = vector(chargePos().x, 0, 0), axis = vector(0, chargePos().y, 0), 
                       shaftwidth = .5, headwidth = 0.1, headlength = 0.1, opacity = 0.25, color = color.red)
    ay[n2 % 2] = arrow(pos = vector(0, chargePos().y, 0), axis = vector(chargePos().x, 0, 0), 
                       shaftwidth = .5, headwidth = 0.1, headlength =0.1, opacity = 0.25, color = color.yellow)
    az[n2 % 2] = arrow(pos = vector(chargePos().x, chargePos().y, 0), axis = vector(0, 0, chargePos().z), 
                       shaftwidth = .5, headwidth = 0.1, headlength = 0.1, opacity = 0.25, color = color.green)
    if (!showCoord):
        ax[(n2 % 2)].visible = False
        ay[(n2 % 2)].visible = False
        az[(n2 % 2)].visible = False

# Draws Magnetic Field Vector, Magnetic Force Vector, Velocity Vector based on point clicked on canvas.
# If showVArrow, showBArrow, showFArrow are False, vectors will not be drawn.
# Everytime a new point is clicked, it replaces the old vector.
def drawArrows():
    nonlocal a, n2, ax, ay, az, BFieldArrow, BForceArrow, velArrow, vel, CurrentVel, angle
    if n2 > 0:
        removeOldArrows()
    vel[n2 % 2] = CurrentVel                                        # Put velocity value into holder
    BField[n2 % 2] = calculateBField(chargePos().x, chargePos().y)  # Calculate magnitude of magnetic field at point clicked by mouse
    # Calculate magnitude of magnetic force at point clicked by mouse due to charge q with velocity v
    # multiplied by 1/3 to shorten the vector
    BForce[n2 % 2] = calculateBForce(vel[n2 % 2], BField[n2 % 2]) * 1/3
    
    # Draw magnetic field vector
    BFieldArrow[n2 % 2] = arrow(pos = chargePos(), axis = BField[n2 % 2] , 
                                color = color.cyan, shaftwidth = 1.2, headwidth = 0, headlength =2)
    if (showBArrow == False):
        BFieldArrow[n2 % 2].visible = False                            
    
    # Draw magnetic force vector
    BForceArrow[n2 % 2] = arrow(pos = chargePos(), axis = BForce[n2 % 2],
                            color = color.orange, shaftwidth = 1.2, headwidth = 0, headlength =2)
    if (showFArrow == False):
        BForceArrow[n2 % 2].visible = False
                                
    # Draw velocity vector
    velArrow[n2 % 2] = arrow(pos = chargePos(), axis = vel[n2 % 2] , 
                        color = color.white, shaftwidth = 1.2, headwidth = 0, headlength =2)
    if (showVArrow == False):
        velArrow[n2 % 2].visible = False
    

# Moves point charge while the mouse is clicked and moving
def move():
    nonlocal drag, a, n2, ax, ay, az
    if drag:
        a[n2 % 2].pos = scene.mouse.pos
        ax[n2 % 2].pos = vec(chargePos().x ,0 , 0)
        ay[n2 % 2].pos = vec(0, chargePos().y, 0)
        az[n2 % 2].pos = vec(chargePos().x, chargePos().y, 0)
        ax[n2 % 2].axis = vec(0, chargePos().y, 0)
        ay[n2 % 2].axis = vec(chargePos().x, 0, 0)
        az[n2 % 2].axis = vec(0, 0, chargePos().z)
        
        
# Removes old vectors when clicking new points
def removeOldArrows():
    nonlocal n2
    BFieldArrow[(n2 % 2) - 1].visible = False
    BForceArrow[(n2 % 2) - 1].visible = False
    velArrow[(n2 % 2) - 1].visible = False

    
# Lets users pick a velocity from a defined set v1 - v5 (using radio buttons).
# When the canvas loads, v1 is automatically chosen.
def pickVel():
    nonlocal CurrentVel, justLoad, n2
    radVal = $('input:radio[name = vel]:checked').val()
    if !justLoad:
        if (radVal == "v1"):
            CurrentVel = vec(0,0,0)
        else if (radVal == "v2"):
            CurrentVel = vec(0,-5,0)
        else if (radVal == "v3"):
            CurrentVel = vec(5,0,0)
        else if (radVal == "v4"):
            CurrentVel = vec(0,0,5)
        else if (radVal == "v5"):
            CurrentVel = vec(5,-5,5)
        drawArrows()
        if n2 == 0:
            n2 += 2
    else:
        # if velocity is not defined, old points would not be erased when placing a new charge
        CurrentVel = vec(0,0,0)
        
        
        
#------------------------------------------------------------------    
#---------------------- SHOW/HIDE FUNCTIONS -----------------------
#------------------------------------------------------------------
#------------------------------------------------------------------    


# Shows/Hides the lines showing the location of the charge
def coordShow():
    nonlocal ax, ay, az, n2, showCoord
    if ($('#b1').text() == "Hide Axes"):
        showCoord = False
        ax[n2 % 2].visible = False
        ay[n2 % 2].visible = False
        az[n2 % 2].visible = False
        $('#b1').text("Show Axes")
        X_axis.visible = False
        Y_axis.visible = False
        Z_axis.visible = False
    else if ($('#b1').text() == "Show Axes"):
        showCoord = True
        ax[n2 % 2].visible = True
        ay[n2 % 2].visible = True
        az[n2 % 2].visible = True
        $('#b1').text("Hide Axes")
        X_axis.visible = True
        Y_axis.visible = True
        Z_axis.visible = True
        
#Shows/Hides the velocity vector
def showVel():
    nonlocal velArrow, n2, showVArrow
    if (!showVArrow):
        showVArrow = True
        velArrow[n2 % 2].visible = True
        $('#b2').text("Hide Velocity")
    else:
        showVArrow = False
        velArrow[n2 % 2].visible = False
        $('#b2').text("Show Velocity")
        
#Shows/Hides the B-field vector
def showB():
    nonlocal BFieldArrow, n2, showBArrow
    if (!showBArrow):
        BFieldArrow[n2 % 2].visible = True
        showBArrow = True
        $('#b3').text("Hide Magnetic Field at Location")
    else:
        showBArrow = False
        BFieldArrow[n2 % 2].visible = False
        $('#b3').text("Show Magnetic Field at Location")

#Shows/Hides the magnetic force vector
def showF():
    nonlocal BForceArrow, n2, showFArrow
    if (!showFArrow):
        showFArrow = True
        BForceArrow[n2 % 2].visible = True
        $('#b4').text("Hide Magnetic Force on Particle")
    else:
        showFArrow = False
        BForceArrow[n2 % 2].visible = False
        $('#b4').text("Show Magnetic Force on Particle")


#-------------------------------------------------------------------------------
#---------------------------Canvas Events---------------------------------------
#-------------------------------------------------------------------------------

scene.one("draw_complete", def():
    nonlocal justLoad
    #read note on pickVel()
    bind = pickVel()
    #place a charge on canvas load
    bind = down(vec(-10,-10,10))
    drawCoordinateLocator()
    justLoad = False
)


scene.bind("mousedown", def():
    down(None)
    drawCoordinateLocator()
)

#allows users to drag the point while left-clicking to move charge around
scene.bind("mousemove", def():
    nonlocal drag
    if drag:
        move()
)

scene.bind("mouseup", def():
    nonlocal drag
    drawArrows()
    drag = False
)
