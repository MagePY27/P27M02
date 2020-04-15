#### 简单的用户管理系统实现用户的增删改查(CBV)

>urls.py
```python
app_name = 'hello'
urlpatterns = [
    path('', views.UserList.as_view(), name='UserList'),
    path('useradd/', views.UserAdd.as_view(), name='UserAdd'),
    # pk 为主键，update根据主键检索数据
    re_path('(?P<pk>[0-9]+)/userupdate/', views.UserUpdate.as_view(), name='UserModify'),
    re_path('(?P<pk>[0-9]+)/userdel/', views.UserDel.as_view(), name='UserDel'),
    re_path('(?P<pk>[0-9]+)/userdetail',views.UserDetail.as_view(), name='UserDetail')
]
```
>views.py
```python
# 创建数据视图
class UserAdd(SuccessMessageMixin,CreateView):
    #get 请求渲染的模板
    template_name = 'hello/UserAdd.html'
    # 数据库类
    model = User
    # 数据库字段名称
    fields = ('name', 'password', 'sex')
    success_message = "%(name)s was created successfully"

    # 成功后跳转
    def get_success_url(self):
        if '_addanother' in self.request.POST:
            return reverse('hello:UserAdd')
        return reverse('hello:UserList')


class UserList(ListView):
    template_name = "hello/UserList.html"
    context_object_name = 'users'
    model = User
    keyword = ""

    # 用户过滤
    def get_queryset(self):
        queryset = super().get_queryset()
        self.keyword = self.request.GET.get("keyword","")
        if self.keyword:
            queryset = queryset.filter(name__icontains=self.keyword)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['keyword'] = self.keyword
        return context

    def get_success_url(self):
        return reverse('hello:index')


class UserUpdate(UpdateView):
    template_name = "hello/UserUpdate.html"
    model = User
    fields = ('name', 'password', 'sex')
    context_object_name = 'users'

    def get_success_url(self):
        return reverse('hello:UserList')


class UserDel(DeleteView):
    template_name = "hello/UserDel.html"
    model = User

    def get_success_url(self):
        return reverse('hello:UserList')


class UserDetail(DetailView):
    template_name = 'hello/UserDetail.html'
    model = User

```
>实现效果
##### List
![f502478aaf57beca2990bf2f8e111edb](DAY03.resources/B6E71453-654A-40A3-B935-B5543B6BFE0C.png)
##### Add
![a0f99fe3b8079077d4f9d9878d413d09](DAY03.resources/76F4A228-D3DF-481F-8962-65B26ED43416.png)
![d0a3c50d13576f602fbee7cbaee96fc9](DAY03.resources/78DC4E6E-702E-4A99-805B-DE0754738E6C.png)

##### Update
![61a17579afb745a17bcda53434a99fa1](DAY03.resources/7B2366E4-7EAD-430E-9C72-EBA7A023EED3.png)
![9eb70ab41881fab72a256e9d93338a5b](DAY03.resources/B2F2CE8B-C2FE-4A27-A60F-0C07D8C38997.png)
##### Delete
![9fada4b5bac1c6ab8b7f9287a34453a8](DAY03.resources/8969C216-DA3A-4342-96BF-8011F25F8F50.png)

![f03249deedaa5269aa3148a5849ebcee](DAY03.resources/09F89CD9-E0AF-45C2-AC38-364AC45E1A0C.png)



