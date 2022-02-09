# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Imagetbl(models.Model):
    imageid = models.IntegerField(db_column='imageID', primary_key=True)  # Field name made lowercase.
    imagename = models.CharField(db_column='imageName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    recipeid = models.ForeignKey('Recipetbl', models.DO_NOTHING, db_column='recipeID', blank=True, null=True)  # Field name made lowercase.
    userrecipeid = models.ForeignKey('Userrecipetbl', models.DO_NOTHING, db_column='userRecipeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'imageTBL'


class Ingredienttbl(models.Model):
    ingrecode = models.IntegerField(db_column='ingreCode', primary_key=True)  # Field name made lowercase.
    ingrename = models.CharField(db_column='ingreName', max_length=20)  # Field name made lowercase.
    ingretype = models.CharField(db_column='ingreType', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ingredientTBL'


class Listtbl(models.Model):
    listid = models.IntegerField(db_column='listID', primary_key=True)  # Field name made lowercase.
    usercode = models.ForeignKey('Usertbl', models.DO_NOTHING, db_column='userCode', blank=True, null=True)  # Field name made lowercase.
    ingrecode = models.ForeignKey(Ingredienttbl, models.DO_NOTHING, db_column='ingreCode', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listTBL'


class Recipetbl(models.Model):
    recipeid = models.IntegerField(db_column='recipeID', primary_key=True)  # Field name made lowercase.
    recipename = models.CharField(db_column='recipeName', max_length=20)  # Field name made lowercase.
    recipedetail = models.TextField(db_column='recipeDetail')  # Field name made lowercase.
    recipetype = models.CharField(db_column='recipeType', max_length=5)  # Field name made lowercase.
    least = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipeTBL'


class Recipeingredienttbl(models.Model):
    recingid = models.IntegerField(db_column='recIngID', primary_key=True)  # Field name made lowercase.
    recipeid = models.ForeignKey(Recipetbl, models.DO_NOTHING, db_column='recipeID', blank=True, null=True)  # Field name made lowercase.
    ingrecode = models.ForeignKey(Ingredienttbl, models.DO_NOTHING, db_column='ingreCode', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(blank=True, null=True)
    recipetype = models.CharField(db_column='recipeType', max_length=3, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipeingredientTBL'


class Userrecipetbl(models.Model):
    userrecipeid = models.IntegerField(db_column='userRecipeID', primary_key=True)  # Field name made lowercase.
    usercode = models.ForeignKey('Usertbl', models.DO_NOTHING, db_column='userCode', blank=True, null=True)  # Field name made lowercase.
    recipename = models.CharField(db_column='recipeName', max_length=45)  # Field name made lowercase.
    recipedetail = models.TextField(db_column='recipeDetail')  # Field name made lowercase.
    recipetype = models.CharField(db_column='recipeType', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userRecipeTBL'


class Usertbl(models.Model):
    usercode = models.AutoField(db_column='userCode', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    useremail = models.CharField(db_column='userEmail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    userpassword = models.CharField(db_column='userPassword', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='userID', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userTBL'