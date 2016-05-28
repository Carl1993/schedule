from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Template, Context, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import auth
import datetime
from django import forms
from models import user, User
import MySQLdb
from mydb import *
# Create your views here.

def hello(request):
	return HttpResponse("hello, world!")


def main(request):
    return render_to_response('main.html')

def register(request):
    tip = ''
    if request.method == 'POST':
        post = request.POST
        try:
            user = User.objects.get(username = post['username'])
            if user is not None:
                tip = 'Username already exists!'
            else:
                tip = 'Unknown error'
        except:
            if post['password'] == post['passwd']:
                if post['password'] == '':
                    tip = 'The password can\'t be null'
                else:
                  #  try:
                        User.objects.create_user(username = post['username'], password = post['password'])
                        user = auth.authenticate(username = post['username'], password = post['password'])
                        auth.login(request, user)
                        db = connect_db()
                        #op_db(db, 'use mysite;')
                        cmd = 'insert into usr values (\"%s\",%s,\"%s\");' % (post['username'], post['usertype'], post['name'])
                        op_db(db, cmd)
                        close_db(db)
                        return HttpResponseRedirect('/main/')
                #    except:
                  #      tip = 'Invalid username'
            else:
                tip = 'Two password not the same'
    c = Context({'tip':tip})
    return render_to_response('register.html', c)


def login(request):
    tip = ''
    if request.user.is_authenticated():
        return HttpResponseRedirect('/main/')
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username = username, password = password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/main/')
        else:
            tip = 'username/password is incorrect!'
    c = Context({'tip': tip})
    return render_to_response('login.html', c)

def main(request):
    db = connect_db()
    user = request.user
    if user.is_authenticated():
        cmd = 'select usr_name, usr_type from usr where usr_id = \"%s\";' %user.username
        data = op_db(db, cmd)
        username = data[0][0]
        usertype = data[0][1]
        cmd = 'select od_date, start_time, end_time from on_duty where usr_id = \"%s\" and (od_date > current_date() or od_date = current_date() and end_time >= current_time()) limit 10;' %user.username
        data = op_db(db, cmd)
        data = [[str(data[j][i]) for i in xrange(len(data[j]))] for j in xrange(len(data))]
        print data
        '''for j in xrange(len(data)):
            for i in xrange(len(data[j])):
                data[j][i] = str(data[j][i])
        print data'''
        #data = tuple(data)
        c = Context({'username':username, 'usertype':usertype, 'on_duty':data})
        return render_to_response('main.html', c)
    return render_to_response('main.html')

def search(request):
    db = connect_db()
    user = request.user
    if user.is_authenticated():
        cmd = 'select usr_name, usr_type from usr where usr_id = \"%s\";' %user.username
        data = op_db(db, cmd)
        username = data[0][0]
        usertype = data[0][1]
        cmd = 'select usr_id, od_date, start_time, end_time from on_duty where (od_date > current_date() or od_date = current_date() and end_time >= current_time()) limit 10;'
        data = op_db(db, cmd)
        data = [[data[j][0]] + [str(data[j][i]) for i in xrange(1, len(data[j]))] for j in xrange(len(data))]
        '''for j in xrange(len(data)):
            for i in xrange(len(data[j])):
                data[j][i] = str(data[j][i])
        print data'''
        #data = tuple(data)
        c = Context({'username':username, 'usertype':usertype, 'on_duty':data})
        return render_to_response('search.html', c)
    return render_to_response('search.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('../')

def password(request):
    tip = ''
    if request.POST:
        post = request.POST
        user = request.user
        if user.is_authenticated():
            if auth.authenticate(username = user.username, password = post['prepasswd']) != None:
                if post['passwd'] == post['newpasswd']:
                    if post['passwd'] != '':
                        user.set_password(post['passwd'])
                        user.save()
                        auth.logout(request)
                        return HttpResponseRedirect('../')
                    else:
                        tip = 'New password can\'t be null!'
                else:
                    tip = 'New passwords are not same!'
            else:
                tip = 'Password is incorrect!'
    c = Context({'username': request.user.username, 'tip':tip})
    return render_to_response('change_password.html', c)