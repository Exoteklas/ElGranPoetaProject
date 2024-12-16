from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TicketSoporteForm
from .models import TicketSoporte
from django.contrib import messages
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User

# Create your views here.

@login_required
def crear_ticket_Jefe(request):
    if request.method == 'POST':
        form = TicketSoporteForm(request.POST)
        if form.is_valid():
            # Crear el objeto, pero no guardarlo en la base de datos todavía
            ticket = form.save(commit=False)
            # Asignar el usuario autenticado al ticket
            ticket.usuario = request.user
            # Guardar el ticket en la base de datos
            ticket.save()
            messages.success(request, "¡El ticket de soporte se ha creado exitosamente!")
            return redirect('jefe_bodega')  # Ajusta la redirección según tu lógica
    else:
        form = TicketSoporteForm()

    return render(request, 'crear_ticket_jefe.html', {'form': form})

@login_required
def crear_ticket_Bodeguero(request):
    if request.method == 'POST':
        form = TicketSoporteForm(request.POST)
        if form.is_valid():
            # Crear el objeto, pero no guardarlo en la base de datos todavía
            ticket = form.save(commit=False)
            # Asignar el usuario autenticado al ticket
            ticket.usuario = request.user
            # Guardar el ticket en la base de datos
            ticket.save()
            messages.success(request, "¡El ticket de soporte se ha creado exitosamente!")
            return redirect('bodeguero')  # Ajusta la redirección según tu lógica
    else:
        form = TicketSoporteForm()

    return render(request, 'crear_ticket_bodeguero.html', {'form': form})



@login_required
def detalle_ticket(request, ticket_id):
    ticket = get_object_or_404(TicketSoporte, id=ticket_id)

    # Si el formulario se envía (es decir, el botón "Ticket Realizado" fue presionado)
    if request.method == 'POST' and 'ticket_resuelto' in request.POST:
        ticket.estado = 'resuelto'  # Cambiar el estado a "Resuelto"
        ticket.fecha_resolucion = timezone.now()  # Actualizar la fecha de resolución
        ticket.save()  # Guardar los cambios
        return redirect('detalle_ticket', ticket_id=ticket.id)  # Redirigir al ticket actualizado

    return render(request, 'detalle_ticket.html', {'ticket': ticket})



# Formulario para la observación
class ObservacionForm(forms.ModelForm):
    class Meta:
        model = TicketSoporte
        fields = ['observacion']  # Solo el campo observación

@login_required
def detalle_ticket(request, ticket_id):
    ticket = get_object_or_404(TicketSoporte, id=ticket_id)
    form = ObservacionForm(request.POST or None, instance=ticket)

    # Manejo del formulario
    if request.method == 'POST':
        if 'ticket_resuelto' in request.POST and form.is_valid():
            ticket.estado = 'resuelto'
            ticket.fecha_resolucion = timezone.now()
            form.save()  # Guardar observación y cambios en el ticket
            return redirect('detalle_ticket', ticket_id=ticket.id)

    return render(request, 'detalle_ticket.html', {'ticket': ticket, 'form': form})



def ver_tickets(request):
    tickets = TicketSoporte.objects.all()
    return render(request, 'ver_tickets.html', {'tickets': tickets})



