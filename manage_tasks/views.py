from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
import json

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView
from .models import Task, Answers


class MainView(TemplateView):
    template_name = "task_main.html"

    def get(self, request):
        if request.user.is_authenticated:
            tasks = Task.objects.filter()
            ctx = {"tasks": tasks}
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})


class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = '/tasks/'
    template_name = "login.html"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("/tasks/")


class AddAnswerView(CreateView):
    fields = ["task"] + ["answer_" + str(i) for i in range(1, 28)]
    model = Answers
    success_url = "/tasks/result_answer"
    template_name = "add_answer.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        #self.object.task = Task.objects.get(title = self.object.task)
        self.object.save()
        return redirect(self.success_url)


class ResultView(TemplateView):
    template_name = "result_answer.html"

    def get(self, request):
        if request.user.is_authenticated:
            answers = Answers.objects.filter(author = request.user)
            answer_li = []
            names = ["Задание_" + str(i) for i in range(1, 28)]
            for ans in answers:
                tasks = Task.objects.get(id = ans.task.id)
                res = {}
                _list_ans = [ans.answer_1, ans.answer_2, ans.answer_3, ans.answer_4, ans.answer_5,
                         ans.answer_6, ans.answer_7, ans.answer_8, ans.answer_9, ans.answer_10,
                         ans.answer_11, ans.answer_12, ans.answer_13, ans.answer_14, ans.answer_15,
                         ans.answer_16, ans.answer_17, ans.answer_18, ans.answer_19, ans.answer_20,
                         ans.answer_21, ans.answer_22, ans.answer_23, ans.answer_24, ans.answer_25,
                         ans.answer_26, ans.answer_27]
                _list_res = [not_probel(tasks.task_1) == not_probel(ans.answer_1),
                not_probel(tasks.task_2) == not_probel(ans.answer_2),
                not_probel(tasks.task_3) == not_probel(ans.answer_3),
                not_probel(tasks.task_4) == not_probel(ans.answer_4),
                not_probel(tasks.task_5) == not_probel(ans.answer_5),
                not_probel(tasks.task_6) == not_probel(ans.answer_6),
                not_probel(tasks.task_7) == not_probel(ans.answer_7),
                not_probel(tasks.task_8) == not_probel(ans.answer_8),
                not_probel(tasks.task_9) == not_probel(ans.answer_9),
                not_probel(tasks.task_10) == not_probel(ans.answer_10),
                not_probel(tasks.task_11) == not_probel(ans.answer_11),
                not_probel(tasks.task_12) == not_probel(ans.answer_12),
                not_probel(tasks.task_13) == not_probel(ans.answer_13),
                not_probel(tasks.task_14) == not_probel(ans.answer_14),
                not_probel(tasks.task_15) == not_probel(ans.answer_15),
                not_probel(tasks.task_16) == not_probel(ans.answer_16),
                not_probel(tasks.task_17) == not_probel(ans.answer_17),
                not_probel(tasks.task_18) == not_probel(ans.answer_18),
                not_probel(tasks.task_19) == not_probel(ans.answer_19),
                not_probel(tasks.task_20) == not_probel(ans.answer_20),
                not_probel(tasks.task_21) == not_probel(ans.answer_21),
                not_probel(tasks.task_22) == not_probel(ans.answer_22),
                not_probel(tasks.task_23) == not_probel(ans.answer_23),
                not_probel(tasks.task_24) == not_probel(ans.answer_24),
                not_probel(tasks.task_25) == not_probel(ans.answer_25),
                not_probel(tasks.task_26) == not_probel(ans.answer_26),
                not_probel(tasks.task_27) == not_probel(ans.answer_27)
                ]
                count = 0
                for i in range(len(_list_res)):
                    if i == 25 or i == 26:
                        if _list_res[i]:
                            count += 2
                    else:
                        if _list_res[i]:
                            count += 1
                an = Ans(tasks.title, _list_ans, _list_res, count)
                answer_li.append(an)
            ctx = {"ans": answer_li, "names": names}

            print(ctx)
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})


def not_probel(_str):
    new_str = ""
    for i in str(_str):
        if i != " ":
            new_str += i
    return new_str


class Ans:
    def __init__(self, name_task, list_ans, list_res, itog):
        self.answers = list_ans
        self.results = list_res
        self.name = name_task
        self.itog = itog