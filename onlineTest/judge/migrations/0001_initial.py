# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-05-15 18:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceProblem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='选择题ID')),
                ('title', models.CharField(max_length=200)),
                ('a', models.CharField(max_length=50)),
                ('b', models.CharField(max_length=50)),
                ('c', models.CharField(max_length=50)),
                ('d', models.CharField(max_length=50)),
                ('right_answer', models.CharField(max_length=1)),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='最后修改时间')),
                ('in_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '选择题',
                'ordering': ['id'],
                'verbose_name_plural': '选择题',
            },
        ),
        migrations.CreateModel(
            name='ClassName',
            fields=[
                ('name', models.CharField(max_length=30, verbose_name='课程名称')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'class_name',
                'verbose_name': '课程名称',
                'verbose_name_plural': '课程名称',
            },
        ),
        migrations.CreateModel(
            name='Compileinfo',
            fields=[
                ('solution_id', models.IntegerField(primary_key=True, serialize=False)),
                ('error', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'compileinfo',
            },
        ),
        migrations.CreateModel(
            name='GaicuoProblem',
            fields=[
                ('problem_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='题目id')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('input', models.TextField(blank=True, null=True, verbose_name='输入描述')),
                ('output', models.TextField(blank=True, null=True, verbose_name='输出描述')),
                ('program', models.TextField(blank=True, null=True, verbose_name='程序代码')),
                ('sample_input', models.TextField(blank=True, null=True, verbose_name='样例输入1')),
                ('sample_output', models.TextField(blank=True, null=True, verbose_name='样例输出1')),
                ('sample_input2', models.TextField(blank=True, null=True, verbose_name='样例输入2')),
                ('sample_output2', models.TextField(blank=True, null=True, verbose_name='样例输出2')),
                ('spj', models.CharField(default=0, max_length=1)),
                ('hint', models.TextField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('in_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='录入时间')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='最后修改时间')),
                ('time_limit', models.IntegerField(default=1, verbose_name='限制时间')),
                ('memory_limit', models.IntegerField(default=128, verbose_name='限制内存')),
                ('defunct', models.CharField(default='N', max_length=1)),
                ('accepted', models.IntegerField(blank=True, default=0, null=True, verbose_name='AC数量')),
                ('submit', models.IntegerField(blank=True, default=0, null=True, verbose_name='提交数量')),
                ('solved', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'gaicuoproblem',
                'verbose_name': '程序改错题',
                'ordering': ['problem_id'],
                'verbose_name_plural': '程序改错题',
            },
        ),
        migrations.CreateModel(
            name='KnowledgePoint1',
            fields=[
                ('name', models.CharField(max_length=20, verbose_name='一级知识点名称')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'knowledge_point_1',
                'verbose_name': '一级知识点',
                'verbose_name_plural': '一级知识点',
            },
        ),
        migrations.CreateModel(
            name='KnowledgePoint2',
            fields=[
                ('name', models.CharField(max_length=20, verbose_name='二级知识点名称')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'knowledge_point_2',
                'verbose_name': '二级知识点',
                'verbose_name_plural': '二级知识点',
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('problem_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='题目id')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('input', models.TextField(blank=True, null=True, verbose_name='输入描述')),
                ('output', models.TextField(blank=True, null=True, verbose_name='输出描述')),
                ('sample_input', models.TextField(blank=True, null=True, verbose_name='样例输入1')),
                ('sample_output', models.TextField(blank=True, null=True, verbose_name='样例输出1')),
                ('sample_input2', models.TextField(blank=True, null=True, verbose_name='样例输入2')),
                ('sample_output2', models.TextField(blank=True, null=True, verbose_name='样例输出2')),
                ('spj', models.CharField(default=0, max_length=1)),
                ('hint', models.TextField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('in_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='录入时间')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='最后修改时间')),
                ('time_limit', models.IntegerField(default=1, verbose_name='限制时间')),
                ('memory_limit', models.IntegerField(default=128, verbose_name='限制内存')),
                ('defunct', models.CharField(default='N', max_length=1)),
                ('accepted', models.IntegerField(blank=True, default=0, null=True, verbose_name='AC数量')),
                ('submit', models.IntegerField(blank=True, default=0, null=True, verbose_name='提交数量')),
                ('solved', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'problem',
                'verbose_name': '编程题',
                'ordering': ['problem_id'],
                'verbose_name_plural': '编程题',
            },
        ),
        migrations.CreateModel(
            name='Runtimeinfo',
            fields=[
                ('solution_id', models.IntegerField(primary_key=True, serialize=False)),
                ('error', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'runtimeinfo',
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('solution_id', models.AutoField(primary_key=True, serialize=False)),
                ('problem_id', models.IntegerField()),
                ('user_id', models.CharField(max_length=48)),
                ('time', models.IntegerField(default=0)),
                ('memory', models.IntegerField(default=0)),
                ('in_date', models.DateTimeField(auto_now_add=True)),
                ('result', models.SmallIntegerField(default=0)),
                ('language', models.IntegerField(default=0)),
                ('ip', models.CharField(max_length=15)),
                ('contest_id', models.IntegerField(blank=True, null=True)),
                ('valid', models.IntegerField(default=1)),
                ('num', models.IntegerField(default=-1)),
                ('code_length', models.IntegerField(default=0)),
                ('judgetime', models.DateTimeField(blank=True, null=True)),
                ('pass_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=2)),
                ('lint_error', models.IntegerField(default=0)),
                ('oi_info', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'solution',
            },
        ),
        migrations.CreateModel(
            name='SourceCode',
            fields=[
                ('solution_id', models.IntegerField(primary_key=True, serialize=False)),
                ('source', models.TextField()),
            ],
            options={
                'db_table': 'source_code',
            },
        ),
        migrations.CreateModel(
            name='SourceCodeUser',
            fields=[
                ('solution_id', models.IntegerField(primary_key=True, serialize=False)),
                ('source', models.TextField()),
            ],
            options={
                'db_table': 'source_code_user',
            },
        ),
        migrations.CreateModel(
            name='TiankongProblem',
            fields=[
                ('problem_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='题目id')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('input', models.TextField(blank=True, null=True, verbose_name='输入描述')),
                ('output', models.TextField(blank=True, null=True, verbose_name='输出描述')),
                ('program', models.TextField(blank=True, null=True, verbose_name='程序代码')),
                ('sample_input', models.TextField(blank=True, null=True, verbose_name='样例输入1')),
                ('sample_output', models.TextField(blank=True, null=True, verbose_name='样例输出1')),
                ('sample_input2', models.TextField(blank=True, null=True, verbose_name='样例输入2')),
                ('sample_output2', models.TextField(blank=True, null=True, verbose_name='样例输出2')),
                ('spj', models.CharField(default=0, max_length=1)),
                ('hint', models.TextField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('in_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='录入时间')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='最后修改时间')),
                ('time_limit', models.IntegerField(default=1, verbose_name='限制时间')),
                ('memory_limit', models.IntegerField(default=128, verbose_name='限制内存')),
                ('defunct', models.CharField(default='N', max_length=1)),
                ('accepted', models.IntegerField(blank=True, default=0, null=True, verbose_name='AC数量')),
                ('submit', models.IntegerField(blank=True, default=0, null=True, verbose_name='提交数量')),
                ('solved', models.IntegerField(blank=True, null=True)),
                ('classname', models.ManyToManyField(to='judge.ClassName', verbose_name='所属课程')),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('knowledgePoint1', models.ManyToManyField(to='judge.KnowledgePoint1', verbose_name='一级知识点')),
                ('knowledgePoint2', models.ManyToManyField(to='judge.KnowledgePoint2', verbose_name='二级知识点')),
            ],
            options={
                'db_table': 'tiankongproblem',
                'verbose_name': '程序填空题',
                'ordering': ['problem_id'],
                'verbose_name_plural': '程序填空题',
            },
        ),
    ]
