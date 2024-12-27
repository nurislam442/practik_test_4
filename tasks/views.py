from django.shortcuts import render, redirect
from tasks.models import Task
from tasks.forms import SearchForm, Post_Form
# Create your views here.
def base_view(request):
    return render(request, "base.html")

def ListView(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        search = request.GET.get("search")
        category = request.GET.get("category")
        ordering = request.GET.get("ordering")
        form = SearchForm(request.GET)
        if search:
            tasks = tasks.filter(title__icontains=search)
        if category:
            tasks = tasks.filter(category_id=category)
        if ordering:
            tasks = tasks.order_by(ordering)
        context = {"tasks": tasks, "form":form}
        return render(request, "tasks/TaskList.html", context=context)
def detail_view(request, id):
    tasks = Task.objects.get(id=id)
    context = {"tasks": tasks}
    return render(request, "tasks/TaskDetail.html", context=context)

def create_task(request):
    if request.method == "GET":
        form = Post_Form()
        return render(request, "tasks/task_create.html", context={"form":form})
    if request.method == "POST":
        form = Post_Form(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "tasks/task_create.html", context={"form":form})
        elif form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            task = Task.objects.create(title=title, content=content)
            return redirect("/posts/")
