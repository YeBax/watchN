from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class QueAndAns(models.Model):
    """
    语料
    问题 与 答案
    """
    question = models.CharField(max_length=100, verbose_name="标准问题", default="")
    answer = models.TextField(max_length=300, verbose_name="标准回答", default="")
    # answer = UEditorField(verbose_name="标准回答", height=500, width=950, default='', toolbars='full',
    #                       imagePath='images/answer/%(basename)s_%(datetime)s.%(extname)s',
    #                       filePath='files/answer/%(basename)s_%(datetime)s.%(extname)s',
    #                       upload_settings={'imageMaxSize': 1204000}, help_text='富文本编辑框，上传文件和图片10MB以下')
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    class Meta:
        verbose_name = "问答语料"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Tag(models.Model):
    """
    标签的类别
    建议设置 大类别 和 子类别
    不要有过多的层级
    """
    tag = models.CharField(max_length=20, verbose_name="标签名称", unique=True)
    belong = models.ForeignKey('self', verbose_name="上一级标签名称", on_delete=models.CASCADE, null=True, blank=True,
                               related_name='belong_tag',
                               help_text='选择上一级类别，不选择为最高类别')

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag


class Tag2Question(models.Model):
    """
    问题标签映射
    """
    tag = models.ForeignKey(Tag, verbose_name='标签名称',
                            on_delete=models.CASCADE)
    question = models.ForeignKey(QueAndAns, verbose_name='标准问题', related_name='question_classification',
                                 unique=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "问题标签映射"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '【{type_name}】{question}'.format(type_name=self.tag, question=self.question)


class KeyWord(models.Model):
    """
    关键词
    """
    word = models.CharField(max_length=50, verbose_name="关键词", unique=True)

    class Meta:
        verbose_name = "关键词"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.word


class Word2Tag(models.Model):
    """
    关键词映射
    """
    word = models.ForeignKey(KeyWord, verbose_name='关键词', related_name='word2tag_word', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, verbose_name='关键词', related_name='word2tag_tag', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "关键词映射"
        verbose_name_plural = verbose_name
        unique_together = ('word', 'tag')

    def __str__(self):
        return "%s-%s" % (self.tag, self.word)


class Collection(models.Model):
    """
    问题收集
    收集没有匹配到的问题
    """
    UNKNOWN_STATE = [
        (0, "未解决"),
        (1, "已解决"),
        (2, "无效问题")
    ]
    questions = models.TextField(max_length=300, verbose_name="未知问题", default="")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    state = models.IntegerField(verbose_name="解决状态", choices=UNKNOWN_STATE, default=0)

    class Meta:
        verbose_name = "问题收集"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.questions
