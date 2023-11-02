from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from todo.models import Task
from todo.forms import TaskForm

 
 
def index(request: HttpRequest) -> HttpResponse:
 
    if request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
 
    form = TaskForm()
    tasks = Task.objects.all().order_by("-created")
 
    context = {"tasks": tasks, "form": form, "Status":Task.StatusChoice}
 
    return render(request, "index.html", context)

def update_task_status(
    request: HttpRequest, task_id: int, new_status: str
) -> HttpResponse:
 
    if not new_status in Task.StatusChoice.values:
        return HttpResponseBadRequest("Invalid status")
 
    task = get_object_or_404(Task, id=task_id)
 
    task.status = new_status
    task.save()
 
    success_url = reverse("index")
 
    return HttpResponseRedirect(success_url)