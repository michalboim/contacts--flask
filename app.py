from flask import Flask, render_template, url_for, redirect, request
from classes import Contact
from function import create_contact, read_all_contacts, read_contact,delete_contact, update_contact, search_name


app = Flask(__name__)

@app.route('/')
def home():
    contacts_info=[]
    info=read_all_contacts('contact')
    for contact in info:
        contact=Contact(contact[1], contact[2], contact[3], contact[0])
        contacts_info.append(contact)
    return render_template('index.html', contacts_info=contacts_info)

@app.route('/create', methods=['get','post'])
def create():
    if request.method=='GET':
        return render_template('create.html')
    else:
        name=request.form['name'].title()
        email=request.form["email"].capitalize()
        phone=request.form['phone']
        contact=Contact(name, email, phone)
        create_contact("contact", "name, email, phone", f"'{contact.name}', '{contact.email}', '{contact.phone}'")
        return redirect ('/')


@app.route('/choose', methods=['post'])
def choose():
    tid=request.form['tid']
    info=read_contact('contact', tid)
    for contact in info:
        contact=Contact(contact[1], contact[2], contact[3], contact[0])
    return render_template('choose.html', contact=contact)

@app.route ('/delete', methods=['post'])
def delete():
    tid=request.form['tid_delete']
    delete_contact('contact', tid)
    return redirect(url_for('home'))

@app.route('/update', methods=['get','post'])
def update():
    if request.method=='POST':
        tid=request.form['tid_update']
        info=read_contact('contact', tid)
        for contact in info:
            contact=Contact(contact[1], contact[2], contact[3], contact[0])
            return render_template('update.html', contact=contact)
    else:
        tid=request.args['tid_update']
        name=request.args['name'].title()
        email=request.args["email"].capitalize()
        phone=request.args['phone']
        contact=Contact(name, email, phone,tid)
        update_contact("contact", "name, email, phone", f"'{contact.name}', '{contact.email}', '{contact.phone}'", tid)
        return redirect(url_for('home'))

@app.route('/go_home', methods=['get','post'])
def go_home():
    return redirect(url_for('home'))

@app.route('/search', methods=['get','post'])
def search():        
    if request.method=='GET':
        contacts_info=[]
        info=read_all_contacts('contact')
        for contact in info:
            contact=Contact(contact[1], contact[2], contact[3], contact[0])
            contacts_info.append(contact)
        return render_template('search.html', contacts_info=contacts_info)
    else:
        contacts_list=[]
        name=request.form["search_name"].title()
        search_contact=search_name('contact',name)
        for contact in search_contact:
            contact=Contact(contact[1], contact[2], contact[3], contact[0])
            contacts_list.append(contact)
        return render_template('search.html', contacts_list=contacts_list)





