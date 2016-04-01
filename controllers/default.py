# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

import serial
import time
import sys

def index():         
    te = "??"
    hu = "??"
    
    exs = "??"   
     
    return dict(tempe=te, hume=hu, extra=exs)
    pass

def procesa():
	puerto = '/dev/ttyACM0'
	baudios = 115200
	timout = 1
	bits_datos = serial.EIGHTBITS # FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS
	paridad = serial.PARITY_NONE #PARITY_NONE, PARITY_EVEN, PARITY_ODD PARITY_MARK, PARITY_SPACE
	bits_stop = serial.STOPBITS_ONE #STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO

	try:
		ser = serial.Serial(puerto, 
							baudrate=baudios,
							timeout=0, 
							bytesize=bits_datos, 
							parity=paridad, 
							stopbits = bits_stop)

		#~ ser.reset_input_buffer()
		buff = ""
		
		response.flash="leyendo datos"
		
		c = ser.read()
		while c != '\n':
			#~ buff = buff + c
			c = ser.read()
			
		c = ser.read()
		while c != '\n':
			buff = buff + c
			c = ser.read()
		
		ser.close()

	except serial.serialutil.SerialException, mensaje:
		response.flash="error de comunicaciones"
		buff = "eee"
		#~ print mensaje
		#~ print "No se puede continuar con la ejecución"
		#raise SystemExit

	return buff

def form():
    form=FORM(TABLE(TR("puerto:",INPUT(_type="text",_name="puerto",requires=IS_NOT_EMPTY())),
                    TR("velocidad:",INPUT(_type="text",_name="baudrate",requires=IS_EMAIL())),
                    #~ TR("Admin",INPUT(_type="checkbox",_name="admin")),
                    #~ TR("Sure?",SELECT('yes','no',_name="sure",requires=IS_IN_SET(['yes','no']))),
                    #~ TR("Profile",TEXTAREA(_name="profile",value="write something here")),
                    TR("",INPUT(_type="submit",_value="SUBMIT"))))
    if form.accepts(request,session):
        response.flash="form accepted"
    elif form.errors:
        response.flash="form is invalid"
    else:
        response.flash="please fill the form"
    return dict(form=form,vars=form.vars)

def data():
    if not session.m or len(session.m)==10: session.m=[]
    if request.vars.q: session.m.append(request.vars.q)
    session.m.sort()
    return TABLE(*[TR(v) for v in session.m]).xml()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())




@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
