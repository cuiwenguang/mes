from .models import Module, AccessModule


def get_modules(user, parent_id):
    '''获取用户可以操作的模块信息'''
    modules = []
    try:
        group_ids = user.groups.all().values_list('id')
        modules = Module.objects.filter(parent_id=parent_id, modules__group_id__in=group_ids)
    except Exception as e:
        print(e)

    return modules