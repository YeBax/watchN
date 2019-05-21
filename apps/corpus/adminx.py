import xadmin

from .models import QueAndAns, Tag, KeyWord, Tag2Question, Word2Tag, Collection


class QueAndAnsAdmin:
    show_bookmarks = False
    list_display = ['id', 'question', 'answer', 'create_time']  # 添加要显示的列
    list_filter = ['create_time']  # 要筛选的列
    search_fields = ['question', 'answer']  # 要查询的列
    show_detail_fields = ['question']  # 显示详情
    list_editable = ['question', 'answer']  # 列表中修改某个字段
    ordering = ["id"]
    # style_fields = {'answer': 'ueditor'}
    date_hierarchy = 'publication_date'


class TagAdmin:
    show_bookmarks = False
    list_display = ['id', 'tag', 'belong']
    list_filter = ['tag']
    list_editable = ['tag', 'belong']
    ordering = ["id"]


class Tag2QuestionAdmin:
    show_bookmarks = False
    list_display = ['id', 'tag', 'question']
    list_filter = ['tag']
    list_editable = ['tag', 'question']
    search_fields = ['question']
    ordering = ["id"]


class KeyWordAdmin:
    show_bookmarks = False
    list_display = ['id', 'word']
    list_editable = ['word']
    search_fields = ['word']
    ordering = ["-id"]


class Word2TagAdmin:
    show_bookmarks = False
    list_display = ['id', 'word', 'tag']
    list_editable = ['word', 'tag']
    search_fields = ['word', 'tag']
    ordering = ["-id"]


class CollectionAdmin:
    show_bookmarks = False
    list_display = ['id', 'questions', 'state', 'create_time']
    list_editable = ['state', 'create_time']
    search_fields = ['questions']
    list_filter = ['create_time', 'state']
    ordering = ["state"]

xadmin.site.register(QueAndAns, QueAndAnsAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Tag2Question, Tag2QuestionAdmin)
xadmin.site.register(KeyWord, KeyWordAdmin)
xadmin.site.register(Word2Tag, Word2TagAdmin)
xadmin.site.register(Collection, CollectionAdmin)
