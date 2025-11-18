import csv
from django.shortcuts import render
from django.template import loader
from django.http.request import HttpRequest
from django.http.response import HttpResponse, StreamingHttpResponse

# Create your views here.


def index(request):
    return render(request, "home/index.html", {})


def download_csv(request: HttpRequest) -> HttpResponse:
    """Regular CSV file output"""

    response = HttpResponse(
        content_type = 'text/csv',
        headers = {'Content-Disposition': "attachment; filename=my_csv_file.csv"},
    )

    writer = csv.writer(response)
    writer.writerow(["First row", "Foo", "Bar", "Baz"])
    writer.writerow(["Second row", "A", "B", "C", '"Testing"', "Here's a quote"])

    return response


class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def stream_csv(request: HttpRequest) -> HttpResponse:
    """Stream large CSV ouput by generating sequences of rows."""

    rows = (["Row {}".format(idx, str(idx))] for idx in range(65536))
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    return StreamingHttpResponse(
        (writer.writerow(row) for row in rows),
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="somefilename.csv"'},
    )


def template_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="somefilename.csv"'},
    )

    # The data is hard-coded here, but you could load it from a database or
    # some other source.
    csv_data = (
        ("First row", "Foo", "Bar", "Baz"),
        ("Second row", "A", "B", "C", '"Testing"', "Here's a quote"),
    )

    t = loader.get_template("home/csv.txt")
    c = {"data": csv_data}
    response.write(t.render(c))
    return response


def template_csv_improved(request):
    data = [
        {'name': "Some Guy", 'age': 30},
        {'name': "Another Guy", 'age': 46}
    ]

    csv_content = loader.render_to_string("home/data.csv", {"data": data})

    response = HttpResponse(csv_content, content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    return response