import Server.data
import Server.register
import threading
import Server.fire

r = Server.register.Register()
f = Server.fire.Fire()


def register_thread():
    while 1:
        r.register()


def fire_thread():
    while 1:
        if Server.data.adresses.__len__() > 0:
            for address in Server.data.adresses:
                f.fire(address, 0x000111000)
                print("Fired against " % address)


register_thread_init = threading.Thread(target=register_thread())
fire_thread_init = threading.Thread(target=fire_thread())
register_thread_init.start()
fire_thread_init.start()
