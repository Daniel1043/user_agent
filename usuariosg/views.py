from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_user_agents.utils import get_user_agent
from django.shortcuts import render





def index(request):
    
    return render(request, 'info/user-agent.html')


def my_view(request):

    # Let's assume that the visitor uses an iPhone...
    request.user_agent.is_mobile # returns True
    request.user_agent.is_tablet # returns False
    request.user_agent.is_pc # returns False
    request.user_agent.is_bot # returns False
    request.user_agent.is_touch_capable # returns True

    # Accessing user agent's browser attributes
    request.user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
    request.user_agent.browser.family  # returns 'Mobile Safari'
    request.user_agent.browser.version  # returns (5, 1)
    request.user_agent.browser.version_string   # returns '5.1'

    # Operating System properties
    request.user_agent.os  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
    request.user_agent.os.family  # returns 'iOS'
    request.user_agent.os.version  # returns (5, 1)
    request.user_agent.os.version_string  # returns '5.1'

    # Device properties
    request.user_agent.device  # returns Device(family='iPhone')
    request.user_agent.device.family  # returns 'iPhone'
    
def obtener_info_cliente(request):
    # Obtén el nombre del host del cliente
    client_host = request.get_host()

    # Obtén la dirección IP del cliente
    client_ip = request.META.get('REMOTE_ADDR')



    return render(request, 'info/user-agent.html',{ 'client_host': client_host,'client_ip': client_ip})