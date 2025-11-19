## Providing initial data for models

It's often useful to prepopulate database with hard-coded data when setting up a new app or project.<br>
This can be done using <u><b>migrations</b></u> or <u><b>fixtures</b></u>.


### 1. Using Data Migrations:

Data migrations: as well as changing db schema, migrations can also be instructed to change the data in db itself,
in conjunction with the schema.

These migrations that alter the data as well, are called data migrations.
they cannot be made automatically.
they are made of Operation objects classes. one of them is RunPython.

(for this example, i created the shop app)
```
> python manage.py startapp shop
```
- Then add it to INSTALLED_APPS.<br>

now we need a sample model, i will name mine Product. after adding the sample model, create a migration for it.

ok, now the actual process of this howto guide starts.
- generate a new empty migration file:
```
> python manage.py makemigrations --empty <appName>
```

In this migration file, we see a Migration class.

This class has two class attributes named <b>dependencies</b>and <b>operations</b>.
We'll leave dependencies (not currently relevant).
We'll need the operations. in data migration <b>RunPython</b> is used to run python code for each migration file.
We need to pass a callable to RunPython and add it to the list of operations.<br>
We added a simple function (provide_sample_product) to aquire the name of the model we want (in this case, Product), create one sample object from it,
and then save it as a record.<br>
The first arg is the django's <b>apps</b> registry which keeps track of all your apps.<br>
The second one is <b>shema_editor</b>, which is used to manually effect database schema changes.<br>
(You should NOT manually use shema_editor, (according to ducmentation) django's migration autodetector does not like it.)

Ok, now if you run the migrations and check the database, you should see one record that exists in our Product table.
(the table is named shop_product)


### 2. Using Fixtures:

Data can aslo be provided using fixtures, but not automatically.
fixture is a collection of data that can be imported into database. usually by <b>python manage.py dumpdata</b> command.<br>

They can be written as JSON, YAML, XML files.<br>

#### <b>2.1. </b> I will initially use JSON for this example.

- Create a <b>fixtures</b> directory inside your app.
- I added the [sample_product.json](shop/fixtures/sample_product.json) file to it (feel free to take a look).<br>
(The primary key i used for the sample record is 2, since my first record was provided using data migration)<br>
- Then call the <b>loaddata</b> command and provide the fixture file name:
```
> python manage.py loaddata sample_product.json
```

Django will look into the <b>fixtures directory of each app</b>, and if fixture file is found, will insert the content of it into database.

#### <b>2.2. </b>You can also use relative paths (relative to your app).<br>
I used this approach and YAML file to insert the third record (Sample3)
- To use YAML file you need to install pyYAML:
```
> pip install pyYAML
```
- Then after adding the [yaml file](shop/data/sample_product.yaml) to a custom path (i named my folder data), run the loaddata command:
```
> python manage.py shop/data/sample_product.yaml
```

(for some reason '.yml' resulted in error: `yml is not a known serialization format.` '.yaml' was ok.)

#### <b>2.3. </b> Djagno will also look into a directory defined in a list of directories in FIXTURE_DIRS config var (in settings.py).<br>
I used this approach and a [xml file](fixtures/sample_product.xml) to insert the Sample4 record.<br>
- First create a folder named 'fixtures' in top level project directory (next to manage.py).<br>
Put your fixture file inside it <u>(No sub-directory with app name required.)</u>.
- Then add `FIXTURE_DIRS = [ BASE_DIR / "fixtures" ]` to settings.py
- Then run:
```
> python manage.py loaddata sample_product.xml
```
- Check the database, if everything went fine, you should see the Sample4 record.


#### Summary:
- Sample -> was provided using <b>data migration</b> (RunPython)
- Sample2 -> was provided using <b>fixture and json format</b> (fixtures folder in app folder)
- Sample3 -> was provided using <b>fixture and yml format</b> (relative custom location)
- Sample4 -> was provided using <b>top-level fixtures directory and xml format</b> (FIXTURE_DIRS)
