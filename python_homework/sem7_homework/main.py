from format_txt import read as import_txt
from format_txt import write as export_txt
from format_csv import read as import_csv
from format_csv import write as export_csv
from format_html import write as export_html

book = import_txt('phonebook1')
export_csv('phonebook1', book)
book = import_csv('phonebook1')
export_txt('phonebook2', book)
export_html('phonebook1', book)


for rec in book:
    print(rec)