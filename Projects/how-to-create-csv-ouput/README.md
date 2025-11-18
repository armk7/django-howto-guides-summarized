## How to create CSV output

To output CSV using django, you can use either python csv library or django template system.

### 1. Using Python CSV library
Python's standard library comes with a csv module that allows for working with csv files.

- First, set up an app and basic urls.

- Then we add a view to return an CSV file as response (index view)

Notable points:
- In index view, we create a django <b>HttpResponse</b> object, first arg (<b>content_type</b>) is set to '<b>text/csv</b>'.<br>
content_type (or Content-Type) is a http header indicating the nature/format of the document provided by current URL.<br>
Its value is set as a standard identifier known as <b>MIME type</b> (or media type).<br>
text/csv is an example of a MIME type.

- Another header used here is <b>Content-Disposition</b>.<br>
Tells the browser how to proceed with the content of the response.<br>
Whether to simply display it (default for most), or prompt the user to download it.<br>
Setting it to'<b>attachment</b>' indicates that this file should be downloaded.


- The <b>writer()</b> function from python's csv module expects a file-like object.<br>
It can be any file-like object that implements the <b>write()</b> method.<br>
Python's <b>io</b> module uses this method to write data into an object (usually into a file, buffer or stream).<br>
Django's <b>HttpResponse</b> class implements write(), so we pass our response to it.

- The <b>writerow.writer()</b> function object accepts a row (An iterable of strings/numbers).

- If the content you're writing into the file contains characters such as quote or double quotes, there is no need for manually escaping them. (Notice the last item in the second row: Here's a quote.)

### 2. Large CSV outputs
In case of large csv outputs, it is recommended to ues StreamingHttpResponse.
This is to avoid load balancers dropping a timed-out connection when server was trying to generate the response.

- I added another view to for this (stream_csv)
- The client will receive the file chunk by chunk and write them into the disk (as a temp file at first) in the correct order.

### 3. Using django's template system
This approach will pass a list of items to template and iterate over it to add commas.
