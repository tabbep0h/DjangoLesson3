from django.http import HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect,JsonResponse

def index(request):
    login = request.GET.get('login',"Undefined")
    if login != "Undefined" and login != "":
        password = request.GET.get('password', "Undefined")
    else:
        login = "Undefined"
        password = "Undefined"

    return HttpResponse(f"""<h2 style="font-family:Helvetica">Главная страница(Get запрос)</h2> 
                            <h2 style="font-family:Helvetica">Логин: {login}</h2>
                            <h2 style="font-family:Helvetica">Пароль: {password}</h2>"""
                        )

def popposts(request):
    return HttpResponse("Популярные посты")

def lastposts(request):
    return HttpResponse("Последние посты")

def allposts(request):
    return HttpResponse("Все посты")

def likecomm(request,id):
    likes = request.GET.get("likes",0)
    comments = request.GET.get("comments",0)
    return  HttpResponse(f"""<h1 style="font-family:Helvetica">Пост номер {id}</h1>
                             <h2 style="font-family:Helvetica">Лайки:{likes}<h2>
                             <h2 style="font-family:Helvetica">Комментарии:{comments}<h2>""")

def posts(request,id = 0):
    return HttpResponse(f"Пост номер {id}")

def about(request):
    return HttpResponseRedirect("/contacts")
def contacts(request):
    return HttpResponseRedirect("/about")
def err(request):
    return HttpResponse("<h1 >Загрузка страницы была завершена ошибкой</h1>",status = 404,)
def access(request):
    login = request.GET.get("login","Undefined")
    password = request.GET.get("password","Undefined")
    if login == "admin" and password == "admin":
        return HttpResponse(f"""
                                <h2 style="font-family:Helvetica">Логин:{login}<h2>
                                <h2 style="font-family:Helvetica">Пароль:{password}<h2>
                                <h2 style="font-family:Helvetica;color:green">Проходи,не задерживайся</h2>""")
    else:
        return HttpResponse(f"""<h2 style="font-family:Helvetica">Логин:{login}<h2>
                                <h2 style="font-family:Helvetica">Пароль:{password}<h2>
                                <h2 style="font-family:Helvetica:color:red">Доступ запрещен</h2>""")
def json(request):
    name = request.GET.get("name","Undefined")
    if name != "Undefined" and name != "":
        age = request.GET.get("age","Undefined")
    else:
        age = "Undefined"
        name = "Undefined"

    return JsonResponse({"name":name,"age":age})



