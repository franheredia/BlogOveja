from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from pagina.models import Entrada, Categoria, Comentario
from django.core.mail import send_mail

def home(request):
    context = RequestContext(request)
    posts = Entrada.objects.filter(publicado=True)
    return render_to_response('index.html', 
                              {'posts':posts},
                              context)
def broma(request):
    return render_to_response('proyecto.html',
                             {})
def proyectos(request):
    return render_to_response('proyectos.html',
                             {})
def curriculum(request):
    return render_to_response('curriculum.html',
                             {})
def cronometro(request):
    return render_to_response('cronometro.html',
                             {})
def conversor(request):
    return render_to_response('conversor.html',
                             {})
def contacto(request):
    context = RequestContext(request)
    if request.method=="POST":
        nombre = request.POST["nombre"]
        mensaje = request.POST["comentarios"]
        remitente = request.POST["email"]
        send_mail(str(nombre), str(mensaje), remitente,['franheredia.ov@gmail.com'],fail_silently=False)
    return render_to_response("contacto.html",
                             context)
def calculadora(request):
    return render_to_response('calculadora.html',
                             {})
def ver_post(request, id_post):
    context = RequestContext(request)
    post = Entrada.objects.get(id=id_post)
    if request.method=="POST":
        nick = request.POST["nombre"]
        contenido = request.POST["message"]
        entrada = Entrada.objects.get(id=id_post)
        comentario=Comentario()
        comentario.nick = nick
        comentario.contenido = contenido
        comentario.post = entrada
        comentario.save()
    comentarios = Comentario.objects.filter(post=id_post)    
    return render_to_response('post.html', 
                              {'post':post,
                              'comentarios':comentarios},
                              context)
def enviar_comentarios(request):
    context = RequestContext(request)
    if request.method=="POST":
        nick = request.POST["nombre"]
        contenido = request.POST["message"]
        entrada = Entrada.objects.get(id=request.POST['id'])
        comentario=Comentario()
        comentario.nick = nick
        comentario.contenido = contenido
        comentario.post = entrada
        comentario.save()
    comentarios = Comentario.objects.filter(post=request.POST['id'])    
    return render_to_response('comentarios.html', 
                              {'comentarios':comentarios},
                              context)