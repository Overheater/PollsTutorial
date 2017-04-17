{"changed":true,"filter":false,"title":"views.py","tooltip":"/polls/views.py","value":"from django.shortcuts import render,get_object_or_404\nfrom django.http import HttpResponse,HttpResponseRedirect\nfrom django.core.urlresolvers import reverse\nfrom django.http import Http404\nfrom django.views import generic\nfrom django.template import loader\nfrom .models import Choice,Question\n# Create your views here.\nclass IndexView(generic.ListView):\n    template_name = 'polls/index.html'\n    context_object_name = 'latest_question_list'\n\n    def get_queryset(self):\n        \"\"\"Return the last five published questions.\"\"\"\n        return Question.objects.order_by('-pub_date')[:5]\n\n\nclass DetailView(generic.DetailView):\n    model = Question\n    template_name = 'polls/detail.html'\n\n\nclass ResultsView(generic.DetailView):\n    model = Question\n    template_name = 'polls/results.html'\n\n\ndef vote(request, question_id):\n    question = get_object_or_404(Question, pk=question_id)\n    try:\n        selected_choice = question.choice_set.get(pk=request.POST['choice'])\n    except (KeyError, Choice.DoesNotExist):\n        # Redisplay the question voting form.\n        return render(request, 'polls/detail.html', {\n            'question': question,\n            'error_message': \"You didn't select a choice.\",\n        })\n    else:\n        selected_choice.votes += 1\n        selected_choice.save()\n        # Always return an HttpResponseRedirect after successfully dealing\n        # with POST data. This prevents data from being posted twice if a\n        # user hits the Back button.\n        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))","undoManager":{"mark":96,"position":100,"stack":[[{"start":{"row":11,"column":0},"end":{"row":16,"column":71},"action":"remove","lines":["def detail(request, question_id):","    try:","        question = Question.objects.get(pk=question_id)","    except Question.DoesNotExist:","        raise Http404(\"Question does not exist\")","    return render(request, 'polls/detail.html', {'question': question})"],"id":230},{"start":{"row":11,"column":0},"end":{"row":13,"column":71},"action":"insert","lines":["def detail(request, question_id):","    question = get_object_or_404(Question, pk=question_id)","    return render(request, 'polls/detail.html', {'question': question})"]}],[{"start":{"row":19,"column":0},"end":{"row":20,"column":70},"action":"remove","lines":["def vote(request, question_id):","    return HttpResponse(\"You're voting on question %s.\" % question_id)"],"id":231},{"start":{"row":19,"column":0},"end":{"row":35,"column":82},"action":"insert","lines":["def vote(request, question_id):","    question = get_object_or_404(Question, pk=question_id)","    try:","        selected_choice = question.choice_set.get(pk=request.POST['choice'])","    except (KeyError, Choice.DoesNotExist):","        # Redisplay the question voting form.","        return render(request, 'polls/detail.html', {","            'question': question,","            'error_message': \"You didn't select a choice.\",","        })","    else:","        selected_choice.votes += 1","        selected_choice.save()","        # Always return an HttpResponseRedirect after successfully dealing","        # with POST data. This prevents data from being posted twice if a","        # user hits the Back button.","        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))"]}],[{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"insert","lines":["C"],"id":232}],[{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":["h"],"id":233}],[{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["o"],"id":234}],[{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"insert","lines":["i"],"id":235}],[{"start":{"row":4,"column":20},"end":{"row":4,"column":24},"action":"remove","lines":["Choi"],"id":236},{"start":{"row":4,"column":20},"end":{"row":4,"column":26},"action":"insert","lines":["Choice"]}],[{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"insert","lines":[","],"id":237}],[{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"insert","lines":[","],"id":238}],[{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"insert","lines":["h"],"id":239}],[{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"insert","lines":["t"],"id":240}],[{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"insert","lines":["t"],"id":241}],[{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"insert","lines":["p"],"id":242}],[{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"insert","lines":["r"],"id":243}],[{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"insert","lines":["e"],"id":244}],[{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"remove","lines":["e"],"id":245}],[{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"remove","lines":["r"],"id":246}],[{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"remove","lines":["p"],"id":247}],[{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"remove","lines":["t"],"id":248}],[{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"insert","lines":["t"],"id":249}],[{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"remove","lines":["t"],"id":250}],[{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"remove","lines":["t"],"id":251}],[{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"remove","lines":["h"],"id":252}],[{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"insert","lines":["H"],"id":253}],[{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"insert","lines":["t"],"id":254}],[{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"insert","lines":["t"],"id":255}],[{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"insert","lines":["p"],"id":256}],[{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"insert","lines":["R"],"id":257}],[{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"insert","lines":["s"],"id":258}],[{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"remove","lines":["s"],"id":259}],[{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"insert","lines":["e"],"id":260}],[{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"insert","lines":["s"],"id":261}],[{"start":{"row":1,"column":44},"end":{"row":1,"column":45},"action":"insert","lines":["p"],"id":262}],[{"start":{"row":1,"column":45},"end":{"row":1,"column":46},"action":"insert","lines":["o"],"id":263}],[{"start":{"row":1,"column":46},"end":{"row":1,"column":47},"action":"insert","lines":["n"],"id":264}],[{"start":{"row":1,"column":47},"end":{"row":1,"column":48},"action":"insert","lines":["s"],"id":265}],[{"start":{"row":1,"column":48},"end":{"row":1,"column":49},"action":"insert","lines":["e"],"id":266}],[{"start":{"row":1,"column":49},"end":{"row":1,"column":50},"action":"insert","lines":["r"],"id":267}],[{"start":{"row":1,"column":49},"end":{"row":1,"column":50},"action":"remove","lines":["r"],"id":268}],[{"start":{"row":1,"column":49},"end":{"row":1,"column":50},"action":"insert","lines":["R"],"id":269}],[{"start":{"row":1,"column":37},"end":{"row":1,"column":50},"action":"remove","lines":["HttpResponseR"],"id":270},{"start":{"row":1,"column":37},"end":{"row":1,"column":57},"action":"insert","lines":["HttpResponseRedirect"]}],[{"start":{"row":1,"column":57},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":271}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["d"],"id":272}],[{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["j"],"id":273}],[{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["a"],"id":274}],[{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["n"],"id":275}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":["g"],"id":276}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":5},"action":"remove","lines":["djang"],"id":277},{"start":{"row":2,"column":0},"end":{"row":2,"column":6},"action":"insert","lines":["django"]}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"remove","lines":["o"],"id":278}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"remove","lines":["g"],"id":279}],[{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"remove","lines":["n"],"id":280}],[{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"remove","lines":["a"],"id":281}],[{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"remove","lines":["j"],"id":282}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"remove","lines":["d"],"id":283}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["f"],"id":284}],[{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["r"],"id":285}],[{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["o"],"id":286}],[{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["m"],"id":287}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":[" "],"id":288}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["d"],"id":289}],[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["j"],"id":290}],[{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["a"],"id":291}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":8},"action":"remove","lines":["dja"],"id":292},{"start":{"row":2,"column":5},"end":{"row":2,"column":11},"action":"insert","lines":["django"]}],[{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["."],"id":293}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["c"],"id":294}],[{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["o"],"id":295}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":14},"action":"remove","lines":["co"],"id":296},{"start":{"row":2,"column":12},"end":{"row":2,"column":16},"action":"insert","lines":["conf"]}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"remove","lines":["f"],"id":297}],[{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"remove","lines":["n"],"id":298}],[{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["r"],"id":299}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["e"],"id":300}],[{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["."],"id":301}],[{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["u"],"id":302}],[{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":["r"],"id":303}],[{"start":{"row":2,"column":17},"end":{"row":2,"column":19},"action":"remove","lines":["ur"],"id":304},{"start":{"row":2,"column":17},"end":{"row":2,"column":29},"action":"insert","lines":["urlresolvers"]}],[{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":[" "],"id":305}],[{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"insert","lines":["i"],"id":306}],[{"start":{"row":2,"column":31},"end":{"row":2,"column":32},"action":"insert","lines":["m"],"id":307}],[{"start":{"row":2,"column":30},"end":{"row":2,"column":32},"action":"remove","lines":["im"],"id":308},{"start":{"row":2,"column":30},"end":{"row":2,"column":36},"action":"insert","lines":["import"]}],[{"start":{"row":2,"column":36},"end":{"row":2,"column":37},"action":"insert","lines":[" "],"id":309}],[{"start":{"row":2,"column":37},"end":{"row":2,"column":38},"action":"insert","lines":["r"],"id":310}],[{"start":{"row":2,"column":38},"end":{"row":2,"column":39},"action":"insert","lines":["e"],"id":311}],[{"start":{"row":2,"column":39},"end":{"row":2,"column":40},"action":"insert","lines":["v"],"id":312}],[{"start":{"row":2,"column":40},"end":{"row":2,"column":41},"action":"insert","lines":["e"],"id":313}],[{"start":{"row":2,"column":41},"end":{"row":2,"column":42},"action":"insert","lines":["r"],"id":314}],[{"start":{"row":2,"column":37},"end":{"row":2,"column":42},"action":"remove","lines":["rever"],"id":315},{"start":{"row":2,"column":37},"end":{"row":2,"column":46},"action":"insert","lines":["reverse()"]}],[{"start":{"row":2,"column":45},"end":{"row":2,"column":46},"action":"remove","lines":[")"],"id":316}],[{"start":{"row":2,"column":44},"end":{"row":2,"column":45},"action":"remove","lines":["("],"id":317}],[{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"insert","lines":[","],"id":318}],[{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"insert","lines":["g"],"id":319}],[{"start":{"row":0,"column":37},"end":{"row":0,"column":38},"action":"insert","lines":["e"],"id":320}],[{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"insert","lines":["t"],"id":321}],[{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"remove","lines":["t"],"id":322}],[{"start":{"row":0,"column":37},"end":{"row":0,"column":38},"action":"remove","lines":["e"],"id":323}],[{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"remove","lines":["g"],"id":324},{"start":{"row":0,"column":36},"end":{"row":0,"column":55},"action":"insert","lines":["get_object_or_404()"]}],[{"start":{"row":0,"column":54},"end":{"row":0,"column":55},"action":"remove","lines":[")"],"id":325}],[{"start":{"row":0,"column":53},"end":{"row":0,"column":54},"action":"remove","lines":["("],"id":326}],[{"start":{"row":16,"column":0},"end":{"row":18,"column":47},"action":"remove","lines":["def results(request, question_id):","    response = \"You're looking at the results of question %s.\"","    return HttpResponse(response % question_id)"],"id":327},{"start":{"row":16,"column":0},"end":{"row":18,"column":72},"action":"insert","lines":["def results(request, question_id):","    question = get_object_or_404(Question, pk=question_id)","    return render(request, 'polls/results.html', {'question': question})"]}],[{"start":{"row":3,"column":31},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":328}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":32},"action":"insert","lines":["from django.views import generic"],"id":329}],[{"start":{"row":8,"column":0},"end":{"row":21,"column":31},"action":"remove","lines":["def index(request):","    latest_question_list = Question.objects.order_by('-pub_date')[:5]","    context = {'latest_question_list': latest_question_list}","    return render(request, 'polls/index.html', context)","    ","def detail(request, question_id):","    question = get_object_or_404(Question, pk=question_id)","    return render(request, 'polls/detail.html', {'question': question})","","def results(request, question_id):","    question = get_object_or_404(Question, pk=question_id)","    return render(request, 'polls/results.html', {'question': question})","","def vote(request, question_id):"],"id":330},{"start":{"row":8,"column":0},"end":{"row":27,"column":31},"action":"insert","lines":["class IndexView(generic.ListView):","    template_name = 'polls/index.html'","    context_object_name = 'latest_question_list'","","    def get_queryset(self):","        \"\"\"Return the last five published questions.\"\"\"","        return Question.objects.order_by('-pub_date')[:5]","","","class DetailView(generic.DetailView):","    model = Question","    template_name = 'polls/detail.html'","","","class ResultsView(generic.DetailView):","    model = Question","    template_name = 'polls/results.html'","","","def vote(request, question_id):"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":27,"column":31},"end":{"row":27,"column":31},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1492370232688}