## How to integrate Django with a legacy database

Suppose you have an existing (possibly legacy) database, and you want a django project to be able to use. Django has provided some utilities to automate this process as much as possible.

- After you've set up the django project, connect it to your desired database by updating the DATABASES config variable in settings.py

(I used a simple sqlite database with <b>Product</b> table from my previous howto summary "Providing initial data for models".)

- Call <b>inspectdb</b> command
```
> python manage.py inspectdb
```
This command will inspect the database and attempts to re-build the models.<br>
- Calling the <b>inspect</b> command with no args will only output the result in terminal.<br>
To save this result into a file (provide a name of your choosing):
```
> python manage.py inspectdb > <inspected_models.py>
```
- There are some manual actions to take on this generated file that worth mentioning:
1. Rearrange the models if you need to.
2. Make sure each model has one field with primary_key=True
3. Make sure each ForeignKey and OneToOneField has <b>on_delete</b>
4. Remove <b>managed = False</b> on tables that you wish django to control.<br>
The default value for this field is True, if it is set to False, django will include it in migration file but not in the actual migration.

- Model can be renamed, but not db_table and field names.

- you can copy paste the models you want to your app/models.py.
(I copied )