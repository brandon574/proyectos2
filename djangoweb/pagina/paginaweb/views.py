from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from paginaweb.models import usuarios
def index(request):
    return render(request, 'index.html')


def ingresar_usuario(request):
    nombres=request.POST['nombres']
    apellidos=request.POST['apellidos']
    correo=request.POST['correo_personal']
    curp=request.POST['curp']
    usuario=request.POST['tipo_usuario']
    contraseña=request.POST['nombres']+request.POST['apellidos']+request.POST['curp']
    correo_Asignado=request.POST['nombres']+(".")+request.POST['apellidos']+("@uaz.edu.co")
    correo_Asignado = correo_Asignado.replace(" ", ".")
    contraseña=contraseña.replace(" ", "")
    usuarios(nombres=nombres, apellidos=apellidos, correo=correo, curp=curp, usuario=usuario,contraseña=contraseña,correo_Asignado=correo_Asignado).save()
    
    try:
        
        reciving=correo_Asignado
        classing=usuarios.objects.get(correo_Asignado=reciving)
        dates=(classing.correo_Asignado)
        
        
    except:
        dates = reciving
       
       
    print(dates)
    
    try:
        
        reciving1=contraseña
        classed=usuarios.objects.get(contraseña=reciving1)
        datas=(classed.contraseña)
        
        
    except:
        datas = reciving1
       
       
    print(datas)



   
    
    return render(request,'retorno.html',{"reciving1":datas,"reciving":dates})
    
    

def recuperar_contraseña(request):
    curp = request.POST.get('curp')
    try:
        datos= curp
        clase=usuarios.objects.get(curp=datos)
        curp=(clase.contraseña)
    except:
        curp = curp
    print(curp)

    
    
    
    return render(request,'exeption.html',  {"contraseña" : curp})








    
    

     
    

    
    
    
    
    

    


