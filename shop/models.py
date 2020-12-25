import uuid

from django.db import models


class Publisher(models.Model):
    """出版社モデル"""

    class Meta:
        db_table = 'publisher'
        verbose_name = verbose_name_plural = '出版社'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='出版社名', max_length=20)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    """著者モデル"""

    class Meta:
        db_table = 'author'
        verbose_name = verbose_name_plural = '著者'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='著者名', max_length=20)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    """本モデル"""

    class Meta:
        db_table = 'book'
        verbose_name = verbose_name_plural = '本'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', max_length=20, unique=True)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    publish_date = models.DateField(verbose_name='出版日', null=True, blank=True)
    publisher = models.ForeignKey(Publisher, verbose_name='出版社',
                                  on_delete=models.PROTECT, null=True, blank=True)
    authors = models.ManyToManyField(Author, verbose_name='著者', blank=True)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)

    def __str__(self):
        return self.title


class BookStock(models.Model):
    """本の在庫モデル"""

    class Meta:
        db_table = 'book_stock'
        verbose_name = verbose_name_plural = '在庫'

    book = models.OneToOneField(Book, verbose_name='本', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='在庫数', default=0)
