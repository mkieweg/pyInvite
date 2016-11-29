import sendInvite
import cProfile


def impacket_testrun():
    si = sendInvite.SendInvite()
    si.fire("10.0.2.6")


cProfile.run('impacket_testrun()')
