from django.shortcuts import render,redirect
from django.views import View
from ChefGenAI.forms import RecipeForm
from ChefGenAI.langchain import askGenChef
class Home(View):
    def get(self,request):
        ai_recipe=request.session.get('ai_recipe','')
        form=RecipeForm()
        return render(request,'ChefGenAI\home.html',{'form':form,'ai_recipe':ai_recipe})
    
    def post(self,request):
        form=RecipeForm(request.POST)
        if form.is_valid():
            recipe_message=form.cleaned_data['recipe_message']
            ai_res_recipe=askGenChef(recipe_message)
            request.session['ai_recipe']=ai_res_recipe
            print(recipe_message)
        form=RecipeForm()
        return redirect('/')

# Create your views here.

