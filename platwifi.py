import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

import os
import signal
import requests
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = 'platwifi'

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('icon.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    item_login = gtk.MenuItem('Login')
    item_login.connect('activate', login)
    item_logout = gtk.MenuItem('Logout')
    item_logout.connect('activate', logout)

    menu.append(item_login)
    menu.append(item_logout)
    menu.append(item_quit)
    menu.show_all()
    return menu

def login(source):
    requests.post('http://192.168.100.254/login', data={
        'username': os.getenv('wifiuser'),
        'password': os.getenv('wifipass')
    })

def logout(source):
    requests.post('http://192.168.100.254/logout')

def quit(source):
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()    
