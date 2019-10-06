class Template:
    default_template_name = 'model'
    template_name = None
    template_name_suffix = '_list'
    context = None

    def __init__(self,*arg,**kwargs):
        self.kwargs = kwargs
        print(self.kwargs)

    def get_template_name(self):
        if self.template_name is None:
            template_name = self.default_template_name + self.template_name_suffix +'.html'
        if self.template_name is not None:
            template_name = self.template_name
        return template_name


    def render(self):
        render_template = self.get_template_name()
        context_data = self.get_context()
        data = {"template":render_template , "context":context_data}
        return self.print_all_data(**data)

    def get_context(self):
        if self.context == None:
            context = {'pk':self.kwargs.get('pk')}
        elif type(self.context) != dict:
            raise TypeError("Context should be a dictionary")
        else:
            context = self.context
        return context

    def print_all_data(self,template,context):
        print("template", template , ":context" , context)

class MyTemplate(Template):
    pass


class myytemplate(MyTemplate):
    template_name = 'mymodel.html'
    #overriding the context
    def get_context(self):
        context = super(myytemplate,self).get_context()
        context_data = {'name':'Areeba' , 'age':100}
        context.update(context_data)
        return context
    

for i in range(1,5):
    view = myytemplate(pk = i)  #pk is changing again and again that's why it is good to deal with is as a instance variable
    view.render()   #template is constant for all pk that's why better way to declare is as a Class variable





