from django.shortcuts import render, redirect

from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    response = requests.get('https://Jorgejfs78.pythonanywhere.com/livros/')
    livros = response.json() 
    context = {
        'livros' : livros
    }   
    return render(request, 'index.html', context)
def adicionar(request):
    if request.method == "POST":
        dados = request.POST
        novo_livro = {
            "titulo": dados ["titulo"],
            "autor": dados ["autor"],
            "ano_lancamento": dados ["ano_lancamento"],
            "estado": dados ["estado"],
            "paginas": dados ["paginas"],
            "editora": dados ["editora"],
            "imagem": dados["imagem"]
        }
        post_response = requests.post('https://Jorgejfs78.pythonanywhere.com/livros/', json=novo_livro)
        return redirect("index")
    
    context = {}
    return render(request, 'adicionar.html', context)

def editar(request, id):
    if request.method == "POST":
        dados = request.POST
        livro_atualizado = {
            "titulo": dados["titulo"],
            "autor": dados["autor"],
            "ano_lancamento": dados["ano_lancamento"],
            "estado": dados["estado"],
            "paginas": dados["paginas"],
            "editora": dados["editora"],
            "imagem": dados["imagem"]
        }
        url = f"https://Jorgejfs78.pythonanywhere.com/livros/{id}/"
        put_response = requests.put(url, data=livro_atualizado)
        return redirect("index")

    url = f"https://Jorgejfs78.pythonanywhere.com/livros/{id}/"
    get_response = requests.get(url)
    livro = get_response.json()

    context = {
        "livro": livro
    }
    return render(request, 'editar.html', context)

def deletar(request, id):
    delete_url = f"https://Jorgejfs78.pythonanywhere.com/livros/{id}/"
    delete_response = requests.delete(delete_url)
    return redirect("index")